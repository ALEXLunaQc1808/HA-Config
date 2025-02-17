"""Support for recurring_ical_events parser."""
from datetime import date, datetime, timedelta
from typing import Optional, Union

import recurring_ical_events as rie
from homeassistant.components.calendar import CalendarEvent
from icalendar import Calendar

from ..icalendarparser import ICalendarParser


class ParserRIE(ICalendarParser):
    """Provide parser using recurring_ical_events."""

    def __init__(self):
        """Construct ParserRIE."""
        self._calendar = None
        self.oneday = timedelta(days=1)
        self.oneday2 = timedelta(hours=23, minutes=59, seconds=59)

    def set_content(self, content: str):
        """Parse content into a calendar object.

        This must be called at least once before get_event_list or
        get_current_event.
        :param content is the calendar data
        :type content str
        """
        self._calendar = Calendar.from_ical(content)

    def get_event_list(
        self, start: datetime, end: datetime, include_all_day: bool
    ) -> list[CalendarEvent]:
        """Get a list of events.

        Gets the events from start to end, including or excluding all day
        events.
        :param start the earliest start time of events to return
        :type datetime
        :param end the latest start time of events to return
        :type datetime
        :param include_all_day if true, all day events will be included.
        :type boolean
        :returns a list of events, or an empty list
        :rtype list[CalendarEvent]
        """
        event_list = []

        if self._calendar is not None:
            for event in rie.of(self._calendar).between(start, end):
                start, end, all_day = self.is_all_day(event)

                if all_day and not include_all_day:
                    continue

                calendar_event = CalendarEvent(
                    summary=event.get("SUMMARY"),
                    start=start,
                    end=end,
                    location=event.get("LOCATION"),
                    description=event.get("DESCRIPTION"),
                )
                event_list.append(calendar_event)

        return event_list

    def get_current_event(
        self, include_all_day: bool, now: datetime, days: int
    ) -> Optional[CalendarEvent]:
        """Get the current or next event.

        Gets the current event, or the next upcoming event with in the
        specified number of days, if there is no current event.
        :param include_all_day if true, all day events will be included.
        :type boolean
        :param now the current date and time
        :type datetime
        :param days the number of days to check for an upcoming event
        :type int
        :returns a CalendarEvent or None
        """
        if self._calendar is None:
            return None

        temp_event = temp_start = temp_end = None
        end = now + timedelta(days=days)
        for event in rie.of(self._calendar).between(now, end):
            start, end, all_day = self.is_all_day(event)

            if all_day and not include_all_day:
                continue

            if ParserRIE.is_event_newer(temp_end, temp_start, end, start):
                temp_event = event
                temp_start = start
                temp_end = end

        if temp_event is None:
            return None

        return CalendarEvent(
            summary=temp_event.get("SUMMARY"),
            start=temp_start,
            end=temp_end,
            location=temp_event.get("LOCATION"),
            description=temp_event.get("DESCRIPTION"),
        )

    @staticmethod
    def is_event_newer(end2, start2, end, start) -> bool:
        """Determine if end2 and start2 are newer than end and start."""
        return start2 is None or (end2 > end and start <= start2)

    @staticmethod
    def get_date(date_time) -> Union[datetime, date]:
        """Get datetime with timezone information.

        If a date object is passed, it will first have a time component added,
        set to 0.
        :param date_time The date or datetime object
        :type date_time datetime or date
        :type: bool
        :returns The datetime.
        :rtype datetime
        """
        # Must use type here, since a datetime is also a date!
        if type(date_time) == date:  # pylint: disable=C0123
            date_time = datetime.combine(date_time, datetime.min.time())
        return date_time.astimezone()

    def is_all_day(self, event):
        """Determine if the event is an all day event.

        Return all day status and start and end times for the event.
        :param event The event to examine
        """
        start = ParserRIE.get_date(event.get("DTSTART").dt)
        end = ParserRIE.get_date(event.get("DTEND").dt)
        all_day = False
        diff = event.get("DURATION")
        if diff is not None:
            diff = diff.dt
        else:
            diff = end - start
        if diff in {self.oneday, self.oneday2} and all(
            x == 0 for x in [start.hour, start.minute, start.second]
        ):
            # if all_day, start and end must be date, not datetime!
            start = start.date()
            end = end.date()
            all_day = True

        return start, end, all_day
