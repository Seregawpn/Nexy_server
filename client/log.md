default	20:40:18.475362-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:40:18.475544-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:40:18.477282-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:40:18.489317-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54170280.54170289(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:40:18.489398-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54170280.54170289(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:580] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:402-580-5158 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:40:18.489470-0500	runningboardd	Assertion 402-580-5158 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) will be created as active
default	20:40:18.491729-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:40:18.491759-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:40:18.491771-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:40:18.491832-0500	runningboardd	app<application.com.nexy.assistant.54170280.54170289(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:40:18.494730-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:40:18.546504-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] is not RunningBoard jetsam managed.
default	20:40:18.546523-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] This process will not be managed.
default	20:40:18.546535-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:40:18.551696-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:18.555949-0500	gamepolicyd	Hit the server for a process handle bd8c46400001534 that resolved to: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:40:18.556078-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:18.556817-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:40:18.556891-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:402-402-5159 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:18.557033-0500	runningboardd	Assertion 402-402-5159 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:18.563666-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:5428" ID:402-365-5160 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:40:18.563788-0500	runningboardd	Assertion 402-365-5160 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:18.563972-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x81081 com.nexy.assistant starting stopped process.
default	20:40:18.653990-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:18.654005-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:18.654015-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:18.654130-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:18.656667-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:18.669410-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:18.726541-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:40:18.727792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=495.20, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=495, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:40:18.734740-0500	tccd	AUTHREQ_SUBJECT: msgID=495.20, subject=com.nexy.assistant,
default	20:40:18.735505-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4300 at /Applications/Nexy.app
default	20:40:18.752459-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	20:40:18.764478-0500	kernel	Nexy[5428] triggered unnest of range 0x1fa000000->0x1fc000000 of DYLD shared region in VM map 0xadd9bee828bdeff5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:40:18.764508-0500	kernel	Nexy[5428] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xadd9bee828bdeff5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:40:18.990190-0500	Nexy	[0x10642cf70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:40:18.990263-0500	Nexy	[0x10642d4b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:40:19.213819-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xa4f6b0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:40:19.214046-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xa4f6b0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:40:19.214258-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xa4f6b0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:40:19.214468-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xa4f6b0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:40:19.216094-0500	Nexy	[0x10643b0f0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:40:19.216818-0500	Nexy	[0xa4eaf4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:40:19.217139-0500	Nexy	[0xa4eaf4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:40:19.217518-0500	Nexy	[0xa4eaf4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:40:19.219533-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:40:19.220313-0500	Nexy	[0xa4eaf43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:40:19.220954-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:40:19.222539-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.1, subject=com.nexy.assistant,
default	20:40:19.223329-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4300 at /Applications/Nexy.app
default	20:40:19.234124-0500	Nexy	Received configuration update from daemon (initial)
default	20:40:19.237001-0500	Nexy	[0xa4eaf43c0] invalidated after the last release of the connection object
default	20:40:19.237319-0500	Nexy	server port 0x00003613, session port 0x00003613
default	20:40:19.238447-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.248, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:40:19.238473-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:40:19.239305-0500	tccd	AUTHREQ_SUBJECT: msgID=395.248, subject=com.nexy.assistant,
default	20:40:19.240111-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4300 at /Applications/Nexy.app
default	20:40:19.256441-0500	Nexy	New connection 0xf9617 main
default	20:40:19.258903-0500	Nexy	CHECKIN: pid=5428
default	20:40:19.267376-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:5428" ID:402-365-5161 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:40:19.267501-0500	runningboardd	Assertion 402-365-5161 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:19.267592-0500	Nexy	CHECKEDIN: pid=5428 asn=0x0-0x81081 foreground=0
default	20:40:19.268023-0500	runningboardd	Invalidating assertion 402-365-5160 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.coreservices.launchservicesd>:365]
default	20:40:19.267415-0500	launchservicesd	CHECKIN:0x0-0x81081 5428 com.nexy.assistant
default	20:40:19.267973-0500	Nexy	[0xa4eaf43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:40:19.268096-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:40:19.267986-0500	Nexy	[0xa4eaf43c0] Connection returned listener port: 0x4603
default	20:40:19.268244-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:40:19.268913-0500	Nexy	[0xa4eb28300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xa4eaf43c0.peer[365].0xa4eb28300
default	20:40:19.270994-0500	Nexy	FRONTLOGGING: version 1
default	20:40:19.271003-0500	Nexy	Registered, pid=5428 ASN=0x0,0x81081
default	20:40:19.271255-0500	WindowServer	f9617[CreateApplication]: Process creation: 0x0-0x81081 (Nexy) connectionID: F9617 pid: 5428 in session 0x101
default	20:40:19.273884-0500	Nexy	[0xa4eaf43c0] Connection returned listener port: 0x4603
default	20:40:19.273922-0500	Nexy	[0xa4eaf4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:40:19.274521-0500	Nexy	BringForward: pid=5428 asn=0x0-0x81081 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:40:19.274668-0500	Nexy	BringFrontModifier: pid=5428 asn=0x0-0x81081 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:40:19.275980-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:40:19.281318-0500	Nexy	No persisted cache on this platform.
default	20:40:19.282399-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:40:19.283041-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:40:19.286459-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:40:19.286467-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:40:19.286519-0500	Nexy	Initializing connection
default	20:40:19.286557-0500	Nexy	Removing all cached process handles
default	20:40:19.286580-0500	Nexy	Sending handshake request attempt #1 to server
default	20:40:19.286587-0500	Nexy	Creating connection to com.apple.runningboard
default	20:40:19.286595-0500	Nexy	[0xa4eaf4640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:40:19.286956-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] as ready
default	20:40:19.287506-0500	Nexy	Handshake succeeded
default	20:40:19.287519-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:40:19.288088-0500	Nexy	[0xa4eaf43c0] Connection returned listener port: 0x4603
default	20:40:19.288954-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 5428
default	20:40:19.291343-0500	Nexy	[0xa4eaf43c0] Connection returned listener port: 0x4603
default	20:40:19.298125-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:40:19.298160-0500	Nexy	[0xa4eaf4780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:40:19.298295-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:40:19.298780-0500	Nexy	[0xa4eaf4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:40:19.301693-0500	Nexy	[0xa4eaf4a00] Connection returned listener port: 0x6903
default	20:40:19.302370-0500	Nexy	Registered process with identifier 5428-177970
default	20:40:20.805413-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 929A84AF-86BA-4609-B414-D6E2DFEFFB4A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52477,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x7b5b1e32 tp_proto=0x06"
default	20:40:20.805531-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52477<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390800 t_state: SYN_SENT process: Nexy:5428 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8bd26e8a
default	20:40:24.490416-0500	runningboardd	Assertion did invalidate due to timeout: 402-402-5159 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428])
default	20:40:24.689532-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:24.689558-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:24.689577-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:24.689614-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:24.693521-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:24.694308-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:25.806548-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52477<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390800 t_state: SYN_SENT process: Nexy:5428 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8bd26e8a
default	20:40:25.806590-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52477<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390800 t_state: SYN_SENT process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:40:25.807276-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B78D1AE4-8D6F-4BAA-92FB-97CF577DAC69 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52478,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x03bd59de tp_proto=0x06"
default	20:40:25.807434-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52478<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390817 t_state: SYN_SENT process: Nexy:5428 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa9b086f1
default	20:40:29.163192-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:40:30.263062-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:40:30.807699-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52478<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390817 t_state: SYN_SENT process: Nexy:5428 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa9b086f1
default	20:40:30.807735-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52478<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390817 t_state: SYN_SENT process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:40:30.813833-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:40:30.814230-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:40:30.816637-0500	Nexy	nw_path_libinfo_path_check [D6464216-7145-4A3C-AE5E-6D75527E1E0C Hostname#81fc51a5:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:40:30.817588-0500	mDNSResponder	[R76803] DNSServiceCreateConnection START PID[5428](Nexy)
default	20:40:30.817768-0500	mDNSResponder	[R76804] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 5428 (Nexy), name hash: f92d5498
default	20:40:30.818804-0500	mDNSResponder	[R76805] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5428 (Nexy), name hash: f92d5498
default	20:40:30.835854-0500	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 602DDE52-6690-4C71-B007-86B6987F2286 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52480,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3062fead tp_proto=0x06"
default	20:40:30.836002-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52480<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390848 t_state: SYN_SENT process: Nexy:5428 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 3 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb48332ca
default	20:40:35.809864-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52480<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390848 t_state: SYN_SENT process: Nexy:5428 Duration: 4.974 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 3 ms so_error: 0 svc/tc: 0 flow: 0xb48332ca
default	20:40:35.809886-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52480<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 390848 t_state: SYN_SENT process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/10 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:40:36.992383-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:40:36.993387-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:40:36.994961-0500	Nexy	[0xa4eaf4dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:40:36.999288-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
default	20:40:37.003937-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:40:37.005749-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:40:37.005911-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:40:37.006073-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:40:37.006087-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:40:37.006123-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:40:37.006263-0500	Nexy	[0xa4eaf4f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:40:37.006947-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:40:37.014292-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.2, subject=com.nexy.assistant,
default	20:40:37.015022-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:37.028884-0500	Nexy	[0xa4eaf4f00] invalidated after the last release of the connection object
default	20:40:37.028947-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:40:37.034563-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.85, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:37.035512-0500	tccd	AUTHREQ_SUBJECT: msgID=406.85, subject=com.nexy.assistant,
default	20:40:37.036077-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
error	20:40:37.048569-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=406, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:40:37.049483-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.87, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:37.050498-0500	tccd	AUTHREQ_SUBJECT: msgID=406.87, subject=com.nexy.assistant,
default	20:40:37.051103-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:37.069314-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:40:37.069334-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa51387740> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:40:37.086575-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:40:37.086708-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:40:37.091260-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:40:37.097316-0500	Nexy	[0xa4eaf4f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:40:38.841003-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa4fd68740) Selecting device 85 from constructor
default	20:40:38.841021-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:38.841028-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:38.841531-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa4fd68740) nothing to teardown
default	20:40:38.841542-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa4fd68740) connecting device 85
default	20:40:38.841726-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa4fd68740) Device ID: 85 (Input:No | Output:Yes): true
default	20:40:38.841847-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa4fd68740) created ioproc 0xa for device 85
default	20:40:38.841964-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 7 device listeners to device 85
default	20:40:38.842163-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 85
default	20:40:38.842175-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa4fd68740)
default	20:40:38.842278-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:40:38.842288-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:40:38.842295-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:40:38.842304-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:40:38.842314-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:40:38.842407-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:40:38.842422-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:40:38.842428-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:40:38.842443-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device listeners from device 0
default	20:40:38.842453-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 0
default	20:40:38.842458-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:38.842478-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:40:38.842581-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xa4fd68740) caller requesting device change from 85 to 91
default	20:40:38.842591-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:38.842597-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:38.842601-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa4fd68740) disconnecting device 85
default	20:40:38.842606-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa4fd68740) destroying ioproc 0xa for device 85
default	20:40:38.842686-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:40:38.844489-0500	Nexy	[0xa4eaf5180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:40:38.846472-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":{"PID":5428,"session_type":"Primary"} }
default	20:40:38.846609-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5428}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4005, sessionType: 'prim', isRecording: false }, 
]
default	20:40:38.847700-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 5428, name = Nexy
default	20:40:38.848155-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa4f6cafc0 with ID: 0x1f4005
default	20:40:38.850450-0500	Nexy	[0xa4eaf52c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:40:38.851044-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=23313082482689 }
default	20:40:38.851066-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:40:38.851145-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:40:38.851331-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa4fd68740) connecting device 91
default	20:40:38.851490-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa4fd68740) Device ID: 91 (Input:Yes | Output:No): true
default	20:40:38.853672-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.88, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:38.855547-0500	tccd	AUTHREQ_SUBJECT: msgID=406.88, subject=com.nexy.assistant,
default	20:40:38.856348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:38.877217-0500	tccd	AUTHREQ_PROMPTING: msgID=406.88, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:40:40.796525-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	20:40:40.798453-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa4fd68740) created ioproc 0xa for device 91
default	20:40:40.798682-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 7 device listeners to device 91
default	20:40:40.798938-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 91
default	20:40:40.798952-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa4fd68740)
default	20:40:40.798964-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:40:40.798980-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:40:40.799186-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:40:40.799196-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:40:40.799204-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:40:40.799325-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:40:40.799426-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:40:40.799477-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:40:40.799504-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 7 device listeners from device 85
default	20:40:40.799756-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 85
default	20:40:40.799796-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:40.800467-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:40:40.802534-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.89, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:40.804863-0500	tccd	AUTHREQ_SUBJECT: msgID=406.89, subject=com.nexy.assistant,
default	20:40:40.806395-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:40.807980-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:40:40.824934-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:40:40.824984-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:40:40.825064-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbc00, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:40:40.825258-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:40:40.826144-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.90, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:40.827148-0500	tccd	AUTHREQ_SUBJECT: msgID=406.90, subject=com.nexy.assistant,
default	20:40:40.827764-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:40.846057-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.91, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:40.846982-0500	tccd	AUTHREQ_SUBJECT: msgID=406.91, subject=com.nexy.assistant,
default	20:40:40.847543-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:40.863465-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:40:40.863871-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:40:40.863905-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:40:40.864042-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:40:40.864986-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:40:40.868577-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:40.868634-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:40.961399-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:40:40.962793-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:447 called from <private>
default	20:40:40.962815-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:40:40.963617-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:40.964953-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5196 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:40.965034-0500	runningboardd	Assertion 402-336-5196 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:40.966562-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:40.966590-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:40.966629-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:40.963646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:40.966931-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:40.963654-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:40.963985-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:40.964133-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:40.964145-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:40.964608-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:40.969700-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:40:40.970349-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	20:40:40.969160-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
default	20:40:40.972223-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:40.972249-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:40.972259-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:40.972266-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:40.972275-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:40.972286-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:40.973520-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:40:40.973592-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:40:40.972381-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:447 called from <private>
default	20:40:40.972508-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:40.973701-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:40.972578-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:40.972626-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:40.972661-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:447 called from <private>
default	20:40:40.974069-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4005, Nexy(5428), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:40:40.972723-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:40.972747-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:40.975914-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:40.975915-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.975965-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:40.976408-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:40:40.977675-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4005, Nexy(5428), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 6 starting recording
default	20:40:40.979784-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
fault	20:40:40.972070-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
default	20:40:40.980030-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:40:40.980154-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4005, Nexy(5428), 'prim'', displayID:'com.nexy.assistant'}
default	20:40:40.978725-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:40.980309-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:40:40.980453-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:40:40.980318-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:40:40.977866-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.982271-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:40.987011-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:40.987020-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:40.976999-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.92, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:40.988174-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:446 called from <private>
default	20:40:40.988183-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:446 called from <private>
default	20:40:40.988445-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:40.990686-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:40.992391-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:40.992693-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:446 called from <private>
default	20:40:40.992703-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:446 called from <private>
default	20:40:40.991820-0500	runningboardd	Invalidating assertion 402-336-5196 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.powerd>:336]
default	20:40:40.992799-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:40.995124-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:40.994457-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.995925-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:40.996414-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:40.996424-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:40.995023-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:40:40.996460-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:40.996490-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:40.996499-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:40.996511-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:40.995533-0500	tccd	AUTHREQ_SUBJECT: msgID=406.92, subject=com.nexy.assistant,
default	20:40:40.996524-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:40.996659-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:40.996721-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:40.996773-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:40.996834-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:40.996907-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:40.997014-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:40.997121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:40.997256-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:40.997292-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:40.998290-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.998442-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.998624-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:41.001092-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:40.997330-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:40.999074-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:41.001673-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:40.998395-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:40.998172-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:41.001821-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:40:41.001996-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:40:41.002130-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:40:41.002453-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:40:40.999301-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:40.999310-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:40.999322-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:40.999332-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:41.030457-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/gestures-enabled newValue: (null)
default	20:40:41.034008-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/background-replacement-enabled newValue: (null)
default	20:40:41.033181-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:447 called from <private>
default	20:40:41.034001-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5197 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:41.034074-0500	runningboardd	Assertion 402-336-5197 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:41.040108-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-width newValue: (null)
default	20:40:41.040385-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-color newValue: (null)
default	20:40:41.040580-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-autocolorenabled newValue: (null)
default	20:40:41.040678-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-recommendedcolor newValue: (null)
default	20:40:41.040965-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-autosupported newValue: (null)
default	20:40:41.041100-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-mode newValue: (null)
default	20:40:41.041320-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-onboarding-state newValue: (null)
default	20:40:41.041560-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-onboarding-strikecount newValue: (null)
default	20:40:41.046812-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:40:41.051661-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:41.068983-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:40:41.071306-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:41.071367-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:41.094459-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:41.094480-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:41.094501-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:41.094537-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:41.097029-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:41.097498-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:41.109307-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:40:41.110635-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5198 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:41.111629-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:447 called from <private>
default	20:40:41.112483-0500	runningboardd	Assertion 402-336-5198 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:41.113075-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:41.111658-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 1 1, id:447 called from <private>
default	20:40:41.111783-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
error	20:40:41.114073-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	20:40:41.113332-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:41.113365-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:41.114084-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:41.114288-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:41.114664-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:40:41.114773-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:41.114825-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:40:41.114850-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4005, Nexy(5428), 'prim'', displayID:'com.nexy.assistant'}
default	20:40:41.115021-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4005, Nexy(5428), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 6 stopping recording
default	20:40:41.115087-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:40:41.115072-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:40:41.115153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:41.114094-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:41.114100-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:41.114109-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:447 called from <private>
default	20:40:41.114114-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:41.114142-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:41.115281-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:40:41.114356-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:40:41.115761-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:40:41.115458-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:40:41.115488-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:40:41.115248-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:41.115551-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:40:41.117177-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:41.117441-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:41.117218-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:41.117461-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:447 called from <private>
default	20:40:41.117248-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:41.117476-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:447 called from <private>
default	20:40:41.116998-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:41.117264-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:40:41.117485-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:41.117146-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:41.117284-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:41.117502-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:41.117510-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:447 called from <private>
default	20:40:41.117515-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:447 called from <private>
default	20:40:41.117536-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:40:41.117544-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:41.117701-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:41.117701-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:41.117811-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:40:41.117795-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:447 called from <private>
default	20:40:41.121557-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:41.121867-0500	runningboardd	Invalidating assertion 402-336-5198 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.powerd>:336]
default	20:40:41.122270-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:41.123749-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:40:41.124053-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[loc] Weather (com.apple.weather), [mic] Nexy (com.nexy.assistant)]
default	20:40:41.124125-0500	ControlCenter	Active activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:40:41.124463-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:40:41.124980-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.124990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.125005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:41.125019-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.125026-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:41.125035-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:41.125158-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:41.125313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.125344-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.125382-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:41.125396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:41.125422-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:41.125483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:41.125886-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:41.227586-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:41.227601-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:41.227613-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:41.227634-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:41.228307-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa4fd68740) Selecting device 0 from destructor
default	20:40:41.228317-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:41.228323-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:41.228327-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa4fd68740) disconnecting device 91
default	20:40:41.228333-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa4fd68740) destroying ioproc 0xa for device 91
default	20:40:41.228357-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:40:41.228382-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:40:41.228491-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xa4fd68740) nothing to setup
default	20:40:41.228502-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device listeners to device 0
default	20:40:41.228507-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 0
default	20:40:41.228513-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 7 device listeners from device 91
default	20:40:41.228699-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 91
default	20:40:41.228710-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:41.230113-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:41.230787-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:42.645617-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:40:42.647456-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:42.647485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:42.647512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:42.647531-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:42.647550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:42.647564-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:42.647753-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:43.822845-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:43.822957-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:43.822967-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:43.822987-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:43.823003-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:447 called from <private>
default	20:40:43.823009-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:43.832616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:43.832645-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:43.833492-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:43.833529-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:43.833545-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:446 called from <private>
default	20:40:43.833553-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:446 called from <private>
default	20:40:43.833564-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:43.833570-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:447 called from <private>
default	20:40:43.834698-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:43.834821-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:43.835223-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:446 called from <private>
default	20:40:43.835313-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:43.835347-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:446 called from <private>
default	20:40:43.835398-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:43.847712-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:446 called from <private>
default	20:40:43.847742-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:446 called from <private>
default	20:40:43.848654-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:446 called from <private>
default	20:40:43.848681-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:446 called from <private>
default	20:40:43.848820-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:43.851625-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:43.851877-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:446 called from <private>
default	20:40:43.851888-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:446 called from <private>
default	20:40:43.852005-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:43.856841-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:43.857063-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:446 called from <private>
default	20:40:43.857076-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:446 called from <private>
default	20:40:43.857125-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:43.857135-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:43.857142-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:43.857150-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:43.857156-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:43.857186-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:43.857243-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:43.857342-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:43.857503-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:43.857603-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:43.857762-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:43.857832-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:43.857887-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:43.857995-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:43.858119-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:43.858294-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:54.234572-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa4fd68740) Selecting device 85 from constructor
default	20:40:54.234606-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:54.234622-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:54.234635-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa4fd68740) nothing to teardown
default	20:40:54.234646-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa4fd68740) connecting device 85
default	20:40:54.234886-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa4fd68740) Device ID: 85 (Input:No | Output:Yes): true
default	20:40:54.235167-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa4fd68740) created ioproc 0xb for device 85
default	20:40:54.235460-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 7 device listeners to device 85
default	20:40:54.235908-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 85
default	20:40:54.235929-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa4fd68740)
default	20:40:54.236144-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:40:54.236167-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:40:54.236186-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:40:54.236234-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:40:54.236255-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:40:54.236522-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:40:54.236550-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:40:54.236566-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:40:54.236579-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device listeners from device 0
default	20:40:54.236591-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 0
default	20:40:54.236603-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:54.236641-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:40:54.236787-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xa4fd68740) caller requesting device change from 85 to 91
default	20:40:54.236809-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:54.236824-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:54.236835-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa4fd68740) disconnecting device 85
default	20:40:54.236846-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa4fd68740) destroying ioproc 0xb for device 85
default	20:40:54.236890-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:40:54.236982-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:40:54.237178-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa4fd68740) connecting device 91
default	20:40:54.237385-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa4fd68740) Device ID: 91 (Input:Yes | Output:No): true
default	20:40:54.240665-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.94, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:54.243496-0500	tccd	AUTHREQ_SUBJECT: msgID=406.94, subject=com.nexy.assistant,
default	20:40:54.245778-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.271615-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa4fd68740) created ioproc 0xb for device 91
default	20:40:54.271786-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 7 device listeners to device 91
default	20:40:54.271960-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 91
default	20:40:54.271970-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa4fd68740)
default	20:40:54.271981-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:40:54.271991-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:40:54.272126-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:40:54.272135-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:40:54.272140-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:40:54.272264-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:40:54.272274-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa4fd68740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:40:54.272279-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:40:54.272285-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 7 device listeners from device 85
default	20:40:54.272454-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 85
default	20:40:54.272464-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:54.272474-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:40:54.272830-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:40:54.274034-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.95, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:54.275245-0500	tccd	AUTHREQ_SUBJECT: msgID=406.95, subject=com.nexy.assistant,
default	20:40:54.275888-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.293786-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbc00, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:40:54.294011-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:40:54.295156-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.96, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:54.296272-0500	tccd	AUTHREQ_SUBJECT: msgID=406.96, subject=com.nexy.assistant,
default	20:40:54.296894-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.318599-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.97, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:54.319792-0500	tccd	AUTHREQ_SUBJECT: msgID=406.97, subject=com.nexy.assistant,
default	20:40:54.320439-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.339927-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:40:54.340114-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:40:54.341819-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:447 called from <private>
default	20:40:54.341883-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:40:54.341902-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:40:54.342598-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:54.347064-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:40:54.348308-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:40:54.342983-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:54.348566-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5204 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:54.348701-0500	runningboardd	Assertion 402-336-5204 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:54.343015-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:54.343023-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:54.343029-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:54.343033-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:54.343036-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:54.349358-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:54.350050-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:54.350255-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:54.350522-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:54.354152-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:54.354186-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:54.354195-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:447 called from <private>
default	20:40:54.354203-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:447 called from <private>
default	20:40:54.354212-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:447 called from <private>
default	20:40:54.354219-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:447 called from <private>
default	20:40:54.354227-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:54.354273-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:54.357196-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:447 called from <private>
default	20:40:54.357212-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:54.357233-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:54.358520-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:54.358793-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:54.359560-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:40:54.359682-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:40:54.359797-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4005, Nexy(5428), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:40:54.360246-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:54.360680-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4005, Nexy(5428), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:40:54.361015-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:54.361123-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:54.361649-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:40:54.361721-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4005, Nexy(5428), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 6 starting recording
default	20:40:54.361947-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:54.362056-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:40:54.362179-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4005, Nexy(5428), 'prim'', displayID:'com.nexy.assistant'}
default	20:40:54.362443-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:40:54.362448-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:40:54.362781-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.98, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:40:54.362473-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:40:54.364706-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:54.365308-0500	runningboardd	Invalidating assertion 402-336-5204 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.powerd>:336]
default	20:40:54.366508-0500	tccd	AUTHREQ_SUBJECT: msgID=406.98, subject=com.nexy.assistant,
default	20:40:54.366525-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:54.367970-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.369936-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:54.369956-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:54.371778-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:446 called from <private>
default	20:40:54.371790-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:446 called from <private>
default	20:40:54.371902-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:54.375380-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:54.375562-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:446 called from <private>
default	20:40:54.375591-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:446 called from <private>
default	20:40:54.375670-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:54.377104-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:40:54.377207-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:40:54.377281-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:40:54.377492-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:40:54.379705-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:54.380151-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:54.380161-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:54.380481-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:54.380495-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:54.380568-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:54.380574-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:54.380649-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:54.380934-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:54.381002-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:54.381232-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:54.382159-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.382352-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.382411-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.381309-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:54.382479-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.381392-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:54.381496-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:54.381603-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:54.381731-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:54.382539-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.382608-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.382735-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.382572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.383157-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.382863-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.382877-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.382889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.383716-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.384000-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:54.383733-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.384170-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.384051-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.384375-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.384483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.384963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.385117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.385302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.386025-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.386009-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:54.381834-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:54.386266-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:40:54.384973-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:54.406543-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:447 called from <private>
default	20:40:54.407084-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:40:54.407341-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5205 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:54.407494-0500	runningboardd	Assertion 402-336-5205 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
error	20:40:54.408258-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	20:40:54.408273-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:54.408283-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:54.408288-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:54.418339-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:40:54.421132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.421142-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.421150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.421158-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.421164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.421170-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.421269-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:54.438803-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:40:54.440727-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:54.440784-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:40:54.470267-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:54.470289-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:54.470303-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:54.470333-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:54.472769-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:54.473426-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:54.485435-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:40:54.486977-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:447 called from <private>
default	20:40:54.487077-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:447 called from <private>
default	20:40:54.487220-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:40:54.488883-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5206 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:54.488686-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:54.488946-0500	runningboardd	Assertion 402-336-5206 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:54.488790-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:54.488802-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:447 called from <private>
default	20:40:54.488810-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:447 called from <private>
default	20:40:54.489243-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:54.489445-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:54.489515-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:54.489595-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:54.489773-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:40:54.490097-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:40:54.490658-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:54.490822-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:447 called from <private>
default	20:40:54.490833-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:447 called from <private>
default	20:40:54.490847-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:54.493942-0500	tccd	AUTHREQ_SUBJECT: msgID=406.100, subject=com.nexy.assistant,
default	20:40:54.494115-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:54.495024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:40:54.495345-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:40:54.495394-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:40:54.495451-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:40:54.495635-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:40:54.495738-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.495748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.495755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.516295-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:447 called from <private>
default	20:40:54.517607-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5207 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:40:54.517770-0500	runningboardd	Assertion 402-336-5207 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:40:54.522614-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:40:54.522651-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:40:54.522706-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:40:54.522964-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.522973-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.522984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.522990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.522998-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.523003-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.523015-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523025-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523061-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.523087-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.523154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.523293-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:54.523502-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:40:54.523577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523586-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523595-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.523602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.523624-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.523650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.656464-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:40:54.656847-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:40:54.656950-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:54.657004-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:40:54.657028-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4005, Nexy(5428), 'prim'', displayID:'com.nexy.assistant'}
default	20:40:54.657075-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4005, Nexy(5428), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 6 stopping recording
default	20:40:54.657095-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:40:54.657102-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:40:54.657130-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:40:54.657175-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:40:54.657305-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:40:54.657319-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:40:54.657412-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:40:54.659617-0500	runningboardd	Invalidating assertion 402-336-5207 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.powerd>:336]
default	20:40:54.659760-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:54.659806-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:54.659837-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:40:54.659663-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:40:54.659863-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.659718-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.659931-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:40:54.659945-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:40:54.659955-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:40:54.661267-0500	ControlCenter	Recent activity attributions changed to ["loc:com.apple.weather", "mic:com.nexy.assistant"]
default	20:40:54.664655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.664668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.664680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.664688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:40:54.664696-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:40:54.664705-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:40:54.664815-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:40:54.758246-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa4fd68740) Selecting device 0 from destructor
default	20:40:54.758260-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68740)
default	20:40:54.758270-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68740) not already running
default	20:40:54.758276-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa4fd68740) disconnecting device 91
default	20:40:54.758284-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa4fd68740) destroying ioproc 0xb for device 91
default	20:40:54.758326-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:40:54.758363-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:40:54.758539-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xa4fd68740) nothing to setup
default	20:40:54.758552-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device listeners to device 0
default	20:40:54.758558-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68740) adding 0 device delegate listeners to device 0
default	20:40:54.758564-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 7 device listeners from device 91
default	20:40:54.758794-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68740) removing 0 device delegate listeners from device 91
default	20:40:54.758810-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68740)
default	20:40:54.761460-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:40:54.761476-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:40:54.761485-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:40:54.761521-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:40:54.763928-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:40:54.764709-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:40:57.103526-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:57.103581-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:446 called from <private>
default	20:40:57.103595-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:446 called from <private>
default	20:40:57.104643-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(447)
default	20:40:57.104686-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:447 called from <private>
default	20:40:57.104707-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:447 called from <private>
default	20:40:57.117136-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(447)
default	20:40:57.117196-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:447 called from <private>
default	20:40:57.117203-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:447 called from <private>
default	20:40:57.117816-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:57.117832-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:57.120281-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:57.130903-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:446 called from <private>
default	20:40:57.130933-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:446 called from <private>
default	20:40:57.131059-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:57.136018-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:57.136595-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:446 called from <private>
default	20:40:57.136634-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:446 called from <private>
default	20:40:57.136795-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:57.141865-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:57.142232-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:57.142245-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:57.142584-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:57.142596-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:57.142616-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:57.142626-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:57.142646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:57.142730-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(446)
default	20:40:57.142839-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:57.143116-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:57.143255-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:57.143395-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:57.143522-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:57.143656-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:57.143752-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:57.143840-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:446 called from <private>
default	20:40:57.143923-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:446 called from <private>
default	20:40:57.144855-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(446)
default	20:40:57.145109-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:446 called from <private>
default	20:40:57.145124-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:446 called from <private>
default	20:40:57.145138-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:446 called from <private>
default	20:40:57.145148-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:446 called from <private>
default	20:40:57.770150-0500	Nexy	[0xa4eaf5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:40:57.772073-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:40:57.775033-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.3, subject=com.nexy.assistant,
default	20:40:57.776401-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4300 at /Applications/Nexy.app
default	20:40:57.799254-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[5428], responsiblePID[5428], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:40:57.799609-0500	Nexy	[0xa4eaf5540] invalidated after the last release of the connection object
default	20:40:58.115874-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:40:58.142250-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:40:58.142333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	20:40:58.146846-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:40:58.740010-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	20:40:58.746134-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:40:58.777789-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	20:40:58.830157-0500	nesessionmanager	UUID: Found for com.nexy.assistant: (
    "A813CAC5-DDAB-3196-5E8B-D5195C61E475",
    "BFBD67BF-5CB9-E2FB-FCCA-B2E0CE67D159"
)
error	20:41:01.805032-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	20:41:01.934513-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:41:01.934595-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:41:02.646895-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:41:05.553514-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:05.576211-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5e00 at /Applications/Nexy.app
default	20:41:05.588035-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:41:05.666073-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:41:05.669045-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:41:05.716780-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:41:05.719887-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:41:10.809633-0500	Nexy	[0xa4eaf5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:41:10.811561-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:10.816071-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.4, subject=com.nexy.assistant,
default	20:41:10.817780-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:10.845530-0500	Nexy	[0xa4eaf5540] invalidated after the last release of the connection object
default	20:41:10.848108-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	20:41:10.851279-0500	Nexy	[0xa4eaf5540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:41:10.851449-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:41:10.851883-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:41:10.864739-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:41:10.864765-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:10.865772-0500	tccd	AUTHREQ_SUBJECT: msgID=94711.2, subject=com.nexy.assistant,
default	20:41:10.866487-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:10.893395-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.274, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:10.893424-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:10.894284-0500	tccd	AUTHREQ_SUBJECT: msgID=395.274, subject=com.nexy.assistant,
default	20:41:10.894949-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:10.915098-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	20:41:10.943847-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:41:10.943977-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:41:10.944035-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:41:10.945652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.945672-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.945692-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.945702-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:41:10.945712-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:41:10.945719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:41:10.945859-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:41:13.923558-0500	kernel	udp connect: [<IPv4-redacted>:57325<-><IPv4-redacted>:80] interface:  (skipped: 0)
so_gencnt: 391183 so_state: 0x0102 process: Nexy:5428 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8803884e
default	20:41:13.923774-0500	kernel	udp_connection_summary [<IPv4-redacted>:57325<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 391183 so_state: 0x0102 process: Nexy:5428 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8803884e flowctl: 0us (0x)
default	20:41:13.925296-0500	Nexy	nw_path_libinfo_path_check [73A6136E-4285-4D1C-9FB8-8F85CF641527 IPv4#0a359ba4:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:41:13.927509-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 84C670C5-3925-495C-9445-20E53465799E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52508,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1868f6f6 tp_proto=0x06"
default	20:41:13.927629-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52508<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391184 t_state: SYN_SENT process: Nexy:5428 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x82c72a16
default	20:41:14.928271-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52508<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391184 t_state: SYN_SENT process: Nexy:5428 Duration: 1.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x82c72a16
default	20:41:14.928308-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52508<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391184 t_state: SYN_SENT process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:41:14.931101-0500	kernel	tcp listen: [<IPv4-redacted>:52509<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 391186 t_state: LISTEN process: Nexy:5428 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	20:41:14.931339-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52509<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 391186 t_state: LISTEN process: Nexy:5428 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	20:41:14.931364-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52509<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 391186 t_state: LISTEN process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:41:21.018134-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	20:41:27.938829-0500	Nexy	nw_path_libinfo_path_check [6350E354-88EE-44BA-BFC8-D6D35E973CA6 IPv4#0a359ba4:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:41:27.939524-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B26E4DAA-ADEF-47E4-95AB-46912097DB5A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52511,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x02e98fc0 tp_proto=0x06"
default	20:41:27.939677-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52511<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391241 t_state: SYN_SENT process: Nexy:5428 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa6050437
default	20:41:28.440576-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52511<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391241 t_state: SYN_SENT process: Nexy:5428 Duration: 0.501 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa6050437
default	20:41:28.440613-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52511<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391241 t_state: SYN_SENT process: Nexy:5428 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:41:31.477139-0500	Nexy	[0xa4eaf5680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:41:31.477765-0500	Nexy	[0xa4eaf57c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:41:31.478099-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:31.478528-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:31.480549-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.6, subject=com.nexy.assistant,
default	20:41:31.481587-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:31.482531-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.5, subject=com.nexy.assistant,
default	20:41:31.484775-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:41:31.497464-0500	Nexy	[0xa4eaf57c0] invalidated after the last release of the connection object
default	20:41:31.497589-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:41:31.498728-0500	Nexy	[0xa4eaf57c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:41:31.499217-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:41:31.500356-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.7, subject=com.nexy.assistant,
default	20:41:31.501096-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:31.502005-0500	Nexy	[0xa4eaf5680] invalidated after the last release of the connection object
default	20:41:31.517097-0500	tccd	AUTHREQ_PROMPTING: msgID=5428.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:41:33.429480-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	20:41:33.430085-0500	Nexy	[0xa4eaf57c0] invalidated after the last release of the connection object
default	20:41:33.433170-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:41:33.450217-0500	Nexy	[0xa4eaf57c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:41:33.453876-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.97, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:41:33.455739-0500	tccd	AUTHREQ_SUBJECT: msgID=389.97, subject=com.nexy.assistant,
default	20:41:33.456804-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.498759-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.98, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:41:33.500555-0500	tccd	AUTHREQ_SUBJECT: msgID=389.98, subject=com.nexy.assistant,
default	20:41:33.501326-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.529026-0500	Nexy	[0xa4eaf5680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:41:33.531060-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:41:33.531280-0500	Nexy	<private> 0xa4f870840: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:41:33.531353-0500	Nexy	<private> 0xa4f870840: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:41:33.532892-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:41:33.544142-0500	Nexy	[0xa4eaf5900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:41:33.546205-0500	Nexy	[0xa4eaf5900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.546293-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:41:33.546624-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:41:33.549344-0500	Nexy	[0xa4ecd83c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.550386-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.683, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.550430-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.551858-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.683, subject=com.nexy.assistant,
default	20:41:33.552849-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.574932-0500	Nexy	[0xa4ecd83c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.575058-0500	Nexy	[0xa4ecd83c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.575166-0500	Nexy	[0xa4ecd8500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.576215-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.684, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.576265-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.580544-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.684, subject=com.nexy.assistant,
default	20:41:33.581691-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.603779-0500	Nexy	[0xa4ecd8500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.603873-0500	Nexy	[0xa4ecd8500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.603941-0500	Nexy	[0xa4ecd8640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.605025-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.685, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.605061-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.606539-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.685, subject=com.nexy.assistant,
default	20:41:33.607347-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.634397-0500	Nexy	[0xa4ecd8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.634483-0500	Nexy	[0xa4ecd8640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.634557-0500	Nexy	[0xa4ecd8780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.635766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.686, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.635802-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.637665-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.686, subject=com.nexy.assistant,
default	20:41:33.638542-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.664540-0500	Nexy	[0xa4ecd8780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.664619-0500	Nexy	[0xa4ecd8780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.676568-0500	Nexy	Did add XPC store
default	20:41:33.676587-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:41:33.679255-0500	Nexy	0xa4f6cb900: Using cached account information
default	20:41:33.680357-0500	Nexy	[0xa4eb4b700] Session created.
default	20:41:33.680367-0500	Nexy	[0xa4eb4b700] Session created with Mach Service: <private>
default	20:41:33.680377-0500	Nexy	[0xa4ecd8dc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:41:33.680546-0500	Nexy	[0xa4eb4b700] Session activated
default	20:41:33.683269-0500	Nexy	[0xa4ecd8dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.683276-0500	Nexy	[0xa4eb4b700] Session canceled.
default	20:41:33.683291-0500	Nexy	[0xa4eb4b700] Disposing of session
default	20:41:33.683851-0500	Nexy	[0xa4ecd8dc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:41:33.685079-0500	Nexy	[0xa4ecd8dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.685136-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:41:33.685163-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:41:33.688791-0500	Nexy	[0xa4ecdb840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.690220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.687, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.690254-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.692224-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.687, subject=com.nexy.assistant,
default	20:41:33.693370-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.720549-0500	Nexy	[0xa4ecdb840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.720635-0500	Nexy	[0xa4ecdb840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.720715-0500	Nexy	[0xa4ecdb980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.721868-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.688, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.721904-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.723495-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.688, subject=com.nexy.assistant,
default	20:41:33.724421-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.750550-0500	Nexy	[0xa4ecdb980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.750634-0500	Nexy	[0xa4ecdb980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.750734-0500	Nexy	[0xa4ecdbac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.751867-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.689, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.751914-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.753526-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.689, subject=com.nexy.assistant,
default	20:41:33.754354-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.777863-0500	Nexy	[0xa4ecdbac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.777941-0500	Nexy	[0xa4ecdbac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.778008-0500	Nexy	[0xa4ecdbc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.779067-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.690, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.779102-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.780544-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.690, subject=com.nexy.assistant,
default	20:41:33.781327-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.805649-0500	Nexy	[0xa4ecdbc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.805735-0500	Nexy	[0xa4ecdbc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.817327-0500	Nexy	Did add XPC store
default	20:41:33.817353-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:41:33.817502-0500	Nexy	[0xa4ecdbe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:41:33.818176-0500	Nexy	[0xa4ecdbe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.818195-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:41:33.818212-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:41:33.823210-0500	Nexy	[0xa4ed0e940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.824400-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.691, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.824436-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.826172-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.691, subject=com.nexy.assistant,
default	20:41:33.827002-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.853127-0500	Nexy	[0xa4ed0e940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.853200-0500	Nexy	[0xa4ed0e940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.853262-0500	Nexy	[0xa4ed0ea80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.854309-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.692, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.854345-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.855748-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.692, subject=com.nexy.assistant,
default	20:41:33.856535-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.881566-0500	Nexy	[0xa4ed0ea80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.881653-0500	Nexy	[0xa4ed0ea80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.881726-0500	Nexy	[0xa4ed0ebc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.882882-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.693, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.882913-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.884443-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.693, subject=com.nexy.assistant,
default	20:41:33.885256-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.907480-0500	Nexy	[0xa4ed0ebc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.907546-0500	Nexy	[0xa4ed0ebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.907613-0500	Nexy	[0xa4ed0ed00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:41:33.908615-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.694, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.908651-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.910008-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.694, subject=com.nexy.assistant,
default	20:41:33.910809-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.933626-0500	Nexy	[0xa4ed0ed00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:33.933702-0500	Nexy	[0xa4ed0ed00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:41:33.935173-0500	Nexy	Did add XPC store
default	20:41:33.935197-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:41:33.958102-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.695, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.958142-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.959945-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.695, subject=com.nexy.assistant,
default	20:41:33.961126-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:33.988065-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.696, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:41:33.988115-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:33.989772-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.696, subject=com.nexy.assistant,
default	20:41:33.990739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:41:34.031316-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:41:34.048335-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:41:34.048392-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	20:41:34.048484-0500	Nexy	<private> 0xa4f870840: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:41:34.054783-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	20:41:34.054871-0500	Nexy	[0xa4ecd8780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:34.054888-0500	Nexy	[0xa4ecd8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:34.054930-0500	Nexy	[0xa4ecd8500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:34.054948-0500	Nexy	[0xa4ecd83c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:41:36.268695-0500	Nexy	[0xa4ed0f0c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	20:41:47.631900-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5501.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=5501, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:41:47.633423-0500	tccd	AUTHREQ_SUBJECT: msgID=5501.1, subject=com.nexy.assistant,
default	20:41:47.634222-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:47.649769-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.282, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=5501, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:41:47.650758-0500	tccd	AUTHREQ_SUBJECT: msgID=395.282, subject=com.nexy.assistant,
default	20:41:47.651487-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:47.709985-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:41:47.740875-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 618: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 08b80200 };
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
default	20:41:47.762989-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:41:47.775239-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:41:47.794126-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	20:41:49.784498-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	20:41:49.792259-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	20:41:49.797307-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:42:00.640127-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5504.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=5504, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:42:00.642275-0500	tccd	AUTHREQ_SUBJECT: msgID=5504.1, subject=com.nexy.assistant,
default	20:42:00.643178-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:42:00.660082-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.285, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=5504, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:00.660979-0500	tccd	AUTHREQ_SUBJECT: msgID=395.285, subject=com.nexy.assistant,
default	20:42:00.661696-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:42:00.699734-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:42:00.725107-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 618: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0eb80200 };
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
default	20:42:00.740772-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:03.758610-0500	Nexy	[0xa4ed0f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:42:03.760016-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:42:03.762118-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.8, subject=com.nexy.assistant,
default	20:42:03.763520-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:42:03.785222-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[5428], responsiblePID[5428], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:42:03.785662-0500	Nexy	[0xa4ed0f200] invalidated after the last release of the connection object
default	20:42:03.830589-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5e00 at /Applications/Nexy.app
default	20:42:03.850595-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	20:42:03.854840-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:42:06.842238-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:42:07.360213-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:42:07.415735-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	20:42:08.049863-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	20:42:10.891889-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4c00 at /Applications/Nexy.app
default	20:42:10.914441-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4f00 at /Applications/Nexy.app
default	20:42:10.924365-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:42:11.079344-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:11.079998-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:11.083759-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:11.084024-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:11.117357-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:11.117646-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:11.117726-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:11.118015-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:11.118952-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:42:11.119322-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:42:16.793415-0500	Nexy	server port 0x00013b4b, session port 0x00003613
default	20:42:16.795229-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.305, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:16.795308-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:16.798237-0500	tccd	AUTHREQ_SUBJECT: msgID=395.305, subject=com.nexy.assistant,
default	20:42:16.799501-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4f00 at /Applications/Nexy.app
default	20:42:19.835377-0500	Nexy	[0xa4ed0f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:42:19.836934-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:42:19.839690-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.9, subject=com.nexy.assistant,
default	20:42:19.841346-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4f00 at /Applications/Nexy.app
default	20:42:19.863039-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[5428], responsiblePID[5428], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:42:19.863428-0500	Nexy	[0xa4ed0f200] invalidated after the last release of the connection object
default	20:42:19.898261-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4c00 at /Applications/Nexy.app
default	20:42:19.918740-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4f00 at /Applications/Nexy.app
default	20:42:19.923017-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:42:22.315617-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:42:22.352425-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	20:42:23.276892-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:23.277084-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:23.282366-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:42:23.282566-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:42:28.131261-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6100 at /Applications/Nexy.app
default	20:42:28.151184-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:28.176825-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:42:28.217463-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:28.217705-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:28.217890-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:28.218463-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:28.219502-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:28.219738-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:28.220324-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:28.220447-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:28.275034-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:28.276901-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:28.277851-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:28.282665-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:28.285927-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:42:28.288532-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:42:32.944596-0500	Nexy	[0xa4ed0f200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:42:32.945341-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:42:32.945544-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5428.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:42:32.946892-0500	tccd	AUTHREQ_SUBJECT: msgID=5428.10, subject=com.nexy.assistant,
default	20:42:32.947730-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:32.968874-0500	Nexy	[0xa4ed0f200] invalidated after the last release of the connection object
default	20:42:35.979417-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.100, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:42:35.999381-0500	tccd	AUTHREQ_SUBJECT: msgID=389.100, subject=com.nexy.assistant,
default	20:42:36.001009-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:36.032176-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:42:36.162848-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:37.342210-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	20:42:38.162921-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:38.164530-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:38.174190-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:38.174109-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	20:42:38.347340-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:38.349215-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
default	20:42:38.650052-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:42:42.392463-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4600 at /Applications/Nexy.app
default	20:42:42.432316-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:42.442531-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:42:42.609513-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:42.609749-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:42.609949-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:42.610368-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:42:42.610522-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:42.611773-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:42.611998-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:42:42.612384-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:42:42.612828-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:42:42.612979-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:42:42.640435-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:42.640758-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:42.641666-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:42:42.649925-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:42:42.650249-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:42:42.651165-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:42:49.253978-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.101, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:42:49.257102-0500	tccd	AUTHREQ_SUBJECT: msgID=389.101, subject=com.nexy.assistant,
default	20:42:49.258994-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:52.301714-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	20:42:52.302165-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:42:52.303685-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	20:42:52.304265-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	20:42:52.304400-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	20:42:52.322256-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:42:52.322437-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:42:52.328943-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 125
default	20:42:52.346060-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa4fd68e40) Selecting device 85 from constructor
default	20:42:52.346071-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa4fd68e40)
default	20:42:52.346077-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa4fd68e40) not already running
default	20:42:52.346084-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa4fd68e40) nothing to teardown
default	20:42:52.346087-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa4fd68e40) connecting device 85
default	20:42:52.346174-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa4fd68e40) Device ID: 85 (Input:No | Output:Yes): true
default	20:42:52.346272-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa4fd68e40) created ioproc 0xc for device 85
default	20:42:52.346362-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68e40) adding 7 device listeners to device 85
default	20:42:52.346503-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa4fd68e40) adding 0 device delegate listeners to device 85
default	20:42:52.346509-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa4fd68e40)
default	20:42:52.346577-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.346585-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:42:52.346590-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.346596-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:42:52.346605-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:42:52.346692-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa4fd68e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:42:52.346702-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa4fd68e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:42:52.346707-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:42:52.346710-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68e40) removing 0 device listeners from device 0
default	20:42:52.346714-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa4fd68e40) removing 0 device delegate listeners from device 0
default	20:42:52.346719-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa4fd68e40)
default	20:42:52.346764-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:42:52.347048-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.348479-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbde0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.348525-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.350073-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.350276-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.357048-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.357244-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.359344-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbc90, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.359359-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.359652-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.360235-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbc90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.360256-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa4c8fbc90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:42:52.360261-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.360260-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:42:52.360270-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:42:52.360275-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:42:52.360972-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa4c8fbc90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:42:52.360981-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa4c8fbc90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:42:52.360985-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:42:52.360987-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:42:52.360996-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:42:52.361002-0500	Nexy	AudioConverter -> 0xa4c8fbc90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:42:52.361144-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa4c8fbc90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:42:53.375091-0500	Nexy	[0xa4ed0f480] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:42:53.388823-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:42:53.391172-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3000000033 pid: 5428
default	20:42:53.403147-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xa4f698820
 (
    "<NSDarkAquaAppearance: 0xa4f6986e0>",
    "<NSSystemAppearance: 0xa4f698780>"
)>
default	20:42:53.408828-0500	Nexy	[0xa4ed0f980] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:42:53.410896-0500	Nexy	[0xa4ed0fac0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:42:53.413889-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:42:53.414190-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:42:53.414201-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:42:53.414237-0500	Nexy	[0xa4ed0fc00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:42:53.414294-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:42:53.414369-0500	Nexy	[0xa4ed0fd40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.414437-0500	Nexy	FBSWorkspace registering source: <private>
default	20:42:53.415234-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:42:53.415529-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:42:53.416193-0500	Nexy	<FBSWorkspaceScenesClient:0xa515072a0 <private>> attempting immediate handshake from activate
default	20:42:53.416245-0500	Nexy	<FBSWorkspaceScenesClient:0xa515072a0 <private>> sent handshake
default	20:42:53.416702-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:42:53.417001-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.417030-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.417138-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Registering event dispatcher at init
default	20:42:53.417267-0500	ControlCenter	Created <FBWorkspace: 0xbdc9e9c20; <FBApplicationProcess: 0xbdeadcc00; app<application.com.nexy.assistant.54170280.54170289>:5428(v2B732)>>
default	20:42:53.417287-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54170280.54170289> with intent background
default	20:42:53.417434-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:42:53.417691-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54170280.54170289(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:42:53.417855-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54170280.54170289(501)> from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-5547 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:42:53.418037-0500	runningboardd	Assertion 402-625-5547 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) will be created as active
default	20:42:53.418072-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-5547 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.418462-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.418473-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.418489-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.419174-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:42:53.418901-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.421030-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:42:53.421907-0500	Nexy	Requesting scene <FBSScene: 0xa51507660; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC> from com.apple.controlcenter.statusitems
default	20:42:53.422288-0500	Nexy	Request for <FBSScene: 0xa51507660; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC> complete!
default	20:42:53.422370-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:42:53.424076-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.424437-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:42:53.424818-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:42:53.425084-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:42:53.425122-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:42:53.425328-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.425405-0500	Nexy	Requesting scene <FBSScene: 0xa515077a0; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:42:53.425692-0500	Nexy	Request for <FBSScene: 0xa515077a0; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView> complete!
default	20:42:53.426820-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Bootstrap success!
default	20:42:53.427556-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.427573-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:42:53.427666-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Setting process visibility to: Background
default	20:42:53.427774-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:42:53.428221-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:402-625-5548 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:42:53.428329-0500	runningboardd	Assertion 402-625-5548 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.428780-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.428790-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.428798-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.428894-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.431122-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.431586-0500	ControlCenter	Adding: <FBApplicationProcess: 0xbdeadcc00; app<application.com.nexy.assistant.54170280.54170289>:5428(v2B732)>
default	20:42:53.431838-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.432218-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Connection established.
default	20:42:53.432267-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.432337-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xbdc60a370>
default	20:42:53.432365-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Connection to remote process established!
default	20:42:53.433177-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.433197-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:42:53.433312-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:42:53.441097-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.441124-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdeadcc00; app<application.com.nexy.assistant.54170280.54170289>:5428(v2B732)>
default	20:42:53.441293-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Registered new scene: <FBWorkspaceScene: 0xbde3d1f80; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC> (fromRemnant = 0)
default	20:42:53.441342-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Workspace interruption policy did change: reconnect
default	20:42:53.441631-0500	ControlCenter	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC] Client process connected: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.441633-0500	Nexy	Request for <FBSScene: 0xa51507660; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC> complete!
default	20:42:53.441829-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:402-625-5549 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:42:53.441975-0500	runningboardd	Assertion 402-625-5549 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as inactive as originator process has not exited
default	20:42:53.442711-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-5550 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:42:53.442826-0500	runningboardd	Assertion 402-625-5550 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.442926-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:42:53.443213-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.443221-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.443229-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.443240-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdeadcc00; app<application.com.nexy.assistant.54170280.54170289>:5428(v2B732)>
default	20:42:53.443239-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.443304-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Registered new scene: <FBWorkspaceScene: 0xbde3d2a00; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:42:53.443459-0500	ControlCenter	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.443335-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.443725-0500	Nexy	<FBSWorkspaceScenesClient:0xa515072a0 <private>> Reconnecting scene com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC
default	20:42:53.444063-0500	Nexy	<FBSWorkspaceScenesClient:0xa515072a0 <private>> Reconnecting scene com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView
default	20:42:53.444190-0500	Nexy	Request for <FBSScene: 0xa515077a0; com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView> complete!
default	20:42:53.445971-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.446466-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.446886-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.450036-0500	Nexy	Registering for test daemon availability notify post.
default	20:42:53.450207-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:53.450294-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:53.450383-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:42:53.452191-0500	Nexy	[0xa4eaf7d40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:42:53.456015-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:53.460429-0500	Nexy	[0xa4eaf43c0] Connection returned listener port: 0x4603
default	20:42:53.460971-0500	Nexy	SignalReady: pid=5428 asn=0x0-0x81081
default	20:42:53.461707-0500	Nexy	SIGNAL: pid=5428 asn=0x0x-0x81081
default	20:42:53.462565-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:42:53.474354-0500	Nexy	0xa4f8706c0: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	20:42:53.474370-0500	Nexy	0xa4ec0ee50: Updating using cached account information
default	20:42:53.481543-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.485577-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.487592-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:42:53.487601-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:42:53.487641-0500	Nexy	[0xa4eaf5400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:42:53.487750-0500	Nexy	[0xa4eaf5400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.489135-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:42:53.493288-0500	Nexy	[C:2] Alloc <private>
default	20:42:53.493330-0500	Nexy	[0xa4eaf5400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.495269-0500	WindowManager	Connection activated | (5428) Nexy
default	20:42:53.496761-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5551 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.496835-0500	runningboardd	Assertion 402-5428-5551 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.497205-0500	runningboardd	Invalidating assertion 402-5428-5551 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.497265-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.497282-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.497314-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.497370-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.497389-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5552 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.497459-0500	runningboardd	Assertion 402-5428-5552 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.497792-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-5428). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:42:53.499629-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-5428)
default	20:42:53.499690-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.500024-0500	runningboardd	Invalidating assertion 402-5428-5552 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.499979-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(D211C955, (bid:com.nexy.assistant-Item-0-5428)) for (bid:com.nexy.assistant-Item-0-5428)
default	20:42:53.500267-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5553 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.500364-0500	runningboardd	Assertion 402-5428-5553 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.500473-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.500999-0500	runningboardd	Invalidating assertion 402-5428-5553 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.501187-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-5428)]
default	20:42:53.500632-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.501197-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5554 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.501250-0500	runningboardd	Assertion 402-5428-5554 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.501574-0500	runningboardd	Invalidating assertion 402-5428-5554 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.501687-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5555 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.501724-0500	runningboardd	Assertion 402-5428-5555 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.501956-0500	runningboardd	Invalidating assertion 402-5428-5555 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.502135-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5556 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.502182-0500	runningboardd	Assertion 402-5428-5556 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.502260-0500	ControlCenter	Created instance DisplayableId(319A1415) in .menuBar for DisplayableAppStatusItemType(D211C955, (bid:com.nexy.assistant-Item-0-5428)) .menuBar
default	20:42:53.502516-0500	runningboardd	Invalidating assertion 402-5428-5556 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.502691-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5428-5557 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:42:53.502742-0500	runningboardd	Assertion 402-5428-5557 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.503017-0500	runningboardd	Invalidating assertion 402-5428-5557 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:53.504162-0500	Nexy	[0xa4eaf7840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:42:53.504230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1078, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.504265-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.504745-0500	Nexy	[0xa4eaf7840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.504764-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:42:53.504780-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:42:53.505620-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1078, subject=com.nexy.assistant,
default	20:42:53.506351-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	20:42:53.507209-0500	Nexy	[0xa4ecd8640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.507895-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1079, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.507929-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.509273-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1079, subject=com.nexy.assistant,
default	20:42:53.509408-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:42:53.510375-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.510775-0500	ControlCenter	Created ephemaral instance DisplayableId(319A1415) for (bid:com.nexy.assistant-Item-0-5428) with positioning .ephemeral
default	20:42:53.510922-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.511548-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.512160-0500	Nexy	[com.apple.controlcenter:540DD80E-D993-4843-95CF-7326EEB406DC] Sending action(s) in update: NSSceneFenceAction
default	20:42:53.527503-0500	Nexy	[0xa4ecd8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.527554-0500	Nexy	[0xa4ecd8640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.527626-0500	Nexy	[0xa4ecd8500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.528268-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1080, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.528301-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.528599-0500	Nexy	Defaultable: persistentAccounts: <private>
default	20:42:53.528631-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0xa51506800: identifier=_acceptedIntroductions, name=Other Known, baseURL=(nil), dsid=(nil)> because it can't become default
default	20:42:53.528645-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0xa51506760: identifier=_directoryServices, name=Directory Services, baseURL=(nil), dsid=(nil)> because it can't become default
default	20:42:53.529314-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1080, subject=com.nexy.assistant,
default	20:42:53.529494-0500	Nexy	-awakeFromLoad
default	20:42:53.529606-0500	Nexy	-setServername: <private>  Parsed into scheme: https  host: <private>  port: 0  path: <private>
default	20:42:53.529661-0500	Nexy	-initWithUID:persistence: called on thread: <private>
default	20:42:53.529854-0500	Nexy	-clearPrincipalProperties
default	20:42:53.529877-0500	Nexy	-clearHomeContainers
default	20:42:53.529917-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.530369-0500	Nexy	Defaultable: Final list: <private>
default	20:42:53.530386-0500	Nexy	New account should become the default account
default	20:42:53.530603-0500	Nexy	0xa4f8706c0: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	20:42:53.530638-0500	Nexy	0xa4ec0ee50: Updating using cached account information
default	20:42:53.546046-0500	Nexy	[0xa4ecd8500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.546082-0500	Nexy	[0xa4cb90000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.546120-0500	Nexy	[0xa4cb90140] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.546724-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1081, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.546755-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.547702-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1081, subject=com.nexy.assistant,
default	20:42:53.548264-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.563996-0500	Nexy	[0xa4cb90140] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.564030-0500	Nexy	[0xa4cb90140] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.564074-0500	Nexy	[0xa4cb90280] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.564645-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1082, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.564677-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.565555-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1082, subject=com.nexy.assistant,
default	20:42:53.566099-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.582086-0500	Nexy	[0xa4cb90280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.582119-0500	Nexy	[0xa4cb90280] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.583278-0500	Nexy	Did add XPC store
default	20:42:53.583293-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:42:53.583342-0500	Nexy	[0xa4cb908c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:42:53.583694-0500	Nexy	[0xa4cb908c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.583712-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:42:53.583739-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:42:53.585769-0500	Nexy	[0xa4cb93340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.586349-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1083, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.586380-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.587352-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1083, subject=com.nexy.assistant,
default	20:42:53.587915-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.602961-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.602972-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.602982-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.602999-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.603859-0500	Nexy	[0xa4cb93340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.603907-0500	Nexy	[0xa4cb93340] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.603945-0500	Nexy	[0xa4cb93480] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.604547-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1084, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.604577-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.605483-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1084, subject=com.nexy.assistant,
default	20:42:53.605637-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.606024-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.606035-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.606179-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.613316-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:42:53.617259-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:42:53.617880-0500	Nexy	[GMS] availability notification token 120
default	20:42:53.622409-0500	Nexy	[0xa4cb93480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.622443-0500	Nexy	[0xa4cb935c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.622483-0500	Nexy	[0xa4cb93480] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.623053-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1085, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.623080-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.623987-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1085, subject=com.nexy.assistant,
default	20:42:53.624548-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.640362-0500	Nexy	[0xa4cb93480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.640399-0500	Nexy	[0xa4cb93480] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.640433-0500	Nexy	[0xa4cb93700] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:42:53.640984-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1086, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:42:53.641010-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5428, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:53.641871-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1086, subject=com.nexy.assistant,
default	20:42:53.642419-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:42:53.658255-0500	Nexy	[0xa4cb93700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:42:53.658293-0500	Nexy	[0xa4cb93700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:42:53.659077-0500	Nexy	Did add XPC store
default	20:42:53.659092-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:42:53.665232-0500	Nexy	Client change history token is invalid: <private>, current token: <private>, error: Error Domain=NSCocoaErrorDomain Code=134501 UserInfo={NSLocalizedFailureReason=<private>}
error	20:42:53.665460-0500	Nexy	Failed to fetch change history: Error Domain=CNErrorDomain Code=1006 "Full Sync Required" UserInfo={NSLocalizedFailureReason=A full sync is required., NSLocalizedDescription=Full Sync Required, NSUnderlyingError=0xa4cbdcae0 {Error Domain=CNErrorDomain Code=604 "Invalid Change History Anchor" UserInfo={NSLocalizedDescription=Invalid Change History Anchor, NSLocalizedFailureReason=The change history anchor is invalid.}}}
default	20:42:53.665740-0500	Nexy	0000 BEGIN: Will execute fetch for request: <private>
default	20:42:53.665751-0500	Nexy	0000 Entry point: executeFetchRequest:error:
default	20:42:53.665757-0500	Nexy	0000 Predicate: (null) <private>
default	20:42:53.674607-0500	Nexy	App is linked against Fall 2022 SDK or later
default	20:42:53.674618-0500	Nexy	Note access is not granted, so Notes are inaccessible
fault	20:42:53.674705-0500	Nexy	Attempt to read notes by an unentitled app
default	20:42:53.682286-0500	Nexy	0000 History anchor returned to client: <CNChangeHistoryAnchor: 0xa51686d80: version=2, token=<NSPersistentHistoryToken - {
    "121C6BBC-8A11-4E34-B252-321D0995C010" = 6;
    "CE445509-54F5-473C-9A96-89025D6F9355" = 4782;
}>>
default	20:42:53.682358-0500	Nexy	0000 Contact: 3EE990C2-437C-497A-B4CF-4787E78B5D0C:ABPerson
default	20:42:53.682368-0500	Nexy	0000 Contact: 2645688D-4F81-4C23-847F-96DEA47CCE6D:ABPerson
default	20:42:53.682373-0500	Nexy	0000 Contact: C822EB31-1F0F-41F6-9120-A322A5874983:ABPerson
default	20:42:53.682378-0500	Nexy	0000 Contact: 50AD2AD1-9340-4D1D-8702-DB033FCB2397:ABPerson
default	20:42:53.682384-0500	Nexy	0000 Contact: EDB979D3-287A-47DC-BC6D-006167336515:ABPerson
default	20:42:53.682389-0500	Nexy	0000 Contact: 9595A838-850C-49DB-8998-80F19667F619:ABPerson
default	20:42:53.682394-0500	Nexy	0000 Contact: 9891AB4D-DDC3-49D3-8FAA-45BFB1995A79:ABPerson
default	20:42:53.682398-0500	Nexy	0000 Contact: 34B7C886-745F-477F-BAF4-C6494310C1C1:ABPerson
default	20:42:53.682403-0500	Nexy	0000 Contact: 3426C1A4-CACA-42EF-8793-7312DCEE5E69:ABPerson
default	20:42:53.682406-0500	Nexy	0000 Contact: AFFBAE3D-BA02-4D6F-AE25-87E55C2E4CD9:ABPerson
default	20:42:53.682411-0500	Nexy	0000 Contact: 55C7A0C2-9163-43BC-95A9-A92E4F5427BD:ABPerson
default	20:42:53.682415-0500	Nexy	0000 Contact: CBAABC59-9B06-47EE-9311-0823CE3EE179:ABPerson
default	20:42:53.682427-0500	Nexy	0000 Contact: FF2BD9DD-8A6D-4E97-BB7D-7B1A5C4FAC0F:ABPerson
default	20:42:53.682434-0500	Nexy	0000 Contact: F6E944AE-3E32-4C0C-BA60-EE94D9402DA7:ABPerson
default	20:42:53.682442-0500	Nexy	0000 Contact: 0E222C4B-C87D-403F-A824-B8B8EAABF29D:ABPerson
default	20:42:53.682451-0500	Nexy	0000 Contact: 160B58EE-E9AF-4BBE-B484-7D4E18CA0CD4:ABPerson
default	20:42:53.682466-0500	Nexy	0000 Contact: D6931A27-6BBA-4ABF-AB86-AA94288C8731:ABPerson
default	20:42:53.682471-0500	Nexy	0000 Contact: 04E7F59A-3D30-4CF9-8395-AE8737EE1154:ABPerson
default	20:42:53.682482-0500	Nexy	0000 Contact: 863252FB-26EB-421B-9B96-91673ED81D35:ABPerson
default	20:42:53.682490-0500	Nexy	0000 Contact: 742C7DAC-D2A9-4D1C-A93D-DC71F37722B9:ABPerson
default	20:42:53.682501-0500	Nexy	0000 Contact: 99649BEC-0C02-4588-9CCA-09103FDC430C:ABPerson
default	20:42:53.682513-0500	Nexy	0000 Contact: 8898FA76-8C7B-4917-B353-30B4A337A32B:ABPerson
default	20:42:53.682518-0500	Nexy	0000 Contact: 75C5C7DD-DD9E-437F-91B9-34AFD56C5A14:ABPerson
default	20:42:53.682528-0500	Nexy	0000 Contact: DDC41FDC-94BF-4147-9863-5AFCC485C4BA:ABPerson
default	20:42:53.682533-0500	Nexy	0000 Contact: B6D0B979-BBDF-4FF5-93A8-0974C5AE45C7:ABPerson
default	20:42:53.682543-0500	Nexy	0000 Contact: B7A8ADD0-A952-45B0-B7A2-D15A3D34A898:ABPerson
default	20:42:53.682555-0500	Nexy	0000 Contact: 35894E4A-BF98-44E4-85B9-33C2A0A01944:ABPerson
default	20:42:53.682562-0500	Nexy	0000 Contact: 67B532BB-C394-4D14-B2E6-C1B93DE930E4:ABPerson
default	20:42:53.682566-0500	Nexy	0000 Contact: A71518ED-EC1D-4740-9D8C-2C5F81C71467:ABPerson
default	20:42:53.682571-0500	Nexy	0000 Contact: EE1E04AC-AF03-428A-97EF-6E8851A86066:ABPerson
default	20:42:53.682580-0500	Nexy	0000 Contact: 54E381BF-247A-4AB7-81FD-8C78CBB93296:ABPerson
default	20:42:53.682586-0500	Nexy	0000 Contact: A5DB19AB-C77E-44EC-87A4-8459DA494E7B:ABPerson
default	20:42:53.682595-0500	Nexy	0000 Contact: FC26680D-B85F-4E40-812F-4F169185AE50:ABPerson
default	20:42:53.682601-0500	Nexy	0000 Contact: E36EA0A4-41F7-4C3F-AAF9-A93099626D77:ABPerson
default	20:42:53.682610-0500	Nexy	0000 Contact: 37E2B276-263E-40A5-BF81-1628796DB605:ABPerson
default	20:42:53.682615-0500	Nexy	0000 Contact: D989E37A-D5DC-4A68-8D47-AD8FEE0B37BA:ABPerson
default	20:42:53.682626-0500	Nexy	0000 Contact: 204F2E81-2324-4937-9859-E8732482C902:ABPerson
default	20:42:53.682631-0500	Nexy	0000 Contact: C4831F25-FE6F-4217-92D2-C4D6C01013BC:ABPerson
default	20:42:53.682641-0500	Nexy	0000 Contact: 4FD77C47-1199-46DF-B186-25C3BB8E54C4:ABPerson
default	20:42:53.682651-0500	Nexy	0000 Contact: 16FA5BBF-AADB-4362-83EB-09668C0C6A84:ABPerson
default	20:42:53.682656-0500	Nexy	0000 Contact: D9A061DB-8A77-472E-A6B3-AF6A4A6727A9:ABPerson
default	20:42:53.682666-0500	Nexy	0000 Contact: 62AC02AD-E5FE-4F18-8DEB-151D2FFD50D2:ABPerson
default	20:42:53.682676-0500	Nexy	0000 Contact: 9D4856E4-4610-4169-9460-115522478752:ABPerson
default	20:42:53.682681-0500	Nexy	0000 Contact: 8038DF9A-4503-4464-BA80-1A8B28F523E6:ABPerson
default	20:42:53.682692-0500	Nexy	0000 Contact: DE31B769-37E8-406B-BC5C-FC44F37A37D1:ABPerson
default	20:42:53.682698-0500	Nexy	0000 Contact: B2E8FADF-3954-4D05-B047-C43474BF8E54:ABPerson
default	20:42:53.682706-0500	Nexy	0000 Contact: 5C30DD83-8C53-4FB6-943A-DF0CED6109D6:ABPerson
default	20:42:53.682712-0500	Nexy	0000 Contact: 16A1EC92-AB39-4C1E-8E16-706B5F47397C:ABPerson
default	20:42:53.682722-0500	Nexy	0000 Contact: 36994EED-FC81-46EF-86F8-8B3217234A98:ABPerson
default	20:42:53.682730-0500	Nexy	0000 Contact: D0D31CD7-6F0F-4030-A30D-197CE5187EED:ABPerson
default	20:42:53.682735-0500	Nexy	0000 Contact: F5676762-711F-4325-8A7A-FCB211127327:ABPerson
default	20:42:53.682744-0500	Nexy	0000 Contact: 99378C4C-7187-4A49-A938-AF1E4D9750E9:ABPerson
default	20:42:53.682749-0500	Nexy	0000 Contact: FE93F61D-6DD6-4CF7-9D17-F972815C60EB:ABPerson
default	20:42:53.682760-0500	Nexy	0000 Contact: E7CCA41A-8A2E-4351-852A-A5CFB6BD2AF5:ABPerson
default	20:42:53.682770-0500	Nexy	0000 Contact: EC41AC6A-1CB5-41D5-B70A-D7D261B5F6B3:ABPerson
default	20:42:53.682775-0500	Nexy	0000 Contact: 2A13AE99-82FE-4A26-A768-1B8C4A11C6C3:ABPerson
default	20:42:53.682790-0500	Nexy	0000 Contact: D5B5277E-F18A-48C2-B93C-E578CEB16C34:ABPerson
default	20:42:53.682799-0500	Nexy	0000 Contact: 1148E024-6D8F-4279-921E-7936B62EB2B8:ABPerson
default	20:42:53.682805-0500	Nexy	0000 Contact: FAF205FC-E995-4261-90F7-336A4D237F48:ABPerson
default	20:42:53.682809-0500	Nexy	0000 Contact: 88E161CA-F779-4608-BE32-D15726C295C6:ABPerson
default	20:42:53.682813-0500	Nexy	0000 Contact: BE244260-8495-47EA-9EFA-A4A129388623:ABPerson
default	20:42:53.682818-0500	Nexy	0000 Contact: FC34E363-0467-4B9C-95B0-F8C585C41741:ABPerson
default	20:42:53.682825-0500	Nexy	0000 Contact: F244F65D-0A57-4A3C-B8B8-9E1C389A5E77:ABPerson
default	20:42:53.682836-0500	Nexy	0000 Contact: 9DE56935-FB3E-470E-9878-89DB593E2DFE:ABPerson
default	20:42:53.682846-0500	Nexy	0000 Contact: 51D61586-1A8A-4EC4-8568-45B5296B1751:ABPerson
default	20:42:53.682852-0500	Nexy	0000 Contact: F34A454E-F1D3-4849-9368-950A6FFA8DD1:ABPerson
default	20:42:53.682857-0500	Nexy	0000 Contact: 5E09571D-9D8E-4D12-8480-F04FD91A55C4:ABPerson
default	20:42:53.682867-0500	Nexy	0000 Contact: 997D7D2F-4504-4C65-A31D-535219B806F5:ABPerson
default	20:42:53.682873-0500	Nexy	0000 Contact: F4D5E6E8-6B00-4329-94DC-82661F45DDB5:ABPerson
default	20:42:53.682879-0500	Nexy	0000 Contact: B3F91E16-48C2-4383-BFDA-F39E45D698A9:ABPerson
default	20:42:53.682888-0500	Nexy	0000 Contact: 972B1CC5-A00E-409A-A1C8-1035B67228F2:ABPerson
default	20:42:53.682895-0500	Nexy	0000 Contact: C9342200-2A80-485B-8777-A59F252176D4:ABPerson
default	20:42:53.682904-0500	Nexy	0000 Contact: FCD5548B-6E7B-4B57-9097-496095F0C27B:ABPerson
default	20:42:53.682909-0500	Nexy	0000 Contact: 32E90B79-BC48-4AFC-A5CE-495011FBE68F:ABPerson
default	20:42:53.682919-0500	Nexy	0000 Contact: 799B442D-0C1B-41A7-982A-5A795CF5AC7E:ABPerson
default	20:42:53.682929-0500	Nexy	0000 Contact: 4BC8FD3A-601A-4905-B4F0-AAEE2EA51FFC:ABPerson
default	20:42:53.682934-0500	Nexy	0000 Contact: EB01D8DC-AD35-4332-B52D-021C69F834F5:ABPerson
default	20:42:53.682943-0500	Nexy	0000 Contact: 34439B56-399C-41AE-8A94-926BE1F059E3:ABPerson
default	20:42:53.682948-0500	Nexy	0000 Contact: 5B2AA695-5EAB-4F85-9EA7-0F11FEE7BF7E:ABPerson
default	20:42:53.682957-0500	Nexy	0000 Contact: 680613B6-43E0-4C77-8B2B-0F21D4D6F558:ABPerson
default	20:42:53.682967-0500	Nexy	0000 Contact: FEFADE95-1917-4F12-AF5F-E9AF0F50E039:ABPerson
default	20:42:53.682972-0500	Nexy	0000 Contact: 1CED5FB1-D054-43C6-BF35-E035DFF16C75:ABPerson
default	20:42:53.682981-0500	Nexy	0000 Contact: 4D6A09F3-71D7-4E04-83FD-9BB5EF7442CF:ABPerson
default	20:42:53.682986-0500	Nexy	0000 Contact: 03F9DBA8-764B-4F5E-AFB8-4FE555600768:ABPerson
default	20:42:53.682996-0500	Nexy	0000 Contact: 33E6AEE6-78CC-42D7-80DA-478EDE698964:ABPerson
default	20:42:53.683002-0500	Nexy	0000 Contact: 2B720652-555E-462B-8C74-277B5F6F5F59:ABPerson
default	20:42:53.683012-0500	Nexy	0000 Contact: D8AB7561-7ABC-404E-A1AD-D9765D7DD983:ABPerson
default	20:42:53.683017-0500	Nexy	0000 Contact: 8256DD81-94E0-404F-BE4E-E6831011073C:ABPerson
default	20:42:53.683028-0500	Nexy	0000 Contact: 260C090E-52D7-4D15-AE22-6804C72C9DBF:ABPerson
default	20:42:53.683034-0500	Nexy	0000 Contact: F5703214-DEA8-429F-ADBF-5465A9AFE1BC:ABPerson
default	20:42:53.683039-0500	Nexy	0000 Contact: 1FBE32BC-B2F2-4B98-8BA8-04A4E25A4F0E:ABPerson
default	20:42:53.683051-0500	Nexy	0000 Contact: 2285EC2D-05CF-42C3-8C59-C4930AD792E3:ABPerson
default	20:42:53.683057-0500	Nexy	0000 Contact: 96E50230-0A5E-4B64-A2E9-A2F57018F4EA:ABPerson
default	20:42:53.683069-0500	Nexy	0000 Contact: 1D80A41C-48FF-40D8-A1F7-EB1FCAF019EC:ABPerson
default	20:42:53.683075-0500	Nexy	0000 Contact: 3C49D81F-04DC-4318-93D4-B25373EDFE30:ABPerson
default	20:42:53.683084-0500	Nexy	0000 Contact: 5B4B2182-FBEA-48F0-B9C7-742552BF6CF6:ABPerson
default	20:42:53.683093-0500	Nexy	0000 Contact: 697396C6-6DF5-4A8D-BBC1-7CFB8C26B531:ABPerson
default	20:42:53.683098-0500	Nexy	0000 Contact: BC83C14B-9BF3-4E6D-A5BD-1252B3AF3A72:ABPerson
default	20:42:53.683109-0500	Nexy	0000 Contact: 29B138C5-7412-4C36-A514-72D80434AC26:ABPerson
default	20:42:53.683115-0500	Nexy	0000 Contact: 93438337-7E2C-4A3D-99F8-28AECEE7A491:ABPerson
default	20:42:53.683125-0500	Nexy	0000 Contact: BEEDDC1A-71AD-4FBD-9241-9F6B4669022C:ABPerson
default	20:42:53.683130-0500	Nexy	0000 Contact: 516FCDD2-D694-4336-9C5C-B3F9398876E3:ABPerson
default	20:42:53.683137-0500	Nexy	0000 Contact: CB798F66-5E15-419F-8CB1-A22A10034846:ABPerson
default	20:42:53.683146-0500	Nexy	0000 Contact: 9BE2908B-57F8-42EB-85AB-E556B53D5008:ABPerson
default	20:42:53.683154-0500	Nexy	0000 Contact: 74E5D1E4-D560-47F5-800D-2B15C8F128ED:ABPerson
default	20:42:53.683159-0500	Nexy	0000 Contact: 73FA4D96-88CD-4E81-B755-D3C151251CB2:ABPerson
default	20:42:53.683163-0500	Nexy	0000 Contact: A159EB30-CDD4-4876-B3EB-7A251E5003A1:ABPerson
default	20:42:53.683176-0500	Nexy	0000 Contact: 2E020885-F8C2-47BB-AEE3-DD7CF66B13B4:ABPerson
default	20:42:53.683182-0500	Nexy	0000 Contact: 05A17C92-D301-4B09-A90C-D64806C4CA53:ABPerson
default	20:42:53.683187-0500	Nexy	0000 Contact: AD733A8E-1D66-4608-811D-8B3CC382D864:ABPerson
default	20:42:53.683193-0500	Nexy	0000 Contact: E567A65A-A157-4ABD-B1FD-82CC549DEDED:ABPerson
default	20:42:53.683203-0500	Nexy	0000 Contact: 7F0336C8-01E0-47A7-A79A-9400EBF86D9C:ABPerson
default	20:42:53.683208-0500	Nexy	0000 Contact: 46F95F55-6525-42E6-A4B3-332AB9ECB6C9:ABPerson
default	20:42:53.683217-0500	Nexy	0000 Contact: 0BF7B2D3-D0E4-4CF5-A2E5-BBAB2F74860F:ABPerson
default	20:42:53.683226-0500	Nexy	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	20:42:53.683232-0500	Nexy	0000 Contact: DF05522B-2972-4CAB-8C0F-9FDECE2E3D80:ABPerson
default	20:42:53.683243-0500	Nexy	0000 Contact: 32C28665-F08E-4EE8-AFEB-487908D24319:ABPerson
default	20:42:53.683248-0500	Nexy	0000 Contact: 23512481-0DEF-42CA-8985-3D92A24DC0D9:ABPerson
default	20:42:53.683257-0500	Nexy	0000 Contact: C799BC2E-8783-42B8-BE80-6B9329212F7F:ABPerson
default	20:42:53.683265-0500	Nexy	0000 Contact: AF84B174-40F6-4E9C-A51A-D3FACA6CD75E:ABPerson
default	20:42:53.683273-0500	Nexy	0000 Contact: D41F250E-DF7F-4F9C-9D25-DC402CAC6533:ABPerson
default	20:42:53.683280-0500	Nexy	0000 Contact: E5E58063-920E-46E6-8939-C1A7ACCF23F0:ABPerson
default	20:42:53.683291-0500	Nexy	0000 Contact: F48B9D39-03E0-45D0-AA05-14488FC68C6F:ABPerson
default	20:42:53.683296-0500	Nexy	0000 Contact: B599DEB9-C4DF-472F-9B9E-67C3935077CD:ABPerson
default	20:42:53.683301-0500	Nexy	0000 Contact: CD1D19AA-FC19-4C03-9DC9-C147E8C245D1:ABPerson
default	20:42:53.683312-0500	Nexy	0000 Contact: 4F833F31-870E-4630-825C-0F532CBA3D39:ABPerson
default	20:42:53.683324-0500	Nexy	0000 Contact: BD409DD5-797E-41A8-B955-2CC4520A8769:ABPerson
default	20:42:53.683329-0500	Nexy	0000 Contact: 8A88B309-DB9A-4B6A-B1D9-CD6910D5845B:ABPerson
default	20:42:53.683336-0500	Nexy	0000 Contact: 18BDFAAD-5A5F-42D6-890A-2C5AEA9201D4:ABPerson
default	20:42:53.683341-0500	Nexy	0000 Contact: 96309E07-28A0-4C3F-8B27-7224031FF6EB:ABPerson
default	20:42:53.683351-0500	Nexy	0000 Contact: BF324B31-1F91-4723-87BC-8FE02890D85F:ABPerson
default	20:42:53.683356-0500	Nexy	0000 Contact: A0DA1AD3-5F0A-4625-8A45-AEE2662B5DF7:ABPerson
default	20:42:53.683365-0500	Nexy	0000 Contact: 76DEED21-9E22-4327-83F8-C1C1DDF67DEE:ABPerson
default	20:42:53.683371-0500	Nexy	0000 Contact: 7C25BC81-A7AB-4059-A199-45F36EBE02EB:ABPerson
default	20:42:53.683381-0500	Nexy	0000 Contact: 919E5AE9-2160-41DC-8E41-9C2536932C86:ABPerson
default	20:42:53.683387-0500	Nexy	0000 Contact: 8FC46F73-8C76-4F4F-A480-86AD43FB3197:ABPerson
default	20:42:53.683398-0500	Nexy	0000 Contact: 758B39F6-7626-4392-A342-2F56B6D94427:ABPerson
default	20:42:53.683403-0500	Nexy	0000 Contact: 8A6084C7-9664-4FCF-BD0E-DF7B4AE169BC:ABPerson
default	20:42:53.683413-0500	Nexy	0000 Contact: 51857A1F-41AD-4ABC-BC2E-82377C39162B:ABPerson
default	20:42:53.683418-0500	Nexy	0000 Contact: 0145E52B-5388-4DF4-9BA6-041E2688EA53:ABPerson
default	20:42:53.683427-0500	Nexy	0000 Contact: 7C58562E-BF30-4BE5-AC33-E0A88F42AB76:ABPerson
default	20:42:53.683437-0500	Nexy	0000 Contact: C7C8564C-DF73-4360-B286-BB2CF4C72F17:ABPerson
default	20:42:53.683444-0500	Nexy	0000 Contact: F9EE7585-B534-46B5-848E-58FFD7152121:ABPerson
default	20:42:53.683450-0500	Nexy	0000 Contact: DABCF335-B625-47DD-918B-704381FD587D:ABPerson
default	20:42:53.683455-0500	Nexy	0000 Contact: A68807CD-0A21-4F90-BE39-09BAF83835E8:ABPerson
default	20:42:53.683465-0500	Nexy	0000 Contact: 3B7F983F-D8F3-400C-8462-CA84B84968A4:ABPerson
default	20:42:53.683470-0500	Nexy	0000 Contact: BE53EA52-E9F8-4C18-8446-4FA2489ADE02:ABPerson
default	20:42:53.683480-0500	Nexy	0000 Contact: A804F4AE-3921-4E55-83D8-094B7C4F17A3:ABPerson
default	20:42:53.683485-0500	Nexy	0000 Contact: 489A6364-6AEC-4FC5-8F52-FC08E5527BA0:ABPerson
default	20:42:53.683495-0500	Nexy	0000 Contact: B43BC68C-E9BB-48C1-98C3-A32A09C9A802:ABPerson
default	20:42:53.683501-0500	Nexy	0000 Contact: 05518C4D-4F67-4CD6-83D7-85AA7F2525A5:ABPerson
default	20:42:53.683511-0500	Nexy	0000 Contact: 955CE160-9CC8-4013-829C-A68FD99C7595:ABPerson
default	20:42:53.683521-0500	Nexy	0000 Contact: C13FF96F-DEF6-4C53-83DE-4B45963DD9AF:ABPerson
default	20:42:53.683526-0500	Nexy	0000 Contact: AE65B570-135A-4B14-BA64-EC538224DA56:ABPerson
default	20:42:53.683531-0500	Nexy	0000 Contact: C2132A98-A61A-4358-A681-AF1A1DA20915:ABPerson
default	20:42:53.683542-0500	Nexy	0000 Contact: C3CC1CBC-2410-4DA6-A83E-0477D239E755:ABPerson
default	20:42:53.683547-0500	Nexy	0000 Contact: 0FB60F1D-91EC-4396-A66A-69F15AF14BC5:ABPerson
default	20:42:53.683558-0500	Nexy	0000 Contact: FC6CD704-B936-454E-9EBD-E1701A5DE7D8:ABPerson
default	20:42:53.683563-0500	Nexy	0000 Contact: ED88C6F4-1641-473F-A5BC-DA8C11FCE9D2:ABPerson
default	20:42:53.683573-0500	Nexy	0000 Contact: 88083F13-CF73-4821-896D-8C9EDB5E9029:ABPerson
default	20:42:53.683578-0500	Nexy	0000 Contact: C5BAA4A8-B489-4A59-9400-5C0DFDAA91CA:ABPerson
default	20:42:53.683587-0500	Nexy	0000 Contact: F0187322-8BFE-4EE7-BA9E-BF7D7A056616:ABPerson
default	20:42:53.683597-0500	Nexy	0000 Contact: BA26FE3B-CB6A-471A-8E10-5000CF5332C2:ABPerson
default	20:42:53.683600-0500	Nexy	0000 Contact: DB250DFB-C87D-447B-B125-220B6E3DA663:ABPerson
default	20:42:53.683609-0500	Nexy	0000 Contact: B436BB91-BBBB-49E7-9C6A-93DDDD421478:ABPerson
default	20:42:53.683614-0500	Nexy	0000 Contact: DFCC4D11-6BC3-4ACD-B8C6-F8C46F7C8369:ABPerson
default	20:42:53.683624-0500	Nexy	0000 Contact: 0B435818-E34A-41BF-8808-417BCB956E97:ABPerson
default	20:42:53.683633-0500	Nexy	0000 Contact: E336CBFC-CF06-4672-BEF7-926884FB9BC8:ABPerson
default	20:42:53.683639-0500	Nexy	0000 Contact: A04F02F1-D5E5-4B3E-B5D0-287A46E6DB37:ABPerson
default	20:42:53.683648-0500	Nexy	0000 Contact: 274D78AE-37CF-4B30-B57D-D218F7D433BC:ABPerson
default	20:42:53.683653-0500	Nexy	0000 Contact: AFC75DDF-9D56-451F-8FFA-33CEF512BC9E:ABPerson
default	20:42:53.683662-0500	Nexy	0000 Contact: 36B84A8B-DD90-4609-9407-3BED73397C90:ABPerson
default	20:42:53.683671-0500	Nexy	0000 Contact: 25B2E948-39F0-4DA0-984A-6EAAFC4452BF:ABPerson
default	20:42:53.683676-0500	Nexy	0000 Contact: FD3874CC-9147-45D7-9635-BA7057F1E4CE:ABPerson
default	20:42:53.683686-0500	Nexy	0000 Contact: 93C427E1-DE52-48BF-AFC1-082EC9E9EDA0:ABPerson
default	20:42:53.683696-0500	Nexy	0000 Contact: 0ADD2D08-B0E0-4789-8BA5-3036146B6B78:ABPerson
default	20:42:53.683701-0500	Nexy	0000 Contact: C1626763-A8D5-4907-A0D9-325529F3E7B5:ABPerson
default	20:42:53.683711-0500	Nexy	0000 Contact: A691F96E-80C3-406D-A1F3-443C491D30D0:ABPerson
default	20:42:53.683717-0500	Nexy	0000 Contact: 331AE8C5-F99D-4F0A-B33F-36D558A607C3:ABPerson
default	20:42:53.683725-0500	Nexy	0000 Contact: 5C041266-AB76-41D1-BBBA-5FE4A4792084:ABPerson
default	20:42:53.683729-0500	Nexy	0000 Contact: F3BDC31E-20AF-4198-B696-F389C8F31C9F:ABPerson
default	20:42:53.683739-0500	Nexy	0000 Contact: 0CC4651C-3FC4-4644-BAB9-41107FBFF900:ABPerson
default	20:42:53.683746-0500	Nexy	0000 Contact: 9C0BE147-A58C-44D2-9C4A-FC7DFE653F3E:ABPerson
default	20:42:53.683754-0500	Nexy	0000 Contact: 0C5D18DF-0E63-4D12-AB19-70F9449BFDD3:ABPerson
default	20:42:53.683760-0500	Nexy	0000 Contact: 1EB1F958-3A33-4C17-AEFC-E59EA17F5D5B:ABPerson
default	20:42:53.683770-0500	Nexy	0000 Contact: E9510B2D-16FE-4F94-BBBE-BFACDEEF0759:ABPerson
default	20:42:53.683775-0500	Nexy	0000 Contact: 5D99F42B-5A12-4DD2-9DA9-063C524A30C7:ABPerson
default	20:42:53.683787-0500	Nexy	0000 Contact: 7C44FDAA-3756-43F4-B87F-DDA61E480B1C:ABPerson
default	20:42:53.683795-0500	Nexy	0000 Contact: DFDA976C-6D05-4677-AAA2-604A3688988F:ABPerson
default	20:42:53.683800-0500	Nexy	0000 Contact: 91B8C6A6-858C-4158-B742-E97BCFF7F054:ABPerson
default	20:42:53.683811-0500	Nexy	0000 Contact: 2A16F554-F4B5-4D1A-84FF-1B1B9CD41A6F:ABPerson
default	20:42:53.683819-0500	Nexy	0000 Contact: 51FDBD11-7239-4140-9605-7B2CFF1426E4:ABPerson
default	20:42:53.683829-0500	Nexy	0000 Contact: 2F813EA9-9EFC-409F-A1C4-64F820E4D179:ABPerson
default	20:42:53.683834-0500	Nexy	0000 Contact: 6B7D950D-D374-429D-91CE-A6E1B5D41AAA:ABPerson
default	20:42:53.683842-0500	Nexy	0000 Contact: F7679D0A-6363-40EC-A12A-63E9F2C28321:ABPerson
default	20:42:53.683850-0500	Nexy	0000 Contact: 6703F826-C4D7-43ED-83B5-77B3CBF74E39:ABPerson
default	20:42:53.683856-0500	Nexy	0000 Contact: ED036238-8F1A-4104-98CA-4C44E9BC5990:ABPerson
default	20:42:53.683866-0500	Nexy	0000 Contact: 00F2C374-C9A3-4DD0-B92B-E70CEFC1C968:ABPerson
default	20:42:53.683877-0500	Nexy	0000 Contact: E984A144-E505-46AA-AA38-1CF1EE5DF265:ABPerson
default	20:42:53.683882-0500	Nexy	0000 Contact: 444D762E-7CC5-479E-B3C7-D5172CE8F56B:ABPerson
default	20:42:53.683887-0500	Nexy	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	20:42:53.683893-0500	Nexy	0000 Contact: AA3A68CB-8A4B-4BAD-94D4-F0B1FDEF6AD2:ABPerson
default	20:42:53.683904-0500	Nexy	0000 Contact: B729AB23-719C-4993-99D4-97F17990CA6E:ABPerson
default	20:42:53.683909-0500	Nexy	0000 Contact: DDD6C0A5-9D08-4756-BB6E-06612386E694:ABPerson
default	20:42:53.683918-0500	Nexy	0000 Contact: DAA81742-1BAC-4E0A-86AB-1805922F5BFB:ABPerson
default	20:42:53.683923-0500	Nexy	0000 Contact: CCCE8074-7CFC-4765-87C4-3DA3398ED5E3:ABPerson
default	20:42:53.683934-0500	Nexy	0000 Contact: B3126A39-DB1F-4EB9-BA9E-057A701FEADB:ABPerson
default	20:42:53.683944-0500	Nexy	0000 Contact: D7A6F43C-FFAB-4219-B325-4345A3EBA5B5:ABPerson
default	20:42:53.683950-0500	Nexy	0000 Contact: F3959633-1472-4370-AE25-6C163A86F28A:ABPerson
default	20:42:53.683964-0500	Nexy	0000 Contact: 818A8D3F-5A2E-44CA-B4CF-47B295DB8C98:ABPerson
default	20:42:53.683969-0500	Nexy	0000 Contact: 228410FA-14BD-488B-A385-35C7112B9635:ABPerson
default	20:42:53.683978-0500	Nexy	0000 Contact: 1A2FDBB3-F370-4D0F-8C9A-34D9C191D7E3:ABPerson
default	20:42:53.683983-0500	Nexy	0000 Contact: 5FDB4463-1088-4EF5-9E20-48795D669908:ABPerson
default	20:42:53.683991-0500	Nexy	0000 Contact: 241E5174-F04C-45D2-BB1E-C4295A53CA80:ABPerson
default	20:42:53.683996-0500	Nexy	0000 Contact: 135FEF8F-5A69-49C6-97E1-E218FAD43A7E:ABPerson
default	20:42:53.684006-0500	Nexy	0000 Contact: F7BF6E9A-A1DE-4F0A-B9FE-DD0E61EBC464:ABPerson
default	20:42:53.684011-0500	Nexy	0000 Contact: F4DA25ED-6C3C-44D5-8A9B-87F14829E713:ABPerson
default	20:42:53.684024-0500	Nexy	0000 Contact: 95FF7EB7-87CC-416D-8811-B8DCC6FE7621:ABPerson
default	20:42:53.684029-0500	Nexy	0000 Contact: 751FAE5C-98A6-414E-B107-317AF0CBED37:ABPerson
default	20:42:53.684034-0500	Nexy	0000 Contact: 5465ECDD-A832-402B-BB73-FDF36810C6E0:ABPerson
default	20:42:53.684042-0500	Nexy	0000 Contact: 52FD2EC7-BEF6-4D05-BCAC-73FBAA131CDF:ABPerson
default	20:42:53.684048-0500	Nexy	0000 Contact: 9D848D63-FDF8-461C-9756-F8AAC3070EFF:ABPerson
default	20:42:53.684053-0500	Nexy	0000 Contact: D6BF6AC9-65CA-41BE-AFA2-C3071A2539F5:ABPerson
default	20:42:53.684065-0500	Nexy	0000 Contact: 4E4C0E62-3EE9-4F23-A226-025907D6882D:ABPerson
default	20:42:53.684073-0500	Nexy	0000 Contact: 1006869C-954C-4394-BFE9-09E9CE09AFB5:ABPerson
default	20:42:53.684078-0500	Nexy	0000 Contact: 339B0201-420C-414B-96CB-1D8150AEF6BB:ABPerson
default	20:42:53.684089-0500	Nexy	0000 Contact: 6A713058-BCB2-4635-BC21-577F0261940C:ABPerson
default	20:42:53.684094-0500	Nexy	0000 Contact: 8B61AAC1-DF6F-440A-B5AC-33331AF930E1:ABPerson
default	20:42:53.684104-0500	Nexy	0000 Contact: B5C0C11D-6F8A-4CCE-872A-DEC086F666A6:ABPerson
default	20:42:53.684108-0500	Nexy	0000 Contact: D17EDFE8-D58A-41FF-B738-D480ED1B54BB:ABPerson
default	20:42:53.684118-0500	Nexy	0000 Contact: 8D969F0D-4878-45C3-A329-14C8F1B9A1C4:ABPerson
default	20:42:53.684123-0500	Nexy	0000 Contact: 4DC763F6-4288-4A25-AE37-52DAC0E54434:ABPerson
default	20:42:53.684134-0500	Nexy	0000 Contact: BB62CE57-7037-4156-BE7F-D1E84FA0B46F:ABPerson
default	20:42:53.684139-0500	Nexy	0000 Contact: 32598CF7-ABA5-4AF8-B60C-8B3F9BB79824:ABPerson
default	20:42:53.684148-0500	Nexy	0000 Contact: 4C93D59E-2641-437E-8D5E-6E5135B4B9D7:ABPerson
default	20:42:53.684153-0500	Nexy	0000 Contact: 95C0601A-0362-4E71-9B56-8E66BA6334DB:ABPerson
default	20:42:53.684161-0500	Nexy	0000 Contact: F23EFEDD-DB9E-4EEE-86A8-A0BB0B161DCE:ABPerson
default	20:42:53.684168-0500	Nexy	0000 Contact: A25C8DA8-E066-47BE-A228-BA3A79122649:ABPerson
default	20:42:53.684180-0500	Nexy	0000 Contact: 7709CB5C-F45D-4130-AFCC-F66EB248B381:ABPerson
default	20:42:53.684185-0500	Nexy	0000 Contact: A95901C1-18E2-412B-9429-B9A87D46EEF1:ABPerson
default	20:42:53.684190-0500	Nexy	0000 Contact: 90CCE3F7-7CB8-44CE-8E3B-0E1FEE5B8574:ABPerson
default	20:42:53.684195-0500	Nexy	0000 Contact: D21F44BE-5C0B-49C1-ACBC-50C7FDD0E574:ABPerson
default	20:42:53.684206-0500	Nexy	0000 Contact: 9A341135-6F8F-42C6-A5D8-776E0F0EF424:ABPerson
default	20:42:53.684211-0500	Nexy	0000 Contact: 60C9F9CC-1758-4215-94FA-79E8E5591D0D:ABPerson
default	20:42:53.684222-0500	Nexy	0000 Contact: 7A0D8FED-170A-4F26-B868-532276E4BDF6:ABPerson
default	20:42:53.684227-0500	Nexy	0000 Contact: 791662EB-B4C3-41EA-8207-065A1C9F0AA0:ABPerson
default	20:42:53.684232-0500	Nexy	0000 Contact: D5AB1F03-8C06-438F-8713-DCCBBCD76892:ABPerson
default	20:42:53.684243-0500	Nexy	0000 Contact: 96EC0E50-9CC0-4769-8082-E7C877889553:ABPerson
default	20:42:53.684248-0500	Nexy	0000 Contact: 33394098-1926-4C5F-AA29-7B8610A5C7E6:ABPerson
default	20:42:53.684257-0500	Nexy	0000 Contact: B5956767-6E1D-49F2-8708-69E0D16EC786:ABPerson
default	20:42:53.684266-0500	Nexy	0000 Contact: 918AF5E7-EDE6-400D-A786-261C7B3BC323:ABPerson
default	20:42:53.684272-0500	Nexy	0000 Contact: 78374AF4-D2CF-4636-B824-5922E7BCDAA7:ABPerson
default	20:42:53.684284-0500	Nexy	0000 Contact: E1E5926D-F19D-45D4-9FFE-12E3198D0E67:ABPerson
default	20:42:53.684289-0500	Nexy	0000 Contact: DB957E68-3771-4194-AB47-1B347BE66F63:ABPerson
default	20:42:53.684298-0500	Nexy	0000 Contact: 2112C6EB-840A-49FE-B03E-5DDBFE2F6992:ABPerson
default	20:42:53.684304-0500	Nexy	0000 Contact: 3E8DAA1B-0AD6-465E-BDAB-A68A5FD23D3E:ABPerson
default	20:42:53.684313-0500	Nexy	0000 Contact: 5B8A6BDC-5927-4718-B89F-674DCC70DA16:ABPerson
default	20:42:53.684319-0500	Nexy	0000 Contact: 44BFDAD7-D780-4604-8369-CD3317F7F3FB:ABPerson
default	20:42:53.684328-0500	Nexy	0000 Contact: DD452BC2-AA0F-4E55-9417-30946834E7D9:ABPerson
default	20:42:53.684336-0500	Nexy	0000 Contact: A79E1C58-6726-4518-9160-5833FD1D9E85:ABPerson
default	20:42:53.684343-0500	Nexy	0000 Contact: EEDB6E81-803C-4D9E-9479-23840064FF07:ABPerson
default	20:42:53.684346-0500	Nexy	0000 Contact: E8BAA178-7C7C-4B0C-837F-07B80E6A8155:ABPerson
default	20:42:53.684353-0500	Nexy	0000 Contact: A8C84C99-FF9C-48DF-A603-CEB3050F0BC6:ABPerson
default	20:42:53.684361-0500	Nexy	0000 Contact: 0FD65269-7801-440C-A119-71EBE23C4E70:ABPerson
default	20:42:53.684370-0500	Nexy	0000 Contact: 0A4FEAE5-C426-4926-8B49-A5260D97B9E6:ABPerson
default	20:42:53.684376-0500	Nexy	0000 Contact: CA81313F-6121-4FF6-B60C-EEE869ECF990:ABPerson
default	20:42:53.684386-0500	Nexy	0000 Contact: EA9B96E2-2F87-4EB2-AD12-46F37DFF0EC9:ABPerson
default	20:42:53.684392-0500	Nexy	0000 Contact: 7A89C56B-6D06-419B-A08D-00F14B94AA1C:ABPerson
default	20:42:53.684402-0500	Nexy	0000 Contact: 660A1E96-3CA3-48B5-B94A-96D6D35A72E6:ABPerson
default	20:42:53.684410-0500	Nexy	0000 Contact: 3F5D85F3-9B89-4AD7-A353-FEFEA5DA1C36:ABPerson
default	20:42:53.684417-0500	Nexy	0000 Contact: 8F99EACB-5E71-4F4C-9899-AE7E1FF5280E:ABPerson
default	20:42:53.684423-0500	Nexy	0000 Contact: 9E8B52AD-B9B2-41CA-8134-7861A90F9A02:ABPerson
default	20:42:53.684432-0500	Nexy	0000 Contact: 98237DEC-70B4-4CA5-A4B8-FEE401C3F3C4:ABPerson
default	20:42:53.684442-0500	Nexy	0000 Contact: BD690A56-23D5-4941-B041-50C06351C977:ABPerson
default	20:42:53.684447-0500	Nexy	0000 Contact: D191A589-BA65-49F2-86A3-08D90FB284FD:ABPerson
default	20:42:53.684459-0500	Nexy	0000 Contact: AAF5FE8A-214C-4B65-9B4F-C2578C97C51D:ABPerson
default	20:42:53.684465-0500	Nexy	0000 Contact: 3D737248-8F03-4732-8B3A-8CDA2D45B5AA:ABPerson
default	20:42:53.684478-0500	Nexy	0000 Contact: E120A189-E8F5-4B5F-A2A2-B1A60E6DF145:ABPerson
default	20:42:53.684483-0500	Nexy	0000 Contact: 46187B48-32E0-4B21-B7CE-D3B44766EEEC:ABPerson
default	20:42:53.684492-0500	Nexy	0000 Contact: B72ACD21-62D9-4BC2-8F5A-F33464EEEED5:ABPerson
default	20:42:53.684497-0500	Nexy	0000 Contact: 1D1B1CB1-D316-4BC5-B11C-BC2D4D437605:ABPerson
default	20:42:53.684505-0500	Nexy	0000 Contact: EEC7F987-F555-4025-8B35-10CBE93E26D7:ABPerson
default	20:42:53.684514-0500	Nexy	0000 Contact: A4F96105-C3FC-4D3D-842F-E729A3F28760:ABPerson
default	20:42:53.684520-0500	Nexy	0000 Contact: F0613D78-6887-4B13-AC52-703B5D1A7060:ABPerson
default	20:42:53.684528-0500	Nexy	0000 Contact: BDD5E012-4C2D-4949-9778-80672887C0EC:ABPerson
default	20:42:53.684534-0500	Nexy	0000 Contact: E03CBC1C-C4D5-476B-A9AE-20A246A5FE73:ABPerson
default	20:42:53.684541-0500	Nexy	0000 Contact: A9567605-C983-4D5B-9877-2D3BC5D341CF:ABPerson
default	20:42:53.684551-0500	Nexy	0000 Contact: 378D10F9-7887-44F8-B0A5-9683F2AF012D:ABPerson
default	20:42:53.684560-0500	Nexy	0000 Contact: 29F7EE25-03CA-4DEA-AB4C-5E84B0046094:ABPerson
default	20:42:53.684566-0500	Nexy	0000 Contact: 6045438B-32EF-4240-BCDE-3A83DD6098C1:ABPerson
default	20:42:53.684575-0500	Nexy	0000 Contact: CC00B3CB-4536-414F-8E8F-116901AAAB66:ABPerson
default	20:42:53.684580-0500	Nexy	0000 Contact: CDF1FCD3-669F-4B16-9D7A-07091B53B43E:ABPerson
default	20:42:53.684588-0500	Nexy	0000 Contact: 1C7A8AAA-2853-4C56-892C-93832C406B2F:ABPerson
default	20:42:53.684597-0500	Nexy	0000 Contact: 5FA233B8-A72C-468F-8344-138CB3A320AD:ABPerson
default	20:42:53.684603-0500	Nexy	0000 Contact: CC42A082-921C-4A2F-9B2A-20AD5E63DE26:ABPerson
default	20:42:53.684612-0500	Nexy	0000 Contact: 4D22B39B-A7C9-4F71-B531-0D0A75E819DC:ABPerson
default	20:42:53.684621-0500	Nexy	0000 Contact: 10DA5D0D-F87E-40C2-A2FB-1B4E18ADEED7:ABPerson
default	20:42:53.684627-0500	Nexy	0000 Contact: 1020F64F-877A-46EF-A85B-0B7B4702F30A:ABPerson
default	20:42:53.684634-0500	Nexy	0000 Contact: 7A3258A0-4EF6-4C07-8BAC-DE67AFC5BF0F:ABPerson
default	20:42:53.684642-0500	Nexy	0000 Contact: D8BF88A0-50CD-408B-91AC-FABB6153F0E7:ABPerson
default	20:42:53.684647-0500	Nexy	0000 Contact: F96FB111-3581-4F57-A0DB-8D18E0A5CE3D:ABPerson
default	20:42:53.684658-0500	Nexy	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	20:42:53.684665-0500	Nexy	0000 Contact: 2DD46A4A-00EA-4AF2-BED6-A0E4704A401E:ABPerson
default	20:42:53.684674-0500	Nexy	0000 Contact: E75A43A8-9126-46AD-BDE0-2F09D8195FCE:ABPerson
default	20:42:53.684679-0500	Nexy	0000 Contact: 0CE70590-2C7E-400D-AAC3-E2AB83B20E6D:ABPerson
default	20:42:53.684689-0500	Nexy	0000 Contact: C93B2BF3-4882-418D-A785-20AABA5900CA:ABPerson
default	20:42:53.684695-0500	Nexy	0000 Contact: 72A79220-BD0A-4F38-A644-7891B8D6D08C:ABPerson
default	20:42:53.684700-0500	Nexy	0000 Contact: 5168F235-33BF-487B-9C88-9A0977EF3D96:ABPerson
default	20:42:53.684710-0500	Nexy	0000 Contact: EF5D8980-C0E4-4FBD-8942-AC7EC9F886BE:ABPerson
default	20:42:53.684715-0500	Nexy	0000 Contact: 8335160D-3EFF-4C7A-B500-08D4AAF9D6C4:ABPerson
default	20:42:53.684725-0500	Nexy	0000 Contact: F30C415E-480E-47D7-A697-2DDF78C62B78:ABPerson
default	20:42:53.684731-0500	Nexy	0000 Contact: 4B86EE6B-7192-4DEC-9A5D-DB2A68A29544:ABPerson
default	20:42:53.684740-0500	Nexy	0000 Contact: 7028A821-E1BB-4996-9F0A-B483955BBD46:ABPerson
default	20:42:53.684750-0500	Nexy	0000 Contact: 7C930844-C857-4F62-B795-A317F57982E7:ABPerson
default	20:42:53.684755-0500	Nexy	0000 Contact: 2958D2B1-193E-4859-97A7-E9D0A6DDAC5B:ABPerson
default	20:42:53.684767-0500	Nexy	0000 Contact: CF7AC9E0-68F2-4C92-A7E7-2F56630F8B8B:ABPerson
default	20:42:53.684772-0500	Nexy	0000 Contact: ADDCC376-3417-4952-A610-3D53B96EC2BD:ABPerson
default	20:42:53.684778-0500	Nexy	0000 Contact: 19855E2F-023D-4999-A9F8-0515B5257D6F:ABPerson
default	20:42:53.684783-0500	Nexy	0000 Contact: 2BAB4AEF-3D51-42E4-BBCA-4587A6EF5B42:ABPerson
default	20:42:53.684793-0500	Nexy	0000 Contact: B68F306A-9F87-4675-9C7C-73ADAC3CF928:ABPerson
default	20:42:53.684798-0500	Nexy	0000 Contact: EBEFEBC5-E9A8-48CB-B48D-DE0E2C3AE2B9:ABPerson
default	20:42:53.684808-0500	Nexy	0000 Contact: C1E29AB3-927E-4614-A170-469712D37DE0:ABPerson
default	20:42:53.684813-0500	Nexy	0000 Contact: 1E18829A-DFA4-4A9A-AEBA-FFF85B2D3E00:ABPerson
default	20:42:53.684823-0500	Nexy	0000 Contact: 41E94FCB-1477-45AF-AB50-6AF7C4651D76:ABPerson
default	20:42:53.684834-0500	Nexy	0000 Contact: 55D05EF1-7380-43F3-9CCC-FCCBB0A382A9:ABPerson
default	20:42:53.684839-0500	Nexy	0000 Contact: 88B8B688-3607-4FD1-BE7E-73F6DAA20674:ABPerson
default	20:42:53.684847-0500	Nexy	0000 Contact: 6A7FA276-678E-44BC-A5CD-1E7AB887CD37:ABPerson
default	20:42:53.684853-0500	Nexy	0000 Contact: A6FD2708-9CD8-45E0-9E88-5BE836285468:ABPerson
default	20:42:53.684863-0500	Nexy	0000 Contact: FFBA4F3C-8FF6-4FC6-9CB6-F62755FFB90C:ABPerson
default	20:42:53.684874-0500	Nexy	0000 Contact: F5A10DB4-BCD8-4342-9435-C976615D2367:ABPerson
default	20:42:53.684879-0500	Nexy	0000 Contact: 1C210F17-EE8F-4513-8100-4877479969F3:ABPerson
default	20:42:53.684887-0500	Nexy	0000 Contact: E6ACEB4F-3D7F-4D37-8463-568D34A3D393:ABPerson
default	20:42:53.684892-0500	Nexy	0000 Contact: 05B170A2-D739-4BCB-A7A9-927DAAC7B3FD:ABPerson
default	20:42:53.684901-0500	Nexy	0000 Contact: 791F5495-5017-4DBF-ABB6-4220285C8A7F:ABPerson
default	20:42:53.684911-0500	Nexy	0000 Contact: DFA3FE46-B8CF-41EC-B2E6-04C798B63209:ABPerson
default	20:42:53.684916-0500	Nexy	0000 Contact: 09772BD5-23E2-45C0-8579-EAA3F5DFAA04:ABPerson
default	20:42:53.684926-0500	Nexy	0000 Contact: 21D1D25A-A332-455E-BF6D-219DAED4CF2E:ABPerson
default	20:42:53.684935-0500	Nexy	0000 Contact: 85CBC919-29F4-4481-90E8-91811DF04251:ABPerson
default	20:42:53.684942-0500	Nexy	0000 Contact: 7D4E6C00-B562-4BD3-84B2-BE3484A218DC:ABPerson
default	20:42:53.684947-0500	Nexy	0000 Contact: 7CEA1D92-BD70-4661-A995-FC9C088765E4:ABPerson
default	20:42:53.684952-0500	Nexy	0000 Contact: 5BC153A8-ECD2-4153-8199-62D228ED9EFF:ABPerson
default	20:42:53.684963-0500	Nexy	0000 Contact: 539E00F6-4B11-4899-9B48-833F1C83B1AF:ABPerson
default	20:42:53.684969-0500	Nexy	0000 Contact: 480BDC40-266E-44A2-A7F0-81FF207F9107:ABPerson
default	20:42:53.684974-0500	Nexy	0000 Contact: AD76EC2F-309C-4663-88AB-5380B537AD21:ABPerson
default	20:42:53.684979-0500	Nexy	0000 Contact: E8D00EFB-149F-4D70-9E53-DCC37B11CA41:ABPerson
default	20:42:53.684989-0500	Nexy	0000 Contact: F1AC5DD9-2463-40B4-A31D-D698D4A81A07:ABPerson
default	20:42:53.684995-0500	Nexy	0000 Contact: 5CC4AD9E-AFA2-4D91-93BB-A2AEE0287CA1:ABPerson
default	20:42:53.685003-0500	Nexy	0000 Contact: 82273310-7E56-45DD-8F38-49E6EFB991AF:ABPerson
default	20:42:53.685009-0500	Nexy	0000 Contact: 52C4710F-7736-48E9-81CB-BFB715D2471F:ABPerson
default	20:42:53.685019-0500	Nexy	0000 Contact: 3DAF2C1D-E01A-4ECE-88B6-7A1FEC8F43AC:ABPerson
default	20:42:53.685028-0500	Nexy	0000 Contact: C66A3203-5558-449A-90CB-DECEC564C830:ABPerson
default	20:42:53.685034-0500	Nexy	0000 Contact: 1587F0BD-924E-4B7A-B625-9C3C29B7D02B:ABPerson
default	20:42:53.685043-0500	Nexy	0000 Contact: 8E669F37-64D4-4FCD-83DF-C7AB7025BAED:ABPerson
default	20:42:53.685048-0500	Nexy	0000 Contact: 42E8C30D-1FB0-42FC-833E-588AB5BBE3DB:ABPerson
default	20:42:53.685060-0500	Nexy	0000 Contact: EAE3066F-0C4F-41A6-8DBE-F68459786EC0:ABPerson
default	20:42:53.685065-0500	Nexy	0000 Contact: 2AF16E0B-3963-42BF-9826-D9FEA11B3CCA:ABPerson
default	20:42:53.685075-0500	Nexy	0000 Contact: 319E891D-32E9-49AF-B4E4-B5BAE8155200:ABPerson
default	20:42:53.685080-0500	Nexy	0000 Contact: 1594CB17-7E0F-473A-929D-C52CB3C2ADF4:ABPerson
default	20:42:53.685089-0500	Nexy	0000 Contact: 77010702-80A2-4E97-B0A7-B2EE441BFF58:ABPerson
default	20:42:53.685096-0500	Nexy	0000 Contact: 878309A1-31D9-4B89-8226-32C4BFA85E5A:ABPerson
default	20:42:53.685106-0500	Nexy	0000 Contact: 8C53459B-D709-4754-8779-C759C5D30623:ABPerson
default	20:42:53.685111-0500	Nexy	0000 Contact: 2D7A7BAB-3BDE-4E62-9336-46D7687262C6:ABPerson
default	20:42:53.685117-0500	Nexy	0000 Contact: ADE039BB-356A-4FF6-9B48-11643C1A74A3:ABPerson
default	20:42:53.685127-0500	Nexy	0000 Contact: 1DAA78BA-EBAD-4BF6-B582-A4DE8A4A1F60:ABPerson
default	20:42:53.685132-0500	Nexy	0000 Contact: E3B3AD82-9DE2-41D8-BAB4-955DF431F0D7:ABPerson
default	20:42:53.685141-0500	Nexy	0000 Contact: 4EA7F008-36E8-457A-AB52-5E92AB655707:ABPerson
default	20:42:53.685149-0500	Nexy	0000 Contact: 2EE1FF46-FBE2-4A40-8CE4-EC8C163406A8:ABPerson
default	20:42:53.685154-0500	Nexy	0000 Contact: 4749FF87-CDF6-4765-A605-FBF954CEC3DD:ABPerson
default	20:42:53.685163-0500	Nexy	0000 Contact: 78533628-5040-45D4-907C-06311D0B83C8:ABPerson
default	20:42:53.685172-0500	Nexy	0000 Contact: 55ED3DE3-FD66-4A5E-995C-7174A0F57355:ABPerson
default	20:42:53.685180-0500	Nexy	0000 Contact: 1EB3E13D-C8C2-40B4-B5C1-95672F5BB775:ABPerson
default	20:42:53.685185-0500	Nexy	0000 Contact: F83287C3-CE0B-407B-88A2-A5B43CAB98EC:ABPerson
default	20:42:53.685194-0500	Nexy	0000 Contact: 2D1AC54F-1C05-415F-803B-EB84B4DE155C:ABPerson
default	20:42:53.685199-0500	Nexy	0000 Contact: C8633A15-35F4-4ABC-9A2A-82EBF1A6767D:ABPerson
default	20:42:53.685209-0500	Nexy	0000 Contact: D62A5235-E401-4A9F-AC82-61328161530D:ABPerson
default	20:42:53.685218-0500	Nexy	0000 Contact: C80DE5B6-E12E-4835-863B-E63D84C0DEB5:ABPerson
default	20:42:53.685228-0500	Nexy	0000 Contact: 922530A8-0D72-4067-AAC0-1FF5C4ABE1BA:ABPerson
default	20:42:53.685234-0500	Nexy	0000 Contact: A66AB62E-7C4B-489D-A5AC-97BE240AF07B:ABPerson
default	20:42:53.685237-0500	Nexy	0000 Contact: C42862EB-E49A-4500-B5A0-744247A93DC0:ABPerson
default	20:42:53.685242-0500	Nexy	0000 Contact: 3608E376-1FDF-4DA6-94BE-B39CF8F32D25:ABPerson
default	20:42:53.685254-0500	Nexy	0000 Contact: 3D44B959-62DC-41CB-825F-C0FB5D231322:ABPerson
default	20:42:53.685264-0500	Nexy	0000 Contact: 47FCBCE3-65D3-44A4-8283-4C1AF6654C9F:ABPerson
default	20:42:53.685270-0500	Nexy	0000 Contact: 93BAC1B1-3857-40CA-A143-09E6F7A990EF:ABPerson
default	20:42:53.685277-0500	Nexy	0000 Contact: F1B433EB-BB39-4CD7-A784-1E41309B908C:ABPerson
default	20:42:53.685283-0500	Nexy	0000 Contact: A52B8A51-99C7-427A-BD9F-97EC5E9F7EA8:ABPerson
default	20:42:53.685293-0500	Nexy	0000 Contact: 0191E2F5-DF4D-441F-A40B-BBEE1682877B:ABPerson
default	20:42:53.685303-0500	Nexy	0000 Contact: 0697FA50-06C8-4FDB-A5D3-B10F8A859674:ABPerson
default	20:42:53.685307-0500	Nexy	0000 Contact: 093F142A-458F-4ACF-BEEE-FAB7BA5E520A:ABPerson
default	20:42:53.685313-0500	Nexy	0000 Contact: 98F95301-000C-4EF9-91DF-E637EF0C27F4:ABPerson
default	20:42:53.685323-0500	Nexy	0000 Contact: 720814F5-D603-40AE-A834-D49467F3A7FD:ABPerson
default	20:42:53.685329-0500	Nexy	0000 Contact: 40CDB1E4-DC18-4D79-AE2F-6242CCF62978:ABPerson
default	20:42:53.685338-0500	Nexy	0000 Contact: A8D9C348-1926-49B7-98C2-A2C917FB651B:ABPerson
default	20:42:53.685348-0500	Nexy	0000 Contact: 7656FBDF-5810-4382-9538-529EC1E5EF83:ABPerson
default	20:42:53.685353-0500	Nexy	0000 Contact: 8F442B0B-AFC7-4087-AEFC-FDC987F28E2C:ABPerson
default	20:42:53.685364-0500	Nexy	0000 Contact: DE96F2D0-DA7E-4742-AD3E-6D43BC32C213:ABPerson
default	20:42:53.685369-0500	Nexy	0000 Contact: DA1B14DD-D92B-4633-BF3C-0CCCE7117BE4:ABPerson
default	20:42:53.685378-0500	Nexy	0000 Contact: 0134E272-51ED-44B6-AC46-4C34642F56AA:ABPerson
default	20:42:53.685384-0500	Nexy	0000 Contact: FA551EE7-6781-4874-B9EA-0B6893B3293F:ABPerson
default	20:42:53.685391-0500	Nexy	0000 Contact: A88C8AF6-EF10-48E8-9C60-3709424155EB:ABPerson
default	20:42:53.685398-0500	Nexy	0000 Contact: C00692B4-EC26-459C-A690-D23F5BCEF621:ABPerson
default	20:42:53.685408-0500	Nexy	0000 Contact: 652921DA-B2DA-4539-A7F6-6B5A80149E2C:ABPerson
default	20:42:53.685419-0500	Nexy	0000 Contact: 88DED267-1D14-49FB-B0EA-D61FEEEA7475:ABPerson
default	20:42:53.685424-0500	Nexy	0000 Contact: CEB05018-C421-4234-BE90-56F8041F2286:ABPerson
default	20:42:53.685429-0500	Nexy	0000 Contact: DFB23C20-7349-4617-9A20-48014D8D844F:ABPerson
default	20:42:53.685440-0500	Nexy	0000 Contact: 9AC48DA6-FEAA-4630-AD56-EF041D62524A:ABPerson
default	20:42:53.685445-0500	Nexy	0000 Contact: 936230C2-1597-4A80-898D-31476BAE0C72:ABPerson
default	20:42:53.685456-0500	Nexy	0000 Contact: E99AC935-51E8-4AC2-9D90-C3ED9A41CF89:ABPerson
default	20:42:53.685465-0500	Nexy	0000 Contact: 1041C9F3-A247-4866-BCE3-A908919C3641:ABPerson
default	20:42:53.685470-0500	Nexy	0000 Contact: AA55B04C-AA66-4E4C-BE73-FCD01D057FF4:ABPerson
default	20:42:53.685480-0500	Nexy	0000 Contact: 8E1DE28A-250A-438D-ADCC-EC00B09AFDCF:ABPerson
default	20:42:53.685486-0500	Nexy	0000 Contact: 9D974937-BC35-459C-9596-7F3C287A39DE:ABPerson
default	20:42:53.685496-0500	Nexy	0000 Contact: 7A52455B-63F6-4500-850D-4CD4CAEE7CDA:ABPerson
default	20:42:53.685504-0500	Nexy	0000 Contact: BB0E685F-E844-4A51-8837-01C68FCCEECD:ABPerson
default	20:42:53.685511-0500	Nexy	0000 Contact: 958F31A6-1E1B-4833-99AC-EC3D8191CACE:ABPerson
default	20:42:53.685519-0500	Nexy	0000 Contact: 88212F02-02C2-4E0B-AD31-33A4F57D97C3:ABPerson
default	20:42:53.685528-0500	Nexy	0000 Contact: 060A07B0-DE54-4CA0-82F9-C5E7D642FE04:ABPerson
default	20:42:53.685534-0500	Nexy	0000 Contact: 84FD0E15-D8B4-4C4A-AF3F-ECACC4D7D2AB:ABPerson
default	20:42:53.685539-0500	Nexy	0000 Contact: E03C33D7-9B66-41CC-9823-13495C0F1BFF:ABPerson
default	20:42:53.685549-0500	Nexy	0000 Contact: 4F05D0EB-A7C7-4CE9-8BBE-252CDE0913B6:ABPerson
default	20:42:53.685554-0500	Nexy	0000 Contact: 0D4D94BE-BE27-4924-B1EF-D18DBC8CB9CB:ABPerson
default	20:42:53.685560-0500	Nexy	0000 Contact: DE3244DE-AA8B-42BE-9E6B-D93D5F072FC8:ABPerson
default	20:42:53.685566-0500	Nexy	0000 Contact: D2349093-8AC3-493E-A63B-2FDDBF010597:ABPerson
default	20:42:53.685576-0500	Nexy	0000 Contact: 582B6770-D754-4F28-BE23-DE8B912C1D70:ABPerson
default	20:42:53.685583-0500	Nexy	0000 Contact: 7230DAA8-42F7-4810-9E64-7E0576DEC21F:ABPerson
default	20:42:53.685587-0500	Nexy	0000 Contact: A044BEEF-238E-4A88-9B39-26B87097EDBA:ABPerson
default	20:42:53.685599-0500	Nexy	0000 Contact: 37C10F00-3A36-4D68-A9FE-F7CBB93250AA:ABPerson
default	20:42:53.685604-0500	Nexy	0000 Contact: BF90E79B-597F-4512-8E44-EA4CE870BBE2:ABPerson
default	20:42:53.685615-0500	Nexy	0000 Contact: BC75C771-F624-4E3A-AD7C-60B2F270D59D:ABPerson
default	20:42:53.685621-0500	Nexy	0000 Contact: C9795424-7E48-45EA-BBDF-4E008BDD9978:ABPerson
default	20:42:53.685627-0500	Nexy	0000 Contact: 40A1ED53-5876-46E0-B311-D54958985F34:ABPerson
default	20:42:53.685636-0500	Nexy	0000 Contact: 7E4C40BE-99FF-4182-ACF1-5DF8D2DDBE83:ABPerson
default	20:42:53.685642-0500	Nexy	0000 Contact: 6E048310-6707-4D3C-BD0B-81F080042AD6:ABPerson
default	20:42:53.685652-0500	Nexy	0000 Contact: 7268EB56-C8B9-4982-99B0-A40D08B65BA9:ABPerson
default	20:42:53.685662-0500	Nexy	0000 Contact: 0E2D5908-AAC6-40CB-BFB1-0CE7506D0A99:ABPerson
default	20:42:53.685669-0500	Nexy	0000 Contact: D2628142-CF91-46B0-A289-5CA32977E44D:ABPerson
default	20:42:53.685676-0500	Nexy	0000 Contact: 914E27F4-B07C-487A-BF66-F3CA485B9275:ABPerson
default	20:42:53.685684-0500	Nexy	0000 Contact: D014DC3B-188A-4277-A1D5-FBE211695D60:ABPerson
default	20:42:53.685689-0500	Nexy	0000 Contact: 48C9CC87-0557-4A05-B9B6-9FC3799AA710:ABPerson
default	20:42:53.685698-0500	Nexy	0000 Contact: D19BADAB-1850-4DC5-BEEF-B4D77FFCF312:ABPerson
default	20:42:53.685704-0500	Nexy	0000 Contact: 5F52D0B4-4801-47FD-A2E8-E1EC4C2CFBF7:ABPerson
default	20:42:53.685713-0500	Nexy	0000 Contact: F8F59880-57E4-410D-B266-90532EAA85ED:ABPerson
default	20:42:53.685722-0500	Nexy	0000 Contact: 894EBF35-6AF8-4262-8E87-8394A0235AEA:ABPerson
default	20:42:53.685728-0500	Nexy	0000 Contact: 57AEA313-D5E2-4575-AA16-1A5115913CC7:ABPerson
default	20:42:53.685738-0500	Nexy	0000 Contact: F89D0C36-26A8-41DC-83C9-B4FBE705654B:ABPerson
default	20:42:53.685743-0500	Nexy	0000 Contact: 1B9D8EA6-9499-4BFC-8492-1342D6A1460A:ABPerson
default	20:42:53.685753-0500	Nexy	0000 Contact: 35990211-93E2-4128-9887-673DB78EB237:ABPerson
default	20:42:53.685760-0500	Nexy	0000 Contact: E09D3D05-8D17-403A-BB6D-AE0A7DAC6A91:ABPerson
default	20:42:53.685770-0500	Nexy	0000 Contact: 6947AB19-73BD-4633-9B74-8444F2D5EB48:ABPerson
default	20:42:53.685775-0500	Nexy	0000 Contact: 327524E2-8EE7-43AD-A10C-4D95E5236B33:ABPerson
default	20:42:53.685784-0500	Nexy	0000 Contact: 5C927C23-EC97-4E44-979D-C91168A0225F:ABPerson
default	20:42:53.685790-0500	Nexy	0000 Contact: 3E96739C-79E5-47F2-8D58-297DAFFED273:ABPerson
default	20:42:53.685798-0500	Nexy	0000 Contact: 923B5225-B958-47B8-A994-56D2C6594BC3:ABPerson
default	20:42:53.685810-0500	Nexy	0000 Contact: 71E3945F-552E-4A87-81E7-3B4F6B837FB0:ABPerson
default	20:42:53.685815-0500	Nexy	0000 Contact: 98BB4D37-BA08-403B-863B-EA841E79DDEC:ABPerson
default	20:42:53.685823-0500	Nexy	0000 Contact: 3C958CB9-9822-42CE-908D-E1263845615F:ABPerson
default	20:42:53.685831-0500	Nexy	0000 Contact: 99F6FF83-6AC8-4BB2-A7FB-0E45BF397CE1:ABPerson
default	20:42:53.685836-0500	Nexy	0000 Contact: ECEB9C46-3E9A-4B07-BA0A-83A9F5AC9BD8:ABPerson
default	20:42:53.685846-0500	Nexy	0000 Contact: 2D8CF878-704D-4216-A869-2AA3CE40DC8B:ABPerson
default	20:42:53.685856-0500	Nexy	0000 Contact: D6E1C189-3EE0-4001-BBD7-BA1BAA052DCD:ABPerson
default	20:42:53.685864-0500	Nexy	0000 Contact: 0FB6D688-1124-496D-8A74-936908325AC4:ABPerson
default	20:42:53.685869-0500	Nexy	0000 Contact: 8E63BF2D-7068-4689-AA89-3F14A6D447C7:ABPerson
default	20:42:53.685878-0500	Nexy	0000 Contact: A6A438A5-EBCC-4387-AE2C-974496DF3475:ABPerson
default	20:42:53.685889-0500	Nexy	0000 Contact: A7980BCA-3250-42B1-9819-B7F094FC4046:ABPerson
default	20:42:53.685894-0500	Nexy	0000 Contact: 4C6A56D0-B520-49E0-8E8E-16BA4BC6CC20:ABPerson
default	20:42:53.685903-0500	Nexy	0000 Contact: C0FC9CF3-3693-4D44-981C-6047B6AEE5AB:ABPerson
default	20:42:53.685911-0500	Nexy	0000 Contact: 9436B5EC-36D3-4607-B5EB-7EF577DAA4E1:ABPerson
default	20:42:53.685918-0500	Nexy	0000 Contact: FC8D2904-8F71-4E20-8978-D780134A1143:ABPerson
default	20:42:53.685928-0500	Nexy	0000 Contact: 8E15809F-EDFE-43EB-A729-82985D40BEDD:ABPerson
default	20:42:53.685933-0500	Nexy	0000 Contact: 4CFCE671-0922-422E-84D2-7E3D755B9AA0:ABPerson
default	20:42:53.685941-0500	Nexy	0000 Contact: 97F9A37A-8704-4049-B22E-5464D3555283:ABPerson
default	20:42:53.685946-0500	Nexy	0000 Contact: 5EAB76EB-1518-4AB1-A60F-6440D4E97C67:ABPerson
default	20:42:53.685956-0500	Nexy	0000 Contact: 66AA346D-AFEA-46E3-AB76-B76AB73EEFE6:ABPerson
default	20:42:53.685966-0500	Nexy	0000 Contact: A94FA9D0-8D8F-482E-A1FA-415674AAE3CD:ABPerson
default	20:42:53.685971-0500	Nexy	0000 Contact: E26AEFB0-1D2D-4ED3-B1E2-B7D352747749:ABPerson
default	20:42:53.685980-0500	Nexy	0000 Contact: AE956307-DB6F-4D84-8479-F99A334DD9D9:ABPerson
default	20:42:53.685986-0500	Nexy	0000 Contact: D85CE9F6-4FD9-4FE4-BAC1-3B143BBF015B:ABPerson
default	20:42:53.685996-0500	Nexy	0000 Contact: D86C98C7-EA2A-4783-9D89-B5CCC7F3F76F:ABPerson
default	20:42:53.686002-0500	Nexy	0000 Contact: 9BD95D2C-57F9-41BC-82A1-01276B837DE5:ABPerson
default	20:42:53.686011-0500	Nexy	0000 Contact: D73A9313-DE0F-415F-AEB6-A3064AD4E8D4:ABPerson
default	20:42:53.686017-0500	Nexy	0000 Contact: 0D652AFC-47EC-4A75-8D39-2C5235F7B2D8:ABPerson
default	20:42:53.686028-0500	Nexy	0000 Contact: ACA1A5BD-6656-45E2-BD86-154568B82D42:ABPerson
default	20:42:53.686034-0500	Nexy	0000 Contact: 4EEB39AF-CB99-4D4F-99E0-813379D86B51:ABPerson
default	20:42:53.686044-0500	Nexy	0000 Contact: 37348E4E-8173-4E70-B552-CB72B6A9AF42:ABPerson
default	20:42:53.686049-0500	Nexy	0000 Contact: 3D23A662-D7CC-4235-A90D-B25C77F75FB1:ABPerson
default	20:42:53.686058-0500	Nexy	0000 Contact: F5DA0315-4AD8-41C4-B7CF-81A2E12E2691:ABPerson
default	20:42:53.686068-0500	Nexy	0000 Contact: 61773524-5763-4829-81ED-9B3EFF5744C8:ABPerson
default	20:42:53.686074-0500	Nexy	0000 Contact: 3A8DC04F-FBB6-495A-8E75-D22B3ACFD775:ABPerson
default	20:42:53.686084-0500	Nexy	0000 Contact: 8E1B53A0-CE9F-4B5A-BCD2-6FCBB2FE03C1:ABPerson
default	20:42:53.686089-0500	Nexy	0000 Contact: 927F81A1-D726-4969-8419-5DAAAB376B20:ABPerson
default	20:42:53.686098-0500	Nexy	0000 Contact: 499571CA-8847-4A36-8AFD-700D10BA01B6:ABPerson
default	20:42:53.686109-0500	Nexy	0000 Contact: 687940D3-01D3-4EE6-8DF6-B77137DF4358:ABPerson
default	20:42:53.686115-0500	Nexy	0000 Contact: AC2B4231-8E18-49D2-A6E0-4DAD10C52F8E:ABPerson
default	20:42:53.686124-0500	Nexy	0000 Contact: B9C8A612-D08C-4C98-AFEC-7B492BFFCF09:ABPerson
default	20:42:53.686134-0500	Nexy	0000 Contact: 4DE12C0D-88F3-46EA-AE7A-52A8C97B2642:ABPerson
default	20:42:53.686141-0500	Nexy	0000 Contact: 74E71AB9-12C3-492C-8D90-44002E96E279:ABPerson
default	20:42:53.686145-0500	Nexy	0000 Contact: F06E384F-51AB-4945-8C9A-CDDA3D1F1726:ABPerson
default	20:42:53.686152-0500	Nexy	0000 Contact: B4392798-7C17-4630-9433-A03FD74A67B6:ABPerson
default	20:42:53.686161-0500	Nexy	0000 Contact: 81B63730-E89B-4309-B937-6526BC363BE9:ABPerson
default	20:42:53.686167-0500	Nexy	0000 Contact: 67260B0D-B185-469D-A099-1F276E9003E9:ABPerson
default	20:42:53.686178-0500	Nexy	0000 Contact: 523939B5-07BC-4BA9-8827-8E5DE74ABD59:ABPerson
default	20:42:53.686184-0500	Nexy	0000 Contact: 448593D9-FFE0-4A5E-85CF-951EBD64FD34:ABPerson
default	20:42:53.686191-0500	Nexy	0000 Contact: 39E0059F-CE32-4A7F-8412-CBB5B8512D91:ABPerson
default	20:42:53.686197-0500	Nexy	0000 Contact: BD79F9BE-48FE-4B17-A966-4900444CB4BE:ABPerson
default	20:42:53.686204-0500	Nexy	0000 Contact: CB117BD9-26BB-482F-BE1D-474050D4F877:ABPerson
default	20:42:53.686211-0500	Nexy	0000 Contact: 1BE44750-F897-4471-B2BB-23F1750F6052:ABPerson
default	20:42:53.686220-0500	Nexy	0000 Contact: F521BF7D-BEA0-4970-8ABB-0D36D0C55CFB:ABPerson
default	20:42:53.686229-0500	Nexy	0000 Contact: B31F68AA-132A-4764-BF9C-07AFF1DFEBE9:ABPerson
default	20:42:53.686235-0500	Nexy	0000 Contact: BFC74FBC-8459-4E5C-926D-CA8CB584E493:ABPerson
default	20:42:53.686244-0500	Nexy	0000 Contact: 513D3922-7269-4052-92B9-A5DDC7F20D85:ABPerson
default	20:42:53.686253-0500	Nexy	0000 Contact: 1680643C-880B-4F66-A23A-54553511F91E:ABPerson
default	20:42:53.686259-0500	Nexy	0000 Contact: AC09AA75-399F-4388-B06D-B36195539921:ABPerson
default	20:42:53.686269-0500	Nexy	0000 Contact: 905AEE60-BF17-4861-8B9D-D8A7C93CA851:ABPerson
default	20:42:53.686280-0500	Nexy	0000 Contact: 605EC366-1BE6-4728-AF4F-35065DDE105E:ABPerson
default	20:42:53.686285-0500	Nexy	0000 Contact: 2E5AC2EB-1D50-48E4-A733-1565B7FBD9B0:ABPerson
default	20:42:53.686291-0500	Nexy	0000 Contact: 8DBBC6C7-2A3B-452A-A683-96B213129365:ABPerson
default	20:42:53.686301-0500	Nexy	0000 Contact: D1ABDE8F-AB3A-4A78-B366-8122520E469C:ABPerson
default	20:42:53.686309-0500	Nexy	0000 Contact: 2BBC7823-B462-47BC-97A1-FAF56A6CD6D4:ABPerson
default	20:42:53.686317-0500	Nexy	0000 Contact: CBBBAAFD-0C8A-4928-B6C5-104BD483B756:ABPerson
default	20:42:53.686323-0500	Nexy	0000 Contact: 7B546412-E513-4FAC-8F04-5B93F8284CD9:ABPerson
default	20:42:53.686331-0500	Nexy	0000 Contact: BEDFD270-E6D5-4BD4-9396-F461E76A3D6D:ABPerson
default	20:42:53.686337-0500	Nexy	0000 Contact: DFF04280-7038-4F29-96DF-CE1264E33F45:ABPerson
default	20:42:53.686347-0500	Nexy	0000 Contact: DA723208-FBEF-435F-9D7D-AF23C3292A04:ABPerson
default	20:42:53.686357-0500	Nexy	0000 Contact: 689B7484-1008-4903-8E58-C16D6135D1BE:ABPerson
default	20:42:53.686362-0500	Nexy	0000 Contact: 2EBB3BBB-AA1B-44AB-AEB2-507047DFB1BF:ABPerson
default	20:42:53.686372-0500	Nexy	0000 Contact: 2C4816A3-74B3-44EE-8613-D4A9EA487364:ABPerson
default	20:42:53.686378-0500	Nexy	0000 Contact: 327FE41D-07EB-426D-B40A-C41E6414A032:ABPerson
default	20:42:53.686383-0500	Nexy	0000 Contact: 661E42B6-4641-42DC-ADAD-F2F4F64E9A7F:ABPerson
default	20:42:53.686393-0500	Nexy	0000 Contact: 5B3F5B1B-AEB4-49F2-9295-98A6D2E90DF3:ABPerson
default	20:42:53.686399-0500	Nexy	0000 Contact: 3B9A0F65-3862-4239-9B4C-22A3937CB3E3:ABPerson
default	20:42:53.686409-0500	Nexy	0000 Contact: 1F5296B1-D8A8-4DEE-A3AC-4F6FF8EB8592:ABPerson
default	20:42:53.686415-0500	Nexy	0000 Contact: 83367917-4C48-420D-BED6-953D5D799BA3:ABPerson
default	20:42:53.686424-0500	Nexy	0000 Contact: CB81A645-AA3F-4E01-A5E8-7FFB1DE784B8:ABPerson
default	20:42:53.686434-0500	Nexy	0000 Contact: 76C1E860-76F6-46A7-AE8B-0B8D533979A1:ABPerson
default	20:42:53.686439-0500	Nexy	0000 Contact: 38D87E84-8FFA-4644-89BB-3B2C64683F25:ABPerson
default	20:42:53.686444-0500	Nexy	0000 Contact: BFC89011-6208-402B-902D-227391CF84D7:ABPerson
default	20:42:53.686450-0500	Nexy	0000 Contact: AE1E272C-12CF-4D37-AA16-321C66EB1922:ABPerson
default	20:42:53.686460-0500	Nexy	0000 Contact: 37AF5276-1B9C-4873-9D80-6BD7C5AE160B:ABPerson
default	20:42:53.686469-0500	Nexy	0000 Contact: 873FBA93-2932-4885-9ABA-B766E56EF823:ABPerson
default	20:42:53.686479-0500	Nexy	0000 Contact: DA14AB47-A56B-4F79-A505-4A5F3CF9709B:ABPerson
default	20:42:53.686484-0500	Nexy	0000 Contact: 5DBDC986-75E3-45D5-BDAC-840F64A095F3:ABPerson
default	20:42:53.686489-0500	Nexy	0000 Contact: 7E2E667C-A7D1-4A88-9C92-C2F38557DF00:ABPerson
default	20:42:53.686499-0500	Nexy	0000 Contact: 5307FC68-117A-42FB-92AA-DFB24F94E71D:ABPerson
default	20:42:53.686505-0500	Nexy	0000 Contact: 5F493737-ED28-4B1F-8903-5BA4CE98E525:ABPerson
default	20:42:53.686515-0500	Nexy	0000 Contact: 581AB38B-88DC-4442-B96C-20827400BCDB:ABPerson
default	20:42:53.686527-0500	Nexy	0000 Contact: E7A269EB-3583-4C11-9FA2-A805E372821C:ABPerson
default	20:42:53.686532-0500	Nexy	0000 Contact: 17A33554-E561-4BBD-9CEB-2A42D78570CB:ABPerson
default	20:42:53.686537-0500	Nexy	0000 Contact: B6294A95-D955-4DE1-981A-1C81A88B3C77:ABPerson
default	20:42:53.686542-0500	Nexy	0000 Contact: 2775B95B-E344-4E6E-860A-2E7C048D2F1D:ABPerson
default	20:42:53.686552-0500	Nexy	0000 Contact: C811339F-FA52-4CA4-B33E-D0F308EB497B:ABPerson
default	20:42:53.686557-0500	Nexy	0000 Contact: 3EBCE39A-CFA0-4AE5-A027-E77300906D8C:ABPerson
default	20:42:53.686566-0500	Nexy	0000 Contact: EE34E8D6-8FA8-43EA-956D-B93BBAEE1A85:ABPerson
default	20:42:53.686574-0500	Nexy	0000 Contact: 9502BE8E-CE6C-45C1-B06E-06F25C1B2DB2:ABPerson
default	20:42:53.686582-0500	Nexy	0000 Contact: CB72BAE7-75D4-4B69-B8B1-6F54BA25195A:ABPerson
default	20:42:53.686590-0500	Nexy	0000 Contact: 8ABDA833-5BB8-43D2-9DD4-D9977041708F:ABPerson
default	20:42:53.686595-0500	Nexy	0000 Contact: BC7FC3F8-6E58-42C6-8D38-58B4E05E74D8:ABPerson
default	20:42:53.686604-0500	Nexy	0000 Contact: 8C9E4B42-EDDD-4DA5-8291-79608D7118FD:ABPerson
default	20:42:53.686614-0500	Nexy	0000 Contact: 88A354D2-628D-4BBD-A9D2-4025114C2B74:ABPerson
default	20:42:53.686619-0500	Nexy	0000 Contact: D671E4A8-5C78-48DB-9F39-C9F55D0773F0:ABPerson
default	20:42:53.686630-0500	Nexy	0000 Contact: B55652C2-FF9A-492E-9E74-59BF77FF7657:ABPerson
default	20:42:53.686635-0500	Nexy	0000 Contact: D40BEEF6-659C-4640-8883-A886679E7683:ABPerson
default	20:42:53.686644-0500	Nexy	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	20:42:53.686652-0500	Nexy	0000 Contact: 2501625C-D3F0-448F-BE59-758CB4781991:ABPerson
default	20:42:53.686657-0500	Nexy	0000 Contact: 95793C06-46A7-463F-B79D-BD4828AA82E5:ABPerson
default	20:42:53.686667-0500	Nexy	0000 Contact: 39FB6543-CE8F-4850-B087-CB9BC9D83CD1:ABPerson
default	20:42:53.686677-0500	Nexy	0000 Contact: 4899EBC6-6B1B-4110-ACC0-42C6281F11F0:ABPerson
default	20:42:53.686686-0500	Nexy	0000 Contact: 2152007E-EC7F-40ED-A920-334BFEE05F62:ABPerson
default	20:42:53.686692-0500	Nexy	0000 Contact: E5FB73BD-A112-4CB1-A44C-4AE9AA8A7FD9:ABPerson
default	20:42:53.686701-0500	Nexy	0000 Contact: 9DF4B53B-8E66-438F-A541-31A6AC43028E:ABPerson
default	20:42:53.686709-0500	Nexy	0000 Contact: ED52C6FA-B011-454D-BF73-CD97015FEDF8:ABPerson
default	20:42:53.686714-0500	Nexy	0000 Contact: 637D6BED-2C4A-4F5E-9BF9-E5A8854E4DF1:ABPerson
default	20:42:53.686722-0500	Nexy	0000 Contact: 763CD797-4630-439F-982D-34ACFA2E7238:ABPerson
default	20:42:53.686732-0500	Nexy	0000 Contact: DE4A7BAA-4835-447E-9B59-F863ACBFA092:ABPerson
default	20:42:53.686738-0500	Nexy	0000 Contact: FE3ED792-5C16-4CA6-AD68-BBDFDF93EAC3:ABPerson
default	20:42:53.686743-0500	Nexy	0000 Contact: F5F336E5-374B-4E45-B851-690629571134:ABPerson
default	20:42:53.686753-0500	Nexy	0000 Contact: 00E52FC0-B1F1-47C4-A4E2-351A2927B2AC:ABPerson
default	20:42:53.686758-0500	Nexy	0000 Contact: 5AA6919D-04C9-470A-99B9-9FB0D437DA6A:ABPerson
default	20:42:53.686768-0500	Nexy	0000 Contact: 1FC22462-8E84-43E6-8F68-5D141CC903D6:ABPerson
default	20:42:53.686773-0500	Nexy	0000 Contact: 379EEF06-D880-4C4C-81B4-19232497B238:ABPerson
default	20:42:53.686781-0500	Nexy	0000 Contact: 9AA12C79-AC0F-40D8-82D4-7D1D1B6024D4:ABPerson
default	20:42:53.686790-0500	Nexy	0000 Contact: B584C21D-4B54-4F37-A1B1-B5EF3AEC170C:ABPerson
default	20:42:53.686796-0500	Nexy	0000 Contact: D2940461-BB6C-4224-8218-88019B5DB07D:ABPerson
default	20:42:53.686805-0500	Nexy	0000 Contact: 734CE2EC-7CFA-4475-B601-8F5A0EDC5AFC:ABPerson
default	20:42:53.686810-0500	Nexy	0000 Contact: 693CFFC7-F57A-478E-BBA2-CB65EB6C5425:ABPerson
default	20:42:53.686819-0500	Nexy	0000 Contact: 522D9347-0C39-4479-9A87-99551E9F992C:ABPerson
default	20:42:53.686827-0500	Nexy	0000 Contact: BC6A800E-2E2E-4B39-B37E-6639FBEE75EF:ABPerson
default	20:42:53.686836-0500	Nexy	0000 Contact: 4B6CD270-FA88-4F64-9F96-22BB79CBD541:ABPerson
default	20:42:53.686841-0500	Nexy	0000 Contact: 77ED343F-8BF8-4BFD-A0F9-901367A608BC:ABPerson
default	20:42:53.686850-0500	Nexy	0000 Contact: 37D2B9B0-053A-474C-BE44-09B4453D4050:ABPerson
default	20:42:53.686856-0500	Nexy	0000 Contact: 62B0EB86-C5BA-495C-9E28-535D2EF0354A:ABPerson
default	20:42:53.686867-0500	Nexy	0000 Contact: 670ECAAE-6CD8-4A3A-8EA6-614A11174BD6:ABPerson
default	20:42:53.686878-0500	Nexy	0000 Contact: A45DAD74-F719-4D46-9EA6-6DFEEF650375:ABPerson
default	20:42:53.686885-0500	Nexy	0000 Contact: B7008B2E-FA86-42D5-8656-CE248026D27E:ABPerson
default	20:42:53.686889-0500	Nexy	0000 Contact: 66B98153-BD62-4141-BD1F-DADC79D75A4F:ABPerson
default	20:42:53.686894-0500	Nexy	0000 Contact: FA38B842-F2F3-4FED-B33D-A5010D4304B0:ABPerson
default	20:42:53.686904-0500	Nexy	0000 Contact: 14743D61-F4A1-4392-9E1B-26918104BF14:ABPerson
default	20:42:53.686911-0500	Nexy	0000 Contact: B2D8BD53-113A-4BF0-91CA-D5DEB28674B5:ABPerson
default	20:42:53.686920-0500	Nexy	0000 Contact: 64B8389E-447B-4C35-B14E-8146CA91B47B:ABPerson
default	20:42:53.686925-0500	Nexy	0000 Contact: 3FF7B769-C140-4D4C-B32F-6B8F440DE2D8:ABPerson
default	20:42:53.686930-0500	Nexy	0000 Contact: 1F6916A9-1A84-48F4-B955-59E227D8C9DF:ABPerson
default	20:42:53.686943-0500	Nexy	0000 Contact: F334D708-4AFD-4933-99D2-F8F1D76176A9:ABPerson
default	20:42:53.686949-0500	Nexy	0000 Contact: 626EC525-A04F-4FBF-8FEE-BA93D0436808:ABPerson
default	20:42:53.686956-0500	Nexy	0000 Contact: A4D2F572-E7C4-45EE-AE51-345CC039C259:ABPerson
default	20:42:53.686968-0500	Nexy	0000 Contact: 014698F9-DA96-407C-A1B8-DEC6B51A33F6:ABPerson
default	20:42:53.686974-0500	Nexy	0000 Contact: F5B2550B-7B88-4DCE-A7A3-1B10271953FC:ABPerson
default	20:42:53.686984-0500	Nexy	0000 Contact: 1EAD0F34-5228-476C-B4EB-ACD91782DD85:ABPerson
default	20:42:53.686989-0500	Nexy	0000 Contact: F7E0D308-2E0A-49CC-849B-C883B6F8730F:ABPerson
default	20:42:53.686996-0500	Nexy	0000 Contact: 145A9F4B-B827-49A2-B108-81359AEE2B8F:ABPerson
default	20:42:53.687001-0500	Nexy	0000 Contact: 0AA46F26-7B70-4230-AC5B-AFDC6D2DD22B:ABPerson
default	20:42:53.687011-0500	Nexy	0000 Contact: AE79C4EC-990E-4BA3-913E-7C842EB653EF:ABPerson
default	20:42:53.687021-0500	Nexy	0000 Contact: C05B9998-16AE-4F34-8E4F-817C3D9B8EC6:ABPerson
default	20:42:53.687031-0500	Nexy	0000 Contact: 7F27B5B3-D0F5-483F-89C6-8B9931845E1F:ABPerson
default	20:42:53.687036-0500	Nexy	0000 Contact: 84E58627-BCB4-42D0-BDFA-EE699F5FBDD8:ABPerson
default	20:42:53.687041-0500	Nexy	0000 Contact: 2513C61B-7EFC-4A92-88AB-DF9479B99E6A:ABPerson
default	20:42:53.687047-0500	Nexy	0000 Contact: 84CFF237-6D8B-4620-9181-D1B4BB0809EE:ABPerson
default	20:42:53.687057-0500	Nexy	0000 Contact: 0BFD29DC-60C9-4B71-9D65-4ADA47472277:ABPerson
default	20:42:53.687066-0500	Nexy	0000 Contact: 69998C87-7B1A-45AA-ABB3-2D84128DD9EE:ABPerson
default	20:42:53.687072-0500	Nexy	0000 Contact: A7C3EEE8-11F8-4C0C-848D-3AC49C688578:ABPerson
default	20:42:53.687083-0500	Nexy	0000 Contact: A64A1E7E-C301-454E-A9A9-D685C82EF693:ABPerson
default	20:42:53.687088-0500	Nexy	0000 Contact: 91C379A3-DE9D-456A-A6AD-0F1F963582E7:ABPerson
default	20:42:53.687098-0500	Nexy	0000 Contact: 6ACE0F8B-171F-450C-83E2-081B5F26881E:ABPerson
default	20:42:53.687103-0500	Nexy	0000 Contact: AC074808-2D0D-48F8-8B23-3F0CA6D51D26:ABPerson
default	20:42:53.687115-0500	Nexy	0000 Contact: F4F5D7A0-BC90-4C27-BBCE-BE969384F1C0:ABPerson
default	20:42:53.687120-0500	Nexy	0000 Contact: 1ABDAACE-D0B1-4F9B-96D1-DC2C524CE1C6:ABPerson
default	20:42:53.687127-0500	Nexy	0000 Contact: 43585BE0-779A-4596-A518-8D5E4ADB3D19:ABPerson
default	20:42:53.687136-0500	Nexy	0000 Contact: 67051D02-C728-4665-B5FC-4F1B269F02BD:ABPerson
default	20:42:53.687141-0500	Nexy	0000 Contact: 4473A678-C9E7-4D62-84E0-753DF60913D1:ABPerson
default	20:42:53.687151-0500	Nexy	0000 Contact: D56AB0C8-7D93-4C12-B5B5-95E0DC8F2240:ABPerson
default	20:42:53.687156-0500	Nexy	0000 Contact: 9579BC4C-AF0F-4D50-A15C-319AACBFC2A5:ABPerson
default	20:42:53.687163-0500	Nexy	0000 Contact: 4BE75408-838B-4CDE-A088-588AE1E78C84:ABPerson
default	20:42:53.687171-0500	Nexy	0000 Contact: C87BCEEB-0D99-4BCD-B837-B1790FEF5A35:ABPerson
default	20:42:53.687180-0500	Nexy	0000 Contact: 11C070CC-DE86-43A2-AC2E-BD5D0E666C75:ABPerson
default	20:42:53.687185-0500	Nexy	0000 Contact: 1BC6C401-C80C-443B-86A1-DE142581F385:ABPerson
default	20:42:53.687196-0500	Nexy	0000 Contact: 0A5F3B64-AC92-4AC6-A80F-C08A85FC26AF:ABPerson
default	20:42:53.687201-0500	Nexy	0000 Contact: 87E03F74-07D8-4C64-9DA7-D99DC9CA7445:ABPerson
default	20:42:53.687211-0500	Nexy	0000 Contact: 94F55698-438B-4D8C-9CA0-71DDFD6367D5:ABPerson
default	20:42:53.687216-0500	Nexy	0000 Contact: 15748416-FFAD-4D4B-B4AF-076BF4C1B672:ABPerson
default	20:42:53.687226-0500	Nexy	0000 Contact: 74B3EEDB-C36E-4B91-AAF8-A7D433556574:ABPerson
default	20:42:53.687235-0500	Nexy	0000 Contact: 951A73EB-D920-4420-8258-81B51426DEF7:ABPerson
default	20:42:53.687244-0500	Nexy	0000 Contact: 6B194999-7994-412B-8F16-25AB9317AAB4:ABPerson
default	20:42:53.687249-0500	Nexy	0000 Contact: 2EC20223-DCBF-406A-9D39-5F1D770A8BC4:ABPerson
default	20:42:53.687258-0500	Nexy	0000 Contact: 1562F9E4-94A8-48AB-BF2B-C1EB0C1BE5A4:ABPerson
default	20:42:53.687266-0500	Nexy	0000 Contact: F6C3B173-427B-4C46-AA87-E8AA5B4E4C47:ABPerson
default	20:42:53.687278-0500	Nexy	0000 Contact: 5340250A-2C48-4FA9-9A43-1E9438F76204:ABPerson
default	20:42:53.687283-0500	Nexy	0000 Contact: 910FA8BF-611B-4C75-9EB0-5F2EFD716C1F:ABPerson
default	20:42:53.687293-0500	Nexy	0000 Contact: 08B0DE06-259B-449C-B66B-FFBA5AB8D812:ABPerson
default	20:42:53.687299-0500	Nexy	0000 Contact: 3C20B58D-2CA5-485E-A9A6-F77768532665:ABPerson
default	20:42:53.687305-0500	Nexy	0000 Contact: 6524FEA4-C209-419D-8A29-C534C9D1627C:ABPerson
default	20:42:53.687314-0500	Nexy	0000 Contact: 9A063C74-04C9-4AD8-AB36-6C8734D43E2D:ABPerson
default	20:42:53.687319-0500	Nexy	0000 Contact: AEAB4360-3F45-4F6B-9F79-B5D0B38B9A81:ABPerson
default	20:42:53.687328-0500	Nexy	0000 Contact: 044C1B1D-1FA6-46AA-B69A-444A8B442B7C:ABPerson
default	20:42:53.687335-0500	Nexy	0000 Contact: 67E45E85-4716-4AD1-9FE5-0DD5A68A6D7E:ABPerson
default	20:42:53.687344-0500	Nexy	0000 Contact: 4ADAEDF0-6C5E-4C06-9C0A-B8594FF82BDA:ABPerson
default	20:42:53.687350-0500	Nexy	0000 Contact: DA46038B-56C6-4414-9F21-077B66E8C91C:ABPerson
default	20:42:53.687359-0500	Nexy	0000 Contact: 75FADFA1-F7C3-437C-8B58-DAA8A4B54442:ABPerson
default	20:42:53.687365-0500	Nexy	0000 Contact: B6E3347E-7AC5-41E7-ACA5-D2CEF067A1CA:ABPerson
default	20:42:53.687375-0500	Nexy	0000 Contact: 4EFFE145-11B7-42A5-822C-A4BAB5D83906:ABPerson
default	20:42:53.687380-0500	Nexy	0000 Contact: EAB298D5-435C-4D40-83A7-2C55723A0BFD:ABPerson
default	20:42:53.687388-0500	Nexy	0000 Contact: B0D78C24-E588-4901-88A7-6B1BB429B840:ABPerson
default	20:42:53.687393-0500	Nexy	0000 Contact: 1CB20B90-D9D5-4C8F-9AB0-DAA44D00BDD4:ABPerson
default	20:42:53.687402-0500	Nexy	0000 Contact: 527699A5-81B2-4D67-AEED-D6EED43F9044:ABPerson
default	20:42:53.687410-0500	Nexy	0000 Contact: CB5E53D4-5C8B-43F5-94AF-6B7D8BA543FD:ABPerson
default	20:42:53.687418-0500	Nexy	0000 Contact: 04598613-6173-4B93-B8E7-285BC4F3D8E8:ABPerson
default	20:42:53.687429-0500	Nexy	0000 Contact: ADD86E64-7CF0-4510-AD39-66BD6BD079BC:ABPerson
default	20:42:53.687436-0500	Nexy	0000 Contact: 32788248-0C60-4FEA-85E7-FA758B61DD1D:ABPerson
default	20:42:53.687439-0500	Nexy	0000 Contact: AA1A4C67-F155-4EE5-9010-31149EE1E39C:ABPerson
default	20:42:53.687452-0500	Nexy	0000 Contact: 961DCC0E-AAAD-4D01-9678-0A7621D2AFB0:ABPerson
default	20:42:53.687457-0500	Nexy	0000 Contact: 66B11FA1-1DE3-48ED-A067-665E7467482A:ABPerson
default	20:42:53.687467-0500	Nexy	0000 Contact: F5182AF8-32D2-40E6-993D-C0489EBC89E4:ABPerson
default	20:42:53.687473-0500	Nexy	0000 Contact: 0D60E67B-3CE2-4AA5-A3A7-78022070A092:ABPerson
default	20:42:53.687482-0500	Nexy	0000 Contact: 3AAC52F8-BF6B-4AF2-BB6D-03A1310B24E5:ABPerson
default	20:42:53.687491-0500	Nexy	0000 Contact: CE41D8E9-94C5-4D35-9B34-26811B12C410:ABPerson
default	20:42:53.687496-0500	Nexy	0000 Contact: F13294CA-A587-43D6-B693-775C43EE2187:ABPerson
default	20:42:53.687509-0500	Nexy	0000 Contact: 89FE41AC-035D-4508-9B13-A7A61A86A77D:ABPerson
default	20:42:53.687514-0500	Nexy	0000 Contact: 31E21B40-260C-42C1-9677-7C97CC1B201D:ABPerson
default	20:42:53.687519-0500	Nexy	0000 Contact: F0D80C37-667F-495B-83CE-9F5BF918C730:ABPerson
default	20:42:53.687527-0500	Nexy	0000 Contact: 06259E4E-E4B7-4654-BF6B-33F4F0FCB23A:ABPerson
default	20:42:53.687537-0500	Nexy	0000 Contact: 55FDAC9D-D436-4535-BE96-A71F62A0AF9E:ABPerson
default	20:42:53.687542-0500	Nexy	0000 Contact: F790FA9D-7B36-4AEA-8012-0BDEED54CF62:ABPerson
default	20:42:53.687551-0500	Nexy	0000 Contact: 276E4846-224E-4119-AB43-FE2E963D133E:ABPerson
default	20:42:53.687556-0500	Nexy	0000 Contact: DB25F4B4-E218-42CD-959A-C88098B61FD4:ABPerson
default	20:42:53.687566-0500	Nexy	0000 Contact: 7E8FC80C-607C-43E2-BF92-C5FCC8403326:ABPerson
default	20:42:53.687576-0500	Nexy	0000 Contact: 6BE779B6-7D7F-4DB2-A36A-3696730156FE:ABPerson
default	20:42:53.687581-0500	Nexy	0000 Contact: A45B54DD-B6FC-4653-84D5-0757EB2F2ED6:ABPerson
default	20:42:53.687589-0500	Nexy	0000 Contact: 8605C2C8-7153-4112-9036-FAA472B7FD44:ABPerson
default	20:42:53.687594-0500	Nexy	0000 Contact: CD272F42-E884-45F1-84C3-CFD3A0B1BF35:ABPerson
default	20:42:53.687603-0500	Nexy	0000 Contact: 4D2116D6-A645-48BB-B220-E9ED03C71748:ABPerson
default	20:42:53.687613-0500	Nexy	0000 Contact: B502B3DD-9E9D-4150-B4A9-4872364793EF:ABPerson
default	20:42:53.687618-0500	Nexy	0000 Contact: 0C360F68-EDE2-457E-AC4B-ACE762AD5BD0:ABPerson
default	20:42:53.687625-0500	Nexy	0000 Contact: FF4175C6-26DF-47BC-BF00-2E75EEE8B1FD:ABPerson
default	20:42:53.687632-0500	Nexy	0000 Contact: 09A457F3-A9F4-4F24-9B11-9FA58D4C1508:ABPerson
default	20:42:53.687638-0500	Nexy	0000 Contact: B89DEF47-D413-46AD-BAEA-7D496DD46FB1:ABPerson
default	20:42:53.687650-0500	Nexy	0000 Contact: 3598E3CB-8A76-4D70-AC49-D3EB37CA2029:ABPerson
default	20:42:53.687654-0500	Nexy	0000 Contact: AA991FC9-EB3D-43B4-8CBD-8E604A09B637:ABPerson
default	20:42:53.687664-0500	Nexy	0000 Contact: CC5195D6-422A-4FB7-B9EE-A2A04E601EC0:ABPerson
default	20:42:53.687674-0500	Nexy	0000 Contact: B569062E-A03D-4DD9-A53C-5D2D8D57CB4B:ABPerson
default	20:42:53.687680-0500	Nexy	0000 Contact: 73B6BD20-2014-4F01-90D9-4428F13B690A:ABPerson
default	20:42:53.687690-0500	Nexy	0000 Contact: AA3A3E50-90A8-4525-8DAA-B8B4FADD18DA:ABPerson
default	20:42:53.687695-0500	Nexy	0000 Contact: 3BAE7091-1579-47D0-B90D-0D3CF681C569:ABPerson
default	20:42:53.687704-0500	Nexy	0000 Contact: 56A226DF-9ECE-4143-BA65-8AD0B646C7CB:ABPerson
default	20:42:53.687707-0500	Nexy	0000 Contact: 50F1ED96-0C6B-4F81-AA14-43DC6EBECD59:ABPerson
default	20:42:53.687716-0500	Nexy	0000 Contact: 5A494BDA-3B74-4B7B-92A5-ADDBE7FB8C87:ABPerson
default	20:42:53.687726-0500	Nexy	0000 Contact: 6BD609FD-5007-4D59-A4EF-493CADDB85B2:ABPerson
default	20:42:53.687731-0500	Nexy	0000 Contact: 7E64D4B3-BC6D-4959-B7A0-E823B049142C:ABPerson
default	20:42:53.687740-0500	Nexy	0000 Contact: 621AF0D1-3352-4F82-9C69-D6B0F8D4F5A9:ABPerson
default	20:42:53.687745-0500	Nexy	0000 Contact: 4E051A3F-F33F-42F6-A635-4F6B6FEFCFB2:ABPerson
default	20:42:53.687753-0500	Nexy	0000 Contact: 30F7C290-B84E-45EF-8777-D14EBB9D4BB1:ABPerson
default	20:42:53.687760-0500	Nexy	0000 Contact: B489EA28-72B0-4D87-8E65-2FCC5266CCBB:ABPerson
default	20:42:53.687769-0500	Nexy	0000 Contact: E5C00A28-C49D-4782-B544-D726CFE29EF0:ABPerson
default	20:42:53.687777-0500	Nexy	0000 Contact: DA65C871-7E16-4359-B34C-C5906692C623:ABPerson
default	20:42:53.687783-0500	Nexy	0000 Contact: 5BAFBA23-8FAE-41B7-86D6-A6B3DB070404:ABPerson
default	20:42:53.687792-0500	Nexy	0000 Contact: EA0D316B-758E-4C59-B0A6-6FFB7AD3E09F:ABPerson
default	20:42:53.687800-0500	Nexy	0000 Contact: 9BD347CB-8966-4118-92F7-D6D42F5F8C7C:ABPerson
default	20:42:53.687805-0500	Nexy	0000 Contact: 018F45A5-C534-4FC0-871A-DB5567A8D78E:ABPerson
default	20:42:53.687814-0500	Nexy	0000 Contact: 9FC18618-FB9D-4960-8474-07F6A0D062F8:ABPerson
default	20:42:53.687819-0500	Nexy	0000 Contact: C8BDDDAE-C009-4DB9-B3FC-01F3B16C6D25:ABPerson
default	20:42:53.687829-0500	Nexy	0000 Contact: 1D0198ED-A6C3-4B64-AA1A-2E8A8C4A0172:ABPerson
default	20:42:53.687839-0500	Nexy	0000 Contact: 3BD67570-1034-422C-85A2-6F28BE24C33A:ABPerson
default	20:42:53.687846-0500	Nexy	0000 Contact: D75A5B27-BD0C-4D34-AC6B-FC2822769519:ABPerson
default	20:42:53.687853-0500	Nexy	0000 Contact: 6B5F7DDD-1E04-453D-8539-4B54A251117A:ABPerson
default	20:42:53.687864-0500	Nexy	0000 Contact: 49E369CD-B10E-4CD5-B030-5393AB2ADE18:ABPerson
default	20:42:53.687874-0500	Nexy	0000 Contact: A9AB0613-621A-427C-9150-83893BA072C5:ABPerson
default	20:42:53.687882-0500	Nexy	0000 Contact: 9B8281D5-C780-436F-988A-96C01722B038:ABPerson
default	20:42:53.687899-0500	Nexy	0000 FINISH (22.2 ms)
default	20:42:53.718595-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:42:53.718729-0500	runningboardd	Invalidating assertion 402-625-5550 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	20:42:53.820030-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.820045-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.820058-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.820077-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.822664-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.823285-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.823386-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.985097-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5428] from originator [osservice<com.apple.WindowServer(88)>:395] with description <RBSAssertionDescriptor| "AppDrawing" ID:402-395-5558 target:5428 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:42:53.985263-0500	runningboardd	Assertion 402-395-5558 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5428]) will be created as active
default	20:42:53.985914-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring jetsam update because this process is not memory-managed
default	20:42:53.985935-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring suspend because this process is not lifecycle managed
default	20:42:53.985955-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring GPU update because this process is not GPU managed
default	20:42:53.985991-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] Ignoring memory limit update because this process is not memory-managed
default	20:42:53.990463-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:53.991045-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:53.991270-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:54.321759-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x81081 (Nexy) connectionID: F9617 pid: 5428 in session 0x101
default	20:42:54.321846-0500	WindowServer	<BSCompoundAssertion:0x9a3011580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x81081 (Nexy) acq:0x9a2243940 count:1
default	20:42:54.323045-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4005","name":"Nexy(5428)"}, "details":null }
default	20:42:54.323127-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4005 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":5428})
default	20:42:54.323137-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":5428})
default	20:42:54.323281-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Workspace connection invalidated.
default	20:42:54.323308-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Now flagged as pending exit for reason: workspace client connection invalidated
default	20:42:54.323627-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:42:54.323719-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 6, PID = 5428, Name = sid:0x1f4005, Nexy(5428), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:42:54.323281-0500	WindowManager	Connection invalidated | (5428) Nexy
default	20:42:54.323803-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.324137-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.324212-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.324085-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.324230-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.324359-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:42:54.330317-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x81081 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x81081 (Nexy)"
)}
default	20:42:54.331573-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1534 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x81081 (Nexy)"
)}
default	20:42:54.339025-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:42:54.339243-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:42:54.342705-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.347295-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:42:54.347315-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_447.388.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:42:54.357063-0500	mDNSResponder	[R76803] DNSServiceCreateConnection STOP PID[5428](Nexy)
default	20:42:54.360223-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5428] termination reported by launchd (0, 0, 0)
default	20:42:54.360261-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.360605-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.360780-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.360821-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.369770-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: none (role: NonUserInteractive) (endowments: (null))
default	20:42:54.370227-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Process exited: <RBSProcessExitContext| voluntary>.
default	20:42:54.370250-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Setting process task state to: Not Running
default	20:42:54.370263-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Setting process visibility to: Unknown
default	20:42:54.370170-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: none (role: NonUserInteractive) (endowments: (null))
default	20:42:54.370296-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5428] Invalidating workspace.
default	20:42:54.370347-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.370445-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 5428, name = Nexy
default	20:42:54.370929-0500	ControlCenter	Removing: <FBApplicationProcess: 0xbdeadcc00; app<application.com.nexy.assistant.54170280.54170289>:5428(v2B732)>
default	20:42:54.371221-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, none-NotVisible
default	20:42:54.371522-0500	ControlCenter	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, none-NotVisible
default	20:42:54.373253-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-5428)
default	20:42:54.374656-0500	launchservicesd	Hit the server for a process handle bd8c46400001534 that resolved to: [app<application.com.nexy.assistant.54170280.54170289(501)>:5428]
default	20:42:54.375098-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(319A1415) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-5428)
default	20:42:54.375178-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(319A1415, (bid:com.nexy.assistant-Item-0-5428))]
default	20:42:54.377433-0500	gamepolicyd	Received state update for 5428 (app<application.com.nexy.assistant.54170280.54170289(501)>, none-NotVisible
default	20:42:54.387923-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x81081} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:42:54.387959-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9ad572940: Nexy> state 3
default	20:42:54.387980-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:42:54.389045-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9ad572940: Nexy> state 4
default	20:42:54.389055-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:42:55.526912-0500	runningboardd	Invalidating assertion 402-625-5547 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) from originator [osservice<com.apple.controlcenter(501)>:625]
default	20:42:55.628624-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:42:55.635812-0500	gamepolicyd	Received state update for -1 (app<application.com.nexy.assistant.54170280.54170289(501)>, none-NotVisible
default	20:42:57.449934-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	20:42:57.537754-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:42:57.537926-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:42:57.540368-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:42:57.550077-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:42:57.551418-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54170280.54170289(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:42:57.551491-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54170280.54170289(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:580] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:402-580-5562 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:42:57.551565-0500	runningboardd	Assertion 402-580-5562 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) will be created as active
default	20:42:57.554548-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:42:57.554585-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:42:57.554603-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:42:57.554668-0500	runningboardd	app<application.com.nexy.assistant.54170280.54170289(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:42:57.566250-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] is not RunningBoard jetsam managed.
default	20:42:57.566262-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] This process will not be managed.
default	20:42:57.566276-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:42:57.566457-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:57.567048-0500	gamepolicyd	Hit the server for a process handle 1a048945000015e5 that resolved to: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:42:57.567085-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:57.569485-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:42:57.569546-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:402-402-5563 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:42:57.569669-0500	runningboardd	Assertion 402-402-5563 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:42:57.569860-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:42:57.569881-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:42:57.569907-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Set darwin role to: UserInteractive
default	20:42:57.569925-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:42:57.569955-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:42:57.569983-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] reported to RB as running
default	20:42:57.571475-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:5605" ID:402-365-5564 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:42:57.571615-0500	CoreServicesUIAgent	LAUNCH: 0x0-0xad0ad com.nexy.assistant starting stopped process.
default	20:42:57.571553-0500	runningboardd	Assertion 402-365-5564 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:42:57.572669-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:42:57.572833-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9ad7c00a0: Nexy> state 2
default	20:42:57.572854-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:42:57.572930-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:42:57.572997-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:42:57.573055-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:42:57.573133-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:42:57.573242-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:42:57.574268-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:57.574621-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:42:57.574723-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:57.574666-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:42:57.574584-0500	runningboardd	Invalidating assertion 402-580-5562 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:580]
default	20:42:57.574700-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:42:57.574764-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:42:57.577186-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:57.586483-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:57.623332-0500	logger	detected new pid 5605 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:57.655818-0500	Nexy	[0x1028bca60] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:42:57.655888-0500	Nexy	[0x1028bcfa0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:42:57.678837-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:42:57.678849-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:42:57.678860-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:42:57.678879-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:42:57.679047-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:42:57.681430-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:42:57.681770-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
error	20:42:57.769423-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x857558000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:42:57.769673-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x857558000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:42:57.769891-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x857558000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:42:57.770100-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x857558000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:42:57.771394-0500	Nexy	[0x1028c88c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:42:57.772172-0500	Nexy	[0x85663c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:42:57.772478-0500	Nexy	[0x85663c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:42:57.772840-0500	Nexy	[0x85663c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:42:57.773742-0500	Nexy	Received configuration update from daemon (initial)
default	20:42:57.774966-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:42:57.775309-0500	Nexy	[0x85663c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:42:57.776026-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5605.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:42:57.777636-0500	tccd	AUTHREQ_SUBJECT: msgID=5605.1, subject=com.nexy.assistant,
default	20:42:57.778347-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:57.797827-0500	Nexy	[0x85663c3c0] invalidated after the last release of the connection object
default	20:42:57.798151-0500	Nexy	server port 0x0000310b, session port 0x0000310b
default	20:42:57.799138-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.343, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:42:57.799170-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:42:57.800087-0500	tccd	AUTHREQ_SUBJECT: msgID=395.343, subject=com.nexy.assistant,
default	20:42:57.800761-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:42:57.827342-0500	Nexy	New connection 0xc387b main
default	20:42:57.830281-0500	Nexy	CHECKIN: pid=5605
default	20:42:57.840200-0500	Nexy	CHECKEDIN: pid=5605 asn=0x0-0xad0ad foreground=0
default	20:42:57.840379-0500	runningboardd	Invalidating assertion 402-365-5564 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.coreservices.launchservicesd>:365]
default	20:42:57.840061-0500	launchservicesd	CHECKIN:0x0-0xad0ad 5605 com.nexy.assistant
default	20:42:57.843836-0500	WindowServer	c387b[CreateApplication]: Process creation: 0x0-0xad0ad (Nexy) connectionID: C387B pid: 5605 in session 0x101
default	20:42:57.844379-0500	Nexy	[0x85663c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:42:57.848027-0500	Nexy	BringFrontModifier: pid=5605 asn=0x0-0xad0ad Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:42:57.848769-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:42:57.852628-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:42:57.856936-0500	Nexy	Handshake succeeded
default	20:42:57.856952-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:42:57.857440-0500	Nexy	[0x85663c3c0] Connection returned listener port: 0x5003
default	20:42:57.861506-0500	Nexy	[0x85663c3c0] Connection returned listener port: 0x5003
default	20:42:57.865488-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:42:57.865541-0500	Nexy	[0x85663c780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:42:57.865652-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:42:58.834985-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A19E9ED5-100E-4083-B7DE-482B92EFD72C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52555,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc6ca3f79 tp_proto=0x06"
default	20:42:58.835104-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52555<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391908 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x95201f49
default	20:43:03.539565-0500	runningboardd	Assertion did invalidate due to timeout: 402-402-5563 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605])
default	20:43:03.689573-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:03.689598-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:03.689620-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:03.689656-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:03.694252-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:03.694947-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:03.836114-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52555<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391908 t_state: SYN_SENT process: Nexy:5605 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x95201f49
default	20:43:03.836138-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52555<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391908 t_state: SYN_SENT process: Nexy:5605 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:43:03.836672-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E07C7383-359D-4A86-9B04-669DED4D87B3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52558,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xacfd108c tp_proto=0x06"
default	20:43:03.836796-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52558<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391932 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb16c9a58
default	20:43:08.231987-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:43:08.836791-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52558<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391932 t_state: SYN_SENT process: Nexy:5605 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb16c9a58
default	20:43:08.836819-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52558<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391932 t_state: SYN_SENT process: Nexy:5605 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:43:08.841285-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:43:08.841527-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:43:08.843003-0500	Nexy	nw_path_libinfo_path_check [9C2D6CFB-6030-4A67-B4D6-3E5761AF9F98 Hostname#72448d89:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:43:08.843750-0500	mDNSResponder	[R77072] DNSServiceCreateConnection START PID[5605](Nexy)
default	20:43:08.843909-0500	mDNSResponder	[R77073] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: f92d5498
default	20:43:08.844779-0500	mDNSResponder	[R77074] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: f92d5498
default	20:43:08.846401-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EC461BBE-5813-479D-A893-51B5CBF80BC9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52561,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb54efdba tp_proto=0x06"
default	20:43:08.846543-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52561<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391967 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 3 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc374af7
default	20:43:08.859760-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:43:13.837949-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:52561<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391967 t_state: SYN_SENT process: Nexy:5605 Duration: 4.992 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 3 ms so_error: 0 svc/tc: 0 flow: 0xbc374af7
default	20:43:13.837985-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52561<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 391967 t_state: SYN_SENT process: Nexy:5605 flowctl: 0us (0x) SYN in/out: 0/11 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:43:14.899899-0500	Nexy	[0x85663cdc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:43:14.900461-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5605.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:43:14.901551-0500	tccd	AUTHREQ_SUBJECT: msgID=5605.2, subject=com.nexy.assistant,
default	20:43:14.902196-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:43:14.923429-0500	Nexy	[0x85663cdc0] invalidated after the last release of the connection object
default	20:43:14.923569-0500	Nexy	server port 0x00002113, session port 0x0000310b
default	20:43:14.924302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.344, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:43:14.924326-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:14.925178-0500	tccd	AUTHREQ_SUBJECT: msgID=395.344, subject=com.nexy.assistant,
default	20:43:14.926126-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	20:43:14.957803-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:43:14.958427-0500	Nexy	[0x85663cf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:43:14.959161-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"PID":5605,"session_type":"Primary"} }
default	20:43:14.959233-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5605}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4006, sessionType: 'prim', isRecording: false }, 
]
default	20:43:14.959827-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 5605, name = Nexy
default	20:43:14.960118-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x85772c740 with ID: 0x1f4006
default	20:43:14.960335-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:43:14.961070-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:43:14.962263-0500	Nexy	[0x85663d040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:43:14.964438-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
default	20:43:14.967391-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:43:14.968858-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:43:14.969000-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:43:14.969125-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:43:14.969136-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:43:14.969166-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:43:14.969274-0500	Nexy	[0x85663d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:14.969372-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:43:14.969721-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5605.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:43:14.975698-0500	tccd	AUTHREQ_SUBJECT: msgID=5605.3, subject=com.nexy.assistant,
default	20:43:14.976386-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:14.993180-0500	Nexy	[0x85663d180] invalidated after the last release of the connection object
default	20:43:14.993354-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:43:14.993390-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:43:14.993654-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:43:14.994796-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.101, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:14.995795-0500	tccd	AUTHREQ_SUBJECT: msgID=406.101, subject=com.nexy.assistant,
default	20:43:14.996391-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:15.016170-0500	tccd	AUTHREQ_SUBJECT: msgID=406.103, subject=com.nexy.assistant,
default	20:43:15.016714-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:15.030055-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:43:15.030071-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8588eb500> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:43:15.043595-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:43:15.043605-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:43:15.046113-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:15.046236-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:15.051110-0500	Nexy	[0x85663d180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:43:15.051412-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=24073291694081 }
default	20:43:15.051485-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	20:43:15.051528-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	20:43:15.051558-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	20:43:15.059710-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:15.059876-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:15.074511-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	20:43:15.074528-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:43:15.078607-0500	Nexy	[0x85663d2c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:43:15.091365-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:43:15.091409-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:43:15.091547-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x854784a20, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:43:15.091572-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:15.096889-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:15.096846-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	20:43:15.097589-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x854786070, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:43:15.097600-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x854786070: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:15.097605-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:43:15.097609-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:15.097613-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:43:15.097637-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:43:15.098372-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x854786070, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:43:15.098382-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x854786070: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:15.098387-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:15.098387-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:43:15.098397-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:43:15.098402-0500	Nexy	AudioConverter -> 0x854786070: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:43:15.098558-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x854786070: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:15.101773-0500	mDNSResponder	[R77090] DNSServiceQueryRecord START -- qname: <mask.hash: 'Msnutn5+cka0lGHzy+ILEw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: 2d50b096
default	20:43:15.120076-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 116AFF89-1BFD-46A7-ABBD-ADFFD54ED9CC flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52573,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xdbeab804 tp_proto=0x06"
default	20:43:15.120125-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52573<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 392111 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x83820b94
default	20:43:15.132914-0500	kernel	tcp connected: [<IPv4-redacted>:52573<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 392111 t_state: ESTABLISHED process: Nexy:5605 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x83820b94
default	20:43:15.241621-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 5621: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 38b90200 };
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
default	20:43:15.251909-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:15.262511-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:43:15.278582-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	20:43:15.530731-0500	Nexy	[0x85663d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:43:15.531564-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5605.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:43:15.540446-0500	tccd	AUTHREQ_SUBJECT: msgID=5605.4, subject=com.nexy.assistant,
default	20:43:15.541202-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:15.561559-0500	Nexy	[0x85663d680] invalidated after the last release of the connection object
default	20:43:15.561903-0500	Nexy	[0x85663d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:43:15.562566-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5605.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:43:15.563570-0500	tccd	AUTHREQ_SUBJECT: msgID=5605.5, subject=com.nexy.assistant,
default	20:43:15.564287-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:15.582526-0500	Nexy	[0x85663d680] invalidated after the last release of the connection object
default	20:43:15.582621-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:43:15.583111-0500	Nexy	[0x85663d680] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:43:15.583260-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:43:15.583349-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:43:15.585474-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:43:15.585503-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:15.586422-0500	tccd	AUTHREQ_SUBJECT: msgID=94711.3, subject=com.nexy.assistant,
default	20:43:15.587078-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:15.618048-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.350, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:43:15.618073-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:15.619057-0500	tccd	AUTHREQ_SUBJECT: msgID=395.350, subject=com.nexy.assistant,
default	20:43:15.619761-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:15.680577-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	20:43:15.707165-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
fault	20:43:15.710269-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54170280.54170289 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54170280.54170289>
default	20:43:15.731527-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:15.731673-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:15.731738-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:15.958270-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:43:15.960622-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x857724640: start, was running 0
default	20:43:15.961983-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5589 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:15.962049-0500	runningboardd	Assertion 402-336-5589 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:15.962296-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:15.962307-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:15.962316-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:15.962335-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:15.965131-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:15.965553-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.184161-0500	Nexy	[0x85663da40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:43:16.197118-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:43:16.199419-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 5605
default	20:43:16.212330-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x8575486e0
 (
    "<NSDarkAquaAppearance: 0x857548500>",
    "<NSSystemAppearance: 0x857548780>"
)>
default	20:43:16.217503-0500	Nexy	[0x85663df40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:43:16.218601-0500	Nexy	[0x85663e080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:43:16.221664-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:43:16.221985-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:43:16.221993-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:43:16.222029-0500	Nexy	[0x85663e1c0] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:43:16.222047-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:43:16.222124-0500	Nexy	[0x85663e300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:16.222207-0500	Nexy	FBSWorkspace registering source: <private>
default	20:43:16.222966-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:43:16.223089-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:43:16.223706-0500	Nexy	<FBSWorkspaceScenesClient:0x858dc52c0 <private>> attempting immediate handshake from activate
default	20:43:16.223761-0500	Nexy	<FBSWorkspaceScenesClient:0x858dc52c0 <private>> sent handshake
default	20:43:16.223850-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.223867-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:43:16.223882-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.223979-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Registering event dispatcher at init
default	20:43:16.224057-0500	ControlCenter	Created <FBWorkspace: 0xbdc9ea300; <FBApplicationProcess: 0xbdeadcd80; app<application.com.nexy.assistant.54170280.54170289>:5605(v2B91A)>>
default	20:43:16.224090-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54170280.54170289> with intent background
default	20:43:16.224569-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54170280.54170289(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:43:16.224514-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:43:16.224744-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54170280.54170289(501)> from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-5590 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:43:16.224935-0500	runningboardd	Assertion 402-625-5590 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) will be created as active
default	20:43:16.224967-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-5590 target:app<application.com.nexy.assistant.54170280.54170289(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.225373-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.225392-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.225404-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.226351-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:43:16.226931-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.227725-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:43:16.228383-0500	Nexy	Requesting scene <FBSScene: 0x858dc5720; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D> from com.apple.controlcenter.statusitems
default	20:43:16.228770-0500	Nexy	Request for <FBSScene: 0x858dc5720; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D> complete!
default	20:43:16.228869-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:43:16.230618-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:43:16.231003-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:43:16.231280-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:43:16.231317-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:43:16.231718-0500	Nexy	Requesting scene <FBSScene: 0x858dc57c0; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:43:16.231762-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.231942-0500	Nexy	Request for <FBSScene: 0x858dc57c0; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView> complete!
default	20:43:16.232827-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Bootstrap success!
default	20:43:16.233237-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.233340-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Setting process visibility to: Background
default	20:43:16.233416-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:43:16.233767-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:402-625-5591 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:43:16.233853-0500	runningboardd	Assertion 402-625-5591 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:16.234014-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.234035-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:43:16.234253-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.234266-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.234558-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.234705-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.237596-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.238117-0500	ControlCenter	Adding: <FBApplicationProcess: 0xbdeadcd80; app<application.com.nexy.assistant.54170280.54170289>:5605(v2B91A)>
default	20:43:16.238281-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.238300-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:43:16.238359-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.238398-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:43:16.238676-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Connection established.
default	20:43:16.238732-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.238759-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xbdc9b8690>
default	20:43:16.238810-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Connection to remote process established!
default	20:43:16.244191-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.244220-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdeadcd80; app<application.com.nexy.assistant.54170280.54170289>:5605(v2B91A)>
default	20:43:16.244364-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Registered new scene: <FBWorkspaceScene: 0xbde3d1f80; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D> (fromRemnant = 0)
default	20:43:16.244415-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Workspace interruption policy did change: reconnect
default	20:43:16.244637-0500	ControlCenter	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Client process connected: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.244652-0500	Nexy	Request for <FBSScene: 0x858dc5720; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D> complete!
default	20:43:16.244847-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:402-625-5592 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:43:16.244959-0500	runningboardd	Assertion 402-625-5592 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as inactive as originator process has not exited
default	20:43:16.245374-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-5593 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:43:16.245495-0500	runningboardd	Assertion 402-625-5593 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:16.245501-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.245526-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdeadcd80; app<application.com.nexy.assistant.54170280.54170289>:5605(v2B91A)>
default	20:43:16.245583-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:43:16.245598-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Registered new scene: <FBWorkspaceScene: 0xbde3d2a00; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:43:16.245757-0500	Nexy	Request for <FBSScene: 0x858dc57c0; com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView> complete!
default	20:43:16.245841-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.245879-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.245912-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.245759-0500	ControlCenter	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:16.245973-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.246320-0500	Nexy	<FBSWorkspaceScenesClient:0x858dc52c0 <private>> Reconnecting scene com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D
default	20:43:16.246656-0500	Nexy	<FBSWorkspaceScenesClient:0x858dc52c0 <private>> Reconnecting scene com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView
default	20:43:16.247250-0500	Nexy	Registering for test daemon availability notify post.
default	20:43:16.247478-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:43:16.247651-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:43:16.247755-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:43:16.248544-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.249305-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.249706-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.249855-0500	Nexy	[0x85663e6c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:43:16.254100-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:16.257220-0500	Nexy	[0x85663c3c0] Connection returned listener port: 0x5003
default	20:43:16.257805-0500	Nexy	SignalReady: pid=5605 asn=0x0-0xad0ad
default	20:43:16.258342-0500	Nexy	SIGNAL: pid=5605 asn=0x0x-0xad0ad
default	20:43:16.259289-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:43:16.270128-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.273473-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.276376-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:43:16.276396-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:43:16.276426-0500	Nexy	[0x85663d540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:43:16.276504-0500	Nexy	[0x85663d540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:16.277746-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:43:16.282262-0500	Nexy	[C:2] Alloc <private>
default	20:43:16.282290-0500	Nexy	[0x85663d540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:16.282833-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-5605). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:43:16.284003-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5594 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:16.283634-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-5605)
default	20:43:16.284060-0500	runningboardd	Assertion 402-5605-5594 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:16.283734-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(FB029A24, (bid:com.nexy.assistant-Item-0-5605)) for (bid:com.nexy.assistant-Item-0-5605)
default	20:43:16.284281-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-5605)]
default	20:43:16.284806-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.284362-0500	ControlCenter	Created instance DisplayableId(9B810260) in .menuBar for DisplayableAppStatusItemType(FB029A24, (bid:com.nexy.assistant-Item-0-5605)) .menuBar
default	20:43:16.284884-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.284986-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.285196-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.291783-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:43:16.293019-0500	ControlCenter	Created ephemaral instance DisplayableId(9B810260) for (bid:com.nexy.assistant-Item-0-5605) with positioning .ephemeral
default	20:43:16.293693-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:43:16.294344-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	20:43:16.294521-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.284045-0500	WindowManager	Connection activated | (5605) Nexy
default	20:43:16.296812-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:16.299436-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.300126-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.299976-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.341164-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:43:16.341779-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:43:16.341850-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:43:16.341895-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:16.341929-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4006, Nexy(5605), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:43:16.341964-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.341969-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:43:16.341983-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 7 starting playing
default	20:43:16.342042-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:16.342071-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:43:16.342093-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:16.342087-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.342113-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:43:16.342129-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.342159-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:43:16.342174-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f4006 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5605}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4006, sessionType: 'prim', isRecording: false }, 
]
default	20:43:16.342242-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:43:16.342253-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:43:16.342334-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:16.343051-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.343127-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.343149-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:16.343161-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:43:16.343168-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:43:16.343175-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	20:43:16.343220-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:43:16.392776-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:43:16.395443-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:43:16.396127-0500	Nexy	[GMS] availability notification token 90
default	20:43:16.501718-0500	ControlCenter	[app<application.com.nexy.assistant.54170280.54170289>:5605] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:43:16.501946-0500	runningboardd	Invalidating assertion 402-625-5593 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	20:43:16.609416-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.609428-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.609437-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.609457-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.611783-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.612406-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.612607-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.784179-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.WindowServer(88)>:395] with description <RBSAssertionDescriptor| "AppDrawing" ID:402-395-5596 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:16.784323-0500	runningboardd	Assertion 402-395-5596 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:16.784954-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:16.784970-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:16.784984-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:16.785012-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:16.788544-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:16.789104-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:16.789340-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:17.295312-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46d00 at /Applications/Nexy.app
default	20:43:17.302273-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	20:43:17.305354-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:43:17.426537-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:18.327577-0500	runningboardd	Invalidating assertion 402-625-5590 (target:app<application.com.nexy.assistant.54170280.54170289(501)>) from originator [osservice<com.apple.controlcenter(501)>:625]
default	20:43:18.429999-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54170280.54170289(501)>
default	20:43:18.431205-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:18.431231-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:18.431251-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:18.431283-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:18.435144-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:18.441145-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:18.442136-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:20.446194-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:21.200809-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:43:21.237261-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.353, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:43:21.237325-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:21.239511-0500	tccd	AUTHREQ_SUBJECT: msgID=395.353, subject=com.nexy.assistant,
default	20:43:21.240783-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:22.070560-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x858d88740) Selecting device 85 from constructor
default	20:43:22.070570-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:22.070576-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:22.070580-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x858d88740) nothing to teardown
default	20:43:22.070585-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x858d88740) connecting device 85
default	20:43:22.070662-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x858d88740) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:22.070892-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x858d88740) created ioproc 0xb for device 85
default	20:43:22.071028-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 7 device listeners to device 85
default	20:43:22.071182-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 85
default	20:43:22.071191-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x858d88740)
default	20:43:22.071252-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:22.071259-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:22.071265-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:22.071274-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:22.071280-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:22.071362-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:22.071372-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:22.071377-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:22.071379-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device listeners from device 0
default	20:43:22.071384-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 0
default	20:43:22.071388-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:22.071405-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:43:22.071449-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x858d88740) caller requesting device change from 85 to 91
default	20:43:22.071456-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:22.071460-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:22.071465-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x858d88740) disconnecting device 85
default	20:43:22.071475-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x858d88740) destroying ioproc 0xb for device 85
default	20:43:22.071497-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:43:22.071728-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:43:22.072082-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x858d88740) connecting device 91
default	20:43:22.072156-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x858d88740) Device ID: 91 (Input:Yes | Output:No): true
default	20:43:22.073627-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.104, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.075098-0500	tccd	AUTHREQ_SUBJECT: msgID=406.104, subject=com.nexy.assistant,
default	20:43:22.075802-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.086594-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:43:22.086635-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:43:22.088093-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:43:22.088124-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:22.089107-0500	tccd	AUTHREQ_SUBJECT: msgID=94711.4, subject=com.nexy.assistant,
default	20:43:22.089863-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:22.093869-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x858d88740) created ioproc 0xa for device 91
default	20:43:22.093986-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 7 device listeners to device 91
default	20:43:22.094135-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 91
default	20:43:22.094141-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x858d88740)
default	20:43:22.094150-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:43:22.094158-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:22.094263-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:43:22.094269-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:43:22.094274-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:43:22.094368-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:22.094377-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:22.094383-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:22.094388-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 7 device listeners from device 85
default	20:43:22.094512-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 85
default	20:43:22.094520-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:22.095067-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:43:22.096035-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.105, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.097006-0500	tccd	AUTHREQ_SUBJECT: msgID=406.105, subject=com.nexy.assistant,
default	20:43:22.097590-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.113533-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:43:22.114381-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.106, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.115288-0500	tccd	AUTHREQ_SUBJECT: msgID=406.106, subject=com.nexy.assistant,
default	20:43:22.115364-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.356, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:43:22.115391-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:22.115854-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.116203-0500	tccd	AUTHREQ_SUBJECT: msgID=395.356, subject=com.nexy.assistant,
default	20:43:22.116858-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:22.133213-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.107, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.134222-0500	tccd	AUTHREQ_SUBJECT: msgID=406.107, subject=com.nexy.assistant,
default	20:43:22.134826-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.149359-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:43:22.151488-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:43:22.151618-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:43:22.152574-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:43:22.153510-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_469.388.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:43:22.153565-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_469.388.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:43:22.222968-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:43:22.224560-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:469 called from <private>
default	20:43:22.224724-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:22.224756-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:468 called from <private>
default	20:43:22.224781-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:22.225203-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
default	20:43:22.225415-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:22.225446-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:469 called from <private>
default	20:43:22.230210-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:22.230571-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:22.225454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:469 called from <private>
default	20:43:22.226305-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:22.226320-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:22.226325-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:22.226382-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:22.231152-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:22.231153-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:22.231199-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:22.231230-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:475 called from <private>
default	20:43:22.231235-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:22.231268-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:475 called from <private>
default	20:43:22.231286-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:22.231376-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:22.231386-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:22.231427-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:469 called from <private>
default	20:43:22.231456-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:22.226535-0500	runningboardd	Invalidating assertion 402-5605-5594 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:22.231502-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:469 called from <private>
default	20:43:22.231530-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:469 called from <private>
default	20:43:22.226932-0500	runningboardd	Invalidating assertion 402-336-5589 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:22.233647-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5599 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:22.233800-0500	runningboardd	Assertion 402-5605-5599 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:22.231574-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:469 called from <private>
default	20:43:22.231600-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:22.231640-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:22.237874-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:22.237909-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:22.233577-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.108, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.238063-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:22.238106-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:22.238279-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:22.242240-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:22.245954-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:22.245966-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:22.246021-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:22.246187-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:22.246432-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:22.246659-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:22.247345-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:43:22.247365-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:43:22.248138-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:22.248158-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:22.248524-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:22.250049-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:22.250514-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:22.248780-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:475 called from <private>
default	20:43:22.248802-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:475 called from <private>
default	20:43:22.248985-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:22.249020-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:22.249073-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:22.251272-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:22.251290-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:22.251338-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:22.251451-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:475 called from <private>
default	20:43:22.251487-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:22.251661-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:475 called from <private>
default	20:43:22.251880-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:22.252127-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:475 called from <private>
default	20:43:22.252466-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:475 called from <private>
default	20:43:22.252654-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:475 called from <private>
default	20:43:22.252687-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:475 called from <private>
default	20:43:22.252731-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:475 called from <private>
default	20:43:22.252772-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:475 called from <private>
default	20:43:22.252811-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:22.252854-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:22.252863-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:22.252873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:22.253595-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:22.253602-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:22.253607-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:22.253612-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:22.253981-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:43:22.254417-0500	tccd	AUTHREQ_SUBJECT: msgID=406.108, subject=com.nexy.assistant,
default	20:43:22.255842-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:22.255852-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:22.254007-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:22.255950-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:22.259948-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:22.260090-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:22.260133-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:22.260142-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:22.269630-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:22.269660-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:22.269763-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:22.279577-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0x857724640: iounit configuration changed > stopping the engine
default	20:43:22.279875-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0x857724640: stop, was running 1
default	20:43:22.280251-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0x857724640: pause, was running 1
default	20:43:22.282757-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:22.292972-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.293090-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:22.293138-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:22.297763-0500	runningboardd	Assertion 402-336-5602 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:22.298998-0500	runningboardd	Invalidating assertion 402-336-5602 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:22.299228-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5603 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:22.299323-0500	runningboardd	Assertion 402-336-5603 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:22.312747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.312767-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.312783-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.312792-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.312800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.312808-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:22.313389-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:43:22.313297-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:22.319752-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:22.320009-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:22.323103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.109, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.318948-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:22.363439-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:43:22.365493-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_469.388.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:43:22.365581-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b1800] Created node ADM::com.nexy.assistant_469.388.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:43:22.410582-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x857724640: iounit configuration changed > posting notification
default	20:43:22.415311-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:43:22.417629-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5607 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:22.417746-0500	runningboardd	Assertion 402-336-5607 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:22.422260-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:22.422329-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:22.423588-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:22.423892-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:22.423999-0500	runningboardd	Invalidating assertion 402-5605-5606 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:22.424254-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5608 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:22.428561-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:22.429008-0500	runningboardd	Invalidating assertion 402-336-5607 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:22.429828-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.110, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.435041-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.435456-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.444070-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:22.445462-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.445569-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:22.445748-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:22.450037-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:22.455427-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.455544-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:22.455605-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:22.455631-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:43:22.471832-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.471847-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.471863-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.471873-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.471882-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.471889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:22.472063-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:22.480968-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:469 called from <private>
error	20:43:22.481014-0500	Nexy	        HALB_IOThread.cpp:327    HALB_IOThread::_Start: there already is a thread
default	20:43:22.481040-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:469 called from <private>
default	20:43:22.481101-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:43:22.482816-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:469 called from <private>
default	20:43:22.482930-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:22.482744-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5609 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:22.482944-0500	runningboardd	Assertion 402-336-5609 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:22.491652-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.111, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:22.492338-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:43:22.492459-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:43:22.492507-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4006, Nexy(5605), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:43:22.492542-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:22.492609-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4006, Nexy(5605), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:43:22.492654-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.492841-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:22.492979-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:22.493144-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:43:22.493160-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4006, Nexy(5605), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 7 starting recording
default	20:43:22.493061-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.493124-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.493170-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.493355-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:22.493444-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.493508-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:22.493513-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:43:22.493621-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:22.493726-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:43:22.498924-0500	tccd	AUTHREQ_SUBJECT: msgID=406.111, subject=com.nexy.assistant,
default	20:43:22.501077-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.501816-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:22.511179-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.511305-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:22.511379-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:22.512666-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:22.520085-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.520196-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:22.520265-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:22.520287-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:43:22.529795-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:22.531253-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:22.531289-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:22.531307-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:22.531347-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:22.569144-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:22.569243-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:22.569304-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:22.569776-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569787-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569799-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.569807-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569813-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.569820-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:22.569844-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569868-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.569933-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.569958-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.569983-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:43:22.569982-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:22.570075-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.570101-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.570158-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.570271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:22.570310-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:22.570347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:22.570564-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:22.643522-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:22.644100-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:23.433057-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	20:43:26.453067-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	20:43:26.656533-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:26.656778-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:43:26.891707-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:43:26.892219-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:43:26.892349-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:26.892422-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:43:26.892453-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:26.892503-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:43:26.892508-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4006, Nexy(5605), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 7 stopping recording
default	20:43:26.892530-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:43:26.892560-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:26.892591-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:26.892761-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:43:26.892772-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:43:26.892862-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:26.895347-0500	runningboardd	Invalidating assertion 402-5605-5610 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:26.895459-0500	runningboardd	Invalidating assertion 402-336-5611 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:26.895526-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:26.895596-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:26.895675-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:26.895726-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:26.895766-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:26.895800-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:43:26.895888-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:43:26.895906-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:26.895919-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:43:26.903683-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:26.903785-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:26.903855-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:26.903873-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:43:26.904409-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:26.904424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:26.904438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:26.904447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:26.904454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:26.904463-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:26.904589-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:26.913467-0500	Nexy	nw_path_libinfo_path_check [D243F157-4AE9-4D57-8346-D3C5C7A3639D Hostname#858ebdb7:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:43:26.913618-0500	mDNSResponder	[R77093] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: b360ab20
default	20:43:26.914540-0500	mDNSResponder	[R77094] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: b360ab20
default	20:43:26.932235-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F0B0068F-DDE8-4C91-9B7C-BF1D23AF839A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52575,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x5edbd1da tp_proto=0x06"
default	20:43:26.932343-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52575<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392200 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbd0e804a
default	20:43:26.939631-0500	kernel	tcp connected: [<IPv4-redacted>:52575<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392200 t_state: ESTABLISHED process: Nexy:5605 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbd0e804a
default	20:43:26.993189-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x858d88740) Selecting device 0 from destructor
default	20:43:26.993204-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:26.993211-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:26.993216-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x858d88740) disconnecting device 91
default	20:43:26.993222-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x858d88740) destroying ioproc 0xa for device 91
default	20:43:26.993267-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:43:26.993304-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:43:26.993469-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x858d88740) nothing to setup
default	20:43:26.993483-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device listeners to device 0
default	20:43:26.993489-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 0
default	20:43:26.993495-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 7 device listeners from device 91
default	20:43:26.993710-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 91
default	20:43:26.993726-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:27.002470-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:27.002517-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:27.002538-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:27.002595-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:27.005139-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:27.005606-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:27.005825-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:28.057400-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:52575<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392200 t_state: LAST_ACK process: Nexy:5605 Duration: 1.125 sec Conn_Time: 0.007 sec bytes in/out: 726/113941 pkts in/out: 4/25 pkt rxmit: 13 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 5.875 ms rttvar: 0.750 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0xbd0e804a
default	20:43:28.057435-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52575<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392200 t_state: LAST_ACK process: Nexy:5605 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 2/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:43:29.119232-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:29.119298-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:29.119319-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:29.119677-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:29.119739-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:29.119745-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:475 called from <private>
default	20:43:29.119772-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:475 called from <private>
default	20:43:29.120328-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.119775-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:469 called from <private>
default	20:43:29.120755-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
default	20:43:29.120759-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:29.120888-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:29.128076-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:29.128108-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:29.128284-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.128309-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:29.128315-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:29.131316-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.131481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:29.131491-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:29.131525-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:29.131535-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:29.132858-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:29.132874-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:29.132989-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.133106-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:29.133161-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:29.136257-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.137897-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.139720-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:29.139744-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:29.139779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:29.139789-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:29.139796-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:29.139802-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:29.140113-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.140129-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:29.140150-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:29.140470-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.140767-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.140872-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:29.141211-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.140779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:29.141479-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:29.141550-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:29.141570-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:29.141747-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:29.141789-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:29.141753-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:29.142194-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:475 called from <private>
default	20:43:29.142406-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:29.142602-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:475 called from <private>
default	20:43:29.142827-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:469 called from <private>
default	20:43:29.142178-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:29.143289-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:29.145134-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:29.145539-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:29.146305-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:29.146630-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:475 called from <private>
default	20:43:29.146644-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:475 called from <private>
default	20:43:29.146692-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:475 called from <private>
default	20:43:29.146703-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:475 called from <private>
default	20:43:29.146711-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:29.146717-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:29.146723-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:29.146728-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:29.146734-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:29.146739-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:29.155066-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:29.155095-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:29.155214-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:29.155718-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:29.155915-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:29.155925-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:29.155961-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:29.155972-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:29.155978-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:29.155986-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:29.156084-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8583eea40) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:29.156105-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8583eea40)
default	20:43:29.156230-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:29.156240-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:29.156248-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:29.156256-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:29.156294-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:29.156574-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:29.156601-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:29.156610-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:29.159143-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8583eea40) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:29.159173-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8583eea40)
default	20:43:29.159440-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:29.159456-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:29.159465-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:29.159475-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:29.159485-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:29.159630-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:29.159656-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:29.159665-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:29.270724-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x857724640: iounit configuration changed > posting notification
default	20:43:32.086352-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x856d50450, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:43:32.086374-0500	Nexy	AudioConverter -> 0x856d50450: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:43:32.086385-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x856d50450: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:32.086390-0500	Nexy	AudioConverter -> 0x856d50450: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:43:32.086394-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:32.086401-0500	Nexy	AudioConverter -> 0x856d50450: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:43:32.086720-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x856d50450: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:32.086746-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x857724640: start, was running 0
default	20:43:32.087694-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5615 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:32.087801-0500	runningboardd	Assertion 402-5605-5615 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:32.088356-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:32.088387-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5616 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:32.088387-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:32.088524-0500	runningboardd	Assertion 402-336-5616 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:32.088536-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:32.088587-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:32.090517-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:32.090744-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:32.090756-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:32.090769-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:32.090817-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:32.090976-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:32.091329-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:32.092947-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:32.093337-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:32.093609-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:32.504504-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:43:32.505465-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:43:32.505609-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:43:32.505649-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4006, Nexy(5605), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:43:32.505685-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:32.505728-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4006, Nexy(5605), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:43:32.505759-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.505783-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:43:32.505806-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 7 starting playing
default	20:43:32.505872-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:32.505903-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:43:32.505928-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:32.505949-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.506006-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.505951-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:43:32.505984-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:43:32.506025-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f4006 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5605}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4006, sessionType: 'prim', isRecording: false }, 
]
default	20:43:32.506164-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:43:32.506158-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:32.506179-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:43:32.507350-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.507446-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.507472-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:32.507488-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:43:32.507497-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:43:32.507508-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	20:43:32.507572-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:43:32.641566-0500	find_contacts_by_name_swift	[0x10514baf0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:32.642347-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5639.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:32.642374-0500	find_contacts_by_name_swift	[0x10514c680] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:43:32.642441-0500	find_contacts_by_name_swift	[0x10514cc40] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:43:32.644088-0500	find_contacts_by_name_swift	[0x10514c3e0] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:43:32.644315-0500	find_contacts_by_name_swift	[0x754c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:32.644819-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5639.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:32.681293-0500	tccd	AUTHREQ_SUBJECT: msgID=5639.2, subject=com.nexy.assistant,
default	20:43:32.682425-0500	tccd	AUTHREQ_SUBJECT: msgID=5639.1, subject=com.nexy.assistant,
default	20:43:32.687288-0500	find_contacts_by_name_swift	[0x754c54000] invalidated after the last release of the connection object
default	20:43:32.687426-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:32.690143-0500	find_contacts_by_name_swift	[0x10514baf0] invalidated after the last release of the connection object
default	20:43:32.690162-0500	find_contacts_by_name_swift	[0x754c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:32.690279-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	20:43:32.690510-0500	find_contacts_by_name_swift	[0x754c54140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:32.690573-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5639.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:32.691034-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5639.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:32.691646-0500	tccd	AUTHREQ_SUBJECT: msgID=5639.3, subject=com.nexy.assistant,
default	20:43:32.692378-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	20:43:32.692518-0500	tccd	AUTHREQ_SUBJECT: msgID=5639.4, subject=com.nexy.assistant,
default	20:43:32.693296-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.708412-0500	find_contacts_by_name_swift	[0x754c54000] invalidated after the last release of the connection object
default	20:43:32.712006-0500	find_contacts_by_name_swift	[0x754c54140] invalidated after the last release of the connection object
default	20:43:32.712177-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	20:43:32.712194-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	20:43:32.712207-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	20:43:32.713623-0500	find_contacts_by_name_swift	[0x754c54000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:32.714750-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.104, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:43:32.716036-0500	tccd	AUTHREQ_SUBJECT: msgID=389.104, subject=com.nexy.assistant,
default	20:43:32.716768-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.740159-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=389.105, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=389, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:43:32.741491-0500	tccd	AUTHREQ_SUBJECT: msgID=389.105, subject=com.nexy.assistant,
default	20:43:32.742238-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.766920-0500	find_contacts_by_name_swift	[0x754c54140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:43:32.767883-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:43:32.767944-0500	find_contacts_by_name_swift	<private> 0x754c40640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:43:32.767965-0500	find_contacts_by_name_swift	<private> 0x754c40640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:43:32.768680-0500	find_contacts_by_name_swift	[0x754c54280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:32.769088-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5639.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:32.770076-0500	tccd	AUTHREQ_SUBJECT: msgID=5639.5, subject=com.nexy.assistant,
default	20:43:32.770648-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.786973-0500	find_contacts_by_name_swift	[0x754c54280] invalidated after the last release of the connection object
default	20:43:32.787014-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:32.793138-0500	find_contacts_by_name_swift	[0x754c54280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:32.793895-0500	find_contacts_by_name_swift	[0x754c54280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.793931-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:32.794060-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:32.796453-0500	find_contacts_by_name_swift	[0x754c56d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.797188-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1087, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.797218-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.798263-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1087, subject=com.nexy.assistant,
default	20:43:32.798865-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.815334-0500	find_contacts_by_name_swift	[0x754c56d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.815397-0500	find_contacts_by_name_swift	[0x754c56d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.815449-0500	find_contacts_by_name_swift	[0x754c56e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.816169-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1088, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.816196-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.817166-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1088, subject=com.nexy.assistant,
default	20:43:32.817843-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.834608-0500	find_contacts_by_name_swift	[0x754c56e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.834654-0500	find_contacts_by_name_swift	[0x754c56e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.834688-0500	find_contacts_by_name_swift	[0x754c56f80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.835333-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1089, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.835361-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.836249-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1089, subject=com.nexy.assistant,
default	20:43:32.836813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.853086-0500	find_contacts_by_name_swift	[0x754c56f80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.853121-0500	find_contacts_by_name_swift	[0x754c56f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.853148-0500	find_contacts_by_name_swift	[0x754c570c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.853760-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1090, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.853786-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.854657-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1090, subject=com.nexy.assistant,
default	20:43:32.855205-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.871524-0500	find_contacts_by_name_swift	[0x754c570c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.871558-0500	find_contacts_by_name_swift	[0x754c570c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.878743-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:32.878756-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:32.878871-0500	find_contacts_by_name_swift	[0x754c57700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:43:32.880178-0500	find_contacts_by_name_swift	0x754c585e0: Using cached account information
default	20:43:32.880276-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	20:43:32.880433-0500	find_contacts_by_name_swift	[0x75508d4a0] Session created.
default	20:43:32.880439-0500	find_contacts_by_name_swift	[0x75508d4a0] Session created with Mach Service: <private>
default	20:43:32.880446-0500	find_contacts_by_name_swift	[0x754c57840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:43:32.880513-0500	find_contacts_by_name_swift	[0x75508d4a0] Session activated
default	20:43:32.882338-0500	find_contacts_by_name_swift	[0x754c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.882342-0500	find_contacts_by_name_swift	[0x75508d4a0] Session canceled.
default	20:43:32.882369-0500	find_contacts_by_name_swift	[0x75508d4a0] Disposing of session
default	20:43:32.882610-0500	find_contacts_by_name_swift	[0x754c57840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:32.883048-0500	find_contacts_by_name_swift	[0x754c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.883064-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:32.883085-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:32.885298-0500	find_contacts_by_name_swift	[0x754e1e300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.886071-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1091, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.886109-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.887250-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1091, subject=com.nexy.assistant,
default	20:43:32.887866-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.905047-0500	find_contacts_by_name_swift	[0x754e1e300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.905085-0500	find_contacts_by_name_swift	[0x754e1e300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.905122-0500	find_contacts_by_name_swift	[0x754e1e440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.905792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1092, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.905822-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.906757-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1092, subject=com.nexy.assistant,
default	20:43:32.907352-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.923675-0500	find_contacts_by_name_swift	[0x754e1e440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.923715-0500	find_contacts_by_name_swift	[0x754e1e440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.923748-0500	find_contacts_by_name_swift	[0x754e1e580] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.924422-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1093, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.924453-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.925421-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1093, subject=com.nexy.assistant,
default	20:43:32.926007-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.942296-0500	find_contacts_by_name_swift	[0x754e1e580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.942329-0500	find_contacts_by_name_swift	[0x754e1e580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.942359-0500	find_contacts_by_name_swift	[0x754e1e6c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.943037-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1094, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.943068-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.943958-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1094, subject=com.nexy.assistant,
default	20:43:32.944513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.960607-0500	find_contacts_by_name_swift	[0x754e1e6c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.960644-0500	find_contacts_by_name_swift	[0x754e1e6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.966169-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:32.966183-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:32.966249-0500	find_contacts_by_name_swift	[0x754e1e940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:32.966689-0500	find_contacts_by_name_swift	[0x754e1e940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.966701-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:32.966712-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:32.968827-0500	find_contacts_by_name_swift	[0x754e41400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.969518-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1095, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.969547-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.970571-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1095, subject=com.nexy.assistant,
default	20:43:32.971163-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:32.987605-0500	find_contacts_by_name_swift	[0x754e41400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:32.987639-0500	find_contacts_by_name_swift	[0x754e41400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:32.987672-0500	find_contacts_by_name_swift	[0x754e41540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:32.988320-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1096, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:32.988348-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:32.989249-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1096, subject=com.nexy.assistant,
default	20:43:32.989825-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.006086-0500	find_contacts_by_name_swift	[0x754e41540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.006119-0500	find_contacts_by_name_swift	[0x754e41540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.006153-0500	find_contacts_by_name_swift	[0x754e41680] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.006886-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1097, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.006920-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.007812-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1097, subject=com.nexy.assistant,
default	20:43:33.008385-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.024588-0500	find_contacts_by_name_swift	[0x754e41680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.024621-0500	find_contacts_by_name_swift	[0x754e41680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.024651-0500	find_contacts_by_name_swift	[0x754e417c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.025353-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1098, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.025382-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.026262-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1098, subject=com.nexy.assistant,
default	20:43:33.026825-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.042623-0500	find_contacts_by_name_swift	[0x754e417c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.042661-0500	find_contacts_by_name_swift	[0x754e417c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.043517-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.043530-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.053338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1099, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.053365-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.054366-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1099, subject=com.nexy.assistant,
default	20:43:33.054941-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.071731-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1100, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.071768-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5639, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.072690-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1100, subject=com.nexy.assistant,
default	20:43:33.073251-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.095546-0500	find_contacts_by_name_swift	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	20:43:33.097003-0500	find_contacts_by_name_swift	"Error returned from daemon: Error Domain=com.apple.accounts Code=7"
error	20:43:33.097054-0500	find_contacts_by_name_swift	"ACMonitoredAccountStore: Failed to fetch accounts: Error Domain=com.apple.accounts Code=7"
default	20:43:33.136245-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	20:43:33.136257-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	20:43:33.136382-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	20:43:33.137979-0500	find_contacts_by_name_swift	decoratedContacts called with 0 contacts
default	20:43:33.137996-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	20:43:33.138016-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	20:43:33.138022-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	20:43:33.138031-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	20:43:33.138047-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	20:43:33.138088-0500	find_contacts_by_name_swift	0000 FINISH (426 ms)
default	20:43:33.138170-0500	find_contacts_by_name_swift	Entering exit handler.
default	20:43:33.138178-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:43:33.138212-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:43:33.138217-0500	find_contacts_by_name_swift	[0x754c57700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.138268-0500	find_contacts_by_name_swift	Exiting exit handler.
default	20:43:33.138284-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	20:43:33.158957-0500	find_contacts_by_name_swift	[0x104c73ab0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.159713-0500	find_contacts_by_name_swift	[0x104c74600] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:43:33.159782-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5641.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.159784-0500	find_contacts_by_name_swift	[0x104c74bc0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:43:33.161386-0500	find_contacts_by_name_swift	[0x104c75580] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:43:33.161617-0500	find_contacts_by_name_swift	[0x7e4c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.162091-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5641.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.191035-0500	tccd	AUTHREQ_SUBJECT: msgID=5641.2, subject=com.nexy.assistant,
default	20:43:33.196168-0500	find_contacts_by_name_swift	[0x7e4c54000] invalidated after the last release of the connection object
default	20:43:33.196284-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:33.198693-0500	tccd	AUTHREQ_SUBJECT: msgID=5641.1, subject=com.nexy.assistant,
default	20:43:33.204561-0500	find_contacts_by_name_swift	[0x104c73ab0] invalidated after the last release of the connection object
default	20:43:33.204580-0500	find_contacts_by_name_swift	[0x7e4c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.204689-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	20:43:33.204900-0500	find_contacts_by_name_swift	[0x7e4c54140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.204942-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5641.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.205374-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5641.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.205894-0500	tccd	AUTHREQ_SUBJECT: msgID=5641.3, subject=com.nexy.assistant,
default	20:43:33.206533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:43:33.207272-0500	tccd	AUTHREQ_SUBJECT: msgID=5641.4, subject=com.nexy.assistant,
default	20:43:33.208705-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.222598-0500	find_contacts_by_name_swift	[0x7e4c54000] invalidated after the last release of the connection object
default	20:43:33.226156-0500	find_contacts_by_name_swift	[0x7e4c54140] invalidated after the last release of the connection object
default	20:43:33.226326-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	20:43:33.226345-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	20:43:33.226357-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	20:43:33.227678-0500	find_contacts_by_name_swift	[0x7e4c54000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.231596-0500	find_contacts_by_name_swift	[0x7e4c54140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:43:33.232460-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:43:33.232508-0500	find_contacts_by_name_swift	<private> 0x7e4c40640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:43:33.232527-0500	find_contacts_by_name_swift	<private> 0x7e4c40640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:43:33.233165-0500	find_contacts_by_name_swift	[0x7e4c54280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.233577-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5641.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.234549-0500	tccd	AUTHREQ_SUBJECT: msgID=5641.5, subject=com.nexy.assistant,
default	20:43:33.235111-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.251780-0500	find_contacts_by_name_swift	[0x7e4c54280] invalidated after the last release of the connection object
default	20:43:33.251812-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:33.257195-0500	find_contacts_by_name_swift	[0x7e4c54280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.257723-0500	find_contacts_by_name_swift	[0x7e4c54280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.257759-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.257889-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.260265-0500	find_contacts_by_name_swift	[0x7e4c56d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.260979-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1101, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.261008-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.261971-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1101, subject=com.nexy.assistant,
default	20:43:33.262574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.279460-0500	find_contacts_by_name_swift	[0x7e4c56d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.279526-0500	find_contacts_by_name_swift	[0x7e4c56d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.279577-0500	find_contacts_by_name_swift	[0x7e4c56e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.280297-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1102, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.280325-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.281342-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1102, subject=com.nexy.assistant,
default	20:43:33.281938-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.298937-0500	find_contacts_by_name_swift	[0x7e4c56e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.298991-0500	find_contacts_by_name_swift	[0x7e4c56e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.299037-0500	find_contacts_by_name_swift	[0x7e4c56f80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.299743-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1103, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.299771-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.300717-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1103, subject=com.nexy.assistant,
default	20:43:33.301266-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.318111-0500	find_contacts_by_name_swift	[0x7e4c56f80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.318147-0500	find_contacts_by_name_swift	[0x7e4c56f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.318177-0500	find_contacts_by_name_swift	[0x7e4c570c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.318794-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1104, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.318820-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.319678-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1104, subject=com.nexy.assistant,
default	20:43:33.320209-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.336513-0500	find_contacts_by_name_swift	[0x7e4c570c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.336544-0500	find_contacts_by_name_swift	[0x7e4c570c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.341425-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.341437-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.341525-0500	find_contacts_by_name_swift	[0x7e4c57700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:43:33.342135-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	20:43:33.342619-0500	find_contacts_by_name_swift	0x7e4c585e0: Using cached account information
default	20:43:33.342802-0500	find_contacts_by_name_swift	[0x7e508d4a0] Session created.
default	20:43:33.342808-0500	find_contacts_by_name_swift	[0x7e508d4a0] Session created with Mach Service: <private>
default	20:43:33.342813-0500	find_contacts_by_name_swift	[0x7e4c57840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:43:33.342869-0500	find_contacts_by_name_swift	[0x7e508d4a0] Session activated
default	20:43:33.344222-0500	find_contacts_by_name_swift	[0x7e4c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.344227-0500	find_contacts_by_name_swift	[0x7e508d4a0] Session canceled.
default	20:43:33.344264-0500	find_contacts_by_name_swift	[0x7e508d4a0] Disposing of session
default	20:43:33.344443-0500	find_contacts_by_name_swift	[0x7e4c57840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.344836-0500	find_contacts_by_name_swift	[0x7e4c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.344851-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:33.344866-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.346935-0500	find_contacts_by_name_swift	[0x7e4e2a300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.347598-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1105, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.347625-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.348582-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1105, subject=com.nexy.assistant,
default	20:43:33.349119-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.365866-0500	find_contacts_by_name_swift	[0x7e4e2a300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.365904-0500	find_contacts_by_name_swift	[0x7e4e2a300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.365948-0500	find_contacts_by_name_swift	[0x7e4e2a440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.366563-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1106, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.366589-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.367502-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1106, subject=com.nexy.assistant,
default	20:43:33.368031-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.384360-0500	find_contacts_by_name_swift	[0x7e4e2a440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.384390-0500	find_contacts_by_name_swift	[0x7e4e2a580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.384419-0500	find_contacts_by_name_swift	[0x7e4e2a440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.384975-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1107, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.385003-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.385839-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1107, subject=com.nexy.assistant,
default	20:43:33.386356-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.402427-0500	find_contacts_by_name_swift	[0x7e4e2a440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.402458-0500	find_contacts_by_name_swift	[0x7e4e2a440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.402488-0500	find_contacts_by_name_swift	[0x7e4e2a6c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.403048-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1108, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.403078-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.404166-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1108, subject=com.nexy.assistant,
default	20:43:33.405164-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.421546-0500	find_contacts_by_name_swift	[0x7e4e2a6c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.421580-0500	find_contacts_by_name_swift	[0x7e4e2a6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.425592-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.425606-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:33.425657-0500	find_contacts_by_name_swift	[0x7e4e2a940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.426019-0500	find_contacts_by_name_swift	[0x7e4e2a940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.426034-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.426047-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.428020-0500	find_contacts_by_name_swift	[0x7e4e51400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.428648-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1109, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.428677-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.429661-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1109, subject=com.nexy.assistant,
default	20:43:33.430232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.446372-0500	find_contacts_by_name_swift	[0x7e4e51400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.446402-0500	find_contacts_by_name_swift	[0x7e4e51400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.446433-0500	find_contacts_by_name_swift	[0x7e4e51540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.447017-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1110, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.447043-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.447915-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1110, subject=com.nexy.assistant,
default	20:43:33.448456-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.464364-0500	find_contacts_by_name_swift	[0x7e4e51540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.464399-0500	find_contacts_by_name_swift	[0x7e4e51540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.464436-0500	find_contacts_by_name_swift	[0x7e4e51680] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.465020-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1111, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.465045-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.465889-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1111, subject=com.nexy.assistant,
default	20:43:33.466418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.482399-0500	find_contacts_by_name_swift	[0x7e4e51680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.482434-0500	find_contacts_by_name_swift	[0x7e4e51680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.482466-0500	find_contacts_by_name_swift	[0x7e4e517c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.483057-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1112, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.483084-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.484256-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1112, subject=com.nexy.assistant,
default	20:43:33.485465-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.502317-0500	find_contacts_by_name_swift	[0x7e4e517c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.502350-0500	find_contacts_by_name_swift	[0x7e4e517c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.503128-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.503142-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.509560-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1113, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.509588-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.510535-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1113, subject=com.nexy.assistant,
default	20:43:33.511081-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.529402-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1114, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.529431-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5641, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.530313-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1114, subject=com.nexy.assistant,
default	20:43:33.530945-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.566210-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	20:43:33.566221-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	20:43:33.566342-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	20:43:33.567960-0500	find_contacts_by_name_swift	decoratedContacts called with 0 contacts
default	20:43:33.567975-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	20:43:33.567996-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	20:43:33.568002-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	20:43:33.568007-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	20:43:33.568026-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	20:43:33.568064-0500	find_contacts_by_name_swift	0000 FINISH (342 ms)
default	20:43:33.568146-0500	find_contacts_by_name_swift	Entering exit handler.
default	20:43:33.568155-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:43:33.568187-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:43:33.568195-0500	find_contacts_by_name_swift	[0x7e4c57700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.568212-0500	find_contacts_by_name_swift	Exiting exit handler.
default	20:43:33.568228-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	20:43:33.588926-0500	find_contacts_by_name_swift	[0x101663a80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.589723-0500	find_contacts_by_name_swift	[0x101664630] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:43:33.589790-0500	find_contacts_by_name_swift	[0x101664bf0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:43:33.589803-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5642.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.591419-0500	find_contacts_by_name_swift	[0x1016655b0] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:43:33.591650-0500	find_contacts_by_name_swift	[0x918c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.592123-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5642.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.621757-0500	tccd	AUTHREQ_SUBJECT: msgID=5642.2, subject=com.nexy.assistant,
default	20:43:33.627340-0500	find_contacts_by_name_swift	[0x918c54000] invalidated after the last release of the connection object
default	20:43:33.627453-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:33.630235-0500	tccd	AUTHREQ_SUBJECT: msgID=5642.1, subject=com.nexy.assistant,
default	20:43:33.635829-0500	find_contacts_by_name_swift	[0x101663a80] invalidated after the last release of the connection object
default	20:43:33.635848-0500	find_contacts_by_name_swift	[0x918c54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.635972-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	20:43:33.636219-0500	find_contacts_by_name_swift	[0x918c54140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.636254-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5642.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.636718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5642.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.637304-0500	tccd	AUTHREQ_SUBJECT: msgID=5642.3, subject=com.nexy.assistant,
default	20:43:33.637989-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	20:43:33.638952-0500	tccd	AUTHREQ_SUBJECT: msgID=5642.4, subject=com.nexy.assistant,
default	20:43:33.640327-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.654619-0500	find_contacts_by_name_swift	[0x918c54000] invalidated after the last release of the connection object
default	20:43:33.658241-0500	find_contacts_by_name_swift	[0x918c54140] invalidated after the last release of the connection object
default	20:43:33.658418-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	20:43:33.658435-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	20:43:33.658448-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	20:43:33.659789-0500	find_contacts_by_name_swift	[0x918c54000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.663948-0500	find_contacts_by_name_swift	[0x918c54140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:43:33.664849-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:43:33.664895-0500	find_contacts_by_name_swift	<private> 0x918c40640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:43:33.664911-0500	find_contacts_by_name_swift	<private> 0x918c40640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:43:33.665530-0500	find_contacts_by_name_swift	[0x918c54280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:33.665930-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5642.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:33.666920-0500	tccd	AUTHREQ_SUBJECT: msgID=5642.5, subject=com.nexy.assistant,
default	20:43:33.667484-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.684007-0500	find_contacts_by_name_swift	[0x918c54280] invalidated after the last release of the connection object
default	20:43:33.684036-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:33.689459-0500	find_contacts_by_name_swift	[0x918c54280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.690006-0500	find_contacts_by_name_swift	[0x918c54280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.690040-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.690176-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.692531-0500	find_contacts_by_name_swift	[0x918c56d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.693238-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1115, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.693265-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.694192-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1115, subject=com.nexy.assistant,
default	20:43:33.694731-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.711791-0500	find_contacts_by_name_swift	[0x918c56d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.711844-0500	find_contacts_by_name_swift	[0x918c56d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.711890-0500	find_contacts_by_name_swift	[0x918c56e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.712486-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1116, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.712512-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.713589-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1116, subject=com.nexy.assistant,
default	20:43:33.714595-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.731118-0500	find_contacts_by_name_swift	[0x918c56e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.731158-0500	find_contacts_by_name_swift	[0x918c56e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.731193-0500	find_contacts_by_name_swift	[0x918c56f80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.731806-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1117, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.731839-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.732806-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1117, subject=com.nexy.assistant,
default	20:43:33.733380-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.749963-0500	find_contacts_by_name_swift	[0x918c56f80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.749994-0500	find_contacts_by_name_swift	[0x918c56f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.750021-0500	find_contacts_by_name_swift	[0x918c570c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.750595-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1118, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.750622-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.751508-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1118, subject=com.nexy.assistant,
default	20:43:33.752043-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.768282-0500	find_contacts_by_name_swift	[0x918c570c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.768316-0500	find_contacts_by_name_swift	[0x918c570c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.773278-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.773288-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.773380-0500	find_contacts_by_name_swift	[0x918c57700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:43:33.774111-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	20:43:33.774511-0500	find_contacts_by_name_swift	0x918c585e0: Using cached account information
default	20:43:33.774701-0500	find_contacts_by_name_swift	[0x91908d4a0] Session created.
default	20:43:33.774707-0500	find_contacts_by_name_swift	[0x91908d4a0] Session created with Mach Service: <private>
default	20:43:33.774713-0500	find_contacts_by_name_swift	[0x918c57840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:43:33.774763-0500	find_contacts_by_name_swift	[0x91908d4a0] Session activated
default	20:43:33.776170-0500	find_contacts_by_name_swift	[0x918c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.776175-0500	find_contacts_by_name_swift	[0x91908d4a0] Session canceled.
default	20:43:33.776231-0500	find_contacts_by_name_swift	[0x91908d4a0] Disposing of session
default	20:43:33.776376-0500	find_contacts_by_name_swift	[0x918c57840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.776758-0500	find_contacts_by_name_swift	[0x918c57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.776772-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:33.776788-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.778873-0500	find_contacts_by_name_swift	[0x918e22300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.779599-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1119, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.779628-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.780716-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1119, subject=com.nexy.assistant,
default	20:43:33.781300-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.798454-0500	find_contacts_by_name_swift	[0x918e22300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.798492-0500	find_contacts_by_name_swift	[0x918e22300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.798531-0500	find_contacts_by_name_swift	[0x918e22440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.799149-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1120, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.799181-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.800353-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1120, subject=com.nexy.assistant,
default	20:43:33.801306-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.818423-0500	find_contacts_by_name_swift	[0x918e22440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.818464-0500	find_contacts_by_name_swift	[0x918e22440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.818500-0500	find_contacts_by_name_swift	[0x918e22580] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.819288-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1121, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.819320-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.820424-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1121, subject=com.nexy.assistant,
default	20:43:33.821069-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.838644-0500	find_contacts_by_name_swift	[0x918e22580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.838680-0500	find_contacts_by_name_swift	[0x918e22580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.838712-0500	find_contacts_by_name_swift	[0x918e226c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.839457-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1122, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.839483-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.840420-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1122, subject=com.nexy.assistant,
default	20:43:33.840989-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.857167-0500	find_contacts_by_name_swift	[0x918e226c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.857212-0500	find_contacts_by_name_swift	[0x918e226c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.861701-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.861717-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:33.861782-0500	find_contacts_by_name_swift	[0x918e22940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:33.862212-0500	find_contacts_by_name_swift	[0x918e22940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.862229-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.862241-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:33.864332-0500	find_contacts_by_name_swift	[0x918e45400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.864928-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1123, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.864962-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.865995-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1123, subject=com.nexy.assistant,
default	20:43:33.866580-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.883097-0500	find_contacts_by_name_swift	[0x918e45400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.883141-0500	find_contacts_by_name_swift	[0x918e45400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.883187-0500	find_contacts_by_name_swift	[0x918e45540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.883871-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1124, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.883900-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.884810-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1124, subject=com.nexy.assistant,
default	20:43:33.885365-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.902450-0500	find_contacts_by_name_swift	[0x918e45540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.902484-0500	find_contacts_by_name_swift	[0x918e45540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.902518-0500	find_contacts_by_name_swift	[0x918e45680] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.903214-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1125, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.903244-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.904148-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1125, subject=com.nexy.assistant,
default	20:43:33.904700-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.922142-0500	find_contacts_by_name_swift	[0x918e45680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.922178-0500	find_contacts_by_name_swift	[0x918e45680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.922209-0500	find_contacts_by_name_swift	[0x918e457c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:33.922892-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1126, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.922925-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.923810-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1126, subject=com.nexy.assistant,
default	20:43:33.924360-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.941593-0500	find_contacts_by_name_swift	[0x918e457c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:33.941627-0500	find_contacts_by_name_swift	[0x918e457c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:33.942447-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:33.942462-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:33.949321-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1127, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.949352-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.950388-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1127, subject=com.nexy.assistant,
default	20:43:33.950984-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:33.968859-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1128, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:33.968889-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5642, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:33.969773-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1128, subject=com.nexy.assistant,
default	20:43:33.970335-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:34.006844-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	20:43:34.006855-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	20:43:34.006964-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	20:43:34.013386-0500	find_contacts_by_name_swift	decoratedContacts called with 4 contacts
default	20:43:34.013402-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	20:43:34.013422-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	20:43:34.013428-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	20:43:34.013432-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	20:43:34.013452-0500	find_contacts_by_name_swift	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	20:43:34.013559-0500	find_contacts_by_name_swift	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	20:43:34.013576-0500	find_contacts_by_name_swift	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	20:43:34.013587-0500	find_contacts_by_name_swift	0000 Contact: 7E2E667C-A7D1-4A88-9C92-C2F38557DF00:ABPerson
default	20:43:34.013607-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	20:43:34.013648-0500	find_contacts_by_name_swift	0000 Time spent in client code: 114 µs
default	20:43:34.013662-0500	find_contacts_by_name_swift	0000 FINISH (355 ms)
default	20:43:34.013808-0500	find_contacts_by_name_swift	Entering exit handler.
default	20:43:34.013816-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:43:34.013848-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:43:34.013854-0500	find_contacts_by_name_swift	[0x918c57700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:34.013868-0500	find_contacts_by_name_swift	Exiting exit handler.
default	20:43:34.013881-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	20:43:34.549005-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:35.420629-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:35.821822-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:35.823532-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:35.823550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:35.823570-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:35.823580-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:35.823591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:35.823601-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:35.823745-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:38.423043-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:41.428560-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:41.711954-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	20:43:41.738590-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x858d88740) Selecting device 85 from constructor
default	20:43:41.738614-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:41.738621-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:41.738627-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x858d88740) nothing to teardown
default	20:43:41.738632-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x858d88740) connecting device 85
default	20:43:41.738735-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x858d88740) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:41.738991-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x858d88740) created ioproc 0xc for device 85
default	20:43:41.739151-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 7 device listeners to device 85
default	20:43:41.739387-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 85
default	20:43:41.739401-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x858d88740)
default	20:43:41.739511-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:41.739523-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:41.739531-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:41.739538-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:41.739562-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:41.739681-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:41.739694-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:41.739701-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:41.739706-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device listeners from device 0
default	20:43:41.739712-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 0
default	20:43:41.739718-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:41.739741-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:43:41.739811-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x858d88740) caller requesting device change from 85 to 91
default	20:43:41.739824-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:41.739831-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:41.739837-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x858d88740) disconnecting device 85
default	20:43:41.739844-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x858d88740) destroying ioproc 0xc for device 85
default	20:43:41.739864-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	20:43:41.740176-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:43:41.740432-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x858d88740) connecting device 91
default	20:43:41.740602-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x858d88740) Device ID: 91 (Input:Yes | Output:No): true
default	20:43:41.742937-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.112, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:41.745326-0500	tccd	AUTHREQ_SUBJECT: msgID=406.112, subject=com.nexy.assistant,
default	20:43:41.747257-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:41.767841-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x858d88740) created ioproc 0xb for device 91
default	20:43:41.767983-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 7 device listeners to device 91
default	20:43:41.768147-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 91
default	20:43:41.768167-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x858d88740)
default	20:43:41.768177-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:43:41.768187-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:41.768325-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:43:41.768333-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:43:41.768341-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:43:41.768433-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:41.768449-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x858d88740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:41.768454-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:41.768460-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 7 device listeners from device 85
default	20:43:41.768609-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 85
default	20:43:41.768616-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:41.768627-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:43:41.769151-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:43:41.770319-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.113, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:41.771353-0500	tccd	AUTHREQ_SUBJECT: msgID=406.113, subject=com.nexy.assistant,
default	20:43:41.771969-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:41.780571-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:43:41.780605-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:43:41.781972-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:43:41.782000-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:41.782913-0500	tccd	AUTHREQ_SUBJECT: msgID=94711.6, subject=com.nexy.assistant,
default	20:43:41.783793-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:41.789045-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:43:41.789938-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.114, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:41.790944-0500	tccd	AUTHREQ_SUBJECT: msgID=406.114, subject=com.nexy.assistant,
default	20:43:41.791498-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:41.808736-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.115, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:41.809645-0500	tccd	AUTHREQ_SUBJECT: msgID=406.115, subject=com.nexy.assistant,
default	20:43:41.810200-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:41.822945-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:43:41.827142-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:43:41.827275-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:43:41.828636-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:469 called from <private>
default	20:43:41.828641-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:43:41.828722-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:41.828749-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:41.828758-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:41.828825-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.828821-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:41.828886-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:41.829305-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
default	20:43:41.829478-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:41.829499-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:469 called from <private>
default	20:43:41.834274-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:41.834872-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:41.829505-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:469 called from <private>
default	20:43:41.830476-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:41.830658-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:41.831083-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:475 called from <private>
default	20:43:41.831105-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:41.831140-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:475 called from <private>
default	20:43:41.836046-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:41.836086-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:41.836158-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:41.836201-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:41.836318-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:469 called from <private>
default	20:43:41.836370-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:41.830799-0500	runningboardd	Invalidating assertion 402-5605-5615 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:41.836421-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:469 called from <private>
default	20:43:41.836451-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:469 called from <private>
default	20:43:41.831429-0500	runningboardd	Invalidating assertion 402-336-5616 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:41.836512-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:469 called from <private>
default	20:43:41.836544-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:41.836606-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:41.842344-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:41.837244-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5620 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:41.842407-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:41.843024-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:41.837374-0500	runningboardd	Assertion 402-5605-5620 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:41.842389-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:41.843604-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:475 called from <private>
default	20:43:41.843780-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:475 called from <private>
default	20:43:41.844173-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.844209-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:41.844274-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:41.845230-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.845355-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.845418-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:41.845541-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:41.838134-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.116, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:41.845607-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.851665-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:41.851674-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:41.851756-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.854140-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.854154-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.854350-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:41.854365-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:41.855540-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:41.855547-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:41.855722-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.858931-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.859177-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:41.859185-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:41.859201-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:41.859206-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:41.859211-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:41.859376-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8583eea40) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:41.859412-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8583eea40)
default	20:43:41.859617-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:43:41.859663-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:41.859771-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
error	20:43:41.859797-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:43:41.859930-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:41.860061-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:41.860109-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:41.860153-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:41.859558-0500	tccd	AUTHREQ_SUBJECT: msgID=406.116, subject=com.nexy.assistant,
default	20:43:41.860249-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:41.860297-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:41.860402-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:41.860460-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:41.860492-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:41.860542-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:41.861154-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x854786d90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:43:41.861413-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
error	20:43:41.861464-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:43:41.861694-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:41.861809-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:41.861937-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:41.864765-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	20:43:41.862029-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:41.862404-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.865005-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
error	20:43:41.862682-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:43:41.865094-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4006, Nexy(5605), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:43:41.862786-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:41.862935-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:41.865252-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:43:41.863027-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:41.865428-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:41.866854-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:41.865400-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:41.867783-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:43:41.865657-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:41.879367-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:43:41.879378-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:41.879384-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	20:43:41.879796-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:41.879394-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:41.879403-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:41.879535-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:43:41.884829-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:41.886528-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.886538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.886568-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.886668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.899420-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:43:41.899472-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:43:41.910731-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:43:41.910873-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:43:41.913893-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5624 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:41.925390-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:41.930799-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:41.930902-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:41.930955-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:41.931250-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931262-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931273-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.931313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.931473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:41.931530-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931545-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.931602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931636-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:43:41.931641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.931670-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:41.931721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931757-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931793-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.931838-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:41.931869-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:41.932028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:41.932162-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:41.943165-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:41.943861-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=94711.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:43:41.943893-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=94711, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:41.956501-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:43:41.995326-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:43:42.003691-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x857724640: iounit configuration changed > posting notification
default	20:43:42.044234-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:43:42.048815-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5626 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:42.049004-0500	runningboardd	Assertion 402-336-5626 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:42.047285-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:469 called from <private>
default	20:43:42.047308-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:469 called from <private>
default	20:43:42.048300-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:43:42.049371-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
default	20:43:42.049396-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:42.049846-0500	runningboardd	Invalidating assertion 402-5605-5625 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:42.049622-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:469 called from <private>
default	20:43:42.049896-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:42.050184-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5627 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:42.050195-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:42.050299-0500	runningboardd	Assertion 402-5605-5627 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:42.050299-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:42.050400-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:42.049861-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
error	20:43:42.049938-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:43:42.050013-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:42.050067-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:42.050139-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:469 called from <private>
default	20:43:42.050182-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:469 called from <private>
default	20:43:42.051151-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:42.051666-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:42.052289-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:42.052547-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:469 called from <private>
default	20:43:42.052561-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:469 called from <private>
default	20:43:42.052582-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:42.055313-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.118, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:43:42.056298-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:42.056752-0500	runningboardd	Invalidating assertion 402-5605-5627 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:42.056880-0500	runningboardd	Invalidating assertion 402-336-5626 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:42.057219-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:42.057111-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5628 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:42.057176-0500	runningboardd	Assertion 402-5605-5628 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:42.058182-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:42.058315-0500	tccd	AUTHREQ_SUBJECT: msgID=406.118, subject=com.nexy.assistant,
default	20:43:42.059498-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:42.063497-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:42.069103-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:42.069181-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:42.069237-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:42.069637-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069667-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069677-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.069727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069741-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069751-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069761-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069768-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.069794-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069808-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069819-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069848-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.069885-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:43:42.069889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.069911-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.069972-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:42.076080-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:42.076169-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:42.076258-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:42.076296-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:43:42.092245-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.092266-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.092286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.092295-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.092304-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.092313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.092444-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:42.096292-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5629 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:42.096422-0500	runningboardd	Assertion 402-336-5629 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:42.096721-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:469 called from <private>
default	20:43:42.107016-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:42.114309-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:42.114423-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:43:42.114518-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	20:43:42.114938-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.114959-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.114974-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.114986-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.114996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.115006-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.115031-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.115044-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.115124-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.115156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:42.115196-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:43:42.115191-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:42.115298-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:42.115319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:44.453556-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	20:43:45.968656-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:43:45.969232-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:43:45.969364-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:45.969432-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:43:45.969461-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:45.969515-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:43:45.969516-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4006, Nexy(5605), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 7 stopping recording
default	20:43:45.969540-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:43:45.969567-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:45.969599-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:45.969779-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:43:45.969789-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:43:45.969854-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:45.972251-0500	runningboardd	Invalidating assertion 402-5605-5628 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605]
default	20:43:45.972341-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:45.972484-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:45.972417-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:45.972536-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:43:45.972371-0500	runningboardd	Invalidating assertion 402-336-5629 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) from originator [osservice<com.apple.powerd>:336]
default	20:43:45.972577-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:45.972616-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:43:45.972707-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:43:45.972724-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:45.972739-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:43:45.980822-0500	Nexy	nw_path_libinfo_path_check [C7E32863-28C1-4B66-AD3E-A408C007224E Hostname#858ebdb7:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:43:45.980971-0500	mDNSResponder	[R77109] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: b360ab20
default	20:43:45.982089-0500	mDNSResponder	[R77110] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5605 (Nexy), name hash: b360ab20
default	20:43:45.982127-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:45.982240-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:45.982312-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:43:45.982335-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:43:45.983056-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:45.983072-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:45.983086-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:45.983093-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:43:45.983123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:43:45.983133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:43:45.983238-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:43:45.984141-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4CA211FF-2EB1-448D-9434-1751924F0306 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52586,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x8da384c5 tp_proto=0x06"
default	20:43:45.984246-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52586<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392454 t_state: SYN_SENT process: Nexy:5605 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa5e5fc8e
default	20:43:45.995601-0500	kernel	tcp connected: [<IPv4-redacted>:52586<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392454 t_state: ESTABLISHED process: Nexy:5605 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa5e5fc8e
default	20:43:46.069511-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x858d88740) Selecting device 0 from destructor
default	20:43:46.069528-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x858d88740)
default	20:43:46.069535-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x858d88740) not already running
default	20:43:46.069542-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x858d88740) disconnecting device 91
default	20:43:46.069554-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x858d88740) destroying ioproc 0xb for device 91
default	20:43:46.069600-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:43:46.069643-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:43:46.069816-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x858d88740) nothing to setup
default	20:43:46.069828-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device listeners to device 0
default	20:43:46.069837-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x858d88740) adding 0 device delegate listeners to device 0
default	20:43:46.069844-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 7 device listeners from device 91
default	20:43:46.070084-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x858d88740) removing 0 device delegate listeners from device 91
default	20:43:46.070102-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x858d88740)
default	20:43:46.079235-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:46.079255-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:46.079268-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:46.079293-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:46.082427-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:46.083019-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:46.083435-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:46.198976-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:46.898485-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:52586<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392454 t_state: LAST_ACK process: Nexy:5605 Duration: 0.914 sec Conn_Time: 0.011 sec bytes in/out: 630/87243 pkts in/out: 4/19 pkt rxmit: 7 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 7.312 ms rttvar: 3.375 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0xa5e5fc8e
default	20:43:46.898520-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52586<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 392454 t_state: LAST_ACK process: Nexy:5605 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 2/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:43:48.196842-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.196938-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:48.196953-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:48.197530-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:48.197566-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:48.197582-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:48.197870-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:48.197890-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(469)
default	20:43:48.197937-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:475 called from <private>
default	20:43:48.197963-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:469 called from <private>
default	20:43:48.197978-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:475 called from <private>
default	20:43:48.197999-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:469 called from <private>
default	20:43:48.205693-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:48.205730-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:48.206080-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.206109-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:48.206118-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:48.209461-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.209820-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:48.209834-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:48.209857-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:48.209911-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:48.211708-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:468 called from <private>
default	20:43:48.211808-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:468 called from <private>
default	20:43:48.212160-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.212260-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:468 called from <private>
default	20:43:48.212296-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:468 called from <private>
default	20:43:48.217178-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.217216-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.217581-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.218502-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.218692-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.220443-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:468 called from <private>
default	20:43:48.220814-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:468 called from <private>
default	20:43:48.221172-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:48.221225-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(469)
default	20:43:48.221224-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:468 called from <private>
default	20:43:48.221924-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:469 called from <private>
default	20:43:48.222098-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:468 called from <private>
default	20:43:48.222323-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:469 called from <private>
default	20:43:48.222894-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:48.222598-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.223359-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:48.222490-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:48.223670-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:48.223925-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:48.223982-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:48.224028-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:48.224069-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:48.224097-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:48.224112-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:48.224118-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:48.224231-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:475 called from <private>
default	20:43:48.224244-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:475 called from <private>
default	20:43:48.224471-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(475)
default	20:43:48.226888-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:43:48.227236-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:43:48.228081-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(475)
default	20:43:48.228388-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:475 called from <private>
default	20:43:48.228410-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:475 called from <private>
default	20:43:48.228461-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:475 called from <private>
default	20:43:48.228472-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:475 called from <private>
default	20:43:48.228481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:48.228488-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:48.228496-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:475 called from <private>
default	20:43:48.228502-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:475 called from <private>
default	20:43:48.228509-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:475 called from <private>
default	20:43:48.228514-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:475 called from <private>
default	20:43:48.236362-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:48.236392-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:48.236529-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(468)
default	20:43:48.238657-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(468)
default	20:43:48.238892-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:48.238903-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:48.238943-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:468 called from <private>
default	20:43:48.238950-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:468 called from <private>
default	20:43:48.238955-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:468 called from <private>
default	20:43:48.238961-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:468 called from <private>
default	20:43:48.239223-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8583eea40) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:48.239242-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8583eea40)
default	20:43:48.239377-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:48.239388-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:48.239396-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:48.239407-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:48.239444-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:48.239645-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:48.239670-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:48.239679-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:48.239840-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8583eea40) Device ID: 85 (Input:No | Output:Yes): true
default	20:43:48.239851-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8583eea40)
default	20:43:48.239968-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:48.239978-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:43:48.239984-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:43:48.239994-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:43:48.240024-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:43:48.240453-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:43:48.240480-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8583eea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:43:48.240493-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:43:48.351183-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x857724640: iounit configuration changed > posting notification
default	20:43:50.353807-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x856d505d0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:43:50.353821-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x856d505d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:50.353831-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:43:50.353831-0500	Nexy	AudioConverter -> 0x856d505d0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:43:50.353842-0500	Nexy	AudioConverter -> 0x856d505d0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:43:50.353848-0500	Nexy	AudioConverter -> 0x856d505d0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:43:50.354156-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x856d505d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:43:50.354183-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x857724640: start, was running 0
default	20:43:50.355391-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-5605-5634 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:43:50.355496-0500	runningboardd	Assertion 402-5605-5634 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:50.356070-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54170280.54170289(501)>:5605] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-5635 target:5605 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:43:50.356064-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:50.356302-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:50.356339-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:50.356349-0500	runningboardd	Assertion 402-336-5635 (target:[app<application.com.nexy.assistant.54170280.54170289(501)>:5605]) will be created as active
default	20:43:50.356452-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:50.359158-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:50.359349-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring jetsam update because this process is not memory-managed
default	20:43:50.359360-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring suspend because this process is not lifecycle managed
default	20:43:50.359369-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring GPU update because this process is not GPU managed
default	20:43:50.359406-0500	runningboardd	[app<application.com.nexy.assistant.54170280.54170289(501)>:5605] Ignoring memory limit update because this process is not memory-managed
default	20:43:50.359524-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:50.359765-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:50.361505-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54170280.54170289(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:43:50.361877-0500	ControlCenter	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:50.362004-0500	gamepolicyd	Received state update for 5605 (app<application.com.nexy.assistant.54170280.54170289(501)>, running-active-NotVisible
default	20:43:50.720182-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:43:50.721106-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4006","name":"Nexy(5605)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:43:50.721226-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:43:50.721266-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4006, Nexy(5605), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:43:50.721298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:43:50.721343-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4006, Nexy(5605), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:43:50.721362-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.721389-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:43:50.721400-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 7 starting playing
default	20:43:50.721509-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:43:50.721544-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:43:50.721617-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4006, Nexy(5605), 'prim'', displayID:'com.nexy.assistant'}
default	20:43:50.721538-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.721590-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.721645-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 7, PID = 5605, Name = sid:0x1f4006, Nexy(5605), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:43:50.721676-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:43:50.721817-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:43:50.721833-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:43:50.721865-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	20:43:50.721713-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f4006 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5605}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4006, sessionType: 'prim', isRecording: false }, 
]
default	20:43:50.723006-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.723107-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.723131-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:43:50.723145-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:43:50.723155-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:43:50.723166-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	20:43:50.723225-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:43:50.833319-0500	find_contacts_by_name_swift	[0x1014a7c10] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:50.833841-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5660.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:50.833926-0500	find_contacts_by_name_swift	[0x1014a86b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:43:50.833986-0500	find_contacts_by_name_swift	[0x1014a8c70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:43:50.835407-0500	find_contacts_by_name_swift	[0x1014a83e0] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:43:50.835609-0500	find_contacts_by_name_swift	[0x78ac54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:50.836041-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5660.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:50.867403-0500	tccd	AUTHREQ_SUBJECT: msgID=5660.2, subject=com.nexy.assistant,
default	20:43:50.871243-0500	tccd	AUTHREQ_SUBJECT: msgID=5660.1, subject=com.nexy.assistant,
default	20:43:50.872622-0500	find_contacts_by_name_swift	[0x78ac54000] invalidated after the last release of the connection object
default	20:43:50.872739-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:50.876419-0500	find_contacts_by_name_swift	[0x1014a7c10] invalidated after the last release of the connection object
default	20:43:50.876439-0500	find_contacts_by_name_swift	[0x78ac54000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:50.876539-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	20:43:50.876740-0500	find_contacts_by_name_swift	[0x78ac54140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:50.876805-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5660.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:50.877182-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5660.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:50.877862-0500	tccd	AUTHREQ_SUBJECT: msgID=5660.3, subject=com.nexy.assistant,
default	20:43:50.878374-0500	tccd	AUTHREQ_SUBJECT: msgID=5660.4, subject=com.nexy.assistant,
default	20:43:50.878475-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	20:43:50.879071-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:50.894390-0500	find_contacts_by_name_swift	[0x78ac54000] invalidated after the last release of the connection object
default	20:43:50.897994-0500	find_contacts_by_name_swift	[0x78ac54140] invalidated after the last release of the connection object
default	20:43:50.898168-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	20:43:50.898185-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	20:43:50.898200-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	20:43:50.899576-0500	find_contacts_by_name_swift	[0x78ac54000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:50.904139-0500	find_contacts_by_name_swift	[0x78ac54140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:43:50.905086-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:43:50.905153-0500	find_contacts_by_name_swift	<private> 0x78ac40640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:43:50.905175-0500	find_contacts_by_name_swift	<private> 0x78ac40640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:43:50.905816-0500	find_contacts_by_name_swift	[0x78ac54280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:43:50.906234-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5660.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	20:43:50.907246-0500	tccd	AUTHREQ_SUBJECT: msgID=5660.5, subject=com.nexy.assistant,
default	20:43:50.907835-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:50.923624-0500	find_contacts_by_name_swift	[0x78ac54280] invalidated after the last release of the connection object
default	20:43:50.923659-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:43:50.929310-0500	find_contacts_by_name_swift	[0x78ac54280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:50.929868-0500	find_contacts_by_name_swift	[0x78ac54280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:50.929903-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:50.930013-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:50.932351-0500	find_contacts_by_name_swift	[0x78ac56d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:50.933070-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1129, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:50.933099-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:50.934125-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1129, subject=com.nexy.assistant,
default	20:43:50.934725-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:50.951080-0500	find_contacts_by_name_swift	[0x78ac56d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:50.951134-0500	find_contacts_by_name_swift	[0x78ac56d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:50.951181-0500	find_contacts_by_name_swift	[0x78ac56e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:50.951802-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1130, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:50.951836-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:50.952770-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1130, subject=com.nexy.assistant,
default	20:43:50.953341-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:50.969095-0500	find_contacts_by_name_swift	[0x78ac56e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:50.969132-0500	find_contacts_by_name_swift	[0x78ac56e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:50.969161-0500	find_contacts_by_name_swift	[0x78ac56f80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:50.969731-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1131, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:50.969757-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:50.970618-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1131, subject=com.nexy.assistant,
default	20:43:50.971172-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:50.986773-0500	find_contacts_by_name_swift	[0x78ac56f80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:50.986805-0500	find_contacts_by_name_swift	[0x78ac56f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:50.986835-0500	find_contacts_by_name_swift	[0x78ac570c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:50.987391-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1132, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:50.987421-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:50.988259-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1132, subject=com.nexy.assistant,
default	20:43:50.988796-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.004334-0500	find_contacts_by_name_swift	[0x78ac570c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.004370-0500	find_contacts_by_name_swift	[0x78ac570c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.010103-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:51.010113-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:51.010204-0500	find_contacts_by_name_swift	[0x78ac57700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:43:51.011013-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	20:43:51.011327-0500	find_contacts_by_name_swift	0x78ac585e0: Using cached account information
default	20:43:51.011521-0500	find_contacts_by_name_swift	[0x78b08d4a0] Session created.
default	20:43:51.011527-0500	find_contacts_by_name_swift	[0x78b08d4a0] Session created with Mach Service: <private>
default	20:43:51.011533-0500	find_contacts_by_name_swift	[0x78ac57840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:43:51.011590-0500	find_contacts_by_name_swift	[0x78b08d4a0] Session activated
default	20:43:51.013281-0500	find_contacts_by_name_swift	[0x78ac57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.013286-0500	find_contacts_by_name_swift	[0x78b08d4a0] Session canceled.
default	20:43:51.013309-0500	find_contacts_by_name_swift	[0x78b08d4a0] Disposing of session
default	20:43:51.013499-0500	find_contacts_by_name_swift	[0x78ac57840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:51.013906-0500	find_contacts_by_name_swift	[0x78ac57840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.013923-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:51.013942-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:51.016058-0500	find_contacts_by_name_swift	[0x78ae2e300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.016716-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1133, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.016752-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.017766-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1133, subject=com.nexy.assistant,
default	20:43:51.018340-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.034862-0500	find_contacts_by_name_swift	[0x78ae2e300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.034895-0500	find_contacts_by_name_swift	[0x78ae2e300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.034928-0500	find_contacts_by_name_swift	[0x78ae2e440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.035551-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1134, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.035579-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.036540-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1134, subject=com.nexy.assistant,
default	20:43:51.037122-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.053318-0500	find_contacts_by_name_swift	[0x78ae2e440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.053355-0500	find_contacts_by_name_swift	[0x78ae2e440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.053386-0500	find_contacts_by_name_swift	[0x78ae2e580] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.054008-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1135, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.054035-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.054912-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1135, subject=com.nexy.assistant,
default	20:43:51.055468-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.071718-0500	find_contacts_by_name_swift	[0x78ae2e580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.071765-0500	find_contacts_by_name_swift	[0x78ae2e580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.071796-0500	find_contacts_by_name_swift	[0x78ae2e6c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.072484-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1136, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.072523-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.073430-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1136, subject=com.nexy.assistant,
default	20:43:51.073998-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.090101-0500	find_contacts_by_name_swift	[0x78ae2e6c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.090131-0500	find_contacts_by_name_swift	[0x78ae2e800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.095843-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:51.095861-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:43:51.095925-0500	find_contacts_by_name_swift	[0x78ae2e940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:43:51.096330-0500	find_contacts_by_name_swift	[0x78ae2e940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.096343-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:51.096354-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	20:43:51.098484-0500	find_contacts_by_name_swift	[0x78ae51400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.099184-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1137, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.099212-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.100177-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1137, subject=com.nexy.assistant,
default	20:43:51.100754-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.117146-0500	find_contacts_by_name_swift	[0x78ae51400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.117182-0500	find_contacts_by_name_swift	[0x78ae51400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.117218-0500	find_contacts_by_name_swift	[0x78ae51540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.117876-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1138, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.117906-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.118844-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1138, subject=com.nexy.assistant,
default	20:43:51.119429-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.135504-0500	find_contacts_by_name_swift	[0x78ae51540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.135540-0500	find_contacts_by_name_swift	[0x78ae51540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.135572-0500	find_contacts_by_name_swift	[0x78ae51680] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.136213-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1139, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.136245-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.137130-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1139, subject=com.nexy.assistant,
default	20:43:51.137705-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.154023-0500	find_contacts_by_name_swift	[0x78ae51680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.154059-0500	find_contacts_by_name_swift	[0x78ae51680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.154093-0500	find_contacts_by_name_swift	[0x78ae517c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:43:51.154206-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:43:51.154313-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:43:51.154834-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1140, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.154865-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.155814-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1140, subject=com.nexy.assistant,
default	20:43:51.156405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.172653-0500	find_contacts_by_name_swift	[0x78ae517c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.172687-0500	find_contacts_by_name_swift	[0x78ae517c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:43:51.173533-0500	find_contacts_by_name_swift	Did add XPC store
default	20:43:51.173549-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:43:51.180634-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1141, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.180663-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.181674-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1141, subject=com.nexy.assistant,
default	20:43:51.182260-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.200328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96748.1142, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:43:51.200364-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=96748, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=5660, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	20:43:51.201236-0500	tccd	AUTHREQ_SUBJECT: msgID=96748.1142, subject=com.nexy.assistant,
default	20:43:51.201805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	20:43:51.245558-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	20:43:51.245573-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	20:43:51.245686-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	20:43:51.254079-0500	find_contacts_by_name_swift	decoratedContacts called with 1 contacts
default	20:43:51.254098-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	20:43:51.254120-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	20:43:51.254126-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	20:43:51.254131-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	20:43:51.254149-0500	find_contacts_by_name_swift	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	20:43:51.254287-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	20:43:51.254336-0500	find_contacts_by_name_swift	0000 Time spent in client code: 118 µs
default	20:43:51.254352-0500	find_contacts_by_name_swift	0000 FINISH (356 ms)
default	20:43:51.254482-0500	find_contacts_by_name_swift	Entering exit handler.
default	20:43:51.254491-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:43:51.254523-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:43:51.254528-0500	find_contacts_by_name_swift	[0x78ac57700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:43:51.254540-0500	find_contacts_by_name_swift	Exiting exit handler.
default	20:43:51.254559-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	20:43:51.352267-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5661.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=5661, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:43:51.353780-0500	tccd	AUTHREQ_SUBJECT: msgID=5661.1, subject=com.nexy.assistant,
default	20:43:51.354644-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:51.375366-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.357, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5605, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=5661, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:43:51.376218-0500	tccd	AUTHREQ_SUBJECT: msgID=395.357, subject=com.nexy.assistant,
default	20:43:51.376880-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:51.428078-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5200 at /Applications/Nexy.app
default	20:43:51.456316-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 618: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 adb90200 };
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
default	20:43:51.474210-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:43:52.703963-0500	Nexy	[com.apple.controlcenter:6684C63C-1445-4A95-B200-8F844BEB2E7D] Sending action(s) in update: NSSceneFenceAction
default	20:43:53.416800-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:56.418219-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	20:43:59.392256-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
