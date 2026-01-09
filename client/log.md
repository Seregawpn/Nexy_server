default	12:29:29.834980-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	12:29:29.835129-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	12:29:29.836671-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	12:29:29.880604-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] is not RunningBoard jetsam managed.
default	12:29:29.880619-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] This process will not be managed.
default	12:29:29.880630-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:29.880774-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41170369.41170378(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:29:29.881400-0500	gamepolicyd	Hit the server for a process handle 11f3363800004a5b that resolved to: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:29.881434-0500	gamepolicyd	Received state update for 19035 (app<application.com.nexy.assistant.41170369.41170378(501)>, running-active-NotVisible
default	12:29:29.884674-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:29.884737-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41170369.41170378(501)>:19035] from originator [app<application.com.nexy.assistant.41170369.41170378(501)>:19035] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-928865 target:19035 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:29:29.884861-0500	runningboardd	Assertion 394-394-928865 (target:[app<application.com.nexy.assistant.41170369.41170378(501)>:19035]) will be created as active
default	12:29:29.885050-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring jetsam update because this process is not memory-managed
default	12:29:29.885071-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring suspend because this process is not lifecycle managed
default	12:29:29.885087-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Set darwin role to: UserInteractive
default	12:29:29.885097-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring GPU update because this process is not GPU managed
default	12:29:29.885129-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring memory limit update because this process is not memory-managed
default	12:29:29.885175-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] reported to RB as running
default	12:29:29.888273-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	12:29:29.981290-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	12:29:29.982665-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.60, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	12:29:29.991206-0500	tccd	AUTHREQ_SUBJECT: msgID=489.60, subject=com.nexy.assistant,
default	12:29:29.992623-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	12:29:29.995239-0500	gamepolicyd	Received state update for 19035 (app<application.com.nexy.assistant.41170369.41170378(501)>, running-active-NotVisible
default	12:29:30.021286-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	12:29:30.281351-0500	Nexy	[0x103f44c80] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	12:29:30.281434-0500	Nexy	[0x103f45240] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	12:29:30.532404-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x103f344a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:29:30.532888-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x103f344a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:29:30.533154-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x103f344a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	12:29:30.533374-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x103f344a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	12:29:30.534498-0500	Nexy	[0x103f4ef50] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	12:29:30.535233-0500	Nexy	[0xc696f4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	12:29:30.535492-0500	Nexy	[0xc696f4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	12:29:30.536005-0500	Nexy	[0xc696f4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	12:29:30.536992-0500	Nexy	Received configuration update from daemon (initial)
default	12:29:30.537874-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	12:29:30.538191-0500	Nexy	[0xc696f43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:29:30.538868-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=19035.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:29:30.540266-0500	tccd	AUTHREQ_SUBJECT: msgID=19035.1, subject=com.nexy.assistant,
default	12:29:30.540967-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	12:29:30.557771-0500	Nexy	[0xc696f43c0] invalidated after the last release of the connection object
default	12:29:30.557970-0500	Nexy	server port 0x0000340f, session port 0x0000340f
default	12:29:30.558779-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.8959, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	12:29:30.558809-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	12:29:30.559726-0500	tccd	AUTHREQ_SUBJECT: msgID=387.8959, subject=com.nexy.assistant,
default	12:29:30.560400-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	12:29:30.576731-0500	Nexy	New connection 0x5df4b main
default	12:29:30.578850-0500	Nexy	CHECKIN: pid=19035
default	12:29:30.585730-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41170369.41170378(501)>:19035] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:19035" ID:394-357-928869 target:19035 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	12:29:30.585798-0500	runningboardd	Assertion 394-357-928869 (target:[app<application.com.nexy.assistant.41170369.41170378(501)>:19035]) will be created as active
default	12:29:30.586036-0500	Nexy	CHECKEDIN: pid=19035 asn=0x0-0x1472471 foreground=0
default	12:29:30.586169-0500	runningboardd	Invalidating assertion 394-357-928866 (target:[app<application.com.nexy.assistant.41170369.41170378(501)>:19035]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	12:29:30.585930-0500	launchservicesd	CHECKIN:0x0-0x1472471 19035 com.nexy.assistant
default	12:29:30.586285-0500	Nexy	[0xc696f43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:29:30.586297-0500	Nexy	[0xc696f43c0] Connection returned listener port: 0x4d03
default	12:29:30.586046-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	12:29:30.586137-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	12:29:30.586507-0500	Nexy	[0xc68bc0300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xc696f43c0.peer[357].0xc68bc0300
default	12:29:30.591344-0500	Nexy	FRONTLOGGING: version 1
default	12:29:30.591348-0500	Nexy	Registered, pid=19035 ASN=0x0,0x1472471
default	12:29:30.591536-0500	WindowServer	5df4b[CreateApplication]: Process creation: 0x0-0x1472471 (Nexy) connectionID: 5DF4B pid: 19035 in session 0x101
default	12:29:30.591931-0500	Nexy	[0xc696f4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	12:29:30.593154-0500	Nexy	[0xc696f43c0] Connection returned listener port: 0x4d03
default	12:29:30.593883-0500	Nexy	BringForward: pid=19035 asn=0x0-0x1472471 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	12:29:30.594094-0500	Nexy	BringFrontModifier: pid=19035 asn=0x0-0x1472471 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	12:29:30.594799-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:29:30.596250-0500	Nexy	No persisted cache on this platform.
default	12:29:30.597383-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:29:30.598180-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	12:29:30.600738-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	12:29:30.600747-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	12:29:30.600797-0500	Nexy	Initializing connection
default	12:29:30.600831-0500	Nexy	Removing all cached process handles
default	12:29:30.600851-0500	Nexy	Sending handshake request attempt #1 to server
default	12:29:30.600860-0500	Nexy	Creating connection to com.apple.runningboard
default	12:29:30.600867-0500	Nexy	[0xc696f48c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	12:29:30.601227-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.41170369.41170378(501)>:19035] as ready
default	12:29:30.601788-0500	Nexy	Handshake succeeded
default	12:29:30.601802-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41170369.41170378(501)>
default	12:29:30.602312-0500	Nexy	[0xc696f43c0] Connection returned listener port: 0x4d03
default	12:29:30.603362-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 19035
default	12:29:30.605516-0500	Nexy	[0xc696f43c0] Connection returned listener port: 0x4d03
default	12:29:30.608468-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	12:29:30.608486-0500	Nexy	[0xc696f4780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	12:29:30.608566-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	12:29:30.608607-0500	Nexy	[0xc696f4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:29:30.609801-0500	Nexy	[0xc696f4a00] Connection returned listener port: 0x6403
default	12:29:30.610502-0500	Nexy	Registered process with identifier 19035-2766575
default	12:29:31.857532-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 15DD70B6-CB0D-4574-B952-80C5C2A0E6F8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.62128,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd4ee6493 tp_proto=0x06"
default	12:29:31.857554-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:62128<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4780063 t_state: SYN_SENT process: Nexy:19035 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0fc4a4e
default	12:29:31.857734-0500	kernel	tcp connected: [<IPv4-redacted>:62128<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4780063 t_state: ESTABLISHED process: Nexy:19035 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0fc4a4e
default	12:29:31.858056-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:62128<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4780063 t_state: FIN_WAIT_1 process: Nexy:19035 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb0fc4a4e
default	12:29:31.858066-0500	kernel	tcp_connection_summary [<IPv4-redacted>:62128<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4780063 t_state: FIN_WAIT_1 process: Nexy:19035 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	12:29:31.953044-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	12:29:31.954452-0500	Nexy	[0xc696f4c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	12:29:31.958928-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f47ef","name":"Nexy(19035)"}, "details":{"PID":19035,"session_type":"Primary"} }
default	12:29:31.959060-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":19035}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47ef, sessionType: 'prim', isRecording: false }, 
]
default	12:29:31.959836-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 19035, name = Nexy
default	12:29:31.960257-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc697d7480 with ID: 0x1f47ef
default	12:29:31.961265-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	12:29:31.962083-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	12:29:31.964622-0500	Nexy	[0xc696f4dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	12:29:31.966823-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41170369.41170378 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41170369.41170378>
default	12:29:31.972070-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	12:29:31.976908-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	12:29:31.977118-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	12:29:31.977372-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	12:29:31.977385-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	12:29:31.977761-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:29:31.977919-0500	Nexy	[0xc696f4f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	12:29:31.978151-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	12:29:31.978914-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=19035.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:29:31.985785-0500	tccd	AUTHREQ_SUBJECT: msgID=19035.2, subject=com.nexy.assistant,
default	12:29:31.986463-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:32.002671-0500	Nexy	[0xc696f4f00] invalidated after the last release of the connection object
default	12:29:32.002729-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:29:32.005708-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	12:29:32.007102-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8294, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:32.008171-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8294, subject=com.nexy.assistant,
default	12:29:32.008791-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
error	12:29:32.022093-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	12:29:32.023013-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8296, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:32.024182-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8296, subject=com.nexy.assistant,
default	12:29:32.025054-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:32.040462-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	12:29:32.040713-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc69d08480> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	12:29:32.056932-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	12:29:32.058568-0500	Nexy	[0xc696f4f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	12:29:32.058885-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=81754702479361 }
default	12:29:32.059222-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	12:29:32.059264-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	12:29:32.059298-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	12:29:32.072640-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 115
default	12:29:32.109524-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	12:29:32.109549-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	12:29:32.117317-0500	Nexy	[0xc696f5040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	12:29:32.134044-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc69d20040) Selecting device 71 from constructor
default	12:29:32.134056-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc69d20040)
default	12:29:32.134061-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc69d20040) not already running
default	12:29:32.134448-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc69d20040) nothing to teardown
default	12:29:32.134452-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc69d20040) connecting device 71
default	12:29:32.134533-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc69d20040) Device ID: 71 (Input:No | Output:Yes): true
default	12:29:32.134618-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc69d20040) created ioproc 0xa for device 71
default	12:29:32.134711-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20040) adding 7 device listeners to device 71
default	12:29:32.134861-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20040) adding 0 device delegate listeners to device 71
default	12:29:32.134869-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc69d20040)
default	12:29:32.134932-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.134938-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:29:32.134944-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.134954-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:29:32.134963-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:29:32.135045-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc69d20040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:29:32.135052-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc69d20040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:29:32.135057-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:29:32.135061-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20040) removing 0 device listeners from device 0
default	12:29:32.135063-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20040) removing 0 device delegate listeners from device 0
default	12:29:32.135067-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc69d20040)
default	12:29:32.135103-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:29:32.135376-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.137270-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	12:29:32.137331-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	12:29:32.138725-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc69d11ec0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.138765-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.140347-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.140527-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.145447-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.145643-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.147505-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc69d11e00, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.147517-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.147797-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.148456-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc69d133c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.148466-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc69d133c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:29:32.148469-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.148468-0500	Nexy	AudioConverter -> 0xc69d133c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:29:32.148477-0500	Nexy	AudioConverter -> 0xc69d133c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:29:32.148480-0500	Nexy	AudioConverter -> 0xc69d133c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:29:32.149266-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc69d11e00, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.149274-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc69d11e00: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:29:32.149276-0500	Nexy	AudioConverter -> 0xc69d11e00: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	12:29:32.149280-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:29:32.149281-0500	Nexy	AudioConverter -> 0xc69d11e00: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	12:29:32.149286-0500	Nexy	AudioConverter -> 0xc69d11e00: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	12:29:32.149415-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc69d11e00: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:29:32.234915-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc69d20e40) Selecting device 71 from constructor
default	12:29:32.234922-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc69d20e40)
default	12:29:32.234929-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc69d20e40) not already running
default	12:29:32.234931-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc69d20e40) nothing to teardown
default	12:29:32.234935-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc69d20e40) connecting device 71
default	12:29:32.235002-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc69d20e40) Device ID: 71 (Input:No | Output:Yes): true
default	12:29:32.235086-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc69d20e40) created ioproc 0xb for device 71
default	12:29:32.235173-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 7 device listeners to device 71
default	12:29:32.235320-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 0 device delegate listeners to device 71
default	12:29:32.235327-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc69d20e40)
default	12:29:32.235388-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.235395-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:29:32.235400-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:29:32.235407-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:29:32.235414-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:29:32.235492-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc69d20e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:29:32.235500-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc69d20e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:29:32.235503-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:29:32.235507-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 0 device listeners from device 0
default	12:29:32.235511-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 0 device delegate listeners from device 0
default	12:29:32.235515-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc69d20e40)
default	12:29:32.235526-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	12:29:32.235565-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xc69d20e40) caller requesting device change from 71 to 78
default	12:29:32.235572-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc69d20e40)
default	12:29:32.235575-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc69d20e40) not already running
default	12:29:32.235579-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc69d20e40) disconnecting device 71
default	12:29:32.235584-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc69d20e40) destroying ioproc 0xb for device 71
default	12:29:32.235917-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	12:29:32.235982-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:29:32.236052-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc69d20e40) connecting device 78
default	12:29:32.236113-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc69d20e40) Device ID: 78 (Input:Yes | Output:No): true
default	12:29:32.237330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8297, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:32.238590-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8297, subject=com.nexy.assistant,
default	12:29:32.239212-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:32.256371-0500	tccd	AUTHREQ_PROMPTING: msgID=395.8297, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	12:29:34.188651-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	12:29:34.190354-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc69d20e40) created ioproc 0xa for device 78
default	12:29:34.190485-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	12:29:34.190578-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 7 device listeners to device 78
default	12:29:34.190908-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 0 device delegate listeners to device 78
default	12:29:34.190923-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc69d20e40)
default	12:29:34.190938-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	12:29:34.190958-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:29:34.191193-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	12:29:34.191205-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	12:29:34.191215-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	12:29:34.191370-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc69d20e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:29:34.191397-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc69d20e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:29:34.191406-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:29:34.191415-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 7 device listeners from device 71
default	12:29:34.191656-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 0 device delegate listeners from device 71
default	12:29:34.191667-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc69d20e40)
default	12:29:34.192276-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:29:34.194328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8298, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:34.196134-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8298, subject=com.nexy.assistant,
default	12:29:34.197037-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:34.217736-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc69d11da0, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	12:29:34.218010-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	12:29:34.219257-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8299, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:34.220515-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8299, subject=com.nexy.assistant,
default	12:29:34.221215-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:34.242850-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8300, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:29:34.244811-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8300, subject=com.nexy.assistant,
default	12:29:34.246028-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x719171200 at /Applications/Nexy.app
default	12:29:34.265386-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	12:29:34.266836-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:29:34.268245-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41170369.41170378(501)>:19035] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-928893 target:19035 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:29:34.268376-0500	runningboardd	Assertion 394-328-928893 (target:[app<application.com.nexy.assistant.41170369.41170378(501)>:19035]) will be created as active
default	12:29:34.269865-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	12:29:34.272591-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring jetsam update because this process is not memory-managed
default	12:29:34.272608-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring suspend because this process is not lifecycle managed
default	12:29:34.272640-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring GPU update because this process is not GPU managed
default	12:29:34.272696-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring memory limit update because this process is not memory-managed
default	12:29:34.276576-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41170369.41170378(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:29:34.277122-0500	gamepolicyd	Received state update for 19035 (app<application.com.nexy.assistant.41170369.41170378(501)>, running-active-NotVisible
default	12:29:34.295008-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	12:29:34.296277-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47ef","name":"Nexy(19035)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	12:29:34.296396-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:29:34.296511-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:29:34.296596-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47ef, Nexy(19035), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	12:29:34.296686-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:29:34.296689-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.296727-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:29:34.296783-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	12:29:34.296806-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47ef, Nexy(19035), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2030 starting recording
default	12:29:34.296830-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.296926-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.296983-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.297019-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.297128-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.297362-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:29:34.297395-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:29:34.297427-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47ef, Nexy(19035), 'prim'', displayID:'com.nexy.assistant'}
default	12:29:34.297527-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.297538-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	12:29:34.297549-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:29:34.297656-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.297694-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.297720-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	12:29:34.297739-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	12:29:34.297755-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	12:29:34.297811-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	12:29:34.298180-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41170369.41170378 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41170369.41170378>
error	12:29:34.300415-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
fault	12:29:34.300570-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41170369.41170378 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41170369.41170378>
default	12:29:34.302603-0500	coreaudiod	Sending message. { reporterID=81754702479363, category=IO, type=error, message=["cause_set": Optional(0), "io_frame_counter": Optional(15), "multi_cycle_io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "sample_rate": Optional(48000), "careporting_timestamp": 1767979774.3021169, "wg_user_time_mach": Optional(9802), "other_active_clients": Optional([  ]), "issue_type": Optional(overload), "HAL_client_IO_duration": Optional(57125), "output_device_uid_list": Optional(), "time_since_prev_overload": Optional(197402512436375), "output_device_transport_list": Optional(), "input_device_source_list": Optional(Internal Microphone), "smallest_buffer_frame_size": Optional(15), "overload_type": Optional(Overload), "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(0), "wg_instructions": Optional(8869836), "anchor_sample_time": Optional(44), "num_continuous_silent_io_cycles": Optional(0), "lateness": Optional(230), "cause": Optional(Unknown), "is_recovering": Optional(0), "wg_cycles": Optional(7<…> }
default	12:29:34.314023-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	12:29:34.314096-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	12:29:34.314131-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	12:29:34.315052-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.315063-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.315077-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.315100-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.315119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.315129-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:29:34.315598-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:29:34.317348-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.317372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.317384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:29:34.317462-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:29:34.317668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317677-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317683-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.317688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.317693-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.317698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:29:34.323297-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	12:29:34.353364-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	12:29:34.353709-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47ef","name":"Nexy(19035)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:29:34.353853-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:29:34.353916-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	12:29:34.353948-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47ef, Nexy(19035), 'prim'', displayID:'com.nexy.assistant'}
default	12:29:34.354084-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47ef, Nexy(19035), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2030 stopping recording
default	12:29:34.354110-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.354146-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:29:34.354372-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.354432-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	12:29:34.354227-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:29:34.354460-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	12:29:34.354307-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:29:34.354727-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:29:34.354520-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	12:29:34.354741-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:29:34.354942-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.354973-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.354991-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	12:29:34.354784-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.356338-0500	coreaudiod	Sending message. { reporterID=81754702479363, category=IO, type=error, message=["cause_set": Optional(4), "io_frame_counter": Optional(2550), "multi_cycle_io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "sample_rate": Optional(48000), "careporting_timestamp": 1767979774.356018, "wg_user_time_mach": Optional(2334), "other_active_clients": Optional([  ]), "issue_type": Optional(overload), "HAL_client_IO_duration": Optional(1225125), "output_device_uid_list": Optional(), "time_since_prev_overload": Optional(54401583), "output_device_transport_list": Optional(), "input_device_source_list": Optional(Internal Microphone), "smallest_buffer_frame_size": Optional(2147483647), "overload_type": Optional(Overload), "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(0), "wg_instructions": Optional(232126), "anchor_sample_time": Optional(308), "num_continuous_silent_io_cycles": Optional(0), "lateness": Optional(42), "cause": Optional(ClientHALIODurationExceededBudget), "is_recovering": Optiona<…> }
default	12:29:34.360960-0500	runningboardd	Invalidating assertion 394-328-928893 (target:[app<application.com.nexy.assistant.41170369.41170378(501)>:19035]) from originator [osservice<com.apple.powerd>:328]
default	12:29:34.362323-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	12:29:34.366450-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.366462-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.366472-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.366477-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	12:29:34.366485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	12:29:34.366489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	12:29:34.366588-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	12:29:34.455259-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc69d20e40) Selecting device 0 from destructor
default	12:29:34.455275-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc69d20e40)
default	12:29:34.455282-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc69d20e40) not already running
default	12:29:34.455290-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc69d20e40) disconnecting device 78
default	12:29:34.455296-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc69d20e40) destroying ioproc 0xa for device 78
default	12:29:34.455333-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	12:29:34.455374-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	12:29:34.455674-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xc69d20e40) nothing to setup
default	12:29:34.455693-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 0 device listeners to device 0
default	12:29:34.455702-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc69d20e40) adding 0 device delegate listeners to device 0
default	12:29:34.455708-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 7 device listeners from device 78
default	12:29:34.455975-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc69d20e40) removing 0 device delegate listeners from device 78
default	12:29:34.455987-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc69d20e40)
default	12:29:34.467609-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring jetsam update because this process is not memory-managed
default	12:29:34.467725-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring suspend because this process is not lifecycle managed
default	12:29:34.467736-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring GPU update because this process is not GPU managed
default	12:29:34.467876-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] Ignoring memory limit update because this process is not memory-managed
default	12:29:34.472105-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41170369.41170378(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	12:29:34.473079-0500	gamepolicyd	Received state update for 19035 (app<application.com.nexy.assistant.41170369.41170378(501)>, running-active-NotVisible
default	12:29:34.518527-0500	Nexy	[0xc696f5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	12:29:34.519243-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	12:29:34.519438-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=19035.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:29:34.520675-0500	tccd	AUTHREQ_SUBJECT: msgID=19035.3, subject=com.nexy.assistant,
default	12:29:34.521516-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	12:29:34.536464-0500	Nexy	[0xc696f5400] invalidated after the last release of the connection object
default	12:29:34.536604-0500	Nexy	[0xc696f5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	12:29:34.537159-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	12:29:34.537345-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=19035.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=19035, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	12:29:34.538434-0500	tccd	AUTHREQ_SUBJECT: msgID=19035.4, subject=com.nexy.assistant,
default	12:29:34.539310-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	12:29:34.553683-0500	Nexy	[0xc696f5400] invalidated after the last release of the connection object
default	12:29:34.553777-0500	Nexy	[0xc696f5400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	12:29:34.553910-0500	Nexy	[0xc696f5400] invalidated after the last release of the connection object
default	12:29:34.553961-0500	kernel	AMFI: Denying core dump for pid 19035 (Nexy)
default	12:29:34.554095-0500	kernel	Nexy[19035] Corpse allowed 1 of 5
default	12:29:34.554565-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f47ef","name":"Nexy(19035)"}, "details":null }
default	12:29:34.554605-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f47ef from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":19035})
default	12:29:34.554615-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":19035})
default	12:29:34.554991-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:29:34.555622-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.555716-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.555120-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2030, PID = 19035, Name = sid:0x1f47ef, Nexy(19035), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:29:34.555741-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.555310-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.555480-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.555830-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	12:29:34.556967-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1472471 (Nexy) connectionID: 5DF4B pid: 19035 in session 0x101
default	12:29:34.556991-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1472471 (Nexy) acq:0xb6ab83220 count:1
default	12:29:34.561062-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1472471 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1472471 (Nexy)"
)}
default	12:29:34.563071-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x4a5b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1472471 (Nexy)"
)}
default	12:29:34.566247-0500	runningboardd	[app<application.com.nexy.assistant.41170369.41170378(501)>:19035] termination reported by launchd (2, 11, 11)
default	12:29:34.566314-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.566746-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.566953-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.567001-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.574455-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41170369.41170378(501)>: none (role: None) (endowments: (null))
default	12:29:34.574902-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 19035, name = Nexy
default	12:29:34.574825-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41170369.41170378(501)>: none (role: None) (endowments: (null))
default	12:29:34.575877-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.576827-0500	gamepolicyd	Received state update for 19035 (app<application.com.nexy.assistant.41170369.41170378(501)>, none-NotVisible
default	12:29:34.576910-0500	launchservicesd	Hit the server for a process handle 11f3363800004a5b that resolved to: [app<application.com.nexy.assistant.41170369.41170378(501)>:19035]
default	12:29:34.584068-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1472471} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	12:29:34.584103-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aad9220: Nexy> state 3
default	12:29:34.584117-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	12:29:34.584727-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aad9220: Nexy> state 4
default	12:29:34.584739-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	12:29:34.588038-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257900 at /Applications/Nexy.app
default	12:29:34.612246-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	12:29:34.616940-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	12:29:37.149633-0500	ReportCrash	Enabling urgent submission for process Nexy
default	12:29:37.150948-0500	ReportCrash	Formulating fatal 309 report for corpse[19035] Nexy
default	12:29:37.153868-0500	ReportCrash	loadStoreInfo [platform 1] com.nexy.assistant from file:///Applications/Nexy.app/
default	12:29:37.162955-0500	osanalyticshelper	creating type 309 as /Users/sergiyzasorin/Library/Logs/DiagnosticReports/.Nexy-2026-01-09-122937.ips
default	12:29:37.169218-0500	osanalyticshelper	Saved type '309(<private>)' report (2 of max 25) at /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-122937.ips
default	12:29:37.169433-0500	osanalyticshelper	xpc log creation type 309 result success: /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-122937.ips
default	12:29:37.169704-0500	ReportCrash	client log create type 309 result success: /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-122937.ips
default	12:29:37.191766-0500	ReportCrash	com.nexy.assistant is not a MetricKit client
default	12:29:37.199007-0500	ReportCrash	recordCrashEvent; isBeta 0, log: '/Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-122937.ips'
default	12:29:37.830364-0500	SubmitDiagInfo	Retiring (309) submitted '/Users/sergiyzasorin/Library/Logs/DiagnosticReports/Retired/Nexy-2026-01-09-122937.ips': success
