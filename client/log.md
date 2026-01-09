default	09:58:37.051131-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	09:58:37.051419-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	09:58:37.069962-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	09:58:37.078083-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41062796.41062805(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	09:58:37.078295-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41062796.41062805(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:51969] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-51969-883044 target:app<application.com.nexy.assistant.41062796.41062805(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	09:58:37.078442-0500	runningboardd	Assertion 394-51969-883044 (target:app<application.com.nexy.assistant.41062796.41062805(501)>) will be created as active
default	09:58:37.084841-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	09:58:37.084893-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.41062796.41062805(501)>
default	09:58:37.084912-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	09:58:37.085019-0500	runningboardd	app<application.com.nexy.assistant.41062796.41062805(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	09:58:37.225368-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:53679" ID:394-357-883046 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	09:58:37.225610-0500	runningboardd	Assertion 394-357-883046 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:37.302064-0500	gamepolicyd	Hit the server for a process handle 106ec0200000d1af that resolved to: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:37.302519-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:37.342214-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:37.342281-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:37.342318-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
default	09:58:37.342411-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:37.433579-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:37.901437-0500	dmd	Requested application com.nexy.assistant has policy OK, associated categories:DH1005 associated sites:(null) equivalent bundle identifiers:com.nexy.assistant
default	09:58:42.295015-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:42.616578-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant), 0, 0, 1, 0, 4, 4, 1
default	09:58:42.617780-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.58, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	09:58:42.627515-0500	tccd	AUTHREQ_SUBJECT: msgID=489.58, subject=com.nexy.assistant,
default	09:58:42.630283-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254000 at /Applications/Nexy.app
default	09:58:42.657613-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant)
default	09:58:43.070210-0500	kernel	Nexy[53679] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x8acafc5526d17a59. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:43.070239-0500	kernel	Nexy[53679] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x8acafc5526d17a59. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:43.865931-0500	Nexy	[0x101ade130] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:43.866030-0500	Nexy	[0x101ad9890] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:44.482959-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x101ae6450 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:44.483241-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x101ae6450 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:44.483464-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x101ae6450 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:44.483675-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x101ae6450 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:44.485512-0500	Nexy	[0x101ae3bb0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	09:58:44.497164-0500	Nexy	[0xa6625c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	09:58:44.497720-0500	Nexy	[0xa6625c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	09:58:44.499922-0500	Nexy	[0xa6625c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	09:58:44.502342-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	09:58:44.505266-0500	Nexy	[0xa6625c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:44.506186-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53679.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:44.508217-0500	tccd	AUTHREQ_SUBJECT: msgID=53679.1, subject=com.nexy.assistant,
default	09:58:44.509138-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	09:58:44.531382-0500	Nexy	[0xa6625c3c0] invalidated after the last release of the connection object
default	09:58:44.531760-0500	Nexy	server port 0x00003813, session port 0x00003813
default	09:58:44.533299-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.8579, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:44.533329-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:44.535092-0500	tccd	AUTHREQ_SUBJECT: msgID=387.8579, subject=com.nexy.assistant,
default	09:58:44.536298-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	09:58:44.550622-0500	Nexy	Received configuration update from daemon (initial)
default	09:58:44.565354-0500	Nexy	New connection 0x182c23 main
default	09:58:44.571165-0500	Nexy	CHECKIN: pid=53679
default	09:58:44.586669-0500	Nexy	CHECKEDIN: pid=53679 asn=0x0-0x1403402 foreground=0
default	09:58:44.586277-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:53679" ID:394-357-883138 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	09:58:44.586424-0500	runningboardd	Assertion 394-357-883138 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:44.586456-0500	launchservicesd	CHECKIN:0x0-0x1403402 53679 com.nexy.assistant
default	09:58:44.587317-0500	runningboardd	Invalidating assertion 394-357-883046 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	09:58:44.587119-0500	Nexy	[0xa6625c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	09:58:44.587178-0500	Nexy	[0xa6625c3c0] Connection returned listener port: 0x5003
default	09:58:44.588784-0500	Nexy	[0xa674d4300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xa6625c3c0.peer[357].0xa674d4300
default	09:58:44.589809-0500	Nexy	FRONTLOGGING: version 1
default	09:58:44.589853-0500	Nexy	Registered, pid=53679 ASN=0x0,0x1403402
default	09:58:44.590272-0500	WindowServer	182c23[CreateApplication]: Process creation: 0x0-0x1403402 (Nexy) connectionID: 182C23 pid: 53679 in session 0x101
default	09:58:44.590637-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	09:58:44.590961-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	09:58:44.593255-0500	Nexy	[0xa6625c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	09:58:44.593725-0500	Nexy	[0xa6625c3c0] Connection returned listener port: 0x5003
default	09:58:44.595346-0500	Nexy	BringForward: pid=53679 asn=0x0-0x1403402 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	09:58:44.595623-0500	Nexy	BringFrontModifier: pid=53679 asn=0x0-0x1403402 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	09:58:44.597671-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	09:58:44.600657-0500	Nexy	No persisted cache on this platform.
default	09:58:44.604063-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	09:58:44.605329-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	09:58:44.614603-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	09:58:44.614622-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	09:58:44.614727-0500	Nexy	Initializing connection
default	09:58:44.614800-0500	Nexy	Removing all cached process handles
default	09:58:44.614833-0500	Nexy	Sending handshake request attempt #1 to server
default	09:58:44.614845-0500	Nexy	Creating connection to com.apple.runningboard
default	09:58:44.614857-0500	Nexy	[0xa6625c780] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	09:58:44.615539-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] as ready
default	09:58:44.616288-0500	Nexy	Handshake succeeded
default	09:58:44.616307-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41062796.41062805(501)>
default	09:58:44.616843-0500	Nexy	[0xa6625c3c0] Connection returned listener port: 0x5003
default	09:58:44.618154-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 53679
default	09:58:44.621437-0500	Nexy	[0xa6625c3c0] Connection returned listener port: 0x5003
default	09:58:44.651793-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	09:58:44.652196-0500	Nexy	[0xa6625c640] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	09:58:44.652352-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	09:58:44.652446-0500	Nexy	[0xa6625ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	09:58:44.653996-0500	Nexy	[0xa6625ca00] Connection returned listener port: 0x6d03
default	09:58:44.655903-0500	Nexy	Registered process with identifier 53679-2629490
default	09:58:47.758202-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	09:58:48.463964-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1C163160-A668-44BB-ACDD-C1F2FB36DFD6 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64238,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x95df237d tp_proto=0x06"
default	09:58:48.464087-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64238<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4598435 t_state: SYN_SENT process: Nexy:53679 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8bf1710e
default	09:58:48.464741-0500	kernel	tcp connected: [<IPv4-redacted>:64238<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4598435 t_state: ESTABLISHED process: Nexy:53679 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8bf1710e
default	09:58:48.465091-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64238<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4598435 t_state: FIN_WAIT_1 process: Nexy:53679 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8bf1710e
default	09:58:48.465102-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64238<-><IPv4-redacted>:53] interface: utun4 (skipped: 10786)
so_gencnt: 4598435 t_state: FIN_WAIT_1 process: Nexy:53679 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:48.649717-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:48.650600-0500	Nexy	[0xa6625cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:48.652739-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f47e8","name":"Nexy(53679)"}, "details":{"PID":53679,"session_type":"Primary"} }
default	09:58:48.652848-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":53679}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f47e8, sessionType: 'prim', isRecording: false }, 
]
default	09:58:48.653677-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 53679, name = Nexy
default	09:58:48.654131-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa6754bb00 with ID: 0x1f47e8
default	09:58:48.654766-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:48.655860-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:48.657701-0500	Nexy	[0xa6625cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	09:58:48.660752-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41062796.41062805 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41062796.41062805>
default	09:58:48.665208-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:48.666868-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:48.667033-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:48.667187-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:48.667196-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:48.667226-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:48.667390-0500	Nexy	[0xa6625cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:48.667958-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53679.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:48.668412-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:48.675189-0500	tccd	AUTHREQ_SUBJECT: msgID=53679.2, subject=com.nexy.assistant,
default	09:58:48.675822-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:48.688256-0500	Nexy	[0xa6625cf00] invalidated after the last release of the connection object
default	09:58:48.688313-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:48.691535-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	09:58:48.693125-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8153, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.694180-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8153, subject=com.nexy.assistant,
default	09:58:48.694768-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
error	09:58:48.707828-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:48.708666-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8155, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.709676-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8155, subject=com.nexy.assistant,
default	09:58:48.710247-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:48.723455-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:48.723475-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa676a6be0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:58:48.752646-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:48.752780-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:48.758536-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:48.760507-0500	Nexy	[0xa6625cf00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	09:58:48.760853-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=230549549481985 }
default	09:58:48.761313-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	09:58:48.761909-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	09:58:48.761944-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	09:58:48.775449-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:48.775584-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:48.780822-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 126
default	09:58:48.819502-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	09:58:48.819529-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	09:58:48.826423-0500	Nexy	[0xa6625d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:48.842196-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa670b0e40) Selecting device 85 from constructor
default	09:58:48.842205-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa670b0e40)
default	09:58:48.842210-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa670b0e40) not already running
default	09:58:48.842749-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa670b0e40) nothing to teardown
default	09:58:48.842752-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa670b0e40) connecting device 85
default	09:58:48.842845-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa670b0e40) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:48.842935-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa670b0e40) created ioproc 0xa for device 85
default	09:58:48.843030-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0e40) adding 7 device listeners to device 85
default	09:58:48.843180-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0e40) adding 0 device delegate listeners to device 85
default	09:58:48.843192-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa670b0e40)
default	09:58:48.843261-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.843269-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:48.843275-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.843285-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:48.843293-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:48.843381-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa670b0e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:48.843393-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa670b0e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:48.843398-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	09:58:48.843401-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0e40) removing 0 device listeners from device 0
default	09:58:48.843405-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0e40) removing 0 device delegate listeners from device 0
default	09:58:48.843409-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa670b0e40)
default	09:58:48.843446-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:48.843796-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.845359-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	09:58:48.845412-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:48.845555-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa67816fd0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.845596-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.846849-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.847079-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.851816-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.852046-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.853693-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa678170f0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.853707-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.854084-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.854676-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa678170f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.854685-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa678170f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:58:48.854690-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.854686-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	09:58:48.854696-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	09:58:48.854701-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	09:58:48.855382-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa678170f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.855390-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa678170f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:58:48.855391-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	09:58:48.855393-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:48.855397-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	09:58:48.855402-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	09:58:48.855546-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa678170f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:58:48.929626-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa670b0040) Selecting device 85 from constructor
default	09:58:48.929636-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa670b0040)
default	09:58:48.929641-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa670b0040) not already running
default	09:58:48.929645-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa670b0040) nothing to teardown
default	09:58:48.929647-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa670b0040) connecting device 85
default	09:58:48.929717-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa670b0040) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:48.929805-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa670b0040) created ioproc 0xb for device 85
default	09:58:48.929898-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 7 device listeners to device 85
default	09:58:48.930057-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 0 device delegate listeners to device 85
default	09:58:48.930064-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa670b0040)
default	09:58:48.930134-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.930143-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:48.930149-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.930154-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:48.930161-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:48.930248-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa670b0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:48.930255-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa670b0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:48.930260-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	09:58:48.930265-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 0 device listeners from device 0
default	09:58:48.930269-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 0 device delegate listeners from device 0
default	09:58:48.930274-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa670b0040)
default	09:58:48.930285-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:48.930330-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xa670b0040) caller requesting device change from 85 to 91
default	09:58:48.930337-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa670b0040)
default	09:58:48.930346-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa670b0040) not already running
default	09:58:48.930350-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa670b0040) disconnecting device 85
default	09:58:48.930354-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa670b0040) destroying ioproc 0xb for device 85
default	09:58:48.930407-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	09:58:48.930468-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:48.930537-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa670b0040) connecting device 91
default	09:58:48.930608-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa670b0040) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:48.931876-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8156, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.933155-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8156, subject=com.nexy.assistant,
default	09:58:48.933799-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:48.951065-0500	tccd	AUTHREQ_PROMPTING: msgID=395.8156, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	09:58:50.318372-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	09:58:50.318808-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa670b0040) created ioproc 0xa for device 91
default	09:58:50.319086-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 7 device listeners to device 91
default	09:58:50.319434-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 0 device delegate listeners to device 91
default	09:58:50.319452-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa670b0040)
default	09:58:50.319468-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:50.319485-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:50.319750-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:50.319762-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	09:58:50.319772-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:50.319964-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa670b0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:50.319983-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa670b0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:50.319993-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	09:58:50.320002-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 7 device listeners from device 85
default	09:58:50.320297-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 0 device delegate listeners from device 85
default	09:58:50.320312-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa670b0040)
default	09:58:50.321024-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:50.323255-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8157, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.325973-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8157, subject=com.nexy.assistant,
default	09:58:50.327321-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.328176-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	09:58:50.348634-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa678171b0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	09:58:50.348944-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:50.350356-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8158, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.352946-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8158, subject=com.nexy.assistant,
default	09:58:50.353801-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.378762-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8159, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.380000-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8159, subject=com.nexy.assistant,
default	09:58:50.380681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.398997-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:50.399427-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:50.399610-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:50.400829-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:50.401150-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:50.404040-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5200] Created node ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:50.404122-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5200] Created node ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:50.404596-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:50.510513-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:50.512056-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:50.512037-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:47825 called from <private>
default	09:58:50.512145-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:50.513372-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47825 called from <private>
default	09:58:50.513611-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47825)
default	09:58:50.513627-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47825 called from <private>
default	09:58:50.513633-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47825 called from <private>
default	09:58:50.514731-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47824)
default	09:58:50.514746-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47831)
default	09:58:50.518640-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-883203 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:50.518712-0500	runningboardd	Assertion 394-328-883203 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:50.521006-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:50.521734-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:58:50.520487-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41062796.41062805 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41062796.41062805>
default	09:58:50.521755-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:50.521838-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:50.522162-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
default	09:58:50.522250-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:50.515727-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:47824 called from <private>
default	09:58:50.515882-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:47831 called from <private>
default	09:58:50.515893-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47824 called from <private>
default	09:58:50.515913-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47831 called from <private>
default	09:58:50.517173-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47831)
default	09:58:50.518285-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47831 called from <private>
fault	09:58:50.523078-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41062796.41062805 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41062796.41062805>
default	09:58:50.518320-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47831 called from <private>
default	09:58:50.528153-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47825)
default	09:58:50.528191-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47825)
default	09:58:50.528203-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47825)
default	09:58:50.528214-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47825)
default	09:58:50.528354-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:47825 called from <private>
default	09:58:50.528364-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:47825 called from <private>
default	09:58:50.528378-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:47825 called from <private>
default	09:58:50.528384-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:47825 called from <private>
default	09:58:50.528393-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47825 called from <private>
default	09:58:50.528422-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47825 called from <private>
default	09:58:50.534693-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47e8","name":"Nexy(53679)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:50.534884-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:50.535008-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:50.535077-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f47e8, Nexy(53679), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:50.535259-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:50.535337-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:50.535351-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.535475-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:50.535526-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47e8, Nexy(53679), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2023 starting recording
default	09:58:50.535748-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:50.535808-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:50.528487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47825 called from <private>
default	09:58:50.528582-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47825 called from <private>
default	09:58:50.535592-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.528625-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47825 called from <private>
default	09:58:50.535873-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47e8, Nexy(53679), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:50.535628-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.537009-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:50.528687-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47825 called from <private>
default	09:58:50.539933-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:50.536051-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:58:50.536084-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:50.537069-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.540714-0500	runningboardd	Invalidating assertion 394-328-883203 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) from originator [osservice<com.apple.powerd>:328]
default	09:58:50.542706-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47824 called from <private>
default	09:58:50.542733-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47824 called from <private>
default	09:58:50.543430-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.543596-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47824)
default	09:58:50.543622-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:47824 called from <private>
default	09:58:50.543629-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:47824 called from <private>
default	09:58:50.546466-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47824)
default	09:58:50.546506-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47824)
default	09:58:50.546511-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:47824 called from <private>
default	09:58:50.546520-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:47824 called from <private>
default	09:58:50.546535-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47824 called from <private>
default	09:58:50.546542-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47824 called from <private>
default	09:58:50.546844-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47831)
default	09:58:50.546864-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47825)
default	09:58:50.547321-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47825 called from <private>
default	09:58:50.548248-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47824)
default	09:58:50.548615-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47824 called from <private>
default	09:58:50.548959-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:47824 called from <private>
default	09:58:50.549329-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:47824 called from <private>
default	09:58:50.549454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47824 called from <private>
default	09:58:50.549499-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:47831 called from <private>
default	09:58:50.549559-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:47831 called from <private>
default	09:58:50.550472-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47831)
default	09:58:50.551476-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8160, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.554415-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:50.554712-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:50.554755-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.555439-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:50.555480-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.555716-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8160, subject=com.nexy.assistant,
default	09:58:50.555599-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:50.557369-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47824 called from <private>
default	09:58:50.557382-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47824 called from <private>
default	09:58:50.557497-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47824)
default	09:58:50.557509-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:47824 called from <private>
default	09:58:50.557514-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:47824 called from <private>
default	09:58:50.557945-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47831)
default	09:58:50.557959-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47831)
default	09:58:50.558042-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47831)
default	09:58:50.558088-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47831)
default	09:58:50.558291-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47824)
default	09:58:50.558321-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:47831 called from <private>
default	09:58:50.558341-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:47831 called from <private>
default	09:58:50.558408-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47824)
default	09:58:50.558473-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47831 called from <private>
default	09:58:50.558512-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47831 called from <private>
default	09:58:50.558556-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47831 called from <private>
default	09:58:50.558593-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47831 called from <private>
default	09:58:50.558623-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47831 called from <private>
default	09:58:50.558628-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:47824 called from <private>
default	09:58:50.558660-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47831 called from <private>
default	09:58:50.558670-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:47824 called from <private>
default	09:58:50.558707-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47831 called from <private>
default	09:58:50.558748-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47824 called from <private>
default	09:58:50.558768-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:47831 called from <private>
default	09:58:50.559010-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.559040-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.559076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.559084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.559092-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.559128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.559741-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.558795-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47824 called from <private>
default	09:58:50.558818-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:47831 called from <private>
default	09:58:50.558830-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47824 called from <private>
default	09:58:50.558854-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47831 called from <private>
default	09:58:50.558866-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:47824 called from <private>
default	09:58:50.558883-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47831 called from <private>
default	09:58:50.558921-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:47831 called from <private>
default	09:58:50.560976-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa678170f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	09:58:50.561006-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa678170f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:58:50.561043-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	09:58:50.557615-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.561031-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	09:58:50.561125-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	09:58:50.561187-0500	Nexy	AudioConverter -> 0xa678170f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	09:58:50.571595-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.586762-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:50.589843-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:50.589905-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	09:58:50.589942-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	09:58:50.590004-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	09:58:50.607189-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.617197-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:50.617022-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-883205 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:50.617151-0500	runningboardd	Assertion 394-328-883205 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:50.617676-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:50.617727-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:50.617763-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
default	09:58:50.617821-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:50.618606-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:47824 called from <private>
default	09:58:50.618616-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47824 called from <private>
default	09:58:50.619170-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47824)
default	09:58:50.625855-0500	runningboardd	Invalidating assertion 394-328-883205 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) from originator [osservice<com.apple.powerd>:328]
default	09:58:50.625956-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8161, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.627809-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.631262-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.631864-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:50.631980-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:50.632042-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.632348-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.633156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.633183-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.633203-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.633212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.633219-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.633225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.633646-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.656274-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:50.658907-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5200] Created node ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:50.658974-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f5200] Created node ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:50.698506-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:50.703746-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:47825 called from <private>
default	09:58:50.703816-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:47825 called from <private>
default	09:58:50.704075-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:50.704231-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-883206 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:50.704322-0500	runningboardd	Assertion 394-328-883206 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:50.705730-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:47825 called from <private>
default	09:58:50.705936-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(47825)
default	09:58:50.705965-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:47825 called from <private>
default	09:58:50.706181-0500	runningboardd	Invalidating assertion 394-328-883206 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) from originator [osservice<com.apple.powerd>:328]
default	09:58:50.705974-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:47825 called from <private>
default	09:58:50.706840-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:50.706970-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:50.707303-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(47825)
default	09:58:50.707647-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:47825 called from <private>
default	09:58:50.707659-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:47825 called from <private>
default	09:58:50.707673-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:47825 called from <private>
default	09:58:50.709254-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.8162, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:50.711436-0500	tccd	AUTHREQ_SUBJECT: msgID=395.8162, subject=com.nexy.assistant,
default	09:58:50.712393-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:50.712456-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:50.712529-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.712727-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.712810-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x873198000 at /Applications/Nexy.app
default	09:58:50.713116-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713138-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713160-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.713167-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713175-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.713184-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.713330-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.713376-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713387-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.713501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.713567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.713618-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.714195-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.731256-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xa66e706e0: iounit configuration changed > posting notification
default	09:58:50.731848-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:50.731862-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:50.731873-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
default	09:58:50.731894-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:50.734762-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:50.735126-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.737809-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41062796.41062805(501)>:53679] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-883207 target:53679 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:50.738049-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:47825 called from <private>
default	09:58:50.741096-0500	runningboardd	Assertion 394-328-883207 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) will be created as active
default	09:58:50.741637-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:50.741816-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:50.741883-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
default	09:58:50.741981-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:50.746450-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:50.747164-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.747406-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:50.747457-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:50.747503-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.748142-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748188-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748204-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.748230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748245-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.748255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.748301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748343-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748353-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.748382-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.748405-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.748414-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.748554-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.749087-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.749099-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.749109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.749118-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.749140-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.749165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.749176-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:50.830162-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:50.830473-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f47e8","name":"Nexy(53679)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:50.830560-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:50.830605-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:50.830632-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f47e8, Nexy(53679), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:50.830679-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f47e8, Nexy(53679), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2023 stopping recording
default	09:58:50.830703-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:50.830707-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:50.830786-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:50.830868-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:50.830996-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:50.831012-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:50.831007-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	09:58:50.831302-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:50.831223-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:50.831259-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.831351-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:50.831384-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:50.831456-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.831489-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:50.831511-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.831526-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:50.833235-0500	runningboardd	Invalidating assertion 394-328-883207 (target:[app<application.com.nexy.assistant.41062796.41062805(501)>:53679]) from originator [osservice<com.apple.powerd>:328]
default	09:58:50.834623-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:50.835815-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.835825-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.835838-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.835846-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:50.835854-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:50.835860-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:50.835937-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:50.932022-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa670b0040) Selecting device 0 from destructor
default	09:58:50.932037-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa670b0040)
default	09:58:50.932044-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa670b0040) not already running
default	09:58:50.932050-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa670b0040) disconnecting device 91
default	09:58:50.932058-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa670b0040) destroying ioproc 0xa for device 91
default	09:58:50.932102-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:50.932146-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:50.932357-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xa670b0040) nothing to setup
default	09:58:50.932374-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 0 device listeners to device 0
default	09:58:50.932380-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa670b0040) adding 0 device delegate listeners to device 0
default	09:58:50.932388-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 7 device listeners from device 91
default	09:58:50.932715-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa670b0040) removing 0 device delegate listeners from device 91
default	09:58:50.932740-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa670b0040)
default	09:58:50.937829-0500	Nexy	[0xa6625d400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:50.938617-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring jetsam update because this process is not memory-managed
default	09:58:50.938636-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring suspend because this process is not lifecycle managed
default	09:58:50.938646-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring GPU update because this process is not GPU managed
error	09:58:50.938803-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	09:58:50.938668-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] Ignoring memory limit update because this process is not memory-managed
default	09:58:50.939088-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53679.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:50.940711-0500	tccd	AUTHREQ_SUBJECT: msgID=53679.3, subject=com.nexy.assistant,
default	09:58:50.941713-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:50.941673-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	09:58:50.942257-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, running-active-NotVisible
default	09:58:50.959897-0500	Nexy	[0xa6625d400] invalidated after the last release of the connection object
default	09:58:50.960027-0500	Nexy	[0xa6625d400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	09:58:50.960567-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	09:58:50.960753-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53679.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:50.961843-0500	tccd	AUTHREQ_SUBJECT: msgID=53679.4, subject=com.nexy.assistant,
default	09:58:50.962594-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	09:58:50.976083-0500	Nexy	[0xa6625d400] invalidated after the last release of the connection object
default	09:58:50.976156-0500	Nexy	[0xa6625d400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	09:58:50.976265-0500	Nexy	[0xa6625d400] invalidated after the last release of the connection object
default	09:58:50.977782-0500	Nexy	[0xa6625d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:50.978337-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53679.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53679, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:50.979358-0500	tccd	AUTHREQ_SUBJECT: msgID=53679.5, subject=com.nexy.assistant,
default	09:58:50.980017-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	09:58:50.993580-0500	Nexy	[0xa6625d540] invalidated after the last release of the connection object
default	09:58:50.999315-0500	kernel	AMFI: Denying core dump for pid 53679 (Nexy)
default	09:58:51.999831-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f47e8","name":"Nexy(53679)"}, "details":null }
default	09:58:51.999861-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f47e8 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":53679})
default	09:58:51.999872-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":53679})
default	09:58:51.000298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:51.000475-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2023, PID = 53679, Name = sid:0x1f47e8, Nexy(53679), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:50.999413-0500	kernel	Nexy[53679] Corpse allowed 1 of 5
default	09:58:51.001095-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.001146-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.001164-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.001049-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.002131-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1403402 (Nexy) connectionID: 182C23 pid: 53679 in session 0x101
default	09:58:51.001265-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.002165-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1403402 (Nexy) acq:0xb6b569840 count:1
default	09:58:51.019047-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1403402 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1403402 (Nexy)"
)}
default	09:58:51.000912-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.001003-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:51.025154-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xd1af removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1403402 (Nexy)"
)}
default	09:58:51.035398-0500	runningboardd	[app<application.com.nexy.assistant.41062796.41062805(501)>:53679] termination reported by launchd (2, 11, 11)
default	09:58:51.035542-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.036042-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.036299-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.036386-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.037206-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:51.037353-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:51.040910-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::out-0 issue_detected_sample_time=2160.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	09:58:51.040966-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_47825.47718.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	09:58:51.042319-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: none (role: None) (endowments: (null))
default	09:58:51.042803-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 53679, name = Nexy
default	09:58:51.042598-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41062796.41062805(501)>: none (role: None) (endowments: (null))
default	09:58:51.043981-0500	launchservicesd	Hit the server for a process handle 106ec0200000d1af that resolved to: [app<application.com.nexy.assistant.41062796.41062805(501)>:53679]
default	09:58:51.048183-0500	gamepolicyd	Received state update for 53679 (app<application.com.nexy.assistant.41062796.41062805(501)>, none-NotVisible
default	09:58:51.057712-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1403402} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	09:58:51.057754-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb8e0: Nexy> state 3
default	09:58:51.057794-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	09:58:51.058624-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb8e0: Nexy> state 4
default	09:58:51.058638-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	09:58:51.104438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257600 at /Applications/Nexy.app
default	09:58:51.133373-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254000 at /Applications/Nexy.app
default	09:58:51.141258-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	09:58:54.330642-0500	ReportCrash	Enabling urgent submission for process Nexy
default	09:58:54.356683-0500	ReportCrash	Formulating fatal 309 report for corpse[53679] Nexy
default	09:58:54.362063-0500	ReportCrash	loadStoreInfo [platform 1] com.nexy.assistant from file:///Applications/Nexy.app/
default	09:58:54.441354-0500	osanalyticshelper	creating type 309 as /Users/sergiyzasorin/Library/Logs/DiagnosticReports/.Nexy-2026-01-09-095854.ips
default	09:58:54.466234-0500	osanalyticshelper	Saved type '309(<private>)' report (1 of max 25) at /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-095854.ips
default	09:58:54.466429-0500	osanalyticshelper	xpc log creation type 309 result success: /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-095854.ips
default	09:58:54.466675-0500	ReportCrash	client log create type 309 result success: /Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-095854.ips
default	09:58:54.505106-0500	ReportCrash	com.nexy.assistant is not a MetricKit client
default	09:58:54.515583-0500	ReportCrash	recordCrashEvent; isBeta 0, log: '/Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-095854.ips'
default	09:58:54.740502-0500	SubmitDiagInfo	Retiring (309) submitted '/Users/sergiyzasorin/Library/Logs/DiagnosticReports/Retired/Nexy-2026-01-09-095854.ips': success
