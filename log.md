default	10:22:31.822757-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:22:31.822926-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:22:31.824604-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:22:31.833079-0400	runningboardd	Launch request for app<application.com.nexy.assistant.19062835.19062841(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	10:22:31.833177-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.19062835.19062841(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17058] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17058-463177 target:app<application.com.nexy.assistant.19062835.19062841(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:22:31.833265-0400	runningboardd	Assertion 398-17058-463177 (target:app<application.com.nexy.assistant.19062835.19062841(501)>) will be created as active
default	10:22:31.836368-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	10:22:31.836396-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.19062835.19062841(501)>
default	10:22:31.836407-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	10:22:31.836467-0400	runningboardd	app<application.com.nexy.assistant.19062835.19062841(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	10:22:31.840306-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	10:22:31.865014-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] is not RunningBoard jetsam managed.
default	10:22:31.865029-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] This process will not be managed.
default	10:22:31.865041-0400	runningboardd	Now tracking process: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:22:31.865197-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:31.865900-0400	gamepolicyd	Hit the server for a process handle 1c45a45f0001340c that resolved to: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:22:31.865936-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:31.868685-0400	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:22:31.868752-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-463178 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:31.868871-0400	runningboardd	Assertion 398-398-463178 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:31.869060-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:31.869077-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:31.869095-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: UserInteractive
default	10:22:31.869108-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:31.869138-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:31.869235-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] reported to RB as running
default	10:22:31.871156-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:78860" ID:398-363-463179 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:22:31.871490-0400	runningboardd	Assertion 398-363-463179 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:31.871557-0400	CoreServicesUIAgent	LAUNCH: 0x0-0xa00a00 com.nexy.assistant starting stopped process.
default	10:22:31.872782-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:31.872834-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:31.872857-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:31.872930-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:31.873132-0400	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:22:31.873672-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:22:31.874882-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:22:31.876991-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:31.877218-0400	runningboardd	Invalidating assertion 398-17058-463177 (target:app<application.com.nexy.assistant.19062835.19062841(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17058]
default	10:22:31.877265-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:31.877307-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:31.877342-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:31.877405-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:31.877557-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:31.881061-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:31.981921-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:31.981941-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:31.981951-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:31.981987-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:31.982228-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:31.985560-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:32.171017-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=511.78, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	10:22:32.598510-0400	Nexy	[0x1020556b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	10:22:32.598607-0400	Nexy	[0x1020557f0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	10:22:32.765115-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xc82aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:22:32.765377-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xc82aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:22:32.765594-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xc82aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:22:32.765805-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xc82aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	10:22:32.874758-0400	Nexy	[0x10205f780] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	10:22:32.885843-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:22:32.886051-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:22:32.886213-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	10:22:32.886225-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	10:22:32.886261-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:22:32.886492-0400	Nexy	[0xc839d4000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	10:22:32.886615-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	10:22:32.894515-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.1, subject=com.nexy.assistant,
default	10:22:32.895315-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:32.906753-0400	Nexy	[0xc839d4000] invalidated after the last release of the connection object
default	10:22:32.906805-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:22:32.910490-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3854, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:32.941086-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	10:22:32.941236-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc82ab20e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	10:22:32.974694-0400	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	10:22:32.976422-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:22:32.976566-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:22:35.340037-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D63E44D5-5A56-4219-9DE9-66811A65AF62 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55098,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x04fb66e0 tp_proto=0x06"
default	10:22:35.340142-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55098<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464678 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x89b135b2
default	10:22:35.355830-0400	kernel	tcp connected: [<IPv4-redacted>:55098<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464678 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x89b135b2
default	10:22:35.356357-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55098<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464678 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.017 sec Conn_Time: 0.016 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 16.000 ms rttvar: 8.000 ms base rtt: 16 ms so_error: 0 svc/tc: 0 flow: 0x89b135b2
default	10:22:35.356375-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55098<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464678 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:22:35.389098-0400	Nexy	[0xc839d4000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	10:22:35.403887-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc821e7840) Selecting device 85 from constructor
default	10:22:35.403898-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:35.403906-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:35.403911-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc821e7840) nothing to teardown
default	10:22:35.403913-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 85
default	10:22:35.404045-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 85 (Input:No | Output:Yes): true
default	10:22:35.404160-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xa for device 85
default	10:22:35.404267-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 85
default	10:22:35.404438-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 85
default	10:22:35.404447-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:35.404515-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:35.404524-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:22:35.404539-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:35.404546-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:22:35.404556-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:35.404642-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:35.404653-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:35.404658-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:35.404661-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device listeners from device 0
default	10:22:35.404665-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 0
default	10:22:35.404670-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:35.404687-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:22:35.404786-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc821e7840) caller requesting device change from 85 to 91
default	10:22:35.404794-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:35.404798-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:35.404803-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc821e7840) disconnecting device 85
default	10:22:35.404805-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc821e7840) destroying ioproc 0xa for device 85
default	10:22:35.404864-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	10:22:35.406249-0400	Nexy	[0xc839d4280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	10:22:35.408222-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"PID":78860,"session_type":"Primary"} }
default	10:22:35.408308-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:22:35.409064-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 78860, name = Nexy
default	10:22:35.409339-0400	Nexy	    SessionCore_Create.mm:99    Created session 0xc82aae680 with ID: 0x1ef0b4
default	10:22:35.410880-0400	Nexy	[0xc839d43c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	10:22:35.411032-0400	Nexy	No persisted cache on this platform.
error	10:22:35.411706-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=338701120962561 }
default	10:22:35.411722-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	10:22:35.411777-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:22:35.411868-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 91
default	10:22:35.411966-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 91 (Input:Yes | Output:No): true
default	10:22:35.413347-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3857, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:35.414494-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3857, subject=com.nexy.assistant,
default	10:22:35.415098-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:35.428394-0400	tccd	AUTHREQ_PROMPTING: msgID=401.3857, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	10:22:36.878767-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	10:22:36.879966-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xa for device 91
default	10:22:36.880198-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 91
default	10:22:36.880255-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	10:22:36.880471-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 91
default	10:22:36.880486-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:36.880501-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:22:36.880517-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:36.880713-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:22:36.880726-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:22:36.880733-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:22:36.880862-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:36.880880-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:36.880887-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:36.880901-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 7 device listeners from device 85
default	10:22:36.881119-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 85
default	10:22:36.881130-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:36.882025-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:22:36.883590-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3858, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:36.884767-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3858, subject=com.nexy.assistant,
default	10:22:36.886578-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:36.903434-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:22:36.904625-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3859, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:36.905690-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3859, subject=com.nexy.assistant,
default	10:22:36.906326-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:36.919327-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	10:22:36.921224-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3860, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:36.922194-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3860, subject=com.nexy.assistant,
default	10:22:36.922851-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:36.934140-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:22:36.934568-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:22:36.934704-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:22:36.934703-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:22:36.936141-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:22:36.937005-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	10:22:36.938005-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d9200] Created node ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:22:36.938066-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d9200] Created node ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:22:37.019545-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:22:37.021158-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26806 called from <private>
default	10:22:37.021202-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:22:37.021229-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:22:37.026582-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463194 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:37.026695-0400	runningboardd	Assertion 398-334-463194 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:37.021982-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26806 called from <private>
default	10:22:37.022104-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26806)
default	10:22:37.022119-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26806 called from <private>
default	10:22:37.022125-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26806 called from <private>
default	10:22:37.022830-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26805)
default	10:22:37.022927-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26805 called from <private>
default	10:22:37.022973-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26805 called from <private>
default	10:22:37.031610-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:22:37.032363-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:22:37.035157-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26806)
default	10:22:37.035176-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26806)
default	10:22:37.035186-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26806)
default	10:22:37.035190-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26806 called from <private>
default	10:22:37.035196-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26806)
default	10:22:37.035200-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26806 called from <private>
fault	10:22:37.031869-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19062835.19062841 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19062835.19062841>
default	10:22:37.035207-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:26806 called from <private>
default	10:22:37.035234-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:26806 called from <private>
default	10:22:37.035275-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26806 called from <private>
default	10:22:37.035326-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26806 called from <private>
default	10:22:37.043467-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:22:37.043546-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:22:37.043595-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:37.044261-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b4, Nexy(78860), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:22:37.044486-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:37.044589-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:37.035382-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26806 called from <private>
default	10:22:37.035418-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26806 called from <private>
default	10:22:37.040920-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26806 called from <private>
default	10:22:37.044842-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:22:37.045016-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b4, Nexy(78860), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 181 starting recording
default	10:22:37.044632-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:37.046158-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:37.040927-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26806 called from <private>
default	10:22:37.042948-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26805)
default	10:22:37.043595-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26806)
default	10:22:37.046386-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:22:37.043868-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26806 called from <private>
default	10:22:37.046500-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:22:37.046664-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:22:37.046395-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:37.046708-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:22:37.046781-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:22:37.045531-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:37.046720-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:37.046776-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3861, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:37.049235-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3861, subject=com.nexy.assistant,
fault	10:22:37.049488-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19062835.19062841 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19062835.19062841>
default	10:22:37.050065-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:37.050698-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:37.050710-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:37.050745-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:37.050833-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:37.051625-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-463178 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860])
default	10:22:37.053179-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26805 called from <private>
default	10:22:37.053194-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26805 called from <private>
default	10:22:37.053293-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26805)
default	10:22:37.064208-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:37.064857-0400	runningboardd	Invalidating assertion 398-334-463194 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:22:37.070208-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26805)
default	10:22:37.070591-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26805 called from <private>
default	10:22:37.070621-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26805 called from <private>
default	10:22:37.070863-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26805 called from <private>
default	10:22:37.070873-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26805 called from <private>
default	10:22:37.070898-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26805 called from <private>
default	10:22:37.070911-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26805 called from <private>
default	10:22:37.070920-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26805 called from <private>
default	10:22:37.070928-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26805 called from <private>
default	10:22:37.071186-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:37.070934-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26805 called from <private>
default	10:22:37.070941-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26805 called from <private>
default	10:22:37.070970-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26805)
default	10:22:37.071050-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26805 called from <private>
default	10:22:37.071099-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26805 called from <private>
default	10:22:37.096813-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	10:22:37.097219-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.097234-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.097246-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.097254-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.097259-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.097265-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:37.108658-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:22:37.110317-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d9200] Created node ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:22:37.110379-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d9200] Created node ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:22:37.144095-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:22:37.147744-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26806 called from <private>
default	10:22:37.147800-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26806 called from <private>
default	10:22:37.147803-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463197 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:37.147875-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:22:37.147880-0400	runningboardd	Assertion 398-334-463197 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:37.149230-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26806 called from <private>
default	10:22:37.149594-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26806)
default	10:22:37.149617-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26806 called from <private>
default	10:22:37.149570-0400	runningboardd	Invalidating assertion 398-334-463197 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:22:37.149626-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26806 called from <private>
default	10:22:37.150373-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:22:37.150510-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:22:37.150876-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26806)
default	10:22:37.150896-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26806 called from <private>
default	10:22:37.150903-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26806 called from <private>
default	10:22:37.151074-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26806 called from <private>
default	10:22:37.152440-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3863, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:37.153379-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3863, subject=com.nexy.assistant,
default	10:22:37.153956-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:37.154649-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:22:37.154700-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:22:37.154742-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:37.154843-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:37.155554-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.155564-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.155574-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.155580-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.155616-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.155636-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:37.155862-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:22:37.168551-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463198 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:37.168616-0400	runningboardd	Assertion 398-334-463198 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:37.169567-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26806 called from <private>
default	10:22:37.177525-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:22:37.177558-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:22:37.177608-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:37.177930-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.177938-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.177948-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.177957-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.177963-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.177973-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:37.177987-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.178002-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.178011-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.178019-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:37.178047-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:37.178059-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:37.178215-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:22:37.258101-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:37.258124-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:37.258136-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:37.258164-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:37.261035-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:37.261490-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:38.194693-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:22:38.195209-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:22:38.195415-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:38.195518-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:22:38.195576-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:22:38.195661-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:22:38.195671-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b4, Nexy(78860), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 181 stopping recording
default	10:22:38.195718-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:22:38.195765-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:38.195820-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:38.196073-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:22:38.196074-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:22:38.196099-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:22:38.200474-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:38.200510-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:38.200532-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:22:38.200557-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:38.200164-0400	runningboardd	Invalidating assertion 398-334-463198 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:22:38.200648-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:22:38.200330-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:38.200664-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:38.200407-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:38.200710-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:22:38.204427-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:38.206588-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:38.206609-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:38.206635-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:38.206648-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:38.206660-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:38.206669-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:38.206983-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:22:38.297008-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc821e7840) Selecting device 0 from destructor
default	10:22:38.297034-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:38.297046-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:38.297058-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc821e7840) disconnecting device 91
default	10:22:38.297070-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc821e7840) destroying ioproc 0xa for device 91
default	10:22:38.297123-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:22:38.297178-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:22:38.297426-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc821e7840) nothing to setup
default	10:22:38.297447-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device listeners to device 0
default	10:22:38.297458-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 0
default	10:22:38.297471-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 7 device listeners from device 91
default	10:22:38.297867-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 91
default	10:22:38.297893-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:38.307301-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:38.307364-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:38.307383-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:38.307471-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:38.313958-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:22:38.314582-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:38.591443-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78862.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78862, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:22:38.593342-0400	tccd	AUTHREQ_SUBJECT: msgID=78862.1, subject=com.nexy.assistant,
default	10:22:38.594185-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:38.611543-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6397, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78862, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:22:38.612657-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6397, subject=com.nexy.assistant,
default	10:22:38.613392-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:38.646694-0400	launchservicesd	CHECKIN:0x0-0xa00a00 78862 com.nexy.assistant
default	10:22:38.647290-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:22:38.647432-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:22:38.648138-0400	runningboardd	Invalidating assertion 398-363-463179 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	10:22:38.655045-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:38.655893-0400	WindowServer	10f43b[CreateApplication]: Process creation: 0x0-0xa00a00 (Nexy) connectionID: 10F43B pid: 78862 in session 0x101
default	10:22:38.658617-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:22:38.752515-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:38.752526-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:38.752578-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: None
default	10:22:38.752592-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:38.752613-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:38.756429-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-suspended (role: None) (endowments: (null))
default	10:22:38.756875-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-suspended-NotVisible
default	10:22:38.837109-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 ab6b0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:22:38.855474-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:22:38.899712-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0xa00a00 (Nexy) connectionID: 10F43B pid: 78862 in session 0x101
default	10:22:38.899732-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0xa00a00 (Nexy) acq:0x800bd3480 count:1
default	10:22:38.899967-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0xa00a00 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa00a00 (Nexy)"
)}
default	10:22:38.900166-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1340e removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa00a00 (Nexy)"
)}
default	10:22:38.901787-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0xa00a00} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	10:22:38.901807-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 10488320
default	10:22:38.901843-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	10:22:39.058887-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc821e7840) Selecting device 85 from constructor
default	10:22:39.058897-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:39.058902-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:39.058907-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc821e7840) nothing to teardown
default	10:22:39.058909-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 85
default	10:22:39.059014-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 85 (Input:No | Output:Yes): true
default	10:22:39.059135-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xb for device 85
default	10:22:39.059289-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 85
default	10:22:39.059489-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 85
default	10:22:39.059499-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:39.059580-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	10:22:39.059587-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:22:39.059592-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	10:22:39.059600-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:22:39.059607-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:39.059709-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:39.059720-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:39.059725-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:39.059731-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device listeners from device 0
default	10:22:39.059734-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 0
default	10:22:39.059737-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:39.059755-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:22:39.059833-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc821e7840) caller requesting device change from 85 to 91
default	10:22:39.059840-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:39.059844-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:39.059849-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc821e7840) disconnecting device 85
default	10:22:39.059853-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc821e7840) destroying ioproc 0xb for device 85
default	10:22:39.059875-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	10:22:39.059907-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:22:39.059995-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 91
default	10:22:39.060080-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 91 (Input:Yes | Output:No): true
default	10:22:39.061544-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3864, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:39.062688-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3864, subject=com.nexy.assistant,
default	10:22:39.063316-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:39.075010-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xb for device 91
default	10:22:39.075129-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 91
default	10:22:39.075299-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 91
default	10:22:39.075306-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:39.075314-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:22:39.075323-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:39.075443-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:22:39.075452-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:22:39.075457-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:22:39.075551-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:39.075562-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:39.075567-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:39.075571-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 7 device listeners from device 85
default	10:22:39.075757-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 85
default	10:22:39.075767-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:39.076359-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:22:39.077357-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3865, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:39.078115-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3865, subject=com.nexy.assistant,
default	10:22:39.078670-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:39.090332-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	10:22:39.090456-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xc8455d9e0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	10:22:39.090682-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:22:39.091681-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3866, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:39.092525-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3866, subject=com.nexy.assistant,
default	10:22:39.093101-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:39.105920-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3867, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:22:39.106738-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3867, subject=com.nexy.assistant,
default	10:22:39.107295-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:22:39.122545-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:22:39.125828-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:22:39.125935-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:22:39.125967-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b4, Nexy(78860), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:22:39.125994-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:39.126082-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b4, Nexy(78860), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:22:39.126151-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.126270-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:39.126307-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:39.126395-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.126394-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:22:39.126435-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b4, Nexy(78860), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 181 starting recording
default	10:22:39.126434-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.126243-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463216 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:39.126415-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.126339-0400	runningboardd	Assertion 398-334-463216 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:39.126552-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.126601-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:39.127015-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:22:39.126693-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:22:39.126571-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:39.127024-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:22:39.126849-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:22:39.126861-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:39.127118-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:39.126998-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:22:39.127279-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:22:39.127198-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: Background
default	10:22:39.127243-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:39.127465-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:39.128432-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:39.128457-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:39.128357-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:39.128469-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	10:22:39.128478-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	10:22:39.128488-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	10:22:39.128530-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:22:39.135373-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: Background) (endowments: (null))
default	10:22:39.135853-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:39.140959-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:22:39.141032-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:22:39.141091-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:39.143156-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143173-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143192-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.143199-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143208-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.143230-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:39.143280-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143321-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143367-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.143394-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.143430-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.143466-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:39.143728-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:22:39.144558-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:22:39.144820-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.144831-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.144848-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.144855-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:39.144896-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:39.144932-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:40.095679-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	10:22:43.095614-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	10:22:46.095252-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	10:22:46.246854-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:22:46.247453-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:22:46.247692-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:46.247812-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:22:46.247884-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:22:46.248001-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:22:46.248023-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b4, Nexy(78860), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 181 stopping recording
default	10:22:46.248094-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:22:46.248171-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:46.248258-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:46.248511-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:22:46.248514-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:22:46.248557-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:22:46.253602-0400	runningboardd	Invalidating assertion 398-334-463216 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:22:46.254221-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:46.254281-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:46.254004-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:22:46.254316-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:22:46.254118-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:46.254362-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:46.254688-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:22:46.254844-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:46.254914-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:22:46.257611-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:22:46.261341-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:46.261356-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:46.261369-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:46.261378-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:22:46.261387-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:22:46.261394-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:22:46.261527-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:22:46.356872-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:46.356899-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:46.356966-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: None
default	10:22:46.356992-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:46.357065-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:46.365333-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-suspended (role: None) (endowments: (null))
default	10:22:46.365880-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-suspended-NotVisible
default	10:22:46.388744-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc821e7840) Selecting device 0 from destructor
default	10:22:46.388775-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:46.388791-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:46.388803-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc821e7840) disconnecting device 91
default	10:22:46.388818-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc821e7840) destroying ioproc 0xb for device 91
default	10:22:46.388873-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:22:46.388942-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:22:46.389249-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc821e7840) nothing to setup
default	10:22:46.389280-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device listeners to device 0
default	10:22:46.389297-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 0
default	10:22:46.389312-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 7 device listeners from device 91
default	10:22:46.389597-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 91
default	10:22:46.389612-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:46.406672-0400	Nexy	[0xc839d4500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:22:46.407808-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:46.410191-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.2, subject=com.nexy.assistant,
default	10:22:46.411223-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:46.427557-0400	Nexy	[0xc839d4500] invalidated after the last release of the connection object
default	10:22:46.429030-0400	Nexy	[0xc839d4500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:22:46.429738-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:46.430946-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.3, subject=com.nexy.assistant,
default	10:22:46.431569-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:46.443110-0400	Nexy	[0xc839d4500] invalidated after the last release of the connection object
default	10:22:46.443332-0400	Nexy	[0xc839d4500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:22:46.443819-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:46.445003-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.4, subject=com.nexy.assistant,
default	10:22:46.445899-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:46.457529-0400	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[78860], responsiblePID[78860], responsiblePath: /Applications/Nexy.app to UID: 501
default	10:22:46.457788-0400	Nexy	[0xc839d4500] invalidated after the last release of the connection object
default	10:22:46.536977-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	10:22:46.561791-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:22:46.564065-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:22:46.568694-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:22:46.577891-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:22:47.159658-0400	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	10:22:47.164159-0400	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:22:47.183320-0400	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	10:22:48.471631-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26805)
default	10:22:48.471755-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26805 called from <private>
default	10:22:48.471770-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26805 called from <private>
default	10:22:48.476387-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26806)
default	10:22:48.476423-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26806 called from <private>
default	10:22:48.476433-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26806 called from <private>
default	10:22:48.494019-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26806)
default	10:22:48.531039-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26805)
default	10:22:52.112026-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:22:52.126663-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	10:22:52.136406-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:22:53.606534-0400	Nexy	[0xc839d4640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	10:22:53.607572-0400	Nexy	[0xc839d48c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	10:22:53.614711-0400	Nexy	Received configuration update from daemon (initial)
default	10:22:53.660958-0400	Nexy	[0xc839d4a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:22:53.661609-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:22:53.661798-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:53.663170-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.5, subject=com.nexy.assistant,
default	10:22:53.663846-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	10:22:53.676069-0400	Nexy	[0xc839d4a00] invalidated after the last release of the connection object
default	10:22:53.676897-0400	Nexy	[0xc839d4a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:22:53.677270-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:22:53.677437-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:53.678273-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.6, subject=com.nexy.assistant,
default	10:22:53.678945-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	10:22:53.690221-0400	Nexy	[0xc839d4a00] invalidated after the last release of the connection object
default	10:22:53.690270-0400	Nexy	[0xc839d4a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	10:22:53.690362-0400	Nexy	[0xc839d4a00] invalidated after the last release of the connection object
default	10:22:53.690629-0400	Nexy	[0xc839d4b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:22:53.691075-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78860.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:22:53.691924-0400	tccd	AUTHREQ_SUBJECT: msgID=78860.7, subject=com.nexy.assistant,
default	10:22:53.692543-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	10:22:53.704139-0400	tccd	Notifying for access  kTCCServiceListenEvent for target PID[78860], responsiblePID[78860], responsiblePath: /Applications/Nexy.app to UID: 501
default	10:22:53.704348-0400	Nexy	[0xc839d4b40] invalidated after the last release of the connection object
default	10:22:53.704591-0400	Nexy	server port 0x0000b313, session port 0x0000610f
default	10:22:53.705513-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6417, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:22:53.705540-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:22:53.706351-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6417, subject=com.nexy.assistant,
default	10:22:53.707330-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	10:22:53.716607-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	10:22:53.736819-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:22:53.741239-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:22:53.748775-0400	Nexy	server port 0x0000610f, session port 0x0000610f
default	10:22:53.749834-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6418, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:22:53.749861-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78860, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:22:53.750541-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D58C2C10-D2E0-44D0-B7A9-DF2D00724871 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55099,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xbfa6aa4f tp_proto=0x06"
default	10:22:53.750667-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55099<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464724 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 15 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb9944b51
default	10:22:53.752083-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:22:53.752304-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:22:53.751545-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6418, subject=com.nexy.assistant,
default	10:22:53.753026-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:22:53.753119-0400	Nexy	nw_path_libinfo_path_check [298324FA-CBE7-4A00-8A24-AEAC50FDE6D3 IPv4#7a3696dc:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	10:22:53.754255-0400	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 06D497F9-1317-4238-8512-E2FAC1C49939 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55100,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x7145d883 tp_proto=0x06"
default	10:22:53.754318-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55100<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2464725 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9fca7dae
default	10:22:53.764750-0400	kernel	tcp connected: [<IPv4-redacted>:55099<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464724 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 15 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb9944b51
default	10:22:53.767596-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55099<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464724 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.017 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0xb9944b51
default	10:22:53.767612-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55099<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464724 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:22:53.770049-0400	Nexy	[0xc839d4b40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	10:22:53.770585-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0704FF08-2055-4F7B-95F5-E6228C3BFD33 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55101,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe6d7ebbc tp_proto=0x06"
default	10:22:53.770803-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55101<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464726 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x867058cc
default	10:22:53.777209-0400	kernel	tcp connected: [<IPv4-redacted>:55100<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2464725 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9fca7dae
default	10:22:53.778933-0400	Nexy	New connection 0x87887 main
default	10:22:53.779103-0400	Nexy	[0xc839d4c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	10:22:53.783480-0400	kernel	tcp connected: [<IPv4-redacted>:55101<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464726 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x867058cc
default	10:22:53.786484-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55101<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464726 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.016 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x867058cc
default	10:22:53.786497-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55101<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464726 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:22:53.788707-0400	Nexy	[0xc839d4f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	10:22:53.796792-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	10:22:53.804821-0400	Nexy	nw_path_libinfo_path_check [01C91DEA-9724-4F68-8B68-382A2CD03533 Hostname#012e106a:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	10:22:53.805006-0400	mDNSResponder	[R296113] DNSServiceCreateConnection START PID[78860](Nexy)
default	10:22:53.805067-0400	mDNSResponder	[R296114] DNSServiceQueryRecord START -- qname: <mask.hash: 'fzWYXTe2YMapr48UvSyQLQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78860 (Nexy), name hash: 93389144
default	10:22:53.805442-0400	mDNSResponder	[R296115] DNSServiceQueryRecord START -- qname: <mask.hash: 'fzWYXTe2YMapr48UvSyQLQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78860 (Nexy), name hash: 93389144
default	10:22:53.810218-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:22:53.813849-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:22:53.828341-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 7789EDC2-7AA6-4CBA-9AC9-B2D66391FFA4 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55102,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x2edaf872 tp_proto=0x06"
default	10:22:53.830143-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55102<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464738 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x983a751f
default	10:22:53.857841-0400	kernel	tcp connected: [<IPv4-redacted>:55102<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464738 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x983a751f
default	10:22:54.026293-0400	Nexy	nw_path_libinfo_path_check [3BC5DF09-2A56-4547-9708-15130C06F896 Hostname#4b84e09c:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	10:22:54.026413-0400	mDNSResponder	[R296116] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78860 (Nexy), name hash: c6742fa2
default	10:22:54.026982-0400	mDNSResponder	[R296117] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78860 (Nexy), name hash: c6742fa2
default	10:22:54.028085-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1713FA84-62CC-4244-A5CD-08C6C98665C0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55103,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x5f0df9a5 tp_proto=0x06"
default	10:22:54.028142-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55103<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464748 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x985175b9
default	10:22:54.043484-0400	kernel	tcp connected: [<IPv4-redacted>:55103<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464748 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x985175b9
default	10:22:55.262191-0400	kernel	udp connect: [<IPv4-redacted>:52286<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2464754 so_state: 0x0002 process: Nexy:78860 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb6f12fe3
default	10:22:55.262219-0400	kernel	udp_connection_summary [<IPv4-redacted>:52286<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2464754 so_state: 0x0002 process: Nexy:78860 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb6f12fe3 flowctl: 0us (0x)
default	10:22:55.263087-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DD6F12CE-5A54-4C3B-B523-C39375F1F6BE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55105,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0xc8960153 tp_proto=0x06"
default	10:22:55.263148-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55105<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2464756 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9642d8d2
default	10:22:55.286159-0400	kernel	tcp connected: [<IPv4-redacted>:55105<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2464756 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9642d8d2
default	10:22:56.919655-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc821e7840) Selecting device 85 from constructor
default	10:22:56.919675-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:56.919687-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:56.919692-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc821e7840) nothing to teardown
default	10:22:56.919697-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 85
default	10:22:56.919810-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 85 (Input:No | Output:Yes): true
default	10:22:56.920031-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xc for device 85
default	10:22:56.920178-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 85
default	10:22:56.920412-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 85
default	10:22:56.920423-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:56.920516-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:56.920527-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:22:56.920536-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:56.920542-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:22:56.920552-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:56.920677-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:56.920691-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:56.920698-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:56.920705-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device listeners from device 0
default	10:22:56.920711-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 0
default	10:22:56.920715-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:56.920727-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc821e7840) caller requesting device change from 85 to 85
default	10:22:56.920732-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:56.920738-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc821e7840) exiting with nothing to do
default	10:22:56.921356-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:22:56.921871-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:22:56.924362-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc821e7840) Selecting device 0 from destructor
default	10:22:56.924376-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:56.924382-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:56.924387-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc821e7840) disconnecting device 85
default	10:22:56.924393-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc821e7840) destroying ioproc 0xc for device 85
default	10:22:56.924464-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	10:22:56.924500-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:22:56.924637-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc821e7840) nothing to setup
default	10:22:56.924696-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device listeners to device 0
default	10:22:56.924706-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 0
default	10:22:56.924714-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 7 device listeners from device 85
default	10:22:56.924947-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 85
default	10:22:56.924978-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:56.927541-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc821e7840) Selecting device 85 from constructor
default	10:22:56.927577-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:56.927612-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc821e7840) not already running
default	10:22:56.927649-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc821e7840) nothing to teardown
default	10:22:56.927659-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc821e7840) connecting device 85
default	10:22:56.927807-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc821e7840) Device ID: 85 (Input:No | Output:Yes): true
default	10:22:56.927963-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc821e7840) created ioproc 0xd for device 85
default	10:22:56.928169-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 7 device listeners to device 85
default	10:22:56.928417-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc821e7840) adding 0 device delegate listeners to device 85
default	10:22:56.928430-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc821e7840)
default	10:22:56.928543-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:56.928554-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:22:56.928577-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:22:56.928607-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:22:56.928621-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:22:56.928759-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:22:56.928781-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc821e7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:22:56.928788-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:22:56.928796-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device listeners from device 0
default	10:22:56.928801-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc821e7840) removing 0 device delegate listeners from device 0
default	10:22:56.928806-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc821e7840)
default	10:22:56.928837-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc821e7840) caller requesting device change from 85 to 85
default	10:22:56.928843-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc821e7840)
default	10:22:56.928850-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc821e7840) exiting with nothing to do
default	10:22:56.928865-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	10:22:56.929399-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:22:56.929833-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:22:56.936398-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463288 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:22:56.936474-0400	runningboardd	Assertion 398-334-463288 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:22:56.936897-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:22:56.936920-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:22:56.936981-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: Background
default	10:22:56.936999-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:22:56.937036-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:22:56.940356-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: Background) (endowments: (null))
default	10:22:56.940742-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:22:57.336406-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	10:22:57.337503-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	10:22:57.337728-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:22:57.337791-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b4, Nexy(78860), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:22:57.337830-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:22:57.337898-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b4, Nexy(78860), 'prim'', AudioCategory changed to 'MediaPlayback'
default	10:22:57.337918-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.338121-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.337970-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	10:22:57.337981-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 starting playing
default	10:22:57.338166-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:22:57.338218-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:22:57.338254-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:22:57.338298-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	10:22:57.338330-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:22:57.338380-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b4 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:22:57.338176-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.338543-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:22:57.338727-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	10:22:57.338757-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:22:57.339952-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.340055-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.340087-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:22:57.340102-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	10:22:57.340112-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	10:22:57.340126-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	10:22:57.340197-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:22:58.097779-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:22:58.960613-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	10:22:58.980704-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:22:58.989948-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:23:01.097759-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
error	10:23:01.772037-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	10:23:04.095467-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:23:07.095896-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:23:10.094943-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:23:11.601350-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	10:23:11.602174-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:23:11.602298-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 stopping playing
default	10:23:11.602370-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:23:11.602428-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:23:11.602528-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:23:11.602654-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:23:11.602720-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b4 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:23:11.602881-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:23:11.602958-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:23:11.602967-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:23:11.602993-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:23:11.602986-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:23:11.607707-0400	runningboardd	Invalidating assertion 398-334-463288 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:23:11.713087-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:23:11.713102-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:23:11.713186-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: None
default	10:23:11.713200-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:23:11.713233-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:23:11.718185-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-suspended (role: None) (endowments: (null))
default	10:23:11.718782-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-suspended-NotVisible
default	10:23:23.790158-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 38BB1442-F674-4941-ACDA-6209DB215933 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55107,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x2f43b916 tp_proto=0x06"
default	10:23:23.790225-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55107<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464780 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a7e28bf
default	10:23:23.814122-0400	kernel	tcp connected: [<IPv4-redacted>:55107<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464780 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a7e28bf
default	10:23:23.814706-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55107<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464780 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.025 sec Conn_Time: 0.024 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 24.000 ms rttvar: 12.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9a7e28bf
default	10:23:23.814728-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55107<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464780 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:23:23.815195-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9AB5D0DD-0200-40A8-96B3-D572DCE2F667 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55108,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1df232e5 tp_proto=0x06"
default	10:23:23.815234-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55108<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464781 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87a6bd8e
default	10:23:23.828116-0400	kernel	tcp connected: [<IPv4-redacted>:55108<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464781 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87a6bd8e
default	10:23:23.828517-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55108<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464781 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.014 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x87a6bd8e
default	10:23:23.828541-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55108<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2464781 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:23:38.903637-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 10488320, name: Nexy with url: file:///Applications/Nexy.app/
default	10:23:38.904237-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	10:23:38.904261-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	10:23:38.904275-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
default	10:23:53.830845-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 7DCFFD45-5ED0-4468-A683-9DCA9A438953 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55120,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb17a0bd5 tp_proto=0x06"
default	10:23:53.830914-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55120<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465020 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1b209e3
default	10:23:53.844811-0400	kernel	tcp connected: [<IPv4-redacted>:55120<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465020 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1b209e3
default	10:23:53.845396-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55120<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465020 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xa1b209e3
default	10:23:53.845418-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55120<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465020 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:23:53.845877-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4056AE6A-6947-4CAF-926C-42CABDBDDB78 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55121,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf0ea10d3 tp_proto=0x06"
default	10:23:53.845917-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55121<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465021 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x813159b7
default	10:23:53.871095-0400	kernel	tcp connected: [<IPv4-redacted>:55121<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465021 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x813159b7
default	10:23:53.871721-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55121<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465021 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.026 sec Conn_Time: 0.025 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 25.000 ms rttvar: 12.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x813159b7
default	10:23:53.871747-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55121<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465021 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:23:54.634268-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463323 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:23:54.634442-0400	runningboardd	Assertion 398-334-463323 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:23:54.635929-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:23:54.636028-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:23:54.636270-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: Background
default	10:23:54.636349-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:23:54.636559-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:23:54.641922-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: Background) (endowments: (null))
default	10:23:54.642724-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:23:55.095510-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	10:23:55.096443-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	10:23:55.096622-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	10:23:55.096646-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 starting playing
default	10:23:55.096725-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:23:55.096781-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:23:55.096813-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:23:55.096859-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:23:55.096904-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b4 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:23:55.096966-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	10:23:55.096980-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:23:55.097156-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:23:55.098474-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:23:55.098592-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:23:55.098625-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:23:55.098644-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	10:23:55.098654-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	10:23:55.098668-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	10:23:55.098742-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:23:58.096148-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:24:01.096164-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:24:02.673069-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	10:24:02.673590-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:24:02.673752-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 stopping playing
default	10:24:02.673844-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:24:02.673927-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:24:02.674045-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:24:02.674180-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:24:02.674284-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b4 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:24:02.674463-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:24:02.674479-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:24:02.674563-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:24:02.674503-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:24:02.674607-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:24:02.680270-0400	runningboardd	Invalidating assertion 398-334-463323 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:24:02.783444-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:24:02.783462-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:24:02.783546-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: None
default	10:24:02.783564-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:24:02.783593-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:24:02.789190-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-suspended (role: None) (endowments: (null))
default	10:24:02.789830-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-suspended-NotVisible
default	10:24:23.873893-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 46C8402F-85C1-4DD1-93AE-2CCCB740F23E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55133,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x247873ce tp_proto=0x06"
default	10:24:23.873965-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55133<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465178 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86914872
default	10:24:23.887198-0400	kernel	tcp connected: [<IPv4-redacted>:55133<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465178 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86914872
default	10:24:23.887742-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55133<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465178 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x86914872
default	10:24:23.887763-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55133<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465178 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:24:23.888261-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 62B258F7-5FB8-4642-8B33-97CC85CE0A7B flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55134,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x68f606b0 tp_proto=0x06"
default	10:24:23.888317-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55134<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465179 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xab5e27b5
default	10:24:23.902635-0400	kernel	tcp connected: [<IPv4-redacted>:55134<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465179 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xab5e27b5
default	10:24:23.903229-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55134<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465179 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.015 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xab5e27b5
default	10:24:23.903254-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55134<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465179 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:24:53.905401-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FE1E7AB8-B2A0-4E3B-BB8C-542EECB35F52 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55145,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc8e9300d tp_proto=0x06"
default	10:24:53.905469-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55145<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465353 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8997653c
default	10:24:53.926400-0400	kernel	tcp connected: [<IPv4-redacted>:55145<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465353 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8997653c
default	10:24:53.927057-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55145<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465353 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.022 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x8997653c
default	10:24:53.927079-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55145<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465353 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:24:53.927591-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 579943CC-5C86-4CEC-A794-16E21E0816FE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55146,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb6003ca5 tp_proto=0x06"
default	10:24:53.927634-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55146<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465354 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d2ca873
default	10:24:53.946607-0400	kernel	tcp connected: [<IPv4-redacted>:55146<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465354 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d2ca873
default	10:24:53.947036-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55146<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465354 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.019 sec Conn_Time: 0.019 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.000 ms rttvar: 9.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9d2ca873
default	10:24:53.947056-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55146<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465354 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:19.960284-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19062835.19062841(501)>:78860] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463528 target:78860 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:19.960474-0400	runningboardd	Assertion 398-334-463528 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) will be created as active
default	10:25:19.961173-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring jetsam update because this process is not memory-managed
default	10:25:19.961199-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring suspend because this process is not lifecycle managed
default	10:25:19.961312-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Set darwin role to: Background
default	10:25:19.961345-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring GPU update because this process is not GPU managed
default	10:25:19.961390-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] Ignoring memory limit update because this process is not memory-managed
default	10:25:19.967413-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: running-active (role: Background) (endowments: (null))
default	10:25:19.968086-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, running-active-NotVisible
default	10:25:20.143482-0400	kernel	hfs: mounted Nexy on device disk4s1
default	10:25:20.203655-0400	com.apple.appkit.xpc.openAndSavePanelService	CacheDeleteCopyPurgeableSpaceWithInfo result for unknown!! : {
    "CACHE_DELETE_ERROR" = "Bad volume: /private/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_update_sj90rqfn";
}
default	10:25:20.214827-0400	storagekitd	CacheDeleteCopyPurgeableSpaceWithInfo result for unknown!! : {
    "CACHE_DELETE_ERROR" = "Bad volume: /private/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_update_sj90rqfn";
}
default	10:25:20.459673-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	10:25:20.460675-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	10:25:20.460840-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	10:25:20.460858-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 starting playing
default	10:25:20.460958-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:20.461004-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:20.461035-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b4, Nexy(78860), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:20.461091-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:20.461123-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b4 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78860}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b4, sessionType: 'prim', isRecording: false }, 
]
default	10:25:20.461270-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	10:25:20.461282-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:20.461419-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:20.462651-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:20.462759-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:20.462809-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:20.462824-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	10:25:20.462835-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	10:25:20.462848-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	10:25:20.462908-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:22.098325-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:23.949193-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DCA2CBA3-4F4E-4B27-ADFC-CBB1564CE81A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55151,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1aa379a1 tp_proto=0x06"
default	10:25:23.949338-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55151<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465473 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb04b3643
default	10:25:23.964494-0400	kernel	tcp connected: [<IPv4-redacted>:55151<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465473 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb04b3643
default	10:25:23.965356-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55151<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465473 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.017 sec Conn_Time: 0.016 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 16.000 ms rttvar: 8.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xb04b3643
default	10:25:23.965382-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55151<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465473 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:23.965852-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BF4E9CBA-2B5F-4744-B872-0FA72E50F380 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55152,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x237ee616 tp_proto=0x06"
default	10:25:23.965887-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55152<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465474 t_state: SYN_SENT process: Nexy:78860 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa592c21a
default	10:25:23.978343-0400	kernel	tcp connected: [<IPv4-redacted>:55152<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465474 t_state: ESTABLISHED process: Nexy:78860 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa592c21a
default	10:25:23.978893-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55152<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465474 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 0.013 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xa592c21a
default	10:25:23.978910-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55152<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465474 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
error	10:25:24.481493-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	10:25:24.494000-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.513485-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.528155-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.529045-0400	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	10:25:24.529766-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	10:25:24.541099-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.557163-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.572717-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.586056-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	10:25:24.593199-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:24.596967-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.610474-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.611475-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.624957-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.639590-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	10:25:24.646164-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:24.652133-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:24.666671-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	10:25:24.676717-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:24.711877-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	10:25:24.713350-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:25.097878-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:25.114092-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:25:25.114294-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:25:25.116561-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:25.127486-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
error	10:25:25.132838-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:25.133533-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:25:25.134008-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:25:25.137887-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:25.139849-0400	nehelper	Received an apps installed notification with bundle IDs (
    "com.nexy.assistant"
)
error	10:25:25.140265-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	10:25:25.162050-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:25:25.162190-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:25:25.163512-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:25.166419-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	10:25:25.172861-0400	kernel	hfs: unmount initiated on Nexy on device disk4s1
default	10:25:25.206304-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:25:25.206451-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:25:25.207833-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:25:25.211612-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	10:25:25.233748-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef0b4","name":"Nexy(78860)"}, "details":null }
default	10:25:25.233808-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef0b4 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":78860})
default	10:25:25.233822-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":78860})
default	10:25:25.234097-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 181 stopping playing
default	10:25:25.234159-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:25:25.234229-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:25.234431-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 181, PID = 78860, Name = sid:0x1ef0b4, Nexy(78860), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:25:25.235002-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.235048-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.234829-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.234930-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.239933-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.239965-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:25:25.240088-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:25.248727-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55105<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2464756 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 149.985 sec Conn_Time: 0.023 sec bytes in/out: 2526387/1312 pkts in/out: 400/23 pkt rxmit: 2 ooo pkts: 43 dup bytes in: 0 ACKs delayed: 182 delayed ACKs sent: 0
rtt: 51.906 ms rttvar: 37.437 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x9642d8d2
default	10:25:25.248740-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55105<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2464756 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:25.248842-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55103<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464748 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 151.220 sec Conn_Time: 0.016 sec bytes in/out: 97545644/2617 pkts in/out: 15419/4 pkt rxmit: 0 ooo pkts: 2484 dup bytes in: 0 ACKs delayed: 11662 delayed ACKs sent: 0
rtt: 15.125 ms rttvar: 4.812 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0x985175b9
default	10:25:25.248848-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55103<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464748 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:25.248872-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55100<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2464725 t_state: FIN_WAIT_1 process: Nexy:78860 Duration: 151.494 sec Conn_Time: 0.023 sec bytes in/out: 1369/116 pkts in/out: 1/1 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.875 ms rttvar: 8.875 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x9fca7dae
default	10:25:25.248878-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55100<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2464725 t_state: FIN_WAIT_1 process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:25.249003-0400	kernel	tcp_connection_summary (tcp_drop:1348)[<IPv4-redacted>:55102<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464738 t_state: CLOSED process: Nexy:78860 Duration: 151.420 sec Conn_Time: 0.030 sec bytes in/out: 8746/1774 pkts in/out: 7/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 35.781 ms rttvar: 18.687 ms base rtt: 28 ms so_error: 0 svc/tc: 0 flow: 0x983a751f
default	10:25:25.249016-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55102<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2464738 t_state: CLOSED process: Nexy:78860 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	10:25:25.248967-0400	mDNSResponder	[R296113] DNSServiceCreateConnection STOP PID[78860](Nexy)
default	10:25:25.241466-0400	runningboardd	Invalidating assertion 398-334-463528 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860]) from originator [osservice<com.apple.powerd>:334]
default	10:25:25.253618-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:25:25.254010-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:25:25.256058-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::out-0 issue_detected_sample_time=192960.000000 ] -- [ rms:[-38.892303], peaks:[-16.240456] ]
default	10:25:25.256081-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26806.26743.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-35.425350], peaks:[-14.451918] ]
default	10:25:25.257288-0400	runningboardd	[app<application.com.nexy.assistant.19062835.19062841(501)>:78860] termination reported by launchd (0, 0, 0)
default	10:25:25.257339-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:25:25.257589-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:25:25.257832-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:25:25.257854-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:25:25.261962-0400	runningboardd	Launch request for app<application.com.nexy.assistant.19064949.19065311(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	10:25:25.262094-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.19064949.19065311(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17058] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17058-463530 target:app<application.com.nexy.assistant.19064949.19065311(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:25:25.262243-0400	runningboardd	Assertion 398-17058-463530 (target:app<application.com.nexy.assistant.19064949.19065311(501)>) will be created as active
default	10:25:25.264300-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: none (role: None) (endowments: (null))
default	10:25:25.264561-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19062835.19062841(501)>: none (role: None) (endowments: (null))
default	10:25:25.264661-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 78860, name = Nexy
default	10:25:25.271972-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	10:25:25.272037-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.19064949.19065311(501)>
default	10:25:25.272087-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	10:25:25.272233-0400	runningboardd	app<application.com.nexy.assistant.19064949.19065311(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	10:25:25.306431-0400	launchservicesd	Hit the server for a process handle 1c45a45f0001340c that resolved to: [app<application.com.nexy.assistant.19062835.19062841(501)>:78860]
default	10:25:25.306571-0400	gamepolicyd	Received state update for 78860 (app<application.com.nexy.assistant.19062835.19062841(501)>, none-NotVisible
default	10:25:25.307923-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] is not RunningBoard jetsam managed.
default	10:25:25.307945-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] This process will not be managed.
default	10:25:25.307957-0400	runningboardd	Now tracking process: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:25.308121-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:25.310142-0400	gamepolicyd	Hit the server for a process handle 155e840d00013474 that resolved to: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:25.310235-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:25.314287-0400	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:25.314408-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-463532 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:25.314620-0400	runningboardd	Assertion 398-398-463532 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:25.314963-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:25.315074-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:25.315176-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] reported to RB as running
default	10:25:25.315192-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Set darwin role to: UserInteractive
default	10:25:25.315224-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:25.315289-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:25.320386-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:25.320417-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:25.320461-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:25.320518-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:25.322911-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:25.323218-0400	runningboardd	Invalidating assertion 398-17058-463530 (target:app<application.com.nexy.assistant.19064949.19065311(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17058]
default	10:25:25.323261-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:25.323312-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:25.323348-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:25.323442-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:25.328100-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
error	10:25:25.347239-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-334-463528 (target:[app<application.com.nexy.assistant.19062835.19062841(501)>:78860])
default	10:25:25.347439-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:25.347482-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:25.347518-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:25.347579-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:25.352644-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:25.739541-0400	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	10:25:25.743554-0400	nehelper	Handling an apps installed notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:25:25.781114-0400	nesessionmanager	UUID: Found for com.nexy.assistant: (
    "76DC2BBA-2282-E9CE-B01C-BABBAD118617"
)
default	10:25:26.221981-0400	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant)
default	10:25:26.421283-0400	kernel	Nexy[78964] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xda387f3cda8ed7cb. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	10:25:26.421298-0400	kernel	Nexy[78964] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xda387f3cda8ed7cb. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	10:25:27.280651-0400	Nexy	[0x105983580] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	10:25:27.280733-0400	Nexy	[0x10597d040] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	10:25:27.528157-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x73f9fc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:25:27.528393-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x73f9fc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:25:27.528606-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x73f9fc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:25:27.528819-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x73f9fc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	10:25:27.686934-0400	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	10:25:27.690969-0400	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	10:25:27.692405-0400	Nexy	[0x1059851b0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	10:25:27.695103-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19064949.19065311 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19064949.19065311>
default	10:25:27.699001-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	10:25:27.700668-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:25:27.700840-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:25:27.700973-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	10:25:27.700985-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	10:25:27.701016-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:25:27.701191-0400	Nexy	[0x73fabc000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	10:25:27.701313-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	10:25:27.701802-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:27.708175-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.1, subject=com.nexy.assistant,
default	10:25:27.708761-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:27.720566-0400	Nexy	[0x73fabc000] invalidated after the last release of the connection object
default	10:25:27.720693-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:25:27.720721-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:25:27.720913-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	10:25:27.722152-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3868, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:27.722815-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3868, subject=com.nexy.assistant,
default	10:25:27.723300-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
error	10:25:27.734178-0400	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	10:25:27.735034-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3870, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:27.735771-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3870, subject=com.nexy.assistant,
default	10:25:27.736285-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:27.749563-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	10:25:27.749583-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x73ec15060> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	10:25:27.767524-0400	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	10:25:27.767537-0400	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	10:25:27.770441-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:25:27.770569-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:25:27.774759-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:25:31.260940-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-463532 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964])
default	10:25:31.437903-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:31.437928-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:31.437946-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:31.437982-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:31.444024-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:31.445019-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:32.946017-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 089D8B74-0C6C-4AE6-8A2B-46A3CE925DD9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55157,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfc1882ff tp_proto=0x06"
default	10:25:32.946146-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55157<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465517 t_state: SYN_SENT process: Nexy:78964 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb269e096
default	10:25:32.969744-0400	kernel	tcp connected: [<IPv4-redacted>:55157<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465517 t_state: ESTABLISHED process: Nexy:78964 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb269e096
default	10:25:32.970093-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55157<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465517 t_state: FIN_WAIT_1 process: Nexy:78964 Duration: 0.024 sec Conn_Time: 0.024 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 24.000 ms rttvar: 12.000 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xb269e096
default	10:25:32.970104-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55157<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465517 t_state: FIN_WAIT_1 process: Nexy:78964 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:33.037585-0400	Nexy	[0x73fabc000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	10:25:33.051311-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x74076e340) Selecting device 85 from constructor
default	10:25:33.051323-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x74076e340)
default	10:25:33.051330-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x74076e340) not already running
default	10:25:33.051333-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x74076e340) nothing to teardown
default	10:25:33.051337-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x74076e340) connecting device 85
default	10:25:33.051424-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x74076e340) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:33.051526-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x74076e340) created ioproc 0xa for device 85
default	10:25:33.051640-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 7 device listeners to device 85
default	10:25:33.051799-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 0 device delegate listeners to device 85
default	10:25:33.051808-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x74076e340)
default	10:25:33.051882-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:33.051898-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:33.051903-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:33.051908-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:33.051915-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:33.052000-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x74076e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:33.052010-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x74076e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:33.052015-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:33.052020-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 0 device listeners from device 0
default	10:25:33.052022-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 0 device delegate listeners from device 0
default	10:25:33.052026-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x74076e340)
default	10:25:33.052040-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:25:33.052120-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x74076e340) caller requesting device change from 85 to 91
default	10:25:33.052129-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x74076e340)
default	10:25:33.052133-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x74076e340) not already running
default	10:25:33.052135-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x74076e340) disconnecting device 85
default	10:25:33.052140-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x74076e340) destroying ioproc 0xa for device 85
default	10:25:33.052191-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	10:25:33.052721-0400	Nexy	[0x73fabc280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	10:25:33.053611-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"PID":78964,"session_type":"Primary"} }
default	10:25:33.053692-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":78964}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b5, sessionType: 'prim', isRecording: false }, 
]
default	10:25:33.054415-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 78964, name = Nexy
default	10:25:33.054680-0400	Nexy	    SessionCore_Create.mm:99    Created session 0x73e98e680 with ID: 0x1ef0b5
default	10:25:33.055360-0400	Nexy	[0x73fabc3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	10:25:33.055502-0400	Nexy	No persisted cache on this platform.
error	10:25:33.055836-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=339147797561345 }
default	10:25:33.055851-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	10:25:33.055907-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:25:33.055999-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x74076e340) connecting device 91
default	10:25:33.056080-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x74076e340) Device ID: 91 (Input:Yes | Output:No): true
default	10:25:33.057391-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3871, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.058484-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3871, subject=com.nexy.assistant,
default	10:25:33.059092-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:33.070877-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x74076e340) created ioproc 0xa for device 91
default	10:25:33.071011-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 7 device listeners to device 91
default	10:25:33.071176-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 0 device delegate listeners to device 91
default	10:25:33.071183-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x74076e340)
default	10:25:33.071191-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:25:33.071201-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:33.071310-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:25:33.071319-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:25:33.071324-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:25:33.071409-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x74076e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:33.071423-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x74076e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:33.071429-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:33.071434-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 7 device listeners from device 85
default	10:25:33.071598-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 0 device delegate listeners from device 85
default	10:25:33.071605-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x74076e340)
default	10:25:33.072215-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:33.073230-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3872, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.074279-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3872, subject=com.nexy.assistant,
default	10:25:33.075515-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:33.086850-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:33.087802-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3873, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.088624-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3873, subject=com.nexy.assistant,
default	10:25:33.089165-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:33.100516-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	10:25:33.101905-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3874, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.102639-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3874, subject=com.nexy.assistant,
default	10:25:33.103178-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:33.114711-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:25:33.114862-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:25:33.115622-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:25:33.116799-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:33.116864-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:33.192373-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:25:33.194655-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26819 called from <private>
default	10:25:33.194715-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:25:33.196171-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:33.196316-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:33.196342-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:33.196350-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:33.200376-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463538 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:33.200855-0400	runningboardd	Assertion 398-334-463538 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:33.197406-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:33.197424-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26818 called from <private>
default	10:25:33.197432-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:33.207663-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:25:33.208177-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:25:33.211488-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:33.211530-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26819 called from <private>
default	10:25:33.211539-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26819 called from <private>
default	10:25:33.211549-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:33.211584-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:33.211586-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:26819 called from <private>
default	10:25:33.211600-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:26819 called from <private>
default	10:25:33.211613-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:33.215231-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26819 called from <private>
default	10:25:33.215337-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26819 called from <private>
default	10:25:33.215413-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:33.215451-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:33.218508-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:25:33.218601-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:33.218662-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:25:33.220047-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:33.219738-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:25:33.220272-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:25:33.220498-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:25:33.220547-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b5, Nexy(78964), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 182 starting recording
default	10:25:33.221035-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:33.215533-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26819 called from <private>
default	10:25:33.221165-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:33.215760-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:33.216157-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26819 called from <private>
default	10:25:33.218496-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:33.221482-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:25:33.218514-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:33.221653-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:33.221349-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:33.223586-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3875, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.222162-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:33.222148-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:25:33.221934-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:33.223011-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:33.222398-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:33.228341-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:33.228423-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:33.228467-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:33.228583-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:33.230158-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3875, subject=com.nexy.assistant,
default	10:25:33.232304-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:33.232340-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:33.238658-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26818 called from <private>
default	10:25:33.238698-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26818 called from <private>
default	10:25:33.238795-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:33.238823-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:33.241422-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:33.254515-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
fault	10:25:33.254403-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19064949.19065311 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19064949.19065311>
default	10:25:33.263977-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:33.268692-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:33.268742-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:33.305682-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:25:33.305886-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:25:33.314408-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:33.315659-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463542 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:33.315764-0400	runningboardd	Assertion 398-334-463542 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:33.314465-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26819 called from <private>
default	10:25:33.316536-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:33.316713-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:33.316988-0400	runningboardd	Invalidating assertion 398-334-463542 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:33.316735-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:33.316742-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:33.315820-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:33.327045-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:33.327215-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:33.327274-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:33.327490-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:33.328042-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.328061-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.328114-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.328128-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.328135-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.328142-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:33.337238-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.337248-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.337260-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.337266-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.337308-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.337343-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:33.337837-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:33.346019-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:25:33.348181-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:33.348249-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:33.354471-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:33.354487-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:33.354499-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:33.354518-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:33.387716-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:25:33.389288-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463547 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:33.391390-0400	runningboardd	Assertion 398-334-463547 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:33.396238-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:33.396267-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26819 called from <private>
default	10:25:33.396316-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:33.396812-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:33.397239-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:33.399188-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:33.397881-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:33.399074-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:33.399377-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:33.399395-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:33.399403-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:33.400995-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:25:33.401196-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:25:33.402086-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:33.402219-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26819 called from <private>
default	10:25:33.402236-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26819 called from <private>
default	10:25:33.402281-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:33.404584-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3877, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:33.425163-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463549 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:33.425245-0400	runningboardd	Assertion 398-334-463549 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:33.426785-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:33.435713-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:33.435767-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:33.435811-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:33.437000-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437016-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437051-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437061-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437072-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437082-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:33.437105-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437115-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437154-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437175-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437220-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437304-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:33.437413-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:33.437695-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437705-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437712-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437720-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:33.437740-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:33.437752-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:33.437833-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:25:34.026772-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	10:25:34.456264-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:25:34.456739-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:25:34.456912-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:34.456991-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:25:34.457034-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:34.457109-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:34.457123-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b5, Nexy(78964), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 182 stopping recording
default	10:25:34.457160-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:25:34.457257-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:34.457353-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:25:34.457854-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:34.457550-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:25:34.457565-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:34.461844-0400	runningboardd	Invalidating assertion 398-334-463549 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:34.462138-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:34.462173-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:34.461992-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:34.462196-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:34.462065-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:34.462215-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:34.462331-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:34.462388-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:34.462445-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:25:34.466475-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:34.469938-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:34.469955-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:34.469970-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:34.469980-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:34.470005-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:34.470017-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:34.470160-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:34.558156-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x74076e340) Selecting device 0 from destructor
default	10:25:34.558185-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x74076e340)
default	10:25:34.558197-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x74076e340) not already running
default	10:25:34.558204-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x74076e340) disconnecting device 91
default	10:25:34.558216-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x74076e340) destroying ioproc 0xa for device 91
default	10:25:34.558264-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:25:34.558314-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:25:34.558547-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x74076e340) nothing to setup
default	10:25:34.558567-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 0 device listeners to device 0
default	10:25:34.558576-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x74076e340) adding 0 device delegate listeners to device 0
default	10:25:34.558584-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 7 device listeners from device 91
default	10:25:34.558893-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x74076e340) removing 0 device delegate listeners from device 91
default	10:25:34.558914-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x74076e340)
default	10:25:34.565706-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:34.565764-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:34.565846-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:34.565881-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:34.572025-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:34.572751-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:34.715564-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78969.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78969, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:34.717197-0400	tccd	AUTHREQ_SUBJECT: msgID=78969.1, subject=com.nexy.assistant,
default	10:25:34.717864-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:34.732348-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6443, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78969, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:34.733344-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6443, subject=com.nexy.assistant,
default	10:25:34.733941-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:34.761183-0400	launchservicesd	CHECKIN:0x0-0xa0ca0c 78969 com.nexy.assistant
default	10:25:34.762219-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:25:34.762368-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:25:34.763261-0400	runningboardd	Invalidating assertion 398-363-463533 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	10:25:34.763834-0400	WindowServer	117923[CreateApplication]: Process creation: 0x0-0xa0ca0c (Nexy) connectionID: 117923 pid: 78969 in session 0x101
default	10:25:34.766985-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:25:34.771477-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:34.789462-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 e26c0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:34.803137-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:34.829619-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0xa0ca0c (Nexy) connectionID: 117923 pid: 78969 in session 0x101
default	10:25:34.829684-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0xa0ca0c (Nexy) acq:0x7ffa47800 count:1
default	10:25:34.830372-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0xa0ca0c removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa0ca0c (Nexy)"
)}
default	10:25:34.830632-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x13479 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa0ca0c (Nexy)"
)}
default	10:25:34.835480-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0xa0ca0c} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	10:25:34.835623-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 10537484
default	10:25:34.835766-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	10:25:34.868259-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:34.868320-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:34.868408-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Set darwin role to: None
default	10:25:34.868469-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:34.868552-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:34.872760-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-suspended (role: None) (endowments: (null))
default	10:25:34.873051-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-suspended-NotVisible
default	10:25:35.172041-0400	Nexy	[0x73fabc500] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	10:25:35.173969-0400	Nexy	[0x73fabc8c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	10:25:35.185117-0400	Nexy	Received configuration update from daemon (initial)
default	10:25:35.276015-0400	Nexy	[0x73fabca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:25:35.276659-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:25:35.276845-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:35.278652-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.2, subject=com.nexy.assistant,
default	10:25:35.279565-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.295871-0400	Nexy	[0x73fabca00] invalidated after the last release of the connection object
default	10:25:35.296823-0400	Nexy	[0x73fabca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:25:35.297380-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:25:35.297564-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:35.298717-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.3, subject=com.nexy.assistant,
default	10:25:35.299448-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.312231-0400	Nexy	[0x73fabca00] invalidated after the last release of the connection object
default	10:25:35.312315-0400	Nexy	[0x73fabca00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	10:25:35.312447-0400	Nexy	[0x73fabca00] invalidated after the last release of the connection object
default	10:25:35.313021-0400	Nexy	[0x73fabcb40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:25:35.313524-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:35.315483-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.4, subject=com.nexy.assistant,
default	10:25:35.316204-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.328939-0400	Nexy	[0x73fabcb40] invalidated after the last release of the connection object
default	10:25:35.329361-0400	Nexy	server port 0x0000b907, session port 0x0000b80b
default	10:25:35.330441-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6444, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:35.330476-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:35.331626-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6444, subject=com.nexy.assistant,
default	10:25:35.332396-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.352246-0400	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9F0DB657-3636-4A79-9698-CB585399EA81 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55158,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x85c1863e tp_proto=0x06"
default	10:25:35.352375-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55158<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465519 t_state: SYN_SENT process: Nexy:78964 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9926e8f6
default	10:25:35.365922-0400	kernel	tcp connected: [<IPv4-redacted>:55158<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465519 t_state: ESTABLISHED process: Nexy:78964 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9926e8f6
default	10:25:35.405857-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55158<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465519 t_state: FIN_WAIT_1 process: Nexy:78964 Duration: 0.054 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0x9926e8f6
default	10:25:35.405874-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55158<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465519 t_state: FIN_WAIT_1 process: Nexy:78964 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:35.406227-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:25:35.406410-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:25:35.406426-0400	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3ECCC832-A36F-42B1-B546-FD97C3BB19D5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55159,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x83b51a40 tp_proto=0x06"
default	10:25:35.406469-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55159<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465520 t_state: SYN_SENT process: Nexy:78964 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa0cb7ece
default	10:25:35.407489-0400	Nexy	nw_path_libinfo_path_check [838A6C6C-0F48-46B2-8E2A-33380B1A4321 IPv4#12ca8b55:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	10:25:35.407951-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 896D6520-4670-4C17-A942-C117E63C5A90 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55160,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x5c263233 tp_proto=0x06"
default	10:25:35.407999-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55160<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2465521 t_state: SYN_SENT process: Nexy:78964 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e128d47
default	10:25:35.420631-0400	kernel	tcp connected: [<IPv4-redacted>:55159<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465520 t_state: ESTABLISHED process: Nexy:78964 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa0cb7ece
default	10:25:35.420921-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55159<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465520 t_state: FIN_WAIT_1 process: Nexy:78964 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xa0cb7ece
default	10:25:35.420929-0400	kernel	tcp_connection_summary [<IPv4-redacted>:55159<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2465520 t_state: FIN_WAIT_1 process: Nexy:78964 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:25:35.429322-0400	kernel	tcp connected: [<IPv4-redacted>:55160<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2465521 t_state: ESTABLISHED process: Nexy:78964 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e128d47
default	10:25:35.457920-0400	Nexy	[0x73fabcb40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	10:25:35.458564-0400	Nexy	[0x73fabcc80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	10:25:35.460846-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	10:25:35.463850-0400	Nexy	server port 0x0000b80b, session port 0x0000b80b
default	10:25:35.468868-0400	Nexy	New connection 0x14d92b main
default	10:25:35.471528-0400	Nexy	CHECKIN: pid=78964
default	10:25:35.480046-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:78964" ID:398-363-463555 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:25:35.480123-0400	runningboardd	Assertion 398-363-463555 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:35.480477-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:35.480509-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:35.480551-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Set darwin role to: UserInteractive
default	10:25:35.480577-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:35.480628-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:35.480742-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:78964" ID:398-363-463556 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:25:35.480823-0400	runningboardd	Assertion 398-363-463556 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:35.480835-0400	Nexy	CHECKEDIN: pid=78964 asn=0x0-0xa0da0d foreground=0
default	10:25:35.480668-0400	launchservicesd	CHECKIN:0x0-0xa0da0d 78964 com.nexy.assistant
default	10:25:35.481625-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:25:35.481388-0400	Nexy	[0x73fabcf00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	10:25:35.481698-0400	Nexy	[0x73fabd040] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:25:35.481705-0400	Nexy	[0x73fabd040] Connection returned listener port: 0xd603
default	10:25:35.481916-0400	Nexy	[0x73f200600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x73fabd040.peer[363].0x73f200600
default	10:25:35.484616-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:25:35.485802-0400	WindowServer	14d92b[CreateApplication]: Process creation: 0x0-0xa0da0d (Nexy) connectionID: 14D92B pid: 78964 in session 0x101
default	10:25:35.485470-0400	Nexy	FRONTLOGGING: version 1
default	10:25:35.485507-0400	Nexy	Registered, pid=78964 ASN=0x0,0xa0da0d
default	10:25:35.486092-0400	Nexy	[0x73fabd180] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	10:25:35.489808-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:35.490322-0400	runningboardd	Invalidating assertion 398-363-463555 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	10:25:35.490629-0400	Nexy	[0x73fabd040] Connection returned listener port: 0xd603
default	10:25:35.491158-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:35.491061-0400	Nexy	BringForward: pid=78964 asn=0x0-0xa0da0d bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	10:25:35.491530-0400	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:25:35.493354-0400	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:25:35.494164-0400	Nexy	Post-registration system appearance: (HLTB: 1)
default	10:25:35.496512-0400	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	10:25:35.496520-0400	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	10:25:35.496571-0400	Nexy	Initializing connection
default	10:25:35.496607-0400	Nexy	Removing all cached process handles
default	10:25:35.496623-0400	Nexy	Sending handshake request attempt #1 to server
default	10:25:35.496659-0400	Nexy	Creating connection to com.apple.runningboard
default	10:25:35.496726-0400	Nexy	[0x73fabd2c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	10:25:35.496980-0400	Nexy	[0x73fabd040] Connection returned listener port: 0xd603
default	10:25:35.497633-0400	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 200000001b pid: 78964
default	10:25:35.497656-0400	runningboardd	Setting client for [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] as ready
default	10:25:35.501019-0400	Nexy	[0x73fabd040] Connection returned listener port: 0xd603
default	10:25:35.502660-0400	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	10:25:35.502672-0400	Nexy	[0x73fabd680] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	10:25:35.502782-0400	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	10:25:35.506944-0400	Nexy	Handshake succeeded
default	10:25:35.506964-0400	Nexy	Identity resolved as app<application.com.nexy.assistant.19064949.19065311(501)>
default	10:25:35.510060-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:78964" ID:398-363-463558 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	10:25:35.510380-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0xa0da0d; pid: 393>,
    <pid: 78964>
]
default	10:25:35.510401-0400	runningboardd	Assertion 398-363-463558 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:35.529514-0400	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	10:25:35.548978-0400	Nexy	[0x73fabdf40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	10:25:35.554136-0400	Nexy	FBSWorkspace connected to endpoint : <private>
default	10:25:35.554205-0400	Nexy	<FBSWorkspaceScenesClient:0x73e96e1c0 <private>> attempting immediate handshake from activate
default	10:25:35.554250-0400	Nexy	<FBSWorkspaceScenesClient:0x73e96e1c0 <private>> sent handshake
default	10:25:35.554339-0400	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	10:25:35.554742-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:35.554770-0400	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:35.559341-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:35.559688-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:35.559808-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:35.559851-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:35.559746-0400	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	10:25:35.564573-0400	Nexy	Request for <FBSScene: 0x73e96e3a0; com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA> complete!
default	10:25:35.568753-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:398-632-463560 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	10:25:35.568834-0400	runningboardd	Assertion 398-632-463560 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:35.569191-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:35.569263-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:35.569580-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:35.569660-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:35.585859-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:35.585875-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfdf80; app<application.com.nexy.assistant.19064949.19065311>:78964(vE6CD4)>
default	10:25:35.585988-0400	ControlCenter	[app<application.com.nexy.assistant.19064949.19065311>:78964] Registered new scene: <FBWorkspaceScene: 0xaf5085140; com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA> (fromRemnant = 0)
default	10:25:35.586209-0400	Nexy	Request for <FBSScene: 0x73e96e3a0; com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA> complete!
default	10:25:35.589378-0400	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	10:25:35.604768-0400	Nexy	Registering for test daemon availability notify post.
default	10:25:35.607681-0400	Nexy	SignalReady: pid=78964 asn=0x0-0xa0da0d
default	10:25:35.607949-0400	Nexy	SIGNAL: pid=78964 asn=0x0x-0xa0da0d
default	10:25:35.608572-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:25:35.620632-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	10:25:35.620640-0400	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	10:25:35.620667-0400	Nexy	[0x73fabcdc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	10:25:35.620735-0400	Nexy	[0x73fabcdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	10:25:35.624346-0400	Nexy	[0x73fabcdc0] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	10:25:35.624840-0400	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-78964). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	10:25:35.628720-0400	ControlCenter	Created instance DisplayableId(BA9459BB) in .menuBar for DisplayableAppStatusItemType(429308CA, (bid:com.nexy.assistant-Item-0-78964)) .menuBar
default	10:25:35.633239-0400	Nexy	[0x73fabe800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	10:25:35.633845-0400	Nexy	[0x73fabe940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:25:35.633909-0400	Nexy	[0x73fabe940] Connection returned listener port: 0x16303
default	10:25:35.634721-0400	Nexy	[0x73fabcdc0] invalidated after the last release of the connection object
default	10:25:35.635086-0400	Nexy	[C:2] Alloc <private>
default	10:25:35.635119-0400	Nexy	[0x73fabcdc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	10:25:35.635277-0400	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(78964)]
default	10:25:35.635850-0400	ControlCenter	Created ephemaral instance DisplayableId(BA9459BB) for (bid:com.nexy.assistant-Item-0-78964) with positioning .ephemeral
default	10:25:35.637270-0400	WindowManager	Connection activated | (78964) Nexy
default	10:25:35.638216-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-78964-463563 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	10:25:35.638279-0400	runningboardd	Assertion 398-78964-463563 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:35.645477-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:35.745964-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:35.745975-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:35.745986-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:35.746004-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:35.749167-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:35.749527-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:35.749641-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:35.755955-0400	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	10:25:35.760314-0400	Nexy	Start service name com.apple.spotlightknowledged
default	10:25:35.761075-0400	Nexy	[GMS] availability notification token 87
default	10:25:35.791668-0400	kernel	udp connect: [<IPv4-redacted>:52598<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2465524 so_state: 0x0002 process: Nexy:78964 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xbeec9832
default	10:25:35.791683-0400	kernel	udp_connection_summary [<IPv4-redacted>:52598<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2465524 so_state: 0x0002 process: Nexy:78964 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xbeec9832 flowctl: 0us (0x)
default	10:25:35.791946-0400	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1677C810-B665-4B0E-BE23-40C71B8044D6 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55162,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x3cc78bbd tp_proto=0x06"
default	10:25:35.792011-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:55162<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2465526 t_state: SYN_SENT process: Nexy:78964 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbf060f7e
default	10:25:35.800472-0400	Nexy	[com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA] Sending action(s) in update: NSSceneFenceAction
default	10:25:35.825206-0400	kernel	tcp connected: [<IPv4-redacted>:55162<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2465526 t_state: ESTABLISHED process: Nexy:78964 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbf060f7e
default	10:25:35.843895-0400	Nexy	[0x73fabe6c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:25:35.844490-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:35.845498-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.5, subject=com.nexy.assistant,
default	10:25:35.846097-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.858402-0400	Nexy	[0x73fabe6c0] invalidated after the last release of the connection object
default	10:25:35.858634-0400	Nexy	[0x73fabe6c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:25:35.859122-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78964.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:25:35.859987-0400	tccd	AUTHREQ_SUBJECT: msgID=78964.6, subject=com.nexy.assistant,
default	10:25:35.860538-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.862776-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78976.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78976, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:35.863931-0400	tccd	AUTHREQ_SUBJECT: msgID=78976.1, subject=com.nexy.assistant,
default	10:25:35.864465-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:35.872147-0400	Nexy	[0x73fabe6c0] invalidated after the last release of the connection object
default	10:25:35.872844-0400	ControlCenter	[app<application.com.nexy.assistant.19064949.19065311>:78964] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	10:25:35.872947-0400	runningboardd	Invalidating assertion 398-632-463562 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	10:25:35.873456-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	10:25:35.875374-0400	Nexy	[0x73fabe6c0] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	10:25:35.876422-0400	Nexy	[0x73fabca00] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	10:25:35.876442-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6445, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78976, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:35.876571-0400	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	10:25:35.876688-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	10:25:35.877319-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6445, subject=com.nexy.assistant,
default	10:25:35.877857-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:35.882219-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=44004.11, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	10:25:35.882245-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:35.882980-0400	tccd	AUTHREQ_SUBJECT: msgID=44004.11, subject=com.nexy.assistant,
default	10:25:35.883510-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.890609-0400	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	10:25:35.890634-0400	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	10:25:35.892683-0400	Nexy	[0x73fabea80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	10:25:35.893698-0400	Nexy	[0x73fabebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	10:25:35.904712-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6446, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:35.904741-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:35.905704-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6446, subject=com.nexy.assistant,
default	10:25:35.905972-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	10:25:35.906300-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:35.925782-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	10:25:35.939316-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 f06c0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:35.941023-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:35.941076-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	10:25:35.941107-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:35.942085-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:35.942112-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:35.942161-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:35.942187-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:35.942209-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:35.942231-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:35.942379-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:35.945966-0400	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.78964>)
default	10:25:35.950264-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:35.971049-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0xa0da0d (Nexy) mainConnectionID: 14D92B;
} for reason: deferringPolicyEvaluationSuppression
default	10:25:35.971113-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0xa0da0d (Nexy) -> <pid: 78964>
default	10:25:35.971206-0400	WindowServer	new deferring rules for pid:393: [
    [393-64B3]; <keyboardFocus; Nexy:0x0-0xa0da0d>; () -> <pid: 78964>; reason: frontmost PSN --> outbound target,
    [393-64B2]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0xa0da0d; pid: 393>; reason: frontmost PSN,
    [393-64B1]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	10:25:35.971247-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-64B3]; <keyboardFocus; Nexy:0x0-0xa0da0d>; () -> <pid: 78964>; reason: frontmost PSN --> outbound target,
    [393-64B2]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0xa0da0d; pid: 393>; reason: frontmost PSN,
    [393-64B1]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	10:25:35.971920-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0xa0da0d; pid: 393>,
    <pid: 78964>
]
default	10:25:35.981025-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:35.981057-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:35.981070-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:35.981133-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:35.984224-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:35.984544-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:35.984680-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:36.039659-0400	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.78964>)
default	10:25:36.142113-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x740c50740) Selecting device 85 from constructor
default	10:25:36.142126-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c50740)
default	10:25:36.142132-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c50740) not already running
default	10:25:36.142138-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x740c50740) nothing to teardown
default	10:25:36.142142-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c50740) connecting device 85
default	10:25:36.142257-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c50740) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:36.142390-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c50740) created ioproc 0xb for device 85
default	10:25:36.142504-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 7 device listeners to device 85
default	10:25:36.142683-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 0 device delegate listeners to device 85
default	10:25:36.142690-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c50740)
default	10:25:36.142771-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.142782-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:36.142787-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.142796-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:36.142803-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:36.142899-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:36.142908-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:36.142911-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:36.142918-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 0 device listeners from device 0
default	10:25:36.142921-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 0 device delegate listeners from device 0
default	10:25:36.142926-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c50740)
default	10:25:36.142940-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x740c50740) caller requesting device change from 85 to 85
default	10:25:36.142944-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c50740)
default	10:25:36.142947-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x740c50740) exiting with nothing to do
default	10:25:36.143517-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.144196-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	10:25:36.144284-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x73da32130, from  2 ch,  48000 Hz, Float32, interleaved to  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.144315-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.145890-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x740c50740) Selecting device 0 from destructor
default	10:25:36.145899-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c50740)
default	10:25:36.145904-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c50740) not already running
default	10:25:36.145908-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c50740) disconnecting device 85
default	10:25:36.145911-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c50740) destroying ioproc 0xb for device 85
default	10:25:36.145936-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	10:25:36.145987-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:25:36.146085-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x740c50740) nothing to setup
default	10:25:36.146095-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 0 device listeners to device 0
default	10:25:36.146099-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 0 device delegate listeners to device 0
default	10:25:36.146105-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 7 device listeners from device 85
default	10:25:36.146296-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 0 device delegate listeners from device 85
default	10:25:36.146302-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c50740)
default	10:25:36.146836-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x740c50740) Selecting device 85 from constructor
default	10:25:36.146845-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c50740)
default	10:25:36.146848-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c50740) not already running
default	10:25:36.146852-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x740c50740) nothing to teardown
default	10:25:36.146857-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c50740) connecting device 85
default	10:25:36.146924-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c50740) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:36.147017-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c50740) created ioproc 0xc for device 85
default	10:25:36.147136-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 7 device listeners to device 85
default	10:25:36.147288-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c50740) adding 0 device delegate listeners to device 85
default	10:25:36.147296-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c50740)
default	10:25:36.147367-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.147372-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:36.147378-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.147387-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:36.147394-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:36.147499-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:36.147509-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:36.147515-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:36.147519-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 0 device listeners from device 0
default	10:25:36.147524-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c50740) removing 0 device delegate listeners from device 0
default	10:25:36.147527-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c50740)
default	10:25:36.147536-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x740c50740) caller requesting device change from 85 to 85
default	10:25:36.147541-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c50740)
default	10:25:36.147552-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x740c50740) exiting with nothing to do
default	10:25:36.147594-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	10:25:36.148192-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.148513-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x73da32190, from  2 ch,  48000 Hz, Float32, interleaved to  2 ch,  24000 Hz, Float32, interleaved
default	10:25:36.148536-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.149784-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-78964-463571 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	10:25:36.149871-0400	runningboardd	Assertion 398-78964-463571 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:36.151321-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:36.151340-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:36.151386-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:36.153381-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	10:25:36.151462-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:36.155375-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	10:25:36.155508-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:36.155535-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:25:36.155602-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463572 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:36.155570-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:25:36.155848-0400	runningboardd	Assertion 398-334-463572 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:36.155852-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'MediaPlayback'
default	10:25:36.155973-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	10:25:36.156013-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 182 starting playing
default	10:25:36.156197-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:36.156013-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.156311-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:36.156409-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.156451-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.156404-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:36.156815-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	10:25:36.156493-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	10:25:36.156827-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:36.156711-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b5 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78964}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0b5, sessionType: 'prim', isRecording: false }, 
]
default	10:25:36.157165-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:36.156840-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:36.158315-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.158394-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.158420-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:36.158431-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	10:25:36.158438-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	10:25:36.158447-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	10:25:36.158487-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:36.161393-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:36.161746-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:36.161770-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:36.161812-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:36.161864-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:36.162053-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:36.162209-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:36.165889-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:36.166421-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:36.166826-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:36.586287-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.586863-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:36.587934-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:36.587968-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26819 called from <private>
default	10:25:36.593130-0400	runningboardd	Invalidating assertion 398-78964-463571 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:36.587975-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:36.590154-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26818 called from <private>
default	10:25:36.593272-0400	runningboardd	Invalidating assertion 398-334-463572 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:36.590183-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:36.602180-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:36.602209-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:36.606904-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.607217-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:36.607244-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:36.607253-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:26819 called from <private>
default	10:25:36.608625-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.608654-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.608666-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.608849-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:36.608860-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26818 called from <private>
default	10:25:36.619508-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:36.619524-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:36.621512-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26818 called from <private>
default	10:25:36.621524-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26818 called from <private>
default	10:25:36.621623-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.631963-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.632972-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:26818 called from <private>
default	10:25:36.633119-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.633169-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:26818 called from <private>
default	10:25:36.641748-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.641947-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:36.642134-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26818 called from <private>
default	10:25:36.642278-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:36.642313-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c50740) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:36.642395-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:36.642498-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c50740)
default	10:25:36.642551-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:36.642724-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26818 called from <private>
default	10:25:36.642833-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26818 called from <private>
default	10:25:36.642887-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:36.643037-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:36.643141-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:36.643265-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:36.643347-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	10:25:36.644565-0400	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	10:25:36.644625-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:26818 called from <private>
default	10:25:36.644699-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26818 called from <private>
default	10:25:36.644752-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:36.644792-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:36.644828-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:36.644913-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:36.644952-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26818 called from <private>
default	10:25:36.645000-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:36.645052-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:36.645164-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26818 called from <private>
default	10:25:36.645168-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.645198-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26818 called from <private>
default	10:25:36.645478-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	10:25:36.647294-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:36.647874-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:36.648005-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:36.648107-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:36.649266-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c50740) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:36.649476-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c50740)
default	10:25:36.650651-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.650778-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26818 called from <private>
default	10:25:36.652477-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:36.652616-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:36.652714-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:36.652812-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:36.652880-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	10:25:36.653017-0400	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	10:25:36.653095-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:26818 called from <private>
default	10:25:36.653892-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:36.654016-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	10:25:36.654357-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:36.654531-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26818 called from <private>
default	10:25:36.654637-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26818)
default	10:25:36.654921-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:36.654906-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:36.655406-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26818 called from <private>
default	10:25:36.678464-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463576 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:36.678544-0400	runningboardd	Assertion 398-334-463576 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:36.668993-0400	Nexy	-[TUICursorAccessoryAssertionController updateSubjectWithAssertionState]
default	10:25:36.854638-0400	kernel	udp connect: [<IPv4-redacted>:60858<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2465529 so_state: 0x0002 process: Nexy:78964 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa96b0126
default	10:25:36.854661-0400	kernel	udp_connection_summary [<IPv4-redacted>:60858<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2465529 so_state: 0x0002 process: Nexy:78964 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa96b0126 flowctl: 0us (0x)
default	10:25:37.098346-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:37.496164-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26818 called from <private>
default	10:25:37.496217-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26818 called from <private>
default	10:25:37.496248-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:37.499788-0400	runningboardd	Invalidating assertion 398-78964-463575 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:37.500107-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-78964-463578 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	10:25:37.500215-0400	runningboardd	Assertion 398-78964-463578 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:37.501633-0400	runningboardd	Invalidating assertion 398-334-463576 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:37.498462-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:37.502111-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463579 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:37.502275-0400	runningboardd	Assertion 398-334-463579 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:37.498503-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26818 called from <private>
default	10:25:37.626458-0400	Nexy	-[TUICursorAccessoryAssertionController updateSubjectWithAssertionState]
default	10:25:37.626537-0400	Nexy	-[TUICursorAccessoryAssertionController updateSubjectWithAssertionState]
default	10:25:37.626585-0400	Nexy	-[TUICursorAccessoryAssertionController updateSubjectWithAssertionState]
default	10:25:37.668603-0400	runningboardd	Invalidating assertion 398-632-463559 (target:app<application.com.nexy.assistant.19064949.19065311(501)>) from originator [osservice<com.apple.controlcenter(501)>:632]
default	10:25:37.772872-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.19064949.19065311(501)>
default	10:25:37.775901-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:37.775949-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:37.776155-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:37.776388-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:37.784678-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:37.790246-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:37.790491-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.136305-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26818 called from <private>
default	10:25:38.180303-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-463580 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:38.180380-0400	runningboardd	Assertion 398-393-463580 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:38.180692-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:38.180705-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:38.180748-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:38.180820-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:38.184120-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:38.184514-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.184690-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.671221-0400	runningboardd	Invalidating assertion 398-363-463557 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	10:25:38.696079-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-463593 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	10:25:38.696288-0400	runningboardd	Assertion 398-632-463593 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:38.694916-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	10:25:38.696876-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:38.696980-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:38.697024-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:38.697181-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:38.696516-0400	ControlCenter	[app<application.com.nexy.assistant.19064949.19065311>:78964] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	10:25:38.702390-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	10:25:38.703231-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.704248-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.715734-0400	Nexy	-[TUINSCursorUIController hideTextInputMenuHUD:] {
}
default	10:25:38.777895-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:38.777904-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:38.777970-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Set darwin role to: UserInteractive
default	10:25:38.777980-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:38.778043-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:38.782057-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:38.782411-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.782605-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.800216-0400	ControlCenter	[app<application.com.nexy.assistant.19064949.19065311>:78964] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	10:25:38.800357-0400	runningboardd	Invalidating assertion 398-632-463593 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	10:25:38.909540-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:38.909564-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:38.909611-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:38.909682-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:38.913573-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:38.913913-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:38.914701-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:40.097845-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:41.506305-0400	runningboardd	Assertion did invalidate due to timeout: 398-363-463558 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964])
default	10:25:41.709141-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring jetsam update because this process is not memory-managed
default	10:25:41.709167-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring suspend because this process is not lifecycle managed
default	10:25:41.709186-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring GPU update because this process is not GPU managed
default	10:25:41.709222-0400	runningboardd	[app<application.com.nexy.assistant.19064949.19065311(501)>:78964] Ignoring memory limit update because this process is not memory-managed
default	10:25:41.713542-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19064949.19065311(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:25:41.714097-0400	ControlCenter	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:41.714271-0400	gamepolicyd	Received state update for 78964 (app<application.com.nexy.assistant.19064949.19065311(501)>, running-active-NotVisible
default	10:25:43.096683-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:46.009288-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:46.012108-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:46.012123-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:46.012136-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:46.012145-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:46.012151-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:46.012159-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:46.012269-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:46.098345-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
error	10:25:46.178495-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	10:25:46.182544-0400	Nexy	[com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA] Sending action(s) in update: NSSceneFenceAction
default	10:25:46.182873-0400	Nexy	LSExceptions shared instance invalidated for timeout.
default	10:25:46.252748-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78985.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78985, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:46.254508-0400	tccd	AUTHREQ_SUBJECT: msgID=78985.1, subject=com.nexy.assistant,
default	10:25:46.255359-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:46.272066-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6448, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78985, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:46.273058-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6448, subject=com.nexy.assistant,
default	10:25:46.273667-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:46.308603-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:46.328001-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0a6d0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:46.342953-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:47.110853-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78986.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78986, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:47.112339-0400	tccd	AUTHREQ_SUBJECT: msgID=78986.1, subject=com.nexy.assistant,
default	10:25:47.112962-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:47.126636-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6449, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78986, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:47.127522-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6449, subject=com.nexy.assistant,
default	10:25:47.128089-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:47.158276-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:47.175323-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0c6d0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:47.187489-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:49.098450-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:52.098486-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	10:25:52.958189-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x740c51c40) Selecting device 85 from constructor
default	10:25:52.958230-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:52.958246-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:52.958260-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x740c51c40) nothing to teardown
default	10:25:52.958271-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 85
default	10:25:52.958519-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:52.959898-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xd for device 85
default	10:25:52.960424-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 85
default	10:25:52.960938-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 85
default	10:25:52.960963-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:52.961172-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:52.961195-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:52.961218-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:52.961236-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:52.961256-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:52.961520-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:52.961553-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:52.961570-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:52.961584-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device listeners from device 0
default	10:25:52.961596-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 0
default	10:25:52.961608-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:52.961647-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:25:52.961785-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x740c51c40) caller requesting device change from 85 to 91
default	10:25:52.961811-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:52.961824-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:52.961836-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c51c40) disconnecting device 85
default	10:25:52.961867-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c51c40) destroying ioproc 0xd for device 85
default	10:25:52.961913-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	10:25:52.962551-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:52.963063-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 91
default	10:25:52.963407-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 91 (Input:Yes | Output:No): true
default	10:25:52.965847-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3878, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:52.967713-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3878, subject=com.nexy.assistant,
default	10:25:52.968770-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:52.986588-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xb for device 91
default	10:25:52.986748-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 91
default	10:25:52.987088-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 91
default	10:25:52.987119-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:52.987137-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:25:52.987154-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:52.987389-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:25:52.987405-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:25:52.987413-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:25:52.987591-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:52.987612-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:52.987621-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:52.987628-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 7 device listeners from device 85
default	10:25:52.987875-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 85
default	10:25:52.987890-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:52.988723-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:52.990334-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3879, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:52.991575-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3879, subject=com.nexy.assistant,
default	10:25:52.992265-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.004998-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:53.006032-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3880, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.006889-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3880, subject=com.nexy.assistant,
default	10:25:53.007466-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.019428-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x740c51c40) Selecting device 0 from destructor
default	10:25:53.019435-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.019440-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.019444-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c51c40) disconnecting device 91
default	10:25:53.019450-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c51c40) destroying ioproc 0xb for device 91
default	10:25:53.019474-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:25:53.019737-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:53.019836-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x740c51c40) nothing to setup
default	10:25:53.019846-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device listeners to device 0
default	10:25:53.019851-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 0
default	10:25:53.019856-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 7 device listeners from device 91
default	10:25:53.020021-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 91
default	10:25:53.020030-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.020812-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x740c51c40) Selecting device 85 from constructor
default	10:25:53.020829-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.020834-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.020838-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x740c51c40) nothing to teardown
default	10:25:53.020842-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 85
default	10:25:53.020936-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:53.021476-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xe for device 85
default	10:25:53.021605-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 85
default	10:25:53.021763-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 85
default	10:25:53.021770-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:53.021841-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:53.021850-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:53.021856-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:25:53.021861-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:53.021867-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:53.021970-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:53.021981-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:53.021986-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:53.021991-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device listeners from device 0
default	10:25:53.021996-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 0
default	10:25:53.022000-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.022010-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:25:53.022056-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x740c51c40) caller requesting device change from 85 to 91
default	10:25:53.022063-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.022068-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.022073-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c51c40) disconnecting device 85
default	10:25:53.022078-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c51c40) destroying ioproc 0xe for device 85
default	10:25:53.022106-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xe}
default	10:25:53.022325-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:53.022943-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 91
default	10:25:53.023027-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 91 (Input:Yes | Output:No): true
default	10:25:53.024004-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3881, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.024804-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3881, subject=com.nexy.assistant,
default	10:25:53.025357-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.035986-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xc for device 91
default	10:25:53.036108-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 91
default	10:25:53.036287-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 91
default	10:25:53.036294-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:53.036300-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:25:53.036309-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:53.036446-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:25:53.036453-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:25:53.036458-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:25:53.036542-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:53.036552-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:53.036557-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:53.036562-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 7 device listeners from device 85
default	10:25:53.036712-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 85
default	10:25:53.036722-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.036729-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	10:25:53.037276-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:53.038161-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3882, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.038851-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3882, subject=com.nexy.assistant,
default	10:25:53.039376-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.049829-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x73da31440, from  1 ch,  24000 Hz, Float32 to  1 ch,  48000 Hz, Float32
default	10:25:53.050025-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:53.050982-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3883, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.051774-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3883, subject=com.nexy.assistant,
default	10:25:53.052340-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.064471-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3884, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.065190-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3884, subject=com.nexy.assistant,
default	10:25:53.065737-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.077676-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:25:53.077951-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:25:53.079912-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	10:25:53.081948-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	10:25:53.081670-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:53.081691-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26818 called from <private>
default	10:25:53.081707-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:53.082374-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:53.082381-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:53.082043-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:53.082827-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:25:53.082973-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:53.084989-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.085253-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:53.085345-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:53.085397-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.087526-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:53.085226-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	10:25:53.086316-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:53.087865-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:53.087977-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.088188-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b5, Nexy(78964), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 182 starting recording
default	10:25:53.088397-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:53.088630-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:53.088716-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:25:53.088840-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	10:25:53.084726-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26818 called from <private>
default	10:25:53.088965-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.084847-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26819 called from <private>
default	10:25:53.089364-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:53.089095-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	10:25:53.084896-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:53.089243-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	10:25:53.085077-0400	runningboardd	Invalidating assertion 398-78964-463578 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964]
default	10:25:53.089253-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:53.089169-0400	runningboardd	Invalidating assertion 398-334-463579 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:53.102529-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:53.102582-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:53.102612-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:53.102657-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:53.103116-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:53.102976-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:53.102998-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:53.103974-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-78964-463616 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	10:25:53.104120-0400	runningboardd	Assertion 398-78964-463616 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:53.103625-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26818 called from <private>
default	10:25:53.103634-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26818 called from <private>
default	10:25:53.105206-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3885, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.113396-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3885, subject=com.nexy.assistant,
default	10:25:53.113879-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.114129-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26818 called from <private>
default	10:25:53.114141-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26818 called from <private>
default	10:25:53.113984-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.114223-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26818)
default	10:25:53.114063-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.114857-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.114424-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.116523-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.116780-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.119285-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:53.156745-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.156836-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.156874-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.156965-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	10:25:53.154278-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x73da325e0, from  2 ch,  48000 Hz, Float32, interleaved to  2 ch,  24000 Hz, Float32, interleaved
default	10:25:53.154442-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	10:25:53.157120-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.158099-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:53.166189-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.176083-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:53.176131-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463620 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:53.176141-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:53.176181-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:53.176184-0400	runningboardd	Assertion 398-334-463620 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:53.176368-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:53.176553-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.176565-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.176641-0400	runningboardd	Invalidating assertion 398-334-463620 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) from originator [osservice<com.apple.powerd>:334]
default	10:25:53.176619-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.176840-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19064949.19065311(501)>:78964] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-463621 target:78964 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:25:53.176789-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.176883-0400	runningboardd	Assertion 398-334-463621 (target:[app<application.com.nexy.assistant.19064949.19065311(501)>:78964]) will be created as active
default	10:25:53.187544-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:25:53.187664-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-40.277206], peaks:[-22.808556] ]
default	10:25:53.187680-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-37.280659], peaks:[-21.122101] ]
default	10:25:53.188702-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:53.188760-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63db600] Created node ADM::com.nexy.assistant_26819.26743.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:25:53.223225-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:25:53.224667-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:53.224708-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26819 called from <private>
default	10:25:53.224766-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:53.225792-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:53.225904-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:53.225919-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:53.225924-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:53.226645-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:25:53.226787-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:25:53.227152-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:53.227415-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26819 called from <private>
default	10:25:53.227425-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26819 called from <private>
default	10:25:53.227436-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:53.228971-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3887, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.229862-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3887, subject=com.nexy.assistant,
default	10:25:53.230668-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.231831-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:53.231877-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:53.231904-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:53.231915-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:53.232009-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:53.232561-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.232575-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.232585-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.232593-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.232599-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.232641-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.232810-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:53.246061-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:53.246133-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26819 called from <private>
default	10:25:53.246268-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:25:53.247329-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26819 called from <private>
default	10:25:53.247807-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26819)
default	10:25:53.247828-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26819 called from <private>
default	10:25:53.247836-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26819 called from <private>
default	10:25:53.248600-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:25:53.248735-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:25:53.249073-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26819)
default	10:25:53.249228-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26819 called from <private>
default	10:25:53.249239-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26819 called from <private>
default	10:25:53.249250-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26819 called from <private>
default	10:25:53.250479-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3888, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.251269-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3888, subject=com.nexy.assistant,
default	10:25:53.251988-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.252937-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:53.252976-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:53.253001-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:53.253012-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:53.253096-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:53.253362-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.253381-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.253395-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.253401-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.253407-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.253412-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.253520-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:53.266858-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26819 called from <private>
default	10:25:53.272542-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:53.272577-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:53.272600-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:53.272615-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:53.272840-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272850-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272859-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.272865-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272872-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.272878-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.272902-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272916-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272950-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.272980-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.272999-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.273034-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.273154-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:53.273441-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:25:53.273518-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.273525-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.273536-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.273542-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.273576-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.273617-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.430762-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	10:25:53.431799-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	10:25:53.431981-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:53.432023-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	10:25:53.432061-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:53.432090-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.432142-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'MediaPlayback'
default	10:25:53.432147-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:53.432210-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:53.432302-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:53.432363-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.432501-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:53.432578-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:53.432673-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:53.432636-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.432720-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b5, Nexy(78964), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 182 stopping recording
default	10:25:53.432761-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:53.432812-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:53.433063-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	10:25:53.432869-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:53.433085-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:53.432924-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	10:25:53.436430-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:53.436176-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:53.438380-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:53.438615-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:53.439904-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:53.440074-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:53.441544-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441682-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441612-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441715-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441642-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441730-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.441668-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.441746-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	10:25:53.441760-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:53.441776-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
error	10:25:53.441795-0400	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	10:25:53.441831-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.441924-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:53.441956-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.442007-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:53.442153-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:53.442183-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:53.442207-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:53.442306-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:53.442317-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:53.442326-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 1
default	10:25:53.442333-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	10:25:53.442342-0400	audioaccessoryd	Updating local audio category 200 -> 201 app com.nexy.assistant
default	10:25:53.442435-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:53.442895-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	10:25:53.444052-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.444066-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.444080-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.444087-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:53.444093-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:53.444099-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:53.444245-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:53.536623-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x740c51c40) Selecting device 0 from destructor
default	10:25:53.536640-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.536649-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.536655-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c51c40) disconnecting device 91
default	10:25:53.536664-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c51c40) destroying ioproc 0xc for device 91
default	10:25:53.536701-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	10:25:53.537070-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:53.537235-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x740c51c40) nothing to setup
default	10:25:53.537247-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device listeners to device 0
default	10:25:53.537255-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 0
default	10:25:53.537262-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 7 device listeners from device 91
default	10:25:53.537489-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 91
default	10:25:53.537513-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.539800-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x740c51c40) Selecting device 85 from constructor
default	10:25:53.539813-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.539827-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.539833-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x740c51c40) nothing to teardown
default	10:25:53.539836-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 85
default	10:25:53.539958-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 85 (Input:No | Output:Yes): true
default	10:25:53.540446-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xf for device 85
default	10:25:53.540581-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 85
default	10:25:53.540826-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 85
default	10:25:53.540836-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:53.540934-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:53.540945-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	10:25:53.540954-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	10:25:53.540961-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	10:25:53.540970-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:53.541095-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:53.541110-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:53.541117-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:53.541124-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device listeners from device 0
default	10:25:53.541129-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 0
default	10:25:53.541134-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.541150-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:25:53.541209-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x740c51c40) caller requesting device change from 85 to 91
default	10:25:53.541220-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x740c51c40)
default	10:25:53.541227-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x740c51c40) not already running
default	10:25:53.541233-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x740c51c40) disconnecting device 85
default	10:25:53.541238-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x740c51c40) destroying ioproc 0xf for device 85
default	10:25:53.541254-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xf}
default	10:25:53.541557-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	10:25:53.541773-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x740c51c40) connecting device 91
default	10:25:53.541943-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x740c51c40) Device ID: 91 (Input:Yes | Output:No): true
default	10:25:53.544035-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3889, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.545592-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3889, subject=com.nexy.assistant,
default	10:25:53.546468-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.562577-0400	Nexy	[com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA] Sending action(s) in update: NSSceneFenceAction
default	10:25:53.564506-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x740c51c40) created ioproc 0xd for device 91
default	10:25:53.564659-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 7 device listeners to device 91
default	10:25:53.564860-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x740c51c40) adding 0 device delegate listeners to device 91
default	10:25:53.564876-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x740c51c40)
default	10:25:53.564899-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	10:25:53.564913-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:25:53.565061-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	10:25:53.565068-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	10:25:53.565074-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:25:53.565176-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:25:53.565195-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x740c51c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:25:53.565201-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	10:25:53.565205-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 7 device listeners from device 85
default	10:25:53.565376-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x740c51c40) removing 0 device delegate listeners from device 85
default	10:25:53.565388-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x740c51c40)
default	10:25:53.565404-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	10:25:53.566042-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:53.567328-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3890, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.568381-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3890, subject=com.nexy.assistant,
default	10:25:53.569000-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.580835-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:25:53.581883-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3891, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:53.582675-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3891, subject=com.nexy.assistant,
default	10:25:53.583214-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:53.622745-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78988.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78988, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:53.623980-0400	tccd	AUTHREQ_SUBJECT: msgID=78988.1, subject=com.nexy.assistant,
default	10:25:53.624520-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:53.637048-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6450, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78988, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:53.637825-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6450, subject=com.nexy.assistant,
default	10:25:53.638360-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:53.669604-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:53.685058-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 116d0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:53.695936-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:25:54.102523-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3892, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:25:54.104222-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3892, subject=com.nexy.assistant,
default	10:25:54.104994-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109800 at /Applications/Nexy.app
default	10:25:54.128160-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xd}
default	10:25:54.129465-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	10:25:54.129609-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:54.129657-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:25:54.129693-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:54.129723-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:54.129770-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	10:25:54.129774-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:54.129817-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:54.129847-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:54.129867-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:54.129928-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:54.129964-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	10:25:54.129983-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:54.130083-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:54.130021-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0b5, Nexy(78964), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 182 starting recording
default	10:25:54.130083-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:54.130105-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:54.130146-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:25:54.130218-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	10:25:54.130305-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:54.130346-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	10:25:54.131922-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:54.131731-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:54.133498-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	10:25:54.133410-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:54.133522-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:54.133212-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	10:25:54.134680-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	10:25:54.134840-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:54.135790-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135691-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135828-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135737-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135860-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135766-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135885-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	10:25:54.135790-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	10:25:54.135919-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135958-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	10:25:54.135974-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:54.135988-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.135998-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	10:25:54.136030-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:54.136040-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	10:25:54.136051-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	10:25:54.136145-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	10:25:54.136162-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	10:25:54.136173-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 1
default	10:25:54.136183-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	10:25:54.136193-0400	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	10:25:54.136229-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	10:25:54.140296-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:25:54.140388-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:25:54.140436-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	10:25:54.140456-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:25:54.141063-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141077-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141107-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.141119-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141129-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.141136-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:54.141146-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141155-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141163-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.141169-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.141189-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.141196-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:54.141395-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:25:54.142205-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:25:54.142326-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.142338-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.142348-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.142354-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:25:54.142362-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:25:54.142368-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:25:55.098423-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 501, Remote 0NumofApp 1
default	10:25:55.960560-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	10:25:55.962233-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0b5","name":"Nexy(78964)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:25:55.962488-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:25:55.962558-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0b5, Nexy(78964), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	10:25:55.962635-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:55.962698-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:55.962801-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0b5, Nexy(78964), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:25:55.962819-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:55.962882-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:55.962959-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	10:25:55.963010-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:55.963109-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 182 stopping playing
default	10:25:55.963184-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:25:55.963247-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 182, PID = 78964, Name = sid:0x1ef0b5, Nexy(78964), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:25:55.963294-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0b5, Nexy(78964), 'prim'', displayID:'com.nexy.assistant'}
default	10:25:55.963325-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:55.963428-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0b5 to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":78964}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1ef0b5, sessionType: 'prim', isRecording: true }, 
]
default	10:25:55.963581-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:25:55.963615-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:25:55.969394-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:55.969827-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:55.971728-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:25:55.971911-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	10:25:55.972815-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.972721-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.972767-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.972865-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.972794-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.972903-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	10:25:55.972932-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	10:25:55.972954-0400	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	10:25:55.972980-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.973057-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.973074-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:55.973093-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.973103-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:55.973138-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:55.973149-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:25:55.973160-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:25:55.973191-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:25:56.074889-0400	Nexy	[com.apple.controlcenter:CF94BE79-2EDB-4C20-8047-861C614352EA] Sending action(s) in update: NSSceneFenceAction
default	10:25:56.142803-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=78989.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=78989, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:25:56.144316-0400	tccd	AUTHREQ_SUBJECT: msgID=78989.1, subject=com.nexy.assistant,
default	10:25:56.144933-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:56.158632-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6451, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78964, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=78989, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:25:56.159508-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6451, subject=com.nexy.assistant,
default	10:25:56.160077-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:56.192241-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	10:25:56.210587-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 136d0e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	10:25:56.223901-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
