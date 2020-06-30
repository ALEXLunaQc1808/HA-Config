!function(e){var t={};function o(r){if(t[r])return t[r].exports;var n=t[r]={i:r,l:!1,exports:{}};return e[r].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=t,o.d=function(e,t,r){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(o.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)o.d(r,n,function(t){return e[t]}.bind(null,n));return r},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="",o(o.s=1)}([function(e){e.exports=JSON.parse('{"name":"hui-element","private":true,"version":"1.0.1","description":"","scripts":{"build":"webpack","watch":"webpack --watch --mode=development","update-card-tools":"npm uninstall card-tools && npm install thomasloven/lovelace-card-tools"},"repository":{"type":"git","url":"github.com:thomasloven/lovelace-hui-element"},"keywords":[],"author":"Thomas Lovén","license":"MIT","devDependencies":{"webpack":"^4.42.1","webpack-cli":"^3.3.11"},"dependencies":{"card-tools":"github:thomasloven/lovelace-card-tools"}}')},function(e,t,o){"use strict";o.r(t);const r=customElements.get("home-assistant-main")?Object.getPrototypeOf(customElements.get("home-assistant-main")):Object.getPrototypeOf(customElements.get("hui-view")),n=r.prototype.html;r.prototype.css;function i(){if(customElements.get("hui-view"))return!0;const e=document.createElement("partial-panel-resolver");if(e.hass=document.querySelector("hc-main")?document.querySelector("hc-main").hass:document.querySelector("home-assistant")?document.querySelector("home-assistant").hass:void 0,!e.hass||!e.hass.panels)return!1;e.route={path:"/lovelace/"},e._updateRoutes();try{document.querySelector("home-assistant").appendChild(e)}catch(e){}finally{document.querySelector("home-assistant").removeChild(e)}return!!customElements.get("hui-view")}function l(e,t,o=null){if((e=new Event(e,{bubbles:!0,cancelable:!1,composed:!0})).detail=t||{},o)o.dispatchEvent(e);else{var r=function(){var e=document.querySelector("hc-main");return e=e?(e=(e=(e=e&&e.shadowRoot)&&e.querySelector("hc-lovelace"))&&e.shadowRoot)&&e.querySelector("hui-view")||e.querySelector("hui-panel-view"):(e=(e=(e=(e=(e=(e=(e=(e=(e=(e=(e=document.querySelector("home-assistant"))&&e.shadowRoot)&&e.querySelector("home-assistant-main"))&&e.shadowRoot)&&e.querySelector("app-drawer-layout partial-panel-resolver"))&&e.shadowRoot||e)&&e.querySelector("ha-panel-lovelace"))&&e.shadowRoot)&&e.querySelector("hui-root"))&&e.shadowRoot)&&e.querySelector("ha-app-layout #view"))&&e.firstElementChild}();r&&r.dispatchEvent(e)}}let s=window.cardHelpers;const a=new Promise(async(e,t)=>{s&&e();const o=async()=>{s=await window.loadCardHelpers(),window.cardHelpers=s,e()};window.loadCardHelpers?o():window.addEventListener("load",async()=>{i(),window.loadCardHelpers&&o()})});function c(e,t){const o={type:"error",error:e,origConfig:t},r=document.createElement("hui-error-card");return customElements.whenDefined("hui-error-card").then(()=>{const e=document.createElement("hui-error-card");e.setConfig(o),r.parentElement&&r.parentElement.replaceChild(e,r)}),a.then(()=>{l("ll-rebuild",{},r)}),r}function u(e,t){if(!t||"object"!=typeof t||!t.type)return c(`No ${e} type configured`,t);let o=t.type;if(o=o.startsWith("custom:")?o.substr("custom:".length):`hui-${o}-${e}`,customElements.get(o))return function(e,t){let o=document.createElement(e);try{o.setConfig(JSON.parse(JSON.stringify(t)))}catch(e){o=c(e,t)}return a.then(()=>{l("ll-rebuild",{},o)}),o}(o,t);const r=c(`Custom element doesn't exist: ${o}.`,t);r.style.display="None";const n=setTimeout(()=>{r.style.display=""},2e3);return customElements.whenDefined(o).then(()=>{clearTimeout(n),l("ll-rebuild",{},r)}),r}function d(e){return s?s.createCardElement(e):u("card",e)}class p extends r{setConfig(e){const t=JSON.parse(JSON.stringify(e));let o;if(void 0!==t.card_type&&(o="card"),void 0!==t.element_type){if(void 0!==o)return void(this.element=d({type:"error",error:"Must specify only one of card_type, element_type or row_type.",origConfig:t}));o="element"}if(void 0!==t.row_type){if(void 0!==o)return void(this.element=d({type:"error",error:"Must specify only one of card_type, element_type or row_type.",origConfig:t}));o="row"}switch(o){case"card":t.type=t.card_type,delete t.card_type,this.element=d(t);break;case"element":t.type=t.element_type,delete t.element_type,this.element=function(e){return s?s.createHuiElement(e):u("element",e)}(t);break;case"row":t.type=t.row_type,"default"===t.type&&(t.type=void 0),delete t.row_type,this.element=function(e){if(s)return s.createRowElement(e);const t=new Set(["call-service","cast","conditional","divider","section","select","weblink"]),o={alert:"toggle",automation:"toggle",climate:"climate",cover:"cover",fan:"toggle",group:"group",input_boolean:"toggle",input_number:"input-number",input_select:"input-select",input_text:"input-text",light:"toggle",lock:"lock",media_player:"media-player",remote:"toggle",scene:"scene",script:"script",sensor:"sensor",timer:"timer",switch:"toggle",vacuum:"toggle",water_heater:"climate",input_datetime:"input-datetime",none:void 0};if(!e)return c("Invalid configuration given.",e);if("string"==typeof e&&(e={entity:e}),"object"!=typeof e||!e.entity&&!e.type)return c("Invalid configuration given.",e);const r=e.type||"default";return t.has(r)||r.startsWith("custom:")?u("row",e):u("entity-row",{type:o[e.entity?e.entity.split(".",1)[0]:"none"]||"text",...e})}(t);break;default:this.element=d({type:"error",error:"Must specify card_type, element_type or row_type.",origConfig:t})}}set hass(e){this.element.hass=e}createRenderRoot(){return this}get shadowRoot(){return this.element.shadowRoot}render(){return n`${this.element}`}}if(!customElements.get("hui-element")){customElements.define("hui-element",p);const e=o(0);console.info(`%cHUI-ELEMENT ${e.version} IS INSTALLED`,"color: green; font-weight: bold","")}}]);