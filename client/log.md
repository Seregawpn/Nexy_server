default	12:57:06.725352-0500	dmd	Requested application com.nexy.assistant has policy OK, associated categories:DH1005 associated sites:(null) equivalent bundle identifiers:com.nexy.assistant
default	12:57:06.730077-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	12:57:06.730557-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	12:57:06.812649-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] is not RunningBoard jetsam managed.
default	12:57:06.812671-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] This process will not be managed.
default	12:57:06.812686-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:06.812937-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:06.819353-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:06.819526-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-937574 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:06.819741-0500	runningboardd	Assertion 394-394-937574 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:06.820013-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:06.820034-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:06.820061-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Set darwin role to: UserInteractive
default	12:57:06.820080-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:06.824124-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x148c48b com.nexy.assistant starting stopped process.
default	12:57:06.826700-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	12:57:06.826931-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb200: Nexy> state 2
default	12:57:06.826958-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	12:57:06.937978-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:06.997240-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	12:57:07.000147-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.61, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	12:57:07.014353-0500	tccd	AUTHREQ_SUBJECT: msgID=489.61, subject=com.nexy.assistant,
default	12:57:07.015996-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255b00 at /Applications/Nexy.app
default	12:57:07.042258-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	12:57:07.060602-0500	kernel	Nexy[36743] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x4d6aff4ece8313cd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	12:57:07.060626-0500	kernel	Nexy[36743] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x4d6aff4ece8313cd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	12:57:07.338989-0500	Nexy	[0x10379caf0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	12:57:07.339097-0500	Nexy	[0x10379d030] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	12:57:07.592009-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x91b5d80e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:57:07.592242-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x91b5d80e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:57:07.592449-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x91b5d80e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:57:07.592653-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x91b5d80e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	12:57:07.593925-0500	Nexy	[0x1037aa7b0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	12:57:07.594625-0500	Nexy	[0x91aba0000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	12:57:07.594928-0500	Nexy	[0x91aba0140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	12:57:07.595377-0500	Nexy	[0x91aba0280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	12:57:07.596095-0500	Nexy	Received configuration update from daemon (initial)
default	12:57:07.597423-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	12:57:07.597790-0500	Nexy	[0x91aba03c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:57:07.598474-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:07.600013-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.1, subject=com.nexy.assistant,
default	12:57:07.600779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257300 at /Applications/Nexy.app
default	12:57:07.614846-0500	Nexy	[0x91aba03c0] invalidated after the last release of the connection object
default	12:57:07.615191-0500	Nexy	server port 0x0000370f, session port 0x0000370f
default	12:57:07.616156-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9056, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:57:07.616178-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:57:07.616951-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9056, subject=com.nexy.assistant,
default	12:57:07.617791-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257300 at /Applications/Nexy.app
default	12:57:07.634802-0500	Nexy	New connection 0x17bfbb main
default	12:57:07.637381-0500	Nexy	CHECKIN: pid=36743
default	12:57:07.645591-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:36743" ID:394-357-937585 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	12:57:07.645700-0500	runningboardd	Assertion 394-357-937585 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:07.646028-0500	launchservicesd	CHECKIN:0x0-0x148c48b 36743 com.nexy.assistant
default	12:57:07.646153-0500	runningboardd	Invalidating assertion 394-357-937575 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	12:57:07.646181-0500	Nexy	CHECKEDIN: pid=36743 asn=0x0-0x148c48b foreground=0
default	12:57:07.646251-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	12:57:07.646389-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	12:57:07.646467-0500	Nexy	[0x91aba03c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:57:07.646476-0500	Nexy	[0x91aba03c0] Connection returned listener port: 0x4e03
default	12:57:07.646760-0500	Nexy	[0x91b734300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x91aba03c0.peer[357].0x91b734300
default	12:57:07.648493-0500	Nexy	FRONTLOGGING: version 1
default	12:57:07.648499-0500	Nexy	Registered, pid=36743 ASN=0x0,0x148c48b
default	12:57:07.648772-0500	WindowServer	17bfbb[CreateApplication]: Process creation: 0x0-0x148c48b (Nexy) connectionID: 17BFBB pid: 36743 in session 0x101
default	12:57:07.649393-0500	Nexy	[0x91aba0500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	12:57:07.650799-0500	Nexy	[0x91aba03c0] Connection returned listener port: 0x4e03
default	12:57:07.651534-0500	Nexy	BringForward: pid=36743 asn=0x0-0x148c48b bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	12:57:07.651721-0500	Nexy	BringFrontModifier: pid=36743 asn=0x0-0x148c48b Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	12:57:07.652509-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:57:07.653944-0500	Nexy	No persisted cache on this platform.
default	12:57:07.655240-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:57:07.655774-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	12:57:07.658636-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	12:57:07.658648-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	12:57:07.658713-0500	Nexy	Initializing connection
default	12:57:07.658751-0500	Nexy	Removing all cached process handles
default	12:57:07.658775-0500	Nexy	Sending handshake request attempt #1 to server
default	12:57:07.658788-0500	Nexy	Creating connection to com.apple.runningboard
default	12:57:07.658796-0500	Nexy	[0x91aba0640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	12:57:07.659218-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] as ready
default	12:57:07.659845-0500	Nexy	Handshake succeeded
default	12:57:07.659859-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41202063.41202072(501)>
default	12:57:07.660437-0500	Nexy	[0x91aba03c0] Connection returned listener port: 0x4e03
default	12:57:07.661375-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 36743
default	12:57:07.664369-0500	Nexy	[0x91aba03c0] Connection returned listener port: 0x4e03
default	12:57:07.668198-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	12:57:07.668224-0500	Nexy	[0x91aba0780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	12:57:07.668327-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	12:57:07.668410-0500	Nexy	[0x91aba0a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:57:07.669962-0500	Nexy	[0x91aba0a00] Connection returned listener port: 0x6703
default	12:57:07.670887-0500	Nexy	Registered process with identifier 36743-2805259
default	12:57:08.869529-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 368789F9-4758-4DD6-A536-718CD5FD8F2C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64752,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb9d31ec5 tp_proto=0x06"
default	12:57:08.869596-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64752<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4824344 t_state: SYN_SENT process: Nexy:36743 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9efcca95
default	12:57:08.870201-0500	kernel	tcp connected: [<IPv4-redacted>:64752<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4824344 t_state: ESTABLISHED process: Nexy:36743 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9efcca95
default	12:57:08.870495-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64752<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4824344 t_state: FIN_WAIT_1 process: Nexy:36743 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9efcca95
default	12:57:08.870502-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64752<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4824344 t_state: FIN_WAIT_1 process: Nexy:36743 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	12:57:08.947873-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	12:57:08.949459-0500	Nexy	[0x91aba0c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	12:57:08.950772-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"PID":36743,"session_type":"Primary"} }
default	12:57:08.950869-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":36743}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47f1, sessionType: 'prim', isRecording: false }, 
]
default	12:57:08.951603-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 36743, name = Nexy
default	12:57:08.951956-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x91abff960 with ID: 0x1f47f1
default	12:57:08.952585-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	12:57:08.954051-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	12:57:08.956449-0500	Nexy	[0x91aba0dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	12:57:08.959867-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41202063.41202072 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41202063.41202072>
default	12:57:08.965239-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	12:57:08.968461-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	12:57:08.968645-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	12:57:08.968810-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	12:57:08.968821-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	12:57:08.968858-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:57:08.968995-0500	Nexy	[0x91aba0f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	12:57:08.969278-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	12:57:08.969604-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:08.977336-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.2, subject=com.nexy.assistant,
default	12:57:08.978018-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
default	12:57:08.990222-0500	Nexy	[0x91aba0f00] invalidated after the last release of the connection object
default	12:57:08.990289-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:57:08.993681-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	12:57:08.994914-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8307, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:08.996076-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8307, subject=com.nexy.assistant,
default	12:57:08.996690-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
error	12:57:09.013350-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	12:57:09.014264-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8309, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:09.015214-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8309, subject=com.nexy.assistant,
default	12:57:09.015778-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
default	12:57:09.032035-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	12:57:09.032434-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x91c36ca20> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	12:57:09.056504-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:09.056634-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:09.061573-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	12:57:09.063417-0500	Nexy	[0x91aba0f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	12:57:09.063724-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=157809983356929 }
default	12:57:09.063817-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	12:57:09.063864-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	12:57:09.063898-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	12:57:09.077702-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:09.077838-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:09.082490-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 125
default	12:57:09.118530-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	12:57:09.118552-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	12:57:09.125859-0500	Nexy	[0x91aba1040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	12:57:09.630090-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x91bdec040) Selecting device 85 from constructor
default	12:57:09.630104-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdec040)
default	12:57:09.630110-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdec040) not already running
default	12:57:09.630481-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x91bdec040) nothing to teardown
default	12:57:09.630486-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdec040) connecting device 85
default	12:57:09.630609-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:09.630712-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdec040) created ioproc 0xa for device 85
default	12:57:09.630822-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdec040) adding 7 device listeners to device 85
default	12:57:09.631006-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdec040) adding 0 device delegate listeners to device 85
default	12:57:09.631017-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:57:09.631099-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.631109-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:09.631115-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.631129-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:09.631138-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:09.631241-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:09.631249-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:09.631257-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:09.631261-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdec040) removing 0 device listeners from device 0
default	12:57:09.631266-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdec040) removing 0 device delegate listeners from device 0
default	12:57:09.631269-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdec040)
default	12:57:09.631326-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:57:09.631849-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.633394-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	12:57:09.633457-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	12:57:09.633641-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acb4ae0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.633677-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.635852-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.636118-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.640906-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.641172-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.643316-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f258c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.643332-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.643723-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.644339-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f258c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.644351-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x919f258c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:09.644359-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.644359-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:57:09.644370-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:57:09.644375-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:57:09.645107-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f258c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.645116-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x919f258c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:09.645121-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:57:09.645123-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:09.645131-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:57:09.645134-0500	Nexy	AudioConverter -> 0x919f258c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:57:09.645304-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x919f258c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:09.712640-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x91bdece40) Selecting device 85 from constructor
default	12:57:09.712647-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:09.712654-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:09.712657-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x91bdece40) nothing to teardown
default	12:57:09.712661-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 85
default	12:57:09.712734-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:09.712829-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xb for device 85
default	12:57:09.712925-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 85
default	12:57:09.713083-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 85
default	12:57:09.713092-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:09.713155-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.713167-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:09.713174-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.713181-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:09.713188-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:09.713277-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:09.713284-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:09.713291-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:09.713295-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device listeners from device 0
default	12:57:09.713301-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 0
default	12:57:09.713306-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:09.713318-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:57:09.713366-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x91bdece40) caller requesting device change from 85 to 91
default	12:57:09.713378-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:09.713385-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:09.713387-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 85
default	12:57:09.713392-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xb for device 85
default	12:57:09.713495-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:09.713567-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:09.713643-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 91
default	12:57:09.713711-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 91 (Input:Yes | Output:No): true
default	12:57:09.715183-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8310, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:09.716794-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8310, subject=com.nexy.assistant,
default	12:57:09.717462-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
default	12:57:09.736562-0500	tccd	AUTHREQ_PROMPTING: msgID=395.8310, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	12:57:11.801573-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	12:57:11.802201-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xa for device 91
default	12:57:11.802515-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 91
default	12:57:11.802808-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 91
default	12:57:11.802824-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:11.802838-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	12:57:11.802853-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:11.803004-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	12:57:11.803062-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	12:57:11.803073-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	12:57:11.803081-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	12:57:11.803214-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:11.803227-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:11.803235-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:11.803241-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 85
default	12:57:11.803461-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 85
default	12:57:11.803473-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:11.804053-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:11.805738-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8311, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:11.807445-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8311, subject=com.nexy.assistant,
default	12:57:11.809390-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
default	12:57:11.840843-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f7cc30, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	12:57:11.841123-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:11.842658-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8312, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:11.843945-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8312, subject=com.nexy.assistant,
default	12:57:11.844619-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170600 at /Applications/Nexy.app
default	12:57:11.846690-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-937574 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743])
default	12:57:11.863327-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8313, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:11.864310-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8313, subject=com.nexy.assistant,
default	12:57:11.864903-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170000 at /Applications/Nexy.app
default	12:57:11.881189-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	12:57:11.881648-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:57:11.881777-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	12:57:11.882323-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:57:11.883080-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	12:57:11.884866-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	12:57:11.885426-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:11.885487-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:11.944591-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:11.944602-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:11.944611-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:11.944634-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:11.947700-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:11.948070-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:11.980509-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	12:57:11.982028-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:11.982146-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:11.982157-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	12:57:11.982872-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:11.983053-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:11.983069-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:11.984268-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:11.984477-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:11.984484-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:11.984882-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:11.984894-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:11.984946-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:11.984961-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:11.988507-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937610 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:11.988667-0500	runningboardd	Assertion 394-328-937610 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:11.989144-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:11.989361-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:11.989443-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:11.989839-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:11.989917-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
fault	12:57:11.989924-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41202063.41202072 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41202063.41202072>
default	12:57:11.990204-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:11.990360-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:11.990688-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:11.990763-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	12:57:11.992458-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41202063.41202072 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41202063.41202072>
default	12:57:11.992520-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:11.992537-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:11.992538-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48500 called from <private>
default	12:57:11.992547-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48500 called from <private>
default	12:57:11.992547-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:11.992822-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48500 called from <private>
default	12:57:11.993076-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:11.993299-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48500 called from <private>
default	12:57:11.993736-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:11.993901-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:11.993963-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:11.994004-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:11.994225-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:11.994231-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:11.998557-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	12:57:11.998635-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:57:11.998683-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:11.998874-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47f1, Nexy(36743), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	12:57:11.999039-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:57:11.999041-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:11.999051-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:57:11.999171-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:11.999174-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:11.999188-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:57:11.999196-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:57:11.999320-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:12.999509-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.999535-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	12:57:12.999727-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 starting recording
default	12:57:12.999826-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.000786-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.001938-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:12.002322-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:12.002856-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:12.004024-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	12:57:12.004195-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:12.004704-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:57:12.006521-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:12.013422-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:12.013864-0500	runningboardd	Invalidating assertion 394-328-937610 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:12.014888-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:12.015969-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:57:12.015979-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:57:12.015994-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:57:12.016004-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:57:12.017910-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:12.017949-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:12.017956-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:12.019066-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:12.019082-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:12.019087-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:12.019463-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:57:12.019470-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:57:12.021409-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:12.025578-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:12.025731-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:12.027926-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:12.028058-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:12.028100-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.028140-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028160-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028168-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028179-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:12.028189-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028198-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:12.028204-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:12.028302-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:12.028409-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028459-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:12.028595-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:57:12.028697-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:12.028717-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:12.028744-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:12.028939-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:57:12.028983-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:12.029047-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:57:12.029076-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:57:12.029124-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:57:12.029158-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:57:12.029181-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:12.029256-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:12.029354-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:12.029402-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:12.029464-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:12.029514-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:12.029556-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:12.029591-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:12.029623-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:12.029654-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:12.029685-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:12.029711-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:12.029741-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:12.029756-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:12.029769-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:12.029799-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:12.029844-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:12.029885-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:12.029927-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:12.030500-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:12.030709-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:12.030749-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:12.031114-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8314, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:12.031635-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.031738-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.032301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.032397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.032444-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.033647-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.033749-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.033966-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8314, subject=com.nexy.assistant,
default	12:57:12.034466-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:12.034713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170f00 at /Applications/Nexy.app
default	12:57:12.056557-0500	Nexy	AudioConverter -> 0x91acb4b10: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:57:12.057607-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f7d050, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:57:12.057666-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:12.057849-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
error	12:57:12.060139-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	12:57:12.077105-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:57:12.080034-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:57:12.080070-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:12.082720-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:12.082845-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937611 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:12.082951-0500	runningboardd	Assertion 394-328-937611 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:12.091469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8315, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:12.095544-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170f00 at /Applications/Nexy.app
default	12:57:12.116740-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	12:57:12.119286-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:12.119348-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:12.120887-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:12.120904-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:12.120923-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:12.120985-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:12.125696-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:12.157710-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	12:57:12.159324-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937613 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:12.159404-0500	runningboardd	Assertion 394-328-937613 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:12.160667-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:57:12.160741-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:12.160895-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:12.163055-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:12.163214-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:12.163347-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:12.163448-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:12.165062-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:12.165184-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:12.165205-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:12.165210-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:12.166016-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:12.166143-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:12.166476-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:12.166913-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:12.166923-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:12.166938-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:12.168200-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8316, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:12.170196-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x91abf0630: iounit configuration changed > posting notification
default	12:57:12.170711-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8316, subject=com.nexy.assistant,
default	12:57:12.171505-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:12.171876-0500	runningboardd	Invalidating assertion 394-328-937613 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:12.172041-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:12.173132-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170f00 at /Applications/Nexy.app
default	12:57:12.173490-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:12.173549-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:12.173602-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.173980-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.174267-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174280-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174292-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.174299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.174365-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.174544-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:12.174634-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174820-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174879-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.174933-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.174963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.174993-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.175338-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:12.193267-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937614 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:12.194219-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:57:12.195158-0500	runningboardd	Assertion 394-328-937614 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:12.203289-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:12.203324-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:12.203355-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.203543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203552-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203564-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.203577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203589-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.203596-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.203614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203634-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.203672-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.203694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.203741-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.203943-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:12.205246-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.205276-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.205286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.205293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.205302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.205308-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.205338-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	12:57:12.286119-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	12:57:12.286421-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:57:12.286510-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:12.286562-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:12.286601-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:12.286650-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 stopping recording
default	12:57:12.286672-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:57:12.286678-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:57:12.286710-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:12.286748-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:12.286880-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:57:12.286899-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:12.286930-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:57:12.287185-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:12.287220-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.287265-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:12.287307-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:12.287338-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:57:12.287410-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.287426-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:57:12.287446-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:12.287458-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:57:12.288757-0500	runningboardd	Invalidating assertion 394-328-937614 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:12.290935-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:12.294440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.294457-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.294472-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.294481-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:12.294491-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:12.294497-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:12.294650-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:12.387893-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x91bdece40) Selecting device 0 from destructor
default	12:57:12.387907-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:12.387917-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:12.387923-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 91
default	12:57:12.387929-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xa for device 91
default	12:57:12.387973-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	12:57:12.388012-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:12.388225-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x91bdece40) nothing to setup
default	12:57:12.388237-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device listeners to device 0
default	12:57:12.388245-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 0
default	12:57:12.388252-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 91
default	12:57:12.388490-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 91
default	12:57:12.388508-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:12.392944-0500	Nexy	[0x91aba1540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	12:57:12.393893-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	12:57:12.394114-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:12.395674-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.3, subject=com.nexy.assistant,
default	12:57:12.395814-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:12.395828-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:12.395838-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:12.395859-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:12.396815-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257300 at /Applications/Nexy.app
default	12:57:12.399025-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:12.399605-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:12.414508-0500	Nexy	[0x91aba1540] invalidated after the last release of the connection object
default	12:57:12.414635-0500	Nexy	[0x91aba1540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	12:57:12.415154-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	12:57:12.415327-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:12.416416-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.4, subject=com.nexy.assistant,
default	12:57:12.417104-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257300 at /Applications/Nexy.app
default	12:57:12.430826-0500	Nexy	[0x91aba1540] invalidated after the last release of the connection object
default	12:57:12.430907-0500	Nexy	[0x91aba1540] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	12:57:12.431020-0500	Nexy	[0x91aba1540] invalidated after the last release of the connection object
default	12:57:12.432539-0500	Nexy	[0x91aba1400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:57:12.433090-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:12.434182-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.5, subject=com.nexy.assistant,
default	12:57:12.434876-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257300 at /Applications/Nexy.app
default	12:57:12.448299-0500	Nexy	[0x91aba1400] invalidated after the last release of the connection object
default	12:57:12.536050-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257c00 at /Applications/Nexy.app
default	12:57:12.551908-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	12:57:12.563858-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257900 at /Applications/Nexy.app
default	12:57:12.570252-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	12:57:14.722605-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:14.722687-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:14.722703-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:14.723010-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:14.723032-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:14.740382-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:57:14.740502-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:57:14.741074-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:14.741378-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:57:14.741492-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:57:14.743992-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:14.744080-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:14.748215-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:14.748369-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:57:14.748472-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:57:14.767266-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
error	12:57:14.902693-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
default	12:57:17.339055-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	12:57:18.654077-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	12:57:20.574924-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256a00 at /Applications/Nexy.app
default	12:57:20.594794-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	12:57:20.604456-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	12:57:20.643668-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:20.649980-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:20.674520-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	12:57:20.677825-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	12:57:22.682296-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
error	12:57:24.315231-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:24.433267-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	12:57:24.433422-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	12:57:27.728123-0500	Nexy	[0x91aba1680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:57:27.728946-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:27.731630-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.6, subject=com.nexy.assistant,
default	12:57:27.733266-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257900 at /Applications/Nexy.app
default	12:57:27.755103-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[36743], responsiblePID[36743], responsiblePath: /Applications/Nexy.app to UID: 501
default	12:57:27.755491-0500	Nexy	[0x91aba1680] invalidated after the last release of the connection object
error	12:57:30.802838-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:30.805836-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:30.806833-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	12:57:30.807261-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
default	12:57:34.470398-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:34.491148-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254000 at /Applications/Nexy.app
default	12:57:34.502582-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	12:57:34.654052-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:34.654580-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	12:57:34.656074-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	12:57:34.656423-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	12:57:34.690007-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	12:57:34.691709-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	12:57:37.848529-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257900 at /Applications/Nexy.app
default	12:57:42.891592-0500	Nexy	[0x91aba1680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:57:42.893465-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:42.895268-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.7, subject=com.nexy.assistant,
default	12:57:42.896410-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:42.924494-0500	Nexy	[0x91aba1680] invalidated after the last release of the connection object
default	12:57:43.331949-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x91bdece40) Selecting device 85 from constructor
default	12:57:43.331967-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:43.331974-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:43.331980-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x91bdece40) nothing to teardown
default	12:57:43.331985-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 85
default	12:57:43.332109-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:43.332273-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xc for device 85
default	12:57:43.332433-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 85
default	12:57:43.332663-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 85
default	12:57:43.332674-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:43.332794-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:43.332806-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:43.332813-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:43.332822-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:43.332833-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:43.332966-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:43.332978-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:43.332984-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:43.332990-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device listeners from device 0
default	12:57:43.332995-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 0
default	12:57:43.333002-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:43.333022-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:57:43.333086-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x91bdece40) caller requesting device change from 85 to 91
default	12:57:43.333096-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:43.333102-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:43.333107-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 85
default	12:57:43.333113-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xc for device 85
default	12:57:43.333142-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	12:57:43.333199-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:43.333301-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 91
default	12:57:43.333398-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 91 (Input:Yes | Output:No): true
default	12:57:43.335459-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8317, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.337549-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8317, subject=com.nexy.assistant,
default	12:57:43.338460-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.363931-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xb for device 91
default	12:57:43.364140-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 91
default	12:57:43.364356-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 91
default	12:57:43.364370-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:43.364387-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	12:57:43.364399-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:43.364552-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	12:57:43.364561-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	12:57:43.364566-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	12:57:43.364686-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:43.364698-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:43.364702-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:43.364707-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 85
default	12:57:43.364936-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 85
default	12:57:43.364949-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:43.364973-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	12:57:43.365638-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:43.366950-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8318, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.368372-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8318, subject=com.nexy.assistant,
default	12:57:43.369119-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.386035-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f7ccc0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	12:57:43.386287-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:43.387268-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8319, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.388241-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8319, subject=com.nexy.assistant,
default	12:57:43.388837-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.406718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8320, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.407834-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8320, subject=com.nexy.assistant,
default	12:57:43.408494-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.425525-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:57:43.425700-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	12:57:43.427521-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	12:57:43.429141-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:43.429193-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:43.429542-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:43.429614-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:43.429918-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:43.429968-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:43.430649-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:43.431091-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:43.431159-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:43.431205-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:43.431246-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:43.431386-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:43.434885-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:43.435391-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937930 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:43.435544-0500	runningboardd	Assertion 394-328-937930 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:43.435724-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:43.436088-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:43.436567-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:43.436618-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:43.436674-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:43.436996-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:43.437350-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:43.437362-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:43.437376-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:43.437994-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	12:57:43.438102-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:57:43.438146-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f47f1, Nexy(36743), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	12:57:43.438179-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:43.438256-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47f1, Nexy(36743), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	12:57:43.438304-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.438343-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:43.438452-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:43.438605-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	12:57:43.438638-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 starting recording
default	12:57:43.438848-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:43.438932-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.438935-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.438980-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:43.439076-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:43.439080-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.439426-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	12:57:43.439436-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:43.439629-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8321, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.440074-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:57:43.447504-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:43.447527-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:43.447532-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:43.448057-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:43.464585-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:43.465259-0500	runningboardd	Invalidating assertion 394-328-937930 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:43.466450-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8321, subject=com.nexy.assistant,
default	12:57:43.466510-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:43.466820-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:57:43.466840-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:57:43.468164-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.468514-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:43.468538-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:43.468635-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:43.472259-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:43.473177-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:43.474236-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:43.474253-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:43.474255-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:43.474267-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:43.474276-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:43.474287-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:43.474524-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:57:43.474533-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:57:43.474548-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:43.474644-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:43.474694-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:43.474744-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:43.474780-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:43.474813-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:43.474848-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:43.474881-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:43.474919-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:43.474957-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:43.475013-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:43.475069-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:43.475111-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:43.476645-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:43.476942-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:43.477051-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.477508-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.478688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.478724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.478740-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.478776-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.478818-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.478826-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.479077-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.517709-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:57:43.517878-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	12:57:43.525875-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:43.525888-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:43.525919-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:43.526361-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:57:43.526371-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:57:43.526384-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:43.526396-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:43.526957-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:43.526990-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:43.527113-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:43.533195-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.537286-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.538027-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.538044-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.538073-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.538081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.538093-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.538100-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.538746-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.558228-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 issue_detected_sample_time=2160.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	12:57:43.558245-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	12:57:43.558533-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:43.558598-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	12:57:43.571415-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:43.571427-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:43.571438-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:43.571456-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:43.574711-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:43.575357-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:43.621965-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	12:57:43.625190-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:43.625231-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:48500 called from <private>
default	12:57:43.625539-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:43.626980-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937933 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:43.627630-0500	runningboardd	Assertion 394-328-937933 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:43.628046-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:43.628065-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:43.628082-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:43.628175-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:43.628443-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:43.628457-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:43.629067-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:43.629195-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:43.629317-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:43.629333-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:43.629342-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:43.629369-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:43.629575-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:43.629585-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:43.629611-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:43.629641-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:43.629698-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:43.629739-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:43.629833-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:43.629888-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:57:43.630167-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.630176-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:43.630209-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.630263-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:43.630274-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:43.630367-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:43.630820-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:43.630897-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f7d1a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.630990-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:43.631165-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:43.631181-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:43.631189-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:43.631375-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:43.631382-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:57:43.631437-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:43.631457-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:43.631527-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.631673-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:43.631710-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:43.631741-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.631798-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:43.631829-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:43.632148-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:43.632328-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919f7d1a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:57:43.632355-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:43.632487-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:43.632502-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:43.632508-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:43.633930-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8323, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.635519-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8323, subject=com.nexy.assistant,
default	12:57:43.636276-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.636497-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:43.636847-0500	runningboardd	Invalidating assertion 394-328-937933 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:43.637096-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:43.638923-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:43.639000-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:43.639055-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.639211-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.640372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.640397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.640434-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.640467-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.640750-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.640778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.640950-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.657533-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937934 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:43.657624-0500	runningboardd	Assertion 394-328-937934 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:43.658915-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:57:43.662055-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:57:43.662105-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:57:43.664072-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:43.664133-0500	runningboardd	Invalidating assertion 394-328-937934 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:43.664201-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:43.664216-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:57:43.664222-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:57:43.665003-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:43.665182-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:43.665527-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:43.665545-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:57:43.665551-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:57:43.665904-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:43.667589-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8324, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:43.669037-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8324, subject=com.nexy.assistant,
default	12:57:43.669744-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:43.671173-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:43.671255-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:43.671310-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.671489-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.672609-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.672620-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.672650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.672689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.672698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.672707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.672926-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.692317-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937935 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:43.692593-0500	runningboardd	Assertion 394-328-937935 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:43.693321-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:57:43.701339-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:43.701383-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:43.701412-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.701597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701610-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701621-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.701627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701636-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.701642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.701657-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701679-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701687-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.701693-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.701700-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.701705-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.701773-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.702105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.702112-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.702119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.702126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.702132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.702137-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.702167-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	12:57:43.737355-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x91abf0630: iounit configuration changed > posting notification
default	12:57:43.785084-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	12:57:43.785345-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:57:43.785430-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:43.785480-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:43.785510-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:43.785556-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 stopping recording
default	12:57:43.785577-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:57:43.785579-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:57:43.785605-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:43.785643-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:43.785765-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:57:43.785779-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:43.785824-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:57:43.786039-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:43.786075-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.786117-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:43.786159-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:43.786191-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:57:43.786261-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.786287-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:57:43.786298-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:43.786308-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:57:43.787497-0500	runningboardd	Invalidating assertion 394-328-937935 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:43.789589-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:43.793447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.793461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.793473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.793482-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:43.793489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:43.793498-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:43.793592-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:43.886912-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x91bdece40) Selecting device 0 from destructor
default	12:57:43.886925-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:43.886935-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:43.886941-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 91
default	12:57:43.886949-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xb for device 91
default	12:57:43.886986-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	12:57:43.887026-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:43.887211-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x91bdece40) nothing to setup
default	12:57:43.887223-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device listeners to device 0
default	12:57:43.887228-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 0
default	12:57:43.887243-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 91
default	12:57:43.887496-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 91
default	12:57:43.887515-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:43.890976-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:43.890995-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:43.891005-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:43.891022-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:43.894161-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:43.894774-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:43.914942-0500	Nexy	[0x91aba1900] activating connection: mach=true listener=false peer=false name=com.apple.iconservices
default	12:57:43.916263-0500	Nexy	[0x91aba1a40] activating connection: mach=true listener=false peer=false name=com.apple.iconservices.store
default	12:57:43.919719-0500	Nexy	[0x91aba1b80] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	12:57:43.938165-0500	Nexy	[0x91aba2940] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:57:43.939022-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:57:43.940329-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.8, subject=com.nexy.assistant,
default	12:57:43.941119-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:43.961041-0500	Nexy	[0x91aba2940] invalidated after the last release of the connection object
default	12:57:43.961174-0500	Nexy	server port 0x00013d0f, session port 0x0000370f
default	12:57:43.961873-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9109, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:57:43.961895-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:57:43.962733-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9109, subject=com.nexy.assistant,
default	12:57:43.963371-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:43.981857-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9110, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:57:43.981884-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:57:43.982683-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9110, subject=com.nexy.assistant,
default	12:57:43.983325-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:44.025907-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x91bdece40) Selecting device 85 from constructor
default	12:57:44.025918-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:44.025923-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:44.025928-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x91bdece40) nothing to teardown
default	12:57:44.025932-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 85
default	12:57:44.026022-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:44.026127-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xd for device 85
default	12:57:44.026240-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 85
default	12:57:44.026416-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 85
default	12:57:44.026423-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:44.026496-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:44.026504-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:44.026509-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:57:44.026515-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:44.026520-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:44.026652-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:44.026664-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:44.026673-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:44.026676-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device listeners from device 0
default	12:57:44.026680-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 0
default	12:57:44.026685-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:44.026700-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:57:44.026778-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x91bdece40) caller requesting device change from 85 to 91
default	12:57:44.026787-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:44.026791-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:44.026794-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 85
default	12:57:44.026798-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xd for device 85
default	12:57:44.026815-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	12:57:44.026900-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:44.026988-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 91
default	12:57:44.027091-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 91 (Input:Yes | Output:No): true
default	12:57:44.028422-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8325, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:44.029918-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3DB2F586-E1EF-4C3D-8A35-ABC1E3846E8D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64810,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xa693dbc2 tp_proto=0x06"
default	12:57:44.029961-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64810<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825374 t_state: SYN_SENT process: Nexy:36743 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8d2f7054
default	12:57:44.030005-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8325, subject=com.nexy.assistant,
default	12:57:44.030261-0500	kernel	tcp connected: [<IPv4-redacted>:64810<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825374 t_state: ESTABLISHED process: Nexy:36743 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8d2f7054
default	12:57:44.030512-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64810<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825374 t_state: FIN_WAIT_1 process: Nexy:36743 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8d2f7054
default	12:57:44.030522-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64810<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825374 t_state: FIN_WAIT_1 process: Nexy:36743 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	12:57:44.030680-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 86CFE4F2-93A1-4A1D-9131-2BAE54128972 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64811,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x623c8968 tp_proto=0x06"
default	12:57:44.030692-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64811<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825375 t_state: SYN_SENT process: Nexy:36743 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb9bdaa4a
default	12:57:44.030787-0500	kernel	tcp connected: [<IPv4-redacted>:64811<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825375 t_state: ESTABLISHED process: Nexy:36743 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb9bdaa4a
default	12:57:44.030879-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:44.030919-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64811<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825375 t_state: FIN_WAIT_1 process: Nexy:36743 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb9bdaa4a
default	12:57:44.030926-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64811<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4825375 t_state: FIN_WAIT_1 process: Nexy:36743 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	12:57:44.047873-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xc for device 91
default	12:57:44.048010-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 91
default	12:57:44.048191-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 91
default	12:57:44.048199-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:57:44.048207-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	12:57:44.048216-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:44.048330-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	12:57:44.048337-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	12:57:44.048341-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	12:57:44.048450-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:44.048463-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:44.048469-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:44.048474-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 85
default	12:57:44.048628-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 85
default	12:57:44.048635-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:44.048648-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	12:57:44.048955-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:44.049954-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8326, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:44.050949-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8326, subject=com.nexy.assistant,
default	12:57:44.051500-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:44.067250-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x919fb1680, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	12:57:44.067455-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:57:44.068402-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8327, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:44.069427-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8327, subject=com.nexy.assistant,
default	12:57:44.070029-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:44.087753-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8328, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:57:44.088752-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8328, subject=com.nexy.assistant,
default	12:57:44.089353-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:57:44.109358-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	12:57:44.110579-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	12:57:44.110645-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:57:44.110667-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f47f1, Nexy(36743), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	12:57:44.110692-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:44.112384-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47f1, Nexy(36743), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	12:57:44.112406-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:44.112524-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:44.112550-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.112679-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	12:57:44.112690-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 starting recording
default	12:57:44.112768-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.112776-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.112797-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.112829-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:44.112869-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-937941 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:44.112900-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:44.112940-0500	runningboardd	Assertion 394-328-937941 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:44.112961-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:44.113025-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.113163-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.113571-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:44.113611-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:44.113673-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:44.119455-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:57:44.119513-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:57:44.119550-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:44.119909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.119921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.119932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.119940-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.119946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.119954-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:44.119966-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.119996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.120050-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.120089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.120115-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.120187-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:44.120444-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:44.120580-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.120632-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.120675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.120680-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	12:57:44.120769-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.120872-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.120913-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:44.154082-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36950.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=36950, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	12:57:44.176682-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9112, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=36950, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:57:44.177618-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9112, subject=com.nexy.assistant,
default	12:57:44.178311-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:44.199541-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	12:57:44.199875-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:57:44.199980-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:44.200022-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:57:44.200048-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:57:44.200097-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 stopping recording
default	12:57:44.200114-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:57:44.200119-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:57:44.200150-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:44.200180-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:44.200289-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:57:44.200304-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:44.200381-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:57:44.200601-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:44.200635-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.200671-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:44.200710-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:57:44.200738-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:57:44.200790-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.200835-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:57:44.200845-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:57:44.200856-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:57:44.202886-0500	runningboardd	Invalidating assertion 394-328-937941 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:57:44.205295-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:57:44.208026-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:44.208039-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:44.208049-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:44.208069-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:44.208303-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.208313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.208324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.208332-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:57:44.208338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:57:44.208364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:57:44.208657-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:57:44.304848-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x91bdece40) Selecting device 0 from destructor
default	12:57:44.304862-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:57:44.304867-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:57:44.304872-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 91
default	12:57:44.304879-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xc for device 91
default	12:57:44.304912-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	12:57:44.304945-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:57:44.305089-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x91bdece40) nothing to setup
default	12:57:44.305105-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device listeners to device 0
default	12:57:44.305110-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 0
default	12:57:44.305115-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 91
default	12:57:44.305319-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 91
default	12:57:44.305332-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:57:44.397706-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 36951: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d2cf2a00 };
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
default	12:57:44.409261-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	12:57:44.418808-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170000 at /Applications/Nexy.app
default	12:57:44.440753-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	12:57:45.034920-0500	Nexy	[0x91aba2d00] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	12:57:45.043143-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 36743
default	12:57:45.046457-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	12:57:45.052997-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x91aa50780
 (
    "<NSAquaAppearance: 0x91aa50500>",
    "<NSSystemAppearance: 0x91aa50820>"
)>
default	12:57:45.057878-0500	Nexy	[0x91aba3200] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	12:57:45.058499-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	12:57:45.058818-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	12:57:45.058831-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	12:57:45.058861-0500	Nexy	[0x91aba3340] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	12:57:45.058881-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	12:57:45.058944-0500	Nexy	[0x91aba35c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	12:57:45.059025-0500	Nexy	FBSWorkspace registering source: <private>
default	12:57:45.059772-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	12:57:45.060178-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	12:57:45.060261-0500	Nexy	<FBSWorkspaceScenesClient:0x91aa53480 <private>> attempting immediate handshake from activate
default	12:57:45.060417-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.060605-0500	Nexy	<FBSWorkspaceScenesClient:0x91aa53480 <private>> sent handshake
default	12:57:45.061163-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	12:57:45.061172-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.061955-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	12:57:45.062009-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Registering event dispatcher at init
default	12:57:45.062453-0500	ControlCenter	Created <FBWorkspace: 0x8e816eda0; <FBApplicationProcess: 0x8e4145080; app<application.com.nexy.assistant.41202063.41202072>:36743(v2ACE0B)>>
default	12:57:45.062485-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.41202063.41202072> with intent background
default	12:57:45.062908-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41202063.41202072(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	12:57:45.063046-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41202063.41202072(501)> from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-937954 target:app<application.com.nexy.assistant.41202063.41202072(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	12:57:45.063209-0500	runningboardd	Assertion 394-638-937954 (target:app<application.com.nexy.assistant.41202063.41202072(501)>) will be created as active
default	12:57:45.063241-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-937954 target:app<application.com.nexy.assistant.41202063.41202072(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.063570-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.063580-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.063817-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	12:57:45.064143-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.064203-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.065275-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	12:57:45.066123-0500	Nexy	Requesting scene <FBSScene: 0x91aa53980; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1> from com.apple.controlcenter.statusitems
default	12:57:45.067785-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.068511-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.068919-0500	Nexy	Request for <FBSScene: 0x91aa53980; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1> complete!
default	12:57:45.069015-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	12:57:45.070324-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	12:57:45.070617-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	12:57:45.070851-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	12:57:45.070888-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	12:57:45.071170-0500	Nexy	Requesting scene <FBSScene: 0x91aa535c0; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	12:57:45.071367-0500	Nexy	Request for <FBSScene: 0x91aa535c0; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView> complete!
default	12:57:45.072155-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Bootstrap success!
default	12:57:45.072659-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Setting process visibility to: Background
default	12:57:45.072727-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] No launch watchdog for this process, dropping initial assertion in 2.0s
default	12:57:45.073338-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-638-937955 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	12:57:45.073425-0500	runningboardd	Assertion 394-638-937955 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.073826-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.073837-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.073846-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.073885-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.075695-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.075716-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	12:57:45.077208-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.077708-0500	ControlCenter	Adding: <FBApplicationProcess: 0x8e4145080; app<application.com.nexy.assistant.41202063.41202072>:36743(v2ACE0B)>
default	12:57:45.077862-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.078217-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Connection established.
default	12:57:45.078296-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x8e7f68850>
default	12:57:45.078308-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.078319-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Connection to remote process established!
default	12:57:45.079370-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.079387-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	12:57:45.079488-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	12:57:45.085382-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.085410-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e4145080; app<application.com.nexy.assistant.41202063.41202072>:36743(v2ACE0B)>
default	12:57:45.085583-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Registered new scene: <FBWorkspaceScene: 0x8e4ae33c0; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1> (fromRemnant = 0)
default	12:57:45.085628-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace interruption policy did change: reconnect
default	12:57:45.085900-0500	ControlCenter	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1] Client process connected: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.085903-0500	Nexy	Request for <FBSScene: 0x91aa53980; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1> complete!
default	12:57:45.086050-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-638-937956 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	12:57:45.086168-0500	runningboardd	Assertion 394-638-937956 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as inactive as originator process has not exited
default	12:57:45.086638-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-937957 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:45.086747-0500	runningboardd	Assertion 394-638-937957 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.086827-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.086844-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e4145080; app<application.com.nexy.assistant.41202063.41202072>:36743(v2ACE0B)>
default	12:57:45.086853-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:45.086914-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Registered new scene: <FBWorkspaceScene: 0x8e4ae0300; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	12:57:45.087049-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.087090-0500	Nexy	Request for <FBSScene: 0x91aa535c0; com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView> complete!
default	12:57:45.087093-0500	ControlCenter	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.087096-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.087187-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.087321-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.087646-0500	Nexy	<FBSWorkspaceScenesClient:0x91aa53480 <private>> Reconnecting scene com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1
default	12:57:45.087965-0500	Nexy	<FBSWorkspaceScenesClient:0x91aa53480 <private>> Reconnecting scene com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView
default	12:57:45.090711-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.091265-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.091468-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.093753-0500	Nexy	Registering for test daemon availability notify post.
default	12:57:45.093951-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	12:57:45.094058-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	12:57:45.094161-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	12:57:45.095733-0500	Nexy	[0x91aba3840] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	12:57:45.103971-0500	Nexy	[0x91aba03c0] Connection returned listener port: 0x4e03
default	12:57:45.104553-0500	Nexy	SignalReady: pid=36743 asn=0x0-0x148c48b
default	12:57:45.105290-0500	Nexy	SIGNAL: pid=36743 asn=0x0x-0x148c48b
default	12:57:45.106240-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	12:57:45.109169-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257900 at /Applications/Nexy.app
default	12:57:45.123574-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.131570-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.134788-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	12:57:45.134799-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	12:57:45.134824-0500	Nexy	[0x91aba2940] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	12:57:45.134960-0500	Nexy	[0x91aba2940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	12:57:45.136323-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	12:57:45.142224-0500	Nexy	[C:2] Alloc <private>
default	12:57:45.142261-0500	Nexy	[0x91aba2940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	12:57:45.144180-0500	WindowManager	Connection activated | (36743) Nexy
default	12:57:45.144624-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937958 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.144711-0500	runningboardd	Assertion 394-36743-937958 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.145149-0500	runningboardd	Invalidating assertion 394-36743-937958 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.145231-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.145256-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.145268-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.145277-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937959 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.145376-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.145390-0500	runningboardd	Assertion 394-36743-937959 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.145806-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-36743). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	12:57:45.147505-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-36743)
default	12:57:45.148144-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(60486BE5, (bid:com.nexy.assistant-Item-0-36743)) for (bid:com.nexy.assistant-Item-0-36743)
default	12:57:45.148597-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.148853-0500	runningboardd	Invalidating assertion 394-36743-937959 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.148986-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937960 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.149043-0500	runningboardd	Assertion 394-36743-937960 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.149143-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-36743)]
default	12:57:45.149173-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.149352-0500	runningboardd	Invalidating assertion 394-36743-937960 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.149451-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.149535-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937961 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.149605-0500	runningboardd	Assertion 394-36743-937961 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.149868-0500	runningboardd	Invalidating assertion 394-36743-937961 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.149960-0500	ControlCenter	Created instance DisplayableId(60E37410) in .menuBar for DisplayableAppStatusItemType(60486BE5, (bid:com.nexy.assistant-Item-0-36743)) .menuBar
default	12:57:45.150052-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937962 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.150099-0500	runningboardd	Assertion 394-36743-937962 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.150312-0500	runningboardd	Invalidating assertion 394-36743-937962 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.150439-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937963 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.150487-0500	runningboardd	Assertion 394-36743-937963 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.150682-0500	runningboardd	Invalidating assertion 394-36743-937963 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.150790-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937964 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.150829-0500	runningboardd	Assertion 394-36743-937964 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.151050-0500	runningboardd	Invalidating assertion 394-36743-937964 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.151238-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937965 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.151282-0500	runningboardd	Assertion 394-36743-937965 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.151529-0500	runningboardd	Invalidating assertion 394-36743-937965 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.151735-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937966 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.151778-0500	runningboardd	Assertion 394-36743-937966 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.152009-0500	runningboardd	Invalidating assertion 394-36743-937966 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.152148-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-937967 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:45.152196-0500	runningboardd	Assertion 394-36743-937967 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.152411-0500	runningboardd	Invalidating assertion 394-36743-937967 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:57:45.158396-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.159136-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.163079-0500	ControlCenter	Created ephemaral instance DisplayableId(60E37410) for (bid:com.nexy.assistant-Item-0-36743) with positioning .ephemeral
default	12:57:45.167537-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	12:57:45.174921-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.175565-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.176009-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1] Sending action(s) in update: NSSceneFenceAction
default	12:57:45.248090-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.248101-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.248111-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.248130-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.251362-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.251955-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.252007-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.273551-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	12:57:45.276171-0500	Nexy	Start service name com.apple.spotlightknowledged
default	12:57:45.277219-0500	Nexy	[GMS] availability notification token 83
default	12:57:45.398560-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:45.398729-0500	runningboardd	Invalidating assertion 394-638-937957 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:45.504918-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.504935-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.504950-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.504978-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.508495-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.509079-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.509190-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.624294-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-937971 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:45.624402-0500	runningboardd	Assertion 394-387-937971 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:45.624825-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:45.624835-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:45.624845-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:45.624871-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:45.628660-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:45.629163-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:45.629232-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:46.086853-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170900 at /Applications/Nexy.app
default	12:57:46.092784-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	12:57:46.094748-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	12:57:46.422364-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:46.422661-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:46.422688-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:46.425230-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:46.425271-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:46.425281-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:46.426970-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:46.426994-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:57:46.427176-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:57:46.427227-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48500 called from <private>
default	12:57:46.427238-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:57:46.427258-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:57:46.442107-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:57:46.442177-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:57:46.443869-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:46.443927-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:57:46.443937-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:57:46.454511-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:46.454569-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:46.455113-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:46.459805-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:57:46.459861-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:57:46.459877-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:57:46.459892-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:57:46.459901-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:46.459907-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:46.459913-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:46.459944-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:46.460515-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:46.460815-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:46.460840-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:57:46.460855-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:46.460863-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:46.460874-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:57:46.460880-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48500 called from <private>
default	12:57:46.460906-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:46.461221-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:57:46.461358-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:57:46.461595-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:57:46.462028-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:46.462039-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:46.462166-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:46.462306-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:57:46.462455-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:57:46.463371-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:46.463644-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:57:46.463654-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:57:46.463669-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:46.463677-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:46.464413-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:57:46.464659-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:57:46.465637-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:57:46.465919-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:57:46.465933-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:57:46.465981-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:57:46.465991-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:57:46.465997-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:46.466003-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:46.466011-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:57:46.466017-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:57:46.466022-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:57:46.466028-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:57:46.477793-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:46.477830-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:46.477984-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:57:46.481442-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:57:46.481714-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:46.481733-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:46.481780-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:57:46.481843-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:57:46.482028-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:57:46.482064-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:57:46.482688-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:46.482728-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:57:46.482948-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.482988-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:46.483048-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.483165-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:46.483226-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:46.484457-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd5c80, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.484540-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x91acd5c80: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:46.484591-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:46.484652-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:57:46.485111-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:46.485162-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:46.485272-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:46.485567-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:57:46.485601-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:57:46.485845-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.485872-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:57:46.485905-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.486035-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:57:46.486116-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:57:46.486830-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd5c80, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:46.486937-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x91acd5c80: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:46.487226-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:57:46.487552-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:57:46.487843-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:57:46.487878-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:57:46.488137-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:57:46.496249-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:57:46.496290-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:57:46.496448-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:57:46.496473-0500	Nexy	AudioConverter -> 0x91acd5c80: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:57:46.611861-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x91abf0630: iounit configuration changed > posting notification
default	12:57:47.154164-0500	runningboardd	Invalidating assertion 394-638-937954 (target:app<application.com.nexy.assistant.41202063.41202072(501)>) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:47.256308-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.41202063.41202072(501)>
default	12:57:47.257704-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:47.257740-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:47.257766-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:47.257817-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:47.263245-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:47.271789-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:47.272968-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:50.044574-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	12:57:53.781477-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9120, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:57:53.781511-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:57:53.783776-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9120, subject=com.nexy.assistant,
default	12:57:53.784981-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:57:55.057924-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938016 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:55.058048-0500	runningboardd	Assertion 394-638-938016 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:55.058144-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:55.058355-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:55.058366-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:55.058382-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:55.058442-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:55.061433-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:55.061875-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:55.064209-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:55.162193-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:55.162344-0500	runningboardd	Invalidating assertion 394-638-938016 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:55.273936-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:55.273956-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:55.273984-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:55.274032-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:55.278384-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:55.278656-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:55.279124-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:55.551203-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938037 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:55.551336-0500	runningboardd	Assertion 394-638-938037 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:55.551520-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:55.552305-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:55.552557-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:55.552679-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:55.555912-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:55.664343-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:55.664932-0500	runningboardd	Invalidating assertion 394-638-938037 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:55.775846-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:55.775859-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:55.775890-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:55.775942-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:55.779990-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:55.784502-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:55.785471-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:56.042208-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	12:57:56.474426-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938066 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:56.474586-0500	runningboardd	Assertion 394-638-938066 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:56.474807-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:56.646441-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:56.646687-0500	runningboardd	Invalidating assertion 394-638-938066 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:56.755444-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:56.755466-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:56.755495-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:56.755552-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:56.760663-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:56.767046-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:56.768657-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:57.042040-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938086 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:57.042545-0500	runningboardd	Assertion 394-638-938086 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:57.054337-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:57.055141-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:57.055293-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:57.055533-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:57.055968-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:57.063023-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:57.067677-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:57.154730-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:57.231362-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:57.232106-0500	runningboardd	Invalidating assertion 394-638-938086 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:57.330257-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:57.330287-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:57.330317-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:57.330522-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:57.342715-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:57.352948-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:57.368633-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.056973-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938114 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:59.057115-0500	runningboardd	Assertion 394-638-938114 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:59.057368-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:59.058098-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:59.058151-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:59.058187-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:59.058439-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:59.062228-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:59.066709-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.067224-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.162751-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:59.162857-0500	runningboardd	Invalidating assertion 394-638-938114 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:59.267533-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:59.267559-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:59.267585-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:59.267637-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:59.272008-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:59.272897-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.275399-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.345092-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938129 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:57:59.345200-0500	runningboardd	Assertion 394-638-938129 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:57:59.348074-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:57:59.348248-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:59.348258-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:59.348268-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:59.348294-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:59.351058-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:59.378415-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.379203-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.453689-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:57:59.453753-0500	runningboardd	Invalidating assertion 394-638-938129 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:57:59.538888-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:57:59.538898-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:57:59.538925-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:57:59.538966-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:57:59.543343-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:57:59.543540-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:57:59.544259-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:02.031050-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-938179 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	12:58:02.031167-0500	runningboardd	Assertion 394-638-938179 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:02.031280-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	12:58:02.032252-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:02.032309-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:02.032365-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:02.033287-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:02.036847-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:02.040769-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:02.041121-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:02.136976-0500	ControlCenter	[app<application.com.nexy.assistant.41202063.41202072>:36743] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	12:58:02.137204-0500	runningboardd	Invalidating assertion 394-638-938179 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	12:58:02.241175-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:02.241193-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:02.241214-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:02.241269-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:02.245083-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:02.245306-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:02.245946-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:18.078108-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9128, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:58:18.078181-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:58:18.081785-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9128, subject=com.nexy.assistant,
default	12:58:18.083794-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:58:18.887926-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x91abf0630: start, was running 0
default	12:58:18.888825-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938246 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:18.892993-0500	runningboardd	Assertion 394-36743-938246 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:18.893824-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:18.894023-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:18.894469-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:18.894491-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938247 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:18.894546-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:18.894653-0500	runningboardd	Assertion 394-328-938247 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:18.898159-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:18.898490-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:18.898508-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:18.898523-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:18.898555-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:18.898704-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:18.898827-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:18.901297-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:18.901699-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:18.901784-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:19.254396-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:19.256211-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:58:19.256361-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:58:19.256405-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f47f1, Nexy(36743), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	12:58:19.256438-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:58:19.256484-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47f1, Nexy(36743), 'prim'', AudioCategory changed to 'MediaPlayback'
default	12:58:19.256521-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.256560-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:58:19.256592-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 2032 starting playing
default	12:58:19.256752-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.256772-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:58:19.256807-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.256829-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:58:19.256933-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:58:19.256987-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	12:58:19.257083-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	12:58:19.257141-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f47f1 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":36743}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47f1, sessionType: 'prim', isRecording: false }, 
]
default	12:58:19.257425-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:58:19.257441-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:58:19.257460-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:58:19.257678-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.257798-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.257826-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.257841-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	12:58:19.257848-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	12:58:19.257858-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	12:58:19.257971-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	12:58:19.258057-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	12:58:19.695044-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x91bdece40) Selecting device 85 from constructor
default	12:58:19.695054-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:58:19.695060-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:58:19.695065-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x91bdece40) nothing to teardown
default	12:58:19.695070-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 85
default	12:58:19.695147-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 85 (Input:No | Output:Yes): true
default	12:58:19.695588-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xe for device 85
default	12:58:19.695864-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 85
default	12:58:19.696033-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 85
default	12:58:19.696038-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:58:19.696105-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:58:19.696115-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:58:19.696120-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:58:19.696126-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:58:19.696135-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:58:19.696221-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:58:19.696230-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:58:19.696240-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:58:19.696245-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device listeners from device 0
default	12:58:19.696250-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 0
default	12:58:19.696254-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:58:19.696270-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:58:19.696319-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x91bdece40) caller requesting device change from 85 to 91
default	12:58:19.696326-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:58:19.696331-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:58:19.696333-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 85
default	12:58:19.696336-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xe for device 85
default	12:58:19.696363-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xe}
default	12:58:19.696584-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:58:19.697160-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x91bdece40) connecting device 91
default	12:58:19.697252-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdece40) Device ID: 91 (Input:Yes | Output:No): true
default	12:58:19.699135-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8329, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:58:19.700934-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8329, subject=com.nexy.assistant,
default	12:58:19.701646-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:19.710916-0500	Nexy	[0x91aba1540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:58:19.711457-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=36743.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:58:19.712450-0500	tccd	AUTHREQ_SUBJECT: msgID=36743.9, subject=com.nexy.assistant,
default	12:58:19.713104-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:58:19.719814-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x91bdece40) created ioproc 0xd for device 91
default	12:58:19.719935-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 7 device listeners to device 91
default	12:58:19.720108-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 91
default	12:58:19.720117-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdece40)
default	12:58:19.720124-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	12:58:19.720134-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:58:19.720253-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	12:58:19.720262-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	12:58:19.720267-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	12:58:19.720352-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:58:19.720360-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdece40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:58:19.720366-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:58:19.720370-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 85
default	12:58:19.720504-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 85
default	12:58:19.720510-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:58:19.721141-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:58:19.722011-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8330, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:58:19.722965-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8330, subject=com.nexy.assistant,
default	12:58:19.723531-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:19.733432-0500	Nexy	[0x91aba1540] invalidated after the last release of the connection object
default	12:58:19.734769-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	12:58:19.737353-0500	Nexy	[0x91aba1540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	12:58:19.737468-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	12:58:19.737972-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	12:58:19.738945-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:58:19.739818-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8331, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:58:19.740757-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8331, subject=com.nexy.assistant,
default	12:58:19.741305-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:19.748331-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23008.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=23008, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	12:58:19.748356-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=23008, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:58:19.749195-0500	tccd	AUTHREQ_SUBJECT: msgID=23008.2, subject=com.nexy.assistant,
default	12:58:19.749815-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:58:19.758373-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8332, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:58:19.759349-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8332, subject=com.nexy.assistant,
default	12:58:19.759917-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:19.776571-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:58:19.776724-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	12:58:19.776973-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.9132, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:58:19.777002-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:58:19.778198-0500	tccd	AUTHREQ_SUBJECT: msgID=387.9132, subject=com.nexy.assistant,
default	12:58:19.778214-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:58:19.778222-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xd}
default	12:58:19.779016-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:58:19.779198-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:58:19.779223-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:58:19.779233-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:58:19.779462-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:19.779474-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:19.779480-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:19.779499-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:19.779514-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:58:19.779608-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	12:58:19.781816-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:58:19.781977-0500	runningboardd	Invalidating assertion 394-36743-938246 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:19.782377-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:19.782638-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:19.782665-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:58:19.782695-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:58:19.783065-0500	runningboardd	Invalidating assertion 394-328-938247 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:19.786668-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:58:19.787166-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:58:19.788635-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:58:19.788702-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:58:19.788774-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:58:19.788850-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:58:19.789016-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:58:19.789068-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:58:19.789149-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48500 called from <private>
default	12:58:19.789200-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48500 called from <private>
default	12:58:19.789252-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:58:19.789283-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:58:19.789330-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:58:19.789891-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938253 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:19.789995-0500	runningboardd	Assertion 394-36743-938253 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:19.793478-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8333, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=36743, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:58:19.799572-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:58:19.799591-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:58:19.799712-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:19.799740-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:19.799746-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:19.803323-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:19.803342-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:19.803706-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8333, subject=com.nexy.assistant,
default	12:58:19.805459-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:19.806850-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:19.807871-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:19.807892-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:58:19.807929-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:19.807936-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:19.807955-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:58:19.807974-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:58:19.807981-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:58:19.810120-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:58:19.810131-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:58:19.810146-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:19.810498-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:19.810621-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:58:19.810995-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:58:19.812814-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.813199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.813250-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.813333-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.813406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.813415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:19.813728-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
error	12:58:19.815041-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	12:58:19.815051-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48499 called from <private>
default	12:58:19.815057-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:58:19.815063-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:19.815447-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:58:19.816107-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:58:19.817116-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:19.817131-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:19.817244-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:19.817313-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:19.817346-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:19.817354-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:58:19.817404-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:58:19.817466-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:58:19.817503-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:58:19.817547-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:58:19.817574-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:58:19.817686-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:58:19.817714-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:58:19.817779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:58:19.817812-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:58:19.817845-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:19.817873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:19.817898-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:58:19.817905-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:58:19.817945-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:19.817975-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:19.819968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.820095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.822071-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:19.826602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.826612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.826625-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.826711-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.826946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.827060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:19.827630-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:19.828773-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:19.837060-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	12:58:19.846254-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:19.857794-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	12:58:19.857913-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:58:19.857945-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:58:19.857978-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:58:19.859991-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.860050-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.860100-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:19.860173-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	12:58:19.861716-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	12:58:19.872222-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:19.872801-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	12:58:19.873975-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	12:58:19.873996-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:58:19.876969-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:58:19.877109-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:19.877187-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:19.877274-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:19.877382-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:58:19.877545-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:19.878057-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:19.878185-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:19.878307-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	12:58:19.878412-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	12:58:19.878499-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	12:58:19.878566-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:19.878695-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
error	12:58:19.878748-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	12:58:19.878889-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:58:19.878948-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:19.879000-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:58:19.879178-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:58:19.879192-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:19.879240-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:58:19.881422-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:19.882800-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	12:58:19.896652-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:19.896720-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	12:58:19.896779-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	12:58:19.897011-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.897026-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.897037-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.897042-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:19.897068-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:19.897075-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:19.897171-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:19.905059-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:19.911592-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:19.911689-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	12:58:19.911747-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	12:58:19.936312-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 issue_detected_sample_time=4320.000000 ] -- [ rms:[-119.941589], peaks:[-109.947678] ]
default	12:58:19.936345-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.943638], peaks:[-21.081259] ]
default	12:58:19.936661-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	12:58:19.936733-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5800] Created node ADM::com.nexy.assistant_48500.48403.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	12:58:19.945204-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	12:58:19.972505-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:19.972609-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:19.978404-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x91abf0630: iounit configuration changed > posting notification
default	12:58:19.996242-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:19.996256-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:19.996268-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:19.996290-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:20.999593-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:20.000066-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.002571-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.023065-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	12:58:20.029648-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:58:20.029685-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48500 called from <private>
default	12:58:20.030468-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:58:20.032299-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:58:20.032313-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:58:20.032521-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938257 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:20.032663-0500	runningboardd	Assertion 394-328-938257 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:20.033041-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:20.033128-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:20.033179-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:20.033252-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:20.044070-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8335, subject=com.nexy.assistant,
default	12:58:20.046312-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:20.058334-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.065234-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.065341-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	12:58:20.065402-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	12:58:20.065943-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.065958-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.065973-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.065983-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.065992-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.066000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:20.066020-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.066204-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.066278-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:20.066323-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066334-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	12:58:20.066359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066509-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.066519-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.066531-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.066540-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:20.066669-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:20.075278-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.075390-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	12:58:20.075453-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	12:58:20.075472-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:58:20.104506-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:58:20.105223-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:58:20.105479-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.105485-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48500 called from <private>
default	12:58:20.105519-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48500 called from <private>
default	12:58:20.105542-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:58:20.105868-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.105969-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.106148-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.106235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.106359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.106468-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:20.107014-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:20.115117-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719170300 at /Applications/Nexy.app
default	12:58:20.126543-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.126704-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	12:58:20.126804-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	12:58:20.135685-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.135744-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.135770-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.135871-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.136003-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.136051-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:20.140773-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.140836-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	12:58:20.140883-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	12:58:20.140906-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:58:20.146756-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:20.146781-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:20.146805-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:20.146842-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:20.150820-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:20.151380-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.151629-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.157612-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938261 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:20.157721-0500	runningboardd	Assertion 394-328-938261 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:20.161336-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:20.161803-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48500 called from <private>
default	12:58:20.161988-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:20.162070-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:20.162295-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:20.184608-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:20.184756-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	12:58:20.184830-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	12:58:20.190737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.190772-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.190834-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:20.190920-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:20.257406-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:20.257720-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:21.651665-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	12:58:23.236146-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	12:58:23.236563-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:58:23.236800-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:58:23.236926-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:58:23.237016-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:58:23.237129-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	12:58:23.237132-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47f1, Nexy(36743), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2032 stopping recording
default	12:58:23.237185-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:58:23.237250-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:58:23.237324-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:58:23.237586-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:58:23.237608-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:58:23.237651-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:58:23.238147-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:23.238240-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.238331-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:23.238396-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:58:23.238451-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:58:23.238495-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.238627-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:58:23.238657-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.238682-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:58:23.243144-0500	runningboardd	Invalidating assertion 394-36743-938260 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:23.243380-0500	runningboardd	Invalidating assertion 394-328-938261 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:23.251512-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:58:23.251619-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	12:58:23.251682-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	12:58:23.251699-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:58:23.252238-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:23.252254-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:23.252266-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:23.252274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:58:23.252280-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:58:23.252288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:58:23.252391-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:58:23.340740-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x91bdece40) Selecting device 0 from destructor
default	12:58:23.340755-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x91bdece40)
default	12:58:23.340764-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x91bdece40) not already running
default	12:58:23.340770-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x91bdece40) disconnecting device 91
default	12:58:23.340778-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x91bdece40) destroying ioproc 0xd for device 91
default	12:58:23.340821-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	12:58:23.340864-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:58:23.341056-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x91bdece40) nothing to setup
default	12:58:23.341069-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device listeners to device 0
default	12:58:23.341075-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x91bdece40) adding 0 device delegate listeners to device 0
default	12:58:23.341083-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 7 device listeners from device 91
default	12:58:23.341329-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x91bdece40) removing 0 device delegate listeners from device 91
default	12:58:23.341344-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x91bdece40)
default	12:58:23.350419-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:23.350436-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:23.350449-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:23.350466-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:23.353792-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:23.363936-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:23.364186-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:23.393402-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	12:58:23.393584-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	12:58:23.395273-0500	Nexy	nw_path_libinfo_path_check [6915A283-C540-4D8E-82CE-EBEFC01D7BFF Hostname#8b565f35:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	12:58:23.395621-0500	mDNSResponder	[R373610] DNSServiceCreateConnection START PID[36743](Nexy)
default	12:58:23.395792-0500	mDNSResponder	[R373611] DNSServiceQueryRecord START -- qname: <mask.hash: '6PgfGVV2qVzTxZ5cKY0VKQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 36743 (Nexy), name hash: b360ab20
default	12:58:23.396413-0500	mDNSResponder	[R373612] DNSServiceQueryRecord START -- qname: <mask.hash: '6PgfGVV2qVzTxZ5cKY0VKQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 36743 (Nexy), name hash: b360ab20
default	12:58:23.432553-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A338107C-5B1C-4775-96A2-9AA6A098B7B8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64864,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x14a34b51 tp_proto=0x06"
default	12:58:23.432615-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64864<-><IPv4-redacted>:80] interface: utun4 (skipped: 10786)
so_gencnt: 4825767 t_state: SYN_SENT process: Nexy:36743 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbb8e90c8
default	12:58:23.433001-0500	kernel	tcp connected: [<IPv4-redacted>:64864<-><IPv4-redacted>:80] interface: utun4 (skipped: 10786)
so_gencnt: 4825767 t_state: ESTABLISHED process: Nexy:36743 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbb8e90c8
default	12:58:23.706828-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:64864<-><IPv4-redacted>:80] interface: utun4 (skipped: 10786)
so_gencnt: 4825767 t_state: LAST_ACK process: Nexy:36743 Duration: 0.274 sec Conn_Time: 0.001 sec bytes in/out: 380/58509 pkts in/out: 2/19 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.125 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbb8e90c8
default	12:58:23.706864-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64864<-><IPv4-redacted>:80] interface: utun4 (skipped: 10786)
so_gencnt: 4825767 t_state: LAST_ACK process: Nexy:36743 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	12:58:23.723376-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd6340, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:58:23.723459-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:23.724420-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:23.725915-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd6340, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:58:23.725980-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:58:23.725986-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x91acd6340: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:58:23.725996-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:58:23.726005-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:58:23.726022-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:23.727855-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd6340, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:58:23.727875-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x91acd6340: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:58:23.727880-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:58:23.727885-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:23.727893-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:58:23.727899-0500	Nexy	AudioConverter -> 0x91acd6340: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:58:23.728142-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x91acd6340: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:58:23.728197-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x91abf0630: start, was running 0
default	12:58:23.733855-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938280 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:23.734025-0500	runningboardd	Assertion 394-36743-938280 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:23.734538-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:23.736428-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:58:23.736574-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:58:23.736609-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f47f1, Nexy(36743), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	12:58:23.736643-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:58:23.736726-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.736730-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47f1, Nexy(36743), 'prim'', AudioCategory changed to 'MediaPlayback'
default	12:58:23.736788-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:58:23.736814-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 2032 starting playing
default	12:58:23.736954-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:58:23.737006-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:58:23.737077-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47f1, Nexy(36743), 'prim'', displayID:'com.nexy.assistant'}
default	12:58:23.737149-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	12:58:23.737165-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.737296-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f47f1 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":36743}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47f1, sessionType: 'prim', isRecording: false }, 
]
default	12:58:23.737329-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.737530-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	12:58:23.737857-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	12:58:23.738430-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.738575-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.738603-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	12:58:23.738616-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	12:58:23.738662-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	12:58:23.738676-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	12:58:23.738751-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	12:58:23.738828-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938281 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:23.738888-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:23.738934-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	12:58:23.738957-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:23.739003-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:23.739119-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:23.739128-0500	runningboardd	Assertion 394-328-938281 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:23.741133-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:58:23.741358-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:58:23.744098-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:23.744515-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:23.744560-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:23.744596-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:23.744663-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:23.744671-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:23.748554-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:23.748913-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:23.749053-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:23.749192-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:24.019045-0500	Nexy	[com.apple.controlcenter:26EFDCA6-64B8-4E8D-BFFD-BE70332EF6B1] Sending action(s) in update: NSSceneFenceAction
default	12:58:24.661927-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	12:58:25.366594-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:25.366621-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.366656-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:25.366663-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:25.366889-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:58:25.368073-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:25.368119-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48500)
default	12:58:25.368139-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48506 called from <private>
default	12:58:25.368148-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48506 called from <private>
default	12:58:25.368160-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48500 called from <private>
default	12:58:25.368170-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48500 called from <private>
default	12:58:25.371227-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:58:25.371522-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:25.372019-0500	runningboardd	Invalidating assertion 394-36743-938280 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:25.372090-0500	runningboardd	Invalidating assertion 394-328-938281 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:25.378174-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:25.378189-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:25.378199-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:25.378217-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:25.383160-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:25.389883-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:25.390331-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:25.396920-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:58:25.396944-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:58:25.398781-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:25.402493-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	12:58:25.402515-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:48499 called from <private>
default	12:58:25.402532-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:48499 called from <private>
default	12:58:25.402653-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	12:58:25.403321-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:25.403364-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:25.403382-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:25.403558-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48500)
default	12:58:25.403592-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48500 called from <private>
default	12:58:25.403599-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48500 called from <private>
default	12:58:25.403798-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:58:25.403825-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:58:25.403907-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48506 called from <private>
default	12:58:25.403954-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48506 called from <private>
default	12:58:25.403979-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:25.404017-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48506 called from <private>
default	12:58:25.404038-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:25.404050-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48506)
default	12:58:25.404064-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48506 called from <private>
default	12:58:25.404072-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48506 called from <private>
default	12:58:25.404099-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48506 called from <private>
default	12:58:25.404122-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:58:25.404160-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:58:25.404167-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:25.404262-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:25.404329-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:58:25.404365-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:58:25.404393-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48506 called from <private>
default	12:58:25.404421-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48506 called from <private>
default	12:58:25.420831-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:25.420850-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:25.420962-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.428395-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.428905-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:25.428917-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:25.430437-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:25.430454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:25.430537-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.433087-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.433495-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:25.433506-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:25.433551-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:25.433557-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:25.433564-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:25.433571-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:25.433602-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:25.433640-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.433648-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:25.433839-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:25.433967-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:25.434142-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:48499 called from <private>
default	12:58:25.434298-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.434322-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:48499 called from <private>
default	12:58:25.434571-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.434572-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:48499 called from <private>
default	12:58:25.434917-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.435007-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48506)
default	12:58:25.435198-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:48499 called from <private>
default	12:58:25.435468-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48506 called from <private>
default	12:58:25.435659-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:48499 called from <private>
default	12:58:25.435880-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:48506 called from <private>
default	12:58:25.436114-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:48499 called from <private>
default	12:58:25.436791-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:58:25.436829-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.437203-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:48499 called from <private>
default	12:58:25.437355-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:25.437408-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.437510-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:58:25.437618-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.437849-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(48499)
default	12:58:25.438241-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(48499)
default	12:58:25.439932-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938289 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:25.440010-0500	runningboardd	Assertion 394-36743-938289 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:25.440732-0500	runningboardd	Invalidating assertion 394-36743-938289 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:25.440855-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:25.440936-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938290 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:25.440956-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:25.441010-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:25.441045-0500	runningboardd	Assertion 394-36743-938290 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:25.441195-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:25.442832-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:58:25.442862-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:58:25.460969-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938291 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:25.461038-0500	runningboardd	Assertion 394-328-938291 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:25.461338-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:25.461354-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:25.461373-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:25.461407-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:25.488190-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:25.488301-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
error	12:58:25.851701-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	12:58:26.333142-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48499 called from <private>
default	12:58:26.333194-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48499 called from <private>
default	12:58:26.333213-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48499 called from <private>
default	12:58:26.335848-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:26.335896-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:58:26.337622-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd6340, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:58:26.337652-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:26.338521-0500	runningboardd	Invalidating assertion 394-36743-938290 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:26.338687-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938297 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:26.338757-0500	runningboardd	Assertion 394-36743-938297 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:26.339462-0500	runningboardd	Invalidating assertion 394-328-938291 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:26.339970-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938298 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:26.340090-0500	runningboardd	Assertion 394-328-938298 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
error	12:58:26.341764-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	12:58:26.929055-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48499 called from <private>
default	12:58:26.929090-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:48499 called from <private>
default	12:58:26.929120-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:58:26.929245-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:26.930469-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:48499 called from <private>
default	12:58:26.930500-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:48499 called from <private>
default	12:58:26.931212-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:58:26.931665-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:58:26.931689-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:58:26.931699-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:58:26.931796-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x91bdec040) Device ID: 85 (Input:No | Output:Yes): true
default	12:58:26.931834-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x91bdec040)
default	12:58:26.932414-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:58:26.932590-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:58:26.932634-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:58:26.932665-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:58:26.932699-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:58:26.932790-0500	runningboardd	Invalidating assertion 394-36743-938297 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:26.933073-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-36743-938301 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:58:26.933166-0500	runningboardd	Assertion 394-36743-938301 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
default	12:58:26.933693-0500	runningboardd	Invalidating assertion 394-328-938298 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:26.933952-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41202063.41202072(501)>:36743] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-938302 target:36743 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:58:26.934046-0500	runningboardd	Assertion 394-328-938302 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) will be created as active
error	12:58:26.935410-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	12:58:27.500017-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:48499 called from <private>
default	12:58:27.500967-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x91acd6340, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:58:27.501007-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:58:27.501154-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:27.501517-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:58:27.501661-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:58:27.501699-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x91bdec040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:58:27.501710-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:58:27.502625-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0x91abf0630: iounit configuration changed > stopping the engine
default	12:58:27.502636-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0x91abf0630: stop, was running 1
default	12:58:27.502645-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0x91abf0630: pause, was running 1
default	12:58:27.510266-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:58:27.510917-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47f1","name":"Nexy(36743)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:58:27.511167-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 2032 stopping playing
default	12:58:27.511245-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:58:27.511286-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:58:27.511584-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2032, PID = 36743, Name = sid:0x1f47f1, Nexy(36743), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:58:27.511944-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f47f1 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":36743}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47f1, sessionType: 'prim', isRecording: false }, 
]
default	12:58:27.512069-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:58:27.512088-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:58:27.513641-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:27.516935-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:27.517016-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:58:27.517036-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:58:27.517083-0500	runningboardd	Invalidating assertion 394-36743-938301 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [app<application.com.nexy.assistant.41202063.41202072(501)>:36743]
default	12:58:27.517184-0500	runningboardd	Invalidating assertion 394-328-938302 (target:[app<application.com.nexy.assistant.41202063.41202072(501)>:36743]) from originator [osservice<com.apple.powerd>:328]
default	12:58:27.621285-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring jetsam update because this process is not memory-managed
default	12:58:27.621298-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring suspend because this process is not lifecycle managed
default	12:58:27.621308-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring GPU update because this process is not GPU managed
default	12:58:27.621325-0500	runningboardd	[app<application.com.nexy.assistant.41202063.41202072(501)>:36743] Ignoring memory limit update because this process is not memory-managed
default	12:58:27.624228-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41202063.41202072(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:58:27.624593-0500	ControlCenter	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:27.624989-0500	gamepolicyd	Received state update for 36743 (app<application.com.nexy.assistant.41202063.41202072(501)>, running-active-NotVisible
default	12:58:27.637202-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x91abf0630: iounit configuration changed > posting notification
