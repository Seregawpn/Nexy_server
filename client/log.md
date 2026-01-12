default	20:41:06.067090-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:41:06.067280-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:41:06.071424-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:41:06.087177-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41964753.41964762(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:41:06.087284-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41964753.41964762(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99327] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-99327-1349751 target:app<application.com.nexy.assistant.41964753.41964762(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:06.087594-0500	runningboardd	Assertion 394-99327-1349751 (target:app<application.com.nexy.assistant.41964753.41964762(501)>) will be created as active
default	20:41:06.092756-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:41:06.092793-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.41964753.41964762(501)>
default	20:41:06.092808-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:41:06.092982-0500	runningboardd	app<application.com.nexy.assistant.41964753.41964762(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:41:06.087176-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:41:06.171675-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] is not RunningBoard jetsam managed.
default	20:41:06.171690-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] This process will not be managed.
default	20:41:06.171700-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:06.171844-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:06.176985-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:06.177084-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] from originator [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-1349752 target:83987 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:41:06.177222-0500	runningboardd	Assertion 394-394-1349752 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) will be created as active
default	20:41:06.177407-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:06.177421-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:06.177445-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Set darwin role to: UserInteractive
default	20:41:06.177457-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:06.177509-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:06.177681-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] reported to RB as running
default	20:41:06.180206-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83987" ID:394-357-1349753 target:83987 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:06.180361-0500	runningboardd	Assertion 394-357-1349753 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) will be created as active
default	20:41:06.181143-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x181b81a com.nexy.assistant starting stopped process.
default	20:41:06.182041-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:06.182111-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:06.182169-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:06.182274-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:06.182369-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:06.186053-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:06.186422-0500	runningboardd	Invalidating assertion 394-99327-1349751 (target:app<application.com.nexy.assistant.41964753.41964762(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99327]
default	20:41:06.186460-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:06.186757-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:06.186813-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:06.186909-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:06.185502-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:41:06.185647-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a6260: Nexy> state 2
default	20:41:06.185703-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:41:06.193417-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:06.194469-0500	gamepolicyd	Hit the server for a process handle 586f93400014813 that resolved to: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:06.194514-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:06.194730-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:06.289474-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:06.289495-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:06.289508-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:06.289527-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:06.289756-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:06.292093-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:06.292572-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:06.353014-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:41:06.354310-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.74, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:41:06.362715-0500	tccd	AUTHREQ_SUBJECT: msgID=489.74, subject=com.nexy.assistant,
default	20:41:06.364265-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:06.378905-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	20:41:06.595623-0500	Nexy	[0x1058d09c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:41:06.595695-0500	Nexy	[0x1058d0f00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:41:06.819402-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x980a4c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:06.819642-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x980a4c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:06.819849-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x980a4c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:06.820053-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x980a4c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:41:06.821309-0500	Nexy	[0x1058dbe50] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:41:06.822024-0500	Nexy	[0x980004000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:41:06.822369-0500	Nexy	[0x980004140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:41:06.822824-0500	Nexy	[0x980004280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:41:06.823354-0500	Nexy	Received configuration update from daemon (initial)
default	20:41:06.824845-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:41:06.825202-0500	Nexy	[0x9800043c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:06.825891-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:06.827424-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.1, subject=com.nexy.assistant,
default	20:41:06.828175-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	20:41:06.842067-0500	Nexy	[0x9800043c0] invalidated after the last release of the connection object
default	20:41:06.842411-0500	Nexy	server port 0x0000350f, session port 0x0000350f
default	20:41:06.843405-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11408, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:06.843432-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:06.844197-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11408, subject=com.nexy.assistant,
default	20:41:06.845146-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	20:41:06.861552-0500	Nexy	New connection 0x1aa90b main
default	20:41:06.863981-0500	Nexy	CHECKIN: pid=83987
default	20:41:06.873590-0500	Nexy	CHECKEDIN: pid=83987 asn=0x0-0x181b81a foreground=0
default	20:41:06.873400-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83987" ID:394-357-1349756 target:83987 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:06.873503-0500	runningboardd	Assertion 394-357-1349756 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) will be created as active
default	20:41:06.873970-0500	runningboardd	Invalidating assertion 394-357-1349753 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	20:41:06.873462-0500	launchservicesd	CHECKIN:0x0-0x181b81a 83987 com.nexy.assistant
default	20:41:06.873692-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:41:06.873862-0500	Nexy	[0x9800043c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:41:06.873830-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:41:06.873892-0500	Nexy	[0x9800043c0] Connection returned listener port: 0x4f03
default	20:41:06.874296-0500	Nexy	[0x981660300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9800043c0.peer[357].0x981660300
default	20:41:06.876728-0500	Nexy	FRONTLOGGING: version 1
default	20:41:06.876769-0500	Nexy	Registered, pid=83987 ASN=0x0,0x181b81a
default	20:41:06.877090-0500	WindowServer	1aa90b[CreateApplication]: Process creation: 0x0-0x181b81a (Nexy) connectionID: 1AA90B pid: 83987 in session 0x101
default	20:41:06.877353-0500	Nexy	[0x980004500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:41:06.879034-0500	Nexy	[0x9800043c0] Connection returned listener port: 0x4f03
default	20:41:06.879688-0500	Nexy	BringForward: pid=83987 asn=0x0-0x181b81a bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:41:06.879839-0500	Nexy	BringFrontModifier: pid=83987 asn=0x0-0x181b81a Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:41:06.880857-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:41:06.882349-0500	Nexy	No persisted cache on this platform.
default	20:41:06.883364-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:41:06.883858-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:41:06.886617-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:41:06.886627-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:41:06.886686-0500	Nexy	Initializing connection
default	20:41:06.886728-0500	Nexy	Removing all cached process handles
default	20:41:06.886749-0500	Nexy	Sending handshake request attempt #1 to server
default	20:41:06.886758-0500	Nexy	Creating connection to com.apple.runningboard
default	20:41:06.886764-0500	Nexy	[0x980004640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:41:06.887267-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] as ready
default	20:41:06.887980-0500	Nexy	Handshake succeeded
default	20:41:06.887998-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41964753.41964762(501)>
default	20:41:06.888367-0500	Nexy	[0x9800043c0] Connection returned listener port: 0x4f03
default	20:41:06.889369-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 83987
default	20:41:06.892398-0500	Nexy	[0x9800043c0] Connection returned listener port: 0x4f03
default	20:41:06.905702-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:41:06.905725-0500	Nexy	[0x980004780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:41:06.905823-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:41:06.905873-0500	Nexy	[0x980004a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:41:06.907186-0500	Nexy	[0x980004a00] Connection returned listener port: 0x6503
default	20:41:06.908042-0500	Nexy	Registered process with identifier 83987-3698863
default	20:41:08.187175-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5216DD54-E9E1-4448-A4AE-72DBF552781A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52299,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x37a1c46f tp_proto=0x06"
default	20:41:08.187253-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52299<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7349846 t_state: SYN_SENT process: Nexy:83987 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb86ff5be
default	20:41:08.187911-0500	kernel	tcp connected: [<IPv4-redacted>:52299<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7349846 t_state: ESTABLISHED process: Nexy:83987 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb86ff5be
default	20:41:08.188219-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52299<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7349846 t_state: FIN_WAIT_1 process: Nexy:83987 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb86ff5be
default	20:41:08.188230-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52299<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7349846 t_state: FIN_WAIT_1 process: Nexy:83987 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:41:08.271198-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:41:08.272305-0500	Nexy	[0x980004c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:41:08.275625-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":{"PID":83987,"session_type":"Primary"} }
default	20:41:08.275722-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83987}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f483a, sessionType: 'prim', isRecording: false }, 
]
default	20:41:08.276354-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83987, name = Nexy
default	20:41:08.276650-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9800cf940 with ID: 0x1f483a
default	20:41:08.276978-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:41:08.277895-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:41:08.280061-0500	Nexy	[0x980004dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:41:08.282438-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41964753.41964762 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41964753.41964762>
default	20:41:08.286174-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:41:08.287879-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:41:08.288017-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:41:08.288136-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:41:08.288146-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:41:08.288376-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:41:08.288500-0500	Nexy	[0x980004f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:41:08.288753-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:41:08.289227-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:08.295583-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.2, subject=com.nexy.assistant,
default	20:41:08.296209-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:08.308383-0500	Nexy	[0x980004f00] invalidated after the last release of the connection object
default	20:41:08.308442-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:41:08.311923-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	20:41:08.313621-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9457, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:08.314627-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9457, subject=com.nexy.assistant,
default	20:41:08.315196-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
error	20:41:08.327606-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:41:08.328510-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9459, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:08.329466-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9459, subject=com.nexy.assistant,
default	20:41:08.330029-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:08.344651-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:41:08.344854-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x97fae6040> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:41:08.362217-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:41:08.363840-0500	Nexy	[0x980004f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:41:08.364151-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=360721418289153 }
default	20:41:08.364234-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	20:41:08.364545-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	20:41:08.364576-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	20:41:08.377640-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 115
default	20:41:08.387088-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	20:41:08.387109-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:41:08.393201-0500	Nexy	[0x980005040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:41:08.896728-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x97fb6c040) Selecting device 71 from constructor
default	20:41:08.896747-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c040)
default	20:41:08.896754-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c040) not already running
default	20:41:08.896967-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x97fb6c040) nothing to teardown
default	20:41:08.896972-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x97fb6c040) connecting device 71
default	20:41:08.897177-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x97fb6c040) Device ID: 71 (Input:No | Output:Yes): true
default	20:41:08.897334-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x97fb6c040) created ioproc 0xa for device 71
default	20:41:08.897473-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c040) adding 7 device listeners to device 71
default	20:41:08.897696-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c040) adding 0 device delegate listeners to device 71
default	20:41:08.897706-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x97fb6c040)
default	20:41:08.897800-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.897810-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:41:08.897818-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.897834-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:41:08.897845-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:08.897958-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x97fb6c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:08.897969-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x97fb6c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:08.897974-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:08.897979-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c040) removing 0 device listeners from device 0
default	20:41:08.897984-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c040) removing 0 device delegate listeners from device 0
default	20:41:08.897989-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c040)
default	20:41:08.898073-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:41:08.898834-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.901036-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:41:08.901104-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:41:08.901319-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a52c70, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.901374-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.903875-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.904109-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.909971-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.910244-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.912282-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a52d90, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.912308-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.912688-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.913460-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a52d90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.913474-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x980a52d90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:08.913480-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.913479-0500	Nexy	AudioConverter -> 0x980a52d90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:41:08.913490-0500	Nexy	AudioConverter -> 0x980a52d90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:41:08.913497-0500	Nexy	AudioConverter -> 0x980a52d90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:41:08.914380-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a52eb0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.914387-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x980a52eb0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:08.914393-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:08.914410-0500	Nexy	AudioConverter -> 0x980a52eb0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:41:08.914417-0500	Nexy	AudioConverter -> 0x980a52eb0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:41:08.914422-0500	Nexy	AudioConverter -> 0x980a52eb0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:41:08.914568-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x980a52eb0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:08.988151-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x97fb6c740) Selecting device 71 from constructor
default	20:41:08.988162-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:08.988168-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:08.988172-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x97fb6c740) nothing to teardown
default	20:41:08.988176-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x97fb6c740) connecting device 71
default	20:41:08.988262-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x97fb6c740) Device ID: 71 (Input:No | Output:Yes): true
default	20:41:08.988362-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x97fb6c740) created ioproc 0xb for device 71
default	20:41:08.988466-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 7 device listeners to device 71
default	20:41:08.988635-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 71
default	20:41:08.988645-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x97fb6c740)
default	20:41:08.988722-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.988730-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:41:08.988737-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:08.988744-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:41:08.988750-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:08.988842-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:08.988853-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:08.988858-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:08.988863-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device listeners from device 0
default	20:41:08.988867-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 0
default	20:41:08.988871-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:08.988886-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:41:08.988930-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x97fb6c740) caller requesting device change from 71 to 78
default	20:41:08.988936-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:08.988940-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:08.988946-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x97fb6c740) disconnecting device 71
default	20:41:08.988954-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x97fb6c740) destroying ioproc 0xb for device 71
default	20:41:08.989029-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	20:41:08.989110-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:41:08.989202-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x97fb6c740) connecting device 78
default	20:41:08.989279-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x97fb6c740) Device ID: 78 (Input:Yes | Output:No): true
default	20:41:08.990775-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9460, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:08.992297-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9460, subject=com.nexy.assistant,
default	20:41:08.993009-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:09.011553-0500	tccd	AUTHREQ_PROMPTING: msgID=395.9460, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:41:10.575026-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x97fb6c740) created ioproc 0xa for device 78
default	20:41:10.575280-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 7 device listeners to device 78
default	20:41:10.575694-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 78
default	20:41:10.575711-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x97fb6c740)
default	20:41:10.575731-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:41:10.575752-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:10.576030-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	20:41:10.576042-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:41:10.574443-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Initial, csid=(null)>";
    472 = "<TCCDEventSubscriber: token=472, state=Initial, csid=(null)>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	20:41:10.576087-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	20:41:10.576308-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:10.576405-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:10.576416-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:10.576505-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 7 device listeners from device 71
