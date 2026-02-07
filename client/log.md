default	13:37:20.770632-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:37:20.777307-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:37:20.780560-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53267463.53267472(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:37:20.780639-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53267463.53267472(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:75320] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-75320-49392 target:app<application.com.nexy.assistant.53267463.53267472(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:37:20.780728-0500	runningboardd	Assertion 394-75320-49392 (target:app<application.com.nexy.assistant.53267463.53267472(501)>) will be created as active
default	13:37:20.783477-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:37:20.783509-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.53267463.53267472(501)>
default	13:37:20.783524-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:37:20.783591-0500	runningboardd	app<application.com.nexy.assistant.53267463.53267472(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:37:20.846862-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] is not RunningBoard jetsam managed.
default	13:37:20.846879-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] This process will not be managed.
default	13:37:20.846889-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.53267463.53267472(501)>:54698]
default	13:37:20.847174-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:20.848169-0500	gamepolicyd	Hit the server for a process handle 11176c6b0000d5aa that resolved to: [app<application.com.nexy.assistant.53267463.53267472(501)>:54698]
default	13:37:20.848212-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:20.851531-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.53267463.53267472(501)>:54698]
default	13:37:20.851604-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-49393 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:20.851746-0500	runningboardd	Assertion 394-394-49393 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:20.851959-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:20.851979-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:20.852004-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Set darwin role to: UserInteractive
default	13:37:20.852025-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:20.852072-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:20.852154-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] reported to RB as running
default	13:37:20.856323-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x3ae3ae com.nexy.assistant starting stopped process.
default	13:37:20.855623-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:54698" ID:394-357-49394 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:37:20.856005-0500	runningboardd	Assertion 394-357-49394 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:20.861861-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:20.861898-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:20.861929-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:20.862029-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:20.862267-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.53267463.53267472(501)>:54698]
default	13:37:20.860385-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:37:20.860583-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b95fc000: Nexy> state 2
default	13:37:20.860646-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:37:20.864168-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:20.864665-0500	runningboardd	Invalidating assertion 394-75320-49392 (target:app<application.com.nexy.assistant.53267463.53267472(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:75320]
default	13:37:20.864705-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:20.864743-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:20.864785-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:20.865123-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:20.864944-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:20.951389-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	13:37:20.953185-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.42, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	13:37:20.963835-0500	tccd	AUTHREQ_SUBJECT: msgID=489.42, subject=com.nexy.assistant,
default	13:37:20.965610-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	13:37:20.971324-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:20.984035-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	13:37:20.994678-0500	kernel	Nexy[54698] triggered unnest of range 0x1fa000000->0x1fc000000 of DYLD shared region in VM map 0xd4cbadcf6c4bcea1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:37:20.994708-0500	kernel	Nexy[54698] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xd4cbadcf6c4bcea1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:37:21.267455-0500	Nexy	[0x1069605e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:37:21.267555-0500	Nexy	[0x106960b20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:37:21.547466-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x106950320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:37:21.547758-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x106950320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:37:21.548003-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x106950320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:37:21.548238-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x106950320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:37:21.549887-0500	Nexy	[0x10696e310] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:37:21.550669-0500	Nexy	[0x738794000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:37:21.551002-0500	Nexy	[0x738794140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:37:21.551614-0500	Nexy	[0x738794280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:37:21.553723-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:37:21.554106-0500	Nexy	[0x7387943c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:37:21.554800-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:37:21.556582-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.1, subject=com.nexy.assistant,
default	13:37:21.557532-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	13:37:21.559257-0500	Nexy	Received configuration update from daemon (initial)
default	13:37:21.572328-0500	Nexy	[0x7387943c0] invalidated after the last release of the connection object
default	13:37:21.572958-0500	Nexy	server port 0x00003513, session port 0x00003513
default	13:37:21.574596-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.2414, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:37:21.574626-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:37:21.575733-0500	tccd	AUTHREQ_SUBJECT: msgID=387.2414, subject=com.nexy.assistant,
default	13:37:21.576554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	13:37:21.593888-0500	Nexy	New connection 0x47fb3 main
default	13:37:21.596376-0500	Nexy	CHECKIN: pid=54698
default	13:37:21.603732-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:54698" ID:394-357-49395 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:37:21.603818-0500	runningboardd	Assertion 394-357-49395 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:21.604011-0500	Nexy	CHECKEDIN: pid=54698 asn=0x0-0x3ae3ae foreground=0
default	13:37:21.604281-0500	Nexy	[0x7387943c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:37:21.604295-0500	Nexy	[0x7387943c0] Connection returned listener port: 0x4803
default	13:37:21.603876-0500	launchservicesd	CHECKIN:0x0-0x3ae3ae 54698 com.nexy.assistant
default	13:37:21.604311-0500	runningboardd	Invalidating assertion 394-357-49394 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:37:21.604703-0500	Nexy	[0x739744300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7387943c0.peer[357].0x739744300
default	13:37:21.605364-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:37:21.605485-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:37:21.606739-0500	Nexy	FRONTLOGGING: version 1
default	13:37:21.606748-0500	Nexy	Registered, pid=54698 ASN=0x0,0x3ae3ae
default	13:37:21.607040-0500	WindowServer	47fb3[CreateApplication]: Process creation: 0x0-0x3ae3ae (Nexy) connectionID: 47FB3 pid: 54698 in session 0x101
default	13:37:21.607393-0500	Nexy	[0x738794500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:37:21.608939-0500	Nexy	[0x7387943c0] Connection returned listener port: 0x4803
default	13:37:21.609688-0500	Nexy	BringForward: pid=54698 asn=0x0-0x3ae3ae bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:37:21.609838-0500	Nexy	BringFrontModifier: pid=54698 asn=0x0-0x3ae3ae Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:37:21.610554-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:37:21.612123-0500	Nexy	No persisted cache on this platform.
default	13:37:21.613390-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:37:21.614170-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:37:21.617038-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:37:21.617049-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:37:21.617100-0500	Nexy	Initializing connection
default	13:37:21.617142-0500	Nexy	Removing all cached process handles
default	13:37:21.617161-0500	Nexy	Sending handshake request attempt #1 to server
default	13:37:21.617171-0500	Nexy	Creating connection to com.apple.runningboard
default	13:37:21.617177-0500	Nexy	[0x738794640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:37:21.617542-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] as ready
default	13:37:21.618130-0500	Nexy	Handshake succeeded
default	13:37:21.618146-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.53267463.53267472(501)>
default	13:37:21.618704-0500	Nexy	[0x7387943c0] Connection returned listener port: 0x4803
default	13:37:21.619676-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 54698
default	13:37:21.624674-0500	Nexy	[0x7387943c0] Connection returned listener port: 0x4803
default	13:37:21.628109-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:37:21.628130-0500	Nexy	[0x7387948c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:37:21.628238-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:37:21.628297-0500	Nexy	[0x738794a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:37:21.630218-0500	Nexy	[0x738794a00] Connection returned listener port: 0x6803
default	13:37:21.631666-0500	Nexy	Registered process with identifier 54698-1014552
default	13:37:23.141048-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B5E73382-B772-49EE-B7E9-CCAD6ADED7BE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.60284,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe2823d1f tp_proto=0x06"
default	13:37:23.141186-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:60284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1285301 t_state: SYN_SENT process: Nexy:54698 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa47f60b8
default	13:37:23.151784-0500	kernel	tcp connected: [<IPv4-redacted>:60284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1285301 t_state: ESTABLISHED process: Nexy:54698 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa47f60b8
default	13:37:23.152128-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:60284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1285301 t_state: FIN_WAIT_1 process: Nexy:54698 Duration: 0.011 sec Conn_Time: 0.011 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 11.000 ms rttvar: 5.500 ms base rtt: 11 ms so_error: 0 svc/tc: 0 flow: 0xa47f60b8
default	13:37:23.152139-0500	kernel	tcp_connection_summary [<IPv4-redacted>:60284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1285301 t_state: FIN_WAIT_1 process: Nexy:54698 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:37:24.260159-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:37:24.261437-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:37:24.263628-0500	Nexy	[0x738794dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:37:24.268280-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53267463.53267472 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53267463.53267472>
default	13:37:24.275546-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:37:24.277914-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:37:24.278069-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:37:24.278214-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:37:24.278227-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:37:24.278665-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:37:24.278799-0500	Nexy	[0x738794f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:37:24.279253-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:37:24.279526-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:37:24.286026-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.2, subject=com.nexy.assistant,
default	13:37:24.286745-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
default	13:37:24.299686-0500	Nexy	[0x738794f00] invalidated after the last release of the connection object
default	13:37:24.299746-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:37:24.302689-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	13:37:24.303833-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.923, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:24.304903-0500	tccd	AUTHREQ_SUBJECT: msgID=399.923, subject=com.nexy.assistant,
default	13:37:24.305515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
error	13:37:24.318243-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:37:24.319109-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.925, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:24.320132-0500	tccd	AUTHREQ_SUBJECT: msgID=399.925, subject=com.nexy.assistant,
default	13:37:24.320713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
default	13:37:24.335910-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:37:24.336049-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x73b1a9a40> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:37:24.350094-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:37:24.350104-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:37:24.350635-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	13:37:24.355220-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:37:24.355377-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:37:24.360304-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:37:24.368717-0500	Nexy	[0x738794f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:37:24.871249-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x739479540) Selecting device 85 from constructor
default	13:37:24.871264-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:24.871273-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:24.871759-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x739479540) nothing to teardown
default	13:37:24.871768-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x739479540) connecting device 85
default	13:37:24.871962-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x739479540) Device ID: 85 (Input:No | Output:Yes): true
default	13:37:24.872097-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x739479540) created ioproc 0xa for device 85
default	13:37:24.872226-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 7 device listeners to device 85
default	13:37:24.872427-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 85
default	13:37:24.872442-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x739479540)
default	13:37:24.872558-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	13:37:24.872570-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:37:24.872576-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:37:24.872587-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:37:24.872597-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:37:24.872709-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:37:24.872721-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:37:24.872728-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:37:24.872733-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device listeners from device 0
default	13:37:24.872752-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 0
default	13:37:24.872759-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:24.872782-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:37:24.872899-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x739479540) caller requesting device change from 85 to 91
default	13:37:24.872908-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:24.872914-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:24.872919-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x739479540) disconnecting device 85
default	13:37:24.872924-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x739479540) destroying ioproc 0xa for device 85
default	13:37:24.873034-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:37:24.874789-0500	Nexy	[0x738795180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:37:24.877310-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ee03e","name":"Nexy(54698)"}, "details":{"PID":54698,"session_type":"Primary"} }
default	13:37:24.877413-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":54698}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ee03e, sessionType: 'prim', isRecording: false }, 
]
default	13:37:24.878388-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 54698, name = Nexy
default	13:37:24.878818-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x739779000 with ID: 0x1ee03e
default	13:37:24.880229-0500	Nexy	[0x7387952c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:37:24.880857-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=234926121156609 }
default	13:37:24.880881-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:37:24.880956-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:37:24.881129-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x739479540) connecting device 91
default	13:37:24.881278-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x739479540) Device ID: 91 (Input:Yes | Output:No): true
default	13:37:24.883054-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.926, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:24.885071-0500	tccd	AUTHREQ_SUBJECT: msgID=399.926, subject=com.nexy.assistant,
default	13:37:24.885875-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
default	13:37:24.906471-0500	tccd	AUTHREQ_PROMPTING: msgID=399.926, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:37:26.778151-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-49393 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698])
default	13:37:26.978809-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:26.978821-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:26.978831-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:26.978844-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:26.982419-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:26.983031-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:27.380505-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x739479540) created ioproc 0xa for device 91
default	13:37:27.380722-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 7 device listeners to device 91
default	13:37:27.380976-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 91
default	13:37:27.380994-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x739479540)
default	13:37:27.381009-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:37:27.381023-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:37:27.381222-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	13:37:27.381237-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:37:27.379347-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    467 = "<TCCDEventSubscriber: token=467, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	13:37:27.381244-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:37:27.381355-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:37:27.381371-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:37:27.381376-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:37:27.381382-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 7 device listeners from device 85
default	13:37:27.381556-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 85
default	13:37:27.381563-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:27.382035-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:37:27.382589-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:37:27.383635-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.927, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:27.385262-0500	tccd	AUTHREQ_SUBJECT: msgID=399.927, subject=com.nexy.assistant,
default	13:37:27.388492-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
default	13:37:27.407594-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:37:27.407651-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:37:27.407741-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x73b1769d0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:37:27.407970-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:37:27.408929-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.928, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:27.413081-0500	tccd	AUTHREQ_SUBJECT: msgID=399.928, subject=com.nexy.assistant,
default	13:37:27.414763-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59e00 at /Applications/Nexy.app
default	13:37:27.434278-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.929, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:27.435406-0500	tccd	AUTHREQ_SUBJECT: msgID=399.929, subject=com.nexy.assistant,
default	13:37:27.436038-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:37:27.454237-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:37:27.453804-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:37:27.454539-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:37:27.456675-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:37:27.459223-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_3359.3192.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:37:27.459372-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_3359.3192.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:37:27.459754-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:37:27.454242-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:37:27.560794-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:37:27.565097-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49402 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:27.565181-0500	runningboardd	Assertion 394-328-49402 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:27.565737-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:27.565922-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:27.566065-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:27.566215-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:27.564208-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:3359 called from <private>
default	13:37:27.564228-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:37:27.574759-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:37:27.575277-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:37:27.570813-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:27.571120-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:27.571146-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:27.571154-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:27.571225-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:27.571644-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:27.571715-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:27.575934-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:27.576009-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:27.576059-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:27.576126-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:27.576148-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:27.576178-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:27.579464-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:27.581321-0500	runningboardd	Invalidating assertion 394-328-49402 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.powerd>:328]
default	13:37:27.583072-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee03e","name":"Nexy(54698)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:37:27.583308-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:37:27.583780-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:27.584036-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee03e, Nexy(54698), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:37:27.584110-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:27.584105-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.584171-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:27.576195-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:27.576220-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:27.584477-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:37:27.576235-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:27.584526-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee03e, Nexy(54698), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 63 starting recording
default	13:37:27.576244-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:27.576288-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:27.584733-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.576368-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:27.585416-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:27.576431-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:27.585604-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:37:27.585225-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.585715-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee03e, Nexy(54698), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	13:37:27.585405-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.585412-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:27.585824-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:37:27.585460-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:27.585829-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
fault	13:37:27.582353-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53267463.53267472 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53267463.53267472>
default	13:37:27.585875-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:37:27.586415-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:27.585989-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.930, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:27.593441-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
fault	13:37:27.594742-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53267463.53267472 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53267463.53267472>
default	13:37:27.596899-0500	tccd	AUTHREQ_SUBJECT: msgID=399.930, subject=com.nexy.assistant,
default	13:37:27.601030-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:27.601047-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:27.601197-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:27.602015-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:27.604872-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:27.605101-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:27.605108-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:27.605209-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:27.611423-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:27.611624-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:27.611634-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:27.611900-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:27.627099-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.627367-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.627449-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 3
default	13:37:27.618221-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:27.618654-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:27.618920-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:27.626916-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.619215-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:27.657141-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.657203-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.657337-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.657352-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.657363-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.657372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:27.680322-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:37:27.690704-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:27.690735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.690902-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.691054-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.691104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.691169-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.691247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:27.701947-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.701963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.701980-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.701989-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.702001-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.702013-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:27.702188-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:27.778888-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:37:27.781040-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:3359 called from <private>
default	13:37:27.781949-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49407 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:27.782723-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:27.783159-0500	runningboardd	Assertion 394-328-49407 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:27.782763-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:27.783581-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:37:27.783987-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:27.784063-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:27.784152-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:27.784251-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:27.789329-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:27.794307-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:27.794397-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:27.794459-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:27.794596-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:27.795058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.795103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.795124-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.795137-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.795147-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.795156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:27.795337-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:27.822693-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49408 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:27.822794-0500	runningboardd	Assertion 394-328-49408 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:27.823405-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:3359 called from <private>
default	13:37:27.823524-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
error	13:37:27.824791-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	13:37:27.824810-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3359 called from <private>
default	13:37:27.824884-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:37:27.825443-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee03e","name":"Nexy(54698)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:37:27.825515-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3359 called from <private>
default	13:37:27.825524-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:27.825557-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:27.825608-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:37:27.825752-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:27.825643-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee03e, Nexy(54698), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	13:37:27.825694-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee03e, Nexy(54698), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 63 stopping recording
default	13:37:27.825789-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:37:27.825889-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:27.825793-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:37:27.826014-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:27.825608-0500	runningboardd	Invalidating assertion 394-328-49408 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.powerd>:328]
default	13:37:27.825774-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:27.825782-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:27.826682-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:37:27.826864-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	13:37:27.826354-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:37:27.826364-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:37:27.827312-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.827080-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:37:27.827351-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.827126-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:27.827373-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.827236-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.827400-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:37:27.827948-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:27.828213-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:27.828224-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:27.828241-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:27.827847-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:27.828250-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3359 called from <private>
default	13:37:27.827949-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	13:37:27.833398-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:27.833451-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:27.833494-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:27.833617-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:27.833983-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.833997-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.834008-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.834023-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:27.834032-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:27.834038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:27.834218-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:27.895531-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:27.895551-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:27.895570-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:27.895607-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:27.898507-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:27.899074-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:27.938278-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x739479540) Selecting device 0 from destructor
default	13:37:27.938292-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:27.938298-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:27.938303-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x739479540) disconnecting device 91
default	13:37:27.938308-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x739479540) destroying ioproc 0xa for device 91
default	13:37:27.938339-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:37:27.938369-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:37:27.938499-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x739479540) nothing to setup
default	13:37:27.938513-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device listeners to device 0
default	13:37:27.938520-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 0
default	13:37:27.938525-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 7 device listeners from device 91
default	13:37:27.938716-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 91
default	13:37:27.938728-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:30.479819-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:30.479866-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3359 called from <private>
default	13:37:30.479880-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:30.481571-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.481610-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:30.481620-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:30.491687-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:30.491725-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:30.491978-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:30.492007-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:30.492014-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3359 called from <private>
default	13:37:30.492722-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.492748-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:30.492759-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:30.494820-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.494849-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.494944-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.495003-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:30.495012-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:30.511574-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:30.511615-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:30.511998-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:3358 called from <private>
default	13:37:30.512012-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:3358 called from <private>
default	13:37:30.512167-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.516042-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.516442-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:3358 called from <private>
default	13:37:30.516453-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:3358 called from <private>
default	13:37:30.516500-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:30.516506-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:30.516514-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:30.516520-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:30.516633-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.516649-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:30.516915-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:30.517014-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:30.517167-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:30.517291-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:30.517402-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:30.517541-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:30.517592-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:30.523348-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.523672-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:30.523684-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:30.523710-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:30.523720-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:30.524069-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.524096-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:30.524199-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:30.526191-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.526670-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:30.526823-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:30.527774-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.528141-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:30.528183-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:30.528513-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:30.528690-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:30.529231-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:30.529494-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:30.529951-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:31.438771-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:37:32.605851-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	13:37:40.944207-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x739479540) Selecting device 85 from constructor
default	13:37:40.944232-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:40.944242-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:40.944250-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x739479540) nothing to teardown
default	13:37:40.944256-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x739479540) connecting device 85
default	13:37:40.944402-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x739479540) Device ID: 85 (Input:No | Output:Yes): true
default	13:37:40.944571-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x739479540) created ioproc 0xb for device 85
default	13:37:40.944757-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 7 device listeners to device 85
default	13:37:40.945017-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 85
default	13:37:40.945030-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x739479540)
default	13:37:40.945143-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	13:37:40.945154-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:37:40.945167-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:37:40.945178-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:37:40.945188-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:37:40.945337-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:37:40.945354-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:37:40.945364-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:37:40.945373-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device listeners from device 0
default	13:37:40.945379-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 0
default	13:37:40.945384-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:40.945413-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:37:40.945498-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x739479540) caller requesting device change from 85 to 91
default	13:37:40.945513-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:40.945522-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:40.945528-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x739479540) disconnecting device 85
default	13:37:40.945550-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x739479540) destroying ioproc 0xb for device 85
default	13:37:40.945594-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	13:37:40.945656-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:37:40.945769-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x739479540) connecting device 91
default	13:37:40.945884-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x739479540) Device ID: 91 (Input:Yes | Output:No): true
default	13:37:40.948345-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.933, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:40.950964-0500	tccd	AUTHREQ_SUBJECT: msgID=399.933, subject=com.nexy.assistant,
default	13:37:40.952052-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:40.979240-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x739479540) created ioproc 0xb for device 91
default	13:37:40.979439-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 7 device listeners to device 91
default	13:37:40.979625-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 91
default	13:37:40.979636-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x739479540)
default	13:37:40.979649-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:37:40.979660-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:37:40.979830-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	13:37:40.979840-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:37:40.979845-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:37:40.979938-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:37:40.979949-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x739479540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:37:40.979957-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:37:40.979963-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 7 device listeners from device 85
default	13:37:40.980132-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 85
default	13:37:40.980140-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:40.980150-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	13:37:40.980715-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:37:40.982039-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.934, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:40.983249-0500	tccd	AUTHREQ_SUBJECT: msgID=399.934, subject=com.nexy.assistant,
default	13:37:40.983892-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:41.002650-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x73b175e60, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:37:41.002867-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:37:41.003952-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.935, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:41.005120-0500	tccd	AUTHREQ_SUBJECT: msgID=399.935, subject=com.nexy.assistant,
default	13:37:41.005770-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:41.025455-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.936, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:41.027128-0500	tccd	AUTHREQ_SUBJECT: msgID=399.936, subject=com.nexy.assistant,
default	13:37:41.027889-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:41.046911-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:37:41.047090-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:37:41.048896-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:3359 called from <private>
default	13:37:41.048922-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:37:41.048953-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:37:41.049825-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:41.049979-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:41.049998-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:41.050004-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:41.053157-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:41.053172-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:41.056406-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49422 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:41.056906-0500	runningboardd	Assertion 394-328-49422 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:41.058022-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:37:41.054079-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:41.058348-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:41.058585-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:41.058698-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:41.058728-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:37:41.058839-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:41.062136-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:41.062175-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:41.062226-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:41.062277-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:41.064069-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:41.064099-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:41.064112-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:41.064124-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:41.064156-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:41.064224-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:41.064307-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:41.069338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.937, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:41.072734-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee03e","name":"Nexy(54698)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:37:41.072834-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:37:41.072936-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ee03e, Nexy(54698), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:37:41.073106-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:41.073420-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:41.073550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:41.073534-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.073755-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:37:41.073798-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee03e, Nexy(54698), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 63 starting recording
default	13:37:41.073998-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:41.074134-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:37:41.073570-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee03e, Nexy(54698), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:37:41.074215-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee03e, Nexy(54698), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	13:37:41.071837-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:41.071857-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:41.074248-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.075006-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.076216-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:41.074223-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.072062-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:41.074350-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:37:41.074811-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:37:41.074362-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:37:41.076956-0500	runningboardd	Invalidating assertion 394-328-49422 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.powerd>:328]
default	13:37:41.082892-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:41.082911-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:41.083031-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:41.084368-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:41.084640-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:41.084692-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:41.084767-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:41.084891-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:41.084937-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:41.091370-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:41.091633-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:41.091674-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:41.091820-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:41.091830-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:41.091963-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:41.092075-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:41.092133-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:41.092283-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:41.092356-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:41.092401-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:41.092547-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:41.092683-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:41.092734-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:41.092787-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:41.092945-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:41.093035-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:41.093156-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:41.093210-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:41.104093-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:41.104351-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:41.104593-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:41.141520-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:41.141695-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.142108-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.175354-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee03e, Nexy(54698), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	13:37:41.184180-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:41.216181-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:37:41.216366-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:37:41.218125-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49427 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:41.218344-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:3359 called from <private>
default	13:37:41.218389-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:3359 called from <private>
default	13:37:41.218770-0500	runningboardd	Assertion 394-328-49427 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:41.218780-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:37:41.219412-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:41.219430-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:41.219698-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3359 called from <private>
default	13:37:41.219862-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
error	13:37:41.219878-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	13:37:41.219887-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:41.219796-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:41.219975-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:41.219809-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:41.219825-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:41.219932-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:41.228868-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:41.230792-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:41.230998-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:41.231112-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.231462-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.232000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.253721-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:37:41.256866-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_3359.3192.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:37:41.256934-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_3359.3192.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:37:41.295555-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:41.295568-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:41.295586-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:41.295609-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:41.298358-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:41.298990-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:41.327770-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:37:41.329835-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:3359 called from <private>
default	13:37:41.329875-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:3359 called from <private>
default	13:37:41.330349-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:3359 called from <private>
default	13:37:41.330209-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49428 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:41.330338-0500	runningboardd	Assertion 394-328-49428 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:41.330753-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:41.330816-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:41.330862-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:41.330923-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:41.332647-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:37:41.333244-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:37:41.330508-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:37:41.331428-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:41.331600-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:41.331619-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3359 called from <private>
default	13:37:41.331625-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3359 called from <private>
default	13:37:41.333875-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:41.336927-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.939, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:37:41.334120-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3359 called from <private>
default	13:37:41.334187-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3359 called from <private>
default	13:37:41.334242-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:41.338036-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:41.338424-0500	runningboardd	Invalidating assertion 394-328-49428 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.powerd>:328]
default	13:37:41.339133-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:41.339929-0500	tccd	AUTHREQ_SUBJECT: msgID=399.939, subject=com.nexy.assistant,
default	13:37:41.341614-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad59800 at /Applications/Nexy.app
default	13:37:41.344695-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:41.344794-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:41.344852-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.345079-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.345313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345325-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345339-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.345346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345352-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.345364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.345685-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:41.345748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345793-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345828-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.345864-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.345899-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.346153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.346630-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:41.366689-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53267463.53267472(501)>:54698] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49429 target:54698 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:37:41.367065-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:3359 called from <private>
default	13:37:41.367149-0500	runningboardd	Assertion 394-328-49429 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) will be created as active
default	13:37:41.372004-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:41.372046-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:37:41.372080-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.372324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372344-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372358-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372373-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372395-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.372415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372456-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372492-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.372560-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:41.372740-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372761-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372766-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.372773-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.372780-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.372796-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:37:41.507236-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:37:41.507507-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee03e","name":"Nexy(54698)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:37:41.507600-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:41.507642-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:37:41.507668-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee03e, Nexy(54698), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	13:37:41.507708-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee03e, Nexy(54698), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 63 stopping recording
default	13:37:41.507734-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:37:41.507734-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:37:41.507764-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:37:41.507797-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 63, PID = 54698, Name = sid:0x1ee03e, Nexy(54698), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:37:41.507920-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:37:41.507936-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:37:41.507989-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	13:37:41.508198-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:41.508240-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.508281-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:41.508325-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:37:41.509146-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.509171-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:37:41.509407-0500	runningboardd	Invalidating assertion 394-328-49429 (target:[app<application.com.nexy.assistant.53267463.53267472(501)>:54698]) from originator [osservice<com.apple.powerd>:328]
default	13:37:41.509352-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:37:41.509416-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	13:37:41.510431-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:37:41.512161-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.512171-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.512190-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.512196-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:41.512202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:41.512208-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:41.512286-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:37:41.609023-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x739479540) Selecting device 0 from destructor
default	13:37:41.609038-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x739479540)
default	13:37:41.609045-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x739479540) not already running
default	13:37:41.609050-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x739479540) disconnecting device 91
default	13:37:41.609057-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x739479540) destroying ioproc 0xb for device 91
default	13:37:41.609100-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:37:41.609138-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:37:41.609307-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x739479540) nothing to setup
default	13:37:41.609318-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device listeners to device 0
default	13:37:41.609323-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x739479540) adding 0 device delegate listeners to device 0
default	13:37:41.609330-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 7 device listeners from device 91
default	13:37:41.609550-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x739479540) removing 0 device delegate listeners from device 91
default	13:37:41.609563-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x739479540)
default	13:37:41.611996-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring jetsam update because this process is not memory-managed
default	13:37:41.612014-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring suspend because this process is not lifecycle managed
default	13:37:41.612024-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring GPU update because this process is not GPU managed
default	13:37:41.612044-0500	runningboardd	[app<application.com.nexy.assistant.53267463.53267472(501)>:54698] Ignoring memory limit update because this process is not memory-managed
default	13:37:41.614645-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53267463.53267472(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:37:41.615307-0500	gamepolicyd	Received state update for 54698 (app<application.com.nexy.assistant.53267463.53267472(501)>, running-active-NotVisible
default	13:37:43.764209-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3359)
default	13:37:43.764342-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3359 called from <private>
default	13:37:43.764352-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3359 called from <private>
default	13:37:43.771543-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.771610-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:43.771617-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:43.781604-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:43.781639-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:43.782855-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3359)
default	13:37:43.782888-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3359 called from <private>
default	13:37:43.782897-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3359 called from <private>
default	13:37:43.783906-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.783931-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:43.783938-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:43.787391-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.787441-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.787935-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.788166-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:43.788177-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:43.788188-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:43.788201-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:43.788209-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:43.788240-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:43.788382-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:43.788389-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:43.789940-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:3358 called from <private>
default	13:37:43.790002-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:3358 called from <private>
default	13:37:43.805738-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:43.805799-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:43.805951-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.813045-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.813666-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:43.813683-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:43.813743-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:43.813750-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:43.813756-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:43.813762-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:43.813908-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.814239-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:3358 called from <private>
default	13:37:43.814332-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:3358 called from <private>
default	13:37:43.818062-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.818484-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:3358 called from <private>
default	13:37:43.818495-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:3358 called from <private>
default	13:37:43.818510-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:3358 called from <private>
default	13:37:43.818520-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:3358 called from <private>
default	13:37:43.818685-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.818701-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:43.818918-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:43.819050-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(3358)
default	13:37:43.819253-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:3358 called from <private>
default	13:37:43.819410-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:3358 called from <private>
default	13:37:43.822114-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(3358)
default	13:37:43.822165-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:3358 called from <private>
default	13:37:43.822171-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:3358 called from <private>
default	13:37:44.619445-0500	Nexy	[0x738795680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:37:44.620632-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:37:44.622664-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.3, subject=com.nexy.assistant,
default	13:37:44.623790-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	13:37:44.657191-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[54698], responsiblePID[54698], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:37:44.657572-0500	Nexy	[0x738795680] invalidated after the last release of the connection object
default	13:37:44.814723-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad30000 at /Applications/Nexy.app
default	13:37:44.840528-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	13:37:44.842952-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:37:44.845197-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:37:45.436963-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	13:37:45.441014-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:37:45.456661-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
error	13:37:49.330363-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:37:49.330288-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:37:52.919420-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:37:52.936953-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	13:37:53.213558-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:37:53.218247-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
default	13:37:57.666801-0500	Nexy	[0x738795540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:37:57.668349-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:37:57.670741-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.4, subject=com.nexy.assistant,
default	13:37:57.672142-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:37:57.701467-0500	Nexy	[0x738795540] invalidated after the last release of the connection object
default	13:37:57.704205-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	13:37:57.707128-0500	Nexy	[0x738795540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	13:37:57.707317-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	13:37:57.707998-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	13:37:57.719887-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=51214.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=51214, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	13:37:57.719913-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=51214, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:37:57.720861-0500	tccd	AUTHREQ_SUBJECT: msgID=51214.2, subject=com.nexy.assistant,
default	13:37:57.721493-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:37:57.747596-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.2442, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:37:57.747628-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:37:57.749070-0500	tccd	AUTHREQ_SUBJECT: msgID=387.2442, subject=com.nexy.assistant,
default	13:37:57.750036-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:37:57.769850-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	13:37:57.814974-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:37:57.815057-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:37:57.815095-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:37:57.816198-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:57.816212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:57.816226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:57.816234-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:37:57.816241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:37:57.816247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:37:57.816390-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:38:00.802140-0500	Nexy	[0x738795680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:38:00.802752-0500	Nexy	[0x7387957c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:38:00.803112-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:00.803455-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:00.805243-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.6, subject=com.nexy.assistant,
default	13:38:00.806107-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad5a400 at /Applications/Nexy.app
default	13:38:00.806699-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.5, subject=com.nexy.assistant,
default	13:38:00.808341-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:00.821711-0500	Nexy	[0x7387957c0] invalidated after the last release of the connection object
default	13:38:00.821826-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	13:38:00.822861-0500	Nexy	[0x7387957c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:38:00.823309-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:00.824451-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.7, subject=com.nexy.assistant,
default	13:38:00.825099-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad5a400 at /Applications/Nexy.app
default	13:38:00.825284-0500	Nexy	[0x738795680] invalidated after the last release of the connection object
default	13:38:00.841403-0500	tccd	AUTHREQ_PROMPTING: msgID=54698.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:38:02.903331-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    467 = "<TCCDEventSubscriber: token=467, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	13:38:02.904174-0500	Nexy	[0x7387957c0] invalidated after the last release of the connection object
default	13:38:02.906094-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:38:02.915611-0500	Nexy	[0x7387957c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	13:38:02.917196-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54635.21, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=54635, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	13:38:02.921155-0500	tccd	AUTHREQ_SUBJECT: msgID=54635.21, subject=com.nexy.assistant,
default	13:38:02.922543-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad5a400 at /Applications/Nexy.app
default	13:38:02.947325-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54635.22, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=54635, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	13:38:02.948791-0500	tccd	AUTHREQ_SUBJECT: msgID=54635.22, subject=com.nexy.assistant,
default	13:38:02.949750-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad5a400 at /Applications/Nexy.app
default	13:38:02.975963-0500	Nexy	[0x738795680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	13:38:02.977850-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	13:38:02.977942-0500	Nexy	<private> 0x739780740: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	13:38:02.978025-0500	Nexy	<private> 0x739780740: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	13:38:02.979593-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	13:38:03.001247-0500	Nexy	[0x738795900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	13:38:03.002378-0500	Nexy	[0x738795900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.002469-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	13:38:03.002684-0500	Nexy	Will add XPC store with options: <private> <private>
default	13:38:03.006012-0500	Nexy	[0x738cf83c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.007160-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.423, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.007256-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.008680-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.423, subject=com.nexy.assistant,
default	13:38:03.009535-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.031821-0500	Nexy	[0x738cf83c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.031949-0500	Nexy	[0x738cf83c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.032063-0500	Nexy	[0x738cf8500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.032938-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.424, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.032978-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.034286-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.424, subject=com.nexy.assistant,
default	13:38:03.035031-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.057110-0500	Nexy	[0x738cf8500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.057182-0500	Nexy	[0x738cf8500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.057240-0500	Nexy	[0x738cf8640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.058222-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.425, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.058257-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.059803-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.425, subject=com.nexy.assistant,
default	13:38:03.060734-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.083003-0500	Nexy	[0x738cf8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.083071-0500	Nexy	[0x738cf8640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.083127-0500	Nexy	[0x738cf8780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.083998-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.426, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.084033-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.085438-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.426, subject=com.nexy.assistant,
default	13:38:03.086415-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.111641-0500	Nexy	[0x738cf8780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.111710-0500	Nexy	[0x738cf8780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.122831-0500	Nexy	Did add XPC store
default	13:38:03.122848-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	13:38:03.125195-0500	Nexy	0x739778880: Using cached account information
default	13:38:03.126180-0500	Nexy	[0x7387f36b0] Session created.
default	13:38:03.126193-0500	Nexy	[0x7387f36b0] Session created with Mach Service: <private>
default	13:38:03.126202-0500	Nexy	[0x738cf8dc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	13:38:03.126312-0500	Nexy	[0x7387f36b0] Session activated
default	13:38:03.128520-0500	Nexy	[0x738cf8dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.128528-0500	Nexy	[0x7387f36b0] Session canceled.
default	13:38:03.128556-0500	Nexy	[0x7387f36b0] Disposing of session
default	13:38:03.128983-0500	Nexy	[0x738cf8dc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	13:38:03.129597-0500	Nexy	[0x738cf8dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.129621-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	13:38:03.129645-0500	Nexy	Will add XPC store with options: <private> <private>
default	13:38:03.133714-0500	Nexy	[0x738cfb840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.134830-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.427, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.134862-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.136393-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.427, subject=com.nexy.assistant,
default	13:38:03.137243-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.166171-0500	Nexy	[0x738cfb840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.166274-0500	Nexy	[0x738cfb840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.166357-0500	Nexy	[0x738cfb980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.167531-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.428, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.167567-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.171154-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.428, subject=com.nexy.assistant,
default	13:38:03.172375-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.198827-0500	Nexy	[0x738cfb980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.198901-0500	Nexy	[0x738cfb980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.198962-0500	Nexy	[0x738cfbac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.199883-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.429, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.199929-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.201512-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.429, subject=com.nexy.assistant,
default	13:38:03.202656-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.226346-0500	Nexy	[0x738cfbac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.226418-0500	Nexy	[0x738cfbac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.226480-0500	Nexy	[0x738cfbc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.227482-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.430, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.227520-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.229167-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.430, subject=com.nexy.assistant,
default	13:38:03.230046-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.255083-0500	Nexy	[0x738cfbc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.255160-0500	Nexy	[0x738cfbc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.262594-0500	Nexy	Did add XPC store
default	13:38:03.262665-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	13:38:03.262826-0500	Nexy	[0x738cfbe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	13:38:03.263520-0500	Nexy	[0x738cfbe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.263542-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	13:38:03.263561-0500	Nexy	Will add XPC store with options: <private> <private>
default	13:38:03.267611-0500	Nexy	[0x738d1e940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.268796-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.431, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.268838-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.273852-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.431, subject=com.nexy.assistant,
default	13:38:03.275518-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.305161-0500	Nexy	[0x738d1e940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.305290-0500	Nexy	[0x738d1e940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.305378-0500	Nexy	[0x738d1ea80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.306682-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.432, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.306723-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.308681-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.432, subject=com.nexy.assistant,
default	13:38:03.309906-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.337274-0500	Nexy	[0x738d1ea80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.337429-0500	Nexy	[0x738d1ea80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.337510-0500	Nexy	[0x738d1ebc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.338804-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.433, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.338846-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.340886-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.433, subject=com.nexy.assistant,
default	13:38:03.341758-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.368168-0500	Nexy	[0x738d1ebc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.368262-0500	Nexy	[0x738d1ebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.368351-0500	Nexy	[0x738d1ed00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	13:38:03.369524-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.434, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.369561-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.371169-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.434, subject=com.nexy.assistant,
default	13:38:03.372188-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.395009-0500	Nexy	[0x738d1ed00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:03.395064-0500	Nexy	[0x738d1ed00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:38:03.396164-0500	Nexy	Did add XPC store
default	13:38:03.396183-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	13:38:03.415128-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.435, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.415163-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.416753-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.435, subject=com.nexy.assistant,
default	13:38:03.417515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:03.441975-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54648.436, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	13:38:03.442013-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=54648, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:03.443440-0500	tccd	AUTHREQ_SUBJECT: msgID=54648.436, subject=com.nexy.assistant,
default	13:38:03.444262-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97ad58000 at /Applications/Nexy.app
default	13:38:05.674606-0500	Nexy	[0x738d1f0c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	13:38:07.876600-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	13:38:16.836666-0500	Nexy	[0x738d1f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:38:16.838268-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:16.840604-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.8, subject=com.nexy.assistant,
default	13:38:16.841985-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:16.868393-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[54698], responsiblePID[54698], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:38:16.868918-0500	Nexy	[0x738d1f200] invalidated after the last release of the connection object
default	13:38:16.920823-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	13:38:16.942334-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:16.946779-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:38:19.278891-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	13:38:19.319411-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	13:38:19.319459-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	13:38:19.319551-0500	Nexy	<private> 0x739780740: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	13:38:19.335567-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	13:38:19.335668-0500	Nexy	[0x738cf8780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:19.335685-0500	Nexy	[0x738cf8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:19.335724-0500	Nexy	[0x738cf8500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:19.335735-0500	Nexy	[0x738cf83c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:38:19.889720-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	13:38:20.035634-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	13:38:20.445055-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	13:38:20.445398-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:20.448060-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	13:38:20.449794-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:20.517039-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:20.517043-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:20.522000-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:38:20.522254-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:38:23.777669-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	13:38:23.801148-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:23.813049-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	13:38:23.921416-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	13:38:23.922168-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:23.923166-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	13:38:23.923361-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:23.957051-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:23.958547-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:38:23.960256-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:23.961421-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:38:29.876105-0500	Nexy	server port 0x00011133, session port 0x00003513
default	13:38:29.877433-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.2465, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:38:29.877463-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:38:29.879743-0500	tccd	AUTHREQ_SUBJECT: msgID=387.2465, subject=com.nexy.assistant,
default	13:38:29.882091-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:32.987529-0500	Nexy	[0x738d1f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:38:32.988091-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:38:32.988272-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:32.989372-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.9, subject=com.nexy.assistant,
default	13:38:32.990102-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:33.004570-0500	Nexy	[0x738d1f200] invalidated after the last release of the connection object
default	13:38:33.004714-0500	Nexy	[0x738d1f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:38:33.005143-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:38:33.005316-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=54698.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=54698, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:38:33.006186-0500	tccd	AUTHREQ_SUBJECT: msgID=54698.10, subject=com.nexy.assistant,
default	13:38:33.006849-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:33.020350-0500	Nexy	[0x738d1f200] invalidated after the last release of the connection object
default	13:38:33.020426-0500	Nexy	[0x738d1f200] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:38:33.020518-0500	Nexy	[0x738d1f200] invalidated after the last release of the connection object
default	13:38:33.020602-0500	Nexy	[0x738d1f340] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:38:33.020698-0500	Nexy	[0x738d1f340] invalidated after the last release of the connection object
default	13:38:33.032499-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	13:38:33.057811-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	13:38:33.062611-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:38:36.683518-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	13:38:36.719556-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	13:38:37.451911-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:37.451919-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:37.456043-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:38:37.456800-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:38:40.959345-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad30000 at /Applications/Nexy.app
default	13:38:40.986519-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	13:38:40.997452-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	13:38:41.046492-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	13:38:41.046713-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:41.047306-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	13:38:41.048639-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	13:38:41.049285-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:38:41.049449-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	13:38:41.080732-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:41.082271-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:38:41.083159-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	13:38:41.084270-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:39:21.676911-0500	Nexy	"The connection to ACDAccountStore was invalidated."
default	13:39:21.676872-0500	Nexy	[0x738795680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
