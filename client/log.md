default	14:48:22.508914-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	14:48:22.509131-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	14:48:22.510966-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	14:48:22.515321-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	14:48:22.522547-0500	runningboardd	Launch request for app<application.com.nexy.assistant.57221987.57221996(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:48:22.522625-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.57221987.57221996(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:70772] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:404-70772-33080 target:app<application.com.nexy.assistant.57221987.57221996(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:48:22.522705-0500	runningboardd	Assertion 404-70772-33080 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) will be created as active
default	14:48:22.525248-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	14:48:22.525276-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:48:22.525286-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	14:48:22.525352-0500	runningboardd	app<application.com.nexy.assistant.57221987.57221996(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	14:48:22.559797-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] is not RunningBoard jetsam managed.
default	14:48:22.559812-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] This process will not be managed.
default	14:48:22.559823-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:48:22.560142-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:22.562398-0500	gamepolicyd	Hit the server for a process handle 851b7710000220c that resolved to: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:48:22.562431-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:22.565186-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:48:22.565252-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:404-404-33081 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:22.565371-0500	runningboardd	Assertion 404-404-33081 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:22.565545-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:22.565562-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:22.565578-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Set darwin role to: UserInteractive
default	14:48:22.565593-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:22.565618-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:22.565668-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] reported to RB as running
default	14:48:22.567312-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:8716" ID:404-366-33082 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:48:22.567416-0500	runningboardd	Assertion 404-366-33082 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:22.567733-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x165165 com.nexy.assistant starting stopped process.
default	14:48:22.568907-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:22.568972-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:22.569030-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:22.569122-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:22.569267-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:48:22.569068-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	14:48:22.569224-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 2
default	14:48:22.569245-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:48:22.573122-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:22.573358-0500	runningboardd	Invalidating assertion 404-70772-33080 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:70772]
default	14:48:22.573389-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:22.573421-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:22.573455-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:22.573533-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:22.573668-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:22.576404-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:22.576514-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:22.576524-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:22.576534-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:22.576580-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:22.678232-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:22.745856-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	14:48:22.747185-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=496.26, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=496, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	14:48:22.754122-0500	tccd	AUTHREQ_SUBJECT: msgID=496.26, subject=com.nexy.assistant,
default	14:48:22.754863-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:48:22.769406-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	14:48:22.777293-0500	kernel	Nexy[8716] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xc1260fea969fb2fb. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:48:22.777323-0500	kernel	Nexy[8716] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xc1260fea969fb2fb. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:48:23.002934-0500	Nexy	[0x102dc89b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	14:48:23.003002-0500	Nexy	[0x102dc8ef0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	14:48:23.230859-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb27aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:48:23.231084-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb27aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:48:23.231288-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb27aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:48:23.231487-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb27aa8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:48:23.232800-0500	Nexy	[0x102dcf6e0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:48:23.233551-0500	Nexy	[0xb26afc000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:48:23.233879-0500	Nexy	[0xb26afc140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:48:23.234321-0500	Nexy	[0xb26afc280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:48:23.235142-0500	Nexy	Received configuration update from daemon (initial)
default	14:48:23.236363-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:48:23.237149-0500	Nexy	[0xb26afc3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:23.238075-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:48:23.239708-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.1, subject=com.nexy.assistant,
default	14:48:23.240822-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:48:23.254547-0500	Nexy	[0xb26afc3c0] invalidated after the last release of the connection object
default	14:48:23.257498-0500	Nexy	server port 0x00003707, session port 0x00003707
default	14:48:23.258671-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.846, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:48:23.258694-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:48:23.259713-0500	tccd	AUTHREQ_SUBJECT: msgID=396.846, subject=com.nexy.assistant,
default	14:48:23.260418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:48:23.279406-0500	Nexy	New connection 0xcc857 main
default	14:48:23.281678-0500	Nexy	CHECKIN: pid=8716
default	14:48:23.288786-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:8716" ID:404-366-33083 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:48:23.288858-0500	runningboardd	Assertion 404-366-33083 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:23.289180-0500	Nexy	CHECKEDIN: pid=8716 asn=0x0-0x165165 foreground=0
default	14:48:23.289217-0500	runningboardd	Invalidating assertion 404-366-33082 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	14:48:23.289052-0500	launchservicesd	CHECKIN:0x0-0x165165 8716 com.nexy.assistant
default	14:48:23.289402-0500	Nexy	[0xb26afc3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:48:23.289431-0500	Nexy	[0xb26afc3c0] Connection returned listener port: 0x4e03
default	14:48:23.289726-0500	Nexy	[0xb27c94300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb26afc3c0.peer[366].0xb27c94300
default	14:48:23.290317-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	14:48:23.290405-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:48:23.291441-0500	Nexy	FRONTLOGGING: version 1
default	14:48:23.291467-0500	Nexy	Registered, pid=8716 ASN=0x0,0x165165
default	14:48:23.291721-0500	WindowServer	cc857[CreateApplication]: Process creation: 0x0-0x165165 (Nexy) connectionID: CC857 pid: 8716 in session 0x101
default	14:48:23.291862-0500	Nexy	[0xb26afc780] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:48:23.293421-0500	Nexy	[0xb26afc3c0] Connection returned listener port: 0x4e03
default	14:48:23.294027-0500	Nexy	BringForward: pid=8716 asn=0x0-0x165165 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	14:48:23.294157-0500	Nexy	BringFrontModifier: pid=8716 asn=0x0-0x165165 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	14:48:23.294792-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:48:23.295912-0500	Nexy	No persisted cache on this platform.
default	14:48:23.297070-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:48:23.297703-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:48:23.300306-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	14:48:23.300314-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	14:48:23.300365-0500	Nexy	Initializing connection
default	14:48:23.300403-0500	Nexy	Removing all cached process handles
default	14:48:23.300420-0500	Nexy	Sending handshake request attempt #1 to server
default	14:48:23.300429-0500	Nexy	Creating connection to com.apple.runningboard
default	14:48:23.300435-0500	Nexy	[0xb26afc500] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:48:23.300756-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] as ready
default	14:48:23.301296-0500	Nexy	Handshake succeeded
default	14:48:23.301311-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:48:23.301899-0500	Nexy	[0xb26afc3c0] Connection returned listener port: 0x4e03
default	14:48:23.302656-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 8716
default	14:48:23.306787-0500	Nexy	[0xb26afc3c0] Connection returned listener port: 0x4e03
default	14:48:23.309637-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:48:23.309689-0500	Nexy	[0xb26afc640] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:48:23.309798-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:48:23.309855-0500	Nexy	[0xb26afca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:48:23.311014-0500	Nexy	[0xb26afca00] Connection returned listener port: 0x6e03
default	14:48:23.311561-0500	Nexy	Registered process with identifier 8716-1182989
default	14:48:24.776458-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 520A8D72-7E5C-43B6-9B1E-A23CF8D15607 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55224,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x8786223c tp_proto=0x06"
default	14:48:24.776566-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55224<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1046715 t_state: SYN_SENT process: Nexy:8716 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xafd8b04a
default	14:48:24.799098-0500	kernel	tcp connected: [<IPv4-redacted>:55224<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1046715 t_state: ESTABLISHED process: Nexy:8716 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xafd8b04a
default	14:48:24.799415-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55224<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1046715 t_state: FIN_WAIT_1 process: Nexy:8716 Duration: 0.023 sec Conn_Time: 0.023 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 23.000 ms rttvar: 11.500 ms base rtt: 23 ms so_error: 0 svc/tc: 0 flow: 0xafd8b04a
default	14:48:24.799424-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55224<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1046715 t_state: FIN_WAIT_1 process: Nexy:8716 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:48:25.896152-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:48:25.900085-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:48:25.902911-0500	Nexy	[0xb26afcdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	14:48:25.906228-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
default	14:48:25.910531-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:48:25.912300-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:48:25.912442-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:48:25.912578-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:48:25.912589-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:48:25.913005-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:48:25.913125-0500	Nexy	[0xb26afcf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:48:25.913281-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	14:48:25.913606-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:48:25.920428-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.2, subject=com.nexy.assistant,
default	14:48:25.921030-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7cc00 at /Applications/Nexy.app
default	14:48:25.933043-0500	Nexy	[0xb26afcf00] invalidated after the last release of the connection object
default	14:48:25.933094-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:48:25.936280-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	14:48:25.937900-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.618, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:25.939165-0500	tccd	AUTHREQ_SUBJECT: msgID=409.618, subject=com.nexy.assistant,
default	14:48:25.939799-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
error	14:48:25.952054-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=409, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:48:25.952924-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.620, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:25.953854-0500	tccd	AUTHREQ_SUBJECT: msgID=409.620, subject=com.nexy.assistant,
default	14:48:25.954401-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:25.969327-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:48:25.969700-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb25a46780> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	14:48:25.986049-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	14:48:25.986058-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	14:48:25.992480-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:25.993727-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:48:25.998840-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:48:26.004226-0500	Nexy	[0xb26afcf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:48:26.510524-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb27f28e40) Selecting device 85 from constructor
default	14:48:26.510541-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:26.510550-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:26.510956-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb27f28e40) nothing to teardown
default	14:48:26.510962-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb27f28e40) connecting device 85
default	14:48:26.511117-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb27f28e40) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:26.511251-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb27f28e40) created ioproc 0xa for device 85
default	14:48:26.511372-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 7 device listeners to device 85
default	14:48:26.511568-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 85
default	14:48:26.511576-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb27f28e40)
default	14:48:26.511660-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:26.511668-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:48:26.511676-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:26.511683-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:48:26.511693-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:48:26.511795-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:26.511807-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:26.511815-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:26.511820-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device listeners from device 0
default	14:48:26.511831-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 0
default	14:48:26.511840-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:26.511858-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:48:26.511970-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xb27f28e40) caller requesting device change from 85 to 91
default	14:48:26.511980-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:26.511985-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:26.511990-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb27f28e40) disconnecting device 85
default	14:48:26.511996-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb27f28e40) destroying ioproc 0xa for device 85
default	14:48:26.512451-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:48:26.514560-0500	Nexy	[0xb26afd180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:48:26.517812-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":{"PID":8716,"session_type":"Primary"} }
default	14:48:26.517956-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":8716}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f5019, sessionType: 'prim', isRecording: false }, 
]
default	14:48:26.518946-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 8716, name = Nexy
default	14:48:26.519310-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb26b55000 with ID: 0x1f5019
default	14:48:26.521164-0500	Nexy	[0xb26afd2c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	14:48:26.521841-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=37434934951937 }
default	14:48:26.521867-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	14:48:26.521958-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:48:26.522176-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb27f28e40) connecting device 91
default	14:48:26.522349-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb27f28e40) Device ID: 91 (Input:Yes | Output:No): true
default	14:48:26.524408-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.621, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:26.526062-0500	tccd	AUTHREQ_SUBJECT: msgID=409.621, subject=com.nexy.assistant,
default	14:48:26.526771-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:26.544660-0500	tccd	AUTHREQ_PROMPTING: msgID=409.621, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	14:48:28.324358-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    468 = "<TCCDEventSubscriber: token=468, state=Passed, csid=com.apple.photolibraryd>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
}
default	14:48:28.325253-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb27f28e40) created ioproc 0xa for device 91
default	14:48:28.325535-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 7 device listeners to device 91
default	14:48:28.325831-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 91
default	14:48:28.325845-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb27f28e40)
default	14:48:28.325861-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	14:48:28.325881-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:48:28.326101-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	14:48:28.326112-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	14:48:28.326119-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	14:48:28.326252-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:28.326267-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:28.326273-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:28.326281-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 7 device listeners from device 85
default	14:48:28.326551-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 85
default	14:48:28.326579-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:28.327208-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:48:28.329477-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.622, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:28.329971-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:48:28.331789-0500	tccd	AUTHREQ_SUBJECT: msgID=409.622, subject=com.nexy.assistant,
default	14:48:28.333452-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:28.356095-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	14:48:28.356362-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:48:28.356997-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb2a11a4f0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	14:48:28.357270-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:48:28.358458-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.623, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:28.359703-0500	tccd	AUTHREQ_SUBJECT: msgID=409.623, subject=com.nexy.assistant,
default	14:48:28.360348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:28.382467-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.624, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:28.383749-0500	tccd	AUTHREQ_SUBJECT: msgID=409.624, subject=com.nexy.assistant,
default	14:48:28.384438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:28.406066-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:48:28.406497-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:48:28.406675-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:48:28.406760-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:48:28.408200-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	14:48:28.409753-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:28.409816-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:28.409991-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	14:48:28.476950-0500	runningboardd	Assertion did invalidate due to timeout: 404-404-33081 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716])
default	14:48:28.493969-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:48:28.496392-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2713 called from <private>
default	14:48:28.496444-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:48:28.498035-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:28.498172-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:28.498192-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:28.498199-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:28.502871-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33091 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:28.503072-0500	runningboardd	Assertion 404-337-33091 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:28.504039-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:28.504614-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	14:48:28.503499-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
default	14:48:28.498485-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:28.506095-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:28.498511-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2712 called from <private>
default	14:48:28.506145-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
fault	14:48:28.506429-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
default	14:48:28.506206-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:28.506648-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:28.498518-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2712 called from <private>
default	14:48:28.508614-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:28.508678-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:28.508696-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:28.508728-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:28.510041-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:28.510052-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:28.510108-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:28.510201-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:28.510273-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:28.510363-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:28.510482-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
default	14:48:28.514957-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:28.516490-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:28.516524-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2712 called from <private>
default	14:48:28.516732-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2712 called from <private>
default	14:48:28.516944-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2712 called from <private>
default	14:48:28.517041-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2712 called from <private>
default	14:48:28.517235-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:28.517282-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:28.517318-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:28.518037-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:48:28.517515-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:28.517743-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:28.518244-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:48:28.517793-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:28.518455-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:28.517857-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2712 called from <private>
default	14:48:28.517904-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2712 called from <private>
default	14:48:28.518418-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2712 called from <private>
default	14:48:28.518450-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2712 called from <private>
default	14:48:28.518593-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:28.518665-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:28.518912-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:28.519092-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:28.519735-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:48:28.519788-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f5019, Nexy(8716), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 26 starting recording
default	14:48:28.518600-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f5019, Nexy(8716), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:48:28.519004-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:28.520545-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:28.520663-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:48:28.518697-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:28.519098-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:28.519289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:28.520785-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f5019, Nexy(8716), 'prim'', displayID:'com.nexy.assistant'}
default	14:48:28.519392-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:28.519453-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2712 called from <private>
default	14:48:28.521189-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:28.519500-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2712 called from <private>
default	14:48:28.521102-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:48:28.521013-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	14:48:28.530868-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:28.600445-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:48:28.611772-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.626, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:28.642067-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:28.642133-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:28.674355-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:28.674371-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:28.674381-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:28.674396-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:28.677221-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:28.677922-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:28.684250-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:48:28.687818-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2713 called from <private>
default	14:48:28.688342-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33095 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:28.687844-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 1 1, id:2713 called from <private>
default	14:48:28.688525-0500	runningboardd	Assertion 404-337-33095 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:28.687865-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:2713 called from <private>
default	14:48:28.687982-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:28.688771-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:48:28.689028-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:28.690246-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:28.690293-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:28.690433-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:28.691020-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:28.691267-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:48:28.691947-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:28.691991-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:28.692007-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:28.692018-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:28.692027-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:28.692049-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:28.692055-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:28.692065-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:28.692075-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:28.692320-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
default	14:48:28.692367-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2713 called from <private>
default	14:48:28.692524-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:48:28.692822-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:48:28.692943-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:28.693006-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:48:28.693034-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f5019, Nexy(8716), 'prim'', displayID:'com.nexy.assistant'}
default	14:48:28.693084-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f5019, Nexy(8716), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 26 stopping recording
default	14:48:28.693095-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:48:28.693110-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:48:28.693236-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:28.693329-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:28.693564-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:48:28.693577-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:28.693878-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:48:28.694200-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:28.694127-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:28.694243-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:28.694165-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:28.694276-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:28.694298-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:48:28.694412-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:48:28.694433-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:28.694459-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:48:28.700927-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:48:28.700999-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:48:28.701049-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:28.701282-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:28.718689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:28.718703-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:28.718714-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:28.718720-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:28.718729-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:28.718734-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:28.718821-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:28.778717-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:28.778727-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:28.778736-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:28.778796-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:28.781868-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:28.782390-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:28.805382-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb27f28e40) Selecting device 0 from destructor
default	14:48:28.805392-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:28.805397-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:28.805402-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb27f28e40) disconnecting device 91
default	14:48:28.805408-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb27f28e40) destroying ioproc 0xa for device 91
default	14:48:28.805442-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:48:28.805474-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:48:28.805603-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xb27f28e40) nothing to setup
default	14:48:28.805613-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device listeners to device 0
default	14:48:28.805617-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 0
default	14:48:28.805620-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 7 device listeners from device 91
default	14:48:28.805818-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 91
default	14:48:28.805831-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:31.209579-0500	Electron	defer invalidatation: (
    "<ElectronNSWindow: 0x10c03674a40, Nexy_v1.6.1.27 \U2014 Walkthrough>",
    "<ElectronNSWindow: 0x10c0367e180, client \U2014 Walkthrough>",
    "<ElectronNSWindow: 0x10c05115800, server \U2014 main.py>",
    "<_NSFullScreenMouseDetectionWindow: 0x10c05528540, >",
    "<_NSFullScreenMouseDetectionWindow: 0x10c05dc1b00, >",
    "<_NSFullScreenMouseDetectionWindow: 0x10c05dc0d80, >"
)
default	14:48:31.378950-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:31.389949-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:31.390014-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
default	14:48:31.390470-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2713 called from <private>
default	14:48:33.212446-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	14:48:34.294642-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	14:48:34.755948-0500	Nexy	AudioComponentPluginMgr.mm:114   registrationsChanged
default	14:48:43.811937-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb27f28e40) Selecting device 85 from constructor
default	14:48:43.811966-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:43.811980-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:43.812005-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb27f28e40) nothing to teardown
default	14:48:43.812014-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb27f28e40) connecting device 85
default	14:48:43.812218-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb27f28e40) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:43.812458-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb27f28e40) created ioproc 0xb for device 85
default	14:48:43.812674-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 7 device listeners to device 85
default	14:48:43.813055-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 85
default	14:48:43.813081-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb27f28e40)
default	14:48:43.813241-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:43.813261-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:48:43.813275-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:43.813291-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:48:43.813307-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:48:43.813523-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:43.813550-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:43.813574-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:43.813589-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device listeners from device 0
default	14:48:43.813601-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 0
default	14:48:43.813628-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:43.813659-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:48:43.813859-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xb27f28e40) caller requesting device change from 85 to 91
default	14:48:43.813883-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:43.813896-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:43.813908-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb27f28e40) disconnecting device 85
default	14:48:43.813920-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb27f28e40) destroying ioproc 0xb for device 85
default	14:48:43.813962-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:43.814097-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:48:43.814332-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb27f28e40) connecting device 91
default	14:48:43.814543-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb27f28e40) Device ID: 91 (Input:Yes | Output:No): true
default	14:48:43.818073-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.630, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:43.821374-0500	tccd	AUTHREQ_SUBJECT: msgID=409.630, subject=com.nexy.assistant,
default	14:48:43.823581-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:43.850131-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb27f28e40) created ioproc 0xb for device 91
default	14:48:43.850310-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 7 device listeners to device 91
default	14:48:43.850496-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 91
default	14:48:43.850507-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb27f28e40)
default	14:48:43.850517-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	14:48:43.850528-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:48:43.850672-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	14:48:43.850682-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	14:48:43.850689-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	14:48:43.850800-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:43.850811-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb27f28e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:43.850821-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:43.850826-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 7 device listeners from device 85
default	14:48:43.850987-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 85
default	14:48:43.851001-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:43.851011-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	14:48:43.851329-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:48:43.852581-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.631, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:43.853847-0500	tccd	AUTHREQ_SUBJECT: msgID=409.631, subject=com.nexy.assistant,
default	14:48:43.854495-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:43.872518-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb2a11a490, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	14:48:43.872703-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:48:43.873692-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.632, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:43.874702-0500	tccd	AUTHREQ_SUBJECT: msgID=409.632, subject=com.nexy.assistant,
default	14:48:43.875303-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:43.892991-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.633, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:43.893976-0500	tccd	AUTHREQ_SUBJECT: msgID=409.633, subject=com.nexy.assistant,
default	14:48:43.894572-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:43.911441-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:48:43.911640-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:48:43.913602-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2713 called from <private>
default	14:48:43.913659-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:48:43.913664-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:48:43.914845-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:43.918808-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33112 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:43.919224-0500	runningboardd	Assertion 404-337-33112 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:43.914865-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2712 called from <private>
default	14:48:43.921622-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:43.914870-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2712 called from <private>
default	14:48:43.921636-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:43.921705-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:43.921878-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:43.915729-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:43.915848-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:43.924731-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:43.915915-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:43.915952-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:43.925318-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:48:43.927737-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:43.927794-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:43.927813-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:43.927802-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2713 called from <private>
default	14:48:43.927824-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:43.927829-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2713 called from <private>
default	14:48:43.929024-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2713 called from <private>
default	14:48:43.929034-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2713 called from <private>
default	14:48:43.929044-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:43.934376-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:48:43.929080-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:43.929122-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:43.934479-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:48:43.929157-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:43.934520-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f5019, Nexy(8716), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:48:43.929203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:43.934550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:43.936244-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f5019, Nexy(8716), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:48:43.936578-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:43.936697-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:43.937068-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:48:43.937378-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f5019, Nexy(8716), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 26 starting recording
default	14:48:43.929239-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:43.934292-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:43.937800-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:43.938014-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:48:43.938819-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f5019, Nexy(8716), 'prim'', displayID:'com.nexy.assistant'}
default	14:48:43.934721-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:43.934804-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:43.936742-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:43.935106-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:43.942135-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:43.940424-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:43.942836-0500	runningboardd	Invalidating assertion 404-337-33112 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) from originator [osservice<com.apple.powerd>:337]
default	14:48:43.935363-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
default	14:48:43.939125-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	14:48:43.939250-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:43.945256-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2712 called from <private>
default	14:48:43.943339-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:43.945267-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2712 called from <private>
default	14:48:43.937572-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.634, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:43.940370-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:48:43.945388-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:43.946382-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:43.946614-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2712 called from <private>
default	14:48:43.946697-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:43.946734-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2712 called from <private>
default	14:48:43.949558-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:43.949821-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:43.949831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:43.952495-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:43.952507-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:43.952562-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:43.952572-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:43.952579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:43.952584-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:43.952589-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:43.952594-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:43.952681-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:43.952732-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:43.953062-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:43.953236-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:43.953325-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2712 called from <private>
default	14:48:43.953380-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2712 called from <private>
default	14:48:43.953493-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2712 called from <private>
default	14:48:43.971719-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:48:43.957556-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2712)
default	14:48:43.958211-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2712 called from <private>
default	14:48:43.984191-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:43.984201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:43.984213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:43.984220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:43.984227-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:43.984283-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:43.984519-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:44.001728-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:48:44.001888-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:48:44.003487-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33113 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:44.005008-0500	runningboardd	Assertion 404-337-33113 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:44.004322-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2713 called from <private>
default	14:48:44.004401-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2713 called from <private>
default	14:48:44.006962-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:44.007077-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:44.007092-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:44.007097-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:44.007674-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:48:44.007813-0500	runningboardd	Invalidating assertion 404-337-33113 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) from originator [osservice<com.apple.powerd>:337]
default	14:48:44.008230-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:44.016321-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:48:44.016448-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:48:44.016495-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.016695-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.017379-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.017389-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.017399-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.017406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.017437-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.017483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.017657-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:44.036822-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	14:48:44.040323-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:44.040388-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:48:44.048878-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:44.048901-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:44.048918-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:44.048948-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:44.051764-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:44.052360-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:44.112173-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:48:44.114180-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2713 called from <private>
default	14:48:44.116012-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33115 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:44.116197-0500	runningboardd	Assertion 404-337-33115 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:44.116693-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:44.116739-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:44.116801-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:44.116854-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:44.118954-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:48:44.119375-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:48:44.115842-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2713 called from <private>
default	14:48:44.115891-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:48:44.117897-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:44.118031-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:44.118050-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2713 called from <private>
default	14:48:44.118056-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2713 called from <private>
default	14:48:44.120007-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:44.120136-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2713 called from <private>
default	14:48:44.120176-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2713 called from <private>
default	14:48:44.120224-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
default	14:48:44.122164-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.636, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:44.125519-0500	tccd	AUTHREQ_SUBJECT: msgID=409.636, subject=com.nexy.assistant,
default	14:48:44.125804-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:44.126142-0500	runningboardd	Invalidating assertion 404-337-33115 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) from originator [osservice<com.apple.powerd>:337]
default	14:48:44.126363-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d500 at /Applications/Nexy.app
default	14:48:44.126405-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:44.130671-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:48:44.130758-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:48:44.130811-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.130948-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.132051-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.132066-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.132077-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.132121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.132132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.132150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.132431-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:44.150430-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8716] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33116 target:8716 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:44.150542-0500	runningboardd	Assertion 404-337-33116 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) will be created as active
default	14:48:44.148674-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2713 called from <private>
default	14:48:44.163722-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:48:44.163804-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:48:44.163861-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.165950-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.165961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.166038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.166070-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.166105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.166130-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.166160-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.166168-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.166186-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.166234-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.166276-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.166296-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.166558-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:44.167721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.167731-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.167740-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.167747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.167753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.167761-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.167855-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:48:44.288800-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:48:44.288995-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:48:44.289063-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:44.289109-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:48:44.289134-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f5019, Nexy(8716), 'prim'', displayID:'com.nexy.assistant'}
default	14:48:44.289175-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f5019, Nexy(8716), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 26 stopping recording
default	14:48:44.289191-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:48:44.289196-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:48:44.289222-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:44.289254-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:44.289390-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:48:44.289356-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:48:44.289371-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:44.289696-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:44.289731-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:44.289628-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:48:44.289757-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:48:44.289663-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:44.289813-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:44.289824-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:48:44.289840-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:48:44.289850-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:48:44.291038-0500	runningboardd	Invalidating assertion 404-337-33116 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8716]) from originator [osservice<com.apple.powerd>:337]
default	14:48:44.292076-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:48:44.293523-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.293534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.293543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.293549-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:44.293555-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:44.293560-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:44.293633-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:48:44.390640-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb27f28e40) Selecting device 0 from destructor
default	14:48:44.390652-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb27f28e40)
default	14:48:44.390659-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb27f28e40) not already running
default	14:48:44.390665-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb27f28e40) disconnecting device 91
default	14:48:44.390671-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb27f28e40) destroying ioproc 0xb for device 91
default	14:48:44.390702-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:48:44.390733-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:48:44.390873-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xb27f28e40) nothing to setup
default	14:48:44.390887-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device listeners to device 0
default	14:48:44.390893-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb27f28e40) adding 0 device delegate listeners to device 0
default	14:48:44.390901-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 7 device listeners from device 91
default	14:48:44.391119-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb27f28e40) removing 0 device delegate listeners from device 91
default	14:48:44.391134-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb27f28e40)
default	14:48:44.394793-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring jetsam update because this process is not memory-managed
default	14:48:44.394807-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring suspend because this process is not lifecycle managed
default	14:48:44.394817-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring GPU update because this process is not GPU managed
default	14:48:44.394835-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] Ignoring memory limit update because this process is not memory-managed
default	14:48:44.397245-0500	Nexy	[0xb26afd540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:44.397922-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:48:44.398330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:48:44.398662-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:48:44.400135-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.3, subject=com.nexy.assistant,
default	14:48:44.401298-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:48:44.422377-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[8716], responsiblePID[8716], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:48:44.422775-0500	Nexy	[0xb26afd540] invalidated after the last release of the connection object
default	14:48:44.571014-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:48:44.598135-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:48:44.599009-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	14:48:44.606724-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:48:45.194444-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	14:48:45.199783-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	14:48:45.227281-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	14:48:46.538510-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2712)
default	14:48:46.538629-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2712 called from <private>
default	14:48:46.538638-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2712 called from <private>
default	14:48:46.539201-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2713)
default	14:48:46.539247-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2713 called from <private>
default	14:48:46.539254-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2713 called from <private>
default	14:48:46.554996-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2713)
default	14:48:46.555032-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2713 called from <private>
error	14:48:49.326670-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	14:48:49.328891-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	14:48:49.497234-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:48:49.500487-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:48:54.187665-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:48:54.215080-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36400 at /Applications/Nexy.app
default	14:48:54.227149-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	14:48:54.391979-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:48:54.394537-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:48:54.442079-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:48:54.447113-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:48:59.431391-0500	Nexy	[0xb26afd540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:59.432442-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:48:59.434180-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.4, subject=com.nexy.assistant,
default	14:48:59.435483-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:48:59.465504-0500	Nexy	[0xb26afd540] invalidated after the last release of the connection object
default	14:48:59.468338-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	14:48:59.471149-0500	Nexy	[0xb26afd540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	14:48:59.471324-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	14:48:59.471941-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:48:59.482172-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:48:59.482202-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:48:59.483302-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.2, subject=com.nexy.assistant,
default	14:48:59.484021-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:48:59.512398-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.893, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:48:59.512423-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:48:59.513343-0500	tccd	AUTHREQ_SUBJECT: msgID=396.893, subject=com.nexy.assistant,
default	14:48:59.514039-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:48:59.534024-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	14:48:59.539678-0500	kernel	udp connect: [<IPv4-redacted>:49851<-><IPv4-redacted>:80] interface:  (skipped: 21)
so_gencnt: 1047040 so_state: 0x0102 process: Nexy:8716 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xbaab1d10
default	14:48:59.539820-0500	kernel	udp_connection_summary [<IPv4-redacted>:49851<-><IPv4-redacted>:80] interface: en0 (skipped: 21)
so_gencnt: 1047040 so_state: 0x0102 process: Nexy:8716 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xbaab1d10 flowctl: 0us (0x)
default	14:48:59.542007-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:48:59.542215-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:48:59.543339-0500	Nexy	nw_path_libinfo_path_check [83610892-A859-44D9-BFAC-88147415C2E2 IPv4#165a2b86:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:48:59.544441-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0D24AF79-9732-4204-8CB9-5E09AD180F99 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55242,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc165a8fe tp_proto=0x06"
default	14:48:59.544537-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55242<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047041 t_state: SYN_SENT process: Nexy:8716 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 7 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaca3e3a2
default	14:48:59.550703-0500	kernel	tcp connected: [<IPv4-redacted>:55242<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047041 t_state: ESTABLISHED process: Nexy:8716 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 7 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaca3e3a2
default	14:48:59.550791-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55242<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047041 t_state: FIN_WAIT_1 process: Nexy:8716 Duration: 0.007 sec Conn_Time: 0.006 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.000 ms rttvar: 3.000 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0xaca3e3a2
default	14:48:59.550800-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55242<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047041 t_state: FIN_WAIT_1 process: Nexy:8716 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:48:59.550967-0500	kernel	tcp listen: [<IPv4-redacted>:55243<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1047042 t_state: LISTEN process: Nexy:8716 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	14:48:59.551039-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:55243<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1047042 t_state: LISTEN process: Nexy:8716 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	14:48:59.551048-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55243<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1047042 t_state: LISTEN process: Nexy:8716 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:48:59.580796-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:48:59.580893-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:48:59.580936-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:48:59.582540-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:59.582554-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:59.582566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:59.582572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:48:59.582578-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:48:59.582586-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:48:59.582710-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:49:09.637948-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	14:49:14.555058-0500	Nexy	nw_path_libinfo_path_check [B5FDE7D5-BA56-41B1-A49E-1C2095768742 IPv4#165a2b86:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:49:14.555676-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2AB09587-4710-499A-8C4E-70AD4D7048A5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55246,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x01b19142 tp_proto=0x06"
default	14:49:14.555824-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55246<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047133 t_state: SYN_SENT process: Nexy:8716 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a5c9a51
default	14:49:14.563162-0500	kernel	tcp connected: [<IPv4-redacted>:55246<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047133 t_state: ESTABLISHED process: Nexy:8716 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a5c9a51
default	14:49:14.563266-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55246<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047133 t_state: FIN_WAIT_1 process: Nexy:8716 Duration: 0.008 sec Conn_Time: 0.008 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 8.000 ms rttvar: 4.000 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0x9a5c9a51
default	14:49:14.563282-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55246<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047133 t_state: FIN_WAIT_1 process: Nexy:8716 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:49:14.596016-0500	Nexy	[0xb26afd400] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:49:14.596441-0500	Nexy	[0xb26afd680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:49:14.597003-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:49:14.597022-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:49:14.598952-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.6, subject=com.nexy.assistant,
default	14:49:14.599590-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.5, subject=com.nexy.assistant,
default	14:49:14.599821-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7cc00 at /Applications/Nexy.app
default	14:49:14.600972-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7c900 at /Applications/Nexy.app
default	14:49:14.614387-0500	Nexy	[0xb26afd680] invalidated after the last release of the connection object
default	14:49:14.614479-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	14:49:14.615597-0500	Nexy	[0xb26afd680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:49:14.616020-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:49:14.617192-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.7, subject=com.nexy.assistant,
default	14:49:14.617634-0500	Nexy	[0xb26afd400] invalidated after the last release of the connection object
default	14:49:14.617866-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:14.633443-0500	tccd	AUTHREQ_PROMPTING: msgID=8716.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	14:49:17.374888-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    468 = "<TCCDEventSubscriber: token=468, state=Passed, csid=com.apple.photolibraryd>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
}
default	14:49:17.375451-0500	Nexy	[0xb26afd680] invalidated after the last release of the connection object
default	14:49:17.376871-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:49:17.406152-0500	Nexy	[0xb26afd680] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	14:49:17.408283-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78754.16, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78754, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	14:49:17.410583-0500	tccd	AUTHREQ_SUBJECT: msgID=78754.16, subject=com.nexy.assistant,
default	14:49:17.412112-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.438123-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78754.17, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78754, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	14:49:17.439821-0500	tccd	AUTHREQ_SUBJECT: msgID=78754.17, subject=com.nexy.assistant,
default	14:49:17.440686-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.473052-0500	Nexy	[0xb26afd400] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	14:49:17.476480-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	14:49:17.476784-0500	Nexy	<private> 0xb26b7c500: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	14:49:17.476927-0500	Nexy	<private> 0xb26b7c500: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	14:49:17.479793-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	14:49:17.520817-0500	Nexy	[0xb26afd7c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	14:49:17.521769-0500	Nexy	[0xb26afd7c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.521832-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	14:49:17.522092-0500	Nexy	Will add XPC store with options: <private> <private>
default	14:49:17.525054-0500	Nexy	[0xb26c9c280] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.525955-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.711, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.525991-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.528496-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.549288-0500	Nexy	[0xb26c9c280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.549412-0500	Nexy	[0xb26c9c280] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.549503-0500	Nexy	[0xb26c9c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.550316-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.712, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.550349-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.577955-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.713, subject=com.nexy.assistant,
default	14:49:17.600189-0500	Nexy	[0xb26c9c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.600253-0500	Nexy	[0xb26c9c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.600310-0500	Nexy	[0xb26c9c640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.601166-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.714, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.601203-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.602590-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.714, subject=com.nexy.assistant,
default	14:49:17.603496-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.625581-0500	Nexy	[0xb26c9c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.625647-0500	Nexy	[0xb26c9c640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.633542-0500	Nexy	Did add XPC store
default	14:49:17.633558-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	14:49:17.635153-0500	Nexy	0xb26b55cc0: Using cached account information
default	14:49:17.635418-0500	Nexy	[0xb27cbf750] Session created.
default	14:49:17.635428-0500	Nexy	[0xb27cbf750] Session created with Mach Service: <private>
default	14:49:17.635438-0500	Nexy	[0xb26c9cc80] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	14:49:17.635561-0500	Nexy	[0xb27cbf750] Session activated
default	14:49:17.637943-0500	Nexy	[0xb26c9cc80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.637949-0500	Nexy	[0xb27cbf750] Session canceled.
default	14:49:17.637969-0500	Nexy	[0xb27cbf750] Disposing of session
default	14:49:17.638508-0500	Nexy	[0xb26c9cc80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	14:49:17.639203-0500	Nexy	[0xb26c9cc80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.639250-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	14:49:17.639285-0500	Nexy	Will add XPC store with options: <private> <private>
default	14:49:17.641773-0500	Nexy	[0xb26c9f700] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.642802-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.715, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.642841-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.644500-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.715, subject=com.nexy.assistant,
default	14:49:17.645482-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.667840-0500	Nexy	[0xb26c9f700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.667917-0500	Nexy	[0xb26c9f700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.667990-0500	Nexy	[0xb26c9f840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.668925-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.716, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.668963-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.670542-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.716, subject=com.nexy.assistant,
default	14:49:17.671461-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.695884-0500	Nexy	[0xb26c9f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.695980-0500	Nexy	[0xb26c9f840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.696050-0500	Nexy	[0xb26c9f980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.697165-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.717, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.697202-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.698816-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.717, subject=com.nexy.assistant,
default	14:49:17.699621-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.724373-0500	Nexy	[0xb26c9f980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.724467-0500	Nexy	[0xb26c9f980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.724545-0500	Nexy	[0xb26c9fac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.725697-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.718, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.725733-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.727375-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.718, subject=com.nexy.assistant,
default	14:49:17.728225-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.756583-0500	Nexy	[0xb26c9fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.756876-0500	Nexy	[0xb26c9fac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.765945-0500	Nexy	Did add XPC store
default	14:49:17.766036-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	14:49:17.766170-0500	Nexy	[0xb26c9fd40] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	14:49:17.766885-0500	Nexy	[0xb26c9fd40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.766906-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	14:49:17.766923-0500	Nexy	Will add XPC store with options: <private> <private>
default	14:49:17.771373-0500	Nexy	[0xb26cb6800] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.772737-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.719, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.772778-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.774878-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.719, subject=com.nexy.assistant,
default	14:49:17.775810-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.800693-0500	Nexy	[0xb26cb6800] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.800781-0500	Nexy	[0xb26cb6800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.800854-0500	Nexy	[0xb26cb6940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.801964-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.720, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.801997-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.803658-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.720, subject=com.nexy.assistant,
default	14:49:17.804713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.829133-0500	Nexy	[0xb26cb6940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.829226-0500	Nexy	[0xb26cb6940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.829303-0500	Nexy	[0xb26cb6a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.830451-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.721, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.830504-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.832211-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.721, subject=com.nexy.assistant,
default	14:49:17.833041-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.857263-0500	Nexy	[0xb26cb6a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.857357-0500	Nexy	[0xb26cb6a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.857429-0500	Nexy	[0xb26cb6bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	14:49:17.858576-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.722, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.858608-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.860239-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.722, subject=com.nexy.assistant,
default	14:49:17.861044-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.882704-0500	Nexy	[0xb26cb6bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:17.882797-0500	Nexy	[0xb26cb6bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:49:17.884356-0500	Nexy	Did add XPC store
default	14:49:17.884387-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	14:49:17.906074-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.723, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.906112-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.908062-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.723, subject=com.nexy.assistant,
default	14:49:17.908893-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:17.934448-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=77359.724, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	14:49:17.934485-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=77359, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:17.936216-0500	tccd	AUTHREQ_SUBJECT: msgID=77359.724, subject=com.nexy.assistant,
default	14:49:17.937406-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:49:20.172698-0500	Nexy	[0xb26cb6f80] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	14:49:29.740483-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8806.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=8806, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:49:29.742005-0500	tccd	AUTHREQ_SUBJECT: msgID=8806.1, subject=com.nexy.assistant,
default	14:49:29.742768-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:29.758405-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.903, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=8806, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:49:29.759263-0500	tccd	AUTHREQ_SUBJECT: msgID=396.903, subject=com.nexy.assistant,
default	14:49:29.759974-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:29.798955-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:29.828906-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 631: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 160e1200 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:49:29.850805-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:29.860719-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7cc00 at /Applications/Nexy.app
default	14:49:29.878164-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	14:49:31.522284-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7c300 at /Applications/Nexy.app
default	14:49:31.528896-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:49:31.528389-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    468 = "<TCCDEventSubscriber: token=468, state=Passed, csid=com.apple.photolibraryd>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
}
default	14:49:44.744741-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8813.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=8813, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:49:44.746613-0500	tccd	AUTHREQ_SUBJECT: msgID=8813.1, subject=com.nexy.assistant,
default	14:49:44.747406-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:44.764558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.912, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=8813, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:49:44.765477-0500	tccd	AUTHREQ_SUBJECT: msgID=396.912, subject=com.nexy.assistant,
default	14:49:44.766226-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:44.805574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:44.834055-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 631: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 2a0e1200 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:49:44.852593-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:44.864079-0500	Nexy	[0xb26cb70c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:49:44.864797-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:49:44.865894-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.8, subject=com.nexy.assistant,
default	14:49:44.866641-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:44.882091-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[8716], responsiblePID[8716], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:49:44.882364-0500	Nexy	[0xb26cb70c0] invalidated after the last release of the connection object
default	14:49:44.926043-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36400 at /Applications/Nexy.app
default	14:49:44.945919-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37c00 at /Applications/Nexy.app
default	14:49:44.950161-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:49:47.104717-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	14:49:47.122597-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	14:49:47.122714-0500	Nexy	[0xb26c9c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:47.122725-0500	Nexy	[0xb26c9c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:47.122730-0500	Nexy	[0xb26c9c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:47.122739-0500	Nexy	[0xb26c9c280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:49:47.597028-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	14:49:47.762547-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	14:49:48.548222-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:49:48.548872-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	14:49:48.552303-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	14:49:48.628597-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:49:48.629498-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:49:48.629842-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:49:48.630666-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:49:48.633924-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:49:48.634114-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:49:52.432027-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36400 at /Applications/Nexy.app
default	14:49:52.458606-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:49:52.470386-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	14:49:52.648715-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:49:52.648997-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:49:52.652021-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:49:52.653023-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:49:52.702691-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:49:52.703259-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:49:52.705171-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:49:52.705513-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:49:52.705676-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:49:52.707623-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:49:56.433279-0500	Nexy	[0xb26afcf00] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	14:49:56.433382-0500	Nexy	AudioComponentPluginMgr.mm:326   registration server connection interrupted
default	14:49:59.890089-0500	Nexy	server port 0x0000d507, session port 0x00003707
default	14:49:59.891472-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.939, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:49:59.891500-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:49:59.893346-0500	tccd	AUTHREQ_SUBJECT: msgID=396.939, subject=com.nexy.assistant,
default	14:49:59.894076-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:49:59.926026-0500	Nexy	[0xb26cb70c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:49:59.926652-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:49:59.927691-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.9, subject=com.nexy.assistant,
default	14:49:59.928370-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:49:59.942487-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[8716], responsiblePID[8716], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:49:59.942727-0500	Nexy	[0xb26cb70c0] invalidated after the last release of the connection object
default	14:49:59.975745-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36400 at /Applications/Nexy.app
default	14:49:59.996001-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:50:00.000046-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:50:03.023144-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	14:50:04.151968-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	14:50:04.151942-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:04.156883-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	14:50:04.352340-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	14:50:08.454847-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d34c00 at /Applications/Nexy.app
default	14:50:08.476552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37900 at /Applications/Nexy.app
default	14:50:08.503127-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	14:50:08.547282-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:08.547626-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:08.547878-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:08.548445-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:08.549145-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:08.549448-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:08.549695-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:08.550261-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:08.586066-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:08.586129-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:08.586534-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:08.586647-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:08.587776-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:50:08.587799-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:50:15.017631-0500	Nexy	[0xb26cb7200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:50:15.018260-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:50:15.018450-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8716.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:15.019646-0500	tccd	AUTHREQ_SUBJECT: msgID=8716.10, subject=com.nexy.assistant,
default	14:50:15.020334-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37900 at /Applications/Nexy.app
default	14:50:15.039374-0500	Nexy	[0xb26cb7200] invalidated after the last release of the connection object
default	14:50:15.046016-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78754.19, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78754, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	14:50:15.060796-0500	tccd	AUTHREQ_SUBJECT: msgID=78754.19, subject=com.nexy.assistant,
default	14:50:15.062213-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37900 at /Applications/Nexy.app
default	14:50:15.085556-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	14:50:15.085921-0500	kernel	System Policy: Nexy(8716) deny(1) file-read-data /Users/sergiyzasorin/Library/Messages/chat.db
default	14:50:15.168150-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37900 at /Applications/Nexy.app
default	14:50:16.366733-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	14:50:16.489964-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	14:50:17.632222-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	14:50:17.649907-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	14:50:17.846291-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:17.846839-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:17.847106-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:17.848154-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:17.848320-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	14:50:17.848809-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	14:50:17.848922-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:17.849153-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:17.849430-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:17.849570-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:17.907597-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:17.907629-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:17.908130-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:17.908145-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:17.910226-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:50:17.910768-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:50:21.873332-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37900 at /Applications/Nexy.app
default	14:50:21.913382-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36100 at /Applications/Nexy.app
default	14:50:21.922770-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	14:50:22.080046-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:22.080327-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:22.080548-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:22.081033-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	14:50:22.081233-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:22.081829-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:22.082472-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	14:50:22.082763-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	14:50:22.083002-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	14:50:22.083225-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	14:50:22.119354-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:22.119808-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:22.120683-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	14:50:22.121110-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	14:50:22.121519-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	14:50:22.122482-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	14:50:30.219294-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78754.20, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8716, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78754, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	14:50:30.221242-0500	tccd	AUTHREQ_SUBJECT: msgID=78754.20, subject=com.nexy.assistant,
default	14:50:30.223270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d36100 at /Applications/Nexy.app
default	14:50:32.281251-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x165165 (Nexy) connectionID: CC857 pid: 8716 in session 0x101
default	14:50:32.281327-0500	WindowServer	<BSCompoundAssertion:0x76cc11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x165165 (Nexy) acq:0x76fcaf9a0 count:1
default	14:50:32.283287-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f5019","name":"Nexy(8716)"}, "details":null }
default	14:50:32.283396-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f5019 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":8716})
default	14:50:32.283423-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":8716})
default	14:50:32.285619-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:32.285785-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 8716, Name = sid:0x1f5019, Nexy(8716), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:50:32.286412-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.286525-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.287072-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x165165 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x165165 (Nexy)"
)}
default	14:50:32.285959-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.286217-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.288999-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x220c removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x165165 (Nexy)"
)}
default	14:50:32.299894-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:50:32.300335-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:50:32.301214-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.301363-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:32.307320-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.308964-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	14:50:32.308995-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2713.2414.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	14:50:32.316905-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8716] termination reported by launchd (0, 0, 0)
default	14:50:32.317044-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.317306-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.317521-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.317569-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.323503-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: none (role: None) (endowments: (null))
default	14:50:32.323751-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: none (role: None) (endowments: (null))
default	14:50:32.323935-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 8716, name = Nexy
default	14:50:32.324712-0500	gamepolicyd	Received state update for 8716 (app<application.com.nexy.assistant.57221987.57221996(501)>, none-NotVisible
default	14:50:32.324800-0500	launchservicesd	Hit the server for a process handle 851b7710000220c that resolved to: [app<application.com.nexy.assistant.57221987.57221996(501)>:8716]
default	14:50:32.328216-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x165165} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:50:32.328250-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 3
default	14:50:32.328268-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:50:32.332302-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 4
default	14:50:32.332324-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:50:35.435548-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	14:50:35.524113-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	14:50:35.524296-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	14:50:35.526160-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	14:50:35.535916-0500	runningboardd	Launch request for app<application.com.nexy.assistant.57221987.57221996(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:50:35.535981-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.57221987.57221996(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:70772] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:404-70772-33478 target:app<application.com.nexy.assistant.57221987.57221996(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:50:35.536050-0500	runningboardd	Assertion 404-70772-33478 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) will be created as active
default	14:50:35.539971-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	14:50:35.540005-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:50:35.540016-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	14:50:35.540091-0500	runningboardd	app<application.com.nexy.assistant.57221987.57221996(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	14:50:35.551513-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] is not RunningBoard jetsam managed.
default	14:50:35.551529-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] This process will not be managed.
default	14:50:35.551538-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:35.551686-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:35.554531-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:35.554631-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:404-404-33479 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:35.554754-0500	runningboardd	Assertion 404-404-33479 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:35.554918-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:35.554934-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:35.554950-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Set darwin role to: UserInteractive
default	14:50:35.554966-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:35.554996-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:35.555028-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] reported to RB as running
default	14:50:35.556509-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:8916" ID:404-366-33480 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:50:35.556600-0500	runningboardd	Assertion 404-366-33480 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:35.556754-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x193193 com.nexy.assistant starting stopped process.
default	14:50:35.557583-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:35.557617-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:35.557638-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:35.557683-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:35.557781-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:35.558948-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:35.559202-0500	runningboardd	Invalidating assertion 404-70772-33478 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:70772]
default	14:50:35.559246-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:35.559277-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:35.559305-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:35.559351-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:35.562515-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:35.556430-0500	gamepolicyd	Hit the server for a process handle 3143bfa000022d4 that resolved to: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:35.556480-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:35.557607-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	14:50:35.557744-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 2
default	14:50:35.557832-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:50:35.578916-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:35.598041-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:35.601035-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	14:50:35.635238-0500	logger	detected new pid 8916 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:35.648750-0500	Nexy	[0x10647eed0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	14:50:35.648813-0500	Nexy	[0x106478cd0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	14:50:35.661057-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:35.661077-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:35.661093-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:35.661132-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
error	14:50:35.768757-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x9fb938000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:50:35.768980-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x9fb938000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:50:35.769174-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x9fb938000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:50:35.769365-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9fb938000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:50:35.770705-0500	Nexy	[0x106482450] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:50:35.771543-0500	Nexy	[0x9fab18000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:50:35.771889-0500	Nexy	[0x9fab18140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:50:35.772325-0500	Nexy	[0x9fab18280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:50:35.773334-0500	Nexy	Received configuration update from daemon (initial)
default	14:50:35.774343-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:50:35.774722-0500	Nexy	[0x9fab183c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:50:35.775424-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8916.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:35.777112-0500	tccd	AUTHREQ_SUBJECT: msgID=8916.1, subject=com.nexy.assistant,
default	14:50:35.777829-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:35.800139-0500	Nexy	[0x9fab183c0] invalidated after the last release of the connection object
default	14:50:35.800479-0500	Nexy	server port 0x00003407, session port 0x00003407
default	14:50:35.801536-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.985, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:50:35.801562-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:35.803145-0500	tccd	AUTHREQ_SUBJECT: msgID=396.985, subject=com.nexy.assistant,
default	14:50:35.804508-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:35.840135-0500	Nexy	[0x9fab183c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:50:35.840173-0500	Nexy	[0x9fab183c0] Connection returned listener port: 0x4503
default	14:50:35.840442-0500	Nexy	[0x9fba0c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9fab183c0.peer[366].0x9fba0c300
default	14:50:35.840804-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	14:50:35.840993-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:50:35.845566-0500	Nexy	[0x9fab183c0] Connection returned listener port: 0x4503
default	14:50:35.850239-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:50:35.850760-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:50:35.854243-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] as ready
default	14:50:35.854887-0500	Nexy	Handshake succeeded
default	14:50:35.854907-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:50:35.855947-0500	Nexy	[0x9fab183c0] Connection returned listener port: 0x4503
default	14:50:35.863748-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:50:35.863766-0500	Nexy	[0x9fab188c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:50:35.863888-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:50:35.864007-0500	Nexy	[0x9fab18a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:50:36.854640-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5B2FE18D-1694-4CD8-BF23-7EB29BB947D5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55282,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf5590cb6 tp_proto=0x06"
default	14:50:36.854748-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047700 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa2eeab12
default	14:50:36.869714-0500	kernel	tcp connected: [<IPv4-redacted>:55282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047700 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa2eeab12
default	14:50:36.870007-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047700 t_state: FIN_WAIT_1 process: Nexy:8916 Duration: 0.016 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0xa2eeab12
default	14:50:36.870014-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047700 t_state: FIN_WAIT_1 process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:50:37.890084-0500	Nexy	[0x9fab18dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:50:37.890892-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8916.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:37.892189-0500	tccd	AUTHREQ_SUBJECT: msgID=8916.2, subject=com.nexy.assistant,
default	14:50:37.892925-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:37.912220-0500	Nexy	[0x9fab18dc0] invalidated after the last release of the connection object
default	14:50:37.912542-0500	Nexy	server port 0x0000810f, session port 0x00003407
default	14:50:37.913393-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.986, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:50:37.913422-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:37.914239-0500	tccd	AUTHREQ_SUBJECT: msgID=396.986, subject=com.nexy.assistant,
default	14:50:37.914859-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:37.941803-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:50:37.942573-0500	Nexy	[0x9fab18f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:50:37.943519-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"PID":8916,"session_type":"Primary"} }
default	14:50:37.943599-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:50:37.944367-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 8916, name = Nexy
default	14:50:37.944708-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9fab53ec0 with ID: 0x1f501b
default	14:50:37.944983-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:50:37.945983-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:50:37.948409-0500	Nexy	[0x9fab19040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	14:50:37.951067-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
default	14:50:37.955051-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:50:37.956860-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:50:37.957012-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:50:37.957154-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:50:37.957166-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:50:37.957201-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:50:37.957319-0500	Nexy	[0x9fab19180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:50:37.957556-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	14:50:37.957808-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8916.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:37.964342-0500	tccd	AUTHREQ_SUBJECT: msgID=8916.3, subject=com.nexy.assistant,
default	14:50:37.965199-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7c300 at /Applications/Nexy.app
default	14:50:37.982153-0500	Nexy	[0x9fab19180] invalidated after the last release of the connection object
default	14:50:37.982309-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:50:37.982352-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:50:37.982652-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	14:50:37.983918-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.637, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:37.984988-0500	tccd	AUTHREQ_SUBJECT: msgID=409.637, subject=com.nexy.assistant,
default	14:50:37.985610-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
error	14:50:38.001832-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=409, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:50:38.002715-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.639, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:38.003638-0500	tccd	AUTHREQ_SUBJECT: msgID=409.639, subject=com.nexy.assistant,
default	14:50:38.004195-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:38.018727-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:50:38.018749-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9f8443a00> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	14:50:38.033427-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	14:50:38.033438-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	14:50:38.034044-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	14:50:38.036303-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:50:38.036441-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:50:38.040687-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:50:38.041608-0500	Nexy	[0x9fab19180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	14:50:38.041971-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=38293928411137 }
default	14:50:38.042054-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	14:50:38.042085-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	14:50:38.042130-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	14:50:38.055071-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:50:38.055201-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:50:38.059326-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 122
default	14:50:38.076008-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayAndRecord, requires reconfiguration?: NO
default	14:50:38.076066-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	14:50:38.084157-0500	Nexy	[0x9fab192c0] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	14:50:38.084404-0500	Nexy	[0x9fab19400] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:50:38.086879-0500	Nexy	[0x9fab192c0] invalidated after the last release of the connection object
default	14:50:38.087610-0500	kernel	udp connect: [<IPv4-redacted>:49714<-><IPv4-redacted>:53] interface:  (skipped: 21)
so_gencnt: 1047869 so_state: 0x0102 process: Nexy:8916 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x839632ac
default	14:50:38.102550-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 21)
so_gencnt: 1047870 so_state: 0x0000 process: Nexy:8916 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	14:50:38.102560-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 21)
so_gencnt: 1047870 so_state: 0x0000 process: Nexy:8916 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	14:50:38.128523-0500	kernel	udp connect: [<IPv4-redacted>:61110<-><IPv4-redacted>:443] interface:  (skipped: 21)
so_gencnt: 1047871 so_state: 0x0002 process: Nexy:8916 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8cfc4020
default	14:50:38.128532-0500	kernel	udp_connection_summary [<IPv4-redacted>:61110<-><IPv4-redacted>:443] interface:  (skipped: 21)
so_gencnt: 1047871 so_state: 0x0002 process: Nexy:8916 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8cfc4020 flowctl: 0us (0x)
default	14:50:38.128725-0500	kernel	udp_connection_summary [<IPv4-redacted>:49714<-><IPv4-redacted>:53] interface: en0 (skipped: 21)
so_gencnt: 1047869 so_state: 0x0132 process: Nexy:8916 Duration: 0.041 sec Conn_Time: 0.041 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x839632ac flowctl: 0us (0x)
default	14:50:38.129949-0500	UserEventAgent	LocalNetwork: found bundle id com.nexy.assistant by PID
default	14:50:38.130821-0500	UserEventAgent	LocalNetwork: found bundle id com.nexy.assistant by UUID 76725A89-1121-FE40-FADA-E9F599B8BC79
default	14:50:38.130920-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B8755339-747F-42BE-951B-EE2F00C6E20B flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55285,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x2a1ef08e tp_proto=0x06"
default	14:50:38.130985-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55285<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047872 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb1a707dc
default	14:50:38.146543-0500	kernel	tcp connected: [<IPv4-redacted>:55285<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047872 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb1a707dc
default	14:50:38.510616-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9fd10c740) Selecting device 85 from constructor
default	14:50:38.510627-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fd10c740)
default	14:50:38.510632-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fd10c740) not already running
default	14:50:38.510641-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9fd10c740) nothing to teardown
default	14:50:38.510644-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fd10c740) connecting device 85
default	14:50:38.510761-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:50:38.510860-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fd10c740) created ioproc 0xa for device 85
default	14:50:38.510982-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fd10c740) adding 7 device listeners to device 85
default	14:50:38.511149-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fd10c740) adding 0 device delegate listeners to device 85
default	14:50:38.511159-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:50:38.511231-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.511239-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:50:38.511245-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.511251-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:50:38.511260-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:50:38.511348-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:50:38.511363-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:50:38.511369-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:50:38.511374-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fd10c740) removing 0 device listeners from device 0
default	14:50:38.511379-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fd10c740) removing 0 device delegate listeners from device 0
default	14:50:38.511384-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fd10c740)
default	14:50:38.511454-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:50:38.619579-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.621989-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	14:50:38.622086-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:50:38.622430-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371440, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.622551-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.628094-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.628635-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.633595-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.633990-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.636210-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371440, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.636291-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.637432-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.638688-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371440, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.638761-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371440: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.638792-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.638775-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:50:38.638879-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:50:38.638911-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:50:38.640260-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371440, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:50:38.640319-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371440: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.644007-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2F532A30-3944-4EAD-BC8D-53AB29D745EB flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55286,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6d0fda7f tp_proto=0x06"
default	14:50:38.644119-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55286<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047873 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c43d7e2
default	14:50:38.640333-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:50:38.640350-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:38.640362-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:50:38.640459-0500	Nexy	AudioConverter -> 0x9fc371440: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:50:38.640743-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371440: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.654247-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:50:38.654779-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:50:38.657711-0500	Nexy	nw_path_libinfo_path_check [C74AC781-6A83-422B-A11E-D2D157DEF75A Hostname#cf8e6f54:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:50:38.658049-0500	mDNSResponder	[R50553] DNSServiceCreateConnection START PID[8916](Nexy)
default	14:50:38.658212-0500	mDNSResponder	[R50554] DNSServiceQueryRecord START -- qname: <mask.hash: 'YBmNTGww/SUzIPiiLjQ8iw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: 2d50b096
default	14:50:38.659153-0500	mDNSResponder	[R50555] DNSServiceQueryRecord START -- qname: <mask.hash: 'YBmNTGww/SUzIPiiLjQ8iw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: 2d50b096
default	14:50:38.666354-0500	kernel	tcp connected: [<IPv4-redacted>:55286<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047873 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c43d7e2
default	14:50:38.667018-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55286<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047873 t_state: FIN_WAIT_1 process: Nexy:8916 Duration: 0.023 sec Conn_Time: 0.022 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 11.000 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0x8c43d7e2
default	14:50:38.667036-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55286<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047873 t_state: FIN_WAIT_1 process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:50:38.667511-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1BF2EF8F-6340-473D-8BFB-09D28ED9F359 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55287,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc1125ce9 tp_proto=0x06"
default	14:50:38.667557-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55287<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047885 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91bf4a46
default	14:50:38.673369-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D5AB396D-BF8F-4A18-896C-4577D1143EA3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55288,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x88ac11ee tp_proto=0x06"
default	14:50:38.673480-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55288<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047886 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a1bec72
default	14:50:38.678611-0500	kernel	tcp connected: [<IPv4-redacted>:55287<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047885 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91bf4a46
default	14:50:38.679258-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55287<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047885 t_state: FIN_WAIT_1 process: Nexy:8916 Duration: 0.012 sec Conn_Time: 0.011 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 11.000 ms rttvar: 5.500 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0x91bf4a46
default	14:50:38.679271-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55287<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1047885 t_state: FIN_WAIT_1 process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:50:38.688410-0500	kernel	tcp connected: [<IPv4-redacted>:55288<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047886 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a1bec72
default	14:50:39.803947-0500	Nexy	[0x9fab197c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	14:50:39.825685-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	14:50:39.829134-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 8916
default	14:50:39.840693-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x9fa9385a0
 (
    "<NSAquaAppearance: 0x9fa9386e0>",
    "<NSSystemAppearance: 0x9fa938780>"
)>
default	14:50:39.846092-0500	Nexy	[0x9fab19cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	14:50:39.847317-0500	Nexy	[0x9fab19e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	14:50:39.851843-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	14:50:39.852256-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	14:50:39.852333-0500	Nexy	[0x9fab19f40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:50:39.852370-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	14:50:39.852379-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	14:50:39.852411-0500	Nexy	[0x9fab1a080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	14:50:39.852416-0500	Nexy	FBSWorkspace registering source: <private>
default	14:50:39.853949-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:50:39.854028-0500	Nexy	<FBSWorkspaceScenesClient:0x9fa93ad00 <private>> attempting immediate handshake from activate
default	14:50:39.854340-0500	Nexy	<FBSWorkspaceScenesClient:0x9fa93ad00 <private>> sent handshake
default	14:50:39.854470-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	14:50:39.855050-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	14:50:39.855370-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	14:50:39.855901-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.856359-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.856498-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	14:50:39.857218-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Registering event dispatcher at init
default	14:50:39.857779-0500	ControlCenter	Created <FBWorkspace: 0x8e6abdea0; <FBApplicationProcess: 0x8e41e5e00; app<application.com.nexy.assistant.57221987.57221996>:8916(v120F3B)>>
default	14:50:39.857800-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.57221987.57221996> with intent background
default	14:50:39.858071-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	14:50:39.858506-0500	runningboardd	Launch request for app<application.com.nexy.assistant.57221987.57221996(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:50:39.858675-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.57221987.57221996(501)> from originator [osservice<com.apple.controlcenter(501)>:637] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:404-637-33498 target:app<application.com.nexy.assistant.57221987.57221996(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	14:50:39.858875-0500	runningboardd	Assertion 404-637-33498 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) will be created as active
default	14:50:39.858911-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:404-637-33498 target:app<application.com.nexy.assistant.57221987.57221996(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.859092-0500	Nexy	Requesting scene <FBSScene: 0x9fa93af80; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F> from com.apple.controlcenter.statusitems
default	14:50:39.859333-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:39.859344-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:39.859354-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:39.859374-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:39.861006-0500	Nexy	Request for <FBSScene: 0x9fa93af80; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F> complete!
default	14:50:39.861133-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	14:50:39.863188-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:39.863434-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	14:50:39.863794-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	14:50:39.864090-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	14:50:39.864130-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	14:50:39.864465-0500	Nexy	Requesting scene <FBSScene: 0x9fa93b2a0; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:50:39.864670-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:39.864784-0500	Nexy	Request for <FBSScene: 0x9fa93b2a0; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView> complete!
default	14:50:39.867122-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:39.867151-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:50:39.867156-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Bootstrap success!
default	14:50:39.867922-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Setting process visibility to: Background
default	14:50:39.868035-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] No launch watchdog for this process, dropping initial assertion in 2.0s
default	14:50:39.868453-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.controlcenter(501)>:637] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:404-637-33499 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	14:50:39.868537-0500	runningboardd	Assertion 404-637-33499 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:39.868927-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:39.868940-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:39.868976-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:39.869023-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:39.871732-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:39.872356-0500	ControlCenter	Adding: <FBApplicationProcess: 0x8e41e5e00; app<application.com.nexy.assistant.57221987.57221996>:8916(v120F3B)>
default	14:50:39.872848-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:39.872869-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:50:39.872978-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	14:50:39.872999-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Connection established.
default	14:50:39.873099-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x8e6c26bc0>
default	14:50:39.873123-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Connection to remote process established!
default	14:50:39.873147-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:39.873311-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:39.881509-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.881536-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e41e5e00; app<application.com.nexy.assistant.57221987.57221996>:8916(v120F3B)>
default	14:50:39.881715-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Registered new scene: <FBWorkspaceScene: 0x8e6d40f00; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F> (fromRemnant = 0)
default	14:50:39.881763-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Workspace interruption policy did change: reconnect
default	14:50:39.882185-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.controlcenter(501)>:637] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:404-637-33500 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	14:50:39.882283-0500	runningboardd	Assertion 404-637-33500 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as inactive as originator process has not exited
default	14:50:39.882522-0500	ControlCenter	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Client process connected: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.882535-0500	Nexy	Request for <FBSScene: 0x9fa93af80; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F> complete!
default	14:50:39.883331-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.883347-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e41e5e00; app<application.com.nexy.assistant.57221987.57221996>:8916(v120F3B)>
default	14:50:39.883399-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.controlcenter(501)>:637] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:404-637-33501 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	14:50:39.883407-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Registered new scene: <FBWorkspaceScene: 0x8e6d41440; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	14:50:39.883533-0500	runningboardd	Assertion 404-637-33501 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:39.883562-0500	Nexy	Request for <FBSScene: 0x9fa93b2a0; com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView> complete!
default	14:50:39.883560-0500	ControlCenter	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:39.883654-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	14:50:39.883980-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:39.883991-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:39.884001-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:39.884053-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:39.884362-0500	Nexy	<FBSWorkspaceScenesClient:0x9fa93ad00 <private>> Reconnecting scene com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F
default	14:50:39.884692-0500	Nexy	<FBSWorkspaceScenesClient:0x9fa93ad00 <private>> Reconnecting scene com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView
default	14:50:39.886917-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:39.887495-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:39.887782-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:39.889802-0500	Nexy	Registering for test daemon availability notify post.
default	14:50:39.889972-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:50:39.890088-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:50:39.890182-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:50:39.891789-0500	Nexy	[0x9fab1a440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	14:50:39.900222-0500	Nexy	[0x9fab183c0] Connection returned listener port: 0x4503
default	14:50:39.900815-0500	Nexy	SignalReady: pid=8916 asn=0x0-0x193193
default	14:50:39.901360-0500	Nexy	SIGNAL: pid=8916 asn=0x0x-0x193193
default	14:50:39.902367-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	14:50:39.906449-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:39.913041-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:39.916290-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:39.918076-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:50:39.918083-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	14:50:39.918126-0500	Nexy	[0x9fab192c0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	14:50:39.918234-0500	Nexy	[0x9fab192c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:50:39.919713-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:50:39.923477-0500	Nexy	[C:2] Alloc <private>
default	14:50:39.923516-0500	Nexy	[0x9fab192c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:50:39.925229-0500	Nexy	[0x9fab1a800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:50:39.925770-0500	WindowManager	Connection activated | (8916) Nexy
default	14:50:39.926008-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-8916). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
error	14:50:39.926199-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:50:39.926310-0500	Nexy	[0x9fab1a800] invalidated after the last release of the connection object
default	14:50:39.928214-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-8916)
default	14:50:39.928903-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(2BBF3102, (bid:com.nexy.assistant-Item-0-8916)) for (bid:com.nexy.assistant-Item-0-8916)
default	14:50:39.929430-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	14:50:39.930044-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-8916)]
default	14:50:39.931224-0500	ControlCenter	Created instance DisplayableId(341550DD) in .menuBar for DisplayableAppStatusItemType(2BBF3102, (bid:com.nexy.assistant-Item-0-8916)) .menuBar
default	14:50:39.942167-0500	ControlCenter	Created ephemaral instance DisplayableId(341550DD) for (bid:com.nexy.assistant-Item-0-8916) with positioning .ephemeral
default	14:50:40.233926-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:40.235158-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:40.244509-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	14:50:40.249330-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:50:40.250107-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	14:50:40.250220-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:50:40.269429-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:40.353262-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	14:50:40.358628-0500	Nexy	Start service name com.apple.spotlightknowledged
default	14:50:40.359647-0500	Nexy	[GMS] availability notification token 96
default	14:50:40.426459-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppDrawing" ID:404-396-33502 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:40.426588-0500	runningboardd	Assertion 404-396-33502 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:40.427000-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:40.427012-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:40.427023-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:40.427061-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:40.431010-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:40.431734-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:40.431969-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:40.453119-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	14:50:40.453320-0500	runningboardd	Invalidating assertion 404-637-33501 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.controlcenter(501)>:637]
default	14:50:40.556977-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:40.557020-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:40.557044-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:40.557080-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:40.561541-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:40.562282-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:40.562411-0500	runningboardd	Assertion did invalidate due to timeout: 404-404-33479 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916])
default	14:50:40.562716-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:40.762499-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:40.762536-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:40.762597-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:40.762697-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:40.768609-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:40.770762-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:40.771279-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:41.960959-0500	runningboardd	Invalidating assertion 404-637-33498 (target:app<application.com.nexy.assistant.57221987.57221996(501)>) from originator [osservice<com.apple.controlcenter(501)>:637]
default	14:50:42.062386-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:50:42.063431-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:42.063451-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:42.063472-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:42.063512-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:42.068422-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:42.078147-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:42.078402-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:44.831563-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	14:50:46.230357-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	14:50:47.160496-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:47.209054-0500	Nexy	[0x9f87dc280] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:50:47.209939-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8916.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:47.212446-0500	tccd	AUTHREQ_SUBJECT: msgID=8916.5, subject=com.nexy.assistant,
default	14:50:47.213577-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:47.236776-0500	Nexy	[0x9f87dc280] invalidated after the last release of the connection object
default	14:50:47.237021-0500	Nexy	[0x9f87dc280] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:50:47.237545-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8916.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:50:47.238495-0500	tccd	AUTHREQ_SUBJECT: msgID=8916.6, subject=com.nexy.assistant,
default	14:50:47.240089-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:47.259484-0500	Nexy	[0x9f87dc280] invalidated after the last release of the connection object
default	14:50:47.259565-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:50:47.260190-0500	Nexy	[0x9f87dc280] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	14:50:47.260320-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	14:50:47.260448-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:50:47.262535-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:50:47.262562-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:47.263480-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.3, subject=com.nexy.assistant,
default	14:50:47.264144-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:47.294456-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=396.994, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:50:47.294480-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=396, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:47.295373-0500	tccd	AUTHREQ_SUBJECT: msgID=396.994, subject=com.nexy.assistant,
default	14:50:47.296015-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:47.351299-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	14:50:47.365799-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
fault	14:50:47.368287-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.57221987.57221996 AUID=501> and <type=Application identifier=application.com.nexy.assistant.57221987.57221996>
default	14:50:47.381594-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:47.381654-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:50:47.381690-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:50:47.633676-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371440: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:47.633764-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371440: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:47.633908-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x9fab446c0: start, was running 0
default	14:50:47.634949-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33508 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:50:47.635020-0500	runningboardd	Assertion 404-8916-33508 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:47.637197-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33509 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:47.637253-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:47.637363-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:47.637305-0500	runningboardd	Assertion 404-337-33509 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:47.637376-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:47.637482-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:47.640475-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:47.640753-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:47.640765-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:47.640789-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:47.640830-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:47.640924-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:47.641083-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:47.643322-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:47.643814-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:47.643961-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:47.685566-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:50:47.686198-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:50:47.686276-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:50:47.686319-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:50:47.686364-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:50:47.686394-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.686398-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:50:47.686520-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.686450-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 starting playing
default	14:50:47.686551-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.686541-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:47.686593-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:50:47.686640-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:47.686722-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:50:47.686750-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:50:47.686825-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:50:47.686836-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:50:47.686911-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:50:47.687093-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.687167-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.687192-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:47.687203-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:50:47.687221-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:50:50.819412-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	14:50:54.390450-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:55.036145-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:55.038930-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9fda3e340) Selecting device 85 from constructor
default	14:50:55.038943-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:50:55.038948-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:50:55.038952-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9fda3e340) nothing to teardown
default	14:50:55.038954-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 85
default	14:50:55.039037-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 85 (Input:No | Output:Yes): true
default	14:50:55.039247-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xb for device 85
default	14:50:55.039431-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 85
default	14:50:55.039575-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 85
default	14:50:55.039583-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:50:55.039649-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:50:55.039659-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:50:55.039665-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:50:55.039678-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:50:55.039685-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:50:55.039769-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:50:55.039779-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:50:55.039784-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:50:55.039788-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device listeners from device 0
default	14:50:55.039794-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 0
default	14:50:55.039798-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:50:55.039809-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:50:55.039858-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9fda3e340) caller requesting device change from 85 to 91
default	14:50:55.039865-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:50:55.039870-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:50:55.039872-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 85
default	14:50:55.039877-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xb for device 85
default	14:50:55.039890-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:55.040087-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:55.040391-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 91
default	14:50:55.040462-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 91 (Input:Yes | Output:No): true
default	14:50:55.041557-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.640, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.042058-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:50:55.042082-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:50:55.043088-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:50:55.043106-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:50:55.043272-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:50:55.043303-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:55.043488-0500	tccd	AUTHREQ_SUBJECT: msgID=409.640, subject=com.nexy.assistant,
default	14:50:55.044226-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:55.044279-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.4, subject=com.nexy.assistant,
default	14:50:55.045097-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:55.070300-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xa for device 91
default	14:50:55.070450-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 91
default	14:50:55.070664-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 91
default	14:50:55.070676-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:50:55.070683-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	14:50:55.070693-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:50:55.070914-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	14:50:55.070923-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	14:50:55.070928-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	14:50:55.071036-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:50:55.071044-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:50:55.071048-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:50:55.071053-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 85
default	14:50:55.071202-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 85
default	14:50:55.071212-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:50:55.071765-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:50:55.072751-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.641, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.073760-0500	tccd	AUTHREQ_SUBJECT: msgID=409.641, subject=com.nexy.assistant,
default	14:50:55.074336-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:55.090327-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:50:55.091341-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:50:55.091367-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:50:55.092363-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.5, subject=com.nexy.assistant,
default	14:50:55.093178-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:50:55.093621-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:50:55.095158-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.642, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.096199-0500	tccd	AUTHREQ_SUBJECT: msgID=409.642, subject=com.nexy.assistant,
default	14:50:55.096779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:55.115035-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.643, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.116033-0500	tccd	AUTHREQ_SUBJECT: msgID=409.643, subject=com.nexy.assistant,
default	14:50:55.116628-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:55.126157-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:50:55.137176-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:50:55.137303-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:50:55.137942-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	14:50:55.138814-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:50:55.138876-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:50:55.210975-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:50:55.212168-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:50:55.212203-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:50:55.212234-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:50:55.212793-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:50:55.212811-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:50:55.213289-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:50:55.213397-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:50:55.213517-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:50:55.213553-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:50:55.214324-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:50:55.214349-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:50:55.214382-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:50:55.215117-0500	runningboardd	Invalidating assertion 404-8916-33508 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:55.214392-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:50:55.223113-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:50:55.223948-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:50:55.214469-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:50:55.214602-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:50:55.214940-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:50:55.214982-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:50:55.226027-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:50:55.226048-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:50:55.226089-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:50:55.226150-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:50:55.229250-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:50:55.229259-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:50:55.229310-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:50:55.216993-0500	runningboardd	Invalidating assertion 404-337-33509 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:50:55.229383-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:50:55.229455-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:50:55.229518-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:50:55.233534-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33514 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:50:55.233855-0500	runningboardd	Assertion 404-8916-33514 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:55.229579-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:50:55.232338-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:50:55.232340-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:50:55.236679-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:50:55.237178-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:50:55.234869-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2743 called from <private>
default	14:50:55.234905-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2743 called from <private>
default	14:50:55.235162-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:50:55.236463-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:50:55.236501-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:50:55.238068-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:50:55.238128-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:50:55.238168-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:50:55.238202-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:50:55.238236-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:50:55.238487-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2743 called from <private>
default	14:50:55.238492-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2743 called from <private>
default	14:50:55.238527-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:50:55.238574-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:50:55.238612-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:50:55.238647-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:50:55.238719-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:50:55.238754-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:50:55.238779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:50:55.238830-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:50:55.239773-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.644, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.238895-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:50:55.238924-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:50:55.238977-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:50:55.239022-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:50:55.239051-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:50:55.239100-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:50:55.244757-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:50:55.244765-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:50:55.244889-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:50:55.246428-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:50:55.246607-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:50:55.246678-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:50:55.246828-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:50:55.251677-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:50:55.251741-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:50:55.251921-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:50:55.252058-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:50:55.252263-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:50:55.252454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:50:55.252655-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:50:55.252742-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:50:55.252928-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:50:55.253448-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:50:55.253632-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:50:55.253742-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:50:55.253815-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:50:55.253881-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:50:55.253947-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:50:55.254009-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:50:55.273413-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	14:50:55.273654-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:50:55.273724-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:50:55.273811-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:50:55.273910-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.274101-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:55.274182-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:50:55.274286-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.274449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:55.274539-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:50:55.274629-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.274705-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f501b, Nexy(8916), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 28 starting recording
default	14:50:55.274797-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:50:55.280210-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	14:50:55.279382-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	14:50:55.280674-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:50:55.280350-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:50:55.281594-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.281709-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.281759-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.282016-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.281985-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.282957-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:50:55.282190-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:50:55.294440-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:50:55.294657-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.294692-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.294585-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.294719-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	14:50:55.294626-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.294657-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.294754-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:50:55.294836-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.295016-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.295222-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.295317-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:50:55.295598-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:55.295721-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:50:55.301590-0500	runningboardd	Invalidating assertion 404-337-33519 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:50:55.301788-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33521 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:55.301839-0500	runningboardd	Assertion 404-337-33521 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:55.302221-0500	runningboardd	Invalidating assertion 404-337-33521 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:50:55.302414-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33522 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:55.302469-0500	runningboardd	Assertion 404-337-33522 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:55.333201-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:50:55.333482-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:50:55.349684-0500	tccd	AUTHREQ_SUBJECT: msgID=409.645, subject=com.nexy.assistant,
default	14:50:55.349893-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.350903-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:50:55.358100-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.358197-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:50:55.358256-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:50:55.358907-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.358952-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.358971-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.358979-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359029-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.359040-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.359061-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359107-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.359114-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.359133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.359149-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359163-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359177-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.359180-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:50:55.359188-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.359245-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.359288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.359325-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:50:55.365292-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.365355-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:50:55.365400-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:50:55.365417-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:50:55.401371-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:50:55.401467-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:50:55.427831-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:55.428147-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:55.444628-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:55.444644-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:55.444657-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:55.444680-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:55.449161-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:55.452542-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:55.453144-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:50:55.455008-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33525 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:55.455108-0500	runningboardd	Assertion 404-337-33525 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:55.455673-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:50:55.455723-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:2737 called from <private>
default	14:50:55.457355-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:50:55.457725-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:55.457741-0500	runningboardd	Invalidating assertion 404-8916-33524 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:55.457372-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:50:55.457814-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:55.457664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2737 called from <private>
default	14:50:55.463007-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.646, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:50:55.463779-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:55.464209-0500	runningboardd	Invalidating assertion 404-8916-33526 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:55.464400-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33527 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:50:55.464497-0500	runningboardd	Assertion 404-8916-33527 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:50:55.464811-0500	runningboardd	Invalidating assertion 404-337-33525 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:50:55.469755-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.477253-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.477327-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:50:55.477375-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:50:55.478027-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478039-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478070-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478085-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.478106-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478172-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478203-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478210-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.478228-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478246-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:50:55.478250-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478261-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.478271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.478301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.478379-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:50:55.484158-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.484229-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:50:55.484282-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:50:55.484298-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:50:55.506755-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:55.513366-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.513392-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.513408-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.513428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.513438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.513447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.513458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.513500-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:50:55.513505-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.513571-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.513670-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.513746-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:55.514015-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:50:55.513935-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:55.514681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:55.558033-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:55.558335-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:58.316685-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:50:58.867268-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:50:58.867927-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:50:58.868079-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:58.868158-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:50:58.868195-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:58.868247-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:50:58.868252-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f501b, Nexy(8916), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 28 stopping recording
default	14:50:58.868275-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:50:58.868304-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:58.868334-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:50:58.868556-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:50:58.868602-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:50:58.868629-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:50:58.869138-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:58.871066-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:58.871479-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:58.871515-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:50:58.871613-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:58.871639-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:50:58.871438-0500	runningboardd	Invalidating assertion 404-8916-33527 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:50:58.869004-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:50:58.871529-0500	runningboardd	Invalidating assertion 404-337-33528 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:50:58.869081-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:50:58.880207-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:50:58.880378-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:50:58.880477-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:50:58.880497-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:50:58.881243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:58.881264-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:58.881283-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:58.881293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:50:58.881304-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:50:58.881331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:50:58.881582-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:50:58.893627-0500	Nexy	nw_path_libinfo_path_check [7DF47A37-42B9-41E6-B37A-714698221AF3 Hostname#3db1d101:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:50:58.893830-0500	mDNSResponder	[R50629] DNSServiceQueryRecord START -- qname: <mask.hash: 'RtrA/jBwUcahoEP0EKQp9Q=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: b360ab20
default	14:50:58.894635-0500	mDNSResponder	[R50630] DNSServiceQueryRecord START -- qname: <mask.hash: 'RtrA/jBwUcahoEP0EKQp9Q=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: b360ab20
default	14:50:58.915291-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8D081032-BAF4-491C-9D12-96486D4A6EE5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55311,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xc4f4f95c tp_proto=0x06"
default	14:50:58.915400-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55311<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1048761 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85654c81
default	14:50:58.921220-0500	kernel	tcp connected: [<IPv4-redacted>:55311<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1048761 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85654c81
default	14:50:58.971694-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9fda3e340) Selecting device 0 from destructor
default	14:50:58.971713-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:50:58.971724-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:50:58.971729-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 91
default	14:50:58.971741-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xa for device 91
default	14:50:58.971793-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	14:50:58.971837-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:50:58.972057-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9fda3e340) nothing to setup
default	14:50:58.972074-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device listeners to device 0
default	14:50:58.972081-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 0
default	14:50:58.972090-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 91
default	14:50:58.972341-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 91
default	14:50:58.972362-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:50:58.978995-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:50:58.979021-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:50:58.979031-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:50:58.979048-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:50:58.981775-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:50:58.982254-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:58.982423-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:50:59.666013-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:55311<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1048761 t_state: LAST_ACK process: Nexy:8916 Duration: 0.751 sec Conn_Time: 0.006 sec bytes in/out: 842/80764 pkts in/out: 4/10 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 7.750 ms rttvar: 2.625 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x85654c81
default	14:50:59.666039-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55311<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1048761 t_state: LAST_ACK process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:00.808422-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:00.808547-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:01.093338-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:01.093429-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:01.093450-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:01.093677-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:01.093723-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:01.093740-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:01.095750-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:01.095757-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:01.095781-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:01.095803-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2737 called from <private>
default	14:51:01.095837-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:01.095851-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:01.106034-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:01.106070-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:01.106679-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:01.106715-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:01.106726-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:01.108650-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:01.108683-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:01.108917-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:01.108979-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2737 called from <private>
default	14:51:01.110979-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:01.111063-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:01.111151-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:01.111788-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:01.111972-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:01.112034-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:01.112232-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:01.112289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:01.112351-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:01.112427-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:01.112461-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:01.112977-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2743 called from <private>
default	14:51:01.113334-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2743 called from <private>
default	14:51:01.113389-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:01.113997-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:01.114532-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:01.114675-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:01.113574-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:01.114872-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:01.114917-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:01.114931-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:01.115000-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:01.116915-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:01.115031-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:01.117557-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:01.115947-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:01.116200-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:01.116266-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:01.116312-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:01.116339-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:01.118752-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:01.118962-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2743 called from <private>
default	14:51:01.118976-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2743 called from <private>
default	14:51:01.119020-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:01.119029-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:01.119036-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:51:01.119043-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:51:01.119151-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:01.119374-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:01.119476-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:51:01.119524-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:51:01.133177-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:01.133208-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:01.133384-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:01.137665-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:01.137897-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:01.137911-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:01.137948-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:01.137959-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:01.137965-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:01.137972-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:01.140428-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:01.140472-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:51:01.140630-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.140641-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:01.140649-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.140660-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:01.140669-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:01.140818-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:01.140863-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:01.140875-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:01.141563-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:01.141582-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:51:01.144421-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.144460-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:01.144469-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.144484-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:01.144495-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:01.144660-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:01.144690-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:01.144700-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:01.252688-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x9fab446c0: iounit configuration changed > posting notification
default	14:51:03.049918-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:03.050019-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:03.256243-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc3704b0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:03.256278-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc3704b0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:03.256294-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:03.256295-0500	Nexy	AudioConverter -> 0x9fc3704b0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:03.256313-0500	Nexy	AudioConverter -> 0x9fc3704b0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:03.256319-0500	Nexy	AudioConverter -> 0x9fc3704b0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:03.256957-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc3704b0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:03.257262-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x9fab446c0: start, was running 0
default	14:51:03.259128-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33532 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:03.259255-0500	runningboardd	Assertion 404-8916-33532 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:03.259716-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:03.259716-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33533 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:03.259731-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:03.259743-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:03.259782-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:03.259788-0500	runningboardd	Assertion 404-337-33533 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:03.263179-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:03.263475-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:03.263489-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:03.263500-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:03.263540-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:03.263853-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:03.264152-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:03.267204-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:03.267869-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:03.268023-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:03.554538-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:03.555525-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:51:03.555672-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:03.555711-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:51:03.555747-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:03.555794-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:51:03.555823-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.555849-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:51:03.555860-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 starting playing
default	14:51:03.555944-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:03.555989-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:51:03.556015-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:03.556009-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.556071-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.556309-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:51:03.556057-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:51:03.556328-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:03.556327-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:03.556092-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:51:03.556561-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.556638-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.556667-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:03.556682-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	14:51:03.556691-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:51:03.556704-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	14:51:03.556761-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:03.556828-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:51:04.802820-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:05.529439-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:51:05.530399-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:51:07.498337-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:07.500201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:07.500230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:07.500271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:07.500288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:07.500305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:07.500320-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:07.500519-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:08.938761-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:16.196789-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:51:16.196860-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:51:16.802804-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:18.881800-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:19.805763-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:22.802762-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:25.802792-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:28.802690-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:31.729288-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:34.802768-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:37.805727-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:51:38.400831-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:38.403090-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9fda3e340) Selecting device 85 from constructor
default	14:51:38.403114-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:38.403125-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:38.403131-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9fda3e340) nothing to teardown
default	14:51:38.403136-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 85
default	14:51:38.403326-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:38.403842-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xc for device 85
default	14:51:38.404053-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 85
default	14:51:38.404345-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 85
default	14:51:38.404383-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:51:38.404500-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:38.404516-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:38.404525-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:38.404546-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:38.404561-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:38.404712-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:38.404732-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:38.404742-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:38.404751-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device listeners from device 0
default	14:51:38.404757-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 0
default	14:51:38.404762-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:38.404792-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:51:38.405005-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9fda3e340) caller requesting device change from 85 to 91
default	14:51:38.405024-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:38.405033-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:38.405040-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 85
default	14:51:38.405046-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xc for device 85
default	14:51:38.405072-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	14:51:38.405411-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:38.405932-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 91
default	14:51:38.406119-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 91 (Input:Yes | Output:No): true
default	14:51:38.408806-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.647, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:38.411190-0500	tccd	AUTHREQ_SUBJECT: msgID=409.647, subject=com.nexy.assistant,
default	14:51:38.412749-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.412947-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:51:38.413011-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:51:38.415167-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:51:38.415195-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:38.416512-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.6, subject=com.nexy.assistant,
default	14:51:38.417582-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:51:38.433881-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xb for device 91
default	14:51:38.434020-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 91
default	14:51:38.434195-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 91
default	14:51:38.434205-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:51:38.434215-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	14:51:38.434225-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:38.434351-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	14:51:38.434361-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	14:51:38.434367-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	14:51:38.434451-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:38.434464-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:38.434469-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:38.434473-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 85
default	14:51:38.434626-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 85
default	14:51:38.434636-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:38.434644-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	14:51:38.435426-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:38.436470-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.648, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:38.437557-0500	tccd	AUTHREQ_SUBJECT: msgID=409.648, subject=com.nexy.assistant,
default	14:51:38.438177-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.440450-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:51:38.440481-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:51:38.456882-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:51:38.457942-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:51:38.457967-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:38.459023-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:38.459407-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.7, subject=com.nexy.assistant,
default	14:51:38.460402-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.649, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:38.460755-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:51:38.462172-0500	tccd	AUTHREQ_SUBJECT: msgID=409.649, subject=com.nexy.assistant,
default	14:51:38.463381-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.487442-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.487554-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:38.487586-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:38.491238-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.650, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:38.493149-0500	tccd	AUTHREQ_SUBJECT: msgID=409.650, subject=com.nexy.assistant,
default	14:51:38.494229-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.508177-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:51:38.521161-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:51:38.521327-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:51:38.522955-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:51:38.523004-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:38.523356-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:38.523386-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:38.523391-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:38.523463-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:38.523488-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:38.523586-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:38.524585-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:38.524667-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:38.524698-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:38.525350-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:38.525675-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:38.526102-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:38.526222-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:38.526259-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:38.529898-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:38.530267-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:38.532306-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:38.532329-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:38.532340-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:38.532351-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:38.532594-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:38.532604-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:38.532618-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:38.532677-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:38.532757-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:38.532795-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:38.532854-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:38.539191-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:38.539241-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:38.539627-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:38.525496-0500	runningboardd	Invalidating assertion 404-8916-33532 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:38.539616-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:38.540755-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:38.540782-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:38.541245-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:38.541539-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:38.541810-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:38.543684-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:38.528028-0500	runningboardd	Invalidating assertion 404-337-33533 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:38.542901-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33555 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:38.543253-0500	runningboardd	Assertion 404-8916-33555 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:38.544909-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:38.544982-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:38.545032-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:38.545073-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:38.545145-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:38.545322-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:38.546897-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:38.546946-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:38.558808-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
error	14:51:38.627444-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:38.642463-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.647226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.647241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.647253-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.647260-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.647301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.647335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.647627-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:38.654854-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.655250-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:38.655364-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:38.655421-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:38.699489-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:38.696729-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:38.698029-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:38.698069-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:38.699984-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:38.698311-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:38.701335-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:38.709322-0500	tccd	AUTHREQ_SUBJECT: msgID=409.652, subject=com.nexy.assistant,
default	14:51:38.712332-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.712682-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.721735-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.731189-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.731309-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:38.731376-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:38.731415-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:38.743858-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.743906-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.743928-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.743940-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.743948-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.743957-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.744147-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:38.750607-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:38.751694-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:38.751857-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	14:51:38.752165-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:38.754077-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 issue_detected_sample_time=80640.000000 ] -- [ rms:[-18.566854], peaks:[-1.381792] ]
default	14:51:38.754168-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-24.551903], peaks:[-6.741776] ]
default	14:51:38.754137-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x9fab446c0: iounit configuration changed > posting notification
default	14:51:38.754554-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:51:38.754638-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:51:38.837258-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:51:38.839719-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2737 called from <private>
default	14:51:38.839751-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:51:38.840617-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:38.841649-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:38.841680-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:38.841694-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:38.841706-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:38.841742-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:38.841814-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33561 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:38.841801-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:38.841901-0500	runningboardd	Assertion 404-337-33561 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:38.841865-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:38.841917-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:38.842335-0500	runningboardd	Invalidating assertion 404-8916-33560 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:38.842376-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:38.842518-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:38.842603-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:38.842756-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:38.842904-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:38.843388-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:38.843808-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:38.844157-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:38.844172-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:38.844188-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:38.844837-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33562 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:38.844926-0500	runningboardd	Assertion 404-8916-33562 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:38.846585-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.653, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:38.848449-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:38.848591-0500	tccd	AUTHREQ_SUBJECT: msgID=409.653, subject=com.nexy.assistant,
default	14:51:38.848965-0500	runningboardd	Invalidating assertion 404-337-33561 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:38.850047-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:38.853060-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:38.854336-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:38.854392-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.860383-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.860459-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:51:38.860511-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:38.860882-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.860901-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.860914-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.860925-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.860937-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.860945-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.860965-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.860979-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.860989-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.860996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.861006-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.861012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.861028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.861040-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.861049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.861058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.861067-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.861076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.861093-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:38.861118-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:38.867726-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:38.867791-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:38.867841-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:38.867857-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:38.878890-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.878916-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.878932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.878941-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:38.878950-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:38.878957-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:38.879070-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:38.884856-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33563 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:38.884944-0500	runningboardd	Assertion 404-337-33563 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:38.882728-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2737 called from <private>
default	14:51:38.896387-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
error	14:51:38.943795-0500	Nexy	        HALB_IOThread.cpp:327    HALB_IOThread::_Start: there already is a thread
default	14:51:38.943909-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:51:38.945107-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:51:38.945214-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:38.945251-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:51:38.945291-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:38.945348-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:51:38.945391-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945419-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:38.945468-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:38.945553-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945558-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945557-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:51:38.945575-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f501b, Nexy(8916), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 28 starting recording
default	14:51:38.945624-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945681-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:38.945718-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:38.945790-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945831-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:38.945750-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:38.945854-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	14:51:38.945869-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:38.945811-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:38.946032-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:38.946266-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:38.946356-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:38.946391-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:38.946407-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:51:38.946418-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:51:38.946429-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	14:51:38.946482-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	14:51:38.946552-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:39.904813-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:40.727262-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	14:51:41.128350-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371c80, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:41.128393-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:41.129064-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:41.130080-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371c80, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:41.130110-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371c80: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:41.130117-0500	Nexy	AudioConverter -> 0x9fc371c80: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:41.130126-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:41.130135-0500	Nexy	AudioConverter -> 0x9fc371c80: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:41.130143-0500	Nexy	AudioConverter -> 0x9fc371c80: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:41.131222-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371cb0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:41.131236-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371cb0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:41.131246-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:41.131242-0500	Nexy	AudioConverter -> 0x9fc371cb0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:41.131256-0500	Nexy	AudioConverter -> 0x9fc371cb0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:41.131263-0500	Nexy	AudioConverter -> 0x9fc371cb0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:41.131464-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371cb0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:41.131738-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x9fab446c0: start, was running 0
default	14:51:41.133586-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:41.135004-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	14:51:41.135128-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:41.135164-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 200
default	14:51:41.135201-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:41.135231-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.135288-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:41.135281-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	14:51:41.135319-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:41.135375-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:41.135406-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.135544-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.135456-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode PlayAndRecord_WithBluetooth/Default and coreSessionID = 28 starting playing
default	14:51:41.135508-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: Bumping the mode to Voice chat for session as session started playing = <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:41.135535-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:41.135555-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 200
default	14:51:41.135582-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	14:51:41.135608-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.135636-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (200) and New (501) scores.
default	14:51:41.135708-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: true }, 
]
default	14:51:41.135804-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	14:51:41.135787-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:41.135950-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.136363-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	14:51:41.136631-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.137131-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.137290-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.137362-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:41.137471-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.137572-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	14:51:41.137691-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:41.137710-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.137759-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:41.137922-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:41.138010-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	14:51:41.138061-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 501 count 1
default	14:51:41.138092-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
default	14:51:41.136960-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.135823-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
error	14:51:41.138158-0500	audioaccessoryd	Updating local audio category 200 -> 501 app com.nexy.assistant
default	14:51:41.137037-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.137159-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
error	14:51:41.138210-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 501,
}
default	14:51:41.138358-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	14:51:41.161801-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:41.629156-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:51:41.630491-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:51:41.630676-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:41.630722-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	14:51:41.630764-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:41.630799-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.630856-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:51:41.630863-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:41.630907-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:41.630942-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:41.630965-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.631052-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:41.631083-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:41.631108-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.631153-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f501b, Nexy(8916), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 28 stopping recording
default	14:51:41.631181-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:41.631218-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.631212-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:51:41.631233-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:41.631258-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:51:41.631386-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:51:41.631408-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:41.631489-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:41.631664-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.632800-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:41.633044-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.633260-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:51:41.633395-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:41.633562-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633605-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633635-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633660-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:41.633662-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633692-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633708-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633725-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	14:51:41.633737-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:51:41.633749-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	14:51:41.633764-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633799-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
error	14:51:41.633819-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	14:51:41.633888-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:41.633899-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633908-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:41.633936-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:41.633946-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:41.633955-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:41.633982-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:41.633991-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:41.634001-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 1
default	14:51:41.634012-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:51:41.634021-0500	audioaccessoryd	Updating local audio category 200 -> 201 app com.nexy.assistant
error	14:51:41.634052-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:41.634088-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:51:41.645165-0500	Nexy	nw_path_libinfo_path_check [7F03AA36-9B02-4BDE-949E-6C0FA260ACA7 Hostname#3db1d101:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:51:41.645379-0500	mDNSResponder	[R50750] DNSServiceQueryRecord START -- qname: <mask.hash: 'RtrA/jBwUcahoEP0EKQp9Q=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: b360ab20
default	14:51:41.646188-0500	mDNSResponder	[R50751] DNSServiceQueryRecord START -- qname: <mask.hash: 'RtrA/jBwUcahoEP0EKQp9Q=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 8916 (Nexy), name hash: b360ab20
default	14:51:41.646332-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:41.646442-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:41.646514-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:41.646544-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:41.647013-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D73524B4-1801-4F69-89C1-C01F21654132 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55329,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x05902e32 tp_proto=0x06"
default	14:51:41.647126-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55329<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1049971 t_state: SYN_SENT process: Nexy:8916 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d0609c6
default	14:51:41.647231-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:41.647245-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:41.647258-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:41.647265-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:41.647286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:41.647294-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:41.647422-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:41.654210-0500	kernel	tcp connected: [<IPv4-redacted>:55329<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1049971 t_state: ESTABLISHED process: Nexy:8916 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d0609c6
default	14:51:41.734828-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9fda3e340) Selecting device 0 from destructor
default	14:51:41.734843-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:41.734849-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:41.734854-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 91
default	14:51:41.734874-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xb for device 91
default	14:51:41.734920-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	14:51:41.735261-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:41.735414-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9fda3e340) nothing to setup
default	14:51:41.735443-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device listeners to device 0
default	14:51:41.735450-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 0
default	14:51:41.735456-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 91
default	14:51:41.735668-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 91
default	14:51:41.735683-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:41.937833-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:55329<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1049971 t_state: LAST_ACK process: Nexy:8916 Duration: 0.291 sec Conn_Time: 0.008 sec bytes in/out: 398/46912 pkts in/out: 3/7 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 7.000 ms rttvar: 1.562 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x9d0609c6
default	14:51:41.937855-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55329<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1049971 t_state: LAST_ACK process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:43.764247-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:43.764697-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:43.766252-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:43.766253-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:43.766302-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:43.766313-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:43.766310-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2737 called from <private>
default	14:51:43.766324-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:43.767194-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:43.767364-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:43.767430-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:43.767569-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:43.768428-0500	runningboardd	Invalidating assertion 404-8916-33562 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:43.767582-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:43.769073-0500	runningboardd	Invalidating assertion 404-337-33563 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:43.784575-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:43.784632-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:43.784655-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:43.784662-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2737 called from <private>
default	14:51:43.787781-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:43.787817-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:43.788481-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2743 called from <private>
default	14:51:43.788503-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2743 called from <private>
default	14:51:43.788716-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:43.790807-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:43.791299-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:43.792294-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:43.792362-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:43.792380-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:43.792395-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:43.792409-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:43.792596-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2743 called from <private>
default	14:51:43.792613-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2743 called from <private>
default	14:51:43.792676-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:43.792690-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:43.792700-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:43.792706-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:43.792714-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:43.792725-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:43.792735-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:51:43.792741-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:51:43.792747-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:43.792773-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:43.792802-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:51:43.792809-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:51:43.792821-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:43.792829-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:43.800951-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:43.800987-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:43.801116-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:43.807292-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:43.808166-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:43.808187-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:43.808470-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:43.814521-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:43.814574-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:43.815016-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:43.815030-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:43.815131-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:43.815141-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:43.815150-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:43.815172-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:43.815212-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:43.815464-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:43.815656-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:43.815814-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:43.815932-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:43.815960-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:43.816082-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:51:43.816199-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:43.816658-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:43.816565-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:43.816817-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:43.816890-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:43.816926-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
error	14:51:43.817003-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:51:43.817179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:43.817194-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:43.817249-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:43.817286-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:43.817320-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:43.817353-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:43.818196-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:43.818500-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:43.818682-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:43.819000-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:43.841234-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33568 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:43.841327-0500	runningboardd	Assertion 404-337-33568 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
error	14:51:43.995368-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:44.459996-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:51:44.460083-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2736 called from <private>
default	14:51:44.462490-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:44.462538-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:44.464134-0500	runningboardd	Invalidating assertion 404-8916-33567 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:44.464435-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33570 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:44.464539-0500	runningboardd	Assertion 404-8916-33570 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:44.465205-0500	runningboardd	Invalidating assertion 404-337-33568 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:44.465501-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33571 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:44.465584-0500	runningboardd	Assertion 404-337-33571 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:44.463433-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc3704e0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:44.463998-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
error	14:51:44.467667-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:45.090881-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:51:45.090982-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2736 called from <private>
default	14:51:45.093496-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:45.093571-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:45.093841-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:45.094189-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:45.094897-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:45.094966-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:45.095001-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:45.095160-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:45.095189-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:51:45.094194-0500	runningboardd	Invalidating assertion 404-8916-33570 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:45.095226-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33572 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:45.095333-0500	runningboardd	Assertion 404-8916-33572 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:45.096004-0500	runningboardd	Invalidating assertion 404-337-33571 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:45.096256-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33573 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:45.096333-0500	runningboardd	Assertion 404-337-33573 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:45.095302-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:45.095329-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:45.095361-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:45.095406-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:45.095446-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	14:51:45.098459-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:45.633728-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:51:45.634423-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc3704e0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:45.634449-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:45.634552-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:45.634859-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:45.634979-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:45.635013-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:45.635021-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:45.635813-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0x9fab446c0: iounit configuration changed > stopping the engine
default	14:51:45.635828-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0x9fab446c0: stop, was running 1
default	14:51:45.635838-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0x9fab446c0: pause, was running 1
default	14:51:45.643964-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:45.644359-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:45.644479-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 stopping playing
default	14:51:45.644541-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:45.644578-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:45.644640-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:45.644723-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:45.644752-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:51:45.644834-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:45.644845-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:45.644908-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:45.644969-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:45.645009-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:51:45.647495-0500	runningboardd	Invalidating assertion 404-8916-33572 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:45.647592-0500	runningboardd	Invalidating assertion 404-337-33573 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:45.753562-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:45.753580-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:45.753591-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:45.753612-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:45.756530-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:45.757175-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:45.757488-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:45.768716-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x9fab446c0: iounit configuration changed > posting notification
default	14:51:58.027674-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371e60, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:58.027709-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.028261-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.029133-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371e60, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:58.029155-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371e60: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:58.029162-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.029170-0500	Nexy	AudioConverter -> 0x9fc371e60: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:58.029181-0500	Nexy	AudioConverter -> 0x9fc371e60: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:58.029187-0500	Nexy	AudioConverter -> 0x9fc371e60: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:58.030145-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371e90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:58.030158-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371e90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:58.030164-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.030164-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:58.030172-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:58.030178-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:58.030368-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371e90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:58.030599-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x9fab446c0: start, was running 0
default	14:51:58.033745-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33575 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:58.033900-0500	runningboardd	Assertion 404-8916-33575 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:58.034774-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:58.034787-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:58.034770-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33576 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:58.034800-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:58.034817-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:58.034939-0500	runningboardd	Assertion 404-337-33576 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:58.038755-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:58.039134-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:58.039167-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:58.039239-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:58.039258-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:58.039454-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:58.041938-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:58.042829-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:58.043205-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:58.043500-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:58.439369-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:58.440762-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:51:58.440980-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:51:58.440999-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 starting playing
default	14:51:58.441096-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:58.441155-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:51:58.441184-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:58.441236-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:51:58.441271-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:51:58.441335-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:51:58.441358-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:58.441591-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:58.441878-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:58.441998-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:58.442032-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:58.442049-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	14:51:58.442059-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:51:58.442073-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	14:51:58.442140-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:58.442226-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:51:58.645169-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:58.646414-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.646430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.646445-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:58.646454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.646461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:58.646470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:58.646583-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:58.647520-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:58.648679-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9fda3e340) Selecting device 85 from constructor
default	14:51:58.648694-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:58.648701-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:58.648708-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9fda3e340) nothing to teardown
default	14:51:58.648713-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 85
default	14:51:58.648845-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:58.649210-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xd for device 85
default	14:51:58.649653-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 85
default	14:51:58.650052-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 85
default	14:51:58.650067-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:51:58.650197-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:58.650208-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:58.650217-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:58.650224-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:58.650235-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:58.650372-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:58.650388-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:58.650396-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:58.650402-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device listeners from device 0
default	14:51:58.650408-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 0
default	14:51:58.650413-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:58.650434-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:51:58.650517-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9fda3e340) caller requesting device change from 85 to 91
default	14:51:58.650528-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:58.650535-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:58.650540-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 85
default	14:51:58.650546-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xd for device 85
default	14:51:58.650564-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	14:51:58.650902-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:58.651153-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9fda3e340) connecting device 91
default	14:51:58.651366-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fda3e340) Device ID: 91 (Input:Yes | Output:No): true
default	14:51:58.654414-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.654, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.657663-0500	tccd	AUTHREQ_SUBJECT: msgID=409.654, subject=com.nexy.assistant,
default	14:51:58.659446-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:51:58.659535-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:51:58.659965-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:58.661664-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.8, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:51:58.661712-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:58.663336-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.8, subject=com.nexy.assistant,
default	14:51:58.664477-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:51:58.684037-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9fda3e340) created ioproc 0xc for device 91
default	14:51:58.684211-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 7 device listeners to device 91
default	14:51:58.684395-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 91
default	14:51:58.684407-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fda3e340)
default	14:51:58.684417-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	14:51:58.684428-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:58.684556-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	14:51:58.684566-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	14:51:58.684571-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	14:51:58.684675-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:58.684690-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fda3e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:58.684696-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:58.684700-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 85
default	14:51:58.684869-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 85
default	14:51:58.684879-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:58.684889-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	14:51:58.685393-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:51:58.685415-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	14:51:58.685513-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:58.686655-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.655, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.687731-0500	tccd	AUTHREQ_SUBJECT: msgID=409.655, subject=com.nexy.assistant,
default	14:51:58.688343-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:58.712608-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:58.714230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.656, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.714641-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:51:58.716692-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=76554.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:51:58.716721-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=76554, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:58.717042-0500	tccd	AUTHREQ_SUBJECT: msgID=409.656, subject=com.nexy.assistant,
default	14:51:58.720650-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:58.720731-0500	tccd	AUTHREQ_SUBJECT: msgID=76554.9, subject=com.nexy.assistant,
default	14:51:58.721533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x844d37000 at /Applications/Nexy.app
default	14:51:58.734019-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:58.734077-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:58.734112-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:58.734131-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:58.734513-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.734527-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.734538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:58.734545-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.734565-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:58.734575-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:58.734652-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:58.741985-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.657, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.743139-0500	tccd	AUTHREQ_SUBJECT: msgID=409.657, subject=com.nexy.assistant,
default	14:51:58.744705-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:58.763499-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:51:58.767185-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:51:58.767317-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:51:58.768676-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:51:58.768681-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	14:51:58.768832-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:58.769047-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:58.769066-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:51:58.769076-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:51:58.769154-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:58.769171-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:58.769378-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:58.769527-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:58.769548-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:58.769727-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:58.770999-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:58.771042-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:58.774396-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:58.775101-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:58.773770-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:58.773932-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:58.774002-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:58.775763-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:58.775793-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:58.775808-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:58.775849-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:58.776068-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:58.776093-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:58.776141-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:58.776190-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:58.776243-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:58.776281-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:58.776320-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:58.776380-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:58.776433-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:58.771152-0500	runningboardd	Invalidating assertion 404-8916-33575 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:58.776478-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:58.781054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:58.781064-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:58.781246-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:58.781398-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:58.781503-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:58.787868-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:58.788170-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:58.788188-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:58.788203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:58.788253-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:58.788683-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:51:58.773197-0500	runningboardd	Invalidating assertion 404-337-33576 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:58.788763-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:51:58.788924-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:58.789000-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:51:58.789063-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:51:58.791500-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:58.792145-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:58.793409-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:58.794523-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:51:58.794967-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:51:58.798429-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:58.798449-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:58.798463-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:58.800050-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:51:58.800062-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:51:58.800085-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:51:58.800092-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:51:58.800098-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
error	14:51:58.800656-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:51:58.800693-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:58.800713-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2743 called from <private>
default	14:51:58.800649-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33578 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:58.800743-0500	runningboardd	Assertion 404-8916-33578 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:58.800744-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:58.800759-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2743 called from <private>
default	14:51:58.800771-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:58.800800-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:58.802357-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:58.802822-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:58.800988-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
error	14:51:58.801357-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:51:58.801387-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2736 called from <private>
default	14:51:58.801423-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:51:58.801454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:51:58.803723-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:58.803776-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:58.803822-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:58.803883-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:51:58.803895-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:51:58.804102-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2743 called from <private>
default	14:51:58.804110-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2743 called from <private>
default	14:51:58.804138-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:58.804146-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:58.804152-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:58.804178-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:58.804209-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:58.804249-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:58.804296-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:58.804327-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:58.804372-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:58.804404-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:58.804435-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:51:58.804467-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:51:58.804511-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:51:58.804898-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.658, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.804553-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:51:58.815319-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:51:58.815514-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:51:58.818130-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:51:58.819459-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	14:51:58.819545-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:58.819614-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:58.822710-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	14:51:58.822877-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
error	14:51:58.822276-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:58.822927-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:58.822983-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:58.818676-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:58.823137-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:58.824177-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.841099-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:58.841169-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:51:58.841213-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:58.858237-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:58.859039-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:51:58.859124-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:58.859153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	14:51:58.859183-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:58.859209-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:58.859250-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:51:58.859267-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:58.859277-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:58.859313-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:51:58.859406-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:58.859469-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 28 stopping playing
default	14:51:58.859489-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:58.859509-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:58.859545-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:58.859570-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:58.859714-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	14:51:58.859734-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:58.859632-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: true }, 
]
default	14:51:58.860012-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:58.870910-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33580 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:58.873264-0500	runningboardd	Assertion 404-337-33580 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:58.873902-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:58.874288-0500	runningboardd	Invalidating assertion 404-8916-33578 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:58.874022-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:58.874039-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:58.874047-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:58.874504-0500	runningboardd	Invalidating assertion 404-337-33580 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:58.875042-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:58.875211-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:58.875873-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:58.881262-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.659, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:58.889640-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:58.889744-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:51:58.889807-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:58.890115-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.890125-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:58.890139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:58.897357-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:58.897433-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:58.897486-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:58.897506-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:58.916374-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 issue_detected_sample_time=65760.000000 ] -- [ rms:[-37.108170], peaks:[-13.039202] ]
default	14:51:58.916413-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.392162], peaks:[-20.530937] ]
default	14:51:58.916704-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	14:51:58.916788-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xcb9a4b000] Created node ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	14:51:58.969146-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x9fab446c0: iounit configuration changed > posting notification
default	14:51:59.000875-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	14:51:59.002142-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33582 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:59.003899-0500	runningboardd	Assertion 404-337-33582 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:59.004313-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2737 called from <private>
default	14:51:59.004338-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2737 called from <private>
default	14:51:59.004385-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:59.004869-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:59.004961-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:59.005031-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:59.005166-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:59.006190-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:51:59.006438-0500	runningboardd	Invalidating assertion 404-8916-33581 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:59.006314-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:51:59.006330-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2737 called from <private>
default	14:51:59.007375-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:51:59.006336-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2737 called from <private>
default	14:51:59.008027-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:51:59.009082-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:51:59.009375-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2737 called from <private>
default	14:51:59.009388-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2737 called from <private>
default	14:51:59.009404-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:51:59.009877-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33583 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:59.010015-0500	runningboardd	Assertion 404-8916-33583 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:59.011153-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.660, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=8916, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:59.013972-0500	tccd	AUTHREQ_SUBJECT: msgID=409.660, subject=com.nexy.assistant,
default	14:51:59.014388-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:59.014815-0500	runningboardd	Invalidating assertion 404-337-33582 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:59.015142-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.015631-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.015707-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8fcd7d800 at /Applications/Nexy.app
default	14:51:59.020386-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.030117-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.030198-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:51:59.030253-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:59.030571-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030589-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030601-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.030610-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030618-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.030626-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.030648-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.030742-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030792-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:59.030792-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.030850-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.030901-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030919-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.030932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.030950-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.031021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.031074-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.031069-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:59.036681-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.036767-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:59.036860-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:59.036878-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:59.044378-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33584 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:59.045690-0500	runningboardd	Assertion 404-337-33584 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:59.046025-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2737 called from <private>
default	14:51:59.055675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.055689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.055701-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.055711-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.055721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.055731-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.055818-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:59.056966-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.065849-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.065942-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:51:59.066034-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:51:59.071628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.071670-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071679-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.071688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.071707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071729-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.071738-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.071747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.071753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.071835-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:59.072709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.072719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.072729-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.072737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.072745-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.072751-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.072788-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:59.260858-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:51:59.378204-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	14:51:59.378396-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:59.378479-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:59.378525-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:59.378550-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:59.378592-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f501b, Nexy(8916), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 28 stopping recording
default	14:51:59.378604-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	14:51:59.378614-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:59.378645-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:59.378684-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:59.378778-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:59.378788-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:59.378829-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:59.379018-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:59.379084-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:59.379053-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.379121-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:59.379147-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:59.379208-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.379231-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:59.379247-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.379259-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:51:59.379784-0500	runningboardd	Invalidating assertion 404-8916-33583 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:51:59.380335-0500	runningboardd	Invalidating assertion 404-337-33584 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:51:59.386399-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:59.386459-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:59.386502-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:59.386518-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:59.386856-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.386872-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.386884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.386890-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:59.386897-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:59.386904-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:59.387137-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:59.484260-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9fda3e340) Selecting device 0 from destructor
default	14:51:59.484282-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9fda3e340)
default	14:51:59.484293-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9fda3e340) not already running
default	14:51:59.484298-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9fda3e340) disconnecting device 91
default	14:51:59.484307-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9fda3e340) destroying ioproc 0xc for device 91
default	14:51:59.484344-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	14:51:59.484392-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:59.484560-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9fda3e340) nothing to setup
default	14:51:59.484575-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device listeners to device 0
default	14:51:59.484581-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9fda3e340) adding 0 device delegate listeners to device 0
default	14:51:59.484589-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 7 device listeners from device 91
default	14:51:59.484814-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9fda3e340) removing 0 device delegate listeners from device 91
default	14:51:59.484831-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9fda3e340)
default	14:51:59.486846-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:59.486860-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:59.486870-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:59.486888-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:59.489811-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:59.490643-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.491043-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.801095-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371e90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:59.801134-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:59.801762-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:59.802551-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371e90, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:59.802575-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:59.802587-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371e90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:59.802591-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:59.802596-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:59.802599-0500	Nexy	AudioConverter -> 0x9fc371e90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:59.803965-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371d40, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:59.803981-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371d40: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:59.803988-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:59.803987-0500	Nexy	AudioConverter -> 0x9fc371d40: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	14:51:59.804001-0500	Nexy	AudioConverter -> 0x9fc371d40: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	14:51:59.804007-0500	Nexy	AudioConverter -> 0x9fc371d40: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	14:51:59.804193-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9fc371d40: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:51:59.804455-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x9fab446c0: start, was running 0
default	14:51:59.809309-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:51:59.809418-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:59.805047-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33585 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:59.805154-0500	runningboardd	Assertion 404-8916-33585 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:59.809449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f501b, Nexy(8916), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:51:59.809488-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:59.810065-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:51:59.810106-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 starting playing
default	14:51:59.810333-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:59.810380-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:51:59.810448-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:59.810303-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501b, Nexy(8916), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:51:59.810540-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:51:59.810523-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.810657-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:59.810686-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:51:59.810875-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:59.810928-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:59.806853-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:59.811038-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:59.810756-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.810800-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.810831-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:51:59.811120-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33586 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:59.810842-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:59.810853-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:51:59.811273-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x89380001 category Not set
default	14:51:59.811199-0500	runningboardd	Assertion 404-337-33586 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:51:59.811933-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.811960-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:51:59.811974-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	14:51:59.811983-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:51:59.811779-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
error	14:51:59.812021-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	14:51:59.812170-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:51:59.812360-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:51:59.815438-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:59.815752-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:51:59.815769-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:51:59.815785-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:51:59.815841-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:51:59.815968-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.816138-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.818387-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:59.818906-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.818846-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:51:59.833179-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:52:01.810425-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	14:52:02.052486-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:52:02.052542-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:52:02.052552-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:52:02.052572-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:52:02.053747-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:52:02.053785-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2737)
default	14:52:02.053805-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:52:02.053817-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2737 called from <private>
default	14:52:02.059552-0500	runningboardd	Invalidating assertion 404-8916-33585 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:02.055448-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:52:02.055241-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:52:02.055687-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2737 called from <private>
default	14:52:02.059756-0500	runningboardd	Invalidating assertion 404-337-33586 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:52:02.055706-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:52:02.062568-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:52:02.067085-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:52:02.067121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:52:02.067475-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:52:02.067504-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:52:02.067512-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:52:02.071325-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:52:02.071369-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:52:02.071388-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:52:02.071396-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:52:02.071403-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:52:02.071408-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:52:02.071680-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:52:02.071995-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:52:02.072026-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2737)
default	14:52:02.072345-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2737 called from <private>
default	14:52:02.072413-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2737 called from <private>
default	14:52:02.073947-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:52:02.076226-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2743 called from <private>
default	14:52:02.076316-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2743 called from <private>
default	14:52:02.077523-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33587 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:52:02.076698-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2736 called from <private>
default	14:52:02.077672-0500	runningboardd	Assertion 404-8916-33587 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:02.076750-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
error	14:52:02.076792-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:52:02.076814-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:52:02.076925-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:52:02.079212-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	14:52:02.078274-0500	runningboardd	Invalidating assertion 404-8916-33587 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:02.079751-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	14:52:02.080481-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:52:02.080528-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:52:02.080543-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:52:02.080554-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:52:02.080564-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2743)
default	14:52:02.080744-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2743 called from <private>
default	14:52:02.080756-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2743 called from <private>
default	14:52:02.080812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:52:02.080845-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:52:02.080876-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2743 called from <private>
default	14:52:02.080908-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2743 called from <private>
default	14:52:02.080935-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2743 called from <private>
default	14:52:02.080964-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2743 called from <private>
default	14:52:02.080996-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:52:02.081021-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:52:02.081042-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:52:02.081068-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:52:02.081095-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2743 called from <private>
default	14:52:02.081125-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2743 called from <private>
default	14:52:02.081156-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2743 called from <private>
default	14:52:02.081162-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2743 called from <private>
default	14:52:02.090012-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:52:02.090051-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:52:02.092343-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2736 called from <private>
default	14:52:02.092375-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2736 called from <private>
default	14:52:02.092503-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:52:02.099209-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:52:02.099514-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2736 called from <private>
default	14:52:02.099525-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2736 called from <private>
default	14:52:02.099684-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2736)
default	14:52:02.105377-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:52:02.105632-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:52:02.105645-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:52:02.105751-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:52:02.105765-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:52:02.105772-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:52:02.105777-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:52:02.105832-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2736 called from <private>
default	14:52:02.106153-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2736 called from <private>
default	14:52:02.106231-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2736 called from <private>
default	14:52:02.106561-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2736 called from <private>
default	14:52:02.106663-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2736)
default	14:52:02.107367-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2743)
default	14:52:02.107568-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
error	14:52:02.232589-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:52:02.835292-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:52:02.835352-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2736 called from <private>
default	14:52:02.838146-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:52:02.840048-0500	runningboardd	Invalidating assertion 404-8916-33588 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:02.838200-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:52:02.840152-0500	runningboardd	Invalidating assertion 404-337-33589 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:52:02.840470-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33591 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:52:02.840631-0500	runningboardd	Assertion 404-8916-33591 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:02.841417-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33592 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:02.841514-0500	runningboardd	Assertion 404-337-33592 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:02.838910-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371d40, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.838943-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
error	14:52:02.843838-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:52:03.396692-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:52:03.396724-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2736 called from <private>
default	14:52:03.396766-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:52:03.396835-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:52:03.397874-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2736 called from <private>
default	14:52:03.397897-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2736 called from <private>
default	14:52:03.398204-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:03.398545-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:03.398566-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:03.398574-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:52:03.398870-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9fd10c740) Device ID: 85 (Input:No | Output:Yes): true
default	14:52:03.399122-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9fd10c740)
default	14:52:03.399310-0500	runningboardd	Invalidating assertion 404-8916-33591 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:03.399482-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8916-33593 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:52:03.399549-0500	runningboardd	Assertion 404-8916-33593 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:03.400137-0500	runningboardd	Invalidating assertion 404-337-33592 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:52:03.400583-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33594 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:03.400695-0500	runningboardd	Assertion 404-337-33594 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:03.399257-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.399285-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:03.399310-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.399342-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
error	14:52:03.404355-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:52:03.399368-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:03.954457-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2736 called from <private>
default	14:52:03.955255-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9fc371d40, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.955291-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:03.955394-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:52:03.955673-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:03.955959-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:03.956031-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9fd10c740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:03.956044-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:52:03.956954-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:52:03.958035-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0x9fab446c0: iounit configuration changed > stopping the engine
default	14:52:03.958050-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0x9fab446c0: stop, was running 1
default	14:52:03.958180-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:52:03.958070-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0x9fab446c0: pause, was running 1
default	14:52:03.964740-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:52:03.965013-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:52:03.965114-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 28 stopping playing
default	14:52:03.965162-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:52:03.965193-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.965274-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:03.965742-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:52:03.966572-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.966618-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.965765-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.966634-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:52:03.965590-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":8916}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501b, sessionType: 'prim', isRecording: false }, 
]
default	14:52:03.966470-0500	runningboardd	Invalidating assertion 404-8916-33593 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:03.966283-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.966595-0500	runningboardd	Invalidating assertion 404-337-33594 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.powerd>:337]
default	14:52:04.070138-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:52:04.070156-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:52:04.070166-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:52:04.070310-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:52:04.073391-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:52:04.074090-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:04.075239-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:04.085840-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x9fab446c0: iounit configuration changed > posting notification
default	14:52:09.488217-0500	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	14:52:09.488300-0500	Nexy	[0x9f87dcf00] activating connection: mach=false listener=false peer=false name=(anonymous)
error	14:52:09.489270-0500	Nexy	Unable to obtain a task name port right for pid 396: (os/kern) failure (0x5)
default	14:52:09.489698-0500	Nexy	BKSHIDEventDeliveryManager - connection activation
default	14:52:09.497572-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:52:09.515141-0500	runningboardd	Invalidating assertion 404-396-33609 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	14:52:09.517283-0500	runningboardd	Invalidating assertion 404-396-33610 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	14:52:09.619259-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:52:09.620481-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:52:09.620505-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:52:09.620516-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:52:09.620533-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:52:09.620568-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] visiblity is no
default	14:52:09.641607-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:52:09.642204-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:09.642797-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:10.145565-0500	WindowServer	121c2b[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x161161 (Console) mainConnectionID: CB163;
    keyThiefConnectionID: 121C2B;
} for reason: key thief updated 121c2b 0x0-0x193193 (Nexy)
default	14:52:10.145612-0500	WindowServer	<BSCompoundAssertion:0x76cc11440> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 121c2b 0x0-0x193193 (Nexy) <1254> acq:0x76fcaef00 count:1
default	14:52:10.182473-0500	Nexy	[com.apple.controlcenter:2ED3B7B6-834B-4207-8DE9-B554EFCA2F0F] Sending action(s) in update: NSSceneFenceAction
default	14:52:10.193392-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppVisible" ID:404-396-33611 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:10.193471-0500	runningboardd	Assertion 404-396-33611 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:10.194000-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:52:10.194020-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:52:10.194035-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:52:10.194055-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:52:10.197078-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:52:10.197774-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:10.197901-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:10.208621-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.57221987.57221996(501)>:8916] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:404-396-33612 target:8916 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:10.208692-0500	runningboardd	Assertion 404-396-33612 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) will be created as active
default	14:52:10.209032-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring jetsam update because this process is not memory-managed
default	14:52:10.209049-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring suspend because this process is not lifecycle managed
default	14:52:10.209065-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring GPU update because this process is not GPU managed
default	14:52:10.209167-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] Ignoring memory limit update because this process is not memory-managed
default	14:52:10.209229-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] visiblity is yes
default	14:52:10.213435-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:52:10.213813-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:10.213926-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, running-active-NotVisible
default	14:52:12.022135-0500	Nexy	terminate:
default	14:52:12.022186-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	14:52:12.022209-0500	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	14:52:12.022344-0500	Nexy	Attempting sudden termination (1st attempt)
default	14:52:12.022361-0500	Nexy	Checking whether app should terminate
default	14:52:12.022437-0500	Nexy	Asking app delegate whether applicationShouldTerminate:
default	14:52:12.022458-0500	Nexy	replyToApplicationShouldTerminate:YES
default	14:52:12.022512-0500	Nexy	App termination approved
default	14:52:12.022522-0500	Nexy	Termination commencing
default	14:52:12.022531-0500	Nexy	Attempting sudden termination (2nd attempt)
default	14:52:12.025955-0500	Nexy	Termination complete. Exiting without sudden termination.
default	14:52:12.029289-0500	Nexy	[0x9f87dcc80] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	14:52:14.031956-0500	Nexy	Entering exit handler.
default	14:52:14.032013-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	14:52:14.032105-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	14:52:14.032118-0500	Nexy	[0x9fab18000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:52:14.032135-0500	Nexy	Exiting exit handler.
default	14:52:14.032159-0500	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	14:52:14.034073-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f501b","name":"Nexy(8916)"}, "details":null }
default	14:52:14.033559-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Workspace connection invalidated.
default	14:52:14.034118-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f501b from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":8916})
default	14:52:14.033618-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Now flagged as pending exit for reason: workspace client connection invalidated
default	14:52:14.032988-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x193193 (Nexy) connectionID: 121C2B pid: 8916 in session 0x101
default	14:52:14.034143-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":8916})
default	14:52:14.034636-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:14.034825-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 8916, Name = sid:0x1f501b, Nexy(8916), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:14.035000-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.035478-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.035547-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.035634-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.034409-0500	WindowManager	Connection invalidated | (8916) Nexy
default	14:52:14.033041-0500	WindowServer	<BSCompoundAssertion:0x76cc11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x193193 (Nexy) acq:0x76fcaf120 count:1
default	14:52:14.035684-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.035154-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:14.043555-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x193193 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x193193 (Nexy)"
)}
default	14:52:14.043956-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x22d4 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x193193 (Nexy)"
)}
default	14:52:14.046025-0500	runningboardd	Invalidating assertion 404-396-33612 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	14:52:14.046128-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.046221-0500	runningboardd	Invalidating assertion 404-396-33611 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	14:52:14.061045-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	14:52:14.061228-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	14:52:14.064589-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::out-0 issue_detected_sample_time=7680.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	14:52:14.064618-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2737.2414.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	14:52:14.075246-0500	kernel	tcp_connection_summary (tcp_drop:1453)[<IPv4-redacted>:55288<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047886 t_state: CLOSED process: Nexy:8916 Duration: 95.402 sec Conn_Time: 0.015 sec bytes in/out: 3676/769 pkts in/out: 6/3 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 57 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.750 ms rttvar: 13.750 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0x8a1bec72
default	14:52:14.075261-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55288<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047886 t_state: CLOSED process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	14:52:14.075311-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55285<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047872 t_state: FIN_WAIT_1 process: Nexy:8916 Duration: 95.945 sec Conn_Time: 0.016 sec bytes in/out: 1134720/223470 pkts in/out: 130/37 pkt rxmit: 1 ooo pkts: 3 dup bytes in: 0 ACKs delayed: 75 delayed ACKs sent: 0
rtt: 20.656 ms rttvar: 10.000 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xb1a707dc
default	14:52:14.075319-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55285<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1047872 t_state: FIN_WAIT_1 process: Nexy:8916 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:52:14.075161-0500	mDNSResponder	[R50553] DNSServiceCreateConnection STOP PID[8916](Nexy)
default	14:52:14.076839-0500	runningboardd	[app<application.com.nexy.assistant.57221987.57221996(501)>:8916] termination reported by launchd (0, 0, 0)
default	14:52:14.076967-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.077284-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.077554-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.077605-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.077650-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.57221987.57221996(501)>
default	14:52:14.093781-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: none (role: None) (endowments: (null))
default	14:52:14.094189-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Process exited: <RBSProcessExitContext| voluntary>.
default	14:52:14.094219-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Setting process task state to: Not Running
default	14:52:14.094264-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Setting process visibility to: Unknown
default	14:52:14.094310-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, none-NotVisible
default	14:52:14.094345-0500	ControlCenter	[app<application.com.nexy.assistant.57221987.57221996>:8916] Invalidating workspace.
default	14:52:14.094384-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.094167-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 8916, name = Nexy
default	14:52:14.094105-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.57221987.57221996(501)>: none (role: None) (endowments: (null))
default	14:52:14.094656-0500	ControlCenter	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, none-NotVisible
default	14:52:14.094924-0500	ControlCenter	Removing: <FBApplicationProcess: 0x8e41e5e00; app<application.com.nexy.assistant.57221987.57221996>:8916(v120F3B)>
default	14:52:14.096122-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, none-NotVisible
default	14:52:14.096381-0500	gamepolicyd	Received state update for 8916 (app<application.com.nexy.assistant.57221987.57221996(501)>, none-NotVisible
default	14:52:14.096590-0500	launchservicesd	Hit the server for a process handle 3143bfa000022d4 that resolved to: [app<application.com.nexy.assistant.57221987.57221996(501)>:8916]
default	14:52:14.099251-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x193193} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:52:14.099292-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 3
default	14:52:14.099318-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:52:14.103720-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-8916)
default	14:52:14.106996-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(341550DD) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-8916)
default	14:52:14.107069-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(341550DD, (bid:com.nexy.assistant-Item-0-8916))]
default	14:52:14.109915-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1ea0: Nexy> state 4
default	14:52:14.109934-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
error	14:52:14.244471-0500	runningboardd	RBSStateCapture remove item called for untracked item 404-396-33611 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916])
error	14:52:14.244491-0500	runningboardd	RBSStateCapture remove item called for untracked item 404-396-33612 (target:[app<application.com.nexy.assistant.57221987.57221996(501)>:8916])
default	14:52:18.895034-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	14:52:18.897007-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:18.897028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:18.897047-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:18.897058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:18.897068-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:18.897078-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:18.897248-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:19.387608-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
