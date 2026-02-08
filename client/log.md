default	20:02:11.267388-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:02:11.267551-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:02:11.269750-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:02:11.272795-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:02:11.278472-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53705040.53705049(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:02:11.278552-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53705040.53705049(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:587] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-587-16034 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:02:11.278637-0500	runningboardd	Assertion 403-587-16034 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) will be created as active
default	20:02:11.282085-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:02:11.282120-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:02:11.282133-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:02:11.282216-0500	runningboardd	app<application.com.nexy.assistant.53705040.53705049(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:02:11.312130-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] is not RunningBoard jetsam managed.
default	20:02:11.312146-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] This process will not be managed.
default	20:02:11.312160-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:02:11.312324-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:11.313133-0500	gamepolicyd	Hit the server for a process handle 1a89d7a600001ba3 that resolved to: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:02:11.313178-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:11.315963-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:02:11.316035-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-16035 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:11.316176-0500	runningboardd	Assertion 403-403-16035 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:11.316378-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:11.316396-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:11.316416-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Set darwin role to: UserInteractive
default	20:02:11.316437-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:11.316476-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:11.316515-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] reported to RB as running
default	20:02:11.318337-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:7075" ID:403-367-16036 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:02:11.318469-0500	runningboardd	Assertion 403-367-16036 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:11.318528-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x11d11d com.nexy.assistant starting stopped process.
default	20:02:11.319698-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:02:11.319866-0500	loginwindow	-[Application setState:] | enter: <Application: 0x897ae0320: Nexy> state 2
default	20:02:11.319894-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:02:11.320761-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:11.320791-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:11.320810-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:11.320854-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:11.320950-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:02:11.321794-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:11.322086-0500	runningboardd	Invalidating assertion 403-587-16034 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:587]
default	20:02:11.322125-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:11.322140-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:11.322155-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:11.322235-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:11.322243-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:11.325324-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:11.427459-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:11.436640-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:11.436647-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:11.436671-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:11.436727-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:11.440800-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:11.442151-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:02:11.442534-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:11.443736-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=501.22, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=501, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:02:11.450050-0500	tccd	AUTHREQ_SUBJECT: msgID=501.22, subject=com.nexy.assistant,
default	20:02:11.450789-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:11.462608-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	20:02:11.467677-0500	kernel	Nexy[7075] triggered unnest of range 0x1f4000000->0x1f6000000 of DYLD shared region in VM map 0x3fe20fbe9d681b89. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:02:11.467696-0500	kernel	Nexy[7075] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x3fe20fbe9d681b89. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:02:11.662201-0500	Nexy	[0x1052fcb70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:02:11.662277-0500	Nexy	[0x1052fd0b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:02:11.889164-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1052ec480 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:02:11.889401-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1052ec480 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:02:11.889614-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1052ec480 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:02:11.889816-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1052ec480 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:02:11.891149-0500	Nexy	[0x1052edf80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:02:11.891896-0500	Nexy	[0x9b56f4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:02:11.892242-0500	Nexy	[0x9b56f4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:02:11.892678-0500	Nexy	[0x9b56f4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:02:11.892853-0500	Nexy	Received configuration update from daemon (initial)
default	20:02:11.894778-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:02:11.895147-0500	Nexy	[0x9b56f43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:02:11.895807-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:02:11.897377-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.1, subject=com.nexy.assistant,
default	20:02:11.898164-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:11.910943-0500	Nexy	[0x9b56f43c0] invalidated after the last release of the connection object
default	20:02:11.917387-0500	Nexy	server port 0x0000380f, session port 0x0000380f
default	20:02:11.918514-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.723, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:02:11.918541-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:02:11.919681-0500	tccd	AUTHREQ_SUBJECT: msgID=397.723, subject=com.nexy.assistant,
default	20:02:11.920412-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:11.935544-0500	Nexy	New connection 0xfe307 main
default	20:02:11.938045-0500	Nexy	CHECKIN: pid=7075
default	20:02:11.945437-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:7075" ID:403-367-16037 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:02:11.945545-0500	runningboardd	Assertion 403-367-16037 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:11.945714-0500	Nexy	CHECKEDIN: pid=7075 asn=0x0-0x11d11d foreground=0
default	20:02:11.945560-0500	launchservicesd	CHECKIN:0x0-0x11d11d 7075 com.nexy.assistant
default	20:02:11.946044-0500	runningboardd	Invalidating assertion 403-367-16036 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	20:02:11.946014-0500	Nexy	[0x9b56f43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:02:11.946074-0500	Nexy	[0x9b56f43c0] Connection returned listener port: 0x4e03
default	20:02:11.946985-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:02:11.947112-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:02:11.946454-0500	Nexy	[0x9b4b38300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9b56f43c0.peer[367].0x9b4b38300
default	20:02:11.948380-0500	Nexy	FRONTLOGGING: version 1
default	20:02:11.948420-0500	Nexy	Registered, pid=7075 ASN=0x0,0x11d11d
default	20:02:11.948761-0500	WindowServer	fe307[CreateApplication]: Process creation: 0x0-0x11d11d (Nexy) connectionID: FE307 pid: 7075 in session 0x101
default	20:02:11.948987-0500	Nexy	[0x9b56f4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:02:11.950915-0500	Nexy	[0x9b56f43c0] Connection returned listener port: 0x4e03
default	20:02:11.951721-0500	Nexy	BringForward: pid=7075 asn=0x0-0x11d11d bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:02:11.951906-0500	Nexy	BringFrontModifier: pid=7075 asn=0x0-0x11d11d Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:02:11.952580-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:02:11.954322-0500	Nexy	No persisted cache on this platform.
default	20:02:11.955379-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:02:11.955965-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:02:11.958842-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:02:11.958854-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:02:11.958913-0500	Nexy	Initializing connection
default	20:02:11.958952-0500	Nexy	Removing all cached process handles
default	20:02:11.958981-0500	Nexy	Sending handshake request attempt #1 to server
default	20:02:11.958992-0500	Nexy	Creating connection to com.apple.runningboard
default	20:02:11.959001-0500	Nexy	[0x9b56f4640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:02:11.959462-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] as ready
default	20:02:11.960118-0500	Nexy	Handshake succeeded
default	20:02:11.960134-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:02:11.960710-0500	Nexy	[0x9b56f43c0] Connection returned listener port: 0x4e03
default	20:02:11.961731-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 7075
default	20:02:11.964807-0500	Nexy	[0x9b56f43c0] Connection returned listener port: 0x4e03
default	20:02:11.968769-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:02:11.968791-0500	Nexy	[0x9b56f4780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:02:11.968875-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:02:11.968921-0500	Nexy	[0x9b56f4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:02:11.970051-0500	Nexy	[0x9b56f4a00] Connection returned listener port: 0x6503
default	20:02:11.970678-0500	Nexy	Registered process with identifier 7075-216020
default	20:02:13.437994-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5C40919B-3AC7-418D-82B8-44209A51089A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57930,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x41ce1354 tp_proto=0x06"
default	20:02:13.438085-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57930<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208227 t_state: SYN_SENT process: Nexy:7075 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99eb2eef
default	20:02:14.950747-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:02:16.401659-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-16035 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075])
default	20:02:16.602340-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:16.602370-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:16.602391-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:16.602427-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:16.608692-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:16.609426-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:18.439126-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57930<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208227 t_state: SYN_SENT process: Nexy:7075 Duration: 5.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x99eb2eef
default	20:02:18.439157-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57930<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208227 t_state: SYN_SENT process: Nexy:7075 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:02:18.439779-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 455692FA-FBF1-4422-AEE3-A2C82D5FA914 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57937,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3cd4303e tp_proto=0x06"
default	20:02:18.439915-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57937<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208338 t_state: SYN_SENT process: Nexy:7075 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb11d35d5
default	20:02:22.943037-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:02:23.439800-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57937<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208338 t_state: SYN_SENT process: Nexy:7075 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb11d35d5
default	20:02:23.439836-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57937<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208338 t_state: SYN_SENT process: Nexy:7075 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:02:23.446146-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:02:23.446521-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:02:23.448620-0500	Nexy	nw_path_libinfo_path_check [E76E92B4-F9F4-4998-96DA-A426D109FD0B Hostname#a8bb35f0:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:02:23.449291-0500	mDNSResponder	[R21732] DNSServiceCreateConnection START PID[7075](Nexy)
default	20:02:23.449445-0500	mDNSResponder	[R21733] DNSServiceQueryRecord START -- qname: <mask.hash: 'PAT+qg22Mu/apI2NzrlwIw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 7075 (Nexy), name hash: f92d5498
default	20:02:23.450270-0500	mDNSResponder	[R21734] DNSServiceQueryRecord START -- qname: <mask.hash: 'PAT+qg22Mu/apI2NzrlwIw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 7075 (Nexy), name hash: f92d5498
default	20:02:23.561304-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4115B01D-1D39-4003-87B4-F1B9DDC18E44 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57938,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xa2610fc9 tp_proto=0x06"
default	20:02:23.561434-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57938<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208359 t_state: SYN_SENT process: Nexy:7075 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x94422b15
default	20:02:28.440334-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57938<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208359 t_state: SYN_SENT process: Nexy:7075 Duration: 4.879 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x94422b15
default	20:02:28.440370-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57938<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208359 t_state: SYN_SENT process: Nexy:7075 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:02:29.550293-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:02:29.551146-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:02:29.552747-0500	Nexy	[0x9b56f4dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:02:29.555636-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
default	20:02:29.559040-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:02:29.561652-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:02:29.561815-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:02:29.561954-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:02:29.561965-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:02:29.561997-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:02:29.562123-0500	Nexy	[0x9b56f4f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:02:29.562319-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:02:29.562661-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:02:29.570003-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.2, subject=com.nexy.assistant,
default	20:02:29.570638-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:02:29.581809-0500	Nexy	[0x9b56f4f00] invalidated after the last release of the connection object
default	20:02:29.581861-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:02:29.584856-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	20:02:29.585968-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.273, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:29.586962-0500	tccd	AUTHREQ_SUBJECT: msgID=410.273, subject=com.nexy.assistant,
default	20:02:29.587548-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3de00 at /Applications/Nexy.app
error	20:02:29.598834-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=410, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:02:29.599742-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.275, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:29.600641-0500	tccd	AUTHREQ_SUBJECT: msgID=410.275, subject=com.nexy.assistant,
default	20:02:29.601185-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3de00 at /Applications/Nexy.app
default	20:02:29.613929-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:02:29.613949-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9b2649d80> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:02:29.630100-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:02:29.630230-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:02:29.634773-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:02:29.640644-0500	Nexy	[0x9b56f4f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:02:29.654047-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9b23ea340) Selecting device 85 from constructor
default	20:02:29.654057-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:29.654064-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:29.654072-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9b23ea340) nothing to teardown
default	20:02:29.654077-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9b23ea340) connecting device 85
default	20:02:29.654149-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9b23ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:02:29.654223-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9b23ea340) created ioproc 0xa for device 85
default	20:02:29.654320-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 7 device listeners to device 85
default	20:02:29.654481-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 85
default	20:02:29.654489-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9b23ea340)
default	20:02:29.654556-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:02:29.654561-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:02:29.654567-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:02:29.654572-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:02:29.654580-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:02:29.654668-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:02:29.654679-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:02:29.654686-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:02:29.654695-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device listeners from device 0
default	20:02:29.654702-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 0
default	20:02:29.654706-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:29.654721-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:02:29.654784-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9b23ea340) caller requesting device change from 85 to 91
default	20:02:29.654794-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:29.654799-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:29.654803-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9b23ea340) disconnecting device 85
default	20:02:29.654808-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9b23ea340) destroying ioproc 0xa for device 85
default	20:02:29.655133-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:02:29.657054-0500	Nexy	[0x9b56f5180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:02:29.658204-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":{"PID":7075,"session_type":"Primary"} }
default	20:02:29.658272-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":7075}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1fe015, sessionType: 'prim', isRecording: false }, 
]
default	20:02:29.658871-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 7075, name = Nexy
default	20:02:29.659096-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9b5767860 with ID: 0x1fe015
default	20:02:29.660301-0500	Nexy	[0x9b56f52c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:02:29.660598-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=30386893619201 }
default	20:02:29.660614-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:02:29.660662-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:02:29.660744-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9b23ea340) connecting device 91
default	20:02:29.660815-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9b23ea340) Device ID: 91 (Input:Yes | Output:No): true
default	20:02:29.661878-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.276, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:29.663047-0500	tccd	AUTHREQ_SUBJECT: msgID=410.276, subject=com.nexy.assistant,
default	20:02:29.663671-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3de00 at /Applications/Nexy.app
default	20:02:29.678718-0500	tccd	AUTHREQ_PROMPTING: msgID=410.276, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:02:32.978950-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    487 = "<TCCDEventSubscriber: token=487, state=Passed, csid=com.apple.photolibraryd>";
    457 = "<TCCDEventSubscriber: token=457, state=Initial, csid=(null)>";
    484 = "<TCCDEventSubscriber: token=484, state=Passed, csid=com.apple.chronod>";
}
default	20:02:32.979537-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9b23ea340) created ioproc 0xa for device 91
default	20:02:32.979686-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:02:32.979756-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 7 device listeners to device 91
default	20:02:32.980006-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 91
default	20:02:32.980021-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9b23ea340)
default	20:02:32.980036-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:02:32.980051-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:02:32.980237-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:02:32.980248-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:02:32.980256-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:02:32.980374-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:02:32.980391-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:02:32.980401-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:02:32.980407-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 7 device listeners from device 85
default	20:02:32.980608-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 85
default	20:02:32.980622-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:32.981152-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:02:32.982803-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.277, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:32.984339-0500	tccd	AUTHREQ_SUBJECT: msgID=410.277, subject=com.nexy.assistant,
default	20:02:32.987065-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3de00 at /Applications/Nexy.app
default	20:02:33.008580-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:02:33.009387-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:02:33.009501-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9b69fcab0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:02:33.009752-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:02:33.011538-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.278, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:33.014161-0500	tccd	AUTHREQ_SUBJECT: msgID=410.278, subject=com.nexy.assistant,
default	20:02:33.015024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3de00 at /Applications/Nexy.app
default	20:02:33.032933-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.279, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:33.033938-0500	tccd	AUTHREQ_SUBJECT: msgID=410.279, subject=com.nexy.assistant,
default	20:02:33.034593-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:33.051723-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:02:33.052104-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:02:33.052248-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:02:33.052258-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:02:33.053366-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:02:33.054779-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:02:33.055502-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:33.055567-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:33.136845-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:02:33.138163-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:970 called from <private>
default	20:02:33.138180-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:02:33.138652-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:33.138681-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:33.138689-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:33.138848-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:33.139197-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:33.139210-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:970 called from <private>
default	20:02:33.140958-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16095 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:33.139216-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:970 called from <private>
default	20:02:33.141467-0500	runningboardd	Assertion 403-338-16095 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
fault	20:02:33.142855-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
default	20:02:33.144733-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:33.144803-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:33.144932-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:33.145499-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:02:33.145589-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
fault	20:02:33.145718-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
default	20:02:33.146559-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:02:33.148453-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:33.148475-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:970 called from <private>
default	20:02:33.148482-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:970 called from <private>
default	20:02:33.148504-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:33.148519-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:33.148523-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:970 called from <private>
default	20:02:33.148529-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:33.148530-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:970 called from <private>
default	20:02:33.148641-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:970 called from <private>
default	20:02:33.148694-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:970 called from <private>
default	20:02:33.148775-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:970 called from <private>
default	20:02:33.148889-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:970 called from <private>
default	20:02:33.149828-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:970 called from <private>
default	20:02:33.149867-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:970 called from <private>
default	20:02:33.154444-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:02:33.155119-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:02:33.155405-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:33.155962-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:33.155873-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1fe015, Nexy(7075), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:02:33.156061-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:33.156352-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:02:33.156435-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1fe015, Nexy(7075), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 22 starting recording
default	20:02:33.153866-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:33.156893-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:33.157063-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:02:33.157228-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe015, Nexy(7075), 'prim'', displayID:'com.nexy.assistant'}
default	20:02:33.154372-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:33.154443-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:33.156059-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.154643-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:33.154674-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:33.157994-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:02:33.158499-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:02:33.156744-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.280, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:33.158003-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:02:33.158366-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.165745-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:33.165761-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:33.165873-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:33.165375-0500	tccd	AUTHREQ_SUBJECT: msgID=410.280, subject=com.nexy.assistant,
default	20:02:33.168416-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:33.170773-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:33.171165-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:33.172357-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.172594-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:33.171179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:33.171272-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:33.175837-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:33.175071-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.176127-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:33.176136-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:33.176773-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:33.176794-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:33.176912-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:33.173295-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:02:33.177017-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:33.177251-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:33.177544-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:33.177737-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:33.177871-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:33.175720-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.177952-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:33.178101-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:33.175575-0500	runningboardd	Invalidating assertion 403-338-16095 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.powerd>:338]
default	20:02:33.178188-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.178245-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:33.179559-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:33.178443-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:33.178675-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:33.178905-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:33.175688-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:33.179097-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:33.180787-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:33.179253-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:33.192150-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:02:33.192224-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:02:33.192255-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:33.192373-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:33.196361-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:02:33.203629-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16096 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:33.204262-0500	runningboardd	Assertion 403-338-16096 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:33.203605-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:970 called from <private>
default	20:02:33.203664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:970 called from <private>
default	20:02:33.204874-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:02:33.205569-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:33.205672-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:33.205689-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:970 called from <private>
default	20:02:33.205696-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:970 called from <private>
default	20:02:33.205806-0500	runningboardd	Invalidating assertion 403-338-16096 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.powerd>:338]
default	20:02:33.210704-0500	tccd	AUTHREQ_SUBJECT: msgID=410.281, subject=com.nexy.assistant,
default	20:02:33.211911-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:33.230897-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:02:33.233423-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:33.233486-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:33.271965-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:02:33.275800-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:970 called from <private>
default	20:02:33.275859-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:970 called from <private>
default	20:02:33.276144-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16098 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:33.276253-0500	runningboardd	Assertion 403-338-16098 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:33.277765-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:33.277815-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:02:33.278079-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:02:33.278201-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:33.278162-0500	runningboardd	Invalidating assertion 403-338-16098 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.powerd>:338]
default	20:02:33.277895-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:33.278255-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:02:33.278281-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe015, Nexy(7075), 'prim'', displayID:'com.nexy.assistant'}
default	20:02:33.277910-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:970 called from <private>
default	20:02:33.277918-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:970 called from <private>
default	20:02:33.278333-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1fe015, Nexy(7075), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 22 stopping recording
default	20:02:33.278346-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:02:33.278364-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:02:33.278450-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:33.278527-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:33.278744-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:02:33.278755-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:02:33.278763-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:02:33.278934-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:02:33.279153-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:33.279236-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:33.279192-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.279285-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:33.279320-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:02:33.279225-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:02:33.279345-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.279448-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:02:33.279849-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:33.279496-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:33.279565-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:02:33.280076-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:970 called from <private>
default	20:02:33.280083-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:970 called from <private>
default	20:02:33.280097-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:33.280109-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:970 called from <private>
default	20:02:33.285156-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:33.285181-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:33.285201-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:33.285228-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:33.287040-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:02:33.287137-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:02:33.287184-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:33.287420-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:33.287961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.287998-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.288016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:33.288028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.288048-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:33.288055-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:02:33.288466-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:02:33.288516-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.288575-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.288630-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:33.288666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:33.288707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:33.288743-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:02:33.289278-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:02:33.291285-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:33.292145-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:33.391391-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9b23ea340) Selecting device 0 from destructor
default	20:02:33.391402-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:33.391407-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:33.391412-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9b23ea340) disconnecting device 91
default	20:02:33.391416-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9b23ea340) destroying ioproc 0xa for device 91
default	20:02:33.391437-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:02:33.391459-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:02:33.391562-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9b23ea340) nothing to setup
default	20:02:33.391571-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device listeners to device 0
default	20:02:33.391575-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 0
default	20:02:33.391578-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 7 device listeners from device 91
default	20:02:33.391722-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 91
default	20:02:33.391737-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:35.961096-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:35.961163-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:35.961179-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:35.963036-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:35.963077-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:970 called from <private>
default	20:02:35.963090-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:35.966859-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:35.967119-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:35.967334-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:35.967492-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:35.967714-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:35.971472-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:35.971514-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:35.972630-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:35.974364-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:35.974386-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:35.974436-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:35.974448-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:35.974457-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:35.974464-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:35.974472-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:35.974636-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:35.978856-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:35.978899-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:35.978907-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:970 called from <private>
default	20:02:35.980285-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:35.980304-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:35.980643-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:35.992053-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:35.992079-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:35.992161-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:35.997958-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:35.998508-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:35.998529-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:35.998666-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:36.002413-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:36.002666-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:36.002676-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:36.002720-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:36.002728-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:36.002739-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:36.002748-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:36.002772-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:36.002866-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:36.002933-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:36.003073-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:36.003226-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:36.003360-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:46.396953-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9b23ea340) Selecting device 85 from constructor
default	20:02:46.396990-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:46.397006-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:46.397020-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9b23ea340) nothing to teardown
default	20:02:46.397031-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9b23ea340) connecting device 85
default	20:02:46.397278-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9b23ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:02:46.397526-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9b23ea340) created ioproc 0xb for device 85
default	20:02:46.397819-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 7 device listeners to device 85
default	20:02:46.398281-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 85
default	20:02:46.398310-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9b23ea340)
default	20:02:46.398509-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:02:46.398535-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:02:46.398552-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:02:46.398571-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:02:46.398592-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:02:46.398849-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:02:46.398876-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:02:46.398894-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:02:46.398906-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device listeners from device 0
default	20:02:46.398936-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 0
default	20:02:46.398956-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:46.398984-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:02:46.399125-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9b23ea340) caller requesting device change from 85 to 91
default	20:02:46.399149-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:46.399166-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:46.399178-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9b23ea340) disconnecting device 85
default	20:02:46.399188-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9b23ea340) destroying ioproc 0xb for device 85
default	20:02:46.399229-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:02:46.399305-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:02:46.399499-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9b23ea340) connecting device 91
default	20:02:46.399729-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9b23ea340) Device ID: 91 (Input:Yes | Output:No): true
default	20:02:46.402937-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.282, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:46.405620-0500	tccd	AUTHREQ_SUBJECT: msgID=410.282, subject=com.nexy.assistant,
default	20:02:46.407004-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.431153-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9b23ea340) created ioproc 0xb for device 91
default	20:02:46.431344-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 7 device listeners to device 91
default	20:02:46.431531-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 91
default	20:02:46.431541-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9b23ea340)
default	20:02:46.431552-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:02:46.431565-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:02:46.431699-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:02:46.431708-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:02:46.431713-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:02:46.431811-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:02:46.431822-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9b23ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:02:46.431827-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:02:46.431833-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 7 device listeners from device 85
default	20:02:46.432017-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 85
default	20:02:46.432024-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:46.432035-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:02:46.432363-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:02:46.433720-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.283, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:46.435035-0500	tccd	AUTHREQ_SUBJECT: msgID=410.283, subject=com.nexy.assistant,
default	20:02:46.435683-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.451169-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9b69fcab0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:02:46.451368-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:02:46.452336-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.284, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:46.453398-0500	tccd	AUTHREQ_SUBJECT: msgID=410.284, subject=com.nexy.assistant,
default	20:02:46.454019-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.470520-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.285, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:46.471441-0500	tccd	AUTHREQ_SUBJECT: msgID=410.285, subject=com.nexy.assistant,
default	20:02:46.472028-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.487854-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:02:46.488028-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:02:46.490120-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:970 called from <private>
default	20:02:46.490139-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:02:46.490170-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:02:46.490972-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:46.491225-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:46.491239-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:46.491251-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:970 called from <private>
default	20:02:46.491261-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:970 called from <private>
default	20:02:46.491262-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:46.494633-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16101 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:46.491271-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:46.494756-0500	runningboardd	Assertion 403-338-16101 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:46.495521-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:46.495590-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:46.496073-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:46.496675-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:46.499530-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:02:46.500178-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:02:46.501920-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:46.501944-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:46.501948-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:970 called from <private>
default	20:02:46.501955-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:46.501956-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:970 called from <private>
default	20:02:46.501966-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:970 called from <private>
default	20:02:46.501971-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:970 called from <private>
default	20:02:46.501979-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:46.502022-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:970 called from <private>
default	20:02:46.502080-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:970 called from <private>
default	20:02:46.502221-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:970 called from <private>
default	20:02:46.507364-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:02:46.508374-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:02:46.508460-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1fe015, Nexy(7075), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:02:46.508786-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:46.502250-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:970 called from <private>
default	20:02:46.504528-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:970 called from <private>
default	20:02:46.508970-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1fe015, Nexy(7075), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:02:46.509193-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:46.509227-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.509337-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:46.509768-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:02:46.509825-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1fe015, Nexy(7075), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 22 starting recording
default	20:02:46.510194-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:46.504625-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:970 called from <private>
default	20:02:46.506246-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:46.506937-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:46.507431-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:46.510899-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:02:46.509284-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:46.509322-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:46.511077-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe015, Nexy(7075), 'prim'', displayID:'com.nexy.assistant'}
default	20:02:46.509061-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.286, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:02:46.511313-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:02:46.511393-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:02:46.509460-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.511548-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.516872-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:46.509953-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.516882-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:46.517009-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:46.511614-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:02:46.519742-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:46.520925-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:46.520030-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:46.520039-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:46.520173-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:46.524168-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:46.522099-0500	runningboardd	Invalidating assertion 403-338-16101 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.powerd>:338]
default	20:02:46.524363-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:46.524374-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:46.524657-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:46.522325-0500	tccd	AUTHREQ_SUBJECT: msgID=410.286, subject=com.nexy.assistant,
default	20:02:46.524666-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:46.524677-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:46.524683-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:46.524691-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:46.524696-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:46.524701-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:46.524745-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:46.524766-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:46.524904-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:46.524974-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:46.525048-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:46.525141-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:46.525193-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:46.525299-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:46.525547-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.530381-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:46.533092-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:46.533473-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:46.533483-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:46.533489-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:46.533500-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:46.535672-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.536019-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.537712-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:02:46.539947-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.540255-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.541874-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.541913-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:02:46.541923-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:02:46.541935-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	20:02:46.542035-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	20:02:46.542139-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:02:46.554882-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:02:46.567348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.587209-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:02:46.590389-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:46.590553-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:02:46.631330-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:46.631349-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:46.631391-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:46.631448-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:46.639792-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:46.640062-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:970 called from <private>
default	20:02:46.640073-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:970 called from <private>
default	20:02:46.640085-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:46.644032-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3cf00 at /Applications/Nexy.app
default	20:02:46.665779-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16112 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:02:46.666224-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:970 called from <private>
default	20:02:46.665879-0500	runningboardd	Assertion 403-338-16112 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:02:46.675775-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:02:46.675827-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:02:46.675925-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:46.676263-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.676286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.676302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:46.676314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.806468-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:02:46.806787-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:02:46.806891-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:46.806946-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:02:46.806977-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe015, Nexy(7075), 'prim'', displayID:'com.nexy.assistant'}
default	20:02:46.807029-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1fe015, Nexy(7075), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 22 stopping recording
default	20:02:46.807035-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:02:46.807058-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:02:46.807102-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:02:46.807132-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:02:46.807259-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:02:46.807275-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:02:46.807364-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:02:46.807629-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.807668-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.807708-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.807751-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:02:46.807784-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.807806-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:02:46.807868-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:02:46.807883-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:02:46.807892-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:02:46.809561-0500	runningboardd	Invalidating assertion 403-338-16112 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.powerd>:338]
default	20:02:46.811177-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:02:46.819098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.819117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.819130-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:46.819143-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:02:46.819150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:02:46.819156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:02:46.819297-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:02:46.851597-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:02:46.851620-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:02:46.851633-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:02:46.851651-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:02:46.855389-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:02:46.867568-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:02:46.908427-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9b23ea340) Selecting device 0 from destructor
default	20:02:46.908443-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9b23ea340)
default	20:02:46.908452-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9b23ea340) not already running
default	20:02:46.908458-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9b23ea340) disconnecting device 91
default	20:02:46.908467-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9b23ea340) destroying ioproc 0xb for device 91
default	20:02:46.908508-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:02:46.908560-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:02:46.908736-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9b23ea340) nothing to setup
default	20:02:46.908752-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device listeners to device 0
default	20:02:46.908761-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9b23ea340) adding 0 device delegate listeners to device 0
default	20:02:46.908767-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 7 device listeners from device 91
default	20:02:46.908994-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9b23ea340) removing 0 device delegate listeners from device 91
default	20:02:46.909014-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9b23ea340)
default	20:02:49.161946-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:49.162019-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:49.162038-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:49.164325-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(970)
default	20:02:49.164371-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:970 called from <private>
default	20:02:49.164383-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:970 called from <private>
default	20:02:49.171241-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:49.171269-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:49.171926-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:49.171955-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:49.171962-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:49.174242-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:49.174280-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:49.174506-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:49.177259-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:49.177582-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:49.177594-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:49.177609-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:49.177623-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:49.177632-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:49.177639-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:49.177686-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:49.177812-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:49.178158-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(970)
default	20:02:49.178523-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:970 called from <private>
default	20:02:49.178587-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:970 called from <private>
default	20:02:49.179308-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:969 called from <private>
default	20:02:49.179368-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:969 called from <private>
default	20:02:49.192621-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:969 called from <private>
default	20:02:49.192655-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:969 called from <private>
default	20:02:49.192770-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:49.196547-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:49.197047-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:969 called from <private>
default	20:02:49.197062-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:969 called from <private>
default	20:02:49.197303-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(969)
default	20:02:49.203310-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(969)
default	20:02:49.203632-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:969 called from <private>
default	20:02:49.203645-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:969 called from <private>
default	20:02:49.203712-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:49.203720-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:49.203728-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:49.203733-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:49.203990-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:49.204114-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:49.204247-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:969 called from <private>
default	20:02:49.204375-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:969 called from <private>
default	20:02:49.204497-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:969 called from <private>
default	20:02:49.204643-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:969 called from <private>
default	20:02:49.918204-0500	Nexy	[0x9b56f5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:02:49.920036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:02:49.923091-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.3, subject=com.nexy.assistant,
default	20:02:49.924341-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:49.944046-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[7075], responsiblePID[7075], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:02:49.944420-0500	Nexy	[0x9b56f5540] invalidated after the last release of the connection object
default	20:02:49.999373-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:02:50.018857-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:50.023077-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:02:57.430917-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:02:57.449951-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:02:57.459721-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:02:57.524765-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:02:57.526840-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:02:57.561824-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:02:57.561886-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:03:02.952686-0500	Nexy	[0x9b56f5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:03:02.954399-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:02.956690-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.4, subject=com.nexy.assistant,
default	20:03:02.958141-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:02.983436-0500	Nexy	[0x9b56f5540] invalidated after the last release of the connection object
default	20:03:02.986210-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	20:03:02.989268-0500	Nexy	[0x9b56f5540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:03:02.989425-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:03:02.989880-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:03:02.996165-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75614.32, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:03:02.996196-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:02.997176-0500	tccd	AUTHREQ_SUBJECT: msgID=75614.32, subject=com.nexy.assistant,
default	20:03:02.997869-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:03.022145-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.749, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:03:03.022171-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:03.022957-0500	tccd	AUTHREQ_SUBJECT: msgID=397.749, subject=com.nexy.assistant,
default	20:03:03.023546-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:03.042474-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	20:03:03.070178-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:03:03.070311-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:03:03.070367-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:03:03.071772-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:03:03.071784-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:03:03.071810-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:03:03.071816-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:03:03.071825-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:03:03.071830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:03:03.072045-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:03:06.075596-0500	Nexy	[0x9b56f5680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:03:06.076250-0500	Nexy	[0x9b56f57c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:03:06.076709-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:06.076888-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:06.078805-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.6, subject=com.nexy.assistant,
default	20:03:06.079777-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f600 at /Applications/Nexy.app
default	20:03:06.080054-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.5, subject=com.nexy.assistant,
default	20:03:06.081846-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3e400 at /Applications/Nexy.app
default	20:03:06.094296-0500	Nexy	[0x9b56f57c0] invalidated after the last release of the connection object
default	20:03:06.094435-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:03:06.095606-0500	Nexy	[0x9b56f57c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:03:06.096087-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:06.097174-0500	Nexy	[0x9b56f5680] invalidated after the last release of the connection object
default	20:03:06.097193-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.7, subject=com.nexy.assistant,
default	20:03:06.097806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:06.112989-0500	tccd	AUTHREQ_PROMPTING: msgID=7075.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:03:07.824240-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    487 = "<TCCDEventSubscriber: token=487, state=Passed, csid=com.apple.photolibraryd>";
    457 = "<TCCDEventSubscriber: token=457, state=Initial, csid=(null)>";
    484 = "<TCCDEventSubscriber: token=484, state=Passed, csid=com.apple.chronod>";
}
default	20:03:07.824753-0500	Nexy	[0x9b56f57c0] invalidated after the last release of the connection object
default	20:03:07.825668-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:03:07.828543-0500	Nexy	[0x9b56f57c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:03:07.829843-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=59315.107, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=59315, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:03:07.832324-0500	tccd	AUTHREQ_SUBJECT: msgID=59315.107, subject=com.nexy.assistant,
default	20:03:07.833333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:07.862292-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=59315.108, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=59315, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:03:07.863605-0500	tccd	AUTHREQ_SUBJECT: msgID=59315.108, subject=com.nexy.assistant,
default	20:03:07.864702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:07.888381-0500	Nexy	[0x9b56f5680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:03:07.889691-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:03:07.889767-0500	Nexy	<private> 0x9b5016e80: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:03:07.889863-0500	Nexy	<private> 0x9b5016e80: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:03:07.890868-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:03:07.905328-0500	Nexy	[0x9b56f5900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:03:07.905981-0500	Nexy	[0x9b56f5900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:07.906025-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:03:07.906229-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:03:07.908971-0500	Nexy	[0x9b50803c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:07.909939-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1451, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:07.909976-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:07.911359-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1451, subject=com.nexy.assistant,
default	20:03:07.912163-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:07.931756-0500	Nexy	[0x9b50803c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:07.931960-0500	Nexy	[0x9b50803c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:07.932080-0500	Nexy	[0x9b5080500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:07.933023-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1452, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:07.933053-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:07.934293-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1452, subject=com.nexy.assistant,
default	20:03:07.935024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:07.958796-0500	Nexy	[0x9b5080500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:07.958872-0500	Nexy	[0x9b5080500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:07.958941-0500	Nexy	[0x9b5080640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:07.959774-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1453, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:07.959816-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:07.961101-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1453, subject=com.nexy.assistant,
default	20:03:07.961873-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:07.980097-0500	Nexy	[0x9b5080640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:07.980154-0500	Nexy	[0x9b5080640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:07.980209-0500	Nexy	[0x9b5080780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:07.980998-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1454, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:07.981031-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:07.982234-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1454, subject=com.nexy.assistant,
default	20:03:07.982913-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.005805-0500	Nexy	[0x9b5080780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.005870-0500	Nexy	[0x9b5080780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.020667-0500	Nexy	Did add XPC store
default	20:03:08.020704-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:03:08.023190-0500	Nexy	0x9b56079a0: Using cached account information
default	20:03:08.023972-0500	Nexy	[0x9b4b6f6b0] Session created.
default	20:03:08.023983-0500	Nexy	[0x9b4b6f6b0] Session created with Mach Service: <private>
default	20:03:08.023989-0500	Nexy	[0x9b5080dc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:03:08.024104-0500	Nexy	[0x9b4b6f6b0] Session activated
default	20:03:08.026182-0500	Nexy	[0x9b5080dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.026190-0500	Nexy	[0x9b4b6f6b0] Session canceled.
default	20:03:08.026201-0500	Nexy	[0x9b4b6f6b0] Disposing of session
default	20:03:08.026510-0500	Nexy	[0x9b5080dc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:03:08.027024-0500	Nexy	[0x9b5080dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.027045-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:03:08.027062-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:03:08.032265-0500	Nexy	[0x9b5083840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.033457-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1455, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.033494-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.035073-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1455, subject=com.nexy.assistant,
default	20:03:08.035887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.062253-0500	Nexy	[0x9b5083840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.062346-0500	Nexy	[0x9b5083840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.062422-0500	Nexy	[0x9b5083980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.063550-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1456, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.063594-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.065100-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1456, subject=com.nexy.assistant,
default	20:03:08.065922-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.092243-0500	Nexy	[0x9b5083980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.092346-0500	Nexy	[0x9b5083980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.092437-0500	Nexy	[0x9b5083ac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.093591-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1457, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.093626-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.095134-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1457, subject=com.nexy.assistant,
default	20:03:08.095912-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.120894-0500	Nexy	[0x9b5083ac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.121068-0500	Nexy	[0x9b5083ac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.121171-0500	Nexy	[0x9b5083c00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.122319-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1458, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.122355-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.124038-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1458, subject=com.nexy.assistant,
default	20:03:08.124926-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.148960-0500	Nexy	[0x9b5083c00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.149049-0500	Nexy	[0x9b5083c00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.161299-0500	Nexy	Did add XPC store
default	20:03:08.161360-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:03:08.161504-0500	Nexy	[0x9b5083e80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:03:08.162179-0500	Nexy	[0x9b5083e80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.162203-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:03:08.162220-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:03:08.167287-0500	Nexy	[0x9b50a2940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.168706-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1459, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.168742-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.170591-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1459, subject=com.nexy.assistant,
default	20:03:08.171408-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.196736-0500	Nexy	[0x9b50a2940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.196829-0500	Nexy	[0x9b50a2940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.196904-0500	Nexy	[0x9b50a2a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.197954-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1460, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.197990-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.199479-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1460, subject=com.nexy.assistant,
default	20:03:08.200253-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.222628-0500	Nexy	[0x9b50a2a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.222716-0500	Nexy	[0x9b50a2a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.222786-0500	Nexy	[0x9b50a2bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.223977-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1461, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.224018-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.225527-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1461, subject=com.nexy.assistant,
default	20:03:08.226335-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.252455-0500	Nexy	[0x9b50a2bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.252574-0500	Nexy	[0x9b50a2bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.252650-0500	Nexy	[0x9b50a2d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:03:08.253804-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1462, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.253842-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.255338-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1462, subject=com.nexy.assistant,
default	20:03:08.256205-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.280843-0500	Nexy	[0x9b50a2d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:03:08.280936-0500	Nexy	[0x9b50a2d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:03:08.282346-0500	Nexy	Did add XPC store
default	20:03:08.282373-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:03:08.304944-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1463, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.305006-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.307209-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1463, subject=com.nexy.assistant,
default	20:03:08.308208-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:08.338596-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1464, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:03:08.338639-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:08.340332-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1464, subject=com.nexy.assistant,
default	20:03:08.341198-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:03:10.585311-0500	Nexy	[0x9b50a30c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	20:03:13.144484-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	20:03:22.225100-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7122.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=7122, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:03:22.226583-0500	tccd	AUTHREQ_SUBJECT: msgID=7122.1, subject=com.nexy.assistant,
default	20:03:22.227385-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:22.241691-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.757, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=7122, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:03:22.242666-0500	tccd	AUTHREQ_SUBJECT: msgID=397.757, subject=com.nexy.assistant,
default	20:03:22.243421-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:22.274976-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:22.299380-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 65991: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 5d4c0300 };
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
default	20:03:22.318021-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:22.331656-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3ed00 at /Applications/Nexy.app
default	20:03:22.349021-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	20:03:23.944143-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3e100 at /Applications/Nexy.app
default	20:03:23.952670-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    487 = "<TCCDEventSubscriber: token=487, state=Passed, csid=com.apple.photolibraryd>";
    457 = "<TCCDEventSubscriber: token=457, state=Initial, csid=(null)>";
    484 = "<TCCDEventSubscriber: token=484, state=Passed, csid=com.apple.chronod>";
}
default	20:03:23.953141-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:03:35.220155-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7127.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=7127, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:03:35.221605-0500	tccd	AUTHREQ_SUBJECT: msgID=7127.1, subject=com.nexy.assistant,
default	20:03:35.222371-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:35.236535-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.760, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=7127, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:03:35.237345-0500	tccd	AUTHREQ_SUBJECT: msgID=397.760, subject=com.nexy.assistant,
default	20:03:35.237994-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:35.269678-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:35.294338-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 65991: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 6b4c0300 };
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
default	20:03:35.311846-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:38.325027-0500	Nexy	[0x9b50a3200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:03:38.326860-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:38.329891-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.8, subject=com.nexy.assistant,
default	20:03:38.331264-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:38.353910-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[7075], responsiblePID[7075], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:03:38.354458-0500	Nexy	[0x9b50a3200] invalidated after the last release of the connection object
default	20:03:38.395004-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:03:38.416280-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:38.421224-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:03:40.214610-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:03:40.230460-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:03:40.230501-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	20:03:40.230571-0500	Nexy	<private> 0x9b5016e80: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:03:40.714467-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:03:40.832900-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	20:03:41.430641-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:41.431236-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:41.438488-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:03:41.438529-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:03:45.814488-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:03:45.845824-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:45.857572-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:03:46.003285-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:03:46.003463-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:03:46.004818-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:03:46.005462-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:03:46.051791-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:46.051800-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:46.052186-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:03:46.052206-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:03:46.053452-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:03:46.053761-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:03:51.364860-0500	Nexy	server port 0x00010d13, session port 0x0000380f
default	20:03:51.366810-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.780, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:03:51.366852-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:03:51.368906-0500	tccd	AUTHREQ_SUBJECT: msgID=397.780, subject=com.nexy.assistant,
default	20:03:51.370084-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:54.409862-0500	Nexy	[0x9b50a3200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:03:54.411650-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:03:54.414381-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.9, subject=com.nexy.assistant,
default	20:03:54.415908-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:54.436167-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[7075], responsiblePID[7075], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:03:54.436638-0500	Nexy	[0x9b50a3200] invalidated after the last release of the connection object
default	20:03:54.474723-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:03:54.494793-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:03:54.499228-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:03:57.201324-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	20:03:57.784251-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:03:57.788599-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:03:57.789359-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:03:57.796380-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:03:57.796627-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:03:57.928730-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:57.928733-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:03:57.929649-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:03:57.929735-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	20:04:03.044528-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:04:03.063589-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:03.088083-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:04:03.131629-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:03.131819-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:04:03.132028-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:04:03.132623-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:03.133276-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:03.133481-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:04:03.133687-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:04:03.134216-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:03.167880-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:03.167891-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:03.168236-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:04:03.168251-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:04:03.169523-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:04:03.169605-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:04:07.519427-0500	Nexy	[0x9b50a3200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:04:07.520055-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:04:07.520242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7075.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:07.521774-0500	tccd	AUTHREQ_SUBJECT: msgID=7075.10, subject=com.nexy.assistant,
default	20:04:07.522456-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:07.540277-0500	Nexy	[0x9b50a3200] invalidated after the last release of the connection object
default	20:04:10.549710-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=59315.110, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=59315, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:04:10.564568-0500	tccd	AUTHREQ_SUBJECT: msgID=59315.110, subject=com.nexy.assistant,
default	20:04:10.565967-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:10.589942-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:04:10.680583-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:11.357259-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:04:11.716547-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	20:04:12.396508-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:12.398802-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:04:12.398896-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:12.543100-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:12.543600-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:12.549340-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:04:12.550381-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:04:17.726831-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158000 at /Applications/Nexy.app
default	20:04:17.762170-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:17.772211-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:04:17.919136-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:17.919368-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:04:17.919560-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:04:17.919986-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:04:17.920145-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:17.922106-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:17.922353-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:04:17.922806-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:04:17.923073-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:04:17.923197-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:04:17.956779-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:17.957357-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:04:17.957818-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:04:17.958168-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:04:17.958657-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:04:17.959202-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:04:23.727045-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=59315.112, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=59315, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:04:23.729835-0500	tccd	AUTHREQ_SUBJECT: msgID=59315.112, subject=com.nexy.assistant,
default	20:04:23.731550-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:27.789318-0500	Nexy	[0x9b50a3480] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:04:27.803616-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:04:27.807038-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3000000033 pid: 7075
default	20:04:27.816770-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x9b55ec640
 (
    "<NSDarkAquaAppearance: 0x9b55ec820>",
    "<NSSystemAppearance: 0x9b55ec6e0>"
)>
default	20:04:27.821849-0500	Nexy	[0x9b50a3980] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:04:27.823865-0500	Nexy	[0x9b50a3ac0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:04:27.826035-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:04:27.826328-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:04:27.826339-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:04:27.826368-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:04:27.826370-0500	Nexy	[0x9b50a3c00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:04:27.826427-0500	Nexy	[0x9b50a3e80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:27.826500-0500	Nexy	FBSWorkspace registering source: <private>
default	20:04:27.827053-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:04:27.827595-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:04:27.827747-0500	Nexy	<FBSWorkspaceScenesClient:0x9b5058640 <private>> attempting immediate handshake from activate
default	20:04:27.827795-0500	Nexy	<FBSWorkspaceScenesClient:0x9b5058640 <private>> sent handshake
default	20:04:27.827891-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:04:27.828284-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.828310-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.828382-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Registering event dispatcher at init
default	20:04:27.828452-0500	ControlCenter	Created <FBWorkspace: 0xcbd1af5c0; <FBApplicationProcess: 0xcc0135980; app<application.com.nexy.assistant.53705040.53705049>:7075(v34BD4)>>
default	20:04:27.828465-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.53705040.53705049> with intent background
default	20:04:27.828505-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:04:27.828715-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53705040.53705049(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:04:27.828821-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53705040.53705049(501)> from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-672-16457 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:04:27.828969-0500	runningboardd	Assertion 403-672-16457 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) will be created as active
default	20:04:27.829000-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-672-16457 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.829322-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:27.829332-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:27.829341-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:27.829586-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:27.830154-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:04:27.831792-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:04:27.832695-0500	Nexy	Requesting scene <FBSScene: 0x9b505aee0; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089> from com.apple.controlcenter.statusitems
default	20:04:27.835469-0500	Nexy	Request for <FBSScene: 0x9b505aee0; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089> complete!
default	20:04:27.835602-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:04:27.837466-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:04:27.837608-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:27.837969-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:04:27.838342-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:04:27.838385-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:04:27.838649-0500	Nexy	Requesting scene <FBSScene: 0x9b505af80; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:04:27.838917-0500	Nexy	Request for <FBSScene: 0x9b505af80; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView> complete!
default	20:04:27.840795-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:27.840812-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:04:27.841502-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Bootstrap success!
default	20:04:27.842056-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Setting process visibility to: Background
default	20:04:27.842138-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:04:27.842411-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:403-672-16458 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:04:27.842474-0500	runningboardd	Assertion 403-672-16458 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.842818-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:27.842859-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:27.842869-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:27.842916-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:27.845419-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:27.845436-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:04:27.845607-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:04:27.847232-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:27.847652-0500	ControlCenter	Adding: <FBApplicationProcess: 0xcc0135980; app<application.com.nexy.assistant.53705040.53705049>:7075(v34BD4)>
default	20:04:27.848232-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Connection established.
default	20:04:27.848318-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xcbeb45960>
default	20:04:27.848346-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Connection to remote process established!
default	20:04:27.848584-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.849514-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.854916-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.855353-0500	Nexy	Request for <FBSScene: 0x9b505aee0; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089> complete!
default	20:04:27.854931-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xcc0135980; app<application.com.nexy.assistant.53705040.53705049>:7075(v34BD4)>
default	20:04:27.855058-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Registered new scene: <FBWorkspaceScene: 0xcbf633e40; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089> (fromRemnant = 0)
default	20:04:27.855743-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:403-672-16459 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:04:27.855830-0500	runningboardd	Assertion 403-672-16459 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as inactive as originator process has not exited
default	20:04:27.855113-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Workspace interruption policy did change: reconnect
default	20:04:27.855330-0500	ControlCenter	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089] Client process connected: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.856379-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-672-16460 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:04:27.856482-0500	runningboardd	Assertion 403-672-16460 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.856604-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:04:27.856638-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.856652-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xcc0135980; app<application.com.nexy.assistant.53705040.53705049>:7075(v34BD4)>
default	20:04:27.856729-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Registered new scene: <FBWorkspaceScene: 0xcbf633a80; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:04:27.856858-0500	ControlCenter	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.857469-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:27.857481-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:27.857489-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:27.857505-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:27.856885-0500	Nexy	Request for <FBSScene: 0x9b505af80; com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView> complete!
default	20:04:27.857254-0500	Nexy	<FBSWorkspaceScenesClient:0x9b5058640 <private>> Reconnecting scene com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089
default	20:04:27.857599-0500	Nexy	<FBSWorkspaceScenesClient:0x9b5058640 <private>> Reconnecting scene com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView
default	20:04:27.861315-0500	Nexy	Registering for test daemon availability notify post.
default	20:04:27.861453-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:27.861567-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:27.861682-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:27.865159-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:27.858239-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.865603-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.863817-0500	Nexy	[0x9b56f7d40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:04:27.877798-0500	Nexy	[0x9b56f43c0] Connection returned listener port: 0x4e03
default	20:04:27.878473-0500	Nexy	SignalReady: pid=7075 asn=0x0-0x11d11d
default	20:04:27.879219-0500	Nexy	SIGNAL: pid=7075 asn=0x0x-0x11d11d
default	20:04:27.879874-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.881808-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:04:27.885725-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:27.891817-0500	Nexy	0x9b5017000: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	20:04:27.891834-0500	Nexy	0x9b4c12d60: Updating using cached account information
default	20:04:27.898309-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:27.901757-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:27.903810-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:04:27.903815-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:04:27.903856-0500	Nexy	[0x9b56f5400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:04:27.903961-0500	Nexy	[0x9b56f5400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:27.905144-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:04:27.909523-0500	Nexy	[C:2] Alloc <private>
default	20:04:27.909558-0500	Nexy	[0x9b56f5400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:27.911220-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-7075). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:04:27.911588-0500	WindowManager	Connection activated | (7075) Nexy
default	20:04:27.912161-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16461 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.912228-0500	runningboardd	Assertion 403-7075-16461 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.912394-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-7075)
default	20:04:27.912528-0500	runningboardd	Invalidating assertion 403-7075-16461 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.912553-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:27.912590-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:27.912628-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:27.912707-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16462 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.912713-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:27.912796-0500	runningboardd	Assertion 403-7075-16462 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.912869-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(9F5AB745, (bid:com.nexy.assistant-Item-0-7075)) for (bid:com.nexy.assistant-Item-0-7075)
default	20:04:27.913404-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-7075)]
default	20:04:27.914087-0500	ControlCenter	Created instance DisplayableId(EF6BC690) in .menuBar for DisplayableAppStatusItemType(9F5AB745, (bid:com.nexy.assistant-Item-0-7075)) .menuBar
default	20:04:27.917121-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.917701-0500	runningboardd	Invalidating assertion 403-7075-16463 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.917881-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16464 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.917944-0500	runningboardd	Assertion 403-7075-16464 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.918435-0500	runningboardd	Invalidating assertion 403-7075-16464 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.918641-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16465 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.918694-0500	runningboardd	Assertion 403-7075-16465 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.918714-0500	ControlCenter	Created ephemaral instance DisplayableId(EF6BC690) for (bid:com.nexy.assistant-Item-0-7075) with positioning .ephemeral
default	20:04:27.918931-0500	runningboardd	Invalidating assertion 403-7075-16465 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.919047-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16466 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.919096-0500	runningboardd	Assertion 403-7075-16466 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:27.919142-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:27.919336-0500	runningboardd	Invalidating assertion 403-7075-16466 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:27.919449-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7075-16467 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:27.923960-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1853, subject=com.nexy.assistant,
default	20:04:27.924989-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c300 at /Applications/Nexy.app
default	20:04:27.925370-0500	Nexy	[0x9b56f7c00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:27.926536-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1854, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:27.926564-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:27.927928-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1854, subject=com.nexy.assistant,
default	20:04:27.928904-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:27.938874-0500	Nexy	[com.apple.controlcenter:8029CF17-B7C9-4B88-B579-6E8A94B43089] Sending action(s) in update: NSSceneFenceAction
default	20:04:27.949527-0500	Nexy	[0x9b56f7c00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:27.949570-0500	Nexy	[0x9b56f75c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:27.949637-0500	Nexy	[0x9b56f7c00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:27.950371-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1855, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:27.950403-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:27.950685-0500	Nexy	Defaultable: persistentAccounts: <private>
default	20:04:27.950714-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x9b505a9e0: identifier=_acceptedIntroductions, name=Other Known, baseURL=(nil), dsid=(nil)> because it can't become default
default	20:04:27.950730-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x9b505a940: identifier=_directoryServices, name=Directory Services, baseURL=(nil), dsid=(nil)> because it can't become default
default	20:04:27.951452-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1855, subject=com.nexy.assistant,
default	20:04:27.951841-0500	Nexy	-awakeFromLoad
default	20:04:27.951951-0500	Nexy	-setServername: <private>  Parsed into scheme: https  host: <private>  port: 0  path: <private>
default	20:04:27.952020-0500	Nexy	-initWithUID:persistence: called on thread: <private>
default	20:04:27.952042-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:27.952215-0500	Nexy	-clearPrincipalProperties
default	20:04:27.952238-0500	Nexy	-clearHomeContainers
default	20:04:27.952753-0500	Nexy	Defaultable: Final list: <private>
default	20:04:27.952769-0500	Nexy	New account should become the default account
default	20:04:27.953006-0500	Nexy	0x9b5017000: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	20:04:27.953048-0500	Nexy	0x9b4c12d60: Updating using cached account information
default	20:04:27.968364-0500	Nexy	[0x9b56f7c00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:27.968401-0500	Nexy	[0x9b6c38000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:27.968441-0500	Nexy	[0x9b6c38140] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:27.969077-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1856, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:27.969110-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:27.970073-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1856, subject=com.nexy.assistant,
default	20:04:27.970622-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:27.986778-0500	Nexy	[0x9b6c38140] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:27.986901-0500	Nexy	[0x9b6c38140] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:27.986979-0500	Nexy	[0x9b6c38280] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:27.987766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1857, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:27.987795-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:27.988768-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1857, subject=com.nexy.assistant,
default	20:04:27.989341-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:28.005317-0500	Nexy	[0x9b6c38280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.005364-0500	Nexy	[0x9b6c383c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:28.006582-0500	Nexy	Did add XPC store
default	20:04:28.006597-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:04:28.006644-0500	Nexy	[0x9b6c388c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:04:28.007062-0500	Nexy	[0x9b6c388c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.007081-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:04:28.007112-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:04:28.009186-0500	Nexy	[0x9b6c3b340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:28.009809-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1858, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:28.009836-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:28.010823-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1858, subject=com.nexy.assistant,
default	20:04:28.011396-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:28.018403-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:28.018416-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:28.018429-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:28.018449-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:28.021740-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:28.022142-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.022253-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.027172-0500	Nexy	[0x9b6c3b340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.027218-0500	Nexy	[0x9b6c3b480] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:28.027265-0500	Nexy	[0x9b6c3b340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:28.027967-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1859, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:28.027998-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:28.029072-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1859, subject=com.nexy.assistant,
default	20:04:28.029681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:28.044967-0500	Nexy	[0x9b6c3b340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.045027-0500	Nexy	[0x9b6c3b5c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:28.045087-0500	Nexy	[0x9b6c3b340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:28.045808-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1860, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:28.045845-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:28.046808-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1860, subject=com.nexy.assistant,
default	20:04:28.047363-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:28.063488-0500	Nexy	[0x9b6c3b340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.063556-0500	Nexy	[0x9b6c3b340] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:28.063608-0500	Nexy	[0x9b6c3b700] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:04:28.064558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75929.1861, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:04:28.064589-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=75929, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7075, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:28.065723-0500	tccd	AUTHREQ_SUBJECT: msgID=75929.1861, subject=com.nexy.assistant,
default	20:04:28.066368-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f000 at /Applications/Nexy.app
default	20:04:28.075540-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:04:28.078252-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:04:28.079066-0500	Nexy	[GMS] availability notification token 120
default	20:04:28.082926-0500	Nexy	[0x9b6c3b700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:28.082972-0500	Nexy	[0x9b6c3b840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:28.083813-0500	Nexy	Did add XPC store
default	20:04:28.083831-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:04:28.091233-0500	Nexy	Client change history token is invalid: <private>, current token: <private>, error: Error Domain=NSCocoaErrorDomain Code=134501 UserInfo={NSLocalizedFailureReason=<private>}
error	20:04:28.091454-0500	Nexy	Failed to fetch change history: Error Domain=CNErrorDomain Code=1006 "Full Sync Required" UserInfo={NSLocalizedFailureReason=A full sync is required., NSLocalizedDescription=Full Sync Required, NSUnderlyingError=0x9b1dfcf30 {Error Domain=CNErrorDomain Code=604 "Invalid Change History Anchor" UserInfo={NSLocalizedDescription=Invalid Change History Anchor, NSLocalizedFailureReason=The change history anchor is invalid.}}}
default	20:04:28.091702-0500	Nexy	0000 BEGIN: Will execute fetch for request: <private>
default	20:04:28.091712-0500	Nexy	0000 Entry point: executeFetchRequest:error:
default	20:04:28.091718-0500	Nexy	0000 Predicate: (null) <private>
default	20:04:28.101078-0500	Nexy	App is linked against Fall 2022 SDK or later
default	20:04:28.101094-0500	Nexy	Note access is not granted, so Notes are inaccessible
fault	20:04:28.101202-0500	Nexy	Attempt to read notes by an unentitled app
default	20:04:28.109301-0500	Nexy	0000 History anchor returned to client: <CNChangeHistoryAnchor: 0x9b6c42ca0: version=2, token=<NSPersistentHistoryToken - {
    "121C6BBC-8A11-4E34-B252-321D0995C010" = 6;
    "CE445509-54F5-473C-9A96-89025D6F9355" = 4742;
}>>
default	20:04:28.109380-0500	Nexy	0000 Contact: 3EE990C2-437C-497A-B4CF-4787E78B5D0C:ABPerson
default	20:04:28.109390-0500	Nexy	0000 Contact: 2645688D-4F81-4C23-847F-96DEA47CCE6D:ABPerson
default	20:04:28.109395-0500	Nexy	0000 Contact: C822EB31-1F0F-41F6-9120-A322A5874983:ABPerson
default	20:04:28.109400-0500	Nexy	0000 Contact: 50AD2AD1-9340-4D1D-8702-DB033FCB2397:ABPerson
default	20:04:28.109405-0500	Nexy	0000 Contact: EDB979D3-287A-47DC-BC6D-006167336515:ABPerson
default	20:04:28.109410-0500	Nexy	0000 Contact: 9595A838-850C-49DB-8998-80F19667F619:ABPerson
default	20:04:28.109414-0500	Nexy	0000 Contact: 9891AB4D-DDC3-49D3-8FAA-45BFB1995A79:ABPerson
default	20:04:28.109420-0500	Nexy	0000 Contact: 34B7C886-745F-477F-BAF4-C6494310C1C1:ABPerson
default	20:04:28.109425-0500	Nexy	0000 Contact: 3426C1A4-CACA-42EF-8793-7312DCEE5E69:ABPerson
default	20:04:28.109433-0500	Nexy	0000 Contact: AFFBAE3D-BA02-4D6F-AE25-87E55C2E4CD9:ABPerson
default	20:04:28.109441-0500	Nexy	0000 Contact: 55C7A0C2-9163-43BC-95A9-A92E4F5427BD:ABPerson
default	20:04:28.109491-0500	Nexy	0000 Contact: CBAABC59-9B06-47EE-9311-0823CE3EE179:ABPerson
default	20:04:28.109497-0500	Nexy	0000 Contact: FF2BD9DD-8A6D-4E97-BB7D-7B1A5C4FAC0F:ABPerson
default	20:04:28.109502-0500	Nexy	0000 Contact: F6E944AE-3E32-4C0C-BA60-EE94D9402DA7:ABPerson
default	20:04:28.109507-0500	Nexy	0000 Contact: 0E222C4B-C87D-403F-A824-B8B8EAABF29D:ABPerson
default	20:04:28.109512-0500	Nexy	0000 Contact: 160B58EE-E9AF-4BBE-B484-7D4E18CA0CD4:ABPerson
default	20:04:28.109517-0500	Nexy	0000 Contact: D6931A27-6BBA-4ABF-AB86-AA94288C8731:ABPerson
default	20:04:28.109523-0500	Nexy	0000 Contact: 04E7F59A-3D30-4CF9-8395-AE8737EE1154:ABPerson
default	20:04:28.109529-0500	Nexy	0000 Contact: 863252FB-26EB-421B-9B96-91673ED81D35:ABPerson
default	20:04:28.109534-0500	Nexy	0000 Contact: 742C7DAC-D2A9-4D1C-A93D-DC71F37722B9:ABPerson
default	20:04:28.109539-0500	Nexy	0000 Contact: 99649BEC-0C02-4588-9CCA-09103FDC430C:ABPerson
default	20:04:28.109544-0500	Nexy	0000 Contact: 8898FA76-8C7B-4917-B353-30B4A337A32B:ABPerson
default	20:04:28.109549-0500	Nexy	0000 Contact: 75C5C7DD-DD9E-437F-91B9-34AFD56C5A14:ABPerson
default	20:04:28.109555-0500	Nexy	0000 Contact: DDC41FDC-94BF-4147-9863-5AFCC485C4BA:ABPerson
default	20:04:28.109561-0500	Nexy	0000 Contact: B6D0B979-BBDF-4FF5-93A8-0974C5AE45C7:ABPerson
default	20:04:28.109572-0500	Nexy	0000 Contact: B7A8ADD0-A952-45B0-B7A2-D15A3D34A898:ABPerson
default	20:04:28.109577-0500	Nexy	0000 Contact: 35894E4A-BF98-44E4-85B9-33C2A0A01944:ABPerson
default	20:04:28.109596-0500	Nexy	0000 Contact: 67B532BB-C394-4D14-B2E6-C1B93DE930E4:ABPerson
default	20:04:28.109603-0500	Nexy	0000 Contact: A71518ED-EC1D-4740-9D8C-2C5F81C71467:ABPerson
default	20:04:28.109610-0500	Nexy	0000 Contact: EE1E04AC-AF03-428A-97EF-6E8851A86066:ABPerson
default	20:04:28.109615-0500	Nexy	0000 Contact: 54E381BF-247A-4AB7-81FD-8C78CBB93296:ABPerson
default	20:04:28.109620-0500	Nexy	0000 Contact: A5DB19AB-C77E-44EC-87A4-8459DA494E7B:ABPerson
default	20:04:28.109626-0500	Nexy	0000 Contact: FC26680D-B85F-4E40-812F-4F169185AE50:ABPerson
default	20:04:28.109636-0500	Nexy	0000 Contact: E36EA0A4-41F7-4C3F-AAF9-A93099626D77:ABPerson
default	20:04:28.109641-0500	Nexy	0000 Contact: 37E2B276-263E-40A5-BF81-1628796DB605:ABPerson
default	20:04:28.109652-0500	Nexy	0000 Contact: D989E37A-D5DC-4A68-8D47-AD8FEE0B37BA:ABPerson
default	20:04:28.109658-0500	Nexy	0000 Contact: 204F2E81-2324-4937-9859-E8732482C902:ABPerson
default	20:04:28.109663-0500	Nexy	0000 Contact: C4831F25-FE6F-4217-92D2-C4D6C01013BC:ABPerson
default	20:04:28.109694-0500	Nexy	0000 Contact: 4FD77C47-1199-46DF-B186-25C3BB8E54C4:ABPerson
default	20:04:28.109702-0500	Nexy	0000 Contact: 16FA5BBF-AADB-4362-83EB-09668C0C6A84:ABPerson
default	20:04:28.109707-0500	Nexy	0000 Contact: D9A061DB-8A77-472E-A6B3-AF6A4A6727A9:ABPerson
default	20:04:28.109711-0500	Nexy	0000 Contact: 62AC02AD-E5FE-4F18-8DEB-151D2FFD50D2:ABPerson
default	20:04:28.109715-0500	Nexy	0000 Contact: 9D4856E4-4610-4169-9460-115522478752:ABPerson
default	20:04:28.109721-0500	Nexy	0000 Contact: 8038DF9A-4503-4464-BA80-1A8B28F523E6:ABPerson
default	20:04:28.109729-0500	Nexy	0000 Contact: DE31B769-37E8-406B-BC5C-FC44F37A37D1:ABPerson
default	20:04:28.109734-0500	Nexy	0000 Contact: B2E8FADF-3954-4D05-B047-C43474BF8E54:ABPerson
default	20:04:28.109740-0500	Nexy	0000 Contact: 5C30DD83-8C53-4FB6-943A-DF0CED6109D6:ABPerson
default	20:04:28.109745-0500	Nexy	0000 Contact: 16A1EC92-AB39-4C1E-8E16-706B5F47397C:ABPerson
default	20:04:28.109755-0500	Nexy	0000 Contact: 36994EED-FC81-46EF-86F8-8B3217234A98:ABPerson
default	20:04:28.109762-0500	Nexy	0000 Contact: D0D31CD7-6F0F-4030-A30D-197CE5187EED:ABPerson
default	20:04:28.109767-0500	Nexy	0000 Contact: F5676762-711F-4325-8A7A-FCB211127327:ABPerson
default	20:04:28.109771-0500	Nexy	0000 Contact: 99378C4C-7187-4A49-A938-AF1E4D9750E9:ABPerson
default	20:04:28.109777-0500	Nexy	0000 Contact: FE93F61D-6DD6-4CF7-9D17-F972815C60EB:ABPerson
default	20:04:28.109788-0500	Nexy	0000 Contact: E7CCA41A-8A2E-4351-852A-A5CFB6BD2AF5:ABPerson
default	20:04:28.109793-0500	Nexy	0000 Contact: EC41AC6A-1CB5-41D5-B70A-D7D261B5F6B3:ABPerson
default	20:04:28.109800-0500	Nexy	0000 Contact: 2A13AE99-82FE-4A26-A768-1B8C4A11C6C3:ABPerson
default	20:04:28.109816-0500	Nexy	0000 Contact: D5B5277E-F18A-48C2-B93C-E578CEB16C34:ABPerson
default	20:04:28.109822-0500	Nexy	0000 Contact: 1148E024-6D8F-4279-921E-7936B62EB2B8:ABPerson
default	20:04:28.109827-0500	Nexy	0000 Contact: FAF205FC-E995-4261-90F7-336A4D237F48:ABPerson
default	20:04:28.109832-0500	Nexy	0000 Contact: 88E161CA-F779-4608-BE32-D15726C295C6:ABPerson
default	20:04:28.109837-0500	Nexy	0000 Contact: BE244260-8495-47EA-9EFA-A4A129388623:ABPerson
default	20:04:28.109862-0500	Nexy	0000 Contact: FC34E363-0467-4B9C-95B0-F8C585C41741:ABPerson
default	20:04:28.109867-0500	Nexy	0000 Contact: F244F65D-0A57-4A3C-B8B8-9E1C389A5E77:ABPerson
default	20:04:28.109872-0500	Nexy	0000 Contact: 9DE56935-FB3E-470E-9878-89DB593E2DFE:ABPerson
default	20:04:28.109878-0500	Nexy	0000 Contact: 51D61586-1A8A-4EC4-8568-45B5296B1751:ABPerson
default	20:04:28.109882-0500	Nexy	0000 Contact: F34A454E-F1D3-4849-9368-950A6FFA8DD1:ABPerson
default	20:04:28.109886-0500	Nexy	0000 Contact: 5E09571D-9D8E-4D12-8480-F04FD91A55C4:ABPerson
default	20:04:28.109899-0500	Nexy	0000 Contact: 997D7D2F-4504-4C65-A31D-535219B806F5:ABPerson
default	20:04:28.109905-0500	Nexy	0000 Contact: F4D5E6E8-6B00-4329-94DC-82661F45DDB5:ABPerson
default	20:04:28.109920-0500	Nexy	0000 Contact: B3F91E16-48C2-4383-BFDA-F39E45D698A9:ABPerson
default	20:04:28.109926-0500	Nexy	0000 Contact: 972B1CC5-A00E-409A-A1C8-1035B67228F2:ABPerson
default	20:04:28.109931-0500	Nexy	0000 Contact: C9342200-2A80-485B-8777-A59F252176D4:ABPerson
default	20:04:28.109936-0500	Nexy	0000 Contact: FCD5548B-6E7B-4B57-9097-496095F0C27B:ABPerson
default	20:04:28.109951-0500	Nexy	0000 Contact: 32E90B79-BC48-4AFC-A5CE-495011FBE68F:ABPerson
default	20:04:28.109956-0500	Nexy	0000 Contact: 799B442D-0C1B-41A7-982A-5A795CF5AC7E:ABPerson
default	20:04:28.109961-0500	Nexy	0000 Contact: 4BC8FD3A-601A-4905-B4F0-AAEE2EA51FFC:ABPerson
default	20:04:28.109966-0500	Nexy	0000 Contact: EB01D8DC-AD35-4332-B52D-021C69F834F5:ABPerson
default	20:04:28.109972-0500	Nexy	0000 Contact: 34439B56-399C-41AE-8A94-926BE1F059E3:ABPerson
default	20:04:28.109999-0500	Nexy	0000 Contact: 5B2AA695-5EAB-4F85-9EA7-0F11FEE7BF7E:ABPerson
default	20:04:28.110004-0500	Nexy	0000 Contact: 680613B6-43E0-4C77-8B2B-0F21D4D6F558:ABPerson
default	20:04:28.110011-0500	Nexy	0000 Contact: FEFADE95-1917-4F12-AF5F-E9AF0F50E039:ABPerson
default	20:04:28.110014-0500	Nexy	0000 Contact: 1CED5FB1-D054-43C6-BF35-E035DFF16C75:ABPerson
default	20:04:28.110019-0500	Nexy	0000 Contact: 4D6A09F3-71D7-4E04-83FD-9BB5EF7442CF:ABPerson
default	20:04:28.110023-0500	Nexy	0000 Contact: 03F9DBA8-764B-4F5E-AFB8-4FE555600768:ABPerson
default	20:04:28.110028-0500	Nexy	0000 Contact: 33E6AEE6-78CC-42D7-80DA-478EDE698964:ABPerson
default	20:04:28.110033-0500	Nexy	0000 Contact: 2B720652-555E-462B-8C74-277B5F6F5F59:ABPerson
default	20:04:28.110069-0500	Nexy	0000 Contact: D8AB7561-7ABC-404E-A1AD-D9765D7DD983:ABPerson
default	20:04:28.110080-0500	Nexy	0000 Contact: 8256DD81-94E0-404F-BE4E-E6831011073C:ABPerson
default	20:04:28.110088-0500	Nexy	0000 Contact: 260C090E-52D7-4D15-AE22-6804C72C9DBF:ABPerson
default	20:04:28.110093-0500	Nexy	0000 Contact: F5703214-DEA8-429F-ADBF-5465A9AFE1BC:ABPerson
default	20:04:28.110096-0500	Nexy	0000 Contact: 1FBE32BC-B2F2-4B98-8BA8-04A4E25A4F0E:ABPerson
default	20:04:28.110101-0500	Nexy	0000 Contact: 2285EC2D-05CF-42C3-8C59-C4930AD792E3:ABPerson
default	20:04:28.110105-0500	Nexy	0000 Contact: 96E50230-0A5E-4B64-A2E9-A2F57018F4EA:ABPerson
default	20:04:28.110110-0500	Nexy	0000 Contact: 1D80A41C-48FF-40D8-A1F7-EB1FCAF019EC:ABPerson
default	20:04:28.110116-0500	Nexy	0000 Contact: 3C49D81F-04DC-4318-93D4-B25373EDFE30:ABPerson
default	20:04:28.110121-0500	Nexy	0000 Contact: 5B4B2182-FBEA-48F0-B9C7-742552BF6CF6:ABPerson
default	20:04:28.110126-0500	Nexy	0000 Contact: 697396C6-6DF5-4A8D-BBC1-7CFB8C26B531:ABPerson
default	20:04:28.110130-0500	Nexy	0000 Contact: BC83C14B-9BF3-4E6D-A5BD-1252B3AF3A72:ABPerson
default	20:04:28.110135-0500	Nexy	0000 Contact: 29B138C5-7412-4C36-A514-72D80434AC26:ABPerson
default	20:04:28.110151-0500	Nexy	0000 Contact: 93438337-7E2C-4A3D-99F8-28AECEE7A491:ABPerson
default	20:04:28.110157-0500	Nexy	0000 Contact: BEEDDC1A-71AD-4FBD-9241-9F6B4669022C:ABPerson
default	20:04:28.110161-0500	Nexy	0000 Contact: 516FCDD2-D694-4336-9C5C-B3F9398876E3:ABPerson
default	20:04:28.110166-0500	Nexy	0000 Contact: CB798F66-5E15-419F-8CB1-A22A10034846:ABPerson
default	20:04:28.110171-0500	Nexy	0000 Contact: 9BE2908B-57F8-42EB-85AB-E556B53D5008:ABPerson
default	20:04:28.110187-0500	Nexy	0000 Contact: 74E5D1E4-D560-47F5-800D-2B15C8F128ED:ABPerson
default	20:04:28.110193-0500	Nexy	0000 Contact: 73FA4D96-88CD-4E81-B755-D3C151251CB2:ABPerson
default	20:04:28.110198-0500	Nexy	0000 Contact: A159EB30-CDD4-4876-B3EB-7A251E5003A1:ABPerson
default	20:04:28.110203-0500	Nexy	0000 Contact: 2E020885-F8C2-47BB-AEE3-DD7CF66B13B4:ABPerson
default	20:04:28.110229-0500	Nexy	0000 Contact: 05A17C92-D301-4B09-A90C-D64806C4CA53:ABPerson
default	20:04:28.110234-0500	Nexy	0000 Contact: AD733A8E-1D66-4608-811D-8B3CC382D864:ABPerson
default	20:04:28.110239-0500	Nexy	0000 Contact: E567A65A-A157-4ABD-B1FD-82CC549DEDED:ABPerson
default	20:04:28.110244-0500	Nexy	0000 Contact: 7F0336C8-01E0-47A7-A79A-9400EBF86D9C:ABPerson
default	20:04:28.110248-0500	Nexy	0000 Contact: 46F95F55-6525-42E6-A4B3-332AB9ECB6C9:ABPerson
default	20:04:28.110253-0500	Nexy	0000 Contact: 0BF7B2D3-D0E4-4CF5-A2E5-BBAB2F74860F:ABPerson
default	20:04:28.110256-0500	Nexy	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	20:04:28.110263-0500	Nexy	0000 Contact: DF05522B-2972-4CAB-8C0F-9FDECE2E3D80:ABPerson
default	20:04:28.110275-0500	Nexy	0000 Contact: 32C28665-F08E-4EE8-AFEB-487908D24319:ABPerson
default	20:04:28.110280-0500	Nexy	0000 Contact: 23512481-0DEF-42CA-8985-3D92A24DC0D9:ABPerson
default	20:04:28.110296-0500	Nexy	0000 Contact: C799BC2E-8783-42B8-BE80-6B9329212F7F:ABPerson
default	20:04:28.110302-0500	Nexy	0000 Contact: AF84B174-40F6-4E9C-A51A-D3FACA6CD75E:ABPerson
default	20:04:28.110307-0500	Nexy	0000 Contact: D41F250E-DF7F-4F9C-9D25-DC402CAC6533:ABPerson
default	20:04:28.110312-0500	Nexy	0000 Contact: E5E58063-920E-46E6-8939-C1A7ACCF23F0:ABPerson
default	20:04:28.110322-0500	Nexy	0000 Contact: F48B9D39-03E0-45D0-AA05-14488FC68C6F:ABPerson
default	20:04:28.110327-0500	Nexy	0000 Contact: B599DEB9-C4DF-472F-9B9E-67C3935077CD:ABPerson
default	20:04:28.110353-0500	Nexy	0000 Contact: CD1D19AA-FC19-4C03-9DC9-C147E8C245D1:ABPerson
default	20:04:28.110359-0500	Nexy	0000 Contact: 4F833F31-870E-4630-825C-0F532CBA3D39:ABPerson
default	20:04:28.110368-0500	Nexy	0000 Contact: BD409DD5-797E-41A8-B955-2CC4520A8769:ABPerson
default	20:04:28.110374-0500	Nexy	0000 Contact: 8A88B309-DB9A-4B6A-B1D9-CD6910D5845B:ABPerson
default	20:04:28.110382-0500	Nexy	0000 Contact: 18BDFAAD-5A5F-42D6-890A-2C5AEA9201D4:ABPerson
default	20:04:28.110387-0500	Nexy	0000 Contact: 96309E07-28A0-4C3F-8B27-7224031FF6EB:ABPerson
default	20:04:28.110392-0500	Nexy	0000 Contact: BF324B31-1F91-4723-87BC-8FE02890D85F:ABPerson
default	20:04:28.110397-0500	Nexy	0000 Contact: A0DA1AD3-5F0A-4625-8A45-AEE2662B5DF7:ABPerson
default	20:04:28.110402-0500	Nexy	0000 Contact: 76DEED21-9E22-4327-83F8-C1C1DDF67DEE:ABPerson
default	20:04:28.110407-0500	Nexy	0000 Contact: 7C25BC81-A7AB-4059-A199-45F36EBE02EB:ABPerson
default	20:04:28.110411-0500	Nexy	0000 Contact: 919E5AE9-2160-41DC-8E41-9C2536932C86:ABPerson
default	20:04:28.110421-0500	Nexy	0000 Contact: 8FC46F73-8C76-4F4F-A480-86AD43FB3197:ABPerson
default	20:04:28.110428-0500	Nexy	0000 Contact: 758B39F6-7626-4392-A342-2F56B6D94427:ABPerson
default	20:04:28.110436-0500	Nexy	0000 Contact: 8A6084C7-9664-4FCF-BD0E-DF7B4AE169BC:ABPerson
default	20:04:28.110443-0500	Nexy	0000 Contact: 51857A1F-41AD-4ABC-BC2E-82377C39162B:ABPerson
default	20:04:28.110460-0500	Nexy	0000 Contact: 0145E52B-5388-4DF4-9BA6-041E2688EA53:ABPerson
default	20:04:28.110466-0500	Nexy	0000 Contact: 7C58562E-BF30-4BE5-AC33-E0A88F42AB76:ABPerson
default	20:04:28.110471-0500	Nexy	0000 Contact: C7C8564C-DF73-4360-B286-BB2CF4C72F17:ABPerson
default	20:04:28.110476-0500	Nexy	0000 Contact: F9EE7585-B534-46B5-848E-58FFD7152121:ABPerson
default	20:04:28.110481-0500	Nexy	0000 Contact: DABCF335-B625-47DD-918B-704381FD587D:ABPerson
default	20:04:28.110496-0500	Nexy	0000 Contact: A68807CD-0A21-4F90-BE39-09BAF83835E8:ABPerson
default	20:04:28.110502-0500	Nexy	0000 Contact: 3B7F983F-D8F3-400C-8462-CA84B84968A4:ABPerson
default	20:04:28.110507-0500	Nexy	0000 Contact: BE53EA52-E9F8-4C18-8446-4FA2489ADE02:ABPerson
default	20:04:28.110516-0500	Nexy	0000 Contact: A804F4AE-3921-4E55-83D8-094B7C4F17A3:ABPerson
default	20:04:28.110521-0500	Nexy	0000 Contact: 489A6364-6AEC-4FC5-8F52-FC08E5527BA0:ABPerson
default	20:04:28.110529-0500	Nexy	0000 Contact: B43BC68C-E9BB-48C1-98C3-A32A09C9A802:ABPerson
default	20:04:28.110536-0500	Nexy	0000 Contact: 05518C4D-4F67-4CD6-83D7-85AA7F2525A5:ABPerson
default	20:04:28.110546-0500	Nexy	0000 Contact: 955CE160-9CC8-4013-829C-A68FD99C7595:ABPerson
default	20:04:28.110552-0500	Nexy	0000 Contact: C13FF96F-DEF6-4C53-83DE-4B45963DD9AF:ABPerson
default	20:04:28.110569-0500	Nexy	0000 Contact: AE65B570-135A-4B14-BA64-EC538224DA56:ABPerson
default	20:04:28.110574-0500	Nexy	0000 Contact: C2132A98-A61A-4358-A681-AF1A1DA20915:ABPerson
default	20:04:28.110579-0500	Nexy	0000 Contact: C3CC1CBC-2410-4DA6-A83E-0477D239E755:ABPerson
default	20:04:28.110584-0500	Nexy	0000 Contact: 0FB60F1D-91EC-4396-A66A-69F15AF14BC5:ABPerson
default	20:04:28.110590-0500	Nexy	0000 Contact: FC6CD704-B936-454E-9EBD-E1701A5DE7D8:ABPerson
default	20:04:28.110611-0500	Nexy	0000 Contact: ED88C6F4-1641-473F-A5BC-DA8C11FCE9D2:ABPerson
default	20:04:28.110616-0500	Nexy	0000 Contact: 88083F13-CF73-4821-896D-8C9EDB5E9029:ABPerson
default	20:04:28.110624-0500	Nexy	0000 Contact: C5BAA4A8-B489-4A59-9400-5C0DFDAA91CA:ABPerson
default	20:04:28.110630-0500	Nexy	0000 Contact: F0187322-8BFE-4EE7-BA9E-BF7D7A056616:ABPerson
default	20:04:28.110636-0500	Nexy	0000 Contact: BA26FE3B-CB6A-471A-8E10-5000CF5332C2:ABPerson
default	20:04:28.110641-0500	Nexy	0000 Contact: DB250DFB-C87D-447B-B125-220B6E3DA663:ABPerson
default	20:04:28.110646-0500	Nexy	0000 Contact: B436BB91-BBBB-49E7-9C6A-93DDDD421478:ABPerson
default	20:04:28.110654-0500	Nexy	0000 Contact: DFCC4D11-6BC3-4ACD-B8C6-F8C46F7C8369:ABPerson
default	20:04:28.110660-0500	Nexy	0000 Contact: 0B435818-E34A-41BF-8808-417BCB956E97:ABPerson
default	20:04:28.110665-0500	Nexy	0000 Contact: E336CBFC-CF06-4672-BEF7-926884FB9BC8:ABPerson
default	20:04:28.110675-0500	Nexy	0000 Contact: A04F02F1-D5E5-4B3E-B5D0-287A46E6DB37:ABPerson
default	20:04:28.110692-0500	Nexy	0000 Contact: 274D78AE-37CF-4B30-B57D-D218F7D433BC:ABPerson
default	20:04:28.110699-0500	Nexy	0000 Contact: AFC75DDF-9D56-451F-8FFA-33CEF512BC9E:ABPerson
default	20:04:28.110706-0500	Nexy	0000 Contact: 36B84A8B-DD90-4609-9407-3BED73397C90:ABPerson
default	20:04:28.110711-0500	Nexy	0000 Contact: 25B2E948-39F0-4DA0-984A-6EAAFC4452BF:ABPerson
default	20:04:28.110714-0500	Nexy	0000 Contact: FD3874CC-9147-45D7-9635-BA7057F1E4CE:ABPerson
default	20:04:28.110721-0500	Nexy	0000 Contact: 93C427E1-DE52-48BF-AFC1-082EC9E9EDA0:ABPerson
default	20:04:28.110727-0500	Nexy	0000 Contact: 0ADD2D08-B0E0-4789-8BA5-3036146B6B78:ABPerson
default	20:04:28.110740-0500	Nexy	0000 Contact: C1626763-A8D5-4907-A0D9-325529F3E7B5:ABPerson
default	20:04:28.110745-0500	Nexy	0000 Contact: A691F96E-80C3-406D-A1F3-443C491D30D0:ABPerson
default	20:04:28.110750-0500	Nexy	0000 Contact: 331AE8C5-F99D-4F0A-B33F-36D558A607C3:ABPerson
default	20:04:28.110764-0500	Nexy	0000 Contact: 5C041266-AB76-41D1-BBBA-5FE4A4792084:ABPerson
default	20:04:28.110769-0500	Nexy	0000 Contact: F3BDC31E-20AF-4198-B696-F389C8F31C9F:ABPerson
default	20:04:28.110775-0500	Nexy	0000 Contact: 0CC4651C-3FC4-4644-BAB9-41107FBFF900:ABPerson
default	20:04:28.110780-0500	Nexy	0000 Contact: 9C0BE147-A58C-44D2-9C4A-FC7DFE653F3E:ABPerson
default	20:04:28.110802-0500	Nexy	0000 Contact: 0C5D18DF-0E63-4D12-AB19-70F9449BFDD3:ABPerson
default	20:04:28.110807-0500	Nexy	0000 Contact: 1EB1F958-3A33-4C17-AEFC-E59EA17F5D5B:ABPerson
default	20:04:28.110811-0500	Nexy	0000 Contact: E9510B2D-16FE-4F94-BBBE-BFACDEEF0759:ABPerson
default	20:04:28.110816-0500	Nexy	0000 Contact: 5D99F42B-5A12-4DD2-9DA9-063C524A30C7:ABPerson
default	20:04:28.110822-0500	Nexy	0000 Contact: 7C44FDAA-3756-43F4-B87F-DDA61E480B1C:ABPerson
default	20:04:28.110827-0500	Nexy	0000 Contact: DFDA976C-6D05-4677-AAA2-604A3688988F:ABPerson
default	20:04:28.110831-0500	Nexy	0000 Contact: 91B8C6A6-858C-4158-B742-E97BCFF7F054:ABPerson
default	20:04:28.110852-0500	Nexy	0000 Contact: 2A16F554-F4B5-4D1A-84FF-1B1B9CD41A6F:ABPerson
default	20:04:28.110857-0500	Nexy	0000 Contact: 51FDBD11-7239-4140-9605-7B2CFF1426E4:ABPerson
default	20:04:28.110862-0500	Nexy	0000 Contact: 2F813EA9-9EFC-409F-A1C4-64F820E4D179:ABPerson
default	20:04:28.110867-0500	Nexy	0000 Contact: 6B7D950D-D374-429D-91CE-A6E1B5D41AAA:ABPerson
default	20:04:28.110872-0500	Nexy	0000 Contact: F7679D0A-6363-40EC-A12A-63E9F2C28321:ABPerson
default	20:04:28.110876-0500	Nexy	0000 Contact: 6703F826-C4D7-43ED-83B5-77B3CBF74E39:ABPerson
default	20:04:28.110893-0500	Nexy	0000 Contact: ED036238-8F1A-4104-98CA-4C44E9BC5990:ABPerson
default	20:04:28.110898-0500	Nexy	0000 Contact: 00F2C374-C9A3-4DD0-B92B-E70CEFC1C968:ABPerson
default	20:04:28.110905-0500	Nexy	0000 Contact: E984A144-E505-46AA-AA38-1CF1EE5DF265:ABPerson
default	20:04:28.110912-0500	Nexy	0000 Contact: 444D762E-7CC5-479E-B3C7-D5172CE8F56B:ABPerson
default	20:04:28.110918-0500	Nexy	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	20:04:28.110923-0500	Nexy	0000 Contact: AA3A68CB-8A4B-4BAD-94D4-F0B1FDEF6AD2:ABPerson
default	20:04:28.110928-0500	Nexy	0000 Contact: B729AB23-719C-4993-99D4-97F17990CA6E:ABPerson
default	20:04:28.110976-0500	Nexy	0000 Contact: DDD6C0A5-9D08-4756-BB6E-06612386E694:ABPerson
default	20:04:28.110989-0500	Nexy	0000 Contact: DAA81742-1BAC-4E0A-86AB-1805922F5BFB:ABPerson
default	20:04:28.110996-0500	Nexy	0000 Contact: CCCE8074-7CFC-4765-87C4-3DA3398ED5E3:ABPerson
default	20:04:28.111001-0500	Nexy	0000 Contact: B3126A39-DB1F-4EB9-BA9E-057A701FEADB:ABPerson
default	20:04:28.111006-0500	Nexy	0000 Contact: D7A6F43C-FFAB-4219-B325-4345A3EBA5B5:ABPerson
default	20:04:28.111011-0500	Nexy	0000 Contact: F3959633-1472-4370-AE25-6C163A86F28A:ABPerson
default	20:04:28.111015-0500	Nexy	0000 Contact: 818A8D3F-5A2E-44CA-B4CF-47B295DB8C98:ABPerson
default	20:04:28.111021-0500	Nexy	0000 Contact: 228410FA-14BD-488B-A385-35C7112B9635:ABPerson
default	20:04:28.111026-0500	Nexy	0000 Contact: 1A2FDBB3-F370-4D0F-8C9A-34D9C191D7E3:ABPerson
default	20:04:28.111031-0500	Nexy	0000 Contact: 5FDB4463-1088-4EF5-9E20-48795D669908:ABPerson
default	20:04:28.111036-0500	Nexy	0000 Contact: 241E5174-F04C-45D2-BB1E-C4295A53CA80:ABPerson
default	20:04:28.111041-0500	Nexy	0000 Contact: 135FEF8F-5A69-49C6-97E1-E218FAD43A7E:ABPerson
default	20:04:28.111044-0500	Nexy	0000 Contact: F7BF6E9A-A1DE-4F0A-B9FE-DD0E61EBC464:ABPerson
default	20:04:28.111051-0500	Nexy	0000 Contact: F4DA25ED-6C3C-44D5-8A9B-87F14829E713:ABPerson
default	20:04:28.111054-0500	Nexy	0000 Contact: 95FF7EB7-87CC-416D-8811-B8DCC6FE7621:ABPerson
default	20:04:28.111062-0500	Nexy	0000 Contact: 751FAE5C-98A6-414E-B107-317AF0CBED37:ABPerson
default	20:04:28.111068-0500	Nexy	0000 Contact: 5465ECDD-A832-402B-BB73-FDF36810C6E0:ABPerson
default	20:04:28.111073-0500	Nexy	0000 Contact: 52FD2EC7-BEF6-4D05-BCAC-73FBAA131CDF:ABPerson
default	20:04:28.111078-0500	Nexy	0000 Contact: 9D848D63-FDF8-461C-9756-F8AAC3070EFF:ABPerson
default	20:04:28.111083-0500	Nexy	0000 Contact: D6BF6AC9-65CA-41BE-AFA2-C3071A2539F5:ABPerson
default	20:04:28.111107-0500	Nexy	0000 Contact: 4E4C0E62-3EE9-4F23-A226-025907D6882D:ABPerson
default	20:04:28.111112-0500	Nexy	0000 Contact: 1006869C-954C-4394-BFE9-09E9CE09AFB5:ABPerson
default	20:04:28.111118-0500	Nexy	0000 Contact: 339B0201-420C-414B-96CB-1D8150AEF6BB:ABPerson
default	20:04:28.111123-0500	Nexy	0000 Contact: 6A713058-BCB2-4635-BC21-577F0261940C:ABPerson
default	20:04:28.111128-0500	Nexy	0000 Contact: 8B61AAC1-DF6F-440A-B5AC-33331AF930E1:ABPerson
default	20:04:28.111131-0500	Nexy	0000 Contact: B5C0C11D-6F8A-4CCE-872A-DEC086F666A6:ABPerson
default	20:04:28.111136-0500	Nexy	0000 Contact: D17EDFE8-D58A-41FF-B738-D480ED1B54BB:ABPerson
default	20:04:28.111141-0500	Nexy	0000 Contact: 8D969F0D-4878-45C3-A329-14C8F1B9A1C4:ABPerson
default	20:04:28.111152-0500	Nexy	0000 Contact: 4DC763F6-4288-4A25-AE37-52DAC0E54434:ABPerson
default	20:04:28.111159-0500	Nexy	0000 Contact: BB62CE57-7037-4156-BE7F-D1E84FA0B46F:ABPerson
default	20:04:28.111171-0500	Nexy	0000 Contact: 32598CF7-ABA5-4AF8-B60C-8B3F9BB79824:ABPerson
default	20:04:28.111176-0500	Nexy	0000 Contact: 4C93D59E-2641-437E-8D5E-6E5135B4B9D7:ABPerson
default	20:04:28.111229-0500	Nexy	0000 Contact: 95C0601A-0362-4E71-9B56-8E66BA6334DB:ABPerson
default	20:04:28.111238-0500	Nexy	0000 Contact: F23EFEDD-DB9E-4EEE-86A8-A0BB0B161DCE:ABPerson
default	20:04:28.111243-0500	Nexy	0000 Contact: A25C8DA8-E066-47BE-A228-BA3A79122649:ABPerson
default	20:04:28.111248-0500	Nexy	0000 Contact: 7709CB5C-F45D-4130-AFCC-F66EB248B381:ABPerson
default	20:04:28.111253-0500	Nexy	0000 Contact: A95901C1-18E2-412B-9429-B9A87D46EEF1:ABPerson
default	20:04:28.111258-0500	Nexy	0000 Contact: 90CCE3F7-7CB8-44CE-8E3B-0E1FEE5B8574:ABPerson
default	20:04:28.111262-0500	Nexy	0000 Contact: D21F44BE-5C0B-49C1-ACBC-50C7FDD0E574:ABPerson
default	20:04:28.111268-0500	Nexy	0000 Contact: 9A341135-6F8F-42C6-A5D8-776E0F0EF424:ABPerson
default	20:04:28.111277-0500	Nexy	0000 Contact: 60C9F9CC-1758-4215-94FA-79E8E5591D0D:ABPerson
default	20:04:28.111284-0500	Nexy	0000 Contact: 7A0D8FED-170A-4F26-B868-532276E4BDF6:ABPerson
default	20:04:28.111288-0500	Nexy	0000 Contact: 791662EB-B4C3-41EA-8207-065A1C9F0AA0:ABPerson
default	20:04:28.111294-0500	Nexy	0000 Contact: D5AB1F03-8C06-438F-8713-DCCBBCD76892:ABPerson
default	20:04:28.111298-0500	Nexy	0000 Contact: 96EC0E50-9CC0-4769-8082-E7C877889553:ABPerson
default	20:04:28.111304-0500	Nexy	0000 Contact: 33394098-1926-4C5F-AA29-7B8610A5C7E6:ABPerson
default	20:04:28.111309-0500	Nexy	0000 Contact: B5956767-6E1D-49F2-8708-69E0D16EC786:ABPerson
default	20:04:28.111314-0500	Nexy	0000 Contact: 918AF5E7-EDE6-400D-A786-261C7B3BC323:ABPerson
default	20:04:28.111319-0500	Nexy	0000 Contact: 78374AF4-D2CF-4636-B824-5922E7BCDAA7:ABPerson
default	20:04:28.111324-0500	Nexy	0000 Contact: E1E5926D-F19D-45D4-9FFE-12E3198D0E67:ABPerson
default	20:04:28.111329-0500	Nexy	0000 Contact: DB957E68-3771-4194-AB47-1B347BE66F63:ABPerson
default	20:04:28.111332-0500	Nexy	0000 Contact: 2112C6EB-840A-49FE-B03E-5DDBFE2F6992:ABPerson
default	20:04:28.111340-0500	Nexy	0000 Contact: 3E8DAA1B-0AD6-465E-BDAB-A68A5FD23D3E:ABPerson
default	20:04:28.111352-0500	Nexy	0000 Contact: 5B8A6BDC-5927-4718-B89F-674DCC70DA16:ABPerson
default	20:04:28.111357-0500	Nexy	0000 Contact: 44BFDAD7-D780-4604-8369-CD3317F7F3FB:ABPerson
default	20:04:28.111363-0500	Nexy	0000 Contact: DD452BC2-AA0F-4E55-9417-30946834E7D9:ABPerson
default	20:04:28.111373-0500	Nexy	0000 Contact: A79E1C58-6726-4518-9160-5833FD1D9E85:ABPerson
default	20:04:28.111380-0500	Nexy	0000 Contact: EEDB6E81-803C-4D9E-9479-23840064FF07:ABPerson
default	20:04:28.111391-0500	Nexy	0000 Contact: E8BAA178-7C7C-4B0C-837F-07B80E6A8155:ABPerson
default	20:04:28.111396-0500	Nexy	0000 Contact: A8C84C99-FF9C-48DF-A603-CEB3050F0BC6:ABPerson
default	20:04:28.111402-0500	Nexy	0000 Contact: 0FD65269-7801-440C-A119-71EBE23C4E70:ABPerson
default	20:04:28.111407-0500	Nexy	0000 Contact: 0A4FEAE5-C426-4926-8B49-A5260D97B9E6:ABPerson
default	20:04:28.111417-0500	Nexy	0000 Contact: CA81313F-6121-4FF6-B60C-EEE869ECF990:ABPerson
default	20:04:28.111423-0500	Nexy	0000 Contact: EA9B96E2-2F87-4EB2-AD12-46F37DFF0EC9:ABPerson
default	20:04:28.111433-0500	Nexy	0000 Contact: 7A89C56B-6D06-419B-A08D-00F14B94AA1C:ABPerson
default	20:04:28.111438-0500	Nexy	0000 Contact: 660A1E96-3CA3-48B5-B94A-96D6D35A72E6:ABPerson
default	20:04:28.111450-0500	Nexy	0000 Contact: 3F5D85F3-9B89-4AD7-A353-FEFEA5DA1C36:ABPerson
default	20:04:28.111455-0500	Nexy	0000 Contact: 8F99EACB-5E71-4F4C-9899-AE7E1FF5280E:ABPerson
default	20:04:28.111460-0500	Nexy	0000 Contact: 9E8B52AD-B9B2-41CA-8134-7861A90F9A02:ABPerson
default	20:04:28.111473-0500	Nexy	0000 Contact: 98237DEC-70B4-4CA5-A4B8-FEE401C3F3C4:ABPerson
default	20:04:28.111478-0500	Nexy	0000 Contact: BD690A56-23D5-4941-B041-50C06351C977:ABPerson
default	20:04:28.111489-0500	Nexy	0000 Contact: D191A589-BA65-49F2-86A3-08D90FB284FD:ABPerson
default	20:04:28.111500-0500	Nexy	0000 Contact: AAF5FE8A-214C-4B65-9B4F-C2578C97C51D:ABPerson
default	20:04:28.111505-0500	Nexy	0000 Contact: 3D737248-8F03-4732-8B3A-8CDA2D45B5AA:ABPerson
default	20:04:28.111514-0500	Nexy	0000 Contact: E120A189-E8F5-4B5F-A2A2-B1A60E6DF145:ABPerson
default	20:04:28.111532-0500	Nexy	0000 Contact: 46187B48-32E0-4B21-B7CE-D3B44766EEEC:ABPerson
default	20:04:28.111537-0500	Nexy	0000 Contact: B72ACD21-62D9-4BC2-8F5A-F33464EEEED5:ABPerson
default	20:04:28.111545-0500	Nexy	0000 Contact: 1D1B1CB1-D316-4BC5-B11C-BC2D4D437605:ABPerson
default	20:04:28.111550-0500	Nexy	0000 Contact: EEC7F987-F555-4025-8B35-10CBE93E26D7:ABPerson
default	20:04:28.111558-0500	Nexy	0000 Contact: A4F96105-C3FC-4D3D-842F-E729A3F28760:ABPerson
default	20:04:28.111566-0500	Nexy	0000 Contact: F0613D78-6887-4B13-AC52-703B5D1A7060:ABPerson
default	20:04:28.111572-0500	Nexy	0000 Contact: BDD5E012-4C2D-4949-9778-80672887C0EC:ABPerson
default	20:04:28.111576-0500	Nexy	0000 Contact: E03CBC1C-C4D5-476B-A9AE-20A246A5FE73:ABPerson
default	20:04:28.111581-0500	Nexy	0000 Contact: A9567605-C983-4D5B-9877-2D3BC5D341CF:ABPerson
default	20:04:28.111587-0500	Nexy	0000 Contact: 378D10F9-7887-44F8-B0A5-9683F2AF012D:ABPerson
default	20:04:28.111597-0500	Nexy	0000 Contact: 29F7EE25-03CA-4DEA-AB4C-5E84B0046094:ABPerson
default	20:04:28.111612-0500	Nexy	0000 Contact: 6045438B-32EF-4240-BCDE-3A83DD6098C1:ABPerson
default	20:04:28.111617-0500	Nexy	0000 Contact: CC00B3CB-4536-414F-8E8F-116901AAAB66:ABPerson
default	20:04:28.111623-0500	Nexy	0000 Contact: CDF1FCD3-669F-4B16-9D7A-07091B53B43E:ABPerson
default	20:04:28.111628-0500	Nexy	0000 Contact: 1C7A8AAA-2853-4C56-892C-93832C406B2F:ABPerson
default	20:04:28.111633-0500	Nexy	0000 Contact: 5FA233B8-A72C-468F-8344-138CB3A320AD:ABPerson
default	20:04:28.111643-0500	Nexy	0000 Contact: CC42A082-921C-4A2F-9B2A-20AD5E63DE26:ABPerson
default	20:04:28.111648-0500	Nexy	0000 Contact: 4D22B39B-A7C9-4F71-B531-0D0A75E819DC:ABPerson
default	20:04:28.111658-0500	Nexy	0000 Contact: 10DA5D0D-F87E-40C2-A2FB-1B4E18ADEED7:ABPerson
default	20:04:28.111664-0500	Nexy	0000 Contact: 1020F64F-877A-46EF-A85B-0B7B4702F30A:ABPerson
default	20:04:28.111675-0500	Nexy	0000 Contact: 7A3258A0-4EF6-4C07-8BAC-DE67AFC5BF0F:ABPerson
default	20:04:28.111681-0500	Nexy	0000 Contact: D8BF88A0-50CD-408B-91AC-FABB6153F0E7:ABPerson
default	20:04:28.111691-0500	Nexy	0000 Contact: F96FB111-3581-4F57-A0DB-8D18E0A5CE3D:ABPerson
default	20:04:28.111701-0500	Nexy	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	20:04:28.111712-0500	Nexy	0000 Contact: 2DD46A4A-00EA-4AF2-BED6-A0E4704A401E:ABPerson
default	20:04:28.111717-0500	Nexy	0000 Contact: E75A43A8-9126-46AD-BDE0-2F09D8195FCE:ABPerson
default	20:04:28.111727-0500	Nexy	0000 Contact: 0CE70590-2C7E-400D-AAC3-E2AB83B20E6D:ABPerson
default	20:04:28.111752-0500	Nexy	0000 Contact: C93B2BF3-4882-418D-A785-20AABA5900CA:ABPerson
default	20:04:28.111757-0500	Nexy	0000 Contact: 72A79220-BD0A-4F38-A644-7891B8D6D08C:ABPerson
default	20:04:28.111763-0500	Nexy	0000 Contact: 5168F235-33BF-487B-9C88-9A0977EF3D96:ABPerson
default	20:04:28.111777-0500	Nexy	0000 Contact: EF5D8980-C0E4-4FBD-8942-AC7EC9F886BE:ABPerson
default	20:04:28.111783-0500	Nexy	0000 Contact: 8335160D-3EFF-4C7A-B500-08D4AAF9D6C4:ABPerson
default	20:04:28.111788-0500	Nexy	0000 Contact: F30C415E-480E-47D7-A697-2DDF78C62B78:ABPerson
default	20:04:28.111797-0500	Nexy	0000 Contact: 4B86EE6B-7192-4DEC-9A5D-DB2A68A29544:ABPerson
default	20:04:28.111803-0500	Nexy	0000 Contact: 7028A821-E1BB-4996-9F0A-B483955BBD46:ABPerson
default	20:04:28.111813-0500	Nexy	0000 Contact: 7C930844-C857-4F62-B795-A317F57982E7:ABPerson
default	20:04:28.111819-0500	Nexy	0000 Contact: 2958D2B1-193E-4859-97A7-E9D0A6DDAC5B:ABPerson
default	20:04:28.111830-0500	Nexy	0000 Contact: CF7AC9E0-68F2-4C92-A7E7-2F56630F8B8B:ABPerson
default	20:04:28.111857-0500	Nexy	0000 Contact: ADDCC376-3417-4952-A610-3D53B96EC2BD:ABPerson
default	20:04:28.111865-0500	Nexy	0000 Contact: 19855E2F-023D-4999-A9F8-0515B5257D6F:ABPerson
default	20:04:28.111869-0500	Nexy	0000 Contact: 2BAB4AEF-3D51-42E4-BBCA-4587A6EF5B42:ABPerson
default	20:04:28.111874-0500	Nexy	0000 Contact: B68F306A-9F87-4675-9C7C-73ADAC3CF928:ABPerson
default	20:04:28.111879-0500	Nexy	0000 Contact: EBEFEBC5-E9A8-48CB-B48D-DE0E2C3AE2B9:ABPerson
default	20:04:28.111887-0500	Nexy	0000 Contact: C1E29AB3-927E-4614-A170-469712D37DE0:ABPerson
default	20:04:28.111893-0500	Nexy	0000 Contact: 1E18829A-DFA4-4A9A-AEBA-FFF85B2D3E00:ABPerson
default	20:04:28.111900-0500	Nexy	0000 Contact: 41E94FCB-1477-45AF-AB50-6AF7C4651D76:ABPerson
default	20:04:28.111905-0500	Nexy	0000 Contact: 55D05EF1-7380-43F3-9CCC-FCCBB0A382A9:ABPerson
default	20:04:28.111910-0500	Nexy	0000 Contact: 88B8B688-3607-4FD1-BE7E-73F6DAA20674:ABPerson
default	20:04:28.111926-0500	Nexy	0000 Contact: 6A7FA276-678E-44BC-A5CD-1E7AB887CD37:ABPerson
default	20:04:28.111931-0500	Nexy	0000 Contact: A6FD2708-9CD8-45E0-9E88-5BE836285468:ABPerson
default	20:04:28.111937-0500	Nexy	0000 Contact: FFBA4F3C-8FF6-4FC6-9CB6-F62755FFB90C:ABPerson
default	20:04:28.111943-0500	Nexy	0000 Contact: F5A10DB4-BCD8-4342-9435-C976615D2367:ABPerson
default	20:04:28.111949-0500	Nexy	0000 Contact: 1C210F17-EE8F-4513-8100-4877479969F3:ABPerson
default	20:04:28.111963-0500	Nexy	0000 Contact: E6ACEB4F-3D7F-4D37-8463-568D34A3D393:ABPerson
default	20:04:28.111968-0500	Nexy	0000 Contact: 05B170A2-D739-4BCB-A7A9-927DAAC7B3FD:ABPerson
default	20:04:28.111973-0500	Nexy	0000 Contact: 791F5495-5017-4DBF-ABB6-4220285C8A7F:ABPerson
default	20:04:28.111979-0500	Nexy	0000 Contact: DFA3FE46-B8CF-41EC-B2E6-04C798B63209:ABPerson
default	20:04:28.111990-0500	Nexy	0000 Contact: 09772BD5-23E2-45C0-8579-EAA3F5DFAA04:ABPerson
default	20:04:28.111995-0500	Nexy	0000 Contact: 21D1D25A-A332-455E-BF6D-219DAED4CF2E:ABPerson
default	20:04:28.112009-0500	Nexy	0000 Contact: 85CBC919-29F4-4481-90E8-91811DF04251:ABPerson
default	20:04:28.112016-0500	Nexy	0000 Contact: 7D4E6C00-B562-4BD3-84B2-BE3484A218DC:ABPerson
default	20:04:28.112021-0500	Nexy	0000 Contact: 7CEA1D92-BD70-4661-A995-FC9C088765E4:ABPerson
default	20:04:28.112026-0500	Nexy	0000 Contact: 5BC153A8-ECD2-4153-8199-62D228ED9EFF:ABPerson
default	20:04:28.112031-0500	Nexy	0000 Contact: 539E00F6-4B11-4899-9B48-833F1C83B1AF:ABPerson
default	20:04:28.112042-0500	Nexy	0000 Contact: 480BDC40-266E-44A2-A7F0-81FF207F9107:ABPerson
default	20:04:28.112047-0500	Nexy	0000 Contact: AD76EC2F-309C-4663-88AB-5380B537AD21:ABPerson
default	20:04:28.112083-0500	Nexy	0000 Contact: E8D00EFB-149F-4D70-9E53-DCC37B11CA41:ABPerson
default	20:04:28.112090-0500	Nexy	0000 Contact: F1AC5DD9-2463-40B4-A31D-D698D4A81A07:ABPerson
default	20:04:28.112095-0500	Nexy	0000 Contact: 5CC4AD9E-AFA2-4D91-93BB-A2AEE0287CA1:ABPerson
default	20:04:28.112099-0500	Nexy	0000 Contact: 82273310-7E56-45DD-8F38-49E6EFB991AF:ABPerson
default	20:04:28.112103-0500	Nexy	0000 Contact: 52C4710F-7736-48E9-81CB-BFB715D2471F:ABPerson
default	20:04:28.112108-0500	Nexy	0000 Contact: 3DAF2C1D-E01A-4ECE-88B6-7A1FEC8F43AC:ABPerson
default	20:04:28.112112-0500	Nexy	0000 Contact: C66A3203-5558-449A-90CB-DECEC564C830:ABPerson
default	20:04:28.112118-0500	Nexy	0000 Contact: 1587F0BD-924E-4B7A-B625-9C3C29B7D02B:ABPerson
default	20:04:28.112123-0500	Nexy	0000 Contact: 8E669F37-64D4-4FCD-83DF-C7AB7025BAED:ABPerson
default	20:04:28.112128-0500	Nexy	0000 Contact: 42E8C30D-1FB0-42FC-833E-588AB5BBE3DB:ABPerson
default	20:04:28.112143-0500	Nexy	0000 Contact: EAE3066F-0C4F-41A6-8DBE-F68459786EC0:ABPerson
default	20:04:28.112149-0500	Nexy	0000 Contact: 2AF16E0B-3963-42BF-9826-D9FEA11B3CCA:ABPerson
default	20:04:28.112154-0500	Nexy	0000 Contact: 319E891D-32E9-49AF-B4E4-B5BAE8155200:ABPerson
default	20:04:28.112168-0500	Nexy	0000 Contact: 1594CB17-7E0F-473A-929D-C52CB3C2ADF4:ABPerson
default	20:04:28.112174-0500	Nexy	0000 Contact: 77010702-80A2-4E97-B0A7-B2EE441BFF58:ABPerson
default	20:04:28.112185-0500	Nexy	0000 Contact: 878309A1-31D9-4B89-8226-32C4BFA85E5A:ABPerson
default	20:04:28.112193-0500	Nexy	0000 Contact: 8C53459B-D709-4754-8779-C759C5D30623:ABPerson
default	20:04:28.112199-0500	Nexy	0000 Contact: 2D7A7BAB-3BDE-4E62-9336-46D7687262C6:ABPerson
default	20:04:28.112204-0500	Nexy	0000 Contact: ADE039BB-356A-4FF6-9B48-11643C1A74A3:ABPerson
default	20:04:28.112209-0500	Nexy	0000 Contact: 1DAA78BA-EBAD-4BF6-B582-A4DE8A4A1F60:ABPerson
default	20:04:28.112217-0500	Nexy	0000 Contact: E3B3AD82-9DE2-41D8-BAB4-955DF431F0D7:ABPerson
default	20:04:28.112230-0500	Nexy	0000 Contact: 4EA7F008-36E8-457A-AB52-5E92AB655707:ABPerson
default	20:04:28.112235-0500	Nexy	0000 Contact: 2EE1FF46-FBE2-4A40-8CE4-EC8C163406A8:ABPerson
default	20:04:28.112240-0500	Nexy	0000 Contact: 4749FF87-CDF6-4765-A605-FBF954CEC3DD:ABPerson
default	20:04:28.112255-0500	Nexy	0000 Contact: 78533628-5040-45D4-907C-06311D0B83C8:ABPerson
default	20:04:28.112260-0500	Nexy	0000 Contact: 55ED3DE3-FD66-4A5E-995C-7174A0F57355:ABPerson
default	20:04:28.112265-0500	Nexy	0000 Contact: 1EB3E13D-C8C2-40B4-B5C1-95672F5BB775:ABPerson
default	20:04:28.112270-0500	Nexy	0000 Contact: F83287C3-CE0B-407B-88A2-A5B43CAB98EC:ABPerson
default	20:04:28.112274-0500	Nexy	0000 Contact: 2D1AC54F-1C05-415F-803B-EB84B4DE155C:ABPerson
default	20:04:28.112289-0500	Nexy	0000 Contact: C8633A15-35F4-4ABC-9A2A-82EBF1A6767D:ABPerson
default	20:04:28.112294-0500	Nexy	0000 Contact: D62A5235-E401-4A9F-AC82-61328161530D:ABPerson
default	20:04:28.112299-0500	Nexy	0000 Contact: C80DE5B6-E12E-4835-863B-E63D84C0DEB5:ABPerson
default	20:04:28.112314-0500	Nexy	0000 Contact: 922530A8-0D72-4067-AAC0-1FF5C4ABE1BA:ABPerson
default	20:04:28.112320-0500	Nexy	0000 Contact: A66AB62E-7C4B-489D-A5AC-97BE240AF07B:ABPerson
default	20:04:28.112325-0500	Nexy	0000 Contact: C42862EB-E49A-4500-B5A0-744247A93DC0:ABPerson
default	20:04:28.112329-0500	Nexy	0000 Contact: 3608E376-1FDF-4DA6-94BE-B39CF8F32D25:ABPerson
default	20:04:28.112337-0500	Nexy	0000 Contact: 3D44B959-62DC-41CB-825F-C0FB5D231322:ABPerson
default	20:04:28.112350-0500	Nexy	0000 Contact: 47FCBCE3-65D3-44A4-8283-4C1AF6654C9F:ABPerson
default	20:04:28.112356-0500	Nexy	0000 Contact: 93BAC1B1-3857-40CA-A143-09E6F7A990EF:ABPerson
default	20:04:28.112361-0500	Nexy	0000 Contact: F1B433EB-BB39-4CD7-A784-1E41309B908C:ABPerson
default	20:04:28.112373-0500	Nexy	0000 Contact: A52B8A51-99C7-427A-BD9F-97EC5E9F7EA8:ABPerson
default	20:04:28.112382-0500	Nexy	0000 Contact: 0191E2F5-DF4D-441F-A40B-BBEE1682877B:ABPerson
default	20:04:28.112387-0500	Nexy	0000 Contact: 0697FA50-06C8-4FDB-A5D3-B10F8A859674:ABPerson
default	20:04:28.112401-0500	Nexy	0000 Contact: 093F142A-458F-4ACF-BEEE-FAB7BA5E520A:ABPerson
default	20:04:28.112406-0500	Nexy	0000 Contact: 98F95301-000C-4EF9-91DF-E637EF0C27F4:ABPerson
default	20:04:28.112411-0500	Nexy	0000 Contact: 720814F5-D603-40AE-A834-D49467F3A7FD:ABPerson
default	20:04:28.112425-0500	Nexy	0000 Contact: 40CDB1E4-DC18-4D79-AE2F-6242CCF62978:ABPerson
default	20:04:28.112430-0500	Nexy	0000 Contact: A8D9C348-1926-49B7-98C2-A2C917FB651B:ABPerson
default	20:04:28.112436-0500	Nexy	0000 Contact: 7656FBDF-5810-4382-9538-529EC1E5EF83:ABPerson
default	20:04:28.112442-0500	Nexy	0000 Contact: 8F442B0B-AFC7-4087-AEFC-FDC987F28E2C:ABPerson
default	20:04:28.112451-0500	Nexy	0000 Contact: DE96F2D0-DA7E-4742-AD3E-6D43BC32C213:ABPerson
default	20:04:28.112457-0500	Nexy	0000 Contact: DA1B14DD-D92B-4633-BF3C-0CCCE7117BE4:ABPerson
default	20:04:28.112462-0500	Nexy	0000 Contact: 0134E272-51ED-44B6-AC46-4C34642F56AA:ABPerson
default	20:04:28.112474-0500	Nexy	0000 Contact: FA551EE7-6781-4874-B9EA-0B6893B3293F:ABPerson
default	20:04:28.112482-0500	Nexy	0000 Contact: A88C8AF6-EF10-48E8-9C60-3709424155EB:ABPerson
default	20:04:28.112492-0500	Nexy	0000 Contact: C00692B4-EC26-459C-A690-D23F5BCEF621:ABPerson
default	20:04:28.112498-0500	Nexy	0000 Contact: 652921DA-B2DA-4539-A7F6-6B5A80149E2C:ABPerson
default	20:04:28.112504-0500	Nexy	0000 Contact: 88DED267-1D14-49FB-B0EA-D61FEEEA7475:ABPerson
default	20:04:28.112536-0500	Nexy	0000 Contact: CEB05018-C421-4234-BE90-56F8041F2286:ABPerson
default	20:04:28.112543-0500	Nexy	0000 Contact: DFB23C20-7349-4617-9A20-48014D8D844F:ABPerson
default	20:04:28.112546-0500	Nexy	0000 Contact: 9AC48DA6-FEAA-4630-AD56-EF041D62524A:ABPerson
default	20:04:28.112551-0500	Nexy	0000 Contact: 936230C2-1597-4A80-898D-31476BAE0C72:ABPerson
default	20:04:28.112557-0500	Nexy	0000 Contact: E99AC935-51E8-4AC2-9D90-C3ED9A41CF89:ABPerson
default	20:04:28.112564-0500	Nexy	0000 Contact: 1041C9F3-A247-4866-BCE3-A908919C3641:ABPerson
default	20:04:28.112567-0500	Nexy	0000 Contact: AA55B04C-AA66-4E4C-BE73-FCD01D057FF4:ABPerson
default	20:04:28.112572-0500	Nexy	0000 Contact: 8E1DE28A-250A-438D-ADCC-EC00B09AFDCF:ABPerson
default	20:04:28.112577-0500	Nexy	0000 Contact: 9D974937-BC35-459C-9596-7F3C287A39DE:ABPerson
default	20:04:28.112595-0500	Nexy	0000 Contact: 7A52455B-63F6-4500-850D-4CD4CAEE7CDA:ABPerson
default	20:04:28.112600-0500	Nexy	0000 Contact: BB0E685F-E844-4A51-8837-01C68FCCEECD:ABPerson
default	20:04:28.112605-0500	Nexy	0000 Contact: 958F31A6-1E1B-4833-99AC-EC3D8191CACE:ABPerson
default	20:04:28.112610-0500	Nexy	0000 Contact: 88212F02-02C2-4E0B-AD31-33A4F57D97C3:ABPerson
default	20:04:28.112613-0500	Nexy	0000 Contact: 060A07B0-DE54-4CA0-82F9-C5E7D642FE04:ABPerson
default	20:04:28.112627-0500	Nexy	0000 Contact: 84FD0E15-D8B4-4C4A-AF3F-ECACC4D7D2AB:ABPerson
default	20:04:28.112634-0500	Nexy	0000 Contact: E03C33D7-9B66-41CC-9823-13495C0F1BFF:ABPerson
default	20:04:28.112639-0500	Nexy	0000 Contact: 4F05D0EB-A7C7-4CE9-8BBE-252CDE0913B6:ABPerson
default	20:04:28.112644-0500	Nexy	0000 Contact: 0D4D94BE-BE27-4924-B1EF-D18DBC8CB9CB:ABPerson
default	20:04:28.112653-0500	Nexy	0000 Contact: DE3244DE-AA8B-42BE-9E6B-D93D5F072FC8:ABPerson
default	20:04:28.112658-0500	Nexy	0000 Contact: D2349093-8AC3-493E-A63B-2FDDBF010597:ABPerson
default	20:04:28.112669-0500	Nexy	0000 Contact: 582B6770-D754-4F28-BE23-DE8B912C1D70:ABPerson
default	20:04:28.112677-0500	Nexy	0000 Contact: 7230DAA8-42F7-4810-9E64-7E0576DEC21F:ABPerson
default	20:04:28.112685-0500	Nexy	0000 Contact: A044BEEF-238E-4A88-9B39-26B87097EDBA:ABPerson
default	20:04:28.112692-0500	Nexy	0000 Contact: 37C10F00-3A36-4D68-A9FE-F7CBB93250AA:ABPerson
default	20:04:28.112709-0500	Nexy	0000 Contact: BF90E79B-597F-4512-8E44-EA4CE870BBE2:ABPerson
default	20:04:28.112715-0500	Nexy	0000 Contact: BC75C771-F624-4E3A-AD7C-60B2F270D59D:ABPerson
default	20:04:28.112720-0500	Nexy	0000 Contact: C9795424-7E48-45EA-BBDF-4E008BDD9978:ABPerson
default	20:04:28.112725-0500	Nexy	0000 Contact: 40A1ED53-5876-46E0-B311-D54958985F34:ABPerson
default	20:04:28.112730-0500	Nexy	0000 Contact: 7E4C40BE-99FF-4182-ACF1-5DF8D2DDBE83:ABPerson
default	20:04:28.112735-0500	Nexy	0000 Contact: 6E048310-6707-4D3C-BD0B-81F080042AD6:ABPerson
default	20:04:28.112750-0500	Nexy	0000 Contact: 7268EB56-C8B9-4982-99B0-A40D08B65BA9:ABPerson
default	20:04:28.112756-0500	Nexy	0000 Contact: 0E2D5908-AAC6-40CB-BFB1-0CE7506D0A99:ABPerson
default	20:04:28.112761-0500	Nexy	0000 Contact: D2628142-CF91-46B0-A289-5CA32977E44D:ABPerson
default	20:04:28.112786-0500	Nexy	0000 Contact: 914E27F4-B07C-487A-BF66-F3CA485B9275:ABPerson
default	20:04:28.112792-0500	Nexy	0000 Contact: D014DC3B-188A-4277-A1D5-FBE211695D60:ABPerson
default	20:04:28.112797-0500	Nexy	0000 Contact: 48C9CC87-0557-4A05-B9B6-9FC3799AA710:ABPerson
default	20:04:28.112806-0500	Nexy	0000 Contact: D19BADAB-1850-4DC5-BEEF-B4D77FFCF312:ABPerson
default	20:04:28.112812-0500	Nexy	0000 Contact: 5F52D0B4-4801-47FD-A2E8-E1EC4C2CFBF7:ABPerson
default	20:04:28.112817-0500	Nexy	0000 Contact: F8F59880-57E4-410D-B266-90532EAA85ED:ABPerson
default	20:04:28.112822-0500	Nexy	0000 Contact: 894EBF35-6AF8-4262-8E87-8394A0235AEA:ABPerson
default	20:04:28.112827-0500	Nexy	0000 Contact: 57AEA313-D5E2-4575-AA16-1A5115913CC7:ABPerson
default	20:04:28.112832-0500	Nexy	0000 Contact: F89D0C36-26A8-41DC-83C9-B4FBE705654B:ABPerson
default	20:04:28.112844-0500	Nexy	0000 Contact: 1B9D8EA6-9499-4BFC-8492-1342D6A1460A:ABPerson
default	20:04:28.112849-0500	Nexy	0000 Contact: 35990211-93E2-4128-9887-673DB78EB237:ABPerson
default	20:04:28.112854-0500	Nexy	0000 Contact: E09D3D05-8D17-403A-BB6D-AE0A7DAC6A91:ABPerson
default	20:04:28.112864-0500	Nexy	0000 Contact: 6947AB19-73BD-4633-9B74-8444F2D5EB48:ABPerson
default	20:04:28.112871-0500	Nexy	0000 Contact: 327524E2-8EE7-43AD-A10C-4D95E5236B33:ABPerson
default	20:04:28.112883-0500	Nexy	0000 Contact: 5C927C23-EC97-4E44-979D-C91168A0225F:ABPerson
default	20:04:28.112888-0500	Nexy	0000 Contact: 3E96739C-79E5-47F2-8D58-297DAFFED273:ABPerson
default	20:04:28.112893-0500	Nexy	0000 Contact: 923B5225-B958-47B8-A994-56D2C6594BC3:ABPerson
default	20:04:28.112904-0500	Nexy	0000 Contact: 71E3945F-552E-4A87-81E7-3B4F6B837FB0:ABPerson
default	20:04:28.112910-0500	Nexy	0000 Contact: 98BB4D37-BA08-403B-863B-EA841E79DDEC:ABPerson
default	20:04:28.112921-0500	Nexy	0000 Contact: 3C958CB9-9822-42CE-908D-E1263845615F:ABPerson
default	20:04:28.112926-0500	Nexy	0000 Contact: 99F6FF83-6AC8-4BB2-A7FB-0E45BF397CE1:ABPerson
default	20:04:28.112943-0500	Nexy	0000 Contact: ECEB9C46-3E9A-4B07-BA0A-83A9F5AC9BD8:ABPerson
default	20:04:28.112951-0500	Nexy	0000 Contact: 2D8CF878-704D-4216-A869-2AA3CE40DC8B:ABPerson
default	20:04:28.112956-0500	Nexy	0000 Contact: D6E1C189-3EE0-4001-BBD7-BA1BAA052DCD:ABPerson
default	20:04:28.112961-0500	Nexy	0000 Contact: 0FB6D688-1124-496D-8A74-936908325AC4:ABPerson
default	20:04:28.112966-0500	Nexy	0000 Contact: 8E63BF2D-7068-4689-AA89-3F14A6D447C7:ABPerson
default	20:04:28.112979-0500	Nexy	0000 Contact: A6A438A5-EBCC-4387-AE2C-974496DF3475:ABPerson
default	20:04:28.112986-0500	Nexy	0000 Contact: A7980BCA-3250-42B1-9819-B7F094FC4046:ABPerson
default	20:04:28.112991-0500	Nexy	0000 Contact: 4C6A56D0-B520-49E0-8E8E-16BA4BC6CC20:ABPerson
default	20:04:28.112994-0500	Nexy	0000 Contact: C0FC9CF3-3693-4D44-981C-6047B6AEE5AB:ABPerson
default	20:04:28.113003-0500	Nexy	0000 Contact: 9436B5EC-36D3-4607-B5EB-7EF577DAA4E1:ABPerson
default	20:04:28.113013-0500	Nexy	0000 Contact: FC8D2904-8F71-4E20-8978-D780134A1143:ABPerson
default	20:04:28.113018-0500	Nexy	0000 Contact: 8E15809F-EDFE-43EB-A729-82985D40BEDD:ABPerson
default	20:04:28.113025-0500	Nexy	0000 Contact: 4CFCE671-0922-422E-84D2-7E3D755B9AA0:ABPerson
default	20:04:28.113035-0500	Nexy	0000 Contact: 97F9A37A-8704-4049-B22E-5464D3555283:ABPerson
default	20:04:28.113042-0500	Nexy	0000 Contact: 5EAB76EB-1518-4AB1-A60F-6440D4E97C67:ABPerson
default	20:04:28.113055-0500	Nexy	0000 Contact: 66AA346D-AFEA-46E3-AB76-B76AB73EEFE6:ABPerson
default	20:04:28.113061-0500	Nexy	0000 Contact: A94FA9D0-8D8F-482E-A1FA-415674AAE3CD:ABPerson
default	20:04:28.113073-0500	Nexy	0000 Contact: E26AEFB0-1D2D-4ED3-B1E2-B7D352747749:ABPerson
default	20:04:28.113078-0500	Nexy	0000 Contact: AE956307-DB6F-4D84-8479-F99A334DD9D9:ABPerson
default	20:04:28.113082-0500	Nexy	0000 Contact: D85CE9F6-4FD9-4FE4-BAC1-3B143BBF015B:ABPerson
default	20:04:28.113099-0500	Nexy	0000 Contact: D86C98C7-EA2A-4783-9D89-B5CCC7F3F76F:ABPerson
default	20:04:28.113106-0500	Nexy	0000 Contact: 9BD95D2C-57F9-41BC-82A1-01276B837DE5:ABPerson
default	20:04:28.113114-0500	Nexy	0000 Contact: D73A9313-DE0F-415F-AEB6-A3064AD4E8D4:ABPerson
default	20:04:28.113118-0500	Nexy	0000 Contact: 0D652AFC-47EC-4A75-8D39-2C5235F7B2D8:ABPerson
default	20:04:28.113123-0500	Nexy	0000 Contact: ACA1A5BD-6656-45E2-BD86-154568B82D42:ABPerson
default	20:04:28.113128-0500	Nexy	0000 Contact: 4EEB39AF-CB99-4D4F-99E0-813379D86B51:ABPerson
default	20:04:28.113133-0500	Nexy	0000 Contact: 37348E4E-8173-4E70-B552-CB72B6A9AF42:ABPerson
default	20:04:28.113140-0500	Nexy	0000 Contact: 3D23A662-D7CC-4235-A90D-B25C77F75FB1:ABPerson
default	20:04:28.113179-0500	Nexy	0000 Contact: F5DA0315-4AD8-41C4-B7CF-81A2E12E2691:ABPerson
default	20:04:28.113184-0500	Nexy	0000 Contact: 61773524-5763-4829-81ED-9B3EFF5744C8:ABPerson
default	20:04:28.113189-0500	Nexy	0000 Contact: 3A8DC04F-FBB6-495A-8E75-D22B3ACFD775:ABPerson
default	20:04:28.113194-0500	Nexy	0000 Contact: 8E1B53A0-CE9F-4B5A-BCD2-6FCBB2FE03C1:ABPerson
default	20:04:28.113199-0500	Nexy	0000 Contact: 927F81A1-D726-4969-8419-5DAAAB376B20:ABPerson
default	20:04:28.113204-0500	Nexy	0000 Contact: 499571CA-8847-4A36-8AFD-700D10BA01B6:ABPerson
default	20:04:28.113209-0500	Nexy	0000 Contact: 687940D3-01D3-4EE6-8DF6-B77137DF4358:ABPerson
default	20:04:28.113214-0500	Nexy	0000 Contact: AC2B4231-8E18-49D2-A6E0-4DAD10C52F8E:ABPerson
default	20:04:28.113219-0500	Nexy	0000 Contact: B9C8A612-D08C-4C98-AFEC-7B492BFFCF09:ABPerson
default	20:04:28.113224-0500	Nexy	0000 Contact: 4DE12C0D-88F3-46EA-AE7A-52A8C97B2642:ABPerson
default	20:04:28.113229-0500	Nexy	0000 Contact: 74E71AB9-12C3-492C-8D90-44002E96E279:ABPerson
default	20:04:28.113234-0500	Nexy	0000 Contact: F06E384F-51AB-4945-8C9A-CDDA3D1F1726:ABPerson
default	20:04:28.113240-0500	Nexy	0000 Contact: B4392798-7C17-4630-9433-A03FD74A67B6:ABPerson
default	20:04:28.113255-0500	Nexy	0000 Contact: 81B63730-E89B-4309-B937-6526BC363BE9:ABPerson
default	20:04:28.113262-0500	Nexy	0000 Contact: 67260B0D-B185-469D-A099-1F276E9003E9:ABPerson
default	20:04:28.113267-0500	Nexy	0000 Contact: 523939B5-07BC-4BA9-8827-8E5DE74ABD59:ABPerson
default	20:04:28.113272-0500	Nexy	0000 Contact: 448593D9-FFE0-4A5E-85CF-951EBD64FD34:ABPerson
default	20:04:28.113276-0500	Nexy	0000 Contact: 39E0059F-CE32-4A7F-8412-CBB5B8512D91:ABPerson
default	20:04:28.113282-0500	Nexy	0000 Contact: BD79F9BE-48FE-4B17-A966-4900444CB4BE:ABPerson
default	20:04:28.113293-0500	Nexy	0000 Contact: CB117BD9-26BB-482F-BE1D-474050D4F877:ABPerson
default	20:04:28.113298-0500	Nexy	0000 Contact: 1BE44750-F897-4471-B2BB-23F1750F6052:ABPerson
default	20:04:28.113311-0500	Nexy	0000 Contact: F521BF7D-BEA0-4970-8ABB-0D36D0C55CFB:ABPerson
default	20:04:28.113317-0500	Nexy	0000 Contact: B31F68AA-132A-4764-BF9C-07AFF1DFEBE9:ABPerson
default	20:04:28.113332-0500	Nexy	0000 Contact: BFC74FBC-8459-4E5C-926D-CA8CB584E493:ABPerson
default	20:04:28.113337-0500	Nexy	0000 Contact: 513D3922-7269-4052-92B9-A5DDC7F20D85:ABPerson
default	20:04:28.113343-0500	Nexy	0000 Contact: 1680643C-880B-4F66-A23A-54553511F91E:ABPerson
default	20:04:28.113349-0500	Nexy	0000 Contact: AC09AA75-399F-4388-B06D-B36195539921:ABPerson
default	20:04:28.113354-0500	Nexy	0000 Contact: 905AEE60-BF17-4861-8B9D-D8A7C93CA851:ABPerson
default	20:04:28.113363-0500	Nexy	0000 Contact: 605EC366-1BE6-4728-AF4F-35065DDE105E:ABPerson
default	20:04:28.113368-0500	Nexy	0000 Contact: 2E5AC2EB-1D50-48E4-A733-1565B7FBD9B0:ABPerson
default	20:04:28.113379-0500	Nexy	0000 Contact: 8DBBC6C7-2A3B-452A-A683-96B213129365:ABPerson
default	20:04:28.113384-0500	Nexy	0000 Contact: D1ABDE8F-AB3A-4A78-B366-8122520E469C:ABPerson
default	20:04:28.113394-0500	Nexy	0000 Contact: 2BBC7823-B462-47BC-97A1-FAF56A6CD6D4:ABPerson
default	20:04:28.113400-0500	Nexy	0000 Contact: CBBBAAFD-0C8A-4928-B6C5-104BD483B756:ABPerson
default	20:04:28.113406-0500	Nexy	0000 Contact: 7B546412-E513-4FAC-8F04-5B93F8284CD9:ABPerson
default	20:04:28.113416-0500	Nexy	0000 Contact: BEDFD270-E6D5-4BD4-9396-F461E76A3D6D:ABPerson
default	20:04:28.113421-0500	Nexy	0000 Contact: DFF04280-7038-4F29-96DF-CE1264E33F45:ABPerson
default	20:04:28.113472-0500	Nexy	0000 Contact: DA723208-FBEF-435F-9D7D-AF23C3292A04:ABPerson
default	20:04:28.113481-0500	Nexy	0000 Contact: 689B7484-1008-4903-8E58-C16D6135D1BE:ABPerson
default	20:04:28.113487-0500	Nexy	0000 Contact: 2EBB3BBB-AA1B-44AB-AEB2-507047DFB1BF:ABPerson
default	20:04:28.113493-0500	Nexy	0000 Contact: 2C4816A3-74B3-44EE-8613-D4A9EA487364:ABPerson
default	20:04:28.113497-0500	Nexy	0000 Contact: 327FE41D-07EB-426D-B40A-C41E6414A032:ABPerson
default	20:04:28.113502-0500	Nexy	0000 Contact: 661E42B6-4641-42DC-ADAD-F2F4F64E9A7F:ABPerson
default	20:04:28.113507-0500	Nexy	0000 Contact: 5B3F5B1B-AEB4-49F2-9295-98A6D2E90DF3:ABPerson
default	20:04:28.113512-0500	Nexy	0000 Contact: 3B9A0F65-3862-4239-9B4C-22A3937CB3E3:ABPerson
default	20:04:28.113517-0500	Nexy	0000 Contact: 1F5296B1-D8A8-4DEE-A3AC-4F6FF8EB8592:ABPerson
default	20:04:28.113521-0500	Nexy	0000 Contact: 83367917-4C48-420D-BED6-953D5D799BA3:ABPerson
default	20:04:28.113526-0500	Nexy	0000 Contact: CB81A645-AA3F-4E01-A5E8-7FFB1DE784B8:ABPerson
default	20:04:28.113531-0500	Nexy	0000 Contact: 76C1E860-76F6-46A7-AE8B-0B8D533979A1:ABPerson
default	20:04:28.113535-0500	Nexy	0000 Contact: 38D87E84-8FFA-4644-89BB-3B2C64683F25:ABPerson
default	20:04:28.113540-0500	Nexy	0000 Contact: BFC89011-6208-402B-902D-227391CF84D7:ABPerson
default	20:04:28.113547-0500	Nexy	0000 Contact: AE1E272C-12CF-4D37-AA16-321C66EB1922:ABPerson
default	20:04:28.113552-0500	Nexy	0000 Contact: 37AF5276-1B9C-4873-9D80-6BD7C5AE160B:ABPerson
default	20:04:28.113555-0500	Nexy	0000 Contact: 873FBA93-2932-4885-9ABA-B766E56EF823:ABPerson
default	20:04:28.113584-0500	Nexy	0000 Contact: DA14AB47-A56B-4F79-A505-4A5F3CF9709B:ABPerson
default	20:04:28.113590-0500	Nexy	0000 Contact: 5DBDC986-75E3-45D5-BDAC-840F64A095F3:ABPerson
default	20:04:28.113595-0500	Nexy	0000 Contact: 7E2E667C-A7D1-4A88-9C92-C2F38557DF00:ABPerson
default	20:04:28.113599-0500	Nexy	0000 Contact: 5307FC68-117A-42FB-92AA-DFB24F94E71D:ABPerson
default	20:04:28.113604-0500	Nexy	0000 Contact: 5F493737-ED28-4B1F-8903-5BA4CE98E525:ABPerson
default	20:04:28.113607-0500	Nexy	0000 Contact: 581AB38B-88DC-4442-B96C-20827400BCDB:ABPerson
default	20:04:28.113614-0500	Nexy	0000 Contact: E7A269EB-3583-4C11-9FA2-A805E372821C:ABPerson
default	20:04:28.113617-0500	Nexy	0000 Contact: 17A33554-E561-4BBD-9CEB-2A42D78570CB:ABPerson
default	20:04:28.113625-0500	Nexy	0000 Contact: B6294A95-D955-4DE1-981A-1C81A88B3C77:ABPerson
default	20:04:28.113630-0500	Nexy	0000 Contact: 2775B95B-E344-4E6E-860A-2E7C048D2F1D:ABPerson
default	20:04:28.113640-0500	Nexy	0000 Contact: C811339F-FA52-4CA4-B33E-D0F308EB497B:ABPerson
default	20:04:28.113656-0500	Nexy	0000 Contact: 3EBCE39A-CFA0-4AE5-A027-E77300906D8C:ABPerson
default	20:04:28.113662-0500	Nexy	0000 Contact: EE34E8D6-8FA8-43EA-956D-B93BBAEE1A85:ABPerson
default	20:04:28.113667-0500	Nexy	0000 Contact: 9502BE8E-CE6C-45C1-B06E-06F25C1B2DB2:ABPerson
default	20:04:28.113672-0500	Nexy	0000 Contact: CB72BAE7-75D4-4B69-B8B1-6F54BA25195A:ABPerson
default	20:04:28.113677-0500	Nexy	0000 Contact: 8ABDA833-5BB8-43D2-9DD4-D9977041708F:ABPerson
default	20:04:28.113688-0500	Nexy	0000 Contact: BC7FC3F8-6E58-42C6-8D38-58B4E05E74D8:ABPerson
default	20:04:28.113699-0500	Nexy	0000 Contact: 8C9E4B42-EDDD-4DA5-8291-79608D7118FD:ABPerson
default	20:04:28.113707-0500	Nexy	0000 Contact: 88A354D2-628D-4BBD-A9D2-4025114C2B74:ABPerson
default	20:04:28.113712-0500	Nexy	0000 Contact: D671E4A8-5C78-48DB-9F39-C9F55D0773F0:ABPerson
default	20:04:28.113717-0500	Nexy	0000 Contact: B55652C2-FF9A-492E-9E74-59BF77FF7657:ABPerson
default	20:04:28.113740-0500	Nexy	0000 Contact: D40BEEF6-659C-4640-8883-A886679E7683:ABPerson
default	20:04:28.113746-0500	Nexy	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	20:04:28.113751-0500	Nexy	0000 Contact: 2501625C-D3F0-448F-BE59-758CB4781991:ABPerson
default	20:04:28.113756-0500	Nexy	0000 Contact: 95793C06-46A7-463F-B79D-BD4828AA82E5:ABPerson
default	20:04:28.113760-0500	Nexy	0000 Contact: 39FB6543-CE8F-4850-B087-CB9BC9D83CD1:ABPerson
default	20:04:28.113765-0500	Nexy	0000 Contact: 4899EBC6-6B1B-4110-ACC0-42C6281F11F0:ABPerson
default	20:04:28.113770-0500	Nexy	0000 Contact: 2152007E-EC7F-40ED-A920-334BFEE05F62:ABPerson
default	20:04:28.113781-0500	Nexy	0000 Contact: E5FB73BD-A112-4CB1-A44C-4AE9AA8A7FD9:ABPerson
default	20:04:28.113787-0500	Nexy	0000 Contact: 9DF4B53B-8E66-438F-A541-31A6AC43028E:ABPerson
default	20:04:28.113797-0500	Nexy	0000 Contact: ED52C6FA-B011-454D-BF73-CD97015FEDF8:ABPerson
default	20:04:28.113805-0500	Nexy	0000 Contact: 637D6BED-2C4A-4F5E-9BF9-E5A8854E4DF1:ABPerson
default	20:04:28.113814-0500	Nexy	0000 Contact: 763CD797-4630-439F-982D-34ACFA2E7238:ABPerson
default	20:04:28.113818-0500	Nexy	0000 Contact: DE4A7BAA-4835-447E-9B59-F863ACBFA092:ABPerson
default	20:04:28.113830-0500	Nexy	0000 Contact: FE3ED792-5C16-4CA6-AD68-BBDFDF93EAC3:ABPerson
default	20:04:28.113838-0500	Nexy	0000 Contact: F5F336E5-374B-4E45-B851-690629571134:ABPerson
default	20:04:28.113845-0500	Nexy	0000 Contact: 00E52FC0-B1F1-47C4-A4E2-351A2927B2AC:ABPerson
default	20:04:28.113853-0500	Nexy	0000 Contact: 5AA6919D-04C9-470A-99B9-9FB0D437DA6A:ABPerson
default	20:04:28.113859-0500	Nexy	0000 Contact: 1FC22462-8E84-43E6-8F68-5D141CC903D6:ABPerson
default	20:04:28.113871-0500	Nexy	0000 Contact: 379EEF06-D880-4C4C-81B4-19232497B238:ABPerson
default	20:04:28.113881-0500	Nexy	0000 Contact: 9AA12C79-AC0F-40D8-82D4-7D1D1B6024D4:ABPerson
default	20:04:28.113886-0500	Nexy	0000 Contact: B584C21D-4B54-4F37-A1B1-B5EF3AEC170C:ABPerson
default	20:04:28.113894-0500	Nexy	0000 Contact: D2940461-BB6C-4224-8218-88019B5DB07D:ABPerson
default	20:04:28.113900-0500	Nexy	0000 Contact: 734CE2EC-7CFA-4475-B601-8F5A0EDC5AFC:ABPerson
default	20:04:28.113912-0500	Nexy	0000 Contact: 693CFFC7-F57A-478E-BBA2-CB65EB6C5425:ABPerson
default	20:04:28.113920-0500	Nexy	0000 Contact: 522D9347-0C39-4479-9A87-99551E9F992C:ABPerson
default	20:04:28.113925-0500	Nexy	0000 Contact: BC6A800E-2E2E-4B39-B37E-6639FBEE75EF:ABPerson
default	20:04:28.113935-0500	Nexy	0000 Contact: 4B6CD270-FA88-4F64-9F96-22BB79CBD541:ABPerson
default	20:04:28.113940-0500	Nexy	0000 Contact: 77ED343F-8BF8-4BFD-A0F9-901367A608BC:ABPerson
default	20:04:28.113950-0500	Nexy	0000 Contact: 37D2B9B0-053A-474C-BE44-09B4453D4050:ABPerson
default	20:04:28.113956-0500	Nexy	0000 Contact: 62B0EB86-C5BA-495C-9E28-535D2EF0354A:ABPerson
default	20:04:28.113965-0500	Nexy	0000 Contact: 670ECAAE-6CD8-4A3A-8EA6-614A11174BD6:ABPerson
default	20:04:28.113987-0500	Nexy	0000 Contact: A45DAD74-F719-4D46-9EA6-6DFEEF650375:ABPerson
default	20:04:28.114000-0500	Nexy	0000 Contact: B7008B2E-FA86-42D5-8656-CE248026D27E:ABPerson
default	20:04:28.114005-0500	Nexy	0000 Contact: 66B98153-BD62-4141-BD1F-DADC79D75A4F:ABPerson
default	20:04:28.114010-0500	Nexy	0000 Contact: FA38B842-F2F3-4FED-B33D-A5010D4304B0:ABPerson
default	20:04:28.114017-0500	Nexy	0000 Contact: 14743D61-F4A1-4392-9E1B-26918104BF14:ABPerson
default	20:04:28.114023-0500	Nexy	0000 Contact: B2D8BD53-113A-4BF0-91CA-D5DEB28674B5:ABPerson
default	20:04:28.114028-0500	Nexy	0000 Contact: 64B8389E-447B-4C35-B14E-8146CA91B47B:ABPerson
default	20:04:28.114032-0500	Nexy	0000 Contact: 3FF7B769-C140-4D4C-B32F-6B8F440DE2D8:ABPerson
default	20:04:28.114037-0500	Nexy	0000 Contact: 1F6916A9-1A84-48F4-B955-59E227D8C9DF:ABPerson
default	20:04:28.114042-0500	Nexy	0000 Contact: F334D708-4AFD-4933-99D2-F8F1D76176A9:ABPerson
default	20:04:28.114047-0500	Nexy	0000 Contact: 626EC525-A04F-4FBF-8FEE-BA93D0436808:ABPerson
default	20:04:28.114052-0500	Nexy	0000 Contact: A4D2F572-E7C4-45EE-AE51-345CC039C259:ABPerson
default	20:04:28.114058-0500	Nexy	0000 Contact: 014698F9-DA96-407C-A1B8-DEC6B51A33F6:ABPerson
default	20:04:28.114068-0500	Nexy	0000 Contact: F5B2550B-7B88-4DCE-A7A3-1B10271953FC:ABPerson
default	20:04:28.114073-0500	Nexy	0000 Contact: 1EAD0F34-5228-476C-B4EB-ACD91782DD85:ABPerson
default	20:04:28.114111-0500	Nexy	0000 Contact: F7E0D308-2E0A-49CC-849B-C883B6F8730F:ABPerson
default	20:04:28.114120-0500	Nexy	0000 Contact: 145A9F4B-B827-49A2-B108-81359AEE2B8F:ABPerson
default	20:04:28.114125-0500	Nexy	0000 Contact: 0AA46F26-7B70-4230-AC5B-AFDC6D2DD22B:ABPerson
default	20:04:28.114130-0500	Nexy	0000 Contact: AE79C4EC-990E-4BA3-913E-7C842EB653EF:ABPerson
default	20:04:28.114135-0500	Nexy	0000 Contact: C05B9998-16AE-4F34-8E4F-817C3D9B8EC6:ABPerson
default	20:04:28.114140-0500	Nexy	0000 Contact: 7F27B5B3-D0F5-483F-89C6-8B9931845E1F:ABPerson
default	20:04:28.114145-0500	Nexy	0000 Contact: 84E58627-BCB4-42D0-BDFA-EE699F5FBDD8:ABPerson
default	20:04:28.114151-0500	Nexy	0000 Contact: 2513C61B-7EFC-4A92-88AB-DF9479B99E6A:ABPerson
default	20:04:28.114156-0500	Nexy	0000 Contact: 84CFF237-6D8B-4620-9181-D1B4BB0809EE:ABPerson
default	20:04:28.114161-0500	Nexy	0000 Contact: 0BFD29DC-60C9-4B71-9D65-4ADA47472277:ABPerson
default	20:04:28.114166-0500	Nexy	0000 Contact: 69998C87-7B1A-45AA-ABB3-2D84128DD9EE:ABPerson
default	20:04:28.114170-0500	Nexy	0000 Contact: A7C3EEE8-11F8-4C0C-848D-3AC49C688578:ABPerson
default	20:04:28.114175-0500	Nexy	0000 Contact: A64A1E7E-C301-454E-A9A9-D685C82EF693:ABPerson
default	20:04:28.114181-0500	Nexy	0000 Contact: 91C379A3-DE9D-456A-A6AD-0F1F963582E7:ABPerson
default	20:04:28.114190-0500	Nexy	0000 Contact: 6ACE0F8B-171F-450C-83E2-081B5F26881E:ABPerson
default	20:04:28.114200-0500	Nexy	0000 Contact: AC074808-2D0D-48F8-8B23-3F0CA6D51D26:ABPerson
default	20:04:28.114204-0500	Nexy	0000 Contact: F4F5D7A0-BC90-4C27-BBCE-BE969384F1C0:ABPerson
default	20:04:28.114211-0500	Nexy	0000 Contact: 1ABDAACE-D0B1-4F9B-96D1-DC2C524CE1C6:ABPerson
default	20:04:28.114219-0500	Nexy	0000 Contact: 43585BE0-779A-4596-A518-8D5E4ADB3D19:ABPerson
default	20:04:28.114229-0500	Nexy	0000 Contact: 67051D02-C728-4665-B5FC-4F1B269F02BD:ABPerson
default	20:04:28.114236-0500	Nexy	0000 Contact: 4473A678-C9E7-4D62-84E0-753DF60913D1:ABPerson
default	20:04:28.114244-0500	Nexy	0000 Contact: D56AB0C8-7D93-4C12-B5B5-95E0DC8F2240:ABPerson
default	20:04:28.114249-0500	Nexy	0000 Contact: 9579BC4C-AF0F-4D50-A15C-319AACBFC2A5:ABPerson
default	20:04:28.114259-0500	Nexy	0000 Contact: 4BE75408-838B-4CDE-A088-588AE1E78C84:ABPerson
default	20:04:28.114265-0500	Nexy	0000 Contact: C87BCEEB-0D99-4BCD-B837-B1790FEF5A35:ABPerson
default	20:04:28.114274-0500	Nexy	0000 Contact: 11C070CC-DE86-43A2-AC2E-BD5D0E666C75:ABPerson
default	20:04:28.114284-0500	Nexy	0000 Contact: 1BC6C401-C80C-443B-86A1-DE142581F385:ABPerson
default	20:04:28.114289-0500	Nexy	0000 Contact: 0A5F3B64-AC92-4AC6-A80F-C08A85FC26AF:ABPerson
default	20:04:28.114299-0500	Nexy	0000 Contact: 87E03F74-07D8-4C64-9DA7-D99DC9CA7445:ABPerson
default	20:04:28.114305-0500	Nexy	0000 Contact: 94F55698-438B-4D8C-9CA0-71DDFD6367D5:ABPerson
default	20:04:28.114310-0500	Nexy	0000 Contact: 15748416-FFAD-4D4B-B4AF-076BF4C1B672:ABPerson
default	20:04:28.114321-0500	Nexy	0000 Contact: 74B3EEDB-C36E-4B91-AAF8-A7D433556574:ABPerson
default	20:04:28.114326-0500	Nexy	0000 Contact: 951A73EB-D920-4420-8258-81B51426DEF7:ABPerson
default	20:04:28.114342-0500	Nexy	0000 Contact: 6B194999-7994-412B-8F16-25AB9317AAB4:ABPerson
default	20:04:28.114347-0500	Nexy	0000 Contact: 2EC20223-DCBF-406A-9D39-5F1D770A8BC4:ABPerson
default	20:04:28.114353-0500	Nexy	0000 Contact: 1562F9E4-94A8-48AB-BF2B-C1EB0C1BE5A4:ABPerson
default	20:04:28.114360-0500	Nexy	0000 Contact: F6C3B173-427B-4C46-AA87-E8AA5B4E4C47:ABPerson
default	20:04:28.114368-0500	Nexy	0000 Contact: 5340250A-2C48-4FA9-9A43-1E9438F76204:ABPerson
default	20:04:28.114376-0500	Nexy	0000 Contact: 910FA8BF-611B-4C75-9EB0-5F2EFD716C1F:ABPerson
default	20:04:28.114403-0500	Nexy	0000 Contact: 08B0DE06-259B-449C-B66B-FFBA5AB8D812:ABPerson
default	20:04:28.114429-0500	Nexy	0000 Contact: 3C20B58D-2CA5-485E-A9A6-F77768532665:ABPerson
default	20:04:28.114437-0500	Nexy	0000 Contact: 6524FEA4-C209-419D-8A29-C534C9D1627C:ABPerson
default	20:04:28.114443-0500	Nexy	0000 Contact: 9A063C74-04C9-4AD8-AB36-6C8734D43E2D:ABPerson
default	20:04:28.114448-0500	Nexy	0000 Contact: AEAB4360-3F45-4F6B-9F79-B5D0B38B9A81:ABPerson
default	20:04:28.114453-0500	Nexy	0000 Contact: 044C1B1D-1FA6-46AA-B69A-444A8B442B7C:ABPerson
default	20:04:28.114458-0500	Nexy	0000 Contact: 67E45E85-4716-4AD1-9FE5-0DD5A68A6D7E:ABPerson
default	20:04:28.114461-0500	Nexy	0000 Contact: 4ADAEDF0-6C5E-4C06-9C0A-B8594FF82BDA:ABPerson
default	20:04:28.114465-0500	Nexy	0000 Contact: DA46038B-56C6-4414-9F21-077B66E8C91C:ABPerson
default	20:04:28.114470-0500	Nexy	0000 Contact: 75FADFA1-F7C3-437C-8B58-DAA8A4B54442:ABPerson
default	20:04:28.114475-0500	Nexy	0000 Contact: B6E3347E-7AC5-41E7-ACA5-D2CEF067A1CA:ABPerson
default	20:04:28.114480-0500	Nexy	0000 Contact: 4EFFE145-11B7-42A5-822C-A4BAB5D83906:ABPerson
default	20:04:28.114485-0500	Nexy	0000 Contact: EAB298D5-435C-4D40-83A7-2C55723A0BFD:ABPerson
default	20:04:28.114490-0500	Nexy	0000 Contact: B0D78C24-E588-4901-88A7-6B1BB429B840:ABPerson
default	20:04:28.114494-0500	Nexy	0000 Contact: 1CB20B90-D9D5-4C8F-9AB0-DAA44D00BDD4:ABPerson
default	20:04:28.114499-0500	Nexy	0000 Contact: 527699A5-81B2-4D67-AEED-D6EED43F9044:ABPerson
default	20:04:28.114504-0500	Nexy	0000 Contact: CB5E53D4-5C8B-43F5-94AF-6B7D8BA543FD:ABPerson
default	20:04:28.114507-0500	Nexy	0000 Contact: 04598613-6173-4B93-B8E7-285BC4F3D8E8:ABPerson
default	20:04:28.114512-0500	Nexy	0000 Contact: ADD86E64-7CF0-4510-AD39-66BD6BD079BC:ABPerson
default	20:04:28.114520-0500	Nexy	0000 Contact: 32788248-0C60-4FEA-85E7-FA758B61DD1D:ABPerson
default	20:04:28.114531-0500	Nexy	0000 Contact: AA1A4C67-F155-4EE5-9010-31149EE1E39C:ABPerson
default	20:04:28.114537-0500	Nexy	0000 Contact: 961DCC0E-AAAD-4D01-9678-0A7621D2AFB0:ABPerson
default	20:04:28.114547-0500	Nexy	0000 Contact: 66B11FA1-1DE3-48ED-A067-665E7467482A:ABPerson
default	20:04:28.114559-0500	Nexy	0000 Contact: F5182AF8-32D2-40E6-993D-C0489EBC89E4:ABPerson
default	20:04:28.114566-0500	Nexy	0000 Contact: 0D60E67B-3CE2-4AA5-A3A7-78022070A092:ABPerson
default	20:04:28.114583-0500	Nexy	0000 Contact: 3AAC52F8-BF6B-4AF2-BB6D-03A1310B24E5:ABPerson
default	20:04:28.114592-0500	Nexy	0000 Contact: CE41D8E9-94C5-4D35-9B34-26811B12C410:ABPerson
default	20:04:28.114597-0500	Nexy	0000 Contact: F13294CA-A587-43D6-B693-775C43EE2187:ABPerson
default	20:04:28.114604-0500	Nexy	0000 Contact: 89FE41AC-035D-4508-9B13-A7A61A86A77D:ABPerson
default	20:04:28.114612-0500	Nexy	0000 Contact: 31E21B40-260C-42C1-9677-7C97CC1B201D:ABPerson
default	20:04:28.114615-0500	Nexy	0000 Contact: F0D80C37-667F-495B-83CE-9F5BF918C730:ABPerson
default	20:04:28.114620-0500	Nexy	0000 Contact: 06259E4E-E4B7-4654-BF6B-33F4F0FCB23A:ABPerson
default	20:04:28.114625-0500	Nexy	0000 Contact: 55FDAC9D-D436-4535-BE96-A71F62A0AF9E:ABPerson
default	20:04:28.114630-0500	Nexy	0000 Contact: F790FA9D-7B36-4AEA-8012-0BDEED54CF62:ABPerson
default	20:04:28.114635-0500	Nexy	0000 Contact: 276E4846-224E-4119-AB43-FE2E963D133E:ABPerson
default	20:04:28.114651-0500	Nexy	0000 Contact: DB25F4B4-E218-42CD-959A-C88098B61FD4:ABPerson
default	20:04:28.114656-0500	Nexy	0000 Contact: 7E8FC80C-607C-43E2-BF92-C5FCC8403326:ABPerson
default	20:04:28.114661-0500	Nexy	0000 Contact: 6BE779B6-7D7F-4DB2-A36A-3696730156FE:ABPerson
default	20:04:28.114666-0500	Nexy	0000 Contact: A45B54DD-B6FC-4653-84D5-0757EB2F2ED6:ABPerson
default	20:04:28.114671-0500	Nexy	0000 Contact: 8605C2C8-7153-4112-9036-FAA472B7FD44:ABPerson
default	20:04:28.114677-0500	Nexy	0000 Contact: CD272F42-E884-45F1-84C3-CFD3A0B1BF35:ABPerson
default	20:04:28.114689-0500	Nexy	0000 Contact: 4D2116D6-A645-48BB-B220-E9ED03C71748:ABPerson
default	20:04:28.114695-0500	Nexy	0000 Contact: B502B3DD-9E9D-4150-B4A9-4872364793EF:ABPerson
default	20:04:28.114723-0500	Nexy	0000 Contact: 0C360F68-EDE2-457E-AC4B-ACE762AD5BD0:ABPerson
default	20:04:28.114728-0500	Nexy	0000 Contact: FF4175C6-26DF-47BC-BF00-2E75EEE8B1FD:ABPerson
default	20:04:28.114734-0500	Nexy	0000 Contact: 09A457F3-A9F4-4F24-9B11-9FA58D4C1508:ABPerson
default	20:04:28.114739-0500	Nexy	0000 Contact: B89DEF47-D413-46AD-BAEA-7D496DD46FB1:ABPerson
default	20:04:28.114743-0500	Nexy	0000 Contact: 3598E3CB-8A76-4D70-AC49-D3EB37CA2029:ABPerson
default	20:04:28.114748-0500	Nexy	0000 Contact: AA991FC9-EB3D-43B4-8CBD-8E604A09B637:ABPerson
default	20:04:28.114753-0500	Nexy	0000 Contact: CC5195D6-422A-4FB7-B9EE-A2A04E601EC0:ABPerson
default	20:04:28.114764-0500	Nexy	0000 Contact: B569062E-A03D-4DD9-A53C-5D2D8D57CB4B:ABPerson
default	20:04:28.114768-0500	Nexy	0000 Contact: 73B6BD20-2014-4F01-90D9-4428F13B690A:ABPerson
default	20:04:28.114779-0500	Nexy	0000 Contact: AA3A3E50-90A8-4525-8DAA-B8B4FADD18DA:ABPerson
default	20:04:28.114785-0500	Nexy	0000 Contact: 3BAE7091-1579-47D0-B90D-0D3CF681C569:ABPerson
default	20:04:28.114795-0500	Nexy	0000 Contact: 56A226DF-9ECE-4143-BA65-8AD0B646C7CB:ABPerson
default	20:04:28.114800-0500	Nexy	0000 Contact: 50F1ED96-0C6B-4F81-AA14-43DC6EBECD59:ABPerson
default	20:04:28.114818-0500	Nexy	0000 Contact: 5A494BDA-3B74-4B7B-92A5-ADDBE7FB8C87:ABPerson
default	20:04:28.114825-0500	Nexy	0000 Contact: 6BD609FD-5007-4D59-A4EF-493CADDB85B2:ABPerson
default	20:04:28.114830-0500	Nexy	0000 Contact: 7E64D4B3-BC6D-4959-B7A0-E823B049142C:ABPerson
default	20:04:28.114834-0500	Nexy	0000 Contact: 621AF0D1-3352-4F82-9C69-D6B0F8D4F5A9:ABPerson
default	20:04:28.114839-0500	Nexy	0000 Contact: 4E051A3F-F33F-42F6-A635-4F6B6FEFCFB2:ABPerson
default	20:04:28.114845-0500	Nexy	0000 Contact: 30F7C290-B84E-45EF-8777-D14EBB9D4BB1:ABPerson
default	20:04:28.114860-0500	Nexy	0000 Contact: B489EA28-72B0-4D87-8E65-2FCC5266CCBB:ABPerson
default	20:04:28.114865-0500	Nexy	0000 Contact: E5C00A28-C49D-4782-B544-D726CFE29EF0:ABPerson
default	20:04:28.114870-0500	Nexy	0000 Contact: DA65C871-7E16-4359-B34C-C5906692C623:ABPerson
default	20:04:28.114878-0500	Nexy	0000 Contact: 5BAFBA23-8FAE-41B7-86D6-A6B3DB070404:ABPerson
default	20:04:28.114883-0500	Nexy	0000 Contact: EA0D316B-758E-4C59-B0A6-6FFB7AD3E09F:ABPerson
default	20:04:28.114893-0500	Nexy	0000 Contact: 9BD347CB-8966-4118-92F7-D6D42F5F8C7C:ABPerson
default	20:04:28.114901-0500	Nexy	0000 Contact: 018F45A5-C534-4FC0-871A-DB5567A8D78E:ABPerson
default	20:04:28.114911-0500	Nexy	0000 Contact: 9FC18618-FB9D-4960-8474-07F6A0D062F8:ABPerson
default	20:04:28.114916-0500	Nexy	0000 Contact: C8BDDDAE-C009-4DB9-B3FC-01F3B16C6D25:ABPerson
default	20:04:28.114927-0500	Nexy	0000 Contact: 1D0198ED-A6C3-4B64-AA1A-2E8A8C4A0172:ABPerson
default	20:04:28.114932-0500	Nexy	0000 Contact: 3BD67570-1034-422C-85A2-6F28BE24C33A:ABPerson
default	20:04:28.114943-0500	Nexy	0000 Contact: D75A5B27-BD0C-4D34-AC6B-FC2822769519:ABPerson
default	20:04:28.114948-0500	Nexy	0000 Contact: 6B5F7DDD-1E04-453D-8539-4B54A251117A:ABPerson
default	20:04:28.114958-0500	Nexy	0000 Contact: 49E369CD-B10E-4CD5-B030-5393AB2ADE18:ABPerson
default	20:04:28.115030-0500	Nexy	0000 Contact: A9AB0613-621A-427C-9150-83893BA072C5:ABPerson
default	20:04:28.115037-0500	Nexy	0000 Contact: 9B8281D5-C780-436F-988A-96C01722B038:ABPerson
default	20:04:28.115070-0500	Nexy	0000 FINISH (23.3 ms)
default	20:04:28.125760-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:04:28.125864-0500	runningboardd	Invalidating assertion 403-672-16460 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:04:28.229897-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:28.229911-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:28.229922-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:28.229940-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:28.233273-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:28.233669-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.233788-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.397197-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7075] from originator [osservice<com.apple.WindowServer(88)>:397] with description <RBSAssertionDescriptor| "AppDrawing" ID:403-397-16468 target:7075 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:28.397363-0500	runningboardd	Assertion 403-397-16468 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7075]) will be created as active
default	20:04:28.397761-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring jetsam update because this process is not memory-managed
default	20:04:28.397774-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring suspend because this process is not lifecycle managed
default	20:04:28.397784-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring GPU update because this process is not GPU managed
default	20:04:28.397803-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] Ignoring memory limit update because this process is not memory-managed
default	20:04:28.401937-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:28.402368-0500	ControlCenter	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.402523-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:28.785388-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x11d11d (Nexy) connectionID: FE307 pid: 7075 in session 0x101
default	20:04:28.785500-0500	WindowServer	<BSCompoundAssertion:0x9d2c09580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x11d11d (Nexy) acq:0x9cfaa2560 count:1
default	20:04:28.790530-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1fe015","name":"Nexy(7075)"}, "details":null }
default	20:04:28.790623-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1fe015 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":7075})
default	20:04:28.790649-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":7075})
default	20:04:28.791229-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:04:28.791495-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 7075, Name = sid:0x1fe015, Nexy(7075), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:04:28.791625-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.791289-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Workspace connection invalidated.
default	20:04:28.791428-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Now flagged as pending exit for reason: workspace client connection invalidated
default	20:04:28.791770-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.791878-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.791949-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.791342-0500	WindowManager	Connection invalidated | (7075) Nexy
default	20:04:28.793025-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x11d11d removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x11d11d (Nexy)"
)}
default	20:04:28.793683-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1ba3 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x11d11d (Nexy)"
)}
default	20:04:28.802120-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.802217-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:28.802978-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:04:28.803231-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:04:28.806772-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.810333-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:04:28.810365-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_970.898.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:04:28.819969-0500	mDNSResponder	[R21732] DNSServiceCreateConnection STOP PID[7075](Nexy)
default	20:04:28.820730-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7075] termination reported by launchd (0, 0, 0)
default	20:04:28.820811-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.821161-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.821346-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.821399-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.829462-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: none (role: NonUserInteractive) (endowments: (null))
default	20:04:28.829849-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: none (role: NonUserInteractive) (endowments: (null))
default	20:04:28.829827-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Process exited: <RBSProcessExitContext| voluntary>.
default	20:04:28.829853-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Setting process task state to: Not Running
default	20:04:28.829878-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 7075, name = Nexy
default	20:04:28.829864-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Setting process visibility to: Unknown
default	20:04:28.829905-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7075] Invalidating workspace.
default	20:04:28.829932-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.830455-0500	ControlCenter	Removing: <FBApplicationProcess: 0xcc0135980; app<application.com.nexy.assistant.53705040.53705049>:7075(v34BD4)>
default	20:04:28.833005-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-7075)
default	20:04:28.834752-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(EF6BC690) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-7075)
default	20:04:28.834868-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(EF6BC690, (bid:com.nexy.assistant-Item-0-7075))]
default	20:04:28.839623-0500	launchservicesd	Hit the server for a process handle 1a89d7a600001ba3 that resolved to: [app<application.com.nexy.assistant.53705040.53705049(501)>:7075]
default	20:04:28.839660-0500	gamepolicyd	Received state update for 7075 (app<application.com.nexy.assistant.53705040.53705049(501)>, none-NotVisible
default	20:04:28.844686-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x11d11d} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:04:28.844722-0500	loginwindow	-[Application setState:] | enter: <Application: 0x897ae0320: Nexy> state 3
default	20:04:28.844741-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:04:28.845813-0500	loginwindow	-[Application setState:] | enter: <Application: 0x897ae0320: Nexy> state 4
default	20:04:28.845823-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:04:29.942127-0500	runningboardd	Invalidating assertion 403-672-16457 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:04:30.045394-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:04:30.052053-0500	gamepolicyd	Received state update for -1 (app<application.com.nexy.assistant.53705040.53705049(501)>, none-NotVisible
default	20:04:31.917658-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	20:04:32.001347-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:04:32.001516-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:04:32.003495-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:04:32.009921-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:04:32.012279-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53705040.53705049(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:04:32.012347-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53705040.53705049(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:587] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-587-16469 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:04:32.012419-0500	runningboardd	Assertion 403-587-16469 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) will be created as active
default	20:04:32.016016-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:04:32.016063-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:04:32.016074-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:04:32.016149-0500	runningboardd	app<application.com.nexy.assistant.53705040.53705049(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	20:04:32.027785-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] is not RunningBoard jetsam managed.
default	20:04:32.027798-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] This process will not be managed.
default	20:04:32.027812-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:32.027986-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:32.028626-0500	gamepolicyd	Hit the server for a process handle f46f8ad00001c31 that resolved to: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:32.028670-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:32.031636-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:32.031699-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-16470 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:32.031833-0500	runningboardd	Assertion 403-403-16470 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:32.032021-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:32.032043-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:32.032062-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Set darwin role to: UserInteractive
default	20:04:32.032073-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:32.032089-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:32.032139-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] reported to RB as running
default	20:04:32.033581-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:7217" ID:403-367-16471 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:04:32.033684-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x146146 com.nexy.assistant starting stopped process.
default	20:04:32.033870-0500	runningboardd	Assertion 403-367-16471 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:32.034655-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:32.034790-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:04:32.034681-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:32.034703-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:32.034960-0500	loginwindow	-[Application setState:] | enter: <Application: 0x897ae0320: Nexy> state 2
default	20:04:32.034807-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:32.034984-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:04:32.034981-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:32.037889-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:32.038288-0500	runningboardd	Invalidating assertion 403-587-16469 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:587]
default	20:04:32.038328-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:32.038347-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:32.038366-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:32.038455-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:32.038464-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:32.042648-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:32.048391-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:32.084305-0500	logger	detected new pid 7217 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:32.114095-0500	Nexy	[0x1028f4b00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:04:32.114171-0500	Nexy	[0x1028f5040] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:04:32.140239-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:32.143218-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:32.143232-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:32.143244-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:32.143261-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:32.146729-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:32.147280-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
error	20:04:32.246208-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1028e5f80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:04:32.246475-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1028e5f80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:04:32.249248-0500	Nexy	[0x102902000] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:04:32.250281-0500	Nexy	[0xabf638000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:04:32.254076-0500	Nexy	[0xabf6383c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:04:32.254936-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7217.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:32.259035-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:32.286767-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.821, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:32.286861-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:32.322313-0500	Nexy	CHECKIN: pid=7217
default	20:04:32.333921-0500	Nexy	CHECKEDIN: pid=7217 asn=0x0-0x146146 foreground=0
default	20:04:32.333728-0500	launchservicesd	CHECKIN:0x0-0x146146 7217 com.nexy.assistant
default	20:04:32.340631-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:7217" ID:403-367-16481 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:04:32.340769-0500	runningboardd	Assertion 403-367-16481 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:32.352062-0500	runningboardd	Invalidating assertion 403-367-16471 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	20:04:32.358587-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:04:32.361711-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:04:32.362759-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:04:32.367364-0500	Nexy	Initializing connection
default	20:04:32.367429-0500	Nexy	Removing all cached process handles
default	20:04:32.368942-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] as ready
default	20:04:32.367556-0500	Nexy	Sending handshake request attempt #1 to server
default	20:04:32.367580-0500	Nexy	Creating connection to com.apple.runningboard
default	20:04:32.367594-0500	Nexy	[0xabf638780] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:04:32.370008-0500	Nexy	Handshake succeeded
default	20:04:32.370032-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:04:32.382019-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:04:32.382196-0500	Nexy	[0xabf638a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:04:33.503096-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0EFBE578-8659-4AA4-9B7F-72ABE96A6BC8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57961,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xecc75fe7 tp_proto=0x06"
default	20:04:33.503220-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57961<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208961 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x919f6fab
default	20:04:38.011176-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-16470 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217])
default	20:04:38.070986-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:38.071018-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:38.071043-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:38.071090-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:38.077292-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:38.077972-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:38.504256-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57961<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208961 t_state: SYN_SENT process: Nexy:7217 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x919f6fab
default	20:04:38.504288-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57961<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208961 t_state: SYN_SENT process: Nexy:7217 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:04:38.504993-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6E0BF157-0200-4CEA-BDC5-2707ECF2E4E0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57962,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5210b565 tp_proto=0x06"
default	20:04:38.505151-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57962<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208972 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x948b9614
default	20:04:42.696120-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:04:43.367475-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:04:43.504940-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57962<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208972 t_state: SYN_SENT process: Nexy:7217 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x948b9614
default	20:04:43.504966-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57962<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208972 t_state: SYN_SENT process: Nexy:7217 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:04:43.508476-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:04:43.508703-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:04:43.510165-0500	Nexy	nw_path_libinfo_path_check [9C972432-630B-44FB-BC2C-2B9D4BD9EBBF Hostname#619365cb:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:04:43.510739-0500	mDNSResponder	[R21915] DNSServiceCreateConnection START PID[7217](Nexy)
default	20:04:43.510864-0500	mDNSResponder	[R21916] DNSServiceQueryRecord START -- qname: <mask.hash: 'PAT+qg22Mu/apI2NzrlwIw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: f92d5498
default	20:04:43.511499-0500	mDNSResponder	[R21917] DNSServiceQueryRecord START -- qname: <mask.hash: 'PAT+qg22Mu/apI2NzrlwIw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: f92d5498
default	20:04:43.526567-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0726AC9F-F774-4A6C-81B3-6DA10BBC6A4A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57963,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xa7f552dd tp_proto=0x06"
default	20:04:43.526680-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57963<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208985 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8246ae70
default	20:04:48.505887-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:57963<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208985 t_state: SYN_SENT process: Nexy:7217 Duration: 4.980 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8246ae70
default	20:04:48.505923-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57963<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 208985 t_state: SYN_SENT process: Nexy:7217 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:04:49.675580-0500	Nexy	[0xabf638dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:04:49.676492-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7217.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:49.677881-0500	tccd	AUTHREQ_SUBJECT: msgID=7217.2, subject=com.nexy.assistant,
default	20:04:49.678716-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:49.706211-0500	Nexy	[0xabf638dc0] invalidated after the last release of the connection object
default	20:04:49.706485-0500	Nexy	server port 0x00001623, session port 0x00003407
default	20:04:49.707496-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.825, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:49.707537-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:49.708627-0500	tccd	AUTHREQ_SUBJECT: msgID=397.825, subject=com.nexy.assistant,
default	20:04:49.709651-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:49.763385-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:04:49.764270-0500	Nexy	[0xabf638f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:04:49.765256-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1fe016","name":"Nexy(7217)"}, "details":{"PID":7217,"session_type":"Primary"} }
default	20:04:49.765345-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":7217}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1fe016, sessionType: 'prim', isRecording: false }, 
]
default	20:04:49.766180-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 7217, name = Nexy
default	20:04:49.766573-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xabf694660 with ID: 0x1fe016
default	20:04:49.766853-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:04:49.767796-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:04:49.769629-0500	Nexy	[0xabf639040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:04:49.772841-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
default	20:04:49.778913-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:04:49.781548-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:04:49.781747-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:04:49.781917-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:04:49.781933-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:04:49.781972-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:04:49.782346-0500	Nexy	[0xabf639180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:04:49.782489-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:04:49.782917-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7217.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:49.790848-0500	tccd	AUTHREQ_SUBJECT: msgID=7217.3, subject=com.nexy.assistant,
default	20:04:49.791764-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3fc00 at /Applications/Nexy.app
default	20:04:49.813395-0500	Nexy	[0xabf639180] invalidated after the last release of the connection object
default	20:04:49.813595-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:04:49.813643-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:04:49.813937-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:04:49.815330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.289, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:49.816595-0500	tccd	AUTHREQ_SUBJECT: msgID=410.289, subject=com.nexy.assistant,
default	20:04:49.817307-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c000 at /Applications/Nexy.app
default	20:04:49.845128-0500	tccd	AUTHREQ_SUBJECT: msgID=410.291, subject=com.nexy.assistant,
default	20:04:49.867538-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:04:49.867563-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xabc89eba0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:04:49.902806-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	20:04:49.902903-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	20:04:49.902959-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	20:04:49.924688-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 120
default	20:04:49.987062-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.009116-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C646CAA9-6E5C-4D9B-8839-21E8E7C36B7F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57974,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfe27bf10 tp_proto=0x06"
default	20:04:50.009193-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57974<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 209654 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb00cbd90
default	20:04:50.010973-0500	Nexy	nw_path_libinfo_path_check [81271E46-230C-4E7F-B32A-B6DA2D00EF5F Hostname#2e30df78:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:04:50.011104-0500	mDNSResponder	[R21935] DNSServiceQueryRecord START -- qname: <mask.hash: '7wJy4Xm1+ZzGgQIvaPC6Pw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: 2d50b096
default	20:04:50.011887-0500	mDNSResponder	[R21936] DNSServiceQueryRecord START -- qname: <mask.hash: '7wJy4Xm1+ZzGgQIvaPC6Pw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: 2d50b096
default	20:04:50.019335-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.827, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=7347, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:50.031737-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B8F4CF56-803D-4973-9345-B0060D16839C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57975,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x38bd9af0 tp_proto=0x06"
default	20:04:50.031822-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57975<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 209664 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa072945a
default	20:04:50.105528-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.184088-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 7358: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 404e0300 };
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
default	20:04:50.200548-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:50.212310-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3ed00 at /Applications/Nexy.app
default	20:04:50.232381-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	20:04:50.457519-0500	Nexy	[0xabf639680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:04:50.458172-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7217.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:50.464823-0500	tccd	AUTHREQ_SUBJECT: msgID=7217.4, subject=com.nexy.assistant,
default	20:04:50.465490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.484213-0500	Nexy	[0xabf639680] invalidated after the last release of the connection object
default	20:04:50.484489-0500	Nexy	[0xabf639680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:04:50.485027-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7217.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:04:50.485894-0500	tccd	AUTHREQ_SUBJECT: msgID=7217.5, subject=com.nexy.assistant,
default	20:04:50.486649-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.505055-0500	Nexy	[0xabf639680] invalidated after the last release of the connection object
default	20:04:50.505146-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:04:50.505578-0500	Nexy	[0xabf639680] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:04:50.505709-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:04:50.505786-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:04:50.507678-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75614.33, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:04:50.507705-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:50.508620-0500	tccd	AUTHREQ_SUBJECT: msgID=75614.33, subject=com.nexy.assistant,
default	20:04:50.509274-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.532259-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.831, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:50.532289-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:50.533164-0500	tccd	AUTHREQ_SUBJECT: msgID=397.831, subject=com.nexy.assistant,
default	20:04:50.533847-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:50.574589-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	20:04:50.618820-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
fault	20:04:50.620543-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53705040.53705049 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53705040.53705049>
default	20:04:50.638029-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:50.638144-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:04:50.638192-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:04:51.071975-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:04:51.074043-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xabe6a4650: start, was running 0
default	20:04:51.075464-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16537 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:51.075526-0500	runningboardd	Assertion 403-338-16537 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:51.075769-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.075781-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.075789-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.075807-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.078749-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.079165-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.113508-0500	Nexy	[0xabf639a40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:04:51.123613-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:04:51.124562-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 7217
default	20:04:51.134610-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xabf52c780
 (
    "<NSDarkAquaAppearance: 0xabf52c820>",
    "<NSSystemAppearance: 0xabf52c6e0>"
)>
default	20:04:51.137556-0500	Nexy	[0xabf639f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:04:51.138668-0500	Nexy	[0xabf63a080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:04:51.141079-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:04:51.141344-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:04:51.141357-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:04:51.141386-0500	Nexy	[0xabf63a1c0] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:04:51.141411-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:04:51.141469-0500	Nexy	[0xabf63a300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:51.141530-0500	Nexy	FBSWorkspace registering source: <private>
default	20:04:51.142092-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:04:51.142221-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:04:51.142620-0500	Nexy	<FBSWorkspaceScenesClient:0xac0a692c0 <private>> attempting immediate handshake from activate
default	20:04:51.142662-0500	Nexy	<FBSWorkspaceScenesClient:0xac0a692c0 <private>> sent handshake
default	20:04:51.142704-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.142726-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.142750-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:04:51.142795-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Registering event dispatcher at init
default	20:04:51.142859-0500	ControlCenter	Created <FBWorkspace: 0xcbd1af3e0; <FBApplicationProcess: 0xcc0136a00; app<application.com.nexy.assistant.53705040.53705049>:7217(v34D57)>>
default	20:04:51.142874-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.53705040.53705049> with intent background
default	20:04:51.143186-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53705040.53705049(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:04:51.143296-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53705040.53705049(501)> from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-672-16538 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:04:51.143438-0500	runningboardd	Assertion 403-672-16538 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) will be created as active
default	20:04:51.143471-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-672-16538 target:app<application.com.nexy.assistant.53705040.53705049(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.143312-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:04:51.143791-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.143804-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.143843-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.144085-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.145085-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:04:51.146379-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:04:51.146985-0500	Nexy	Requesting scene <FBSScene: 0xac0a69720; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A> from com.apple.controlcenter.statusitems
default	20:04:51.147305-0500	Nexy	Request for <FBSScene: 0xac0a69720; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A> complete!
default	20:04:51.147388-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:04:51.149209-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:04:51.149573-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:04:51.149914-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:04:51.149950-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:04:51.150377-0500	Nexy	Requesting scene <FBSScene: 0xac0a697c0; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:04:51.150572-0500	Nexy	Request for <FBSScene: 0xac0a697c0; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView> complete!
default	20:04:51.152498-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.152518-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:04:51.153788-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.154557-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Bootstrap success!
default	20:04:51.155024-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Setting process visibility to: Background
default	20:04:51.155077-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:04:51.155333-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:403-672-16539 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:04:51.155399-0500	runningboardd	Assertion 403-672-16539 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:51.155759-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.155770-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.155877-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.155978-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.156476-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.156497-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:04:51.156595-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:04:51.159492-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.159897-0500	ControlCenter	Adding: <FBApplicationProcess: 0xcc0136a00; app<application.com.nexy.assistant.53705040.53705049>:7217(v34D57)>
default	20:04:51.160417-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Connection established.
default	20:04:51.160480-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.160482-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xcbeb468b0>
default	20:04:51.160510-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Connection to remote process established!
default	20:04:51.164408-0500	Nexy	Registering for test daemon availability notify post.
default	20:04:51.164544-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:51.164645-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:51.164731-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:04:51.165043-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.165060-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xcc0136a00; app<application.com.nexy.assistant.53705040.53705049>:7217(v34D57)>
default	20:04:51.165150-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Registered new scene: <FBWorkspaceScene: 0xcbf633cc0; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A> (fromRemnant = 0)
default	20:04:51.165184-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace interruption policy did change: reconnect
default	20:04:51.165333-0500	ControlCenter	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A] Client process connected: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.165338-0500	Nexy	Request for <FBSScene: 0xac0a69720; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A> complete!
default	20:04:51.165432-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:403-672-16540 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:04:51.165505-0500	runningboardd	Assertion 403-672-16540 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as inactive as originator process has not exited
default	20:04:51.165842-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.165855-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xcc0136a00; app<application.com.nexy.assistant.53705040.53705049>:7217(v34D57)>
default	20:04:51.165913-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Registered new scene: <FBWorkspaceScene: 0xcbf6339c0; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:04:51.165838-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-672-16541 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:04:51.165941-0500	runningboardd	Assertion 403-672-16541 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:51.166023-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:04:51.166044-0500	ControlCenter	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:51.165940-0500	Nexy	[0xabf63a6c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:04:51.166039-0500	Nexy	Request for <FBSScene: 0xac0a697c0; com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView> complete!
default	20:04:51.166359-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.166789-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.166824-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.166568-0500	Nexy	<FBSWorkspaceScenesClient:0xac0a692c0 <private>> Reconnecting scene com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A
default	20:04:51.166946-0500	Nexy	<FBSWorkspaceScenesClient:0xac0a692c0 <private>> Reconnecting scene com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView
default	20:04:51.166929-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.169270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:51.169869-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.173309-0500	Nexy	[0xabf6383c0] Connection returned listener port: 0x5007
default	20:04:51.173798-0500	Nexy	SignalReady: pid=7217 asn=0x0-0x146146
default	20:04:51.174242-0500	Nexy	SIGNAL: pid=7217 asn=0x0x-0x146146
default	20:04:51.175059-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:04:51.183804-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.185194-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.185316-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.186182-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.188707-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:04:51.188713-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:04:51.188728-0500	Nexy	[0xabf639540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:04:51.188796-0500	Nexy	[0xabf639540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:04:51.189907-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:04:51.195455-0500	Nexy	[C:2] Alloc <private>
default	20:04:51.195486-0500	Nexy	[0xabf639540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:04:51.196175-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-7217). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:04:51.196928-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-7217)
default	20:04:51.197031-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(891AC589, (bid:com.nexy.assistant-Item-0-7217)) for (bid:com.nexy.assistant-Item-0-7217)
default	20:04:51.197236-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7217-16542 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:51.197302-0500	runningboardd	Assertion 403-7217-16542 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:51.197408-0500	WindowManager	Connection activated | (7217) Nexy
default	20:04:51.197669-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-7217)]
default	20:04:51.197669-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.197726-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.197803-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.197734-0500	ControlCenter	Created instance DisplayableId(5B9CDFCA) in .menuBar for DisplayableAppStatusItemType(891AC589, (bid:com.nexy.assistant-Item-0-7217)) .menuBar
default	20:04:51.197978-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.202265-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:04:51.203063-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.203244-0500	ControlCenter	Created ephemaral instance DisplayableId(5B9CDFCA) for (bid:com.nexy.assistant-Item-0-7217) with positioning .ephemeral
default	20:04:51.203519-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.203526-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.203666-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
error	20:04:51.204014-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	20:04:51.204147-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.213330-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A] Sending action(s) in update: NSSceneFenceAction
default	20:04:51.359184-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:04:51.362008-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:04:51.362677-0500	Nexy	[GMS] availability notification token 90
default	20:04:51.408849-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:04:51.408958-0500	runningboardd	Invalidating assertion 403-672-16541 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:04:51.452241-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:04:51.453114-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe016","name":"Nexy(7217)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:04:51.453221-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:04:51.453272-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:04:51.453318-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1fe016, Nexy(7217), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:04:51.453345-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.453366-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:04:51.453377-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 23 starting playing
default	20:04:51.453449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:04:51.453479-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:04:51.453471-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.453514-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.453502-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe016, Nexy(7217), 'prim'', displayID:'com.nexy.assistant'}
default	20:04:51.453524-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:04:51.453553-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:04:51.453674-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:04:51.453686-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:04:51.453577-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1fe016 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":7217}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1fe016, sessionType: 'prim', isRecording: false }, 
]
default	20:04:51.453753-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:04:51.453927-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.454005-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.454030-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:51.454045-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:04:51.454055-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:04:51.454065-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	20:04:51.454118-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	20:04:51.454184-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:04:51.512562-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.512573-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.512583-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.512600-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.516266-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.516735-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.516908-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.699707-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.WindowServer(88)>:397] with description <RBSAssertionDescriptor| "AppDrawing" ID:403-397-16544 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:51.699816-0500	runningboardd	Assertion 403-397-16544 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:51.700262-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:51.700278-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:51.700289-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:51.700329-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:51.704495-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:51.705049-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.705326-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:51.943268-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3f900 at /Applications/Nexy.app
default	20:04:51.950858-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    487 = "<TCCDEventSubscriber: token=487, state=Passed, csid=com.apple.photolibraryd>";
    457 = "<TCCDEventSubscriber: token=457, state=Initial, csid=(null)>";
    484 = "<TCCDEventSubscriber: token=484, state=Passed, csid=com.apple.chronod>";
}
default	20:04:51.958448-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:04:53.250247-0500	runningboardd	Invalidating assertion 403-672-16538 (target:app<application.com.nexy.assistant.53705040.53705049(501)>) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:04:53.350629-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.53705040.53705049(501)>
default	20:04:53.351483-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:53.351496-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:53.351510-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:53.351553-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:53.355305-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:04:53.370217-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:53.373570-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:54.442130-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	20:04:54.680807-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:54.680902-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:04:55.834836-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.834, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:55.834883-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:55.836829-0500	tccd	AUTHREQ_SUBJECT: msgID=397.834, subject=com.nexy.assistant,
default	20:04:55.837963-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:56.126799-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:04:56.662106-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xabc3ed540) Selecting device 85 from constructor
default	20:04:56.662117-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xabc3ed540)
default	20:04:56.662122-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xabc3ed540) not already running
default	20:04:56.662126-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xabc3ed540) nothing to teardown
default	20:04:56.662128-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xabc3ed540) connecting device 85
default	20:04:56.662199-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xabc3ed540) Device ID: 85 (Input:No | Output:Yes): true
default	20:04:56.662430-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xabc3ed540) created ioproc 0xb for device 85
default	20:04:56.662584-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 7 device listeners to device 85
default	20:04:56.662739-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 0 device delegate listeners to device 85
default	20:04:56.662750-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xabc3ed540)
default	20:04:56.662815-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:04:56.662823-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:04:56.662827-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:04:56.662834-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:04:56.662842-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:04:56.662923-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xabc3ed540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:04:56.662934-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xabc3ed540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:04:56.662939-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:04:56.662942-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 0 device listeners from device 0
default	20:04:56.662945-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 0 device delegate listeners from device 0
default	20:04:56.662950-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xabc3ed540)
default	20:04:56.662962-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:04:56.663006-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xabc3ed540) caller requesting device change from 85 to 91
default	20:04:56.663014-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xabc3ed540)
default	20:04:56.663019-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xabc3ed540) not already running
default	20:04:56.663023-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xabc3ed540) disconnecting device 85
default	20:04:56.663036-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xabc3ed540) destroying ioproc 0xb for device 85
default	20:04:56.663062-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:04:56.663305-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:04:56.663485-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xabc3ed540) connecting device 91
default	20:04:56.663598-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xabc3ed540) Device ID: 91 (Input:Yes | Output:No): true
default	20:04:56.665093-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.292, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.666475-0500	tccd	AUTHREQ_SUBJECT: msgID=410.292, subject=com.nexy.assistant,
default	20:04:56.667160-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:56.683357-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:04:56.683398-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:04:56.683605-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xabc3ed540) created ioproc 0xa for device 91
default	20:04:56.683725-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 7 device listeners to device 91
default	20:04:56.683895-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 0 device delegate listeners to device 91
default	20:04:56.683902-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xabc3ed540)
default	20:04:56.683912-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:04:56.683923-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:04:56.684065-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:04:56.684075-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:04:56.684081-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:04:56.684174-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xabc3ed540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:04:56.684185-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xabc3ed540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:04:56.684189-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:04:56.684194-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 7 device listeners from device 85
default	20:04:56.684345-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 0 device delegate listeners from device 85
default	20:04:56.684353-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xabc3ed540)
default	20:04:56.684897-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=75614.34, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:04:56.684936-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=75614, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:56.684951-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:04:56.685872-0500	tccd	AUTHREQ_SUBJECT: msgID=75614.34, subject=com.nexy.assistant,
default	20:04:56.685918-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.293, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.686563-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:56.687072-0500	tccd	AUTHREQ_SUBJECT: msgID=410.293, subject=com.nexy.assistant,
default	20:04:56.687731-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:56.703778-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:04:56.704766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.294, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.705692-0500	tccd	AUTHREQ_SUBJECT: msgID=410.294, subject=com.nexy.assistant,
default	20:04:56.706274-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:56.708277-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.837, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:04:56.708302-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:04:56.709067-0500	tccd	AUTHREQ_SUBJECT: msgID=397.837, subject=com.nexy.assistant,
default	20:04:56.709683-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:56.722848-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.295, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.723864-0500	tccd	AUTHREQ_SUBJECT: msgID=410.295, subject=com.nexy.assistant,
default	20:04:56.724432-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:56.738957-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:04:56.741060-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:04:56.741189-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:04:56.741831-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:04:56.742060-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_986.898.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:04:56.742116-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_986.898.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:04:56.809257-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:04:56.810487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:986 called from <private>
default	20:04:56.810497-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:04:56.810527-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:04:56.811104-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:986 called from <private>
default	20:04:56.811249-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(986)
default	20:04:56.811284-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:986 called from <private>
default	20:04:56.811294-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:986 called from <private>
default	20:04:56.811341-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:04:56.811595-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:04:56.812552-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:04:56.812915-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:04:56.813359-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:992 called from <private>
default	20:04:56.813359-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:04:56.813404-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:992 called from <private>
default	20:04:56.813389-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:04:56.816028-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:04:56.816729-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:04:56.813472-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:992 called from <private>
default	20:04:56.813515-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:992 called from <private>
default	20:04:56.820549-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(986)
default	20:04:56.820568-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(986)
default	20:04:56.820578-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(986)
default	20:04:56.820588-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(986)
default	20:04:56.820746-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:986 called from <private>
default	20:04:56.820786-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:986 called from <private>
default	20:04:56.820883-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:986 called from <private>
default	20:04:56.820944-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:986 called from <private>
default	20:04:56.821011-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:986 called from <private>
default	20:04:56.821080-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:986 called from <private>
default	20:04:56.821122-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:986 called from <private>
default	20:04:56.821247-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:986 called from <private>
default	20:04:56.821289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:986 called from <private>
default	20:04:56.821372-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:986 called from <private>
default	20:04:56.822168-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:985 called from <private>
default	20:04:56.822206-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:985 called from <private>
default	20:04:56.822356-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:04:56.822396-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:985 called from <private>
default	20:04:56.822495-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:985 called from <private>
default	20:04:56.813077-0500	runningboardd	Invalidating assertion 403-7217-16542 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:56.826961-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:04:56.828663-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:985 called from <private>
default	20:04:56.828870-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:985 called from <private>
default	20:04:56.813818-0500	runningboardd	Invalidating assertion 403-338-16537 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.powerd>:338]
default	20:04:56.833010-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7217-16562 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:56.833093-0500	runningboardd	Assertion 403-7217-16562 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:56.829005-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:985 called from <private>
default	20:04:56.829157-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:985 called from <private>
default	20:04:56.829838-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:04:56.830010-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:985 called from <private>
default	20:04:56.830466-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
error	20:04:56.834325-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:04:56.834388-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:985 called from <private>
default	20:04:56.834487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:04:56.834547-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:04:56.834913-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:04:56.834919-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(986)
default	20:04:56.835189-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:986 called from <private>
default	20:04:56.836307-0500	runningboardd	Invalidating assertion 403-7217-16562 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:56.836596-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7217-16564 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:56.836659-0500	runningboardd	Assertion 403-7217-16564 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:56.837745-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:04:56.838375-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:04:56.835613-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:985 called from <private>
default	20:04:56.835787-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:985 called from <private>
default	20:04:56.836414-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:992 called from <private>
default	20:04:56.836467-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:992 called from <private>
default	20:04:56.836652-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:04:56.839459-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:04:56.839505-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:04:56.839545-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:04:56.839589-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:04:56.839632-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:04:56.839689-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:992 called from <private>
default	20:04:56.839721-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:992 called from <private>
default	20:04:56.839760-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:992 called from <private>
default	20:04:56.839792-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:992 called from <private>
default	20:04:56.839831-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:992 called from <private>
default	20:04:56.839879-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:992 called from <private>
default	20:04:56.840614-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:992 called from <private>
default	20:04:56.840621-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:992 called from <private>
default	20:04:56.840627-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:992 called from <private>
default	20:04:56.839227-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.296, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.840655-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:992 called from <private>
default	20:04:56.840689-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:992 called from <private>
default	20:04:56.840743-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:992 called from <private>
default	20:04:56.840826-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:992 called from <private>
default	20:04:56.840876-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:992 called from <private>
default	20:04:56.846909-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:985 called from <private>
default	20:04:56.846947-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:985 called from <private>
default	20:04:56.847001-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:04:56.876800-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	20:04:56.876813-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 1
default	20:04:56.876823-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	20:04:56.876832-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
error	20:04:56.876885-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 501,
}
default	20:04:56.876125-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:56.876171-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:56.875993-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xac0934ea0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:04:56.876262-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:04:56.876018-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:04:56.883450-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:56.883765-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x919158300 at /Applications/Nexy.app
default	20:04:56.889874-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:56.889959-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:04:56.890058-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
error	20:04:56.895507-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	20:04:56.895592-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
error	20:04:56.895757-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	20:04:56.895808-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:56.895998-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:04:56.896058-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:56.896137-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:04:56.896333-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:04:56.896476-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:56.896492-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:04:56.896645-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:04:56.897053-0500	runningboardd	Invalidating assertion 403-338-16565 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.powerd>:338]
default	20:04:56.897279-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16566 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:56.897325-0500	runningboardd	Assertion 403-338-16566 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:56.917697-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:04:56.926240-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:986 called from <private>
default	20:04:56.926282-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:986 called from <private>
default	20:04:56.924273-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:04:56.929266-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.297, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:56.934540-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:56.946280-0500	runningboardd	Invalidating assertion 403-338-16568 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.powerd>:338]
default	20:04:56.947889-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:56.963016-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:04:56.976206-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_986.898.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:04:56.976289-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x94cb4a700] Created node ADM::com.nexy.assistant_986.898.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:04:57.008661-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xabe6a4650: iounit configuration changed > posting notification
default	20:04:57.023711-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:04:57.028218-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16570 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:04:57.028387-0500	runningboardd	Assertion 403-338-16570 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:57.028050-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:986 called from <private>
default	20:04:57.028163-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:986 called from <private>
default	20:04:57.028203-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:04:57.030695-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:986 called from <private>
default	20:04:57.030844-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(986)
default	20:04:57.030869-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:986 called from <private>
default	20:04:57.030911-0500	runningboardd	Invalidating assertion 403-7217-16569 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:57.031002-0500	runningboardd	Invalidating assertion 403-338-16570 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.powerd>:338]
default	20:04:57.030879-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:986 called from <private>
default	20:04:57.031640-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:04:57.031863-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:04:57.033325-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7217-16571 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:04:57.033418-0500	runningboardd	Assertion 403-7217-16571 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:04:57.032480-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(986)
default	20:04:57.032757-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:986 called from <private>
default	20:04:57.032773-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:986 called from <private>
default	20:04:57.032790-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:986 called from <private>
default	20:04:57.035240-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=410.298, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=7217, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:04:57.037765-0500	tccd	AUTHREQ_SUBJECT: msgID=410.298, subject=com.nexy.assistant,
default	20:04:57.039560-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa7ed3c900 at /Applications/Nexy.app
default	20:04:57.040200-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:57.045725-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:04:57.045763-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:04:57.045804-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:04:57.045285-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:57.045887-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:04:57.048346-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:57.048434-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:04:57.048501-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:04:57.049185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.049196-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.049211-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.049295-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.049089-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:57.049364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.049446-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.049501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.049839-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:04:57.049849-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.049918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.049962-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.050052-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.050160-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.050278-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.050319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.050360-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.050415-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:04:57.050422-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.050487-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.050519-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.057605-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:57.060144-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:57.060221-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:04:57.060275-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:04:57.060297-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:04:57.099428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099445-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099457-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.099466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.099518-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.099658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099710-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099813-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.099867-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.099951-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.100012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.100019-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:04:57.100076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.100089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.100101-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.100109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:57.100117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:57.100147-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:57.100208-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:04:57.159964-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:57.160274-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:04:57.442173-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:04:59.560996-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A] Sending action(s) in update: NSSceneFenceAction
default	20:04:59.978748-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:04:59.979120-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe016","name":"Nexy(7217)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:04:59.979254-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:04:59.979326-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:04:59.979363-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe016, Nexy(7217), 'prim'', displayID:'com.nexy.assistant'}
default	20:04:59.979418-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1fe016, Nexy(7217), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 23 stopping recording
default	20:04:59.979423-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:04:59.979448-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:04:59.979480-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:04:59.979564-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:04:59.979706-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:04:59.979717-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:04:59.979779-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:04:59.980087-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:59.980134-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:59.980184-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:59.980221-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:04:59.980253-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:59.980278-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:04:59.980348-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:04:59.980364-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:04:59.980377-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:04:59.982050-0500	runningboardd	Invalidating assertion 403-7217-16571 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217]
default	20:04:59.982261-0500	runningboardd	Invalidating assertion 403-338-16572 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.powerd>:338]
default	20:04:59.984019-0500	coreaudiod	Sending message. { reporterID=30996778975235, category=IO, type=error, message=["sample_rate": Optional(24000), "io_cycle": Optional(144), "safety_violation_sample_gap": Optional(0), "wg_system_time_mach": Optional(12150), "is_prewarming": Optional(0), "wg_instructions": Optional(7592986), "io_frame_counter": Optional(69120), "wg_cycles": Optional(7416666), "careporting_timestamp": 1770512699.983247, "wg_user_time_mach": Optional(91378), "io_buffer_size": Optional(480), "num_continuous_silent_io_cycles": Optional(0), "input_device_transport_list": Optional(Bluetooth), "smallest_buffer_frame_size": Optional(2147483647), "multi_cycle_io_page_faults": Optional(0), "start_time": Optional(331469950360), "safety_violation_time_gap": Optional(0), "io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "safety_violation": Optional(0), "multi_cycle_io_page_faults_duration": Optional(0), "num_continuous_nonzero_io_cycles": Optional(0), "HAL_client_IO_duration": Optional(16356875), "lateness": Optional(17), "wg_exter<…> }
default	20:04:59.991641-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:04:59.991738-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:04:59.991818-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:04:59.991848-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:04:59.993061-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:59.993074-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:59.993088-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:59.993096-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:04:59.993103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:04:59.993110-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:04:59.993217-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:04:59.998311-0500	Nexy	nw_path_libinfo_path_check [D9B96BEF-D636-442C-B1C0-157297A82AE1 Hostname#41c2470b:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:04:59.998464-0500	mDNSResponder	[R21940] DNSServiceQueryRecord START -- qname: <mask.hash: '00xiETFdq4TPGd3nFy5jrA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: b360ab20
default	20:04:59.999198-0500	mDNSResponder	[R21941] DNSServiceQueryRecord START -- qname: <mask.hash: '00xiETFdq4TPGd3nFy5jrA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 7217 (Nexy), name hash: b360ab20
default	20:05:00.012029-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BBCF8ED8-F14E-40DF-9169-6E62BB2A9730 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57977,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xf144fcd1 tp_proto=0x06"
default	20:05:00.012132-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57977<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 209744 t_state: SYN_SENT process: Nexy:7217 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb24b3306
default	20:05:00.020004-0500	kernel	tcp connected: [<IPv4-redacted>:57977<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 209744 t_state: ESTABLISHED process: Nexy:7217 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb24b3306
default	20:05:00.081949-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xabc3ed540) Selecting device 0 from destructor
default	20:05:00.081964-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xabc3ed540)
default	20:05:00.081974-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xabc3ed540) not already running
default	20:05:00.081979-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xabc3ed540) disconnecting device 91
default	20:05:00.081988-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xabc3ed540) destroying ioproc 0xa for device 91
default	20:05:00.082027-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:05:00.082062-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:05:00.082231-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xabc3ed540) nothing to setup
default	20:05:00.082247-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 0 device listeners to device 0
default	20:05:00.082254-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xabc3ed540) adding 0 device delegate listeners to device 0
default	20:05:00.082262-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 7 device listeners from device 91
default	20:05:00.082468-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xabc3ed540) removing 0 device delegate listeners from device 91
default	20:05:00.082482-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xabc3ed540)
default	20:05:00.084625-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:00.084651-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:00.084677-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:00.084734-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:00.088134-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:00.088639-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:00.088860-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:00.776776-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:57977<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 209744 t_state: LAST_ACK process: Nexy:7217 Duration: 0.765 sec Conn_Time: 0.008 sec bytes in/out: 601/72352 pkts in/out: 4/20 pkt rxmit: 6 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 10.000 ms rttvar: 4.500 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0xb24b3306
default	20:05:00.776813-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57977<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 209744 t_state: LAST_ACK process: Nexy:7217 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:05:01.515208-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:05:02.202101-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:05:02.202161-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:992 called from <private>
default	20:05:02.202172-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:992 called from <private>
default	20:05:02.202482-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:05:02.202505-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:05:02.202513-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:05:02.203408-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:05:02.203423-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(986)
default	20:05:02.203464-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:992 called from <private>
default	20:05:02.203526-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:986 called from <private>
default	20:05:02.203546-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:992 called from <private>
default	20:05:02.203562-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:986 called from <private>
default	20:05:02.205862-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:985 called from <private>
default	20:05:02.205887-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:985 called from <private>
default	20:05:02.206073-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:05:02.206099-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:985 called from <private>
default	20:05:02.206109-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:985 called from <private>
default	20:05:02.207612-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:05:02.207932-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:05:02.207943-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:985 called from <private>
default	20:05:02.207957-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:05:02.207957-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:985 called from <private>
default	20:05:02.207976-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:985 called from <private>
default	20:05:02.207988-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:985 called from <private>
default	20:05:02.208018-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:985 called from <private>
default	20:05:02.208076-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:985 called from <private>
default	20:05:02.208199-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:05:02.208295-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:05:02.217835-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:05:02.217905-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(986)
default	20:05:02.217930-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:986 called from <private>
default	20:05:02.217936-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:986 called from <private>
default	20:05:02.220345-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:985 called from <private>
default	20:05:02.220367-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:985 called from <private>
default	20:05:02.220495-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:05:02.220519-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:985 called from <private>
default	20:05:02.220526-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:985 called from <private>
default	20:05:02.220696-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:05:02.220846-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:992 called from <private>
default	20:05:02.220942-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:992 called from <private>
default	20:05:02.221143-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(992)
default	20:05:02.221524-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:05:02.221815-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:985 called from <private>
default	20:05:02.221903-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:05:02.221923-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:985 called from <private>
default	20:05:02.223556-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:05:02.224311-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:05:02.221966-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:985 called from <private>
default	20:05:02.222074-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:985 called from <private>
default	20:05:02.222132-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:985 called from <private>
default	20:05:02.222172-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:985 called from <private>
default	20:05:02.225347-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(992)
default	20:05:02.225538-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:992 called from <private>
default	20:05:02.225548-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:992 called from <private>
default	20:05:02.225589-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:992 called from <private>
default	20:05:02.225677-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:992 called from <private>
default	20:05:02.225753-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:992 called from <private>
default	20:05:02.225814-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:992 called from <private>
default	20:05:02.225903-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:992 called from <private>
default	20:05:02.225950-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:992 called from <private>
default	20:05:02.226001-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:992 called from <private>
default	20:05:02.226056-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:992 called from <private>
default	20:05:02.236860-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:05:02.236891-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:05:02.237183-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(985)
default	20:05:02.240606-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(985)
default	20:05:02.240782-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:985 called from <private>
default	20:05:02.240793-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:985 called from <private>
default	20:05:02.240833-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:985 called from <private>
default	20:05:02.240842-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:985 called from <private>
default	20:05:02.240849-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:985 called from <private>
default	20:05:02.240854-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:985 called from <private>
default	20:05:02.241051-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xabc2c8040) Device ID: 85 (Input:No | Output:Yes): true
default	20:05:02.241074-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xabc2c8040)
default	20:05:02.241406-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:05:02.241481-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:05:02.241547-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:05:02.241637-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:05:02.241756-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:05:02.241972-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xabc2c8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:05:02.241997-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xabc2c8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:05:02.242006-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:05:02.242213-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xabc2c8040) Device ID: 85 (Input:No | Output:Yes): true
default	20:05:02.242223-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xabc2c8040)
default	20:05:02.242381-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:05:02.242553-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:05:02.242616-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:05:02.242757-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:05:02.242851-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:05:02.243289-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xabc2c8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:05:02.243554-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xabc2c8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:05:02.243681-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:05:02.350172-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xabe6a4650: iounit configuration changed > posting notification
default	20:05:07.349956-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xabf164390, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:05:07.350004-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xabf164390: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:05:07.350020-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:05:07.350019-0500	Nexy	AudioConverter -> 0xabf164390: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:05:07.350052-0500	Nexy	AudioConverter -> 0xabf164390: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:05:07.350063-0500	Nexy	AudioConverter -> 0xabf164390: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:05:07.350492-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xabf164390: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:05:07.350529-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xabe6a4650: start, was running 0
default	20:05:07.351469-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-7217-16576 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:05:07.351540-0500	runningboardd	Assertion 403-7217-16576 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:05:07.351885-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:07.351994-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:07.352025-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:07.352101-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:07.352112-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-16577 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:05:07.352176-0500	runningboardd	Assertion 403-338-16577 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:05:07.355207-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:07.355402-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:07.355415-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:07.355426-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:07.355479-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:07.355591-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:07.355850-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:07.358531-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:07.358903-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:07.359042-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:07.637455-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:05:07.638339-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1fe016","name":"Nexy(7217)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:05:07.638469-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:05:07.638508-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1fe016, Nexy(7217), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:05:07.638544-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:05:07.638592-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1fe016, Nexy(7217), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:05:07.638623-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.638657-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:05:07.638668-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 23 starting playing
default	20:05:07.638741-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:05:07.638770-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:05:07.638804-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1fe016, Nexy(7217), 'prim'', displayID:'com.nexy.assistant'}
default	20:05:07.638803-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.638833-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 23, PID = 7217, Name = sid:0x1fe016, Nexy(7217), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:05:07.638859-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.638866-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:05:07.638984-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:05:07.639003-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:05:07.638900-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1fe016 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":7217}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1fe016, sessionType: 'prim', isRecording: false }, 
]
default	20:05:07.639040-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xA37F0001 category Not set
default	20:05:07.639234-0500	audiomxd	UpdateAudioState CID 0xA37F0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.639312-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.639338-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:05:07.639350-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:05:07.639360-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:05:07.639370-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	20:05:07.639420-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	20:05:07.639484-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:05:08.265239-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-672-16583 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:05:08.265312-0500	Nexy	[com.apple.controlcenter:11ED9E94-B3F9-42F1-91DE-477E4E01CA1A] Sending action(s) in update: NSSceneFenceAction
default	20:05:08.265423-0500	runningboardd	Assertion 403-672-16583 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:05:08.265588-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:05:08.265850-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:08.265865-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:08.265903-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:08.266011-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:08.269923-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:08.270579-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.271358-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.372826-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:05:08.373007-0500	runningboardd	Invalidating assertion 403-672-16583 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:05:08.482482-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:08.482496-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:08.482505-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:08.482522-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:08.486552-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:08.486984-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.487303-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.548775-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53705040.53705049(501)>:7217] from originator [osservice<com.apple.controlcenter(501)>:672] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-672-16594 target:7217 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:05:08.548932-0500	runningboardd	Assertion 403-672-16594 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) will be created as active
default	20:05:08.552769-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:05:08.553006-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:08.553155-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:08.553231-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:08.553316-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:08.556685-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:08.592756-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.593225-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.658432-0500	ControlCenter	[app<application.com.nexy.assistant.53705040.53705049>:7217] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:05:08.658608-0500	runningboardd	Invalidating assertion 403-672-16594 (target:[app<application.com.nexy.assistant.53705040.53705049(501)>:7217]) from originator [osservice<com.apple.controlcenter(501)>:672]
default	20:05:08.669029-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring jetsam update because this process is not memory-managed
default	20:05:08.669070-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring suspend because this process is not lifecycle managed
default	20:05:08.669106-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring GPU update because this process is not GPU managed
default	20:05:08.669197-0500	runningboardd	[app<application.com.nexy.assistant.53705040.53705049(501)>:7217] Ignoring memory limit update because this process is not memory-managed
default	20:05:08.673357-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53705040.53705049(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:05:08.673718-0500	ControlCenter	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:08.673882-0500	gamepolicyd	Received state update for 7217 (app<application.com.nexy.assistant.53705040.53705049(501)>, running-active-NotVisible
default	20:05:09.442059-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	20:05:10.741466-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:05:10.742664-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:05:10.742680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:05:10.742698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:05:10.742722-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:05:10.742732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:05:10.742739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:05:10.742858-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