default	20:41:10.576904-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 71
default	20:41:10.576915-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:10.577703-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:41:10.579593-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9461, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:10.582312-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:41:10.582489-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9461, subject=com.nexy.assistant,
default	20:41:10.583822-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:10.615751-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a52b80, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:41:10.615968-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:41:10.617257-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9462, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:10.619002-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9462, subject=com.nexy.assistant,
default	20:41:10.619678-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:10.713890-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9463, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:10.716485-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9463, subject=com.nexy.assistant,
default	20:41:10.717343-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198600 at /Applications/Nexy.app
default	20:41:10.735449-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:41:10.736998-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1349776 target:83987 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:41:10.737071-0500	runningboardd	Assertion 394-328-1349776 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) will be created as active
default	20:41:10.737371-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:10.737514-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:41:10.737427-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:10.737483-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:10.737615-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:10.743997-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:10.746052-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:41:10.750754-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:10.760588-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	20:41:10.761782-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:41:10.761881-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:41:10.761970-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:10.762043-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f483a, Nexy(83987), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:41:10.762113-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.762118-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:10.762155-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:10.762207-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:41:10.762208-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.762222-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f483a, Nexy(83987), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2104 starting recording
default	20:41:10.762284-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.762334-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.762367-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.762494-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.763046-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:10.763077-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:41:10.763114-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f483a, Nexy(83987), 'prim'', displayID:'com.nexy.assistant'}
default	20:41:10.763194-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.763206-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	20:41:10.763219-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:41:10.763386-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.763434-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.763453-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:41:10.763464-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:41:10.763478-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:41:10.763931-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
error	20:41:10.764373-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
fault	20:41:10.812370-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41964753.41964762 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41964753.41964762>
fault	20:41:10.814433-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41964753.41964762 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41964753.41964762>
default	20:41:10.817229-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	20:41:10.817399-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:41:10.817481-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:10.817533-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:41:10.817564-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f483a, Nexy(83987), 'prim'', displayID:'com.nexy.assistant'}
default	20:41:10.817616-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f483a, Nexy(83987), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2104 stopping recording
default	20:41:10.817640-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:41:10.817642-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.817667-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:10.817703-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:10.817759-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.817786-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.817811-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:41:10.817842-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:10.817821-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:41:10.817859-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:41:10.817876-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.817956-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:41:10.817985-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:10.818000-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:41:10.822633-0500	runningboardd	Invalidating assertion 394-328-1349776 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) from originator [osservice<com.apple.powerd>:328]
default	20:41:10.828826-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:41:10.829124-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:41:10.829263-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:41:10.830085-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:41:10.831073-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831094-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831120-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.831139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831147-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.831155-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:10.831526-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:10.831538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831549-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831558-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.831566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.831573-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.831579-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:10.831675-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:10.836005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.836019-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.836030-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.836038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.836046-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.836054-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:10.836344-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:10.919083-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x97fb6c740) Selecting device 0 from destructor
default	20:41:10.919096-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:10.919105-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:10.919111-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x97fb6c740) disconnecting device 78
default	20:41:10.919117-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x97fb6c740) destroying ioproc 0xa for device 78
default	20:41:10.919154-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	20:41:10.919192-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:41:10.919339-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x97fb6c740) nothing to setup
default	20:41:10.919354-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device listeners to device 0
default	20:41:10.919362-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 0
default	20:41:10.919368-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 7 device listeners from device 78
default	20:41:10.919570-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 78
default	20:41:10.919584-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:10.923876-0500	Nexy	[0x980005540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:41:10.924921-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:41:10.925180-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:10.925343-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:10.925358-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:10.925367-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:10.925404-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:10.926958-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.3, subject=com.nexy.assistant,
default	20:41:10.927959-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:10.928162-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:10.928780-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:10.944856-0500	Nexy	[0x980005540] invalidated after the last release of the connection object
default	20:41:10.944997-0500	Nexy	[0x980005540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:41:10.945516-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:41:10.945699-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:10.946775-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.4, subject=com.nexy.assistant,
default	20:41:10.947518-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:10.960681-0500	Nexy	[0x980005540] invalidated after the last release of the connection object
default	20:41:10.960823-0500	Nexy	[0x980005540] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	20:41:10.960915-0500	Nexy	[0x980005540] invalidated after the last release of the connection object
default	20:41:11.053616-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	20:41:11.084240-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:11.089174-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:41:11.114404-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-1349752 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987])
default	20:41:11.182384-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83998.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=83998, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:11.184088-0500	tccd	AUTHREQ_SUBJECT: msgID=83998.1, subject=com.nexy.assistant,
default	20:41:11.185118-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:11.215677-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11416, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=83998, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:11.216773-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11416, subject=com.nexy.assistant,
default	20:41:11.217550-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:11.257121-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:11.257143-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:11.257180-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:11.257231-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:11.260235-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:11.261363-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:11.262909-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:11.421694-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 cc703800 };
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
default	20:41:11.435247-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:11.445350-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7198c00 at /Applications/Nexy.app
default	20:41:11.461318-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	20:41:11.980811-0500	Nexy	[0x980005400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:11.982403-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:11.984709-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.5, subject=com.nexy.assistant,
default	20:41:11.986072-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:12.005500-0500	Nexy	[0x980005400] invalidated after the last release of the connection object
default	20:41:12.087178-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84002.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84002, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:12.089209-0500	tccd	AUTHREQ_SUBJECT: msgID=84002.1, subject=com.nexy.assistant,
default	20:41:12.090759-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:12.115253-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11422, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84002, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:12.116252-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11422, subject=com.nexy.assistant,
default	20:41:12.116955-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:12.179615-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:13.117274-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84004.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84004, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:13.118787-0500	tccd	AUTHREQ_SUBJECT: msgID=84004.1, subject=com.nexy.assistant,
default	20:41:13.119529-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:13.140702-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11426, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84004, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:13.141614-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11426, subject=com.nexy.assistant,
default	20:41:13.142312-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:13.176893-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:13.186623-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d7703800 };
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
default	20:41:13.185822-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	20:41:13.198268-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:41:13.207906-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:13.220849-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:13.250124-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 dc703800 };
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
default	20:41:13.262774-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:13.903310-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84006.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84006, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:13.904881-0500	tccd	AUTHREQ_SUBJECT: msgID=84006.1, subject=com.nexy.assistant,
default	20:41:13.905648-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:13.926276-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11429, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84006, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:13.927177-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11429, subject=com.nexy.assistant,
default	20:41:13.927855-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:13.967595-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:13.992486-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 df703800 };
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
default	20:41:14.005984-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:14.146684-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84007.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84007, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:14.148327-0500	tccd	AUTHREQ_SUBJECT: msgID=84007.1, subject=com.nexy.assistant,
default	20:41:14.149112-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:14.169749-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11430, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84007, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:14.170694-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11430, subject=com.nexy.assistant,
default	20:41:14.171403-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:14.212280-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:14.236727-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 e1703800 };
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
default	20:41:14.247842-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:14.687755-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84008.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84008, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:14.689215-0500	tccd	AUTHREQ_SUBJECT: msgID=84008.1, subject=com.nexy.assistant,
default	20:41:14.689949-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:14.710519-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11431, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84008, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:14.711420-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11431, subject=com.nexy.assistant,
default	20:41:14.712166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:14.751333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:14.778512-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 e3703800 };
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
default	20:41:14.792865-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:14.841274-0500	Nexy	[0x980005680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:14.842109-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:14.844038-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.6, subject=com.nexy.assistant,
default	20:41:14.845278-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	20:41:14.860243-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[83987], responsiblePID[83987], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:41:14.860580-0500	Nexy	[0x980005680] invalidated after the last release of the connection object
default	20:41:14.915549-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	20:41:14.934609-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256d00 at /Applications/Nexy.app
default	20:41:14.938682-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:41:16.529659-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	20:41:18.744030-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:41:18.745110-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:41:18.748307-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:41:18.748385-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:41:20.587666-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	20:41:21.025407-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:41:21.166119-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	20:41:23.075166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	20:41:23.100269-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:41:23.111857-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:41:23.260504-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:41:23.260977-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:41:23.262799-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:41:23.263140-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:41:23.296916-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:41:23.297909-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:41:23.299103-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:41:23.300136-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:41:29.883214-0500	Nexy	[0x980005680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:29.884948-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83987.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:29.888967-0500	tccd	AUTHREQ_SUBJECT: msgID=83987.7, subject=com.nexy.assistant,
default	20:41:29.890582-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:29.919323-0500	Nexy	[0x980005680] invalidated after the last release of the connection object
default	20:41:45.063658-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x97fb6c740) Selecting device 71 from constructor
default	20:41:45.063674-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:45.063683-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:45.063693-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x97fb6c740) nothing to teardown
default	20:41:45.063697-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x97fb6c740) connecting device 71
default	20:41:45.063951-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x97fb6c740) Device ID: 71 (Input:No | Output:Yes): true
default	20:41:45.064462-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x97fb6c740) created ioproc 0xc for device 71
default	20:41:45.064645-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 7 device listeners to device 71
default	20:41:45.064954-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 71
default	20:41:45.064965-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x97fb6c740)
default	20:41:45.065139-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:45.065150-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:41:45.065156-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:45.065169-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:41:45.065179-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:45.065308-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:45.065325-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:45.065332-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:45.065340-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device listeners from device 0
default	20:41:45.065346-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 0
default	20:41:45.065359-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:45.065392-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:41:45.065519-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x97fb6c740) caller requesting device change from 71 to 78
default	20:41:45.065530-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:45.065537-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:45.065541-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x97fb6c740) disconnecting device 71
default	20:41:45.065547-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x97fb6c740) destroying ioproc 0xc for device 71
default	20:41:45.065579-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xc}
default	20:41:45.065680-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:41:45.065856-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x97fb6c740) connecting device 78
default	20:41:45.065979-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x97fb6c740) Device ID: 78 (Input:Yes | Output:No): true
default	20:41:45.072993-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9464, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:45.075459-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9464, subject=com.nexy.assistant,
default	20:41:45.076905-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:45.104813-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x97fb6c740) created ioproc 0xb for device 78
default	20:41:45.105005-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 7 device listeners to device 78
default	20:41:45.105249-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 78
default	20:41:45.105257-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x97fb6c740)
default	20:41:45.105269-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:41:45.105281-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:45.105427-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	20:41:45.105434-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:41:45.105443-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	20:41:45.105583-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:45.105595-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x97fb6c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:45.105602-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:45.105607-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 7 device listeners from device 71
default	20:41:45.105797-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 71
default	20:41:45.105806-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:45.105827-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:41:45.106640-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:41:45.108009-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9465, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:45.109241-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9465, subject=com.nexy.assistant,
default	20:41:45.109874-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:45.126882-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x980a53540, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:41:45.127111-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:41:45.128107-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9466, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:45.129070-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9466, subject=com.nexy.assistant,
default	20:41:45.129642-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:45.147480-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9467, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:45.148694-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9467, subject=com.nexy.assistant,
default	20:41:45.149465-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:45.170612-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762(501)>:83987] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1349982 target:83987 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:41:45.170702-0500	runningboardd	Assertion 394-328-1349982 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) will be created as active
default	20:41:45.171127-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:45.171144-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:45.171160-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:45.171257-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:45.175036-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:45.177337-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:45.193038-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	20:41:45.194116-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:41:45.194327-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:41:45.194390-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f483a, Nexy(83987), 'prim'/com.nexy.assistant was not correct. Old score = 201
error	20:41:45.194437-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	20:41:45.194426-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:45.194535-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f483a, Nexy(83987), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:41:45.194561-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:45.194607-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.194649-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:45.194726-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.194737-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:41:45.194751-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f483a, Nexy(83987), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2104 starting recording
default	20:41:45.194827-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.194900-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.194888-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:45.194937-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.194931-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:41:45.194967-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f483a, Nexy(83987), 'prim'', displayID:'com.nexy.assistant'}
default	20:41:45.195025-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.195085-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	20:41:45.195071-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.195095-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:41:45.195161-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.195183-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.195223-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:41:45.195287-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:41:45.195301-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:41:45.195425-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:41:45.207029-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:41:45.207178-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:41:45.207237-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:41:45.208833-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.208849-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.208892-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.208905-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.208919-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.208930-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:45.209275-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:45.217216-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.217235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.217255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.217262-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.217271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.217279-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:45.217391-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:45.218569-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.218583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.218605-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.218614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.218621-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.218627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:45.219069-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:41:45.248224-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	20:41:45.248469-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:41:45.248572-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:45.248625-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:41:45.248656-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f483a, Nexy(83987), 'prim'', displayID:'com.nexy.assistant'}
default	20:41:45.248708-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f483a, Nexy(83987), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2104 stopping recording
default	20:41:45.248732-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:41:45.248756-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:45.248756-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.248799-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:45.248888-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.248910-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:41:45.248924-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:41:45.248951-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.249020-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:41:45.249061-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.249090-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:41:45.249149-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:41:45.249164-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:45.249174-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:41:45.257896-0500	runningboardd	Invalidating assertion 394-328-1349982 (target:[app<application.com.nexy.assistant.41964753.41964762(501)>:83987]) from originator [osservice<com.apple.powerd>:328]
default	20:41:45.258456-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:41:45.258853-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.259114-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.259166-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.259229-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:45.259289-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:45.259351-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:45.259614-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:45.349916-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x97fb6c740) Selecting device 0 from destructor
default	20:41:45.349942-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x97fb6c740)
default	20:41:45.349955-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x97fb6c740) not already running
default	20:41:45.349965-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x97fb6c740) disconnecting device 78
default	20:41:45.349976-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x97fb6c740) destroying ioproc 0xb for device 78
default	20:41:45.350020-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	20:41:45.350070-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:41:45.350305-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x97fb6c740) nothing to setup
default	20:41:45.350326-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device listeners to device 0
default	20:41:45.350336-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x97fb6c740) adding 0 device delegate listeners to device 0
default	20:41:45.350347-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 7 device listeners from device 78
default	20:41:45.350744-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x97fb6c740) removing 0 device delegate listeners from device 78
default	20:41:45.350764-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x97fb6c740)
default	20:41:45.365324-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring jetsam update because this process is not memory-managed
default	20:41:45.365355-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring suspend because this process is not lifecycle managed
default	20:41:45.365389-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring GPU update because this process is not GPU managed
default	20:41:45.365439-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] Ignoring memory limit update because this process is not memory-managed
default	20:41:45.368920-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:45.369594-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, running-active-NotVisible
default	20:41:45.458009-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84059.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84059, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:45.459902-0500	tccd	AUTHREQ_SUBJECT: msgID=84059.1, subject=com.nexy.assistant,
default	20:41:45.460921-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:45.482824-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11453, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83987, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84059, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:45.483828-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11453, subject=com.nexy.assistant,
default	20:41:45.485272-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:45.533217-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:41:45.567776-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 7b713800 };
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
default	20:41:45.583868-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:46.645004-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x181b81a (Nexy) connectionID: 1AA90B pid: 83987 in session 0x101
default	20:41:46.645036-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x181b81a (Nexy) acq:0xb6ab95760 count:1
default	20:41:46.645380-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f483a","name":"Nexy(83987)"}, "details":null }
default	20:41:46.645411-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f483a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83987})
default	20:41:46.645422-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83987})
default	20:41:46.645708-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:41:46.645881-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2104, PID = 83987, Name = sid:0x1f483a, Nexy(83987), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:41:46.646302-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646365-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646004-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646379-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646225-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646454-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:41:46.646635-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x181b81a removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x181b81a (Nexy)"
)}
default	20:41:46.647015-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14813 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x181b81a (Nexy)"
)}
default	20:41:46.647532-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.669279-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762(501)>:83987] termination reported by launchd (0, 0, 0)
default	20:41:46.669429-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.669729-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.669984-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.670031-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.675570-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: none (role: None) (endowments: (null))
default	20:41:46.675717-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762(501)>: none (role: None) (endowments: (null))
default	20:41:46.675843-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83987, name = Nexy
default	20:41:46.676470-0500	launchservicesd	Hit the server for a process handle 586f93400014813 that resolved to: [app<application.com.nexy.assistant.41964753.41964762(501)>:83987]
default	20:41:46.676619-0500	gamepolicyd	Received state update for 83987 (app<application.com.nexy.assistant.41964753.41964762(501)>, none-NotVisible
default	20:41:46.679173-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x181b81a} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:41:46.679222-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a6260: Nexy> state 3
default	20:41:46.679235-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:41:46.680567-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a6260: Nexy> state 4
default	20:41:46.680578-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:41:49.739149-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	20:41:49.838160-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:41:49.838321-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:41:49.840171-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:41:49.846594-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:41:49.847959-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:41:49.848058-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99327] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-99327-1350002 target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:49.848155-0500	runningboardd	Assertion 394-99327-1350002 (target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>) will be created as active
default	20:41:49.851221-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:41:49.851252-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>
default	20:41:49.851269-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:41:49.851344-0500	runningboardd	app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:41:49.864460-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] is not RunningBoard jetsam managed.
default	20:41:49.864475-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] This process will not be managed.
default	20:41:49.864485-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:41:49.864686-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:49.865397-0500	gamepolicyd	Hit the server for a process handle b47550200014871 that resolved to: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:41:49.865437-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:41:49.867933-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:41:49.868012-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-1350003 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:41:49.868156-0500	runningboardd	Assertion 394-394-1350003 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:41:49.868372-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:41:49.868391-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:41:49.868412-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Set darwin role to: UserInteractive
default	20:41:49.868431-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:41:49.868465-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:41:49.868477-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] reported to RB as running
default	20:41:49.870251-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84081" ID:394-357-1350004 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:49.870421-0500	runningboardd	Assertion 394-357-1350004 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:41:49.870438-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x183082f com.nexy.assistant starting stopped process.
default	20:41:49.871530-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:41:49.871747-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a6260: Nexy> state 2
default	20:41:49.871778-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:41:49.872976-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:41:49.873045-0500	kernel	Nexy[84081] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xc7273bd6effc6e97. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:41:49.873004-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:41:49.873071-0500	kernel	Nexy[84081] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xc7273bd6effc6e97. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:41:49.873023-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:41:49.873101-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:41:49.873250-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:41:49.873928-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:49.874526-0500	runningboardd	Invalidating assertion 394-99327-1350002 (target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99327]
default	20:41:49.874560-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:41:49.874690-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:41:49.874747-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:41:49.874804-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:41:49.875829-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:41:49.878134-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:49.887814-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:49.931847-0500	logger	detected new pid 84081 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:49.951886-0500	Nexy	[0x1060bd140] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:41:49.951963-0500	Nexy	[0x1060bd680] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:41:49.980226-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:41:49.980241-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:41:49.980252-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:41:49.980273-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:41:49.980434-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:41:49.983042-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:49.983443-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
error	20:41:50.067889-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x8ec5a4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:50.068133-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x8ec5a4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:50.068351-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x8ec5a4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:41:50.068557-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x8ec5a4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:41:50.069888-0500	Nexy	[0x1060c6940] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:41:50.070607-0500	Nexy	[0x8ec738000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:41:50.070935-0500	Nexy	[0x8ec738140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:41:50.071321-0500	Nexy	[0x8ec738280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:41:50.071861-0500	Nexy	Received configuration update from daemon (initial)
default	20:41:50.073482-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:41:50.073848-0500	Nexy	[0x8ec7383c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:50.074584-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:50.076200-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.1, subject=com.nexy.assistant,
default	20:41:50.076960-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:50.096359-0500	Nexy	[0x8ec7383c0] invalidated after the last release of the connection object
default	20:41:50.096690-0500	Nexy	server port 0x00003413, session port 0x00003413
default	20:41:50.097651-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11454, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:50.097687-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:50.098514-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11454, subject=com.nexy.assistant,
default	20:41:50.099179-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:50.124546-0500	Nexy	New connection 0x10326f main
default	20:41:50.127204-0500	Nexy	CHECKIN: pid=84081
default	20:41:50.136379-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84081" ID:394-357-1350005 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:41:50.136646-0500	Nexy	CHECKEDIN: pid=84081 asn=0x0-0x183082f foreground=0
default	20:41:50.136476-0500	runningboardd	Assertion 394-357-1350005 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:41:50.136507-0500	launchservicesd	CHECKIN:0x0-0x183082f 84081 com.nexy.assistant
default	20:41:50.136982-0500	runningboardd	Invalidating assertion 394-357-1350004 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	20:41:50.136858-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:41:50.136984-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:41:50.136944-0500	Nexy	[0x8ec7383c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:41:50.136953-0500	Nexy	[0x8ec7383c0] Connection returned listener port: 0x5003
default	20:41:50.137336-0500	Nexy	[0x8ed550300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8ec7383c0.peer[357].0x8ed550300
default	20:41:50.145066-0500	Nexy	FRONTLOGGING: version 1
default	20:41:50.145136-0500	Nexy	Registered, pid=84081 ASN=0x0,0x183082f
default	20:41:50.145714-0500	WindowServer	10326f[CreateApplication]: Process creation: 0x0-0x183082f (Nexy) connectionID: 10326F pid: 84081 in session 0x101
default	20:41:50.146168-0500	Nexy	[0x8ec738500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:41:50.148041-0500	Nexy	[0x8ec7383c0] Connection returned listener port: 0x5003
default	20:41:50.150418-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:41:50.154522-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:41:50.159274-0500	Nexy	[0x8ec7383c0] Connection returned listener port: 0x5003
default	20:41:50.163311-0500	Nexy	[0x8ec7383c0] Connection returned listener port: 0x5003
default	20:41:50.167567-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:41:50.167666-0500	Nexy	[0x8ec7388c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:41:50.167810-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:41:50.167881-0500	Nexy	[0x8ec738a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:41:50.991297-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 059E7095-B3B4-4F78-8363-D5906D7075B7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52346,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5eadc75f tp_proto=0x06"
default	20:41:50.991377-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52346<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350112 t_state: SYN_SENT process: Nexy:84081 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8804e553
default	20:41:50.992038-0500	kernel	tcp connected: [<IPv4-redacted>:52346<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350112 t_state: ESTABLISHED process: Nexy:84081 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8804e553
default	20:41:50.992348-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52346<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350112 t_state: FIN_WAIT_1 process: Nexy:84081 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8804e553
default	20:41:50.992360-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52346<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350112 t_state: FIN_WAIT_1 process: Nexy:84081 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:41:51.030404-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:41:51.031061-0500	Nexy	[0x8ec738c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:41:51.032294-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f483b","name":"Nexy(84081)"}, "details":{"PID":84081,"session_type":"Primary"} }
default	20:41:51.032392-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84081}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f483b, sessionType: 'prim', isRecording: false }, 
]
default	20:41:51.033113-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84081, name = Nexy
default	20:41:51.033550-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8ec7c65a0 with ID: 0x1f483b
default	20:41:51.033849-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:41:51.034851-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:41:51.036348-0500	Nexy	[0x8ec738dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:41:51.038954-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC AUID=501> and <type=Application identifier=application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>
default	20:41:51.043504-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:41:51.045125-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:41:51.045299-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:41:51.045450-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:41:51.045464-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:41:51.045497-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:41:51.045630-0500	Nexy	[0x8ec738f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:41:51.045814-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:41:51.046181-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:51.053417-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.2, subject=com.nexy.assistant,
default	20:41:51.054286-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:51.072104-0500	Nexy	[0x8ec738f00] invalidated after the last release of the connection object
default	20:41:51.072238-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:41:51.072276-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:41:51.072501-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:41:51.073609-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9468, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:51.074634-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9468, subject=com.nexy.assistant,
default	20:41:51.075203-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
error	20:41:51.090498-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:41:51.091367-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9470, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:41:51.092247-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9470, subject=com.nexy.assistant,
default	20:41:51.092787-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8c7199200 at /Applications/Nexy.app
default	20:41:51.106916-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:41:51.106933-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8ebb1e0c0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:41:51.121011-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:41:51.121814-0500	Nexy	[0x8ec738f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:41:51.122148-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=361125145214977 }
default	20:41:51.122236-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	20:41:51.122277-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	20:41:51.122307-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	20:41:51.133256-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 115
default	20:41:51.140058-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	20:41:51.140078-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:41:51.143985-0500	Nexy	[0x8ec739040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:41:51.153465-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8ebec8040) Selecting device 71 from constructor
default	20:41:51.153474-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x8ebec8040)
default	20:41:51.153480-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x8ebec8040) not already running
default	20:41:51.153486-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8ebec8040) nothing to teardown
default	20:41:51.153491-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x8ebec8040) connecting device 71
default	20:41:51.153565-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8ebec8040) Device ID: 71 (Input:No | Output:Yes): true
default	20:41:51.153661-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x8ebec8040) created ioproc 0xa for device 71
default	20:41:51.153763-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8ebec8040) adding 7 device listeners to device 71
default	20:41:51.153937-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8ebec8040) adding 0 device delegate listeners to device 71
default	20:41:51.153944-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8ebec8040)
default	20:41:51.154006-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.154012-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:41:51.154023-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.154030-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:41:51.154036-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:41:51.154129-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8ebec8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:41:51.154139-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8ebec8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:41:51.154143-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:41:51.154146-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8ebec8040) removing 0 device listeners from device 0
default	20:41:51.154150-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8ebec8040) removing 0 device delegate listeners from device 0
default	20:41:51.154155-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x8ebec8040)
default	20:41:51.154196-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:41:51.154472-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.155558-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:41:51.155606-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:41:51.155729-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8eb597150, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.155750-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.157120-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.157316-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.159027-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.159212-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.160252-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8eb597270, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.160263-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.160536-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.161235-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8eb597270, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.161245-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8eb597270: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:51.161247-0500	Nexy	AudioConverter -> 0x8eb597270: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:41:51.161250-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.161256-0500	Nexy	AudioConverter -> 0x8eb597270: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:41:51.161262-0500	Nexy	AudioConverter -> 0x8eb597270: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:41:51.161998-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8eb597390, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:41:51.162005-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8eb597390: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:51.162009-0500	Nexy	AudioConverter -> 0x8eb597390: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:41:51.162010-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:41:51.162017-0500	Nexy	AudioConverter -> 0x8eb597390: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:41:51.162026-0500	Nexy	AudioConverter -> 0x8eb597390: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:41:51.162142-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8eb597390: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:41:51.183790-0500	Nexy	[0x8ec739400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:41:51.184253-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:41:51.184423-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:51.185342-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.3, subject=com.nexy.assistant,
default	20:41:51.186091-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:51.203705-0500	Nexy	[0x8ec739400] invalidated after the last release of the connection object
default	20:41:51.203782-0500	Nexy	[0x8ec739400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:41:51.204118-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:41:51.204273-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:51.205038-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.4, subject=com.nexy.assistant,
default	20:41:51.205614-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:51.222779-0500	Nexy	[0x8ec739400] invalidated after the last release of the connection object
default	20:41:51.222835-0500	Nexy	[0x8ec739400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	20:41:51.222918-0500	Nexy	[0x8ec739400] invalidated after the last release of the connection object
default	20:41:51.297565-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84092.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84092, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:51.298824-0500	tccd	AUTHREQ_SUBJECT: msgID=84092.1, subject=com.nexy.assistant,
default	20:41:51.299490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:51.319205-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11455, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84092, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:51.319993-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11455, subject=com.nexy.assistant,
default	20:41:51.320631-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:41:51.362368-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:41:51.387722-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 ba713800 };
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
default	20:41:51.401478-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:51.453747-0500	Nexy	[0x8ec739540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:51.454502-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:51.461443-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.5, subject=com.nexy.assistant,
default	20:41:51.462076-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:41:51.479804-0500	Nexy	[0x8ec739540] invalidated after the last release of the connection object
default	20:41:54.913098-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-1350003 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081])
default	20:41:55.113768-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:41:55.113796-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:41:55.113816-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:41:55.113851-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:41:55.118771-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:41:55.119429-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:00.578423-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:42:01.155036-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:42:06.731081-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84095.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84095, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:06.732877-0500	tccd	AUTHREQ_SUBJECT: msgID=84095.1, subject=com.nexy.assistant,
default	20:42:06.733834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:06.762748-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11456, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84095, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:06.763654-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11456, subject=com.nexy.assistant,
default	20:42:06.764321-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:06.801578-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:06.824245-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c1713800 };
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
default	20:42:06.835655-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:06.896580-0500	Nexy	[0x8ec739900] activating connection: mach=true listener=false peer=false name=com.apple.iconservices
default	20:42:06.897313-0500	Nexy	[0x8ec739a40] activating connection: mach=true listener=false peer=false name=com.apple.iconservices.store
default	20:42:06.899561-0500	Nexy	[0x8ec739b80] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:42:06.912584-0500	Nexy	[0x8ec73a940] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:42:06.913147-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84081.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:42:06.914120-0500	tccd	AUTHREQ_SUBJECT: msgID=84081.6, subject=com.nexy.assistant,
default	20:42:06.914772-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:06.933579-0500	Nexy	[0x8ec73a940] invalidated after the last release of the connection object
default	20:42:06.933768-0500	Nexy	server port 0x00014d0f, session port 0x00003413
default	20:42:06.934514-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11457, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:06.934539-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:06.935333-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11457, subject=com.nexy.assistant,
default	20:42:06.935992-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:06.958584-0500	Nexy	server port 0x00014d1b, session port 0x00003413
default	20:42:06.962321-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DA9B0B2C-F346-404E-B1D0-EB455DF55312 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52376,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x11d62279 tp_proto=0x06"
default	20:42:06.962366-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52376<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350293 t_state: SYN_SENT process: Nexy:84081 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb2208230
default	20:42:06.962654-0500	kernel	tcp connected: [<IPv4-redacted>:52376<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350293 t_state: ESTABLISHED process: Nexy:84081 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb2208230
default	20:42:06.965478-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52376<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350293 t_state: FIN_WAIT_1 process: Nexy:84081 Duration: 0.003 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb2208230
default	20:42:06.965487-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52376<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350293 t_state: FIN_WAIT_1 process: Nexy:84081 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:42:06.966006-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E189B90C-0DF8-4FDE-8D70-971A3E08CEDF flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52377,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x12090b34 tp_proto=0x06"
default	20:42:06.966032-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52377<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350296 t_state: SYN_SENT process: Nexy:84081 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86b5ff98
default	20:42:06.966114-0500	kernel	tcp connected: [<IPv4-redacted>:52377<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350296 t_state: ESTABLISHED process: Nexy:84081 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86b5ff98
default	20:42:06.966583-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52377<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350296 t_state: FIN_WAIT_1 process: Nexy:84081 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x86b5ff98
default	20:42:06.966592-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52377<-><IPv4-redacted>:53] interface: utun4 (skipped: 25994)
so_gencnt: 7350296 t_state: FIN_WAIT_1 process: Nexy:84081 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:42:06.968987-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:42:06.969135-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:42:06.970602-0500	Nexy	nw_path_libinfo_path_check [820D4E5A-0BB5-47CE-B73A-BB4F5F438D60 IPv4#55b11d72:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:42:06.970988-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 95F2980F-80AC-4EE7-8363-2AA3BC19EAEF flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52378,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x3fc06004 tp_proto=0x06"
default	20:42:06.971010-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52378<-><IPv4-redacted>:443] interface: utun4 (skipped: 25994)
so_gencnt: 7350297 t_state: SYN_SENT process: Nexy:84081 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa6ac3d12
default	20:42:06.971369-0500	kernel	tcp connected: [<IPv4-redacted>:52378<-><IPv4-redacted>:443] interface: utun4 (skipped: 25994)
so_gencnt: 7350297 t_state: ESTABLISHED process: Nexy:84081 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa6ac3d12
default	20:42:06.974440-0500	kernel	udp connect: [<IPv4-redacted>:60550<-><IPv4-redacted>:443] interface:  (skipped: 4450)
so_gencnt: 7350298 so_state: 0x0002 process: Nexy:84081 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x800edcfa
default	20:42:06.974448-0500	kernel	udp_connection_summary [<IPv4-redacted>:60550<-><IPv4-redacted>:443] interface:  (skipped: 4450)
so_gencnt: 7350298 so_state: 0x0002 process: Nexy:84081 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x800edcfa flowctl: 0us (0x)
default	20:42:06.976607-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 181F9A08-FF12-4E93-BC7E-E690A03B994E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52380,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xd3452faf tp_proto=0x06"
default	20:42:06.976641-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52380<-><IPv4-redacted>:443] interface: utun4 (skipped: 25994)
so_gencnt: 7350300 t_state: SYN_SENT process: Nexy:84081 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d112105
default	20:42:06.976892-0500	kernel	tcp connected: [<IPv4-redacted>:52380<-><IPv4-redacted>:443] interface: utun4 (skipped: 25994)
so_gencnt: 7350300 t_state: ESTABLISHED process: Nexy:84081 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d112105
default	20:42:06.983642-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84096.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84096, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:06.984894-0500	tccd	AUTHREQ_SUBJECT: msgID=84096.1, subject=com.nexy.assistant,
default	20:42:06.985554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.004661-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11458, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84096, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:07.005501-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11458, subject=com.nexy.assistant,
default	20:42:07.006141-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.044049-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:07.066973-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c3713800 };
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
default	20:42:07.078408-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:07.161849-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84097.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84097, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:07.163047-0500	tccd	AUTHREQ_SUBJECT: msgID=84097.1, subject=com.nexy.assistant,
default	20:42:07.163708-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.183775-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11459, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84097, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:07.184695-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11459, subject=com.nexy.assistant,
default	20:42:07.185424-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.228064-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:07.254878-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c5713800 };
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
default	20:42:07.268733-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:07.389931-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84099.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84099, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:07.391237-0500	tccd	AUTHREQ_SUBJECT: msgID=84099.1, subject=com.nexy.assistant,
default	20:42:07.391935-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.411190-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11460, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84099, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:07.412012-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11460, subject=com.nexy.assistant,
default	20:42:07.412667-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.449163-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:07.473535-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c9713800 };
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
default	20:42:07.487401-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:07.608926-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84100.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84100, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:07.610197-0500	tccd	AUTHREQ_SUBJECT: msgID=84100.1, subject=com.nexy.assistant,
default	20:42:07.610861-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.629849-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11461, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84100, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:07.630677-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11461, subject=com.nexy.assistant,
default	20:42:07.631302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.669542-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:07.693438-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 cb713800 };
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
default	20:42:07.704560-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:07.826339-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84101.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84101, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:07.827708-0500	tccd	AUTHREQ_SUBJECT: msgID=84101.1, subject=com.nexy.assistant,
default	20:42:07.828429-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.847585-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11462, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84081, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84101, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:07.848395-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11462, subject=com.nexy.assistant,
default	20:42:07.849024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:07.886853-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	20:42:07.912080-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84000: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 cd713800 };
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
default	20:42:07.923989-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:08.100059-0500	Nexy	[0x8ec73ae40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:42:08.113464-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:42:08.113799-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 84081
default	20:42:08.125837-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x8ed48c640
 (
    "<NSDarkAquaAppearance: 0x8ed48c820>",
    "<NSSystemAppearance: 0x8ed48c780>"
)>
default	20:42:08.133444-0500	Nexy	[0x8ec73b340] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:42:08.138063-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:42:08.138456-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:42:08.138468-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:42:08.138497-0500	Nexy	[0x8ec73b480] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:42:08.139374-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:42:08.139461-0500	Nexy	[0x8ec73b5c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:08.139538-0500	Nexy	FBSWorkspace registering source: <private>
default	20:42:08.139697-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:42:08.140853-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:42:08.141365-0500	Nexy	<FBSWorkspaceScenesClient:0x8ed48f980 <private>> attempting immediate handshake from activate
default	20:42:08.141707-0500	Nexy	<FBSWorkspaceScenesClient:0x8ed48f980 <private>> sent handshake
default	20:42:08.141833-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:42:08.142508-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:42:08.143994-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:42:08.143435-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.144110-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.145199-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Registering event dispatcher at init
default	20:42:08.145420-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:42:08.145580-0500	ControlCenter	Created <FBWorkspace: 0x8e81b5220; <FBApplicationProcess: 0x8e3780180; app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081(v3871A6)>>
default	20:42:08.145598-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC> with intent background
default	20:42:08.145935-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:42:08.146049-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)> from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-1350081 target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:42:08.146189-0500	runningboardd	Assertion 394-638-1350081 (target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>) will be created as active
default	20:42:08.146219-0500	Nexy	Requesting scene <FBSScene: 0x8ed48fd40; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300> from com.apple.controlcenter.statusitems
default	20:42:08.146222-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-1350081 target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.146541-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:08.146549-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:08.146559-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:08.146728-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:08.148669-0500	Nexy	Request for <FBSScene: 0x8ed48fd40; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300> complete!
default	20:42:08.148758-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:42:08.149518-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:08.150144-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.150175-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:42:08.150413-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:42:08.150631-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:42:08.150665-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:42:08.150927-0500	Nexy	Requesting scene <FBSScene: 0x8ed48fde0; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:42:08.151117-0500	Nexy	Request for <FBSScene: 0x8ed48fde0; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView> complete!
default	20:42:08.152537-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.152554-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:42:08.152820-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Bootstrap success!
default	20:42:08.153197-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Setting process visibility to: Background
default	20:42:08.153239-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:42:08.153466-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-638-1350082 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:42:08.153523-0500	runningboardd	Assertion 394-638-1350082 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:42:08.153819-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:08.153836-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:08.153846-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:08.153865-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:08.156138-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:08.156511-0500	ControlCenter	Adding: <FBApplicationProcess: 0x8e3780180; app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081(v3871A6)>
default	20:42:08.156665-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.156960-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Connection established.
default	20:42:08.157016-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x8e889ebc0>
default	20:42:08.157035-0500	ControlCenter	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.157036-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Connection to remote process established!
default	20:42:08.161323-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.161349-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:42:08.161456-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:42:08.166021-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.166038-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e3780180; app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081(v3871A6)>
default	20:42:08.166148-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Registered new scene: <FBWorkspaceScene: 0x8e4ae0d80; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300> (fromRemnant = 0)
default	20:42:08.166182-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Workspace interruption policy did change: reconnect
default	20:42:08.166358-0500	ControlCenter	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300] Client process connected: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.166369-0500	Nexy	Request for <FBSScene: 0x8ed48fd40; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300> complete!
default	20:42:08.166449-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-638-1350083 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:42:08.166528-0500	runningboardd	Assertion 394-638-1350083 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as inactive as originator process has not exited
default	20:42:08.166941-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.166964-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e3780180; app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081(v3871A6)>
default	20:42:08.167021-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Registered new scene: <FBWorkspaceScene: 0x8e4ae33c0; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:42:08.167150-0500	ControlCenter	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]
default	20:42:08.167159-0500	Nexy	Request for <FBSScene: 0x8ed48fde0; com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView> complete!
default	20:42:08.168047-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-1350084 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:42:08.168153-0500	runningboardd	Assertion 394-638-1350084 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:42:08.168235-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:42:08.168415-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:08.168425-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:08.168435-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:08.168452-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:08.168801-0500	Nexy	<FBSWorkspaceScenesClient:0x8ed48f980 <private>> Reconnecting scene com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300
default	20:42:08.169117-0500	Nexy	<FBSWorkspaceScenesClient:0x8ed48f980 <private>> Reconnecting scene com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView
default	20:42:08.170828-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:08.171196-0500	ControlCenter	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.171369-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.175024-0500	Nexy	Registering for test daemon availability notify post.
default	20:42:08.175168-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:08.175268-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:08.175370-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:08.189086-0500	Nexy	registering darwin observer for name: com.apple.gms.availability.notification
default	20:42:08.189112-0500	Nexy	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	20:42:08.189138-0500	Nexy	registering darwin observer for name: com.apple.language.changed
default	20:42:08.189167-0500	Nexy	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	20:42:08.193404-0500	Nexy	[0x8ec73b980] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:42:08.196305-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	20:42:08.201195-0500	Nexy	[0x8ec7383c0] Connection returned listener port: 0x5003
default	20:42:08.201670-0500	Nexy	SignalReady: pid=84081 asn=0x0-0x183082f
default	20:42:08.202100-0500	Nexy	SIGNAL: pid=84081 asn=0x0x-0x183082f
default	20:42:08.202748-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:42:08.216195-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.219352-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.221864-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:42:08.221877-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:42:08.221894-0500	Nexy	[0x8ec73aa80] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:42:08.221971-0500	Nexy	[0x8ec73aa80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:08.227679-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:42:08.229830-0500	Nexy	[C:2] Alloc <private>
default	20:42:08.229870-0500	Nexy	[0x8ec73aa80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:08.231668-0500	WindowManager	Connection activated | (84081) Nexy
default	20:42:08.231741-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-84081). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:42:08.233391-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-84081)
default	20:42:08.233850-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(7FDB7B64, (bid:com.nexy.assistant-Item-0-84081)) for (bid:com.nexy.assistant-Item-0-84081)
default	20:42:08.234560-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-84081)]
default	20:42:08.235193-0500	ControlCenter	Created instance DisplayableId(4E448296) in .menuBar for DisplayableAppStatusItemType(7FDB7B64, (bid:com.nexy.assistant-Item-0-84081)) .menuBar
default	20:42:08.244601-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.245198-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.248210-0500	ControlCenter	Created ephemaral instance DisplayableId(4E448296) for (bid:com.nexy.assistant-Item-0-84081) with positioning .ephemeral
default	20:42:08.250690-0500	Nexy	[0x8ec739540] activating connection: mach=false listener=false peer=false name=com.apple.ImageIOXPCService
default	20:42:08.297775-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:42:08.299396-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:42:08.299974-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	20:42:08.300086-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.311098-0500	Nexy	[com.apple.controlcenter:1039EA85-E525-4644-A9EB-34D0A81B7300] Sending action(s) in update: NSSceneFenceAction
default	20:42:08.392918-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:42:08.396517-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:42:08.397281-0500	Nexy	[GMS] availability notification token 92
default	20:42:08.505620-0500	ControlCenter	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC>:84081] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:42:08.505747-0500	runningboardd	Invalidating assertion 394-638-1350084 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	20:42:08.610047-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:08.610084-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:08.610110-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:08.610161-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:08.614504-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:08.615531-0500	ControlCenter	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.622188-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.726907-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-1350089 target:84081 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:42:08.727030-0500	runningboardd	Assertion 394-387-1350089 (target:[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081]) will be created as active
default	20:42:08.727401-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:08.727416-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:08.727431-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:08.727451-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:08.730123-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:08.730545-0500	ControlCenter	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:08.730631-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:10.246709-0500	runningboardd	Invalidating assertion 394-638-1350081 (target:app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>) from originator [osservice<com.apple.controlcenter(501)>:638]
default	20:42:10.353491-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>
default	20:42:10.354717-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring jetsam update because this process is not memory-managed
default	20:42:10.354727-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring suspend because this process is not lifecycle managed
default	20:42:10.354734-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring GPU update because this process is not GPU managed
default	20:42:10.354752-0500	runningboardd	[app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>:84081] Ignoring memory limit update because this process is not memory-managed
default	20:42:10.357687-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:10.364511-0500	ControlCenter	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:10.364816-0500	gamepolicyd	Received state update for 84081 (app<application.com.nexy.assistant.41964753.41964762.D3450E74-8385-40E1-8BA1-CB5750D58EBC(501)>, running-active-NotVisible
default	20:42:13.116172-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
