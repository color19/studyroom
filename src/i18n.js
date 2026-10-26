(function(){
var LK='studyroom-lang',lang;
try{lang=localStorage.getItem(LK)}catch(e){}
if(lang!=='en'&&lang!=='zh')lang=/^zh/i.test(navigator.language||'')?'zh':'en';
var D=window.I18N_D||{},EX={},NM={},RX=[],MISS=window.__miss=new Set();
var NUMS='\\d+(?:[.,:]\\d+)*',NUM=new RegExp(NUMS,'g'),CJK=/[\u3400-\u9fff\u3002\uff0c\uff1a\uff1b\uff08\uff09]/;
function esc(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}
Object.keys(D).forEach(function(k){
  if(k.indexOf('{s}')>=0){var parts=k.split(/(\{[ns]\})/),re='^',lit=0;
    parts.forEach(function(p){if(p==='{n}')re+='('+NUMS+')';else if(p==='{s}')re+='(.+?)';else{re+=esc(p);lit+=p.length}});
    RX.push({re:new RegExp(re+'$'),v:D[k],lit:lit})}
  else if(k.indexOf('{n}')>=0)NM[k]=D[k];else EX[k]=D[k]});
RX.sort(function(a,b){return b.lit-a.lit});
var MON=['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],WD={'一':'Mon','二':'Tue','三':'Wed','四':'Thu','五':'Fri','六':'Sat','日':'Sun','天':'Sun'};
function fill(v,caps){var i=0;return v.replace(/\{(\d|n|s)\}/g,function(m,g){var c=/\d/.test(g)?caps[+g]:caps[i++];return c==null?'':c})}
function core(k,depth){
  if(EX.hasOwnProperty(k))return EX[k];
  var t=k.replace(NUM,'{n}');if(NM.hasOwnProperty(t))return fill(NM[t],k.match(NUM)||[]);
  if(depth<3)for(var i=0;i<RX.length;i++){var m=k.match(RX[i].re);if(m){var caps=m.slice(1).map(function(c){if(!CJK.test(c))return c;var r=core(c.trim(),depth+1);return r==null?c:r});var out=fill(RX[i].v,caps);if(out!==k)return out}}
  return null}
function tr(s){
  if(!s||!CJK.test(s))return null;
  var k=s.replace(/\s+/g,' ').trim();if(!k)return null;
  var lead=s.match(/^\s*/)[0],tail=s.match(/\s*$/)[0];
  var r=core(k,0);
  if(r==null){var k2=k.replace(/(\d{1,2})月(\d{1,2})日\s*(?:星期|周)([一二三四五六日天])/g,function(m,a,b,d){return WD[d]+', '+MON[+a]+' '+b}).replace(/星期([一二三四五六日天])/g,function(m,d){return WD[d]}).replace(/周([一二三四五六日])(?![一-鿿])/g,function(m,d){return WD[d]}).replace(/(\d{1,2})月(\d{1,2})日/g,function(m,a,b){return MON[+a]+' '+b});
    if(k2!==k){r=CJK.test(k2)?core(k2,0):k2}}
  if(r==null){MISS.add(k.replace(NUM,'{n}'));return null}
  return lead+r+tail}
window.__tr=tr;
var ATTR=['placeholder','title','aria-label'];
function skip(el){for(;el&&el.nodeType===1;el=el.parentNode){if(el.hasAttribute('data-noi18n'))return true;var n=el.nodeName;if(n==='SCRIPT'||n==='STYLE'||n==='TEXTAREA'||n==='CODE')return true}return false}
function attrs(el){for(var a=0;a<ATTR.length;a++){var v=el.getAttribute(ATTR[a]);if(v){var r=tr(v);if(r!=null&&r!==v)el.setAttribute(ATTR[a],r)}}}
function doNode(n){
  if(n.nodeType===3){if(skip(n.parentNode))return;var r=tr(n.nodeValue);if(r!=null&&r!==n.nodeValue)n.nodeValue=r;return}
  if(n.nodeType!==1)return;if(n.nodeName==='TEXTAREA'){attrs(n);return}if(skip(n))return;attrs(n);
  var w=document.createTreeWalker(n,NodeFilter.SHOW_TEXT|NodeFilter.SHOW_ELEMENT,{acceptNode:function(c){if(c.nodeName==='TEXTAREA'){attrs(c);return NodeFilter.FILTER_REJECT}return c.nodeType===1&&(c.nodeName==='SCRIPT'||c.nodeName==='STYLE'||c.hasAttribute('data-noi18n'))?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}}),c;
  while((c=w.nextNode())){if(c.nodeType===3){var r4=tr(c.nodeValue);if(r4!=null&&r4!==c.nodeValue)c.nodeValue=r4}else attrs(c)}}
window.I18N={lang:lang,set:function(l){try{localStorage.setItem(LK,l)}catch(e){}location.reload()},t:function(s){return lang==='en'?(tr(s)||s):s}};
function setLang(){if(document.documentElement)document.documentElement.lang=lang==='en'?'en':'zh-CN'}setLang();
if(lang!=='en')return;
['alert','confirm','prompt'].forEach(function(f){var o=window[f];window[f]=function(m){var a=[].slice.call(arguments);if(typeof m==='string')a[0]=tr(m)||m;return o.apply(window,a)}});
function start(){setLang();doNode(document.body);var rt=tr(document.title);if(rt)document.title=rt;
  new MutationObserver(function(ms){for(var i=0;i<ms.length;i++){var m=ms[i];
    if(m.type==='childList'){for(var j=0;j<m.addedNodes.length;j++)doNode(m.addedNodes[j])}else doNode(m.target)}
    var tt=tr(document.title);if(tt&&tt!==document.title)document.title=tt})
  .observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:ATTR});}
if(document.body)start();else document.addEventListener('DOMContentLoaded',start);
})();
