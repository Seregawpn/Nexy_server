default	22:05:06.721662-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	22:05:06.721831-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	22:05:06.723592-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	22:05:06.743060-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54571778.54571787(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	22:05:06.743151-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54571778.54571787(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:85540] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:402-85540-70158 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	22:05:06.743266-0500	runningboardd	Assertion 402-85540-70158 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) will be created as active
default	22:05:06.746400-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	22:05:06.746431-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.54571778.54571787(501)>
default	22:05:06.746443-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	22:05:06.746519-0500	runningboardd	app<application.com.nexy.assistant.54571778.54571787(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	22:05:06.728308-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	22:05:06.792680-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] is not RunningBoard jetsam managed.
default	22:05:06.792707-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] This process will not be managed.
default	22:05:06.792722-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:05:06.792922-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:06.799247-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] reported to RB as running
default	22:05:06.817924-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	22:05:06.815711-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:06.820368-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:06.835006-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:06.835026-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:06.835041-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:06.835064-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:06.856657-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:06.911160-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:06.932246-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	22:05:06.934500-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=495.35, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=495, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	22:05:06.945348-0500	tccd	AUTHREQ_SUBJECT: msgID=495.35, subject=com.nexy.assistant,
default	22:05:06.946774-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	22:05:06.969326-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	22:05:06.980981-0500	kernel	Nexy[89561] triggered unnest of range 0x1fa000000->0x1fc000000 of DYLD shared region in VM map 0x3c8313da89f86449. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	22:05:06.981005-0500	kernel	Nexy[89561] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x3c8313da89f86449. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	22:05:07.289931-0500	Nexy	[0x106b11c20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	22:05:07.290033-0500	Nexy	[0x106b12160] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	22:05:07.574994-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x106b00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:05:07.575270-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x106b00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:05:07.575517-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x106b00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:05:07.575752-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x106b00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	22:05:07.577066-0500	Nexy	[0x106b00890] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	22:05:07.577756-0500	Nexy	[0xbcd78c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	22:05:07.578083-0500	Nexy	[0xbcd78c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	22:05:07.578623-0500	Nexy	[0xbcd78c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	22:05:07.580836-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	22:05:07.581140-0500	Nexy	Received configuration update from daemon (initial)
default	22:05:07.581233-0500	Nexy	[0xbcd78c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:05:07.582169-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:05:07.583838-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.1, subject=com.nexy.assistant,
default	22:05:07.584723-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	22:05:07.602288-0500	Nexy	[0xbcd78c3c0] invalidated after the last release of the connection object
default	22:05:07.602550-0500	Nexy	server port 0x00003513, session port 0x00003513
default	22:05:07.603590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2449, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:05:07.603626-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:05:07.605998-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2449, subject=com.nexy.assistant,
default	22:05:07.606924-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	22:05:07.634655-0500	Nexy	New connection 0x87bc3 main
default	22:05:07.637373-0500	Nexy	CHECKIN: pid=89561
default	22:05:07.651618-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:89561" ID:402-365-70161 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	22:05:07.651751-0500	runningboardd	Assertion 402-365-70161 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:05:07.651947-0500	Nexy	CHECKEDIN: pid=89561 asn=0x0-0x5a15a1 foreground=0
default	22:05:07.652159-0500	runningboardd	Invalidating assertion 402-365-70160 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.coreservices.launchservicesd>:365]
default	22:05:07.651751-0500	launchservicesd	CHECKIN:0x0-0x5a15a1 89561 com.nexy.assistant
default	22:05:07.652272-0500	Nexy	[0xbcd78c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	22:05:07.652285-0500	Nexy	[0xbcd78c3c0] Connection returned listener port: 0x4f03
default	22:05:07.652607-0500	Nexy	[0xbcca3c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xbcd78c3c0.peer[365].0xbcca3c300
default	22:05:07.655144-0500	Nexy	FRONTLOGGING: version 1
default	22:05:07.653204-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	22:05:07.655155-0500	Nexy	Registered, pid=89561 ASN=0x0,0x5a15a1
default	22:05:07.653347-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	22:05:07.655664-0500	WindowServer	87bc3[CreateApplication]: Process creation: 0x0-0x5a15a1 (Nexy) connectionID: 87BC3 pid: 89561 in session 0x101
default	22:05:07.656670-0500	Nexy	[0xbcd78c640] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	22:05:07.676206-0500	Nexy	[0xbcd78c3c0] Connection returned listener port: 0x4f03
default	22:05:07.677002-0500	Nexy	BringForward: pid=89561 asn=0x0-0x5a15a1 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	22:05:07.677057-0500	Nexy	BringFrontModifier: pid=89561 asn=0x0-0x5a15a1 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	22:05:07.677849-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	22:05:07.680186-0500	Nexy	No persisted cache on this platform.
default	22:05:07.681679-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	22:05:07.682449-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	22:05:07.686496-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	22:05:07.686510-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	22:05:07.686587-0500	Nexy	Initializing connection
default	22:05:07.686638-0500	Nexy	Removing all cached process handles
default	22:05:07.686662-0500	Nexy	Sending handshake request attempt #1 to server
default	22:05:07.686672-0500	Nexy	Creating connection to com.apple.runningboard
default	22:05:07.686682-0500	Nexy	[0xbcd78c8c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	22:05:07.687262-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] as ready
default	22:05:07.688011-0500	Nexy	Handshake succeeded
default	22:05:07.688031-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.54571778.54571787(501)>
default	22:05:07.694077-0500	Nexy	[0xbcd78c3c0] Connection returned listener port: 0x4f03
default	22:05:07.695245-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 89561
default	22:05:07.697815-0500	Nexy	[0xbcd78c3c0] Connection returned listener port: 0x4f03
default	22:05:07.702424-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	22:05:07.702572-0500	Nexy	[0xbcd78c780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	22:05:07.702760-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	22:05:07.702903-0500	Nexy	[0xbcd78ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	22:05:07.704502-0500	Nexy	[0xbcd78ca00] Connection returned listener port: 0x6503
default	22:05:07.705610-0500	Nexy	Registered process with identifier 89561-1334839
default	22:05:09.300738-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0A80A247-DCDA-4CC1-9D8D-3CFD6B55E18F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53281,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xa7e86118 tp_proto=0x06"
default	22:05:09.300857-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53281<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579456 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xafb53de1
default	22:05:12.740853-0500	runningboardd	Assertion did invalidate due to timeout: 402-402-70159 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561])
default	22:05:12.924248-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:12.924280-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:12.924302-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:12.924336-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:12.930269-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:12.931104-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:14.301970-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53281<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579456 t_state: SYN_SENT process: Nexy:89561 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xafb53de1
default	22:05:14.302001-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53281<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579456 t_state: SYN_SENT process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:05:14.302725-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 96B6DA9B-5688-4F8A-9D03-30D50D6FB98A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53282,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x31132319 tp_proto=0x06"
default	22:05:14.302875-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579463 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99fb7bfb
default	22:05:17.415822-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	22:05:18.672812-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	22:05:19.302831-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579463 t_state: SYN_SENT process: Nexy:89561 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x99fb7bfb
default	22:05:19.302864-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53282<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579463 t_state: SYN_SENT process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:05:19.309842-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	22:05:19.311042-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	22:05:19.313363-0500	Nexy	nw_path_libinfo_path_check [CDDDCBCD-7A17-446C-ADCC-0C381D876C9F Hostname#b53a26e5:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:05:19.313899-0500	mDNSResponder	[R157885] DNSServiceCreateConnection START PID[89561](Nexy)
default	22:05:19.314018-0500	mDNSResponder	[R157886] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 89561 (Nexy), name hash: f92d5498
default	22:05:19.314754-0500	mDNSResponder	[R157887] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 89561 (Nexy), name hash: f92d5498
default	22:05:19.339498-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 11EDCBB5-3307-4E43-83A6-93897D69D80C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53284,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x46c599d6 tp_proto=0x06"
default	22:05:19.339644-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579509 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x82e09f4f
default	22:05:24.304368-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579509 t_state: SYN_SENT process: Nexy:89561 Duration: 4.965 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0x82e09f4f
default	22:05:24.304404-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53284<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579509 t_state: SYN_SENT process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/12 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:05:25.463502-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	22:05:25.464445-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	22:05:25.466645-0500	Nexy	[0xbcd78cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	22:05:25.478262-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
default	22:05:25.483266-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	22:05:25.486130-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	22:05:25.486287-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	22:05:25.486419-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	22:05:25.486432-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	22:05:25.486896-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	22:05:25.487027-0500	Nexy	[0xbcd78cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	22:05:25.488241-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:05:25.487318-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	22:05:25.503674-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.2, subject=com.nexy.assistant,
default	22:05:25.504503-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:25.519531-0500	Nexy	[0xbcd78cf00] invalidated after the last release of the connection object
default	22:05:25.519612-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	22:05:25.522986-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	22:05:25.527360-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1937, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:25.528465-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1937, subject=com.nexy.assistant,
default	22:05:25.529087-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
error	22:05:25.542327-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=406, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	22:05:25.543267-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1939, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:25.544435-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1939, subject=com.nexy.assistant,
default	22:05:25.545180-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:25.565305-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	22:05:25.565566-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xbcbb6aac0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	22:05:25.587387-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:25.587529-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:25.592194-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	22:05:25.597589-0500	Nexy	[0xbcd78cf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	22:05:25.609117-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbcb684040) Selecting device 85 from constructor
default	22:05:25.609127-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:25.609133-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:25.609445-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbcb684040) nothing to teardown
default	22:05:25.609452-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbcb684040) connecting device 85
default	22:05:25.609533-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbcb684040) Device ID: 85 (Input:No | Output:Yes): true
default	22:05:25.609628-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbcb684040) created ioproc 0xa for device 85
default	22:05:25.609735-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 7 device listeners to device 85
default	22:05:25.609908-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 85
default	22:05:25.609918-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbcb684040)
default	22:05:25.609985-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:05:25.609993-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:05:25.610001-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:05:25.610008-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:05:25.610014-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:05:25.610106-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:05:25.610119-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:05:25.610124-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:05:25.610131-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device listeners from device 0
default	22:05:25.610137-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 0
default	22:05:25.610141-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:25.610152-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	22:05:25.610227-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbcb684040) caller requesting device change from 85 to 91
default	22:05:25.610234-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:25.610238-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:25.610240-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbcb684040) disconnecting device 85
default	22:05:25.610244-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbcb684040) destroying ioproc 0xa for device 85
default	22:05:25.610291-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	22:05:25.611352-0500	Nexy	[0xbcd78d180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	22:05:25.613337-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":{"PID":89561,"session_type":"Primary"} }
default	22:05:25.613430-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":89561}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f406a, sessionType: 'prim', isRecording: false }, 
]
default	22:05:25.614032-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 89561, name = Nexy
default	22:05:25.614269-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xbcca5b780 with ID: 0x1f406a
default	22:05:25.615259-0500	Nexy	[0xbcd78d2c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	22:05:25.615567-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=384661565997057 }
default	22:05:25.615582-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	22:05:25.615627-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:05:25.615708-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbcb684040) connecting device 91
default	22:05:25.615781-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbcb684040) Device ID: 91 (Input:Yes | Output:No): true
default	22:05:25.616899-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1940, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:25.618133-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1940, subject=com.nexy.assistant,
default	22:05:25.619023-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:25.636307-0500	tccd	AUTHREQ_PROMPTING: msgID=406.1940, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	22:05:27.501877-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	22:05:27.502831-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbcb684040) created ioproc 0xa for device 91
default	22:05:27.503103-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 7 device listeners to device 91
default	22:05:27.503410-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 91
default	22:05:27.503426-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbcb684040)
default	22:05:27.503439-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	22:05:27.503458-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:05:27.503680-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	22:05:27.503693-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	22:05:27.503700-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	22:05:27.503839-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:05:27.503854-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:05:27.503863-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:05:27.503870-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 7 device listeners from device 85
default	22:05:27.504112-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 85
default	22:05:27.504125-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:27.504748-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:05:27.504574-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	22:05:27.506612-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1941, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:27.508796-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1941, subject=com.nexy.assistant,
default	22:05:27.509859-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:27.539361-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	22:05:27.539457-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	22:05:27.539585-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb557240, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	22:05:27.539906-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:05:27.541261-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1942, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:27.547841-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1942, subject=com.nexy.assistant,
default	22:05:27.549894-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:27.574287-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1943, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:27.575527-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1943, subject=com.nexy.assistant,
default	22:05:27.576280-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:27.596788-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	22:05:27.597187-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:05:27.597353-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	22:05:27.597354-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	22:05:27.598913-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:05:27.600598-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	22:05:27.601003-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:27.601063-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:27.697225-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	22:05:27.700294-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4371 called from <private>
default	22:05:27.700335-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	22:05:27.703792-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:27.702975-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	22:05:27.703625-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:05:27.703906-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70197 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:05:27.704102-0500	runningboardd	Assertion 402-336-70197 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:05:27.703859-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:27.704241-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:27.704345-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:27.704507-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:27.704035-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406a, Nexy(89561), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	22:05:27.700385-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:05:27.702214-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:27.702342-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:27.702368-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:27.704915-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:27.704756-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	22:05:27.705049-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:27.705171-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:27.705439-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:27.705487-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:27.705463-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:27.704819-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406a, Nexy(89561), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 107 starting recording
default	22:05:27.705630-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:27.704984-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:27.705327-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
fault	22:05:27.705769-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
default	22:05:27.705992-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:27.702409-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:27.704900-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:27.706151-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:05:27.705167-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:27.705794-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:27.705210-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:27.705255-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:27.706445-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	22:05:27.706496-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:05:27.706238-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406a, Nexy(89561), 'prim'', displayID:'com.nexy.assistant'}
default	22:05:27.706901-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:05:27.709372-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:27.709454-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:27.709489-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	22:05:27.709518-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	22:05:27.709564-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
fault	22:05:27.710280-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
default	22:05:27.706413-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:05:27.709671-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:05:27.707436-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1944, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:27.709172-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:27.714462-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:27.715146-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:27.714853-0500	runningboardd	Invalidating assertion 402-336-70197 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.powerd>:336]
default	22:05:27.716243-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1944, subject=com.nexy.assistant,
default	22:05:27.717044-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:27.727195-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:05:27.727322-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	22:05:27.727369-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:27.727550-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:27.730079-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.730092-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.730103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:27.730109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.730118-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:27.730128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:27.730739-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:05:27.734440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.734466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.734483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:27.734491-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:27.734498-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:27.734504-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:27.734639-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
error	22:05:27.740434-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:05:27.740467-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:27.802129-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:27.802162-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:27.802170-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:27.805015-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:27.805035-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:27.805038-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:27.805047-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:27.805049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:27.805130-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:27.808680-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:27.808691-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:27.808279-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1945, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:27.808866-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:27.808881-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:27.808887-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:27.812202-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1945, subject=com.nexy.assistant,
default	22:05:27.813256-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:27.813277-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:27.813282-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:27.813301-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:27.817208-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:27.817215-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:27.817224-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:27.822329-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:27.822376-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:27.822412-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:27.822518-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:27.817352-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:27.817451-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:27.817579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:27.817626-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:27.821820-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:27.821866-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:27.826634-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:27.837162-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:27.837177-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:27.837268-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:27.841851-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:27.841341-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:27.842216-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:27.843228-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:27.842226-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:27.842350-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:27.848014-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:27.848288-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:27.848313-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:27.848356-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:27.848368-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:27.848375-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:27.848380-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:27.848385-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:27.848427-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:27.848553-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:27.848608-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:27.867552-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	22:05:27.867665-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:27.867791-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:05:27.867834-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406a, Nexy(89561), 'prim'', displayID:'com.nexy.assistant'}
default	22:05:27.867888-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:05:27.867908-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406a, Nexy(89561), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 107 stopping recording
default	22:05:27.867990-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:27.868000-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:27.867933-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	22:05:27.867960-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:27.868199-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:05:27.868088-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:27.868103-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4371 called from <private>
default	22:05:27.868109-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4371 called from <private>
default	22:05:27.868051-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:27.868304-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	22:05:27.868313-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:05:27.868573-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:27.921098-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:27.921119-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:27.921127-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:27.924122-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:27.924158-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:27.924165-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:27.981013-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbcb684040) Selecting device 0 from destructor
default	22:05:27.981029-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:27.981033-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:27.981036-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbcb684040) disconnecting device 91
default	22:05:27.981040-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbcb684040) destroying ioproc 0xa for device 91
default	22:05:27.981060-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	22:05:27.981081-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:05:27.981162-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbcb684040) nothing to setup
default	22:05:27.981169-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device listeners to device 0
default	22:05:27.981174-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 0
default	22:05:27.981178-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 7 device listeners from device 91
default	22:05:27.981336-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 91
default	22:05:27.981347-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:29.900731-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:29.900804-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:29.900825-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:29.902170-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:29.902219-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:29.902237-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:29.922569-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:29.922600-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:29.932265-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:29.932292-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:29.932389-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:29.933187-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:29.933360-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:29.933371-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:29.933471-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:29.938162-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:29.938360-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:29.938371-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:29.938406-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:29.938415-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:29.938421-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:29.938427-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:29.938432-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:29.938483-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:29.938581-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:29.938652-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:29.938747-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:29.938884-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:29.939093-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:29.939129-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:29.939192-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:29.944962-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:29.945132-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:29.945142-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:29.945154-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:29.945163-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:30.023570-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:30.023627-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:30.023648-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:30.023653-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:30.023660-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:30.023673-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:40.985975-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbcb684040) Selecting device 85 from constructor
default	22:05:40.986015-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:40.986032-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:40.986046-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbcb684040) nothing to teardown
default	22:05:40.986057-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbcb684040) connecting device 85
default	22:05:40.986299-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbcb684040) Device ID: 85 (Input:No | Output:Yes): true
default	22:05:40.986571-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbcb684040) created ioproc 0xb for device 85
default	22:05:40.986877-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 7 device listeners to device 85
default	22:05:40.987356-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 85
default	22:05:40.987385-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbcb684040)
default	22:05:40.987582-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:05:40.987603-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:05:40.987622-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:05:40.987641-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:05:40.987662-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:05:40.987922-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:05:40.987951-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:05:40.987967-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:05:40.987981-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device listeners from device 0
default	22:05:40.987992-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 0
default	22:05:40.988003-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:40.988032-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	22:05:40.988168-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbcb684040) caller requesting device change from 85 to 91
default	22:05:40.988192-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:40.988207-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:40.988221-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbcb684040) disconnecting device 85
default	22:05:40.988234-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbcb684040) destroying ioproc 0xb for device 85
default	22:05:40.988297-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	22:05:40.988379-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:05:40.988571-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbcb684040) connecting device 91
default	22:05:40.988763-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbcb684040) Device ID: 91 (Input:Yes | Output:No): true
default	22:05:40.991533-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1946, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:40.993953-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1946, subject=com.nexy.assistant,
default	22:05:40.995062-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.022152-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbcb684040) created ioproc 0xb for device 91
default	22:05:41.022327-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 7 device listeners to device 91
default	22:05:41.022521-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 91
default	22:05:41.022531-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbcb684040)
default	22:05:41.022543-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	22:05:41.022556-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:05:41.022705-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	22:05:41.022712-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	22:05:41.022718-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	22:05:41.022821-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:05:41.022831-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:05:41.022836-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:05:41.022841-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 7 device listeners from device 85
default	22:05:41.023011-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 85
default	22:05:41.023019-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:41.023031-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	22:05:41.023394-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:05:41.024730-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1947, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.026025-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1947, subject=com.nexy.assistant,
default	22:05:41.026702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.045064-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb557330, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	22:05:41.045342-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:05:41.046785-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1948, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.048089-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1948, subject=com.nexy.assistant,
default	22:05:41.048739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.069365-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1949, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.070569-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1949, subject=com.nexy.assistant,
default	22:05:41.071213-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.090079-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:05:41.090218-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	22:05:41.091543-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4371 called from <private>
default	22:05:41.091578-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:05:41.091579-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:05:41.092319-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:41.093732-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70204 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:05:41.092483-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.093806-0500	runningboardd	Assertion 402-336-70204 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:05:41.092508-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.093914-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:41.094223-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:41.094285-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:41.094337-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:41.094420-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:41.094317-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:41.092514-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.094862-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.095132-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.095140-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.095153-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.095565-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	22:05:41.095634-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:05:41.095662-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406a, Nexy(89561), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:05:41.095690-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:41.095741-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406a, Nexy(89561), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	22:05:41.095854-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:41.095968-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:41.095980-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096065-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	22:05:41.096112-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406a, Nexy(89561), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 107 starting recording
default	22:05:41.096110-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096092-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096143-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096271-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:41.096234-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096349-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:05:41.096568-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1950, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.096302-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.096573-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	22:05:41.096451-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406a, Nexy(89561), 'prim'', displayID:'com.nexy.assistant'}
default	22:05:41.096582-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:05:41.096560-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:05:41.096787-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:05:41.097831-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.097903-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.097925-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.097935-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	22:05:41.097944-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	22:05:41.097979-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	22:05:41.098151-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:05:41.098417-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1950, subject=com.nexy.assistant,
default	22:05:41.099054-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.100846-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:41.101103-0500	runningboardd	Invalidating assertion 402-336-70204 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.powerd>:336]
default	22:05:41.101429-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:41.104372-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:05:41.104446-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	22:05:41.104510-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.104648-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.105242-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.105251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.105259-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.105268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.105273-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.105279-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.105355-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:05:41.117518-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:05:41.118923-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:41.118983-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:41.187964-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
error	22:05:41.188313-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:05:41.188342-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:41.189030-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:41.189043-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:41.189138-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.189157-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.189163-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.189682-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:41.189829-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:41.190129-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.190260-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.190273-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.190285-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.191694-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1951, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.194051-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.194071-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:41.194077-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:41.194463-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.194478-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.192991-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1951, subject=com.nexy.assistant,
default	22:05:41.194489-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.194499-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.195244-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.195316-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.195339-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.201678-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:41.201687-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:41.201823-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.201841-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:41.201848-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:41.203486-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.205372-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.205390-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:41.205396-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:41.207559-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:41.207567-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:41.208486-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.208498-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:41.208729-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:41.212243-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.212301-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:41.212631-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:41.213690-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:41.213852-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:41.214135-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.214205-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:41.214255-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:41.215261-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.215316-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.215481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:41.215538-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:41.215596-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.216305-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:41.216382-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:41.216427-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:41.216494-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:41.215681-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:41.215734-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:41.215827-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:41.215889-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:41.254316-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:41.215930-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:41.272514-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:05:41.272667-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
error	22:05:41.273233-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:05:41.273261-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:41.273271-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:41.273278-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:41.273288-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.274961-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1952, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.276283-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1952, subject=com.nexy.assistant,
default	22:05:41.276948-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.296183-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:05:41.297406-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:41.297472-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:05:41.316905-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.316937-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:41.316945-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:41.331545-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	22:05:41.331736-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.331845-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:41.331856-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
error	22:05:41.331867-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:05:41.331878-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.331885-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.331891-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.331897-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.331903-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.331908-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.331914-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.331919-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.331927-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.331959-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.331995-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.332122-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.332636-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:05:41.332750-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:41.333034-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.333200-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.333215-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.333230-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.333941-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:41.333950-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:41.334034-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:41.334171-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:41.334285-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:41.334295-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:41.334316-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:41.334321-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:41.334330-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:41.334336-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:41.334652-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1953, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.335772-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1953, subject=com.nexy.assistant,
default	22:05:41.336364-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.357213-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4371 called from <private>
default	22:05:41.357247-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4371 called from <private>
default	22:05:41.357404-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:05:41.358495-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70205 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:05:41.358669-0500	runningboardd	Assertion 402-336-70205 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:05:41.359025-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:41.359055-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:41.359092-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:41.359184-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:41.360549-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:41.360564-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.360826-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:41.361872-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
error	22:05:41.360934-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:05:41.362381-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:05:41.360941-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.360954-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:41.361063-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:41.361079-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4371 called from <private>
default	22:05:41.361085-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4371 called from <private>
default	22:05:41.362910-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:41.363332-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4371 called from <private>
default	22:05:41.363341-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4371 called from <private>
default	22:05:41.363352-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:41.364723-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1954, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:05:41.365829-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1954, subject=com.nexy.assistant,
default	22:05:41.366138-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:41.366560-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:41.366466-0500	runningboardd	Invalidating assertion 402-336-70205 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.powerd>:336]
default	22:05:41.366516-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:05:41.367904-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:05:41.367952-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	22:05:41.367986-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.368077-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.368642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.368650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.368670-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.368679-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.368686-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.368707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.368906-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:05:41.386306-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70206 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:05:41.387491-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4371 called from <private>
default	22:05:41.388290-0500	runningboardd	Assertion 402-336-70206 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:05:41.396576-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:05:41.396637-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	22:05:41.396675-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.397310-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397339-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.397347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.397368-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.397419-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.397517-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.397572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.397629-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.397774-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:05:41.398293-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	22:05:41.398397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.398408-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.398417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.398426-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.398432-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.398439-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.527728-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:05:41.527980-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	22:05:41.528054-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:41.528099-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:05:41.528124-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406a, Nexy(89561), 'prim'', displayID:'com.nexy.assistant'}
default	22:05:41.528162-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406a, Nexy(89561), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 107 stopping recording
default	22:05:41.528175-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:05:41.528184-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	22:05:41.528214-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:05:41.528280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:05:41.528455-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:05:41.528429-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	22:05:41.528445-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:05:41.530246-0500	runningboardd	Invalidating assertion 402-336-70206 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.powerd>:336]
default	22:05:41.530432-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.530354-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.530472-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:05:41.530392-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.530503-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:05:41.530563-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.530582-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:05:41.530599-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:05:41.530610-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	22:05:41.531910-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:05:41.532325-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.532336-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.532349-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.532356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:41.532363-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:41.532371-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:41.532507-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:05:41.629448-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbcb684040) Selecting device 0 from destructor
default	22:05:41.629465-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:05:41.629472-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:05:41.629477-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbcb684040) disconnecting device 91
default	22:05:41.629484-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbcb684040) destroying ioproc 0xb for device 91
default	22:05:41.629528-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:05:41.629569-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:05:41.629744-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbcb684040) nothing to setup
default	22:05:41.629757-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device listeners to device 0
default	22:05:41.629765-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 0
default	22:05:41.629772-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 7 device listeners from device 91
default	22:05:41.629960-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 91
default	22:05:41.629972-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:05:41.635015-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:05:41.635029-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:05:41.635039-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:05:41.635056-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:05:41.637900-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:05:41.638534-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:05:44.031888-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4371)
default	22:05:44.031940-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:44.031960-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4371 called from <private>
default	22:05:44.031969-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4371 called from <private>
default	22:05:44.031980-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4370 called from <private>
default	22:05:44.031985-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4370 called from <private>
default	22:05:44.039011-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:44.039042-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:44.039442-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:44.039469-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:44.039477-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:44.040563-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:44.040594-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:44.040610-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:44.040623-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:44.040636-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:44.040646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:44.040652-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:44.040939-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:44.041214-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:44.043977-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:44.044055-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:44.050328-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:44.050357-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:44.064711-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4370 called from <private>
default	22:05:44.064743-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4370 called from <private>
default	22:05:44.064831-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:44.067657-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:44.067899-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4370 called from <private>
default	22:05:44.067912-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4370 called from <private>
default	22:05:44.068078-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4370)
default	22:05:44.072705-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:44.072896-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:44.072905-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:44.072936-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:44.072946-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:44.072952-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:44.072959-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:44.072964-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4370 called from <private>
default	22:05:44.073003-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4370 called from <private>
default	22:05:44.073131-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4370 called from <private>
default	22:05:44.073240-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4370 called from <private>
default	22:05:44.148216-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4371)
default	22:05:44.148278-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4371 called from <private>
default	22:05:44.148288-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4371 called from <private>
default	22:05:44.149606-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4370)
default	22:05:44.149636-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4370 called from <private>
default	22:05:44.149642-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4370 called from <private>
default	22:05:44.639374-0500	Nexy	[0xbcd78d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:05:44.641256-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:05:44.644180-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.3, subject=com.nexy.assistant,
default	22:05:44.645669-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	22:05:44.668222-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[89561], responsiblePID[89561], responsiblePath: /Applications/Nexy.app to UID: 501
default	22:05:44.668603-0500	Nexy	[0xbcd78d680] invalidated after the last release of the connection object
default	22:05:44.850049-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5e00 at /Applications/Nexy.app
default	22:05:44.877259-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4000 at /Applications/Nexy.app
default	22:05:44.877444-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	22:05:44.883408-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	22:05:45.473771-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	22:05:45.479657-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	22:05:45.507416-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	22:05:48.298769-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3694, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=72011, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=72026, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:05:52.165041-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5500 at /Applications/Nexy.app
default	22:05:52.187002-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:05:52.198311-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	22:05:52.353756-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:05:52.357866-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:05:52.389991-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	22:05:52.392966-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	22:05:57.681421-0500	Nexy	[0xbcd78d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:05:57.683484-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:05:57.688513-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.4, subject=com.nexy.assistant,
default	22:05:57.690680-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:05:57.720650-0500	Nexy	[0xbcd78d680] invalidated after the last release of the connection object
default	22:05:57.723341-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	22:05:57.726556-0500	Nexy	[0xbcd78d680] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	22:05:57.726828-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	22:05:57.727412-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:05:57.736310-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:05:57.736340-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:05:57.737389-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.3, subject=com.nexy.assistant,
default	22:05:57.738101-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:05:57.764445-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2473, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:05:57.764472-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:05:57.765327-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2473, subject=com.nexy.assistant,
default	22:05:57.765955-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:05:57.787062-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	22:05:57.816469-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:05:57.816656-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:05:57.816724-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:05:57.820175-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:57.820189-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:57.820214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:57.820225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:05:57.820236-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:05:57.820244-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:05:57.820434-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:06:00.796207-0500	kernel	udp connect: [<IPv4-redacted>:59447<-><IPv4-redacted>:80] interface:  (skipped: 0)
so_gencnt: 1579885 so_state: 0x0102 process: Nexy:89561 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa5233255
default	22:06:00.796365-0500	kernel	udp_connection_summary [<IPv4-redacted>:59447<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1579885 so_state: 0x0102 process: Nexy:89561 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa5233255 flowctl: 0us (0x)
default	22:06:00.797374-0500	Nexy	nw_path_libinfo_path_check [A2D0FDC1-91A3-4467-9646-099863BBBA85 IPv4#b2ff5fdb:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:06:00.798950-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C3AE7015-CEB8-407C-B3CA-F32E06489487 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53324,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd032ab36 tp_proto=0x06"
default	22:06:00.799015-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53324<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579886 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb397e0bb
default	22:06:01.800071-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53324<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579886 t_state: SYN_SENT process: Nexy:89561 Duration: 1.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb397e0bb
default	22:06:01.800085-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53324<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579886 t_state: SYN_SENT process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/2 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:06:01.801728-0500	kernel	tcp listen: [<IPv4-redacted>:53325<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1579888 t_state: LISTEN process: Nexy:89561 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	22:06:01.801829-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53325<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1579888 t_state: LISTEN process: Nexy:89561 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	22:06:01.801836-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53325<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1579888 t_state: LISTEN process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:06:03.614531-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:06:03.614694-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:06:05.200166-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:06:05.200267-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:06:07.889729-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	22:06:14.805397-0500	Nexy	nw_path_libinfo_path_check [3BE18DD9-43F5-4862-98E6-54517EF813D8 IPv4#b2ff5fdb:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:06:14.805886-0500	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4AEF9C1F-5009-4253-9435-506CFE4FD3C0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53327,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x01db0197 tp_proto=0x06"
default	22:06:14.806018-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53327<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579920 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86bc43a4
default	22:06:15.307147-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53327<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579920 t_state: SYN_SENT process: Nexy:89561 Duration: 0.502 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x86bc43a4
default	22:06:15.307182-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53327<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1579920 t_state: SYN_SENT process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:06:18.345777-0500	Nexy	[0xbcd78d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	22:06:18.346329-0500	Nexy	[0xbcd78d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	22:06:18.346937-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:06:18.347014-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:06:18.348860-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.6, subject=com.nexy.assistant,
default	22:06:18.349710-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:18.349741-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.5, subject=com.nexy.assistant,
default	22:06:18.351242-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:06:18.364224-0500	Nexy	[0xbcd78d7c0] invalidated after the last release of the connection object
default	22:06:18.364335-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	22:06:18.365468-0500	Nexy	[0xbcd78d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	22:06:18.365854-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:06:18.366863-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.7, subject=com.nexy.assistant,
default	22:06:18.367497-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:18.367779-0500	Nexy	[0xbcd78d540] invalidated after the last release of the connection object
default	22:06:18.383172-0500	tccd	AUTHREQ_PROMPTING: msgID=89561.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	22:06:20.472178-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	22:06:20.472856-0500	Nexy	[0xbcd78d7c0] invalidated after the last release of the connection object
default	22:06:20.474122-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	22:06:20.478471-0500	Nexy	[0xbcd78d7c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:06:20.480249-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=68009.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=68009, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	22:06:20.482215-0500	tccd	AUTHREQ_SUBJECT: msgID=68009.9, subject=com.nexy.assistant,
default	22:06:20.483302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.509558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=68009.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=68009, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	22:06:20.511060-0500	tccd	AUTHREQ_SUBJECT: msgID=68009.10, subject=com.nexy.assistant,
default	22:06:20.511806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.534167-0500	Nexy	[0xbcd78d540] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	22:06:20.535403-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	22:06:20.535448-0500	Nexy	<private> 0xbcca5c200: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	22:06:20.535470-0500	Nexy	<private> 0xbcca5c200: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	22:06:20.536254-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	22:06:20.546163-0500	Nexy	[0xbcd78d900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:06:20.547678-0500	Nexy	[0xbcd78d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.547738-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:06:20.547982-0500	Nexy	Will add XPC store with options: <private> <private>
default	22:06:20.550846-0500	Nexy	[0xbcd10c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.552156-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3777, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.552191-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.553673-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3777, subject=com.nexy.assistant,
default	22:06:20.554449-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.580467-0500	Nexy	[0xbcd10c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.580624-0500	Nexy	[0xbcd10c3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.580760-0500	Nexy	[0xbcd10c500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.582101-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3778, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.582139-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.583880-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3778, subject=com.nexy.assistant,
default	22:06:20.584830-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.609428-0500	Nexy	[0xbcd10c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.609524-0500	Nexy	[0xbcd10c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.609599-0500	Nexy	[0xbcd10c640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.610718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3779, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.610752-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.612292-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3779, subject=com.nexy.assistant,
default	22:06:20.613071-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.637162-0500	Nexy	[0xbcd10c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.637249-0500	Nexy	[0xbcd10c640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.637317-0500	Nexy	[0xbcd10c780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.638506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3780, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.638547-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.640166-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3780, subject=com.nexy.assistant,
default	22:06:20.640930-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.666572-0500	Nexy	[0xbcd10c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.666657-0500	Nexy	[0xbcd10c780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.681968-0500	Nexy	Did add XPC store
default	22:06:20.681991-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:06:20.686009-0500	Nexy	0xbcccace40: Using cached account information
default	22:06:20.686996-0500	Nexy	[0xbcca4f6b0] Session created.
default	22:06:20.687009-0500	Nexy	[0xbcca4f6b0] Session created with Mach Service: <private>
default	22:06:20.687019-0500	Nexy	[0xbcd10cdc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	22:06:20.687181-0500	Nexy	[0xbcca4f6b0] Session activated
default	22:06:20.690675-0500	Nexy	[0xbcd10cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.690682-0500	Nexy	[0xbcca4f6b0] Session canceled.
default	22:06:20.690696-0500	Nexy	[0xbcca4f6b0] Disposing of session
default	22:06:20.691139-0500	Nexy	[0xbcd10cdc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:06:20.691910-0500	Nexy	[0xbcd10cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.691932-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	22:06:20.691953-0500	Nexy	Will add XPC store with options: <private> <private>
default	22:06:20.697184-0500	Nexy	[0xbcd10f840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.698765-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3781, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.698806-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.700666-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3781, subject=com.nexy.assistant,
default	22:06:20.701515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.730886-0500	Nexy	[0xbcd10f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.730973-0500	Nexy	[0xbcd10f840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.731045-0500	Nexy	[0xbcd10f980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.732278-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3782, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.732311-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.733827-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3782, subject=com.nexy.assistant,
default	22:06:20.734613-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.761399-0500	Nexy	[0xbcd10f980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.761486-0500	Nexy	[0xbcd10f980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.761579-0500	Nexy	[0xbcd10fac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.762789-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3783, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.762830-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.764410-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3783, subject=com.nexy.assistant,
default	22:06:20.765258-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.789959-0500	Nexy	[0xbcd10fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.790047-0500	Nexy	[0xbcd10fac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.790122-0500	Nexy	[0xbcd10fc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.791313-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3784, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.791352-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.792886-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3784, subject=com.nexy.assistant,
default	22:06:20.793679-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.819071-0500	Nexy	[0xbcd10fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.819159-0500	Nexy	[0xbcd10fc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.841419-0500	Nexy	Did add XPC store
default	22:06:20.841464-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	22:06:20.841615-0500	Nexy	[0xbcd10fe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:06:20.842617-0500	Nexy	[0xbcd10fe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.842660-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:06:20.842681-0500	Nexy	Will add XPC store with options: <private> <private>
default	22:06:20.846347-0500	Nexy	[0xbcd136940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.848031-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3785, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.848067-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.849792-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3785, subject=com.nexy.assistant,
default	22:06:20.850588-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.875370-0500	Nexy	[0xbcd136940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.875480-0500	Nexy	[0xbcd136940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.875560-0500	Nexy	[0xbcd136a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.876718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3786, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.876754-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.878621-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3786, subject=com.nexy.assistant,
default	22:06:20.879611-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.909645-0500	Nexy	[0xbcd136a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.909827-0500	Nexy	[0xbcd136a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.909914-0500	Nexy	[0xbcd136bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.911367-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3787, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.911401-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.913156-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3787, subject=com.nexy.assistant,
default	22:06:20.914005-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.940598-0500	Nexy	[0xbcd136bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.940689-0500	Nexy	[0xbcd136bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.940767-0500	Nexy	[0xbcd136d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:06:20.941975-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3788, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:20.942008-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:20.943566-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3788, subject=com.nexy.assistant,
default	22:06:20.944320-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:20.972747-0500	Nexy	[0xbcd136d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:20.972875-0500	Nexy	[0xbcd136d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:06:20.974786-0500	Nexy	Did add XPC store
default	22:06:20.974844-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:06:21.003545-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3789, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:21.003611-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:21.006582-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3789, subject=com.nexy.assistant,
default	22:06:21.008183-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:21.046391-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3790, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:21.046430-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:21.048199-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.3790, subject=com.nexy.assistant,
default	22:06:21.049173-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:06:21.086910-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:06:21.109463-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	22:06:21.109486-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	22:06:21.109520-0500	Nexy	<private> 0xbcca5c200: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	22:06:21.112983-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	22:06:21.113078-0500	Nexy	[0xbcd10c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:21.113092-0500	Nexy	[0xbcd10c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:21.113101-0500	Nexy	[0xbcd10c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:21.113151-0500	Nexy	[0xbcd10c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:06:23.322868-0500	Nexy	[0xbcd1370c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	22:06:34.494298-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89626.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=89626, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	22:06:34.495811-0500	tccd	AUTHREQ_SUBJECT: msgID=89626.1, subject=com.nexy.assistant,
default	22:06:34.496573-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:34.513354-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2488, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=89626, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:06:34.514195-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2488, subject=com.nexy.assistant,
default	22:06:34.514884-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:34.546957-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:34.572922-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 618: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 f25e1400 };
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
default	22:06:34.591505-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:34.601655-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:06:34.619354-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	22:06:36.292511-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:06:36.299660-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	22:06:36.300148-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	22:06:47.493556-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89631.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=89631, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	22:06:47.495311-0500	tccd	AUTHREQ_SUBJECT: msgID=89631.1, subject=com.nexy.assistant,
default	22:06:47.496069-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:47.513456-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2491, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=89631, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:06:47.514333-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2491, subject=com.nexy.assistant,
default	22:06:47.515029-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:47.557346-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:47.585860-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 618: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 005f1400 };
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
default	22:06:47.602727-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	22:06:50.620070-0500	Nexy	[0xbcd137200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:06:50.621872-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:06:50.624620-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.8, subject=com.nexy.assistant,
default	22:06:50.626267-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:50.649419-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[89561], responsiblePID[89561], responsiblePath: /Applications/Nexy.app to UID: 501
default	22:06:50.649867-0500	Nexy	[0xbcd137200] invalidated after the last release of the connection object
default	22:06:50.696435-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5500 at /Applications/Nexy.app
default	22:06:50.716454-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:06:50.720611-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	22:06:52.762453-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:06:52.788197-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	22:06:53.333828-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:06:53.403146-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	22:06:53.835129-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:06:53.835187-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	22:06:53.835728-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	22:06:53.951786-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:06:53.952151-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	22:06:54.133522-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3845, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=72011, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=72026, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:06:57.052103-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5e00 at /Applications/Nexy.app
default	22:06:57.074837-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6100 at /Applications/Nexy.app
default	22:06:57.085274-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	22:06:57.224550-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:06:57.224720-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:06:57.225851-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:06:57.226465-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:06:57.260163-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:06:57.260565-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:06:57.261276-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:06:57.261631-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:06:57.261929-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	22:06:57.262923-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	22:07:03.661178-0500	Nexy	server port 0x0001350f, session port 0x00003513
default	22:07:03.664103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2514, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:07:03.664179-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:03.667943-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2514, subject=com.nexy.assistant,
default	22:07:03.669353-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6100 at /Applications/Nexy.app
default	22:07:06.708204-0500	Nexy	[0xbcd137200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:07:06.710043-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:07:06.713005-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.9, subject=com.nexy.assistant,
default	22:07:06.714572-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6100 at /Applications/Nexy.app
default	22:07:06.736584-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[89561], responsiblePID[89561], responsiblePath: /Applications/Nexy.app to UID: 501
default	22:07:06.736980-0500	Nexy	[0xbcd137200] invalidated after the last release of the connection object
default	22:07:06.774302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5e00 at /Applications/Nexy.app
default	22:07:06.795340-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6100 at /Applications/Nexy.app
default	22:07:06.799649-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	22:07:12.344732-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:07:12.573247-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	22:07:12.713761-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:12.715449-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:12.716048-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:12.718570-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	22:07:12.719546-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	22:07:12.793565-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:12.794349-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:12.794383-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:12.795407-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	22:07:13.605647-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.3976, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=72011, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/private/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/X/com.google.Chrome.code_sign_clone/code_sign_clone.cMqZoh/Google Chrome.app.bundle/Contents/MacOS/Google Chrome}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=72026, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:15.761318-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5800 at /Applications/Nexy.app
default	22:07:15.782872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	22:07:15.808809-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	22:07:15.851815-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:15.852056-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:15.852236-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:15.852809-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:15.853804-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:15.853992-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:15.854197-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:15.854759-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:15.890542-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:15.890665-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:15.890883-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:15.891010-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:15.892095-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	22:07:15.892235-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	22:07:19.817866-0500	Nexy	[0xbcd137340] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	22:07:19.818629-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	22:07:19.818830-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89561.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:07:19.820118-0500	tccd	AUTHREQ_SUBJECT: msgID=89561.10, subject=com.nexy.assistant,
default	22:07:19.820877-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	22:07:19.841270-0500	Nexy	[0xbcd137340] invalidated after the last release of the connection object
default	22:07:22.851145-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=68009.12, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=68009, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	22:07:22.866595-0500	tccd	AUTHREQ_SUBJECT: msgID=68009.12, subject=com.nexy.assistant,
default	22:07:22.867835-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	22:07:22.893894-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	22:07:22.988933-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed5b00 at /Applications/Nexy.app
default	22:07:23.678522-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:07:23.695590-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	22:07:24.136048-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	22:07:24.256520-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	22:07:24.711189-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	22:07:24.716346-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	22:07:24.717299-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:24.718687-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:24.837023-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:24.838038-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:24.851242-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	22:07:28.434490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed6400 at /Applications/Nexy.app
default	22:07:28.477533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:07:28.487757-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	22:07:28.641688-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:28.641891-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:28.642339-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	22:07:28.642618-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:28.642735-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:28.643548-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:28.643737-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	22:07:28.644157-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	22:07:28.644429-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	22:07:28.644548-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	22:07:28.681024-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:28.681356-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:28.682640-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	22:07:28.683748-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	22:07:28.684076-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	22:07:28.685062-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	22:07:36.037247-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=68009.16, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=68009, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	22:07:36.040179-0500	tccd	AUTHREQ_SUBJECT: msgID=68009.16, subject=com.nexy.assistant,
default	22:07:36.042251-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:07:39.084691-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	22:07:39.084884-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:07:39.086191-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	22:07:39.086654-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	22:07:39.086719-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	22:07:39.106228-0500	Nexy	[0xbcd137200] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	22:07:39.108037-0500	Nexy	[0xbcd137200] invalidated after the last release of the connection object
default	22:07:39.108892-0500	kernel	udp connect: [<IPv4-redacted>:50954<-><IPv4-redacted>:53] interface:  (skipped: 0)
so_gencnt: 1580443 so_state: 0x0102 process: Nexy:89561 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8bc8db26
default	22:07:39.109319-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:07:39.109539-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:07:39.115299-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 132
default	22:07:39.131877-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1580444 so_state: 0x0000 process: Nexy:89561 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	22:07:39.131892-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1580444 so_state: 0x0000 process: Nexy:89561 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	22:07:39.133635-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbcb684040) Selecting device 85 from constructor
default	22:07:39.133647-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbcb684040)
default	22:07:39.133654-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbcb684040) not already running
default	22:07:39.133660-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbcb684040) nothing to teardown
default	22:07:39.133665-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbcb684040) connecting device 85
default	22:07:39.133749-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbcb684040) Device ID: 85 (Input:No | Output:Yes): true
default	22:07:39.133856-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbcb684040) created ioproc 0xc for device 85
default	22:07:39.133953-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 7 device listeners to device 85
default	22:07:39.134093-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbcb684040) adding 0 device delegate listeners to device 85
default	22:07:39.134103-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbcb684040)
default	22:07:39.134176-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.134187-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:07:39.134195-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.134212-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:07:39.134219-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:07:39.134304-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:07:39.134314-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbcb684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:07:39.134318-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:07:39.134321-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device listeners from device 0
default	22:07:39.134325-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbcb684040) removing 0 device delegate listeners from device 0
default	22:07:39.134329-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbcb684040)
default	22:07:39.134391-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	22:07:39.134696-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.136219-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb695560, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.136253-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.137164-0500	kernel	udp connect: [<IPv4-redacted>:51264<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1580445 so_state: 0x0002 process: Nexy:89561 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x89e8a0e5
default	22:07:39.137173-0500	kernel	udp_connection_summary [<IPv4-redacted>:51264<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1580445 so_state: 0x0002 process: Nexy:89561 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x89e8a0e5 flowctl: 0us (0x)
default	22:07:39.137322-0500	kernel	udp_connection_summary [<IPv4-redacted>:50954<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580443 so_state: 0x0132 process: Nexy:89561 Duration: 0.028 sec Conn_Time: 0.028 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8bc8db26 flowctl: 0us (0x)
default	22:07:39.137897-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.138113-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.139663-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 77D75F33-1448-4E0E-9D43-D89A92C14B40 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53378,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x1520df1d tp_proto=0x06"
default	22:07:39.139730-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53378<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580446 t_state: SYN_SENT process: Nexy:89561 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb3147f2c
default	22:07:39.146049-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.146269-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.148236-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb695620, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.148248-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.148572-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.149159-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb6959e0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.149173-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbcb6959e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:07:39.149178-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.149179-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	22:07:39.149190-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	22:07:39.149195-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	22:07:39.150100-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbcb6959e0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:07:39.150109-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbcb6959e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:07:39.150110-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	22:07:39.150114-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:07:39.150120-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	22:07:39.150125-0500	Nexy	AudioConverter -> 0xbcb6959e0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	22:07:39.150263-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbcb6959e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:07:39.154733-0500	kernel	tcp connected: [<IPv4-redacted>:53378<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580446 t_state: ESTABLISHED process: Nexy:89561 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb3147f2c
default	22:07:40.162872-0500	Nexy	[0xbcd137480] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	22:07:40.178534-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3000000033 pid: 89561
default	22:07:40.179585-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	22:07:40.187839-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xbcd624780
 (
    "<NSDarkAquaAppearance: 0xbcd624820>",
    "<NSSystemAppearance: 0xbcd624640>"
)>
default	22:07:40.192893-0500	Nexy	[0xbcd137980] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	22:07:40.197072-0500	Nexy	[0xbcd137ac0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	22:07:40.199522-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	22:07:40.199753-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	22:07:40.199762-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	22:07:40.199789-0500	Nexy	[0xbcd137c00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	22:07:40.199842-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	22:07:40.199899-0500	Nexy	[0xbcd137d40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.199959-0500	Nexy	FBSWorkspace registering source: <private>
default	22:07:40.200562-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	22:07:40.200982-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	22:07:40.201394-0500	Nexy	<FBSWorkspaceScenesClient:0xbd000b2a0 <private>> attempting immediate handshake from activate
default	22:07:40.201715-0500	Nexy	<FBSWorkspaceScenesClient:0xbd000b2a0 <private>> sent handshake
default	22:07:40.202070-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	22:07:40.201911-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.202219-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.202779-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	22:07:40.202845-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Registering event dispatcher at init
default	22:07:40.203164-0500	ControlCenter	Created <FBWorkspace: 0xbdbed4a00; <FBApplicationProcess: 0xbdf13f780; app<application.com.nexy.assistant.54571778.54571787>:89561(v145E37)>>
default	22:07:40.203182-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54571778.54571787> with intent background
default	22:07:40.203449-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54571778.54571787(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	22:07:40.203548-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54571778.54571787(501)> from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-70779 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	22:07:40.203675-0500	runningboardd	Assertion 402-625-70779 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) will be created as active
default	22:07:40.203705-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-70779 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.203989-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.204073-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	22:07:40.204001-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.204227-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.204274-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.205346-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	22:07:40.206087-0500	Nexy	Requesting scene <FBSScene: 0xbd000b5c0; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A> from com.apple.controlcenter.statusitems
default	22:07:40.207501-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.208364-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.208419-0500	Nexy	Request for <FBSScene: 0xbd000b5c0; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A> complete!
default	22:07:40.208491-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	22:07:40.209728-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	22:07:40.209944-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	22:07:40.210169-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	22:07:40.210205-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	22:07:40.210459-0500	Nexy	Requesting scene <FBSScene: 0xbd000b700; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	22:07:40.210633-0500	Nexy	Request for <FBSScene: 0xbd000b700; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView> complete!
default	22:07:40.211488-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Bootstrap success!
default	22:07:40.211863-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Setting process visibility to: Background
default	22:07:40.211919-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] No launch watchdog for this process, dropping initial assertion in 2.0s
default	22:07:40.212166-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.212183-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	22:07:40.212701-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:402-625-70780 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	22:07:40.212759-0500	runningboardd	Assertion 402-625-70780 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.213160-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.213171-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.213181-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.213233-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.215770-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.216109-0500	ControlCenter	Adding: <FBApplicationProcess: 0xbdf13f780; app<application.com.nexy.assistant.54571778.54571787>:89561(v145E37)>
default	22:07:40.216319-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.216504-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.216521-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	22:07:40.216619-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	22:07:40.216604-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Connection established.
default	22:07:40.216675-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xbdc9d3020>
default	22:07:40.216685-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.216696-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Connection to remote process established!
default	22:07:40.223262-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.223278-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdf13f780; app<application.com.nexy.assistant.54571778.54571787>:89561(v145E37)>
default	22:07:40.223366-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Registered new scene: <FBWorkspaceScene: 0xbe0dc0480; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A> (fromRemnant = 0)
default	22:07:40.223396-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace interruption policy did change: reconnect
default	22:07:40.223547-0500	ControlCenter	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A] Client process connected: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.223552-0500	Nexy	Request for <FBSScene: 0xbd000b5c0; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A> complete!
default	22:07:40.223628-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:402-625-70781 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	22:07:40.223701-0500	runningboardd	Assertion 402-625-70781 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as inactive as originator process has not exited
default	22:07:40.224029-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-70782 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	22:07:40.224131-0500	runningboardd	Assertion 402-625-70782 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.224215-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	22:07:40.224256-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.224272-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdf13f780; app<application.com.nexy.assistant.54571778.54571787>:89561(v145E37)>
default	22:07:40.224324-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Registered new scene: <FBWorkspaceScene: 0xbe0dc0fc0; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	22:07:40.224380-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.224467-0500	Nexy	Request for <FBSScene: 0xbd000b700; com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView> complete!
default	22:07:40.224466-0500	ControlCenter	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.224390-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.224445-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.224529-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.224766-0500	Nexy	<FBSWorkspaceScenesClient:0xbd000b2a0 <private>> Reconnecting scene com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A
default	22:07:40.225066-0500	Nexy	<FBSWorkspaceScenesClient:0xbd000b2a0 <private>> Reconnecting scene com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView
default	22:07:40.226913-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.227284-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.227399-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.230067-0500	Nexy	Registering for test daemon availability notify post.
default	22:07:40.230181-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:07:40.230266-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:07:40.230348-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:07:40.231570-0500	Nexy	[0xbcd78fd40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	22:07:40.234503-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:07:40.239923-0500	Nexy	[0xbcd78c3c0] Connection returned listener port: 0x4f03
default	22:07:40.240431-0500	Nexy	SignalReady: pid=89561 asn=0x0-0x5a15a1
default	22:07:40.241194-0500	Nexy	SIGNAL: pid=89561 asn=0x0x-0x5a15a1
default	22:07:40.241858-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	22:07:40.251557-0500	Nexy	0xbcca5c380: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	22:07:40.251574-0500	Nexy	0xbcd00bc30: Updating using cached account information
default	22:07:40.258081-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.261195-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.262876-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	22:07:40.262881-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	22:07:40.262896-0500	Nexy	[0xbcd78d400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	22:07:40.262969-0500	Nexy	[0xbcd78d400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.263976-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	22:07:40.267132-0500	Nexy	[C:2] Alloc <private>
default	22:07:40.267168-0500	Nexy	[0xbcd78d400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.268598-0500	WindowManager	Connection activated | (89561) Nexy
default	22:07:40.269541-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70783 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.269608-0500	runningboardd	Assertion 402-89561-70783 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.269921-0500	runningboardd	Invalidating assertion 402-89561-70783 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.269963-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.270028-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-89561). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	22:07:40.269977-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.270000-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.270041-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70784 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.270046-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.270137-0500	runningboardd	Assertion 402-89561-70784 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.271990-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-89561)
default	22:07:40.272567-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(8E2FBCB8, (bid:com.nexy.assistant-Item-0-89561)) for (bid:com.nexy.assistant-Item-0-89561)
default	22:07:40.272593-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.272841-0500	runningboardd	Invalidating assertion 402-89561-70784 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.273086-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.273036-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70785 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.273096-0500	runningboardd	Assertion 402-89561-70785 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.273217-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.273478-0500	runningboardd	Invalidating assertion 402-89561-70785 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.273595-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70786 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.273644-0500	runningboardd	Assertion 402-89561-70786 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.273714-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-89561)]
default	22:07:40.273921-0500	runningboardd	Invalidating assertion 402-89561-70786 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.274064-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70787 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.274120-0500	runningboardd	Assertion 402-89561-70787 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.274323-0500	runningboardd	Invalidating assertion 402-89561-70787 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.274437-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70788 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.274476-0500	ControlCenter	Created instance DisplayableId(CDEFFD02) in .menuBar for DisplayableAppStatusItemType(8E2FBCB8, (bid:com.nexy.assistant-Item-0-89561)) .menuBar
default	22:07:40.274485-0500	runningboardd	Assertion 402-89561-70788 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.274710-0500	runningboardd	Invalidating assertion 402-89561-70788 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.274808-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70789 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.274844-0500	runningboardd	Assertion 402-89561-70789 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.275043-0500	runningboardd	Invalidating assertion 402-89561-70789 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.275151-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70790 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.275191-0500	runningboardd	Assertion 402-89561-70790 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.275408-0500	runningboardd	Invalidating assertion 402-89561-70790 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.275619-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70791 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.275671-0500	runningboardd	Assertion 402-89561-70791 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.275943-0500	runningboardd	Invalidating assertion 402-89561-70791 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.276087-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89561-70792 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:07:40.276140-0500	runningboardd	Assertion 402-89561-70792 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.276343-0500	runningboardd	Invalidating assertion 402-89561-70792 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:40.277216-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.277575-0500	Nexy	[0xbcd78f5c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:07:40.277795-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4175, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.277827-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.277829-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.278213-0500	Nexy	[0xbcd78f5c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.278232-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	22:07:40.278248-0500	Nexy	Will add XPC store with options: <private> <private>
default	22:07:40.279104-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4175, subject=com.nexy.assistant,
default	22:07:40.279964-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46400 at /Applications/Nexy.app
default	22:07:40.280847-0500	Nexy	[0xbcd10c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.281588-0500	ControlCenter	Created ephemaral instance DisplayableId(CDEFFD02) for (bid:com.nexy.assistant-Item-0-89561) with positioning .ephemeral
default	22:07:40.281639-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4176, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.281680-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.282740-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4176, subject=com.nexy.assistant,
default	22:07:40.283564-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.285552-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	22:07:40.286680-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	22:07:40.290142-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	22:07:40.290241-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.290890-0500	Nexy	[com.apple.controlcenter:FDE32645-11C5-4007-8CB0-837BF126621A] Sending action(s) in update: NSSceneFenceAction
default	22:07:40.300764-0500	Nexy	[0xbcd10c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.300806-0500	Nexy	[0xbcd10c3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.300860-0500	Nexy	[0xbcd10c640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.301505-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4177, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.301533-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.302521-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4177, subject=com.nexy.assistant,
default	22:07:40.303087-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.303179-0500	Nexy	Defaultable: persistentAccounts: <private>
default	22:07:40.303209-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0xbd000a760: identifier=_acceptedIntroductions, name=Other Known, baseURL=(nil), dsid=(nil)> because it can't become default
default	22:07:40.303224-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0xbd000a6c0: identifier=_directoryServices, name=Directory Services, baseURL=(nil), dsid=(nil)> because it can't become default
default	22:07:40.304511-0500	Nexy	-awakeFromLoad
default	22:07:40.304615-0500	Nexy	-setServername: <private>  Parsed into scheme: https  host: <private>  port: 0  path: <private>
default	22:07:40.304668-0500	Nexy	-initWithUID:persistence: called on thread: <private>
default	22:07:40.304856-0500	Nexy	-clearPrincipalProperties
default	22:07:40.304878-0500	Nexy	-clearHomeContainers
default	22:07:40.305253-0500	Nexy	Defaultable: Final list: <private>
default	22:07:40.305268-0500	Nexy	New account should become the default account
default	22:07:40.305485-0500	Nexy	0xbcca5c380: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	22:07:40.305516-0500	Nexy	0xbcd00bc30: Updating using cached account information
default	22:07:40.319034-0500	Nexy	[0xbcd10c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.319065-0500	Nexy	[0xbd0148000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.319099-0500	Nexy	[0xbd0148140] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.319734-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4178, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.319761-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.320736-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4178, subject=com.nexy.assistant,
default	22:07:40.321296-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.337069-0500	Nexy	[0xbd0148140] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.337104-0500	Nexy	[0xbd0148140] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.337141-0500	Nexy	[0xbd0148280] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.337727-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4179, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.337754-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.338613-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4179, subject=com.nexy.assistant,
default	22:07:40.339139-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.354453-0500	Nexy	[0xbd0148280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.354490-0500	Nexy	[0xbd0148280] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.355670-0500	Nexy	Did add XPC store
default	22:07:40.355685-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	22:07:40.355732-0500	Nexy	[0xbd01488c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	22:07:40.356136-0500	Nexy	[0xbd01488c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.356153-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:07:40.356180-0500	Nexy	Will add XPC store with options: <private> <private>
default	22:07:40.358239-0500	Nexy	[0xbd014b340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.358813-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4180, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.358839-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.359767-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4180, subject=com.nexy.assistant,
default	22:07:40.360313-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.376322-0500	Nexy	[0xbd014b340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.376360-0500	Nexy	[0xbd014b340] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.376394-0500	Nexy	[0xbd014b480] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.376704-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.376717-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.376725-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.376745-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.376972-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4181, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.377003-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.377897-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4181, subject=com.nexy.assistant,
default	22:07:40.378437-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.379324-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	22:07:40.379700-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.380069-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.380194-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.383265-0500	Nexy	Start service name com.apple.spotlightknowledged
default	22:07:40.384023-0500	Nexy	[GMS] availability notification token 120
default	22:07:40.394815-0500	Nexy	[0xbd014b480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.394855-0500	Nexy	[0xbd014b480] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.394896-0500	Nexy	[0xbd014b5c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.395489-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4182, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.395524-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.396482-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4182, subject=com.nexy.assistant,
default	22:07:40.397046-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.411992-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	22:07:40.412086-0500	runningboardd	Invalidating assertion 402-625-70782 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:07:40.414606-0500	Nexy	[0xbd014b5c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.414676-0500	Nexy	[0xbd014b5c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.414745-0500	Nexy	[0xbd014b700] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	22:07:40.415685-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84841.4183, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	22:07:40.415729-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=84841, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89561, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:40.416996-0500	tccd	AUTHREQ_SUBJECT: msgID=84841.4183, subject=com.nexy.assistant,
default	22:07:40.417716-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:07:40.436187-0500	Nexy	[0xbd014b700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:07:40.436259-0500	Nexy	[0xbd014b700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:07:40.437134-0500	Nexy	Did add XPC store
default	22:07:40.437151-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	22:07:40.443054-0500	Nexy	Client change history token is invalid: <private>, current token: <private>, error: Error Domain=NSCocoaErrorDomain Code=134501 UserInfo={NSLocalizedFailureReason=<private>}
error	22:07:40.443356-0500	Nexy	Failed to fetch change history: Error Domain=CNErrorDomain Code=1006 "Full Sync Required" UserInfo={NSLocalizedFailureReason=A full sync is required., NSLocalizedDescription=Full Sync Required, NSUnderlyingError=0xbd015a730 {Error Domain=CNErrorDomain Code=604 "Invalid Change History Anchor" UserInfo={NSLocalizedDescription=Invalid Change History Anchor, NSLocalizedFailureReason=The change history anchor is invalid.}}}
default	22:07:40.443888-0500	Nexy	0000 BEGIN: Will execute fetch for request: <private>
default	22:07:40.443901-0500	Nexy	0000 Entry point: executeFetchRequest:error:
default	22:07:40.443912-0500	Nexy	0000 Predicate: (null) <private>
default	22:07:40.454627-0500	Nexy	App is linked against Fall 2022 SDK or later
default	22:07:40.454646-0500	Nexy	Note access is not granted, so Notes are inaccessible
fault	22:07:40.454741-0500	Nexy	Attempt to read notes by an unentitled app
default	22:07:40.464380-0500	Nexy	0000 History anchor returned to client: <CNChangeHistoryAnchor: 0xbcb028260: version=2, token=<NSPersistentHistoryToken - {
    "121C6BBC-8A11-4E34-B252-321D0995C010" = 6;
    "CE445509-54F5-473C-9A96-89025D6F9355" = 4818;
}>>
default	22:07:40.464458-0500	Nexy	0000 Contact: 3EE990C2-437C-497A-B4CF-4787E78B5D0C:ABPerson
default	22:07:40.464468-0500	Nexy	0000 Contact: 2645688D-4F81-4C23-847F-96DEA47CCE6D:ABPerson
default	22:07:40.464474-0500	Nexy	0000 Contact: C822EB31-1F0F-41F6-9120-A322A5874983:ABPerson
default	22:07:40.464479-0500	Nexy	0000 Contact: 50AD2AD1-9340-4D1D-8702-DB033FCB2397:ABPerson
default	22:07:40.464484-0500	Nexy	0000 Contact: EDB979D3-287A-47DC-BC6D-006167336515:ABPerson
default	22:07:40.464488-0500	Nexy	0000 Contact: 9595A838-850C-49DB-8998-80F19667F619:ABPerson
default	22:07:40.464497-0500	Nexy	0000 Contact: 9891AB4D-DDC3-49D3-8FAA-45BFB1995A79:ABPerson
default	22:07:40.464502-0500	Nexy	0000 Contact: 34B7C886-745F-477F-BAF4-C6494310C1C1:ABPerson
default	22:07:40.464507-0500	Nexy	0000 Contact: 3426C1A4-CACA-42EF-8793-7312DCEE5E69:ABPerson
default	22:07:40.464512-0500	Nexy	0000 Contact: AFFBAE3D-BA02-4D6F-AE25-87E55C2E4CD9:ABPerson
default	22:07:40.464534-0500	Nexy	0000 Contact: 55C7A0C2-9163-43BC-95A9-A92E4F5427BD:ABPerson
default	22:07:40.464545-0500	Nexy	0000 Contact: CBAABC59-9B06-47EE-9311-0823CE3EE179:ABPerson
default	22:07:40.464550-0500	Nexy	0000 Contact: FF2BD9DD-8A6D-4E97-BB7D-7B1A5C4FAC0F:ABPerson
default	22:07:40.464555-0500	Nexy	0000 Contact: F6E944AE-3E32-4C0C-BA60-EE94D9402DA7:ABPerson
default	22:07:40.464560-0500	Nexy	0000 Contact: 0E222C4B-C87D-403F-A824-B8B8EAABF29D:ABPerson
default	22:07:40.464571-0500	Nexy	0000 Contact: 160B58EE-E9AF-4BBE-B484-7D4E18CA0CD4:ABPerson
default	22:07:40.464577-0500	Nexy	0000 Contact: D6931A27-6BBA-4ABF-AB86-AA94288C8731:ABPerson
default	22:07:40.464589-0500	Nexy	0000 Contact: 04E7F59A-3D30-4CF9-8395-AE8737EE1154:ABPerson
default	22:07:40.464593-0500	Nexy	0000 Contact: 863252FB-26EB-421B-9B96-91673ED81D35:ABPerson
default	22:07:40.464620-0500	Nexy	0000 Contact: 742C7DAC-D2A9-4D1C-A93D-DC71F37722B9:ABPerson
default	22:07:40.464626-0500	Nexy	0000 Contact: 99649BEC-0C02-4588-9CCA-09103FDC430C:ABPerson
default	22:07:40.464632-0500	Nexy	0000 Contact: 8898FA76-8C7B-4917-B353-30B4A337A32B:ABPerson
default	22:07:40.464636-0500	Nexy	0000 Contact: 75C5C7DD-DD9E-437F-91B9-34AFD56C5A14:ABPerson
default	22:07:40.464641-0500	Nexy	0000 Contact: DDC41FDC-94BF-4147-9863-5AFCC485C4BA:ABPerson
default	22:07:40.464646-0500	Nexy	0000 Contact: B6D0B979-BBDF-4FF5-93A8-0974C5AE45C7:ABPerson
default	22:07:40.464651-0500	Nexy	0000 Contact: B7A8ADD0-A952-45B0-B7A2-D15A3D34A898:ABPerson
default	22:07:40.464656-0500	Nexy	0000 Contact: 35894E4A-BF98-44E4-85B9-33C2A0A01944:ABPerson
default	22:07:40.464659-0500	Nexy	0000 Contact: 67B532BB-C394-4D14-B2E6-C1B93DE930E4:ABPerson
default	22:07:40.464665-0500	Nexy	0000 Contact: A71518ED-EC1D-4740-9D8C-2C5F81C71467:ABPerson
default	22:07:40.464677-0500	Nexy	0000 Contact: EE1E04AC-AF03-428A-97EF-6E8851A86066:ABPerson
default	22:07:40.464685-0500	Nexy	0000 Contact: 54E381BF-247A-4AB7-81FD-8C78CBB93296:ABPerson
default	22:07:40.464690-0500	Nexy	0000 Contact: A5DB19AB-C77E-44EC-87A4-8459DA494E7B:ABPerson
default	22:07:40.464700-0500	Nexy	0000 Contact: FC26680D-B85F-4E40-812F-4F169185AE50:ABPerson
default	22:07:40.464706-0500	Nexy	0000 Contact: E36EA0A4-41F7-4C3F-AAF9-A93099626D77:ABPerson
default	22:07:40.464716-0500	Nexy	0000 Contact: 37E2B276-263E-40A5-BF81-1628796DB605:ABPerson
default	22:07:40.464724-0500	Nexy	0000 Contact: D989E37A-D5DC-4A68-8D47-AD8FEE0B37BA:ABPerson
default	22:07:40.464728-0500	Nexy	0000 Contact: 204F2E81-2324-4937-9859-E8732482C902:ABPerson
default	22:07:40.464734-0500	Nexy	0000 Contact: C4831F25-FE6F-4217-92D2-C4D6C01013BC:ABPerson
default	22:07:40.464750-0500	Nexy	0000 Contact: 4FD77C47-1199-46DF-B186-25C3BB8E54C4:ABPerson
default	22:07:40.464755-0500	Nexy	0000 Contact: 16FA5BBF-AADB-4362-83EB-09668C0C6A84:ABPerson
default	22:07:40.464760-0500	Nexy	0000 Contact: D9A061DB-8A77-472E-A6B3-AF6A4A6727A9:ABPerson
default	22:07:40.464766-0500	Nexy	0000 Contact: 62AC02AD-E5FE-4F18-8DEB-151D2FFD50D2:ABPerson
default	22:07:40.464776-0500	Nexy	0000 Contact: 9D4856E4-4610-4169-9460-115522478752:ABPerson
default	22:07:40.464781-0500	Nexy	0000 Contact: 8038DF9A-4503-4464-BA80-1A8B28F523E6:ABPerson
default	22:07:40.464792-0500	Nexy	0000 Contact: DE31B769-37E8-406B-BC5C-FC44F37A37D1:ABPerson
default	22:07:40.464797-0500	Nexy	0000 Contact: B2E8FADF-3954-4D05-B047-C43474BF8E54:ABPerson
default	22:07:40.464812-0500	Nexy	0000 Contact: 5C30DD83-8C53-4FB6-943A-DF0CED6109D6:ABPerson
default	22:07:40.464818-0500	Nexy	0000 Contact: 16A1EC92-AB39-4C1E-8E16-706B5F47397C:ABPerson
default	22:07:40.464823-0500	Nexy	0000 Contact: 36994EED-FC81-46EF-86F8-8B3217234A98:ABPerson
default	22:07:40.464828-0500	Nexy	0000 Contact: D0D31CD7-6F0F-4030-A30D-197CE5187EED:ABPerson
default	22:07:40.464833-0500	Nexy	0000 Contact: F5676762-711F-4325-8A7A-FCB211127327:ABPerson
default	22:07:40.464855-0500	Nexy	0000 Contact: 99378C4C-7187-4A49-A938-AF1E4D9750E9:ABPerson
default	22:07:40.464863-0500	Nexy	0000 Contact: FE93F61D-6DD6-4CF7-9D17-F972815C60EB:ABPerson
default	22:07:40.464867-0500	Nexy	0000 Contact: E7CCA41A-8A2E-4351-852A-A5CFB6BD2AF5:ABPerson
default	22:07:40.464871-0500	Nexy	0000 Contact: EC41AC6A-1CB5-41D5-B70A-D7D261B5F6B3:ABPerson
default	22:07:40.464876-0500	Nexy	0000 Contact: 2A13AE99-82FE-4A26-A768-1B8C4A11C6C3:ABPerson
default	22:07:40.464880-0500	Nexy	0000 Contact: D5B5277E-F18A-48C2-B93C-E578CEB16C34:ABPerson
default	22:07:40.464885-0500	Nexy	0000 Contact: 1148E024-6D8F-4279-921E-7936B62EB2B8:ABPerson
default	22:07:40.464890-0500	Nexy	0000 Contact: FAF205FC-E995-4261-90F7-336A4D237F48:ABPerson
default	22:07:40.464901-0500	Nexy	0000 Contact: 88E161CA-F779-4608-BE32-D15726C295C6:ABPerson
default	22:07:40.464910-0500	Nexy	0000 Contact: BE244260-8495-47EA-9EFA-A4A129388623:ABPerson
default	22:07:40.464916-0500	Nexy	0000 Contact: FC34E363-0467-4B9C-95B0-F8C585C41741:ABPerson
default	22:07:40.464926-0500	Nexy	0000 Contact: F244F65D-0A57-4A3C-B8B8-9E1C389A5E77:ABPerson
default	22:07:40.464931-0500	Nexy	0000 Contact: 9DE56935-FB3E-470E-9878-89DB593E2DFE:ABPerson
default	22:07:40.464943-0500	Nexy	0000 Contact: 51D61586-1A8A-4EC4-8568-45B5296B1751:ABPerson
default	22:07:40.464952-0500	Nexy	0000 Contact: F34A454E-F1D3-4849-9368-950A6FFA8DD1:ABPerson
default	22:07:40.464957-0500	Nexy	0000 Contact: 5E09571D-9D8E-4D12-8480-F04FD91A55C4:ABPerson
default	22:07:40.464968-0500	Nexy	0000 Contact: 997D7D2F-4504-4C65-A31D-535219B806F5:ABPerson
default	22:07:40.464975-0500	Nexy	0000 Contact: F4D5E6E8-6B00-4329-94DC-82661F45DDB5:ABPerson
default	22:07:40.464984-0500	Nexy	0000 Contact: B3F91E16-48C2-4383-BFDA-F39E45D698A9:ABPerson
default	22:07:40.464991-0500	Nexy	0000 Contact: 972B1CC5-A00E-409A-A1C8-1035B67228F2:ABPerson
default	22:07:40.465007-0500	Nexy	0000 Contact: C9342200-2A80-485B-8777-A59F252176D4:ABPerson
default	22:07:40.465012-0500	Nexy	0000 Contact: FCD5548B-6E7B-4B57-9097-496095F0C27B:ABPerson
default	22:07:40.465019-0500	Nexy	0000 Contact: 32E90B79-BC48-4AFC-A5CE-495011FBE68F:ABPerson
default	22:07:40.465027-0500	Nexy	0000 Contact: 799B442D-0C1B-41A7-982A-5A795CF5AC7E:ABPerson
default	22:07:40.465032-0500	Nexy	0000 Contact: 4BC8FD3A-601A-4905-B4F0-AAEE2EA51FFC:ABPerson
default	22:07:40.465037-0500	Nexy	0000 Contact: EB01D8DC-AD35-4332-B52D-021C69F834F5:ABPerson
default	22:07:40.465040-0500	Nexy	0000 Contact: 34439B56-399C-41AE-8A94-926BE1F059E3:ABPerson
default	22:07:40.465046-0500	Nexy	0000 Contact: 5B2AA695-5EAB-4F85-9EA7-0F11FEE7BF7E:ABPerson
default	22:07:40.465053-0500	Nexy	0000 Contact: 680613B6-43E0-4C77-8B2B-0F21D4D6F558:ABPerson
default	22:07:40.465064-0500	Nexy	0000 Contact: FEFADE95-1917-4F12-AF5F-E9AF0F50E039:ABPerson
default	22:07:40.465069-0500	Nexy	0000 Contact: 1CED5FB1-D054-43C6-BF35-E035DFF16C75:ABPerson
default	22:07:40.465079-0500	Nexy	0000 Contact: 4D6A09F3-71D7-4E04-83FD-9BB5EF7442CF:ABPerson
default	22:07:40.465084-0500	Nexy	0000 Contact: 03F9DBA8-764B-4F5E-AFB8-4FE555600768:ABPerson
default	22:07:40.465092-0500	Nexy	0000 Contact: 33E6AEE6-78CC-42D7-80DA-478EDE698964:ABPerson
default	22:07:40.465101-0500	Nexy	0000 Contact: 2B720652-555E-462B-8C74-277B5F6F5F59:ABPerson
default	22:07:40.465125-0500	Nexy	0000 Contact: D8AB7561-7ABC-404E-A1AD-D9765D7DD983:ABPerson
default	22:07:40.465131-0500	Nexy	0000 Contact: 8256DD81-94E0-404F-BE4E-E6831011073C:ABPerson
default	22:07:40.465136-0500	Nexy	0000 Contact: 260C090E-52D7-4D15-AE22-6804C72C9DBF:ABPerson
default	22:07:40.465140-0500	Nexy	0000 Contact: F5703214-DEA8-429F-ADBF-5465A9AFE1BC:ABPerson
default	22:07:40.465145-0500	Nexy	0000 Contact: 1FBE32BC-B2F2-4B98-8BA8-04A4E25A4F0E:ABPerson
default	22:07:40.465150-0500	Nexy	0000 Contact: 2285EC2D-05CF-42C3-8C59-C4930AD792E3:ABPerson
default	22:07:40.465174-0500	Nexy	0000 Contact: 96E50230-0A5E-4B64-A2E9-A2F57018F4EA:ABPerson
default	22:07:40.465181-0500	Nexy	0000 Contact: 1D80A41C-48FF-40D8-A1F7-EB1FCAF019EC:ABPerson
default	22:07:40.465186-0500	Nexy	0000 Contact: 3C49D81F-04DC-4318-93D4-B25373EDFE30:ABPerson
default	22:07:40.465190-0500	Nexy	0000 Contact: 5B4B2182-FBEA-48F0-B9C7-742552BF6CF6:ABPerson
default	22:07:40.465195-0500	Nexy	0000 Contact: 697396C6-6DF5-4A8D-BBC1-7CFB8C26B531:ABPerson
default	22:07:40.465200-0500	Nexy	0000 Contact: BC83C14B-9BF3-4E6D-A5BD-1252B3AF3A72:ABPerson
default	22:07:40.465207-0500	Nexy	0000 Contact: 29B138C5-7412-4C36-A514-72D80434AC26:ABPerson
default	22:07:40.465212-0500	Nexy	0000 Contact: 93438337-7E2C-4A3D-99F8-28AECEE7A491:ABPerson
default	22:07:40.465217-0500	Nexy	0000 Contact: BEEDDC1A-71AD-4FBD-9241-9F6B4669022C:ABPerson
default	22:07:40.465256-0500	Nexy	0000 Contact: 516FCDD2-D694-4336-9C5C-B3F9398876E3:ABPerson
default	22:07:40.465264-0500	Nexy	0000 Contact: CB798F66-5E15-419F-8CB1-A22A10034846:ABPerson
default	22:07:40.465269-0500	Nexy	0000 Contact: 9BE2908B-57F8-42EB-85AB-E556B53D5008:ABPerson
default	22:07:40.465274-0500	Nexy	0000 Contact: 74E5D1E4-D560-47F5-800D-2B15C8F128ED:ABPerson
default	22:07:40.465277-0500	Nexy	0000 Contact: 73FA4D96-88CD-4E81-B755-D3C151251CB2:ABPerson
default	22:07:40.465284-0500	Nexy	0000 Contact: A159EB30-CDD4-4876-B3EB-7A251E5003A1:ABPerson
default	22:07:40.465289-0500	Nexy	0000 Contact: 2E020885-F8C2-47BB-AEE3-DD7CF66B13B4:ABPerson
default	22:07:40.465293-0500	Nexy	0000 Contact: 05A17C92-D301-4B09-A90C-D64806C4CA53:ABPerson
default	22:07:40.465297-0500	Nexy	0000 Contact: AD733A8E-1D66-4608-811D-8B3CC382D864:ABPerson
default	22:07:40.465302-0500	Nexy	0000 Contact: E567A65A-A157-4ABD-B1FD-82CC549DEDED:ABPerson
default	22:07:40.465307-0500	Nexy	0000 Contact: 7F0336C8-01E0-47A7-A79A-9400EBF86D9C:ABPerson
default	22:07:40.465317-0500	Nexy	0000 Contact: 46F95F55-6525-42E6-A4B3-332AB9ECB6C9:ABPerson
default	22:07:40.465325-0500	Nexy	0000 Contact: 0BF7B2D3-D0E4-4CF5-A2E5-BBAB2F74860F:ABPerson
default	22:07:40.465328-0500	Nexy	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	22:07:40.465333-0500	Nexy	0000 Contact: DF05522B-2972-4CAB-8C0F-9FDECE2E3D80:ABPerson
default	22:07:40.465338-0500	Nexy	0000 Contact: 32C28665-F08E-4EE8-AFEB-487908D24319:ABPerson
default	22:07:40.465401-0500	Nexy	0000 Contact: 23512481-0DEF-42CA-8985-3D92A24DC0D9:ABPerson
default	22:07:40.465413-0500	Nexy	0000 Contact: C799BC2E-8783-42B8-BE80-6B9329212F7F:ABPerson
default	22:07:40.465418-0500	Nexy	0000 Contact: AF84B174-40F6-4E9C-A51A-D3FACA6CD75E:ABPerson
default	22:07:40.465425-0500	Nexy	0000 Contact: D41F250E-DF7F-4F9C-9D25-DC402CAC6533:ABPerson
default	22:07:40.465431-0500	Nexy	0000 Contact: E5E58063-920E-46E6-8939-C1A7ACCF23F0:ABPerson
default	22:07:40.465437-0500	Nexy	0000 Contact: F48B9D39-03E0-45D0-AA05-14488FC68C6F:ABPerson
default	22:07:40.465445-0500	Nexy	0000 Contact: B599DEB9-C4DF-472F-9B9E-67C3935077CD:ABPerson
default	22:07:40.465451-0500	Nexy	0000 Contact: CD1D19AA-FC19-4C03-9DC9-C147E8C245D1:ABPerson
default	22:07:40.465456-0500	Nexy	0000 Contact: 4F833F31-870E-4630-825C-0F532CBA3D39:ABPerson
default	22:07:40.465461-0500	Nexy	0000 Contact: BD409DD5-797E-41A8-B955-2CC4520A8769:ABPerson
default	22:07:40.465466-0500	Nexy	0000 Contact: 8A88B309-DB9A-4B6A-B1D9-CD6910D5845B:ABPerson
default	22:07:40.465471-0500	Nexy	0000 Contact: 18BDFAAD-5A5F-42D6-890A-2C5AEA9201D4:ABPerson
default	22:07:40.465487-0500	Nexy	0000 Contact: 96309E07-28A0-4C3F-8B27-7224031FF6EB:ABPerson
default	22:07:40.465497-0500	Nexy	0000 Contact: BF324B31-1F91-4723-87BC-8FE02890D85F:ABPerson
default	22:07:40.465519-0500	Nexy	0000 Contact: A0DA1AD3-5F0A-4625-8A45-AEE2662B5DF7:ABPerson
default	22:07:40.465527-0500	Nexy	0000 Contact: 76DEED21-9E22-4327-83F8-C1C1DDF67DEE:ABPerson
default	22:07:40.465533-0500	Nexy	0000 Contact: 7C25BC81-A7AB-4059-A199-45F36EBE02EB:ABPerson
default	22:07:40.465543-0500	Nexy	0000 Contact: 919E5AE9-2160-41DC-8E41-9C2536932C86:ABPerson
default	22:07:40.465559-0500	Nexy	0000 Contact: 8FC46F73-8C76-4F4F-A480-86AD43FB3197:ABPerson
default	22:07:40.465567-0500	Nexy	0000 Contact: 758B39F6-7626-4392-A342-2F56B6D94427:ABPerson
default	22:07:40.465588-0500	Nexy	0000 Contact: 8A6084C7-9664-4FCF-BD0E-DF7B4AE169BC:ABPerson
default	22:07:40.465594-0500	Nexy	0000 Contact: 51857A1F-41AD-4ABC-BC2E-82377C39162B:ABPerson
default	22:07:40.465606-0500	Nexy	0000 Contact: 0145E52B-5388-4DF4-9BA6-041E2688EA53:ABPerson
default	22:07:40.465635-0500	Nexy	0000 Contact: 7C58562E-BF30-4BE5-AC33-E0A88F42AB76:ABPerson
default	22:07:40.465656-0500	Nexy	0000 Contact: C7C8564C-DF73-4360-B286-BB2CF4C72F17:ABPerson
default	22:07:40.465662-0500	Nexy	0000 Contact: F9EE7585-B534-46B5-848E-58FFD7152121:ABPerson
default	22:07:40.465667-0500	Nexy	0000 Contact: DABCF335-B625-47DD-918B-704381FD587D:ABPerson
default	22:07:40.465675-0500	Nexy	0000 Contact: A68807CD-0A21-4F90-BE39-09BAF83835E8:ABPerson
default	22:07:40.465679-0500	Nexy	0000 Contact: 3B7F983F-D8F3-400C-8462-CA84B84968A4:ABPerson
default	22:07:40.465686-0500	Nexy	0000 Contact: BE53EA52-E9F8-4C18-8446-4FA2489ADE02:ABPerson
default	22:07:40.465704-0500	Nexy	0000 Contact: A804F4AE-3921-4E55-83D8-094B7C4F17A3:ABPerson
default	22:07:40.465724-0500	Nexy	0000 Contact: 489A6364-6AEC-4FC5-8F52-FC08E5527BA0:ABPerson
default	22:07:40.465733-0500	Nexy	0000 Contact: B43BC68C-E9BB-48C1-98C3-A32A09C9A802:ABPerson
default	22:07:40.465738-0500	Nexy	0000 Contact: 05518C4D-4F67-4CD6-83D7-85AA7F2525A5:ABPerson
default	22:07:40.465748-0500	Nexy	0000 Contact: 955CE160-9CC8-4013-829C-A68FD99C7595:ABPerson
default	22:07:40.465756-0500	Nexy	0000 Contact: C13FF96F-DEF6-4C53-83DE-4B45963DD9AF:ABPerson
default	22:07:40.465791-0500	Nexy	0000 Contact: AE65B570-135A-4B14-BA64-EC538224DA56:ABPerson
default	22:07:40.465800-0500	Nexy	0000 Contact: C2132A98-A61A-4358-A681-AF1A1DA20915:ABPerson
default	22:07:40.465806-0500	Nexy	0000 Contact: C3CC1CBC-2410-4DA6-A83E-0477D239E755:ABPerson
default	22:07:40.465811-0500	Nexy	0000 Contact: 0FB60F1D-91EC-4396-A66A-69F15AF14BC5:ABPerson
default	22:07:40.465816-0500	Nexy	0000 Contact: FC6CD704-B936-454E-9EBD-E1701A5DE7D8:ABPerson
default	22:07:40.465822-0500	Nexy	0000 Contact: ED88C6F4-1641-473F-A5BC-DA8C11FCE9D2:ABPerson
default	22:07:40.465835-0500	Nexy	0000 Contact: 88083F13-CF73-4821-896D-8C9EDB5E9029:ABPerson
default	22:07:40.465852-0500	Nexy	0000 Contact: C5BAA4A8-B489-4A59-9400-5C0DFDAA91CA:ABPerson
default	22:07:40.465858-0500	Nexy	0000 Contact: F0187322-8BFE-4EE7-BA9E-BF7D7A056616:ABPerson
default	22:07:40.465868-0500	Nexy	0000 Contact: BA26FE3B-CB6A-471A-8E10-5000CF5332C2:ABPerson
default	22:07:40.465922-0500	Nexy	0000 Contact: DB250DFB-C87D-447B-B125-220B6E3DA663:ABPerson
default	22:07:40.465934-0500	Nexy	0000 Contact: B436BB91-BBBB-49E7-9C6A-93DDDD421478:ABPerson
default	22:07:40.465941-0500	Nexy	0000 Contact: DFCC4D11-6BC3-4ACD-B8C6-F8C46F7C8369:ABPerson
default	22:07:40.465950-0500	Nexy	0000 Contact: 0B435818-E34A-41BF-8808-417BCB956E97:ABPerson
default	22:07:40.465959-0500	Nexy	0000 Contact: E336CBFC-CF06-4672-BEF7-926884FB9BC8:ABPerson
default	22:07:40.465965-0500	Nexy	0000 Contact: A04F02F1-D5E5-4B3E-B5D0-287A46E6DB37:ABPerson
default	22:07:40.465970-0500	Nexy	0000 Contact: 274D78AE-37CF-4B30-B57D-D218F7D433BC:ABPerson
default	22:07:40.465977-0500	Nexy	0000 Contact: AFC75DDF-9D56-451F-8FFA-33CEF512BC9E:ABPerson
default	22:07:40.465984-0500	Nexy	0000 Contact: 36B84A8B-DD90-4609-9407-3BED73397C90:ABPerson
default	22:07:40.465991-0500	Nexy	0000 Contact: 25B2E948-39F0-4DA0-984A-6EAAFC4452BF:ABPerson
default	22:07:40.465997-0500	Nexy	0000 Contact: FD3874CC-9147-45D7-9635-BA7057F1E4CE:ABPerson
default	22:07:40.466003-0500	Nexy	0000 Contact: 93C427E1-DE52-48BF-AFC1-082EC9E9EDA0:ABPerson
default	22:07:40.466010-0500	Nexy	0000 Contact: 0ADD2D08-B0E0-4789-8BA5-3036146B6B78:ABPerson
default	22:07:40.466031-0500	Nexy	0000 Contact: C1626763-A8D5-4907-A0D9-325529F3E7B5:ABPerson
default	22:07:40.466038-0500	Nexy	0000 Contact: A691F96E-80C3-406D-A1F3-443C491D30D0:ABPerson
default	22:07:40.466044-0500	Nexy	0000 Contact: 331AE8C5-F99D-4F0A-B33F-36D558A607C3:ABPerson
default	22:07:40.466078-0500	Nexy	0000 Contact: 5C041266-AB76-41D1-BBBA-5FE4A4792084:ABPerson
default	22:07:40.466088-0500	Nexy	0000 Contact: F3BDC31E-20AF-4198-B696-F389C8F31C9F:ABPerson
default	22:07:40.466157-0500	Nexy	0000 Contact: 0CC4651C-3FC4-4644-BAB9-41107FBFF900:ABPerson
default	22:07:40.466169-0500	Nexy	0000 Contact: 9C0BE147-A58C-44D2-9C4A-FC7DFE653F3E:ABPerson
default	22:07:40.466176-0500	Nexy	0000 Contact: 0C5D18DF-0E63-4D12-AB19-70F9449BFDD3:ABPerson
default	22:07:40.466183-0500	Nexy	0000 Contact: 1EB1F958-3A33-4C17-AEFC-E59EA17F5D5B:ABPerson
default	22:07:40.466191-0500	Nexy	0000 Contact: E9510B2D-16FE-4F94-BBBE-BFACDEEF0759:ABPerson
default	22:07:40.466197-0500	Nexy	0000 Contact: 5D99F42B-5A12-4DD2-9DA9-063C524A30C7:ABPerson
default	22:07:40.466203-0500	Nexy	0000 Contact: 7C44FDAA-3756-43F4-B87F-DDA61E480B1C:ABPerson
default	22:07:40.466209-0500	Nexy	0000 Contact: DFDA976C-6D05-4677-AAA2-604A3688988F:ABPerson
default	22:07:40.466217-0500	Nexy	0000 Contact: 91B8C6A6-858C-4158-B742-E97BCFF7F054:ABPerson
default	22:07:40.466227-0500	Nexy	0000 Contact: 2A16F554-F4B5-4D1A-84FF-1B1B9CD41A6F:ABPerson
default	22:07:40.466236-0500	Nexy	0000 Contact: 51FDBD11-7239-4140-9605-7B2CFF1426E4:ABPerson
default	22:07:40.466243-0500	Nexy	0000 Contact: 2F813EA9-9EFC-409F-A1C4-64F820E4D179:ABPerson
default	22:07:40.466249-0500	Nexy	0000 Contact: 6B7D950D-D374-429D-91CE-A6E1B5D41AAA:ABPerson
default	22:07:40.466260-0500	Nexy	0000 Contact: F7679D0A-6363-40EC-A12A-63E9F2C28321:ABPerson
default	22:07:40.466268-0500	Nexy	0000 Contact: 6703F826-C4D7-43ED-83B5-77B3CBF74E39:ABPerson
default	22:07:40.466289-0500	Nexy	0000 Contact: ED036238-8F1A-4104-98CA-4C44E9BC5990:ABPerson
default	22:07:40.466299-0500	Nexy	0000 Contact: 00F2C374-C9A3-4DD0-B92B-E70CEFC1C968:ABPerson
default	22:07:40.466305-0500	Nexy	0000 Contact: E984A144-E505-46AA-AA38-1CF1EE5DF265:ABPerson
default	22:07:40.466311-0500	Nexy	0000 Contact: 444D762E-7CC5-479E-B3C7-D5172CE8F56B:ABPerson
default	22:07:40.466352-0500	Nexy	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	22:07:40.466408-0500	Nexy	0000 Contact: AA3A68CB-8A4B-4BAD-94D4-F0B1FDEF6AD2:ABPerson
default	22:07:40.466420-0500	Nexy	0000 Contact: B729AB23-719C-4993-99D4-97F17990CA6E:ABPerson
default	22:07:40.466428-0500	Nexy	0000 Contact: DDD6C0A5-9D08-4756-BB6E-06612386E694:ABPerson
default	22:07:40.466437-0500	Nexy	0000 Contact: DAA81742-1BAC-4E0A-86AB-1805922F5BFB:ABPerson
default	22:07:40.466443-0500	Nexy	0000 Contact: CCCE8074-7CFC-4765-87C4-3DA3398ED5E3:ABPerson
default	22:07:40.466465-0500	Nexy	0000 Contact: B3126A39-DB1F-4EB9-BA9E-057A701FEADB:ABPerson
default	22:07:40.466474-0500	Nexy	0000 Contact: D7A6F43C-FFAB-4219-B325-4345A3EBA5B5:ABPerson
default	22:07:40.466480-0500	Nexy	0000 Contact: F3959633-1472-4370-AE25-6C163A86F28A:ABPerson
default	22:07:40.466619-0500	Nexy	0000 Contact: 818A8D3F-5A2E-44CA-B4CF-47B295DB8C98:ABPerson
default	22:07:40.466628-0500	Nexy	0000 Contact: 228410FA-14BD-488B-A385-35C7112B9635:ABPerson
default	22:07:40.466634-0500	Nexy	0000 Contact: 1A2FDBB3-F370-4D0F-8C9A-34D9C191D7E3:ABPerson
default	22:07:40.466640-0500	Nexy	0000 Contact: 5FDB4463-1088-4EF5-9E20-48795D669908:ABPerson
default	22:07:40.466648-0500	Nexy	0000 Contact: 241E5174-F04C-45D2-BB1E-C4295A53CA80:ABPerson
default	22:07:40.466662-0500	Nexy	0000 Contact: 135FEF8F-5A69-49C6-97E1-E218FAD43A7E:ABPerson
default	22:07:40.466685-0500	Nexy	0000 Contact: F7BF6E9A-A1DE-4F0A-B9FE-DD0E61EBC464:ABPerson
default	22:07:40.466691-0500	Nexy	0000 Contact: F4DA25ED-6C3C-44D5-8A9B-87F14829E713:ABPerson
default	22:07:40.466716-0500	Nexy	0000 Contact: 95FF7EB7-87CC-416D-8811-B8DCC6FE7621:ABPerson
default	22:07:40.466747-0500	Nexy	0000 Contact: 751FAE5C-98A6-414E-B107-317AF0CBED37:ABPerson
default	22:07:40.466753-0500	Nexy	0000 Contact: 5465ECDD-A832-402B-BB73-FDF36810C6E0:ABPerson
default	22:07:40.466778-0500	Nexy	0000 Contact: 52FD2EC7-BEF6-4D05-BCAC-73FBAA131CDF:ABPerson
default	22:07:40.466789-0500	Nexy	0000 Contact: 9D848D63-FDF8-461C-9756-F8AAC3070EFF:ABPerson
default	22:07:40.466824-0500	Nexy	0000 Contact: D6BF6AC9-65CA-41BE-AFA2-C3071A2539F5:ABPerson
default	22:07:40.466860-0500	Nexy	0000 Contact: 4E4C0E62-3EE9-4F23-A226-025907D6882D:ABPerson
default	22:07:40.466869-0500	Nexy	0000 Contact: 1006869C-954C-4394-BFE9-09E9CE09AFB5:ABPerson
default	22:07:40.466873-0500	Nexy	0000 Contact: 339B0201-420C-414B-96CB-1D8150AEF6BB:ABPerson
default	22:07:40.466896-0500	Nexy	0000 Contact: 6A713058-BCB2-4635-BC21-577F0261940C:ABPerson
default	22:07:40.466919-0500	Nexy	0000 Contact: 8B61AAC1-DF6F-440A-B5AC-33331AF930E1:ABPerson
default	22:07:40.466937-0500	Nexy	0000 Contact: B5C0C11D-6F8A-4CCE-872A-DEC086F666A6:ABPerson
default	22:07:40.466948-0500	Nexy	0000 Contact: D17EDFE8-D58A-41FF-B738-D480ED1B54BB:ABPerson
default	22:07:40.466957-0500	Nexy	0000 Contact: 8D969F0D-4878-45C3-A329-14C8F1B9A1C4:ABPerson
default	22:07:40.466988-0500	Nexy	0000 Contact: 4DC763F6-4288-4A25-AE37-52DAC0E54434:ABPerson
default	22:07:40.467036-0500	Nexy	0000 Contact: BB62CE57-7037-4156-BE7F-D1E84FA0B46F:ABPerson
default	22:07:40.467051-0500	Nexy	0000 Contact: 32598CF7-ABA5-4AF8-B60C-8B3F9BB79824:ABPerson
default	22:07:40.467076-0500	Nexy	0000 Contact: 4C93D59E-2641-437E-8D5E-6E5135B4B9D7:ABPerson
default	22:07:40.467116-0500	Nexy	0000 Contact: 95C0601A-0362-4E71-9B56-8E66BA6334DB:ABPerson
default	22:07:40.467149-0500	Nexy	0000 Contact: F23EFEDD-DB9E-4EEE-86A8-A0BB0B161DCE:ABPerson
default	22:07:40.467207-0500	Nexy	0000 Contact: A25C8DA8-E066-47BE-A228-BA3A79122649:ABPerson
default	22:07:40.467241-0500	Nexy	0000 Contact: 7709CB5C-F45D-4130-AFCC-F66EB248B381:ABPerson
default	22:07:40.467325-0500	Nexy	0000 Contact: A95901C1-18E2-412B-9429-B9A87D46EEF1:ABPerson
default	22:07:40.467334-0500	Nexy	0000 Contact: 90CCE3F7-7CB8-44CE-8E3B-0E1FEE5B8574:ABPerson
default	22:07:40.467394-0500	Nexy	0000 Contact: D21F44BE-5C0B-49C1-ACBC-50C7FDD0E574:ABPerson
default	22:07:40.467427-0500	Nexy	0000 Contact: 9A341135-6F8F-42C6-A5D8-776E0F0EF424:ABPerson
default	22:07:40.467443-0500	Nexy	0000 Contact: 60C9F9CC-1758-4215-94FA-79E8E5591D0D:ABPerson
default	22:07:40.467470-0500	Nexy	0000 Contact: 7A0D8FED-170A-4F26-B868-532276E4BDF6:ABPerson
default	22:07:40.467478-0500	Nexy	0000 Contact: 791662EB-B4C3-41EA-8207-065A1C9F0AA0:ABPerson
default	22:07:40.467484-0500	Nexy	0000 Contact: D5AB1F03-8C06-438F-8713-DCCBBCD76892:ABPerson
default	22:07:40.467503-0500	Nexy	0000 Contact: 96EC0E50-9CC0-4769-8082-E7C877889553:ABPerson
default	22:07:40.467519-0500	Nexy	0000 Contact: 33394098-1926-4C5F-AA29-7B8610A5C7E6:ABPerson
default	22:07:40.467552-0500	Nexy	0000 Contact: B5956767-6E1D-49F2-8708-69E0D16EC786:ABPerson
default	22:07:40.467561-0500	Nexy	0000 Contact: 918AF5E7-EDE6-400D-A786-261C7B3BC323:ABPerson
default	22:07:40.467567-0500	Nexy	0000 Contact: 78374AF4-D2CF-4636-B824-5922E7BCDAA7:ABPerson
default	22:07:40.467575-0500	Nexy	0000 Contact: E1E5926D-F19D-45D4-9FFE-12E3198D0E67:ABPerson
default	22:07:40.467580-0500	Nexy	0000 Contact: DB957E68-3771-4194-AB47-1B347BE66F63:ABPerson
default	22:07:40.467591-0500	Nexy	0000 Contact: 2112C6EB-840A-49FE-B03E-5DDBFE2F6992:ABPerson
default	22:07:40.467605-0500	Nexy	0000 Contact: 3E8DAA1B-0AD6-465E-BDAB-A68A5FD23D3E:ABPerson
default	22:07:40.467618-0500	Nexy	0000 Contact: 5B8A6BDC-5927-4718-B89F-674DCC70DA16:ABPerson
default	22:07:40.467638-0500	Nexy	0000 Contact: 44BFDAD7-D780-4604-8369-CD3317F7F3FB:ABPerson
default	22:07:40.467647-0500	Nexy	0000 Contact: DD452BC2-AA0F-4E55-9417-30946834E7D9:ABPerson
default	22:07:40.467653-0500	Nexy	0000 Contact: A79E1C58-6726-4518-9160-5833FD1D9E85:ABPerson
default	22:07:40.467672-0500	Nexy	0000 Contact: EEDB6E81-803C-4D9E-9479-23840064FF07:ABPerson
default	22:07:40.467685-0500	Nexy	0000 Contact: E8BAA178-7C7C-4B0C-837F-07B80E6A8155:ABPerson
default	22:07:40.467700-0500	Nexy	0000 Contact: A8C84C99-FF9C-48DF-A603-CEB3050F0BC6:ABPerson
default	22:07:40.467715-0500	Nexy	0000 Contact: 0FD65269-7801-440C-A119-71EBE23C4E70:ABPerson
default	22:07:40.467730-0500	Nexy	0000 Contact: 0A4FEAE5-C426-4926-8B49-A5260D97B9E6:ABPerson
default	22:07:40.467746-0500	Nexy	0000 Contact: CA81313F-6121-4FF6-B60C-EEE869ECF990:ABPerson
default	22:07:40.467761-0500	Nexy	0000 Contact: EA9B96E2-2F87-4EB2-AD12-46F37DFF0EC9:ABPerson
default	22:07:40.467778-0500	Nexy	0000 Contact: 7A89C56B-6D06-419B-A08D-00F14B94AA1C:ABPerson
default	22:07:40.467792-0500	Nexy	0000 Contact: 660A1E96-3CA3-48B5-B94A-96D6D35A72E6:ABPerson
default	22:07:40.467798-0500	Nexy	0000 Contact: 3F5D85F3-9B89-4AD7-A353-FEFEA5DA1C36:ABPerson
default	22:07:40.467814-0500	Nexy	0000 Contact: 8F99EACB-5E71-4F4C-9899-AE7E1FF5280E:ABPerson
default	22:07:40.467828-0500	Nexy	0000 Contact: 9E8B52AD-B9B2-41CA-8134-7861A90F9A02:ABPerson
default	22:07:40.467842-0500	Nexy	0000 Contact: 98237DEC-70B4-4CA5-A4B8-FEE401C3F3C4:ABPerson
default	22:07:40.467856-0500	Nexy	0000 Contact: BD690A56-23D5-4941-B041-50C06351C977:ABPerson
default	22:07:40.467871-0500	Nexy	0000 Contact: D191A589-BA65-49F2-86A3-08D90FB284FD:ABPerson
default	22:07:40.467884-0500	Nexy	0000 Contact: AAF5FE8A-214C-4B65-9B4F-C2578C97C51D:ABPerson
default	22:07:40.467896-0500	Nexy	0000 Contact: 3D737248-8F03-4732-8B3A-8CDA2D45B5AA:ABPerson
default	22:07:40.467912-0500	Nexy	0000 Contact: E120A189-E8F5-4B5F-A2A2-B1A60E6DF145:ABPerson
default	22:07:40.467920-0500	Nexy	0000 Contact: 46187B48-32E0-4B21-B7CE-D3B44766EEEC:ABPerson
default	22:07:40.467935-0500	Nexy	0000 Contact: B72ACD21-62D9-4BC2-8F5A-F33464EEEED5:ABPerson
default	22:07:40.467941-0500	Nexy	0000 Contact: 1D1B1CB1-D316-4BC5-B11C-BC2D4D437605:ABPerson
default	22:07:40.467957-0500	Nexy	0000 Contact: EEC7F987-F555-4025-8B35-10CBE93E26D7:ABPerson
default	22:07:40.467972-0500	Nexy	0000 Contact: A4F96105-C3FC-4D3D-842F-E729A3F28760:ABPerson
default	22:07:40.467988-0500	Nexy	0000 Contact: F0613D78-6887-4B13-AC52-703B5D1A7060:ABPerson
default	22:07:40.468000-0500	Nexy	0000 Contact: BDD5E012-4C2D-4949-9778-80672887C0EC:ABPerson
default	22:07:40.468015-0500	Nexy	0000 Contact: E03CBC1C-C4D5-476B-A9AE-20A246A5FE73:ABPerson
default	22:07:40.468034-0500	Nexy	0000 Contact: A9567605-C983-4D5B-9877-2D3BC5D341CF:ABPerson
default	22:07:40.468051-0500	Nexy	0000 Contact: 378D10F9-7887-44F8-B0A5-9683F2AF012D:ABPerson
default	22:07:40.468061-0500	Nexy	0000 Contact: 29F7EE25-03CA-4DEA-AB4C-5E84B0046094:ABPerson
default	22:07:40.468072-0500	Nexy	0000 Contact: 6045438B-32EF-4240-BCDE-3A83DD6098C1:ABPerson
default	22:07:40.468086-0500	Nexy	0000 Contact: CC00B3CB-4536-414F-8E8F-116901AAAB66:ABPerson
default	22:07:40.468101-0500	Nexy	0000 Contact: CDF1FCD3-669F-4B16-9D7A-07091B53B43E:ABPerson
default	22:07:40.468116-0500	Nexy	0000 Contact: 1C7A8AAA-2853-4C56-892C-93832C406B2F:ABPerson
default	22:07:40.468128-0500	Nexy	0000 Contact: 5FA233B8-A72C-468F-8344-138CB3A320AD:ABPerson
default	22:07:40.468142-0500	Nexy	0000 Contact: CC42A082-921C-4A2F-9B2A-20AD5E63DE26:ABPerson
default	22:07:40.468156-0500	Nexy	0000 Contact: 4D22B39B-A7C9-4F71-B531-0D0A75E819DC:ABPerson
default	22:07:40.468170-0500	Nexy	0000 Contact: 10DA5D0D-F87E-40C2-A2FB-1B4E18ADEED7:ABPerson
default	22:07:40.468183-0500	Nexy	0000 Contact: 1020F64F-877A-46EF-A85B-0B7B4702F30A:ABPerson
default	22:07:40.468199-0500	Nexy	0000 Contact: 7A3258A0-4EF6-4C07-8BAC-DE67AFC5BF0F:ABPerson
default	22:07:40.468214-0500	Nexy	0000 Contact: D8BF88A0-50CD-408B-91AC-FABB6153F0E7:ABPerson
default	22:07:40.468228-0500	Nexy	0000 Contact: F96FB111-3581-4F57-A0DB-8D18E0A5CE3D:ABPerson
default	22:07:40.468240-0500	Nexy	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	22:07:40.468252-0500	Nexy	0000 Contact: 2DD46A4A-00EA-4AF2-BED6-A0E4704A401E:ABPerson
default	22:07:40.468266-0500	Nexy	0000 Contact: E75A43A8-9126-46AD-BDE0-2F09D8195FCE:ABPerson
default	22:07:40.468283-0500	Nexy	0000 Contact: 0CE70590-2C7E-400D-AAC3-E2AB83B20E6D:ABPerson
default	22:07:40.468297-0500	Nexy	0000 Contact: C93B2BF3-4882-418D-A785-20AABA5900CA:ABPerson
default	22:07:40.468311-0500	Nexy	0000 Contact: 72A79220-BD0A-4F38-A644-7891B8D6D08C:ABPerson
default	22:07:40.468322-0500	Nexy	0000 Contact: 5168F235-33BF-487B-9C88-9A0977EF3D96:ABPerson
default	22:07:40.468336-0500	Nexy	0000 Contact: EF5D8980-C0E4-4FBD-8942-AC7EC9F886BE:ABPerson
default	22:07:40.468349-0500	Nexy	0000 Contact: 8335160D-3EFF-4C7A-B500-08D4AAF9D6C4:ABPerson
default	22:07:40.468363-0500	Nexy	0000 Contact: F30C415E-480E-47D7-A697-2DDF78C62B78:ABPerson
default	22:07:40.468379-0500	Nexy	0000 Contact: 4B86EE6B-7192-4DEC-9A5D-DB2A68A29544:ABPerson
default	22:07:40.468393-0500	Nexy	0000 Contact: 7028A821-E1BB-4996-9F0A-B483955BBD46:ABPerson
default	22:07:40.468400-0500	Nexy	0000 Contact: 7C930844-C857-4F62-B795-A317F57982E7:ABPerson
default	22:07:40.468415-0500	Nexy	0000 Contact: 2958D2B1-193E-4859-97A7-E9D0A6DDAC5B:ABPerson
default	22:07:40.468422-0500	Nexy	0000 Contact: CF7AC9E0-68F2-4C92-A7E7-2F56630F8B8B:ABPerson
default	22:07:40.468436-0500	Nexy	0000 Contact: ADDCC376-3417-4952-A610-3D53B96EC2BD:ABPerson
default	22:07:40.468455-0500	Nexy	0000 Contact: 19855E2F-023D-4999-A9F8-0515B5257D6F:ABPerson
default	22:07:40.468461-0500	Nexy	0000 Contact: 2BAB4AEF-3D51-42E4-BBCA-4587A6EF5B42:ABPerson
default	22:07:40.468476-0500	Nexy	0000 Contact: B68F306A-9F87-4675-9C7C-73ADAC3CF928:ABPerson
default	22:07:40.468491-0500	Nexy	0000 Contact: EBEFEBC5-E9A8-48CB-B48D-DE0E2C3AE2B9:ABPerson
default	22:07:40.468499-0500	Nexy	0000 Contact: C1E29AB3-927E-4614-A170-469712D37DE0:ABPerson
default	22:07:40.468514-0500	Nexy	0000 Contact: 1E18829A-DFA4-4A9A-AEBA-FFF85B2D3E00:ABPerson
default	22:07:40.468527-0500	Nexy	0000 Contact: 41E94FCB-1477-45AF-AB50-6AF7C4651D76:ABPerson
default	22:07:40.468540-0500	Nexy	0000 Contact: 55D05EF1-7380-43F3-9CCC-FCCBB0A382A9:ABPerson
default	22:07:40.468555-0500	Nexy	0000 Contact: 88B8B688-3607-4FD1-BE7E-73F6DAA20674:ABPerson
default	22:07:40.468564-0500	Nexy	0000 Contact: 6A7FA276-678E-44BC-A5CD-1E7AB887CD37:ABPerson
default	22:07:40.468579-0500	Nexy	0000 Contact: A6FD2708-9CD8-45E0-9E88-5BE836285468:ABPerson
default	22:07:40.468590-0500	Nexy	0000 Contact: FFBA4F3C-8FF6-4FC6-9CB6-F62755FFB90C:ABPerson
default	22:07:40.468605-0500	Nexy	0000 Contact: F5A10DB4-BCD8-4342-9435-C976615D2367:ABPerson
default	22:07:40.468617-0500	Nexy	0000 Contact: 1C210F17-EE8F-4513-8100-4877479969F3:ABPerson
default	22:07:40.468631-0500	Nexy	0000 Contact: E6ACEB4F-3D7F-4D37-8463-568D34A3D393:ABPerson
default	22:07:40.468647-0500	Nexy	0000 Contact: 05B170A2-D739-4BCB-A7A9-927DAAC7B3FD:ABPerson
default	22:07:40.468661-0500	Nexy	0000 Contact: 791F5495-5017-4DBF-ABB6-4220285C8A7F:ABPerson
default	22:07:40.468673-0500	Nexy	0000 Contact: DFA3FE46-B8CF-41EC-B2E6-04C798B63209:ABPerson
default	22:07:40.468688-0500	Nexy	0000 Contact: 09772BD5-23E2-45C0-8579-EAA3F5DFAA04:ABPerson
default	22:07:40.468703-0500	Nexy	0000 Contact: 21D1D25A-A332-455E-BF6D-219DAED4CF2E:ABPerson
default	22:07:40.468717-0500	Nexy	0000 Contact: 85CBC919-29F4-4481-90E8-91811DF04251:ABPerson
default	22:07:40.468730-0500	Nexy	0000 Contact: 7D4E6C00-B562-4BD3-84B2-BE3484A218DC:ABPerson
default	22:07:40.468744-0500	Nexy	0000 Contact: 7CEA1D92-BD70-4661-A995-FC9C088765E4:ABPerson
default	22:07:40.468758-0500	Nexy	0000 Contact: 5BC153A8-ECD2-4153-8199-62D228ED9EFF:ABPerson
default	22:07:40.468771-0500	Nexy	0000 Contact: 539E00F6-4B11-4899-9B48-833F1C83B1AF:ABPerson
default	22:07:40.468785-0500	Nexy	0000 Contact: 480BDC40-266E-44A2-A7F0-81FF207F9107:ABPerson
default	22:07:40.468797-0500	Nexy	0000 Contact: AD76EC2F-309C-4663-88AB-5380B537AD21:ABPerson
default	22:07:40.468811-0500	Nexy	0000 Contact: E8D00EFB-149F-4D70-9E53-DCC37B11CA41:ABPerson
default	22:07:40.468825-0500	Nexy	0000 Contact: F1AC5DD9-2463-40B4-A31D-D698D4A81A07:ABPerson
default	22:07:40.468836-0500	Nexy	0000 Contact: 5CC4AD9E-AFA2-4D91-93BB-A2AEE0287CA1:ABPerson
default	22:07:40.468847-0500	Nexy	0000 Contact: 82273310-7E56-45DD-8F38-49E6EFB991AF:ABPerson
default	22:07:40.468861-0500	Nexy	0000 Contact: 52C4710F-7736-48E9-81CB-BFB715D2471F:ABPerson
default	22:07:40.468873-0500	Nexy	0000 Contact: 3DAF2C1D-E01A-4ECE-88B6-7A1FEC8F43AC:ABPerson
default	22:07:40.468887-0500	Nexy	0000 Contact: C66A3203-5558-449A-90CB-DECEC564C830:ABPerson
default	22:07:40.468899-0500	Nexy	0000 Contact: 1587F0BD-924E-4B7A-B625-9C3C29B7D02B:ABPerson
default	22:07:40.468914-0500	Nexy	0000 Contact: 8E669F37-64D4-4FCD-83DF-C7AB7025BAED:ABPerson
default	22:07:40.468928-0500	Nexy	0000 Contact: 42E8C30D-1FB0-42FC-833E-588AB5BBE3DB:ABPerson
default	22:07:40.468941-0500	Nexy	0000 Contact: EAE3066F-0C4F-41A6-8DBE-F68459786EC0:ABPerson
default	22:07:40.468955-0500	Nexy	0000 Contact: 2AF16E0B-3963-42BF-9826-D9FEA11B3CCA:ABPerson
default	22:07:40.468969-0500	Nexy	0000 Contact: 319E891D-32E9-49AF-B4E4-B5BAE8155200:ABPerson
default	22:07:40.468982-0500	Nexy	0000 Contact: 1594CB17-7E0F-473A-929D-C52CB3C2ADF4:ABPerson
default	22:07:40.468996-0500	Nexy	0000 Contact: 77010702-80A2-4E97-B0A7-B2EE441BFF58:ABPerson
default	22:07:40.469010-0500	Nexy	0000 Contact: 878309A1-31D9-4B89-8226-32C4BFA85E5A:ABPerson
default	22:07:40.469022-0500	Nexy	0000 Contact: 8C53459B-D709-4754-8779-C759C5D30623:ABPerson
default	22:07:40.469038-0500	Nexy	0000 Contact: 2D7A7BAB-3BDE-4E62-9336-46D7687262C6:ABPerson
default	22:07:40.469048-0500	Nexy	0000 Contact: ADE039BB-356A-4FF6-9B48-11643C1A74A3:ABPerson
default	22:07:40.469063-0500	Nexy	0000 Contact: 1DAA78BA-EBAD-4BF6-B582-A4DE8A4A1F60:ABPerson
default	22:07:40.469078-0500	Nexy	0000 Contact: E3B3AD82-9DE2-41D8-BAB4-955DF431F0D7:ABPerson
default	22:07:40.469091-0500	Nexy	0000 Contact: 4EA7F008-36E8-457A-AB52-5E92AB655707:ABPerson
default	22:07:40.469105-0500	Nexy	0000 Contact: 2EE1FF46-FBE2-4A40-8CE4-EC8C163406A8:ABPerson
default	22:07:40.469119-0500	Nexy	0000 Contact: 4749FF87-CDF6-4765-A605-FBF954CEC3DD:ABPerson
default	22:07:40.469131-0500	Nexy	0000 Contact: 78533628-5040-45D4-907C-06311D0B83C8:ABPerson
default	22:07:40.469146-0500	Nexy	0000 Contact: 55ED3DE3-FD66-4A5E-995C-7174A0F57355:ABPerson
default	22:07:40.469158-0500	Nexy	0000 Contact: 1EB3E13D-C8C2-40B4-B5C1-95672F5BB775:ABPerson
default	22:07:40.469172-0500	Nexy	0000 Contact: F83287C3-CE0B-407B-88A2-A5B43CAB98EC:ABPerson
default	22:07:40.469187-0500	Nexy	0000 Contact: 2D1AC54F-1C05-415F-803B-EB84B4DE155C:ABPerson
default	22:07:40.469197-0500	Nexy	0000 Contact: C8633A15-35F4-4ABC-9A2A-82EBF1A6767D:ABPerson
default	22:07:40.469212-0500	Nexy	0000 Contact: D62A5235-E401-4A9F-AC82-61328161530D:ABPerson
default	22:07:40.469218-0500	Nexy	0000 Contact: C80DE5B6-E12E-4835-863B-E63D84C0DEB5:ABPerson
default	22:07:40.469233-0500	Nexy	0000 Contact: 922530A8-0D72-4067-AAC0-1FF5C4ABE1BA:ABPerson
default	22:07:40.469247-0500	Nexy	0000 Contact: A66AB62E-7C4B-489D-A5AC-97BE240AF07B:ABPerson
default	22:07:40.469260-0500	Nexy	0000 Contact: C42862EB-E49A-4500-B5A0-744247A93DC0:ABPerson
default	22:07:40.469271-0500	Nexy	0000 Contact: 3608E376-1FDF-4DA6-94BE-B39CF8F32D25:ABPerson
default	22:07:40.469285-0500	Nexy	0000 Contact: 3D44B959-62DC-41CB-825F-C0FB5D231322:ABPerson
default	22:07:40.469300-0500	Nexy	0000 Contact: 47FCBCE3-65D3-44A4-8283-4C1AF6654C9F:ABPerson
default	22:07:40.469312-0500	Nexy	0000 Contact: 93BAC1B1-3857-40CA-A143-09E6F7A990EF:ABPerson
default	22:07:40.469326-0500	Nexy	0000 Contact: F1B433EB-BB39-4CD7-A784-1E41309B908C:ABPerson
default	22:07:40.469338-0500	Nexy	0000 Contact: A52B8A51-99C7-427A-BD9F-97EC5E9F7EA8:ABPerson
default	22:07:40.469350-0500	Nexy	0000 Contact: 0191E2F5-DF4D-441F-A40B-BBEE1682877B:ABPerson
default	22:07:40.469362-0500	Nexy	0000 Contact: 0697FA50-06C8-4FDB-A5D3-B10F8A859674:ABPerson
default	22:07:40.469377-0500	Nexy	0000 Contact: 093F142A-458F-4ACF-BEEE-FAB7BA5E520A:ABPerson
default	22:07:40.469389-0500	Nexy	0000 Contact: 98F95301-000C-4EF9-91DF-E637EF0C27F4:ABPerson
default	22:07:40.469403-0500	Nexy	0000 Contact: 720814F5-D603-40AE-A834-D49467F3A7FD:ABPerson
default	22:07:40.469419-0500	Nexy	0000 Contact: 40CDB1E4-DC18-4D79-AE2F-6242CCF62978:ABPerson
default	22:07:40.469433-0500	Nexy	0000 Contact: A8D9C348-1926-49B7-98C2-A2C917FB651B:ABPerson
default	22:07:40.469448-0500	Nexy	0000 Contact: 7656FBDF-5810-4382-9538-529EC1E5EF83:ABPerson
default	22:07:40.469470-0500	Nexy	0000 Contact: 8F442B0B-AFC7-4087-AEFC-FDC987F28E2C:ABPerson
default	22:07:40.469485-0500	Nexy	0000 Contact: DE96F2D0-DA7E-4742-AD3E-6D43BC32C213:ABPerson
default	22:07:40.469500-0500	Nexy	0000 Contact: DA1B14DD-D92B-4633-BF3C-0CCCE7117BE4:ABPerson
default	22:07:40.469511-0500	Nexy	0000 Contact: 0134E272-51ED-44B6-AC46-4C34642F56AA:ABPerson
default	22:07:40.469525-0500	Nexy	0000 Contact: FA551EE7-6781-4874-B9EA-0B6893B3293F:ABPerson
default	22:07:40.469537-0500	Nexy	0000 Contact: A88C8AF6-EF10-48E8-9C60-3709424155EB:ABPerson
default	22:07:40.469549-0500	Nexy	0000 Contact: C00692B4-EC26-459C-A690-D23F5BCEF621:ABPerson
default	22:07:40.469563-0500	Nexy	0000 Contact: 652921DA-B2DA-4539-A7F6-6B5A80149E2C:ABPerson
default	22:07:40.469577-0500	Nexy	0000 Contact: 88DED267-1D14-49FB-B0EA-D61FEEEA7475:ABPerson
default	22:07:40.469589-0500	Nexy	0000 Contact: CEB05018-C421-4234-BE90-56F8041F2286:ABPerson
default	22:07:40.469603-0500	Nexy	0000 Contact: DFB23C20-7349-4617-9A20-48014D8D844F:ABPerson
default	22:07:40.469615-0500	Nexy	0000 Contact: 9AC48DA6-FEAA-4630-AD56-EF041D62524A:ABPerson
default	22:07:40.469629-0500	Nexy	0000 Contact: 936230C2-1597-4A80-898D-31476BAE0C72:ABPerson
default	22:07:40.469643-0500	Nexy	0000 Contact: E99AC935-51E8-4AC2-9D90-C3ED9A41CF89:ABPerson
default	22:07:40.469655-0500	Nexy	0000 Contact: 1041C9F3-A247-4866-BCE3-A908919C3641:ABPerson
default	22:07:40.469669-0500	Nexy	0000 Contact: AA55B04C-AA66-4E4C-BE73-FCD01D057FF4:ABPerson
default	22:07:40.469681-0500	Nexy	0000 Contact: 8E1DE28A-250A-438D-ADCC-EC00B09AFDCF:ABPerson
default	22:07:40.469695-0500	Nexy	0000 Contact: 9D974937-BC35-459C-9596-7F3C287A39DE:ABPerson
default	22:07:40.469710-0500	Nexy	0000 Contact: 7A52455B-63F6-4500-850D-4CD4CAEE7CDA:ABPerson
default	22:07:40.469722-0500	Nexy	0000 Contact: BB0E685F-E844-4A51-8837-01C68FCCEECD:ABPerson
default	22:07:40.469737-0500	Nexy	0000 Contact: 958F31A6-1E1B-4833-99AC-EC3D8191CACE:ABPerson
default	22:07:40.469744-0500	Nexy	0000 Contact: 88212F02-02C2-4E0B-AD31-33A4F57D97C3:ABPerson
default	22:07:40.469764-0500	Nexy	0000 Contact: 060A07B0-DE54-4CA0-82F9-C5E7D642FE04:ABPerson
default	22:07:40.469778-0500	Nexy	0000 Contact: 84FD0E15-D8B4-4C4A-AF3F-ECACC4D7D2AB:ABPerson
default	22:07:40.469793-0500	Nexy	0000 Contact: E03C33D7-9B66-41CC-9823-13495C0F1BFF:ABPerson
default	22:07:40.469820-0500	Nexy	0000 Contact: 4F05D0EB-A7C7-4CE9-8BBE-252CDE0913B6:ABPerson
default	22:07:40.469835-0500	Nexy	0000 Contact: 0D4D94BE-BE27-4924-B1EF-D18DBC8CB9CB:ABPerson
default	22:07:40.469850-0500	Nexy	0000 Contact: DE3244DE-AA8B-42BE-9E6B-D93D5F072FC8:ABPerson
default	22:07:40.469865-0500	Nexy	0000 Contact: D2349093-8AC3-493E-A63B-2FDDBF010597:ABPerson
default	22:07:40.469877-0500	Nexy	0000 Contact: 582B6770-D754-4F28-BE23-DE8B912C1D70:ABPerson
default	22:07:40.469888-0500	Nexy	0000 Contact: 7230DAA8-42F7-4810-9E64-7E0576DEC21F:ABPerson
default	22:07:40.469898-0500	Nexy	0000 Contact: A044BEEF-238E-4A88-9B39-26B87097EDBA:ABPerson
default	22:07:40.469913-0500	Nexy	0000 Contact: 37C10F00-3A36-4D68-A9FE-F7CBB93250AA:ABPerson
default	22:07:40.469926-0500	Nexy	0000 Contact: BF90E79B-597F-4512-8E44-EA4CE870BBE2:ABPerson
default	22:07:40.469939-0500	Nexy	0000 Contact: BC75C771-F624-4E3A-AD7C-60B2F270D59D:ABPerson
default	22:07:40.469954-0500	Nexy	0000 Contact: C9795424-7E48-45EA-BBDF-4E008BDD9978:ABPerson
default	22:07:40.469969-0500	Nexy	0000 Contact: 40A1ED53-5876-46E0-B311-D54958985F34:ABPerson
default	22:07:40.469983-0500	Nexy	0000 Contact: 7E4C40BE-99FF-4182-ACF1-5DF8D2DDBE83:ABPerson
default	22:07:40.470000-0500	Nexy	0000 Contact: 6E048310-6707-4D3C-BD0B-81F080042AD6:ABPerson
default	22:07:40.470006-0500	Nexy	0000 Contact: 7268EB56-C8B9-4982-99B0-A40D08B65BA9:ABPerson
default	22:07:40.470016-0500	Nexy	0000 Contact: 0E2D5908-AAC6-40CB-BFB1-0CE7506D0A99:ABPerson
default	22:07:40.470031-0500	Nexy	0000 Contact: D2628142-CF91-46B0-A289-5CA32977E44D:ABPerson
default	22:07:40.470042-0500	Nexy	0000 Contact: 914E27F4-B07C-487A-BF66-F3CA485B9275:ABPerson
default	22:07:40.470057-0500	Nexy	0000 Contact: D014DC3B-188A-4277-A1D5-FBE211695D60:ABPerson
default	22:07:40.470069-0500	Nexy	0000 Contact: 48C9CC87-0557-4A05-B9B6-9FC3799AA710:ABPerson
default	22:07:40.470083-0500	Nexy	0000 Contact: D19BADAB-1850-4DC5-BEEF-B4D77FFCF312:ABPerson
default	22:07:40.470097-0500	Nexy	0000 Contact: 5F52D0B4-4801-47FD-A2E8-E1EC4C2CFBF7:ABPerson
default	22:07:40.470109-0500	Nexy	0000 Contact: F8F59880-57E4-410D-B266-90532EAA85ED:ABPerson
default	22:07:40.470124-0500	Nexy	0000 Contact: 894EBF35-6AF8-4262-8E87-8394A0235AEA:ABPerson
default	22:07:40.470135-0500	Nexy	0000 Contact: 57AEA313-D5E2-4575-AA16-1A5115913CC7:ABPerson
default	22:07:40.470149-0500	Nexy	0000 Contact: F89D0C36-26A8-41DC-83C9-B4FBE705654B:ABPerson
default	22:07:40.470161-0500	Nexy	0000 Contact: 1B9D8EA6-9499-4BFC-8492-1342D6A1460A:ABPerson
default	22:07:40.470175-0500	Nexy	0000 Contact: 35990211-93E2-4128-9887-673DB78EB237:ABPerson
default	22:07:40.470189-0500	Nexy	0000 Contact: E09D3D05-8D17-403A-BB6D-AE0A7DAC6A91:ABPerson
default	22:07:40.470199-0500	Nexy	0000 Contact: 6947AB19-73BD-4633-9B74-8444F2D5EB48:ABPerson
default	22:07:40.470212-0500	Nexy	0000 Contact: 327524E2-8EE7-43AD-A10C-4D95E5236B33:ABPerson
default	22:07:40.470227-0500	Nexy	0000 Contact: 5C927C23-EC97-4E44-979D-C91168A0225F:ABPerson
default	22:07:40.470240-0500	Nexy	0000 Contact: 3E96739C-79E5-47F2-8D58-297DAFFED273:ABPerson
default	22:07:40.470258-0500	Nexy	0000 Contact: 923B5225-B958-47B8-A994-56D2C6594BC3:ABPerson
default	22:07:40.470269-0500	Nexy	0000 Contact: 71E3945F-552E-4A87-81E7-3B4F6B837FB0:ABPerson
default	22:07:40.470283-0500	Nexy	0000 Contact: 98BB4D37-BA08-403B-863B-EA841E79DDEC:ABPerson
default	22:07:40.470294-0500	Nexy	0000 Contact: 3C958CB9-9822-42CE-908D-E1263845615F:ABPerson
default	22:07:40.470308-0500	Nexy	0000 Contact: 99F6FF83-6AC8-4BB2-A7FB-0E45BF397CE1:ABPerson
default	22:07:40.470320-0500	Nexy	0000 Contact: ECEB9C46-3E9A-4B07-BA0A-83A9F5AC9BD8:ABPerson
default	22:07:40.470335-0500	Nexy	0000 Contact: 2D8CF878-704D-4216-A869-2AA3CE40DC8B:ABPerson
default	22:07:40.470349-0500	Nexy	0000 Contact: D6E1C189-3EE0-4001-BBD7-BA1BAA052DCD:ABPerson
default	22:07:40.470355-0500	Nexy	0000 Contact: 0FB6D688-1124-496D-8A74-936908325AC4:ABPerson
default	22:07:40.470374-0500	Nexy	0000 Contact: 8E63BF2D-7068-4689-AA89-3F14A6D447C7:ABPerson
default	22:07:40.470387-0500	Nexy	0000 Contact: A6A438A5-EBCC-4387-AE2C-974496DF3475:ABPerson
default	22:07:40.470401-0500	Nexy	0000 Contact: A7980BCA-3250-42B1-9819-B7F094FC4046:ABPerson
default	22:07:40.470412-0500	Nexy	0000 Contact: 4C6A56D0-B520-49E0-8E8E-16BA4BC6CC20:ABPerson
default	22:07:40.470427-0500	Nexy	0000 Contact: C0FC9CF3-3693-4D44-981C-6047B6AEE5AB:ABPerson
default	22:07:40.470433-0500	Nexy	0000 Contact: 9436B5EC-36D3-4607-B5EB-7EF577DAA4E1:ABPerson
default	22:07:40.470448-0500	Nexy	0000 Contact: FC8D2904-8F71-4E20-8978-D780134A1143:ABPerson
default	22:07:40.470458-0500	Nexy	0000 Contact: 8E15809F-EDFE-43EB-A729-82985D40BEDD:ABPerson
default	22:07:40.470468-0500	Nexy	0000 Contact: 4CFCE671-0922-422E-84D2-7E3D755B9AA0:ABPerson
default	22:07:40.470483-0500	Nexy	0000 Contact: 97F9A37A-8704-4049-B22E-5464D3555283:ABPerson
default	22:07:40.470496-0500	Nexy	0000 Contact: 5EAB76EB-1518-4AB1-A60F-6440D4E97C67:ABPerson
default	22:07:40.470510-0500	Nexy	0000 Contact: 66AA346D-AFEA-46E3-AB76-B76AB73EEFE6:ABPerson
default	22:07:40.470520-0500	Nexy	0000 Contact: A94FA9D0-8D8F-482E-A1FA-415674AAE3CD:ABPerson
default	22:07:40.470532-0500	Nexy	0000 Contact: E26AEFB0-1D2D-4ED3-B1E2-B7D352747749:ABPerson
default	22:07:40.470547-0500	Nexy	0000 Contact: AE956307-DB6F-4D84-8479-F99A334DD9D9:ABPerson
default	22:07:40.470556-0500	Nexy	0000 Contact: D85CE9F6-4FD9-4FE4-BAC1-3B143BBF015B:ABPerson
default	22:07:40.470571-0500	Nexy	0000 Contact: D86C98C7-EA2A-4783-9D89-B5CCC7F3F76F:ABPerson
default	22:07:40.470585-0500	Nexy	0000 Contact: 9BD95D2C-57F9-41BC-82A1-01276B837DE5:ABPerson
default	22:07:40.470597-0500	Nexy	0000 Contact: D73A9313-DE0F-415F-AEB6-A3064AD4E8D4:ABPerson
default	22:07:40.470611-0500	Nexy	0000 Contact: 0D652AFC-47EC-4A75-8D39-2C5235F7B2D8:ABPerson
default	22:07:40.470623-0500	Nexy	0000 Contact: ACA1A5BD-6656-45E2-BD86-154568B82D42:ABPerson
default	22:07:40.470637-0500	Nexy	0000 Contact: 4EEB39AF-CB99-4D4F-99E0-813379D86B51:ABPerson
default	22:07:40.470650-0500	Nexy	0000 Contact: 37348E4E-8173-4E70-B552-CB72B6A9AF42:ABPerson
default	22:07:40.470664-0500	Nexy	0000 Contact: 3D23A662-D7CC-4235-A90D-B25C77F75FB1:ABPerson
default	22:07:40.470679-0500	Nexy	0000 Contact: F5DA0315-4AD8-41C4-B7CF-81A2E12E2691:ABPerson
default	22:07:40.470693-0500	Nexy	0000 Contact: 61773524-5763-4829-81ED-9B3EFF5744C8:ABPerson
default	22:07:40.470700-0500	Nexy	0000 Contact: 3A8DC04F-FBB6-495A-8E75-D22B3ACFD775:ABPerson
default	22:07:40.470715-0500	Nexy	0000 Contact: 8E1B53A0-CE9F-4B5A-BCD2-6FCBB2FE03C1:ABPerson
default	22:07:40.470731-0500	Nexy	0000 Contact: 927F81A1-D726-4969-8419-5DAAAB376B20:ABPerson
default	22:07:40.470742-0500	Nexy	0000 Contact: 499571CA-8847-4A36-8AFD-700D10BA01B6:ABPerson
default	22:07:40.470751-0500	Nexy	0000 Contact: 687940D3-01D3-4EE6-8DF6-B77137DF4358:ABPerson
default	22:07:40.470767-0500	Nexy	0000 Contact: AC2B4231-8E18-49D2-A6E0-4DAD10C52F8E:ABPerson
default	22:07:40.470782-0500	Nexy	0000 Contact: B9C8A612-D08C-4C98-AFEC-7B492BFFCF09:ABPerson
default	22:07:40.470793-0500	Nexy	0000 Contact: 4DE12C0D-88F3-46EA-AE7A-52A8C97B2642:ABPerson
default	22:07:40.470807-0500	Nexy	0000 Contact: 74E71AB9-12C3-492C-8D90-44002E96E279:ABPerson
default	22:07:40.470820-0500	Nexy	0000 Contact: F06E384F-51AB-4945-8C9A-CDDA3D1F1726:ABPerson
default	22:07:40.470834-0500	Nexy	0000 Contact: B4392798-7C17-4630-9433-A03FD74A67B6:ABPerson
default	22:07:40.470848-0500	Nexy	0000 Contact: 81B63730-E89B-4309-B937-6526BC363BE9:ABPerson
default	22:07:40.470861-0500	Nexy	0000 Contact: 67260B0D-B185-469D-A099-1F276E9003E9:ABPerson
default	22:07:40.470875-0500	Nexy	0000 Contact: 523939B5-07BC-4BA9-8827-8E5DE74ABD59:ABPerson
default	22:07:40.470884-0500	Nexy	0000 Contact: 448593D9-FFE0-4A5E-85CF-951EBD64FD34:ABPerson
default	22:07:40.470897-0500	Nexy	0000 Contact: 39E0059F-CE32-4A7F-8412-CBB5B8512D91:ABPerson
default	22:07:40.470909-0500	Nexy	0000 Contact: BD79F9BE-48FE-4B17-A966-4900444CB4BE:ABPerson
default	22:07:40.470921-0500	Nexy	0000 Contact: CB117BD9-26BB-482F-BE1D-474050D4F877:ABPerson
default	22:07:40.470935-0500	Nexy	0000 Contact: 1BE44750-F897-4471-B2BB-23F1750F6052:ABPerson
default	22:07:40.470948-0500	Nexy	0000 Contact: F521BF7D-BEA0-4970-8ABB-0D36D0C55CFB:ABPerson
default	22:07:40.470962-0500	Nexy	0000 Contact: B31F68AA-132A-4764-BF9C-07AFF1DFEBE9:ABPerson
default	22:07:40.470974-0500	Nexy	0000 Contact: BFC74FBC-8459-4E5C-926D-CA8CB584E493:ABPerson
default	22:07:40.470988-0500	Nexy	0000 Contact: 513D3922-7269-4052-92B9-A5DDC7F20D85:ABPerson
default	22:07:40.470999-0500	Nexy	0000 Contact: 1680643C-880B-4F66-A23A-54553511F91E:ABPerson
default	22:07:40.471013-0500	Nexy	0000 Contact: AC09AA75-399F-4388-B06D-B36195539921:ABPerson
default	22:07:40.471025-0500	Nexy	0000 Contact: 905AEE60-BF17-4861-8B9D-D8A7C93CA851:ABPerson
default	22:07:40.471040-0500	Nexy	0000 Contact: 605EC366-1BE6-4728-AF4F-35065DDE105E:ABPerson
default	22:07:40.471050-0500	Nexy	0000 Contact: 2E5AC2EB-1D50-48E4-A733-1565B7FBD9B0:ABPerson
default	22:07:40.471065-0500	Nexy	0000 Contact: 8DBBC6C7-2A3B-452A-A683-96B213129365:ABPerson
default	22:07:40.471077-0500	Nexy	0000 Contact: D1ABDE8F-AB3A-4A78-B366-8122520E469C:ABPerson
default	22:07:40.471091-0500	Nexy	0000 Contact: 2BBC7823-B462-47BC-97A1-FAF56A6CD6D4:ABPerson
default	22:07:40.471103-0500	Nexy	0000 Contact: CBBBAAFD-0C8A-4928-B6C5-104BD483B756:ABPerson
default	22:07:40.471117-0500	Nexy	0000 Contact: 7B546412-E513-4FAC-8F04-5B93F8284CD9:ABPerson
default	22:07:40.471131-0500	Nexy	0000 Contact: BEDFD270-E6D5-4BD4-9396-F461E76A3D6D:ABPerson
default	22:07:40.471143-0500	Nexy	0000 Contact: DFF04280-7038-4F29-96DF-CE1264E33F45:ABPerson
default	22:07:40.471158-0500	Nexy	0000 Contact: DA723208-FBEF-435F-9D7D-AF23C3292A04:ABPerson
default	22:07:40.471173-0500	Nexy	0000 Contact: 689B7484-1008-4903-8E58-C16D6135D1BE:ABPerson
default	22:07:40.471188-0500	Nexy	0000 Contact: 2EBB3BBB-AA1B-44AB-AEB2-507047DFB1BF:ABPerson
default	22:07:40.471195-0500	Nexy	0000 Contact: 2C4816A3-74B3-44EE-8613-D4A9EA487364:ABPerson
default	22:07:40.471205-0500	Nexy	0000 Contact: 327FE41D-07EB-426D-B40A-C41E6414A032:ABPerson
default	22:07:40.471220-0500	Nexy	0000 Contact: 661E42B6-4641-42DC-ADAD-F2F4F64E9A7F:ABPerson
default	22:07:40.471232-0500	Nexy	0000 Contact: 5B3F5B1B-AEB4-49F2-9295-98A6D2E90DF3:ABPerson
default	22:07:40.471246-0500	Nexy	0000 Contact: 3B9A0F65-3862-4239-9B4C-22A3937CB3E3:ABPerson
default	22:07:40.471257-0500	Nexy	0000 Contact: 1F5296B1-D8A8-4DEE-A3AC-4F6FF8EB8592:ABPerson
default	22:07:40.471271-0500	Nexy	0000 Contact: 83367917-4C48-420D-BED6-953D5D799BA3:ABPerson
default	22:07:40.471283-0500	Nexy	0000 Contact: CB81A645-AA3F-4E01-A5E8-7FFB1DE784B8:ABPerson
default	22:07:40.471297-0500	Nexy	0000 Contact: 76C1E860-76F6-46A7-AE8B-0B8D533979A1:ABPerson
default	22:07:40.471311-0500	Nexy	0000 Contact: 38D87E84-8FFA-4644-89BB-3B2C64683F25:ABPerson
default	22:07:40.471324-0500	Nexy	0000 Contact: BFC89011-6208-402B-902D-227391CF84D7:ABPerson
default	22:07:40.471335-0500	Nexy	0000 Contact: AE1E272C-12CF-4D37-AA16-321C66EB1922:ABPerson
default	22:07:40.471347-0500	Nexy	0000 Contact: 37AF5276-1B9C-4873-9D80-6BD7C5AE160B:ABPerson
default	22:07:40.471360-0500	Nexy	0000 Contact: 873FBA93-2932-4885-9ABA-B766E56EF823:ABPerson
default	22:07:40.471374-0500	Nexy	0000 Contact: DA14AB47-A56B-4F79-A505-4A5F3CF9709B:ABPerson
default	22:07:40.471388-0500	Nexy	0000 Contact: 5DBDC986-75E3-45D5-BDAC-840F64A095F3:ABPerson
default	22:07:40.471402-0500	Nexy	0000 Contact: 7E2E667C-A7D1-4A88-9C92-C2F38557DF00:ABPerson
default	22:07:40.471412-0500	Nexy	0000 Contact: 5307FC68-117A-42FB-92AA-DFB24F94E71D:ABPerson
default	22:07:40.471421-0500	Nexy	0000 Contact: 5F493737-ED28-4B1F-8903-5BA4CE98E525:ABPerson
default	22:07:40.471436-0500	Nexy	0000 Contact: 581AB38B-88DC-4442-B96C-20827400BCDB:ABPerson
default	22:07:40.471448-0500	Nexy	0000 Contact: E7A269EB-3583-4C11-9FA2-A805E372821C:ABPerson
default	22:07:40.471462-0500	Nexy	0000 Contact: 17A33554-E561-4BBD-9CEB-2A42D78570CB:ABPerson
default	22:07:40.471474-0500	Nexy	0000 Contact: B6294A95-D955-4DE1-981A-1C81A88B3C77:ABPerson
default	22:07:40.471488-0500	Nexy	0000 Contact: 2775B95B-E344-4E6E-860A-2E7C048D2F1D:ABPerson
default	22:07:40.471499-0500	Nexy	0000 Contact: C811339F-FA52-4CA4-B33E-D0F308EB497B:ABPerson
default	22:07:40.471515-0500	Nexy	0000 Contact: 3EBCE39A-CFA0-4AE5-A027-E77300906D8C:ABPerson
default	22:07:40.471523-0500	Nexy	0000 Contact: EE34E8D6-8FA8-43EA-956D-B93BBAEE1A85:ABPerson
default	22:07:40.471539-0500	Nexy	0000 Contact: 9502BE8E-CE6C-45C1-B06E-06F25C1B2DB2:ABPerson
default	22:07:40.471554-0500	Nexy	0000 Contact: CB72BAE7-75D4-4B69-B8B1-6F54BA25195A:ABPerson
default	22:07:40.471566-0500	Nexy	0000 Contact: 8ABDA833-5BB8-43D2-9DD4-D9977041708F:ABPerson
default	22:07:40.471580-0500	Nexy	0000 Contact: BC7FC3F8-6E58-42C6-8D38-58B4E05E74D8:ABPerson
default	22:07:40.471594-0500	Nexy	0000 Contact: 8C9E4B42-EDDD-4DA5-8291-79608D7118FD:ABPerson
default	22:07:40.471606-0500	Nexy	0000 Contact: 88A354D2-628D-4BBD-A9D2-4025114C2B74:ABPerson
default	22:07:40.471620-0500	Nexy	0000 Contact: D671E4A8-5C78-48DB-9F39-C9F55D0773F0:ABPerson
default	22:07:40.471632-0500	Nexy	0000 Contact: B55652C2-FF9A-492E-9E74-59BF77FF7657:ABPerson
default	22:07:40.471647-0500	Nexy	0000 Contact: D40BEEF6-659C-4640-8883-A886679E7683:ABPerson
default	22:07:40.471657-0500	Nexy	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	22:07:40.471672-0500	Nexy	0000 Contact: 2501625C-D3F0-448F-BE59-758CB4781991:ABPerson
default	22:07:40.471684-0500	Nexy	0000 Contact: 95793C06-46A7-463F-B79D-BD4828AA82E5:ABPerson
default	22:07:40.471694-0500	Nexy	0000 Contact: 39FB6543-CE8F-4850-B087-CB9BC9D83CD1:ABPerson
default	22:07:40.471709-0500	Nexy	0000 Contact: 4899EBC6-6B1B-4110-ACC0-42C6281F11F0:ABPerson
default	22:07:40.471721-0500	Nexy	0000 Contact: 2152007E-EC7F-40ED-A920-334BFEE05F62:ABPerson
default	22:07:40.471736-0500	Nexy	0000 Contact: E5FB73BD-A112-4CB1-A44C-4AE9AA8A7FD9:ABPerson
default	22:07:40.471749-0500	Nexy	0000 Contact: 9DF4B53B-8E66-438F-A541-31A6AC43028E:ABPerson
default	22:07:40.471762-0500	Nexy	0000 Contact: ED52C6FA-B011-454D-BF73-CD97015FEDF8:ABPerson
default	22:07:40.471776-0500	Nexy	0000 Contact: 637D6BED-2C4A-4F5E-9BF9-E5A8854E4DF1:ABPerson
default	22:07:40.471785-0500	Nexy	0000 Contact: 763CD797-4630-439F-982D-34ACFA2E7238:ABPerson
default	22:07:40.471792-0500	Nexy	0000 Contact: DE4A7BAA-4835-447E-9B59-F863ACBFA092:ABPerson
default	22:07:40.471807-0500	Nexy	0000 Contact: FE3ED792-5C16-4CA6-AD68-BBDFDF93EAC3:ABPerson
default	22:07:40.471843-0500	Nexy	0000 Contact: F5F336E5-374B-4E45-B851-690629571134:ABPerson
default	22:07:40.471849-0500	Nexy	0000 Contact: 00E52FC0-B1F1-47C4-A4E2-351A2927B2AC:ABPerson
default	22:07:40.471854-0500	Nexy	0000 Contact: 5AA6919D-04C9-470A-99B9-9FB0D437DA6A:ABPerson
default	22:07:40.471859-0500	Nexy	0000 Contact: 1FC22462-8E84-43E6-8F68-5D141CC903D6:ABPerson
default	22:07:40.471864-0500	Nexy	0000 Contact: 379EEF06-D880-4C4C-81B4-19232497B238:ABPerson
default	22:07:40.471877-0500	Nexy	0000 Contact: 9AA12C79-AC0F-40D8-82D4-7D1D1B6024D4:ABPerson
default	22:07:40.471888-0500	Nexy	0000 Contact: B584C21D-4B54-4F37-A1B1-B5EF3AEC170C:ABPerson
default	22:07:40.471898-0500	Nexy	0000 Contact: D2940461-BB6C-4224-8218-88019B5DB07D:ABPerson
default	22:07:40.471916-0500	Nexy	0000 Contact: 734CE2EC-7CFA-4475-B601-8F5A0EDC5AFC:ABPerson
default	22:07:40.471925-0500	Nexy	0000 Contact: 693CFFC7-F57A-478E-BBA2-CB65EB6C5425:ABPerson
default	22:07:40.471940-0500	Nexy	0000 Contact: 522D9347-0C39-4479-9A87-99551E9F992C:ABPerson
default	22:07:40.471951-0500	Nexy	0000 Contact: BC6A800E-2E2E-4B39-B37E-6639FBEE75EF:ABPerson
default	22:07:40.471966-0500	Nexy	0000 Contact: 4B6CD270-FA88-4F64-9F96-22BB79CBD541:ABPerson
default	22:07:40.471978-0500	Nexy	0000 Contact: 77ED343F-8BF8-4BFD-A0F9-901367A608BC:ABPerson
default	22:07:40.471992-0500	Nexy	0000 Contact: 37D2B9B0-053A-474C-BE44-09B4453D4050:ABPerson
default	22:07:40.472004-0500	Nexy	0000 Contact: 62B0EB86-C5BA-495C-9E28-535D2EF0354A:ABPerson
default	22:07:40.472018-0500	Nexy	0000 Contact: 670ECAAE-6CD8-4A3A-8EA6-614A11174BD6:ABPerson
default	22:07:40.472033-0500	Nexy	0000 Contact: A45DAD74-F719-4D46-9EA6-6DFEEF650375:ABPerson
default	22:07:40.472043-0500	Nexy	0000 Contact: B7008B2E-FA86-42D5-8656-CE248026D27E:ABPerson
default	22:07:40.472058-0500	Nexy	0000 Contact: 66B98153-BD62-4141-BD1F-DADC79D75A4F:ABPerson
default	22:07:40.472069-0500	Nexy	0000 Contact: FA38B842-F2F3-4FED-B33D-A5010D4304B0:ABPerson
default	22:07:40.472081-0500	Nexy	0000 Contact: 14743D61-F4A1-4392-9E1B-26918104BF14:ABPerson
default	22:07:40.472095-0500	Nexy	0000 Contact: B2D8BD53-113A-4BF0-91CA-D5DEB28674B5:ABPerson
default	22:07:40.472107-0500	Nexy	0000 Contact: 64B8389E-447B-4C35-B14E-8146CA91B47B:ABPerson
default	22:07:40.472121-0500	Nexy	0000 Contact: 3FF7B769-C140-4D4C-B32F-6B8F440DE2D8:ABPerson
default	22:07:40.472135-0500	Nexy	0000 Contact: 1F6916A9-1A84-48F4-B955-59E227D8C9DF:ABPerson
default	22:07:40.472147-0500	Nexy	0000 Contact: F334D708-4AFD-4933-99D2-F8F1D76176A9:ABPerson
default	22:07:40.472162-0500	Nexy	0000 Contact: 626EC525-A04F-4FBF-8FEE-BA93D0436808:ABPerson
default	22:07:40.472174-0500	Nexy	0000 Contact: A4D2F572-E7C4-45EE-AE51-345CC039C259:ABPerson
default	22:07:40.472187-0500	Nexy	0000 Contact: 014698F9-DA96-407C-A1B8-DEC6B51A33F6:ABPerson
default	22:07:40.472201-0500	Nexy	0000 Contact: F5B2550B-7B88-4DCE-A7A3-1B10271953FC:ABPerson
default	22:07:40.472213-0500	Nexy	0000 Contact: 1EAD0F34-5228-476C-B4EB-ACD91782DD85:ABPerson
default	22:07:40.472224-0500	Nexy	0000 Contact: F7E0D308-2E0A-49CC-849B-C883B6F8730F:ABPerson
default	22:07:40.472245-0500	Nexy	0000 Contact: 145A9F4B-B827-49A2-B108-81359AEE2B8F:ABPerson
default	22:07:40.472253-0500	Nexy	0000 Contact: 0AA46F26-7B70-4230-AC5B-AFDC6D2DD22B:ABPerson
default	22:07:40.472259-0500	Nexy	0000 Contact: AE79C4EC-990E-4BA3-913E-7C842EB653EF:ABPerson
default	22:07:40.472280-0500	Nexy	0000 Contact: C05B9998-16AE-4F34-8E4F-817C3D9B8EC6:ABPerson
default	22:07:40.472286-0500	Nexy	0000 Contact: 7F27B5B3-D0F5-483F-89C6-8B9931845E1F:ABPerson
default	22:07:40.472292-0500	Nexy	0000 Contact: 84E58627-BCB4-42D0-BDFA-EE699F5FBDD8:ABPerson
default	22:07:40.472315-0500	Nexy	0000 Contact: 2513C61B-7EFC-4A92-88AB-DF9479B99E6A:ABPerson
default	22:07:40.472321-0500	Nexy	0000 Contact: 84CFF237-6D8B-4620-9181-D1B4BB0809EE:ABPerson
default	22:07:40.472327-0500	Nexy	0000 Contact: 0BFD29DC-60C9-4B71-9D65-4ADA47472277:ABPerson
default	22:07:40.472345-0500	Nexy	0000 Contact: 69998C87-7B1A-45AA-ABB3-2D84128DD9EE:ABPerson
default	22:07:40.472353-0500	Nexy	0000 Contact: A7C3EEE8-11F8-4C0C-848D-3AC49C688578:ABPerson
default	22:07:40.472373-0500	Nexy	0000 Contact: A64A1E7E-C301-454E-A9A9-D685C82EF693:ABPerson
default	22:07:40.472381-0500	Nexy	0000 Contact: 91C379A3-DE9D-456A-A6AD-0F1F963582E7:ABPerson
default	22:07:40.472389-0500	Nexy	0000 Contact: 6ACE0F8B-171F-450C-83E2-081B5F26881E:ABPerson
default	22:07:40.472395-0500	Nexy	0000 Contact: AC074808-2D0D-48F8-8B23-3F0CA6D51D26:ABPerson
default	22:07:40.472412-0500	Nexy	0000 Contact: F4F5D7A0-BC90-4C27-BBCE-BE969384F1C0:ABPerson
default	22:07:40.472420-0500	Nexy	0000 Contact: 1ABDAACE-D0B1-4F9B-96D1-DC2C524CE1C6:ABPerson
default	22:07:40.472428-0500	Nexy	0000 Contact: 43585BE0-779A-4596-A518-8D5E4ADB3D19:ABPerson
default	22:07:40.472449-0500	Nexy	0000 Contact: 67051D02-C728-4665-B5FC-4F1B269F02BD:ABPerson
default	22:07:40.472455-0500	Nexy	0000 Contact: 4473A678-C9E7-4D62-84E0-753DF60913D1:ABPerson
default	22:07:40.472462-0500	Nexy	0000 Contact: D56AB0C8-7D93-4C12-B5B5-95E0DC8F2240:ABPerson
default	22:07:40.472479-0500	Nexy	0000 Contact: 9579BC4C-AF0F-4D50-A15C-319AACBFC2A5:ABPerson
default	22:07:40.472486-0500	Nexy	0000 Contact: 4BE75408-838B-4CDE-A088-588AE1E78C84:ABPerson
default	22:07:40.472506-0500	Nexy	0000 Contact: C87BCEEB-0D99-4BCD-B837-B1790FEF5A35:ABPerson
default	22:07:40.472512-0500	Nexy	0000 Contact: 11C070CC-DE86-43A2-AC2E-BD5D0E666C75:ABPerson
default	22:07:40.472520-0500	Nexy	0000 Contact: 1BC6C401-C80C-443B-86A1-DE142581F385:ABPerson
default	22:07:40.472539-0500	Nexy	0000 Contact: 0A5F3B64-AC92-4AC6-A80F-C08A85FC26AF:ABPerson
default	22:07:40.472547-0500	Nexy	0000 Contact: 87E03F74-07D8-4C64-9DA7-D99DC9CA7445:ABPerson
default	22:07:40.472553-0500	Nexy	0000 Contact: 94F55698-438B-4D8C-9CA0-71DDFD6367D5:ABPerson
default	22:07:40.472573-0500	Nexy	0000 Contact: 15748416-FFAD-4D4B-B4AF-076BF4C1B672:ABPerson
default	22:07:40.472580-0500	Nexy	0000 Contact: 74B3EEDB-C36E-4B91-AAF8-A7D433556574:ABPerson
default	22:07:40.472588-0500	Nexy	0000 Contact: 951A73EB-D920-4420-8258-81B51426DEF7:ABPerson
default	22:07:40.472609-0500	Nexy	0000 Contact: 6B194999-7994-412B-8F16-25AB9317AAB4:ABPerson
default	22:07:40.472615-0500	Nexy	0000 Contact: 2EC20223-DCBF-406A-9D39-5F1D770A8BC4:ABPerson
default	22:07:40.472623-0500	Nexy	0000 Contact: 1562F9E4-94A8-48AB-BF2B-C1EB0C1BE5A4:ABPerson
default	22:07:40.472640-0500	Nexy	0000 Contact: F6C3B173-427B-4C46-AA87-E8AA5B4E4C47:ABPerson
default	22:07:40.472647-0500	Nexy	0000 Contact: 5340250A-2C48-4FA9-9A43-1E9438F76204:ABPerson
default	22:07:40.472654-0500	Nexy	0000 Contact: 910FA8BF-611B-4C75-9EB0-5F2EFD716C1F:ABPerson
default	22:07:40.472675-0500	Nexy	0000 Contact: 08B0DE06-259B-449C-B66B-FFBA5AB8D812:ABPerson
default	22:07:40.472681-0500	Nexy	0000 Contact: 3C20B58D-2CA5-485E-A9A6-F77768532665:ABPerson
default	22:07:40.472687-0500	Nexy	0000 Contact: 6524FEA4-C209-419D-8A29-C534C9D1627C:ABPerson
default	22:07:40.472708-0500	Nexy	0000 Contact: 9A063C74-04C9-4AD8-AB36-6C8734D43E2D:ABPerson
default	22:07:40.472714-0500	Nexy	0000 Contact: AEAB4360-3F45-4F6B-9F79-B5D0B38B9A81:ABPerson
default	22:07:40.472722-0500	Nexy	0000 Contact: 044C1B1D-1FA6-46AA-B69A-444A8B442B7C:ABPerson
default	22:07:40.472740-0500	Nexy	0000 Contact: 67E45E85-4716-4AD1-9FE5-0DD5A68A6D7E:ABPerson
default	22:07:40.472749-0500	Nexy	0000 Contact: 4ADAEDF0-6C5E-4C06-9C0A-B8594FF82BDA:ABPerson
default	22:07:40.472757-0500	Nexy	0000 Contact: DA46038B-56C6-4414-9F21-077B66E8C91C:ABPerson
default	22:07:40.472778-0500	Nexy	0000 Contact: 75FADFA1-F7C3-437C-8B58-DAA8A4B54442:ABPerson
default	22:07:40.472784-0500	Nexy	0000 Contact: B6E3347E-7AC5-41E7-ACA5-D2CEF067A1CA:ABPerson
default	22:07:40.472790-0500	Nexy	0000 Contact: 4EFFE145-11B7-42A5-822C-A4BAB5D83906:ABPerson
default	22:07:40.472810-0500	Nexy	0000 Contact: EAB298D5-435C-4D40-83A7-2C55723A0BFD:ABPerson
default	22:07:40.472817-0500	Nexy	0000 Contact: B0D78C24-E588-4901-88A7-6B1BB429B840:ABPerson
default	22:07:40.472826-0500	Nexy	0000 Contact: 1CB20B90-D9D5-4C8F-9AB0-DAA44D00BDD4:ABPerson
default	22:07:40.472839-0500	Nexy	0000 Contact: 527699A5-81B2-4D67-AEED-D6EED43F9044:ABPerson
default	22:07:40.472861-0500	Nexy	0000 Contact: CB5E53D4-5C8B-43F5-94AF-6B7D8BA543FD:ABPerson
default	22:07:40.472867-0500	Nexy	0000 Contact: 04598613-6173-4B93-B8E7-285BC4F3D8E8:ABPerson
default	22:07:40.472882-0500	Nexy	0000 Contact: ADD86E64-7CF0-4510-AD39-66BD6BD079BC:ABPerson
default	22:07:40.472888-0500	Nexy	0000 Contact: 32788248-0C60-4FEA-85E7-FA758B61DD1D:ABPerson
default	22:07:40.472908-0500	Nexy	0000 Contact: AA1A4C67-F155-4EE5-9010-31149EE1E39C:ABPerson
default	22:07:40.472915-0500	Nexy	0000 Contact: 961DCC0E-AAAD-4D01-9678-0A7621D2AFB0:ABPerson
default	22:07:40.472922-0500	Nexy	0000 Contact: 66B11FA1-1DE3-48ED-A067-665E7467482A:ABPerson
default	22:07:40.472943-0500	Nexy	0000 Contact: F5182AF8-32D2-40E6-993D-C0489EBC89E4:ABPerson
default	22:07:40.472949-0500	Nexy	0000 Contact: 0D60E67B-3CE2-4AA5-A3A7-78022070A092:ABPerson
default	22:07:40.472959-0500	Nexy	0000 Contact: 3AAC52F8-BF6B-4AF2-BB6D-03A1310B24E5:ABPerson
default	22:07:40.472980-0500	Nexy	0000 Contact: CE41D8E9-94C5-4D35-9B34-26811B12C410:ABPerson
default	22:07:40.472986-0500	Nexy	0000 Contact: F13294CA-A587-43D6-B693-775C43EE2187:ABPerson
default	22:07:40.472994-0500	Nexy	0000 Contact: 89FE41AC-035D-4508-9B13-A7A61A86A77D:ABPerson
default	22:07:40.473014-0500	Nexy	0000 Contact: 31E21B40-260C-42C1-9677-7C97CC1B201D:ABPerson
default	22:07:40.473021-0500	Nexy	0000 Contact: F0D80C37-667F-495B-83CE-9F5BF918C730:ABPerson
default	22:07:40.473027-0500	Nexy	0000 Contact: 06259E4E-E4B7-4654-BF6B-33F4F0FCB23A:ABPerson
default	22:07:40.473047-0500	Nexy	0000 Contact: 55FDAC9D-D436-4535-BE96-A71F62A0AF9E:ABPerson
default	22:07:40.473053-0500	Nexy	0000 Contact: F790FA9D-7B36-4AEA-8012-0BDEED54CF62:ABPerson
default	22:07:40.473061-0500	Nexy	0000 Contact: 276E4846-224E-4119-AB43-FE2E963D133E:ABPerson
default	22:07:40.473081-0500	Nexy	0000 Contact: DB25F4B4-E218-42CD-959A-C88098B61FD4:ABPerson
default	22:07:40.473087-0500	Nexy	0000 Contact: 7E8FC80C-607C-43E2-BF92-C5FCC8403326:ABPerson
default	22:07:40.473093-0500	Nexy	0000 Contact: 6BE779B6-7D7F-4DB2-A36A-3696730156FE:ABPerson
default	22:07:40.473114-0500	Nexy	0000 Contact: A45B54DD-B6FC-4653-84D5-0757EB2F2ED6:ABPerson
default	22:07:40.473120-0500	Nexy	0000 Contact: 8605C2C8-7153-4112-9036-FAA472B7FD44:ABPerson
default	22:07:40.473128-0500	Nexy	0000 Contact: CD272F42-E884-45F1-84C3-CFD3A0B1BF35:ABPerson
default	22:07:40.473148-0500	Nexy	0000 Contact: 4D2116D6-A645-48BB-B220-E9ED03C71748:ABPerson
default	22:07:40.473155-0500	Nexy	0000 Contact: B502B3DD-9E9D-4150-B4A9-4872364793EF:ABPerson
default	22:07:40.473161-0500	Nexy	0000 Contact: 0C360F68-EDE2-457E-AC4B-ACE762AD5BD0:ABPerson
default	22:07:40.473181-0500	Nexy	0000 Contact: FF4175C6-26DF-47BC-BF00-2E75EEE8B1FD:ABPerson
default	22:07:40.473189-0500	Nexy	0000 Contact: 09A457F3-A9F4-4F24-9B11-9FA58D4C1508:ABPerson
default	22:07:40.473195-0500	Nexy	0000 Contact: B89DEF47-D413-46AD-BAEA-7D496DD46FB1:ABPerson
default	22:07:40.473210-0500	Nexy	0000 Contact: 3598E3CB-8A76-4D70-AC49-D3EB37CA2029:ABPerson
default	22:07:40.473220-0500	Nexy	0000 Contact: AA991FC9-EB3D-43B4-8CBD-8E604A09B637:ABPerson
default	22:07:40.473237-0500	Nexy	0000 Contact: CC5195D6-422A-4FB7-B9EE-A2A04E601EC0:ABPerson
default	22:07:40.473246-0500	Nexy	0000 Contact: B569062E-A03D-4DD9-A53C-5D2D8D57CB4B:ABPerson
default	22:07:40.473265-0500	Nexy	0000 Contact: 73B6BD20-2014-4F01-90D9-4428F13B690A:ABPerson
default	22:07:40.473273-0500	Nexy	0000 Contact: AA3A3E50-90A8-4525-8DAA-B8B4FADD18DA:ABPerson
default	22:07:40.473283-0500	Nexy	0000 Contact: 3BAE7091-1579-47D0-B90D-0D3CF681C569:ABPerson
default	22:07:40.473289-0500	Nexy	0000 Contact: 56A226DF-9ECE-4143-BA65-8AD0B646C7CB:ABPerson
default	22:07:40.473304-0500	Nexy	0000 Contact: 50F1ED96-0C6B-4F81-AA14-43DC6EBECD59:ABPerson
default	22:07:40.473313-0500	Nexy	0000 Contact: 5A494BDA-3B74-4B7B-92A5-ADDBE7FB8C87:ABPerson
default	22:07:40.473331-0500	Nexy	0000 Contact: 6BD609FD-5007-4D59-A4EF-493CADDB85B2:ABPerson
default	22:07:40.473337-0500	Nexy	0000 Contact: 7E64D4B3-BC6D-4959-B7A0-E823B049142C:ABPerson
default	22:07:40.473345-0500	Nexy	0000 Contact: 621AF0D1-3352-4F82-9C69-D6B0F8D4F5A9:ABPerson
default	22:07:40.473366-0500	Nexy	0000 Contact: 4E051A3F-F33F-42F6-A635-4F6B6FEFCFB2:ABPerson
default	22:07:40.473371-0500	Nexy	0000 Contact: 30F7C290-B84E-45EF-8777-D14EBB9D4BB1:ABPerson
default	22:07:40.473380-0500	Nexy	0000 Contact: B489EA28-72B0-4D87-8E65-2FCC5266CCBB:ABPerson
default	22:07:40.473391-0500	Nexy	0000 Contact: E5C00A28-C49D-4782-B544-D726CFE29EF0:ABPerson
default	22:07:40.473411-0500	Nexy	0000 Contact: DA65C871-7E16-4359-B34C-C5906692C623:ABPerson
default	22:07:40.473417-0500	Nexy	0000 Contact: 5BAFBA23-8FAE-41B7-86D6-A6B3DB070404:ABPerson
default	22:07:40.473423-0500	Nexy	0000 Contact: EA0D316B-758E-4C59-B0A6-6FFB7AD3E09F:ABPerson
default	22:07:40.473443-0500	Nexy	0000 Contact: 9BD347CB-8966-4118-92F7-D6D42F5F8C7C:ABPerson
default	22:07:40.473449-0500	Nexy	0000 Contact: 018F45A5-C534-4FC0-871A-DB5567A8D78E:ABPerson
default	22:07:40.473458-0500	Nexy	0000 Contact: 9FC18618-FB9D-4960-8474-07F6A0D062F8:ABPerson
default	22:07:40.473476-0500	Nexy	0000 Contact: C8BDDDAE-C009-4DB9-B3FC-01F3B16C6D25:ABPerson
default	22:07:40.473484-0500	Nexy	0000 Contact: 1D0198ED-A6C3-4B64-AA1A-2E8A8C4A0172:ABPerson
default	22:07:40.473489-0500	Nexy	0000 Contact: 3BD67570-1034-422C-85A2-6F28BE24C33A:ABPerson
default	22:07:40.473510-0500	Nexy	0000 Contact: D75A5B27-BD0C-4D34-AC6B-FC2822769519:ABPerson
default	22:07:40.473516-0500	Nexy	0000 Contact: 6B5F7DDD-1E04-453D-8539-4B54A251117A:ABPerson
default	22:07:40.473524-0500	Nexy	0000 Contact: 49E369CD-B10E-4CD5-B030-5393AB2ADE18:ABPerson
default	22:07:40.473545-0500	Nexy	0000 Contact: A9AB0613-621A-427C-9150-83893BA072C5:ABPerson
default	22:07:40.473551-0500	Nexy	0000 Contact: 9B8281D5-C780-436F-988A-96C01722B038:ABPerson
default	22:07:40.473582-0500	Nexy	0000 FINISH (29.7 ms)
default	22:07:40.515085-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.515099-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.515110-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.515127-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.517848-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.518218-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.518331-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.854254-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89561] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-70793 target:89561 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	22:07:40.854568-0500	runningboardd	Assertion 402-625-70793 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) will be created as active
default	22:07:40.854810-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	22:07:40.855298-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:40.855329-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:40.855478-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:40.855572-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:40.862032-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:40.862909-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.863184-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:40.961390-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	22:07:40.961642-0500	runningboardd	Invalidating assertion 402-625-70793 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89561]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:07:41.064920-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring jetsam update because this process is not memory-managed
default	22:07:41.064937-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring suspend because this process is not lifecycle managed
default	22:07:41.064949-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring GPU update because this process is not GPU managed
default	22:07:41.064973-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] Ignoring memory limit update because this process is not memory-managed
default	22:07:41.068695-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:41.069266-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:41.069515-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:41.103254-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x5a15a1 (Nexy) connectionID: 87BC3 pid: 89561 in session 0x101
default	22:07:41.104316-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f406a","name":"Nexy(89561)"}, "details":null }
default	22:07:41.104401-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f406a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":89561})
default	22:07:41.104403-0500	WindowManager	Connection invalidated | (89561) Nexy
default	22:07:41.104420-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":89561})
default	22:07:41.103316-0500	WindowServer	<BSCompoundAssertion:0x9a3011580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x5a15a1 (Nexy) acq:0x9a118bfc0 count:1
default	22:07:41.105211-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:07:41.105460-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 107, PID = 89561, Name = sid:0x1f406a, Nexy(89561), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:07:41.106234-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.106317-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.107980-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.106090-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x5a15a1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x5a15a1 (Nexy)"
)}
default	22:07:41.104460-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Workspace connection invalidated.
default	22:07:41.104496-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Now flagged as pending exit for reason: workspace client connection invalidated
default	22:07:41.105922-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.106089-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.108772-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x15dd9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x5a15a1 (Nexy)"
)}
default	22:07:41.108160-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:07:41.119036-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.120321-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:07:41.120572-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	22:07:41.128667-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	22:07:41.128685-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_4371.4293.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	22:07:41.136990-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:53378<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580446 t_state: FIN_WAIT_1 process: Nexy:89561 Duration: 1.998 sec Conn_Time: 0.015 sec bytes in/out: 2269/732 pkts in/out: 4/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.437 ms rttvar: 13.375 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xb3147f2c
default	22:07:41.137008-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53378<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580446 t_state: FIN_WAIT_1 process: Nexy:89561 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:07:41.137181-0500	mDNSResponder	[R157885] DNSServiceCreateConnection STOP PID[89561](Nexy)
default	22:07:41.138032-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89561] termination reported by launchd (0, 0, 0)
default	22:07:41.138107-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.138464-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.138662-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.138715-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.144589-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: none (role: NonUserInteractive) (endowments: (null))
default	22:07:41.144844-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Process exited: <RBSProcessExitContext| voluntary>.
default	22:07:41.144870-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Setting process task state to: Not Running
default	22:07:41.144881-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Setting process visibility to: Unknown
default	22:07:41.144918-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, none-NotVisible
default	22:07:41.144948-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89561] Invalidating workspace.
default	22:07:41.145054-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 89561, name = Nexy
default	22:07:41.144864-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: none (role: NonUserInteractive) (endowments: (null))
default	22:07:41.145005-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.145241-0500	ControlCenter	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, none-NotVisible
default	22:07:41.145505-0500	ControlCenter	Removing: <FBApplicationProcess: 0xbdf13f780; app<application.com.nexy.assistant.54571778.54571787>:89561(v145E37)>
default	22:07:41.146059-0500	launchservicesd	Hit the server for a process handle 14e7373600015dd9 that resolved to: [app<application.com.nexy.assistant.54571778.54571787(501)>:89561]
default	22:07:41.146083-0500	gamepolicyd	Received state update for 89561 (app<application.com.nexy.assistant.54571778.54571787(501)>, none-NotVisible
default	22:07:41.147439-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-89561)
default	22:07:41.148996-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x5a15a1} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	22:07:41.149040-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9b1f841e0: Nexy> state 3
default	22:07:41.149065-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	22:07:41.149713-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(CDEFFD02) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-89561)
default	22:07:41.149806-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(CDEFFD02, (bid:com.nexy.assistant-Item-0-89561))]
default	22:07:41.155380-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9b1f841e0: Nexy> state 4
default	22:07:41.155396-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	22:07:42.304102-0500	runningboardd	Invalidating assertion 402-625-70779 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:07:42.407368-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54571778.54571787(501)>
default	22:07:42.412854-0500	gamepolicyd	Received state update for -1 (app<application.com.nexy.assistant.54571778.54571787(501)>, none-NotVisible
default	22:07:44.218561-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	22:07:44.308139-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	22:07:44.308327-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	22:07:44.310480-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	22:07:44.318276-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	22:07:44.321405-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54571778.54571787(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	22:07:44.321471-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54571778.54571787(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:85540] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:402-85540-70795 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	22:07:44.321542-0500	runningboardd	Assertion 402-85540-70795 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) will be created as active
default	22:07:44.324310-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	22:07:44.324333-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.54571778.54571787(501)>
default	22:07:44.324345-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	22:07:44.324407-0500	runningboardd	app<application.com.nexy.assistant.54571778.54571787(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.001073 ms (wallclock); resolved to {4294967295, (null)}
default	22:07:44.336136-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] is not RunningBoard jetsam managed.
default	22:07:44.336149-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] This process will not be managed.
default	22:07:44.336159-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:07:44.336304-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:44.336843-0500	gamepolicyd	Hit the server for a process handle 2940ae700015e87 that resolved to: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:07:44.336882-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:44.339679-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:07:44.339735-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:402-402-70796 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:07:44.339859-0500	runningboardd	Assertion 402-402-70796 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:07:44.340028-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:07:44.340046-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:07:44.340065-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Set darwin role to: UserInteractive
default	22:07:44.340079-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:07:44.340106-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:07:44.340130-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] reported to RB as running
default	22:07:44.341409-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:89735" ID:402-365-70797 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	22:07:44.341500-0500	runningboardd	Assertion 402-365-70797 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:07:44.341584-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x5c95c9 com.nexy.assistant starting stopped process.
default	22:07:44.342495-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	22:07:44.342636-0500	loginwindow	-[Application setState:] | enter: <Application: 0x9b1f841e0: Nexy> state 2
default	22:07:44.342654-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	22:07:44.342643-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:07:44.342654-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:07:44.342672-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:07:44.342740-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:07:44.342839-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:07:44.344526-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:44.344800-0500	runningboardd	Invalidating assertion 402-85540-70795 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:85540]
default	22:07:44.344829-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:07:44.344861-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:07:44.344896-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:07:44.344917-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:44.344954-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:07:44.347450-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:44.353008-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:44.389202-0500	logger	detected new pid 89735 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:44.423543-0500	Nexy	[0x1048c4ff0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	22:07:44.423620-0500	Nexy	[0x1048c5530] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	22:07:44.450470-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:07:44.450489-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:07:44.450500-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:07:44.450520-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:07:44.450635-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:44.453094-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:44.453388-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
error	22:07:44.534821-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1048b83b0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:07:44.535042-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1048b83b0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:07:44.535243-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1048b83b0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	22:07:44.535445-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1048b83b0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	22:07:44.536412-0500	Nexy	[0x1048ceec0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	22:07:44.537053-0500	Nexy	[0x991a88000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	22:07:44.537302-0500	Nexy	[0x991a88140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	22:07:44.537641-0500	Nexy	[0x991a88280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	22:07:44.539293-0500	Nexy	Received configuration update from daemon (initial)
default	22:07:44.539419-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	22:07:44.539737-0500	Nexy	[0x991a883c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:07:44.540297-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89735.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:07:44.541619-0500	tccd	AUTHREQ_SUBJECT: msgID=89735.1, subject=com.nexy.assistant,
default	22:07:44.542232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:07:44.560816-0500	Nexy	[0x991a883c0] invalidated after the last release of the connection object
default	22:07:44.561068-0500	Nexy	server port 0x0000370f, session port 0x0000370f
default	22:07:44.561892-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2557, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:07:44.561918-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:07:44.562669-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2557, subject=com.nexy.assistant,
default	22:07:44.563308-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:07:44.587270-0500	Nexy	New connection 0x8f493 main
default	22:07:44.589993-0500	Nexy	CHECKIN: pid=89735
default	22:07:44.599391-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.coreservices.launchservicesd>:365] with description <RBSAssertionDescriptor| "uielement:89735" ID:402-365-70798 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	22:07:44.599468-0500	runningboardd	Assertion 402-365-70798 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:07:44.599824-0500	runningboardd	Invalidating assertion 402-365-70797 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.coreservices.launchservicesd>:365]
default	22:07:44.599855-0500	Nexy	CHECKEDIN: pid=89735 asn=0x0-0x5c95c9 foreground=0
default	22:07:44.599745-0500	launchservicesd	CHECKIN:0x0-0x5c95c9 89735 com.nexy.assistant
default	22:07:44.600107-0500	Nexy	[0x991a883c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	22:07:44.600116-0500	Nexy	[0x991a883c0] Connection returned listener port: 0x4f03
default	22:07:44.600390-0500	Nexy	[0x9909b4300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x991a883c0.peer[365].0x9909b4300
default	22:07:44.601311-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	22:07:44.601423-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	22:07:44.603038-0500	Nexy	FRONTLOGGING: version 1
default	22:07:44.603107-0500	Nexy	Registered, pid=89735 ASN=0x0,0x5c95c9
default	22:07:44.603691-0500	WindowServer	8f493[CreateApplication]: Process creation: 0x0-0x5c95c9 (Nexy) connectionID: 8F493 pid: 89735 in session 0x101
default	22:07:44.605650-0500	Nexy	[0x991a883c0] Connection returned listener port: 0x4f03
default	22:07:44.613334-0500	Nexy	No persisted cache on this platform.
default	22:07:44.614284-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	22:07:44.618330-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	22:07:44.618341-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	22:07:44.618402-0500	Nexy	Initializing connection
default	22:07:44.618443-0500	Nexy	Removing all cached process handles
default	22:07:44.618463-0500	Nexy	Sending handshake request attempt #1 to server
default	22:07:44.618472-0500	Nexy	Creating connection to com.apple.runningboard
default	22:07:44.618479-0500	Nexy	[0x991a88640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	22:07:45.592012-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EB0728EF-E0F1-4D6E-A5F9-D9021B5C5646 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53393,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd185a9bb tp_proto=0x06"
default	22:07:45.592123-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53393<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580558 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b50ba44
default	22:07:50.319596-0500	runningboardd	Assertion did invalidate due to timeout: 402-402-70796 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735])
default	22:07:50.516393-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:07:50.516427-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:07:50.516448-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:07:50.516484-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:07:50.521573-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:07:50.522541-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:07:50.593411-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53393<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580558 t_state: SYN_SENT process: Nexy:89735 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x9b50ba44
default	22:07:50.593452-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53393<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580558 t_state: SYN_SENT process: Nexy:89735 flowctl: 0us (0x) SYN in/out: 0/6 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:07:50.594279-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 003D5AD3-45C2-49FE-9A8F-FDD562673CB0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53396,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x12d458a3 tp_proto=0x06"
default	22:07:50.594388-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53396<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580596 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87945de7
default	22:07:54.976484-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	22:07:55.594974-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53396<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580596 t_state: SYN_SENT process: Nexy:89735 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x87945de7
default	22:07:55.595004-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53396<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580596 t_state: SYN_SENT process: Nexy:89735 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:07:55.599617-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	22:07:55.599837-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	22:07:55.601435-0500	Nexy	nw_path_libinfo_path_check [F7D20E94-3CC9-4079-B6A0-6C37CD4129A4 Hostname#6ac91075:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:07:55.601927-0500	mDNSResponder	[R158086] DNSServiceCreateConnection START PID[89735](Nexy)
default	22:07:55.602021-0500	mDNSResponder	[R158087] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: f92d5498
default	22:07:55.602647-0500	mDNSResponder	[R158088] DNSServiceQueryRecord START -- qname: <mask.hash: 'dXMH313VT6V8KeY9ZBDxuA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: f92d5498
default	22:07:55.615174-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	22:07:55.652959-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1787BC56-D457-4AAF-9D0C-DBA293B6D114 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53399,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x4331f8ae tp_proto=0x06"
default	22:07:55.653065-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53399<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580629 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9680e3ed
default	22:08:00.596041-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:53399<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580629 t_state: SYN_SENT process: Nexy:89735 Duration: 4.943 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0x9680e3ed
default	22:08:00.596080-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53399<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1580629 t_state: SYN_SENT process: Nexy:89735 flowctl: 0us (0x) SYN in/out: 0/12 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:08:01.686213-0500	Nexy	[0x991a88dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:08:01.686955-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89735.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:08:01.688365-0500	tccd	AUTHREQ_SUBJECT: msgID=89735.2, subject=com.nexy.assistant,
default	22:08:01.689294-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:01.711945-0500	Nexy	[0x991a88dc0] invalidated after the last release of the connection object
default	22:08:01.712079-0500	Nexy	server port 0x0000441b, session port 0x0000370f
default	22:08:01.712793-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2558, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:08:01.712819-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:01.713618-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2558, subject=com.nexy.assistant,
default	22:08:01.714229-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:01.739265-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	22:08:01.739839-0500	Nexy	[0x991a88f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	22:08:01.740746-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"PID":89735,"session_type":"Primary"} }
default	22:08:01.740819-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":89735}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f406b, sessionType: 'prim', isRecording: false }, 
]
default	22:08:01.741504-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 89735, name = Nexy
default	22:08:01.741797-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x990a58700 with ID: 0x1f406b
default	22:08:01.742012-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	22:08:01.742768-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	22:08:01.744054-0500	Nexy	[0x991a89040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	22:08:01.746067-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
default	22:08:01.749828-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	22:08:01.751447-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	22:08:01.751635-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	22:08:01.751768-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	22:08:01.751780-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	22:08:01.751810-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	22:08:01.752012-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	22:08:01.751919-0500	Nexy	[0x991a89180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	22:08:01.752307-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89735.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:08:01.758750-0500	tccd	AUTHREQ_SUBJECT: msgID=89735.3, subject=com.nexy.assistant,
default	22:08:01.759552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:08:01.775846-0500	Nexy	[0x991a89180] invalidated after the last release of the connection object
default	22:08:01.775984-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	22:08:01.776027-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	22:08:01.776242-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	22:08:01.777364-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1955, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:01.778291-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1955, subject=com.nexy.assistant,
default	22:08:01.778861-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:08:01.797348-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1957, subject=com.nexy.assistant,
default	22:08:01.797895-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45e00 at /Applications/Nexy.app
default	22:08:01.811814-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	22:08:01.811830-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x98f85bac0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	22:08:01.829910-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	22:08:01.829920-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	22:08:01.832593-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:01.832730-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:01.836925-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	22:08:01.837805-0500	Nexy	[0x991a89180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	22:08:01.838155-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=385408890306561 }
default	22:08:01.838231-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	22:08:01.838264-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	22:08:01.838291-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	22:08:01.884083-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:01.884212-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:08:01.898399-0500	mDNSResponder	[R158102] DNSServiceQueryRecord START -- qname: <mask.hash: 'Msnutn5+cka0lGHzy+ILEw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: 2d50b096
default	22:08:01.906879-0500	kernel	tcp connected: [<IPv4-redacted>:53414<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580724 t_state: ESTABLISHED process: Nexy:89735 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xab617418
default	22:08:01.907488-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 148E7272-9FA0-4544-A704-5C0B4450F380 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53415,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xb2c110bf tp_proto=0x06"
default	22:08:01.907504-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53415<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580732 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7498ecf
default	22:08:01.922924-0500	kernel	tcp connected: [<IPv4-redacted>:53415<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1580732 t_state: ESTABLISHED process: Nexy:89735 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7498ecf
default	22:08:01.937128-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:02.107567-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 89750: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 2e601400 };
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
default	22:08:02.124377-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:02.136203-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46100 at /Applications/Nexy.app
default	22:08:02.153781-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	22:08:04.096198-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d45800 at /Applications/Nexy.app
default	22:08:04.103313-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    447 = "<TCCDEventSubscriber: token=447, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    462 = "<TCCDEventSubscriber: token=462, state=Passed, csid=com.apple.chronod>";
}
default	22:08:04.104926-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	22:08:05.432162-0500	Nexy	[0x991a89680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:08:05.433171-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89735.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:08:05.442590-0500	tccd	AUTHREQ_SUBJECT: msgID=89735.4, subject=com.nexy.assistant,
default	22:08:05.443411-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:05.462421-0500	Nexy	[0x991a89680] invalidated after the last release of the connection object
default	22:08:05.462719-0500	Nexy	[0x991a89680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	22:08:05.463228-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=89735.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	22:08:05.464086-0500	tccd	AUTHREQ_SUBJECT: msgID=89735.5, subject=com.nexy.assistant,
default	22:08:05.464728-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:05.483156-0500	Nexy	[0x991a89680] invalidated after the last release of the connection object
default	22:08:05.483277-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	22:08:05.483774-0500	Nexy	[0x991a89680] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	22:08:05.483913-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	22:08:05.484016-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:08:05.486212-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:08:05.486244-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:05.487147-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.4, subject=com.nexy.assistant,
default	22:08:05.487797-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:05.512461-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2566, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:08:05.512490-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:05.513364-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2566, subject=com.nexy.assistant,
default	22:08:05.513992-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:05.540885-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	22:08:05.558432-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
fault	22:08:05.560978-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54571778.54571787 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54571778.54571787>
default	22:08:05.578630-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:05.578735-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:05.578783-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:05.932235-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:05.934065-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x990a50520: start, was running 0
default	22:08:05.937072-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70830 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:05.937252-0500	runningboardd	Assertion 402-336-70830 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:05.937895-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:05.937916-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:05.937933-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:05.937969-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:05.942992-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:05.943753-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.045006-0500	Nexy	[0x991a89a40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	22:08:06.065362-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	22:08:06.065779-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 89735
default	22:08:06.080563-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x991940820
 (
    "<NSDarkAquaAppearance: 0x9919406e0>",
    "<NSSystemAppearance: 0x991940780>"
)>
default	22:08:06.084106-0500	Nexy	[0x991a89f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	22:08:06.085177-0500	Nexy	[0x991a8a080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	22:08:06.088186-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	22:08:06.088511-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	22:08:06.088521-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	22:08:06.088550-0500	Nexy	[0x991a8a1c0] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	22:08:06.088588-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	22:08:06.088674-0500	Nexy	[0x991a8a300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:08:06.088746-0500	Nexy	FBSWorkspace registering source: <private>
default	22:08:06.089512-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	22:08:06.089731-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	22:08:06.090396-0500	Nexy	<FBSWorkspaceScenesClient:0x994135180 <private>> attempting immediate handshake from activate
default	22:08:06.090460-0500	Nexy	<FBSWorkspaceScenesClient:0x994135180 <private>> sent handshake
default	22:08:06.090574-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	22:08:06.090595-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.090635-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.090738-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Registering event dispatcher at init
default	22:08:06.090853-0500	ControlCenter	Created <FBWorkspace: 0xbdbed4be0; <FBApplicationProcess: 0xbdf13eb80; app<application.com.nexy.assistant.54571778.54571787>:89735(v146012)>>
default	22:08:06.090872-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54571778.54571787> with intent background
default	22:08:06.091279-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	22:08:06.091449-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54571778.54571787(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	22:08:06.091626-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54571778.54571787(501)> from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-70831 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	22:08:06.091825-0500	runningboardd	Assertion 402-625-70831 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) will be created as active
default	22:08:06.091862-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:402-625-70831 target:app<application.com.nexy.assistant.54571778.54571787(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.092243-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:06.092253-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:06.092263-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:06.092781-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:06.093061-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	22:08:06.094301-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	22:08:06.094840-0500	Nexy	Requesting scene <FBSScene: 0x9941355e0; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29> from com.apple.controlcenter.statusitems
default	22:08:06.095236-0500	Nexy	Request for <FBSScene: 0x9941355e0; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29> complete!
default	22:08:06.095328-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	22:08:06.096940-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	22:08:06.097292-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	22:08:06.097511-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	22:08:06.097544-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	22:08:06.097856-0500	Nexy	Requesting scene <FBSScene: 0x994135680; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	22:08:06.098037-0500	Nexy	Request for <FBSScene: 0x994135680; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView> complete!
default	22:08:06.099108-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:06.099805-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.099826-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	22:08:06.100145-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Bootstrap success!
default	22:08:06.100373-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.100671-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Setting process visibility to: Background
default	22:08:06.100748-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] No launch watchdog for this process, dropping initial assertion in 2.0s
default	22:08:06.101118-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:402-625-70832 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	22:08:06.101207-0500	runningboardd	Assertion 402-625-70832 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:06.101609-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:06.101622-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:06.101632-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:06.101655-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:06.104024-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.104048-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	22:08:06.104172-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	22:08:06.104866-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:06.105442-0500	ControlCenter	Adding: <FBApplicationProcess: 0xbdf13eb80; app<application.com.nexy.assistant.54571778.54571787>:89735(v146012)>
default	22:08:06.106122-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Connection established.
default	22:08:06.106225-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xbdc185d50>
default	22:08:06.106254-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Connection to remote process established!
default	22:08:06.106410-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.107474-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.112586-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.112612-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdf13eb80; app<application.com.nexy.assistant.54571778.54571787>:89735(v146012)>
default	22:08:06.112786-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Registered new scene: <FBWorkspaceScene: 0xbe0dc0fc0; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29> (fromRemnant = 0)
default	22:08:06.112817-0500	Nexy	Registering for test daemon availability notify post.
default	22:08:06.112843-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Workspace interruption policy did change: reconnect
default	22:08:06.113034-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:08:06.113138-0500	Nexy	Request for <FBSScene: 0x9941355e0; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29> complete!
default	22:08:06.113138-0500	ControlCenter	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Client process connected: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.113157-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:08:06.113270-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	22:08:06.113364-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:402-625-70833 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	22:08:06.113455-0500	runningboardd	Assertion 402-625-70833 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as inactive as originator process has not exited
default	22:08:06.113784-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.113799-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xbdf13eb80; app<application.com.nexy.assistant.54571778.54571787>:89735(v146012)>
default	22:08:06.113883-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Registered new scene: <FBWorkspaceScene: 0xbe0dc0480; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	22:08:06.113897-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-70834 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	22:08:06.113992-0500	runningboardd	Assertion 402-625-70834 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:06.114016-0500	ControlCenter	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:06.114018-0500	Nexy	Request for <FBSScene: 0x994135680; com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView> complete!
default	22:08:06.114078-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	22:08:06.114239-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:06.114288-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:06.114361-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:06.114449-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:06.114620-0500	Nexy	[0x991a8a6c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	22:08:06.114636-0500	Nexy	<FBSWorkspaceScenesClient:0x994135180 <private>> Reconnecting scene com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29
default	22:08:06.114952-0500	Nexy	<FBSWorkspaceScenesClient:0x994135180 <private>> Reconnecting scene com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView
default	22:08:06.117223-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:06.117681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:06.117687-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.117842-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.124388-0500	Nexy	[0x991a883c0] Connection returned listener port: 0x4f03
default	22:08:06.124857-0500	Nexy	SignalReady: pid=89735 asn=0x0-0x5c95c9
default	22:08:06.125323-0500	Nexy	SIGNAL: pid=89735 asn=0x0x-0x5c95c9
default	22:08:06.126007-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	22:08:06.134838-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.137304-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.140204-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	22:08:06.140227-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	22:08:06.140278-0500	Nexy	[0x991a89540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	22:08:06.140362-0500	Nexy	[0x991a89540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	22:08:06.141474-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	22:08:06.143544-0500	Nexy	[C:2] Alloc <private>
default	22:08:06.143574-0500	Nexy	[0x991a89540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	22:08:06.144238-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-89735). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	22:08:06.145003-0500	WindowManager	Connection activated | (89735) Nexy
default	22:08:06.145003-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-89735)
default	22:08:06.145112-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70835 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:06.145174-0500	runningboardd	Assertion 402-89735-70835 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:06.145713-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:06.145761-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:06.145786-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:06.145855-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:06.145123-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(6A22596D, (bid:com.nexy.assistant-Item-0-89735)) for (bid:com.nexy.assistant-Item-0-89735)
default	22:08:06.145828-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-89735)]
default	22:08:06.145896-0500	ControlCenter	Created instance DisplayableId(621B895F) in .menuBar for DisplayableAppStatusItemType(6A22596D, (bid:com.nexy.assistant-Item-0-89735)) .menuBar
default	22:08:06.150487-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:06.150918-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.151079-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	22:08:06.151114-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.152368-0500	ControlCenter	Created ephemaral instance DisplayableId(621B895F) for (bid:com.nexy.assistant-Item-0-89735) with positioning .ephemeral
default	22:08:06.152369-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	22:08:06.152848-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	22:08:06.152971-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.157932-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:06.258871-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	22:08:06.261878-0500	Nexy	Start service name com.apple.spotlightknowledged
default	22:08:06.262809-0500	Nexy	[GMS] availability notification token 90
default	22:08:06.364295-0500	runningboardd	Invalidating assertion 402-625-70834 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:08:06.364131-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	22:08:06.420984-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:06.422171-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	22:08:06.422327-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:06.422394-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:08:06.422440-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'MediaPlayback'
default	22:08:06.422466-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.422487-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	22:08:06.422499-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 108 starting playing
default	22:08:06.422574-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:06.422605-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:06.422640-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:06.422662-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	22:08:06.422658-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.422715-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.422738-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f406b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":89735}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f406b, sessionType: 'prim', isRecording: false }, 
]
default	22:08:06.422707-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:06.423002-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	22:08:06.423032-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:06.422986-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:06.424726-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.424853-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.424885-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:06.424904-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	22:08:06.424913-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	22:08:06.424926-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	22:08:06.424997-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:06.471796-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:06.471807-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:06.471818-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:06.471839-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:06.474598-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:06.474973-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:06.475256-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:07.175769-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	22:08:07.784213-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:07.784388-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:08.198232-0500	runningboardd	Invalidating assertion 402-625-70831 (target:app<application.com.nexy.assistant.54571778.54571787(501)>) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:08:08.303392-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54571778.54571787(501)>
default	22:08:08.304687-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:08.304718-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:08.304742-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:08.304790-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:08.308754-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:08.315917-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:08.316215-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:09.418103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.2567, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	22:08:09.418183-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=395, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:09.421232-0500	tccd	AUTHREQ_SUBJECT: msgID=395.2567, subject=com.nexy.assistant,
default	22:08:09.422528-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:10.172683-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	22:08:11.067668-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	22:08:11.903764-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.WindowServer(88)>:395] with description <RBSAssertionDescriptor| "AppDrawing" ID:402-395-70848 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:11.903867-0500	runningboardd	Assertion 402-395-70848 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:11.904170-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:11.904184-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:11.904195-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:11.904232-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:11.907066-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:11.907546-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:11.907704-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:12.393479-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.controlcenter(501)>:625] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:402-625-70864 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	22:08:12.393634-0500	runningboardd	Assertion 402-625-70864 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:12.394315-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:12.394478-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:12.394644-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:12.394857-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:12.393802-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	22:08:12.402147-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:12.402719-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:12.403453-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:12.497312-0500	ControlCenter	[app<application.com.nexy.assistant.54571778.54571787>:89735] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	22:08:12.497425-0500	runningboardd	Invalidating assertion 402-625-70864 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.controlcenter(501)>:625]
default	22:08:12.605897-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:12.605907-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:12.605916-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:12.605937-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:12.609451-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:12.609805-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:12.610407-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:13.181399-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	22:08:13.419310-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:13.421960-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:14.078377-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:14.079763-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:14.080775-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x98f648040) Selecting device 85 from constructor
default	22:08:14.080784-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f648040)
default	22:08:14.080787-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f648040) not already running
default	22:08:14.080791-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x98f648040) nothing to teardown
default	22:08:14.080796-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x98f648040) connecting device 85
default	22:08:14.080864-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98f648040) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:14.081108-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x98f648040) created ioproc 0xb for device 85
default	22:08:14.081309-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 7 device listeners to device 85
default	22:08:14.081449-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 0 device delegate listeners to device 85
default	22:08:14.081459-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98f648040)
default	22:08:14.081543-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:14.081552-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:14.081559-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:14.081572-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:14.081581-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:14.081671-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98f648040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:14.081681-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98f648040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:14.081686-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:14.081693-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 0 device listeners from device 0
default	22:08:14.081698-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 0 device delegate listeners from device 0
default	22:08:14.081702-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f648040)
default	22:08:14.081715-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	22:08:14.081757-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x98f648040) caller requesting device change from 85 to 91
default	22:08:14.081764-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f648040)
default	22:08:14.081769-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f648040) not already running
default	22:08:14.081773-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x98f648040) disconnecting device 85
default	22:08:14.081778-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x98f648040) destroying ioproc 0xb for device 85
default	22:08:14.081794-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	22:08:14.081986-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	22:08:14.082267-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x98f648040) connecting device 91
default	22:08:14.082360-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98f648040) Device ID: 91 (Input:Yes | Output:No): true
default	22:08:14.083444-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1958, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.084625-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1958, subject=com.nexy.assistant,
default	22:08:14.085427-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.092482-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	22:08:14.092508-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:08:14.093729-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:08:14.093758-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:14.094664-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.5, subject=com.nexy.assistant,
default	22:08:14.095310-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:14.102591-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x98f648040) created ioproc 0xa for device 91
default	22:08:14.102699-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 7 device listeners to device 91
default	22:08:14.102852-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 0 device delegate listeners to device 91
default	22:08:14.102859-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98f648040)
default	22:08:14.102864-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	22:08:14.102874-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:14.102982-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	22:08:14.102993-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	22:08:14.102998-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	22:08:14.103080-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98f648040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:14.103087-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98f648040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:14.103092-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:14.103096-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 7 device listeners from device 85
default	22:08:14.103235-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 0 device delegate listeners from device 85
default	22:08:14.103240-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f648040)
default	22:08:14.103741-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:08:14.104619-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1959, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.105564-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1959, subject=com.nexy.assistant,
default	22:08:14.106121-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.123609-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:08:14.124445-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1960, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.125345-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1960, subject=com.nexy.assistant,
default	22:08:14.125365-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	22:08:14.125387-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:08:14.125896-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.130709-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	22:08:14.131473-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:08:14.131496-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:14.132304-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.6, subject=com.nexy.assistant,
default	22:08:14.132910-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:14.143364-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1961, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.144310-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1961, subject=com.nexy.assistant,
default	22:08:14.144854-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.161462-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:08:14.161591-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	22:08:14.162272-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:08:14.163136-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:14.163193-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:14.167046-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	22:08:14.228432-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	22:08:14.229485-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	22:08:14.230232-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4393 called from <private>
default	22:08:14.230319-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:14.230870-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:14.230976-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:14.230999-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:14.231007-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:14.231978-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:14.232106-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:14.232539-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:14.232889-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:14.232901-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:14.232913-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:14.233849-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	22:08:14.233932-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:14.233958-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:14.233982-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:14.234005-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.234066-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:14.234066-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	22:08:14.234071-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:14.234096-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:14.234153-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.234258-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.234328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1962, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.234301-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:14.234340-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:14.234380-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.234494-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406b, Nexy(89735), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 108 starting recording
default	22:08:14.234555-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:14.234921-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:14.234977-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:14.235047-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	22:08:14.235109-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.235157-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	22:08:14.235341-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:14.235496-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.235758-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	22:08:14.235769-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:14.236387-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:14.236494-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.237119-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	22:08:14.237243-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.237904-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237840-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237935-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237977-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1962, subject=com.nexy.assistant,
default	22:08:14.237874-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237962-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:14.237905-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237981-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.237927-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:14.238032-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.238044-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:14.238058-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.238115-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:14.238266-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:14.238286-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:14.238321-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:14.238358-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:14.238454-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:14.238467-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:14.238480-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 1
default	22:08:14.238487-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	22:08:14.238497-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	22:08:14.238562-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	22:08:14.238785-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.239499-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.243467-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.243530-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	22:08:14.243557-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	22:08:14.244208-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.244225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.244235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.244241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.244249-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.244255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.244388-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:14.247571-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247585-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247595-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.247601-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.247613-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.247688-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:14.247704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247711-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.247724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.247730-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.247735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.247767-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.247802-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:14.247834-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:14.247848-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:08:14.247878-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
error	22:08:14.257811-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:14.257828-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:14.264991-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.265007-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.265023-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.265031-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.265038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.265045-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.265136-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:14.331267-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.331274-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:14.331448-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:14.331456-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:14.331478-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:14.331479-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:14.331487-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:14.331492-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:14.331487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:14.333034-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:14.332864-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:14.333931-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:14.333892-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:14.334031-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:14.333261-0500	runningboardd	Invalidating assertion 402-89735-70835 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:14.334469-0500	runningboardd	Invalidating assertion 402-336-70830 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:14.333090-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:14.334750-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70872 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:14.334913-0500	runningboardd	Assertion 402-89735-70872 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.334084-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:14.334072-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:14.334126-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:14.340437-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1963, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.346733-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:14.346749-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:14.346995-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.347013-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:14.347019-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:14.352852-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.353140-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:14.353241-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:14.353326-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:14.353367-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:14.353600-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:14.353682-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:14.353887-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.353986-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:14.354020-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:14.358376-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.358436-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:14.358474-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:14.359853-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.360795-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:14.361150-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.361859-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:14.362202-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.362526-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:14.362848-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.364247-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:14.364289-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:14.365222-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
error	22:08:14.370105-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:14.370120-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:14.370127-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:14.370136-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:14.370141-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
error	22:08:14.370887-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:14.370879-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:14.370903-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:14.370912-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:14.370994-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1963, subject=com.nexy.assistant,
default	22:08:14.370920-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:14.371064-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:14.371690-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:14.371712-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:14.371725-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:14.371736-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:14.371747-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:14.371759-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:14.372323-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:14.372339-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:14.372374-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:14.372383-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:14.372390-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:14.372397-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:14.372406-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:14.372411-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:14.372447-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:14.372517-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:14.372555-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:14.372587-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:14.372627-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:14.372673-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:14.372710-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:14.372757-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:14.374221-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.381484-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:14.381504-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:14.381630-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:14.383673-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.383703-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.384016-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:14.384027-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:14.384077-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:14.384237-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:14.384295-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:14.384363-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:14.384484-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:14.400580-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:08:14.400682-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:14.401495-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	22:08:14.401611-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:14.401647-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:14.401681-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:14.428710-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:08:14.428905-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
error	22:08:14.429742-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:14.429761-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:14.429771-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:14.429780-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:14.429788-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:14.429986-0500	runningboardd	Invalidating assertion 402-89735-70872 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:14.430660-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70873 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:14.430757-0500	runningboardd	Assertion 402-89735-70873 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.434508-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1964, subject=com.nexy.assistant,
default	22:08:14.435715-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.440227-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:14.440243-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:14.440254-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:14.440279-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:14.467830-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:08:14.469659-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:14.469744-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:14.494550-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:14.494607-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:14.494626-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:14.494636-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:14.494669-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:14.500832-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4392 called from <private>
default	22:08:14.501751-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70874 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:14.501876-0500	runningboardd	Assertion 402-336-70874 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.502337-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:14.502405-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:14.502484-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:14.502623-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:14.520960-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:14.521967-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	22:08:14.522099-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:14.522139-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	22:08:14.522171-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:14.522274-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.522484-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:14.522380-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	22:08:14.522591-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:14.522694-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.522865-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 108 stopping playing
default	22:08:14.522439-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:08:14.522963-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:14.523082-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:08:14.523173-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:14.523529-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	22:08:14.523560-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:14.523665-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.523401-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f406b to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":89735}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1f406b, sessionType: 'prim', isRecording: true }, 
]
default	22:08:14.528954-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:08:14.529275-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:14.529423-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70875 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:14.529536-0500	runningboardd	Assertion 402-89735-70875 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.530777-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.530631-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.530819-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.530711-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.530853-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	22:08:14.530754-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.530873-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	22:08:14.530895-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	22:08:14.530924-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.531016-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.531038-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:14.531058-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.531124-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:14.531219-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:14.531240-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:14.531253-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:14.531296-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:14.531469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1965, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.547954-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:14.548079-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:14.560838-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70876 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:14.560916-0500	runningboardd	Assertion 402-336-70876 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.563586-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4393 called from <private>
default	22:08:14.563649-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4393 called from <private>
default	22:08:14.563775-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:14.565385-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:14.565434-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:14.565450-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:14.565666-0500	runningboardd	Invalidating assertion 402-89735-70875 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:14.565464-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:14.565470-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:14.565733-0500	runningboardd	Invalidating assertion 402-336-70876 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:14.565574-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:14.565608-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:14.565700-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:14.566307-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:14.566536-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:14.566984-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:14.567377-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:14.567389-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:14.567956-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70877 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:14.568022-0500	runningboardd	Assertion 402-89735-70877 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.567404-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:14.569211-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1966, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:14.571034-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1966, subject=com.nexy.assistant,
default	22:08:14.571841-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:14.575185-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.581598-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.581705-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	22:08:14.581773-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	22:08:14.582973-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583041-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583079-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583107-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583172-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583208-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.583241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583321-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583388-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583408-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	22:08:14.583415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.583499-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583530-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583724-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:14.583750-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.583817-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.583875-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.588538-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.588629-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:14.588694-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:14.588712-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:08:14.597661-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4393 called from <private>
default	22:08:14.597924-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70878 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:14.598016-0500	runningboardd	Assertion 402-336-70878 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:14.608565-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.613929-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:14.613993-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	22:08:14.614043-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	22:08:14.619733-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.620852-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.620884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.621112-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.621154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:14.621197-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:14.621233-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:14.630469-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x990a50520: iounit configuration changed > posting notification
default	22:08:16.110183-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:16.110428-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	22:08:16.180639-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	22:08:17.039063-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	22:08:17.039531-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	22:08:17.039639-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:17.039700-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:08:17.039731-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:17.039783-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406b, Nexy(89735), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 108 stopping recording
default	22:08:17.039805-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:08:17.039808-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	22:08:17.039838-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:17.039874-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:08:17.040091-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	22:08:17.040102-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:17.040163-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:17.042066-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:17.042126-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:17.042184-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:17.042228-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:17.042268-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:17.042341-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:17.042370-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:17.042385-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:17.042397-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	22:08:17.044604-0500	runningboardd	Invalidating assertion 402-89735-70877 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:17.045173-0500	runningboardd	Invalidating assertion 402-336-70878 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:17.053210-0500	Nexy	nw_path_libinfo_path_check [F2DBF84A-3347-4B68-978C-4BCC277403E0 Hostname#bbb63510:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:08:17.053402-0500	mDNSResponder	[R158106] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: b360ab20
default	22:08:17.054342-0500	mDNSResponder	[R158107] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: b360ab20
default	22:08:17.058644-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:17.058762-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:17.058826-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:17.058842-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:08:17.059628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:17.059643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:17.059658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:17.059664-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:17.059672-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:17.059724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:17.059952-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:17.073219-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F46BE84C-43FC-48CE-B0DD-3ED31A01DC4A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53419,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xf27dd4a4 tp_proto=0x06"
default	22:08:17.073328-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53419<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580794 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x950d18bd
default	22:08:17.078152-0500	kernel	tcp connected: [<IPv4-redacted>:53419<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580794 t_state: ESTABLISHED process: Nexy:89735 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x950d18bd
default	22:08:17.143759-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x98f648040) Selecting device 0 from destructor
default	22:08:17.143780-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f648040)
default	22:08:17.143793-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f648040) not already running
default	22:08:17.143798-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x98f648040) disconnecting device 91
default	22:08:17.143805-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x98f648040) destroying ioproc 0xa for device 91
default	22:08:17.143867-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	22:08:17.143913-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:08:17.144109-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x98f648040) nothing to setup
default	22:08:17.144153-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 0 device listeners to device 0
default	22:08:17.144160-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f648040) adding 0 device delegate listeners to device 0
default	22:08:17.144167-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 7 device listeners from device 91
default	22:08:17.144459-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f648040) removing 0 device delegate listeners from device 91
default	22:08:17.144484-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f648040)
default	22:08:17.149935-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:17.149949-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:17.149976-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:17.150021-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:17.153753-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:17.154206-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:17.154848-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:17.531686-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:53419<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580794 t_state: LAST_ACK process: Nexy:89735 Duration: 0.459 sec Conn_Time: 0.005 sec bytes in/out: 648/44857 pkts in/out: 3/9 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.812 ms rttvar: 1.062 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x950d18bd
default	22:08:17.531718-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53419<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580794 t_state: LAST_ACK process: Nexy:89735 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:08:19.365941-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:19.366031-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:19.366070-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:19.366081-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:19.366089-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:19.366108-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:19.367935-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:19.367945-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:19.368029-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:19.368185-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:19.368357-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:19.368577-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:19.388510-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:19.388540-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:19.388727-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:19.389430-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:19.389446-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:19.389563-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:19.389585-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:19.389595-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:19.389923-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:19.390126-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:19.390137-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:19.389978-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:19.390150-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:19.390160-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:19.390827-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:19.390638-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:19.390840-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:19.390940-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:19.390960-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:19.390968-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:19.391231-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:19.391396-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:19.391406-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:19.391422-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:19.391457-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:19.391670-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:19.391860-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:19.391870-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:19.391908-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:19.391918-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:19.391926-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:19.391948-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:19.402432-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:19.402467-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:19.402595-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:19.407677-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:19.408173-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:19.408184-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:19.408231-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:19.408240-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:19.408246-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:19.408253-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:19.408555-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98fceaa40) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:19.408642-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98fceaa40)
default	22:08:19.408905-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:19.409131-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:19.409240-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:19.409342-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:19.409356-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:19.409606-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:19.409712-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:19.409786-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:19.411082-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98fceaa40) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:19.411098-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98fceaa40)
default	22:08:19.411433-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:19.411448-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:19.411457-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:19.411465-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:19.411474-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:19.411802-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:19.411823-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:19.411832-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:19.488383-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:19.488384-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:19.488435-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:19.488451-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:19.488482-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:19.488492-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:19.489041-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:19.489037-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:19.489063-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:19.489120-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:19.489240-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:19.489499-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:19.522109-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x990a50520: iounit configuration changed > posting notification
default	22:08:20.514580-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:20.520131-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x990a50520: start, was running 0
default	22:08:20.522274-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x990670840, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:08:20.522305-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x990670840: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:08:20.522320-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:08:20.522319-0500	Nexy	AudioConverter -> 0x990670840: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	22:08:20.522337-0500	Nexy	AudioConverter -> 0x990670840: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	22:08:20.522346-0500	Nexy	AudioConverter -> 0x990670840: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	22:08:20.523005-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x990670840: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:08:20.525127-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70882 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:20.525278-0500	runningboardd	Assertion 402-89735-70882 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:20.526149-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70883 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:20.526143-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:20.526865-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:20.526899-0500	runningboardd	Assertion 402-336-70883 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:20.526913-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:20.527035-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:20.531894-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:20.532236-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:20.532253-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:20.532267-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:20.532294-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:20.532588-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:20.533018-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:20.536400-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:20.536961-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:20.537154-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:20.838615-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:20.839528-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	22:08:20.839644-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:20.839687-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:20.839725-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:08:20.839773-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'MediaPlayback'
default	22:08:20.839798-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.839823-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	22:08:20.839842-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 108 starting playing
default	22:08:20.839920-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:20.839953-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:20.839984-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:20.839987-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.840042-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.840014-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	22:08:20.840054-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:20.840181-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	22:08:20.840090-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f406b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":89735}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f406b, sessionType: 'prim', isRecording: false }, 
]
default	22:08:20.840194-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:20.840245-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:20.841583-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.841686-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.841713-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:20.841730-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	22:08:20.841738-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	22:08:20.841749-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	22:08:20.841810-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:20.845555-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:22.180507-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
default	22:08:22.550050-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:22.552900-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:24.119072-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:24.121571-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:24.122554-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x98f649540) Selecting device 85 from constructor
default	22:08:24.122581-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f649540)
default	22:08:24.122590-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f649540) not already running
default	22:08:24.122596-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x98f649540) nothing to teardown
default	22:08:24.122601-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x98f649540) connecting device 85
default	22:08:24.122704-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98f649540) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:24.123205-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x98f649540) created ioproc 0xc for device 85
default	22:08:24.123385-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 7 device listeners to device 85
default	22:08:24.123662-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 0 device delegate listeners to device 85
default	22:08:24.123676-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98f649540)
default	22:08:24.123790-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:24.123805-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:24.123826-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:24.123836-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:24.123847-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:24.123980-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98f649540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:24.123996-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98f649540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:24.124020-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:24.124027-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 0 device listeners from device 0
default	22:08:24.124033-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 0 device delegate listeners from device 0
default	22:08:24.124039-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f649540)
default	22:08:24.124057-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	22:08:24.124123-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x98f649540) caller requesting device change from 85 to 91
default	22:08:24.124134-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f649540)
default	22:08:24.124140-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f649540) not already running
default	22:08:24.124145-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x98f649540) disconnecting device 85
default	22:08:24.124151-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x98f649540) destroying ioproc 0xc for device 85
default	22:08:24.124171-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	22:08:24.124438-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	22:08:24.124782-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x98f649540) connecting device 91
default	22:08:24.124885-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98f649540) Device ID: 91 (Input:Yes | Output:No): true
default	22:08:24.126586-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1967, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.128240-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1967, subject=com.nexy.assistant,
default	22:08:24.129290-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.130525-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	22:08:24.130554-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:08:24.132173-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:08:24.132213-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:24.133349-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.7, subject=com.nexy.assistant,
default	22:08:24.134059-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:24.146971-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x98f649540) created ioproc 0xb for device 91
default	22:08:24.147078-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 7 device listeners to device 91
default	22:08:24.147214-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 0 device delegate listeners to device 91
default	22:08:24.147221-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98f649540)
default	22:08:24.147228-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	22:08:24.147237-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:24.147340-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	22:08:24.147347-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	22:08:24.147352-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	22:08:24.147442-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98f649540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:24.147452-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98f649540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:24.147456-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:24.147460-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 7 device listeners from device 85
default	22:08:24.147610-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 0 device delegate listeners from device 85
default	22:08:24.147624-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f649540)
default	22:08:24.147630-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	22:08:24.148091-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:08:24.148947-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1968, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.149832-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1968, subject=com.nexy.assistant,
default	22:08:24.150365-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.164052-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	22:08:24.164077-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	22:08:24.167408-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	22:08:24.168368-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1969, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.169363-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1969, subject=com.nexy.assistant,
default	22:08:24.169732-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	22:08:24.169936-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.170533-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=58201.8, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	22:08:24.170561-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=58201, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	22:08:24.171348-0500	tccd	AUTHREQ_SUBJECT: msgID=58201.8, subject=com.nexy.assistant,
default	22:08:24.171972-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xcb4ed4900 at /Applications/Nexy.app
default	22:08:24.187598-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1970, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.188518-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1970, subject=com.nexy.assistant,
default	22:08:24.189074-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.205681-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	22:08:24.206553-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:08:24.206693-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	22:08:24.208108-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4393 called from <private>
default	22:08:24.208144-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:08:24.208230-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:24.209093-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:24.209199-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.209218-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:24.209223-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:24.210134-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:24.210258-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:24.210558-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.210695-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:24.210707-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:24.210721-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:24.211469-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output","1C-77-54-18-C8-A3:input"],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	22:08:24.211550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:24.211574-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:24.211595-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:24.211616-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.211678-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	22:08:24.211755-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:24.211795-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:24.211879-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:24.211939-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.212049-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:24.212107-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.211920-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1971, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.212080-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:24.212121-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.212271-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406b, Nexy(89735), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 108 starting recording
default	22:08:24.212404-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:24.212770-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:24.212893-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:24.212991-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	22:08:24.213082-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.213165-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	22:08:24.213346-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	22:08:24.213361-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:24.213351-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:24.213551-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.213656-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1971, subject=com.nexy.assistant,
default	22:08:24.214338-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.214232-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:24.214919-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.215176-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	22:08:24.215425-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.216094-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216162-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216130-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216156-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216176-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:24.216196-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216223-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:24.216243-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216311-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:24.216325-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216337-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:24.216375-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216391-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:24.216403-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:24.216413-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	22:08:24.216453-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:24.216470-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:24.216479-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	22:08:24.216487-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 1
default	22:08:24.216494-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	22:08:24.216500-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	22:08:24.216526-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	22:08:24.218010-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.221863-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.221934-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	22:08:24.221982-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	22:08:24.222343-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222357-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222368-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222374-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222383-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222390-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.222405-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222425-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222445-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222451-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.222466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222476-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222491-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.222497-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.222521-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	22:08:24.222503-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.222609-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:24.226325-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.226380-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:24.226418-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:24.226433-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:08:24.234693-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:08:24.235563-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::out-0 issue_detected_sample_time=58560.000000 ] -- [ rms:[-30.853930], peaks:[-16.372330] ]
default	22:08:24.235590-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-38.424175], peaks:[-21.588188] ]
default	22:08:24.235795-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:24.235851-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:24.238768-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.238780-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.238790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.238797-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.238804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.238811-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.238887-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:24.274791-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
error	22:08:24.275115-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:24.275135-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:24.275840-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:24.275851-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:24.275943-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.275960-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:24.275966-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:24.276452-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:24.276572-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:24.276838-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.276956-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:24.276966-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:24.276977-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:24.278275-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1972, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.279448-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1972, subject=com.nexy.assistant,
default	22:08:24.280133-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
error	22:08:24.302031-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:24.302048-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:24.310173-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:24.310194-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:24.310201-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:24.310205-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.310214-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:24.310909-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:24.310920-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.310930-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:24.310936-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.310949-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:24.310942-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:24.310954-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.310961-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:24.311197-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.311212-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:24.311233-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.311269-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.311362-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.313592-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:24.313601-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:24.318126-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:24.318136-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:24.318259-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.318274-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:24.318314-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:24.322525-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.322654-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.323873-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.324289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:24.324634-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:24.324704-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:24.324827-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:24.324898-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
error	22:08:24.333424-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:24.333503-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:24.333574-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:24.333632-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:24.333719-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:24.333776-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:24.334392-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.334501-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:24.334538-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:24.335910-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.335974-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.336060-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.338213-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:24.336114-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:24.314994-0500	runningboardd	Invalidating assertion 402-336-70883 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:24.314992-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1973, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.336152-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:24.336482-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:24.336517-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:24.340029-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:24.336729-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:24.342282-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:24.342305-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:24.342319-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:24.342331-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:24.342351-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:24.342520-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:24.342533-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:24.342572-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:24.342638-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:24.342710-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:24.342792-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:24.342859-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:24.342927-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:24.342972-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:24.343060-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:24.343111-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:24.343183-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:24.343249-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:24.343343-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:24.344113-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1973, subject=com.nexy.assistant,
default	22:08:24.346746-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.353269-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:24.353285-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:24.353405-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:24.362586-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.362906-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:24.362936-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:24.362967-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:24.362978-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:24.363027-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:24.369957-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:24.371454-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	22:08:24.373955-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:24.373974-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:24.377661-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:24.378366-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	22:08:24.378482-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:24.378500-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:24.394907-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	22:08:24.395097-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
error	22:08:24.395961-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	22:08:24.395978-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:24.395989-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:24.395998-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:24.396011-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:24.396097-0500	runningboardd	Invalidating assertion 402-89735-70882 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:24.430186-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	22:08:24.431464-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:24.431546-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x7916b2400] Created node ADM::com.nexy.assistant_4393.4293.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	22:08:24.466912-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:24.466952-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:24.466959-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:24.466979-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:24.466995-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:24.470257-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70886 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:24.474189-0500	runningboardd	Assertion 402-336-70886 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:24.474685-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:24.471935-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4392 called from <private>
default	22:08:24.474735-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:24.474788-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:24.474899-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:24.480256-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:24.481668-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	22:08:24.481954-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.489412-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.492012-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:24.492952-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	22:08:24.493062-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:24.493098-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	22:08:24.493138-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:24.493170-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.493223-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	22:08:24.493243-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:08:24.493257-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:24.493300-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	22:08:24.493330-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:24.493381-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 108 stopping playing
default	22:08:24.493515-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.493419-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:24.493494-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:08:24.497474-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:24.498435-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498580-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498486-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498611-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498521-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498631-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	22:08:24.498650-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	22:08:24.498672-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	22:08:24.498697-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498769-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498796-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:24.498837-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.498874-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:24.499007-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:24.499047-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:24.499088-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:24.499231-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:24.526671-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4393 called from <private>
default	22:08:24.526705-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4393 called from <private>
default	22:08:24.526725-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:4393 called from <private>
default	22:08:24.523878-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70887 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:24.526937-0500	runningboardd	Assertion 402-336-70887 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:24.526740-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:4393 called from <private>
default	22:08:24.526776-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	22:08:24.528861-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:24.528876-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:24.528882-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:24.528902-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:24.528925-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4393 called from <private>
default	22:08:24.529160-0500	runningboardd	Invalidating assertion 402-89735-70885 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:24.528966-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4393 called from <private>
default	22:08:24.529405-0500	runningboardd	Invalidating assertion 402-336-70887 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:24.529937-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:24.530153-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:24.530894-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:24.531061-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:24.531982-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70888 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:24.532063-0500	runningboardd	Assertion 402-89735-70888 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:24.531275-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4393 called from <private>
default	22:08:24.533562-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=406.1976, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=89735, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=396, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	22:08:24.531285-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4393 called from <private>
default	22:08:24.531307-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:24.536883-0500	tccd	AUTHREQ_SUBJECT: msgID=406.1976, subject=com.nexy.assistant,
default	22:08:24.537775-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x922d46a00 at /Applications/Nexy.app
default	22:08:24.541688-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.547163-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.547250-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	22:08:24.547308-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	22:08:24.548257-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548270-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.548376-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548418-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.548480-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.548525-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548556-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.548640-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.548691-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	22:08:24.548666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.563292-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70889 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:24.563385-0500	runningboardd	Assertion 402-336-70889 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:24.567039-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4393 called from <private>
default	22:08:24.571537-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.571556-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.571574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.571584-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.571597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.571650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.571749-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:24.578603-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:24.597774-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x990a50520: iounit configuration changed > posting notification
default	22:08:24.601289-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.601342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601368-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.601385-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.601409-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.601449-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.601458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.601484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.601587-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:24.604207-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.604222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.604234-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.604242-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:24.604249-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:24.604255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:24.604305-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	22:08:25.094799-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	22:08:26.266098-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:27.821683-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:08:27.822067-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	22:08:27.822189-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:27.822261-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	22:08:27.822290-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:27.822339-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f406b, Nexy(89735), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 108 stopping recording
default	22:08:27.822359-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	22:08:27.822364-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	22:08:27.822392-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:27.822429-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:08:27.822566-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	22:08:27.822578-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:27.822715-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:27.823843-0500	Nexy	nw_path_libinfo_path_check [E0AE4B75-FFCE-498D-A27A-4C9CF3E80F21 Hostname#bbb63510:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	22:08:27.824031-0500	runningboardd	Invalidating assertion 402-89735-70888 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735]
default	22:08:27.825109-0500	mDNSResponder	[R158112] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: b360ab20
default	22:08:27.825361-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:27.825172-0500	runningboardd	Invalidating assertion 402-336-70889 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) from originator [osservice<com.apple.powerd>:336]
default	22:08:27.825407-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:27.825263-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	22:08:27.825440-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	22:08:27.825310-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:27.825468-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:27.825540-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	22:08:27.825551-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:27.825560-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	22:08:27.826306-0500	mDNSResponder	[R158113] DNSServiceQueryRecord START -- qname: <mask.hash: 'q1G6sMW6DCYisHd84hGxFA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 89735 (Nexy), name hash: b360ab20
default	22:08:27.828056-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E42773F2-1ED2-40B2-8EE9-BF5759C86714 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.53427,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xcfb764d2 tp_proto=0x06"
default	22:08:27.828178-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:53427<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580860 t_state: SYN_SENT process: Nexy:89735 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b6e5f4a
default	22:08:27.829626-0500	coreaudiod	Sending message. { reporterID=385408890306564, category=IO, type=error, message=["io_cycle_budget": Optional(22541666), "deadline": Optional(77820), "multi_cycle_io_page_faults_duration": Optional(0), "scheduler_latency": Optional(15208), "wg_total_wakeups": Optional(6), "cause_set": Optional(4), "io_frame_counter": Optional(77280), "io_cycle": Optional(161), "is_recovering": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "lateness": Optional(294), "wg_user_time_mach": Optional(94465), "wg_external_wakeups": Optional(4), "output_device_transport_list": Optional(), "cause": Optional(ClientHALIODurationExceededBudget), "input_device_source_list": Optional(Unknown), "time_since_prev_overload": Optional(52532198968875), "wg_system_time_mach": Optional(25842), "multi_cycle_io_page_faults": Optional(0), "other_active_clients": Optional([  ]), "io_page_faults_duration": Optional(0), "num_continuous_silent_io_cycles": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "reporting_latenc<…> }
default	22:08:27.834758-0500	kernel	tcp connected: [<IPv4-redacted>:53427<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580860 t_state: ESTABLISHED process: Nexy:89735 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b6e5f4a
default	22:08:27.834916-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:27.835017-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:27.835083-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	22:08:27.835104-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	22:08:27.835753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:27.835771-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:27.835786-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:27.835793-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	22:08:27.835803-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	22:08:27.835812-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	22:08:27.835941-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	22:08:27.927831-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x98f649540) Selecting device 0 from destructor
default	22:08:27.927849-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x98f649540)
default	22:08:27.927858-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x98f649540) not already running
default	22:08:27.927865-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x98f649540) disconnecting device 91
default	22:08:27.927880-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x98f649540) destroying ioproc 0xb for device 91
default	22:08:27.927933-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	22:08:27.927982-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	22:08:27.928186-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x98f649540) nothing to setup
default	22:08:27.928208-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 0 device listeners to device 0
default	22:08:27.928216-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x98f649540) adding 0 device delegate listeners to device 0
default	22:08:27.928225-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 7 device listeners from device 91
default	22:08:27.928517-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x98f649540) removing 0 device delegate listeners from device 91
default	22:08:27.928534-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x98f649540)
default	22:08:27.931658-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:27.931675-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:27.931689-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:27.931716-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:27.935327-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:27.935933-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:27.936156-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:27.970128-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	22:08:27.970247-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	22:08:28.390075-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:53427<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580860 t_state: LAST_ACK process: Nexy:89735 Duration: 0.562 sec Conn_Time: 0.007 sec bytes in/out: 734/61787 pkts in/out: 4/13 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 7.187 ms rttvar: 1.625 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x9b6e5f4a
default	22:08:28.390115-0500	kernel	tcp_connection_summary [<IPv4-redacted>:53427<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1580860 t_state: LAST_ACK process: Nexy:89735 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 2/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	22:08:30.152213-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:30.152268-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4393)
default	22:08:30.152276-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4399 called from <private>
default	22:08:30.152287-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4399 called from <private>
default	22:08:30.152292-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4393 called from <private>
default	22:08:30.152302-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4393 called from <private>
default	22:08:30.152529-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:30.152604-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.152704-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:30.152851-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:30.152865-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:30.152911-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:30.161303-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:30.161336-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:30.162322-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.162347-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:30.162353-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:30.164916-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.164954-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.165746-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.166048-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:30.166059-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:30.166232-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:30.166317-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:30.166407-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:30.166469-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:30.166501-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:30.166553-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:30.173532-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:30.173609-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:30.174114-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:30.174602-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:30.174637-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:30.174765-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.175818-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	22:08:30.176265-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	22:08:30.174827-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4392 called from <private>
default	22:08:30.174897-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4392 called from <private>
default	22:08:30.175318-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.175465-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4392 called from <private>
default	22:08:30.175527-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4392 called from <private>
default	22:08:30.175582-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:30.175643-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:30.177175-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.177175-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:30.177264-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:30.177269-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.177282-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:30.177297-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:30.177314-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:30.177329-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:30.177346-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4392 called from <private>
default	22:08:30.177360-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4399)
default	22:08:30.177371-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4392 called from <private>
default	22:08:30.177423-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:30.177449-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:30.177521-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:30.177601-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:30.177629-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:30.177674-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:30.177702-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4399 called from <private>
default	22:08:30.177730-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4399 called from <private>
default	22:08:30.177756-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4399 called from <private>
default	22:08:30.177793-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4399 called from <private>
default	22:08:30.177819-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:30.177845-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:30.177881-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4399 called from <private>
default	22:08:30.177916-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4399 called from <private>
default	22:08:30.190587-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:30.190649-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:30.190818-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4392)
default	22:08:30.197196-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.197449-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:30.197524-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:30.197665-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4392 called from <private>
default	22:08:30.197793-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4392 called from <private>
default	22:08:30.197907-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4392 called from <private>
default	22:08:30.198088-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98fceaa40) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:30.198370-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4392 called from <private>
default	22:08:30.198597-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98fceaa40)
default	22:08:30.199070-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:30.199297-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:30.199451-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:30.199645-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:30.199779-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	22:08:30.200072-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	22:08:30.200192-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x98fceaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	22:08:30.200297-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	22:08:30.200691-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x98fceaa40) Device ID: 85 (Input:No | Output:Yes): true
default	22:08:30.200764-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x98fceaa40)
default	22:08:30.201062-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:30.201128-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	22:08:30.201172-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	22:08:30.201209-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	22:08:30.271110-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:30.271131-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4393)
default	22:08:30.271167-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4399 called from <private>
default	22:08:30.271167-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4393 called from <private>
default	22:08:30.271174-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4399 called from <private>
default	22:08:30.271178-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4393 called from <private>
default	22:08:30.278634-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4392)
default	22:08:30.278669-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4392 called from <private>
default	22:08:30.278670-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4399)
default	22:08:30.278680-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4392 called from <private>
default	22:08:30.278690-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4399 called from <private>
default	22:08:30.278697-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4399 called from <private>
default	22:08:30.317820-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x990a50520: iounit configuration changed > posting notification
default	22:08:31.152721-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:31.159156-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x990a50520: start, was running 0
default	22:08:31.161282-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x990670cf0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	22:08:31.161329-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x990670cf0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:08:31.161346-0500	Nexy	AudioConverter -> 0x990670cf0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	22:08:31.161355-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	22:08:31.161374-0500	Nexy	AudioConverter -> 0x990670cf0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	22:08:31.161386-0500	Nexy	AudioConverter -> 0x990670cf0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	22:08:31.162239-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x990670cf0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	22:08:31.164520-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] with description <RBSAssertionDescriptor| "AudioHAL" ID:402-89735-70892 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	22:08:31.164690-0500	runningboardd	Assertion 402-89735-70892 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:31.165237-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54571778.54571787(501)>:89735] from originator [osservice<com.apple.powerd>:336] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:402-336-70893 target:89735 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	22:08:31.165244-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:31.165324-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:31.165371-0500	runningboardd	Assertion 402-336-70893 (target:[app<application.com.nexy.assistant.54571778.54571787(501)>:89735]) will be created as active
default	22:08:31.165373-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:31.165455-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:31.169081-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:31.169449-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring jetsam update because this process is not memory-managed
default	22:08:31.169464-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring suspend because this process is not lifecycle managed
default	22:08:31.169476-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring GPU update because this process is not GPU managed
default	22:08:31.169501-0500	runningboardd	[app<application.com.nexy.assistant.54571778.54571787(501)>:89735] Ignoring memory limit update because this process is not memory-managed
default	22:08:31.169807-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:31.170197-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:31.172911-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54571778.54571787(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	22:08:31.173588-0500	ControlCenter	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:31.173880-0500	gamepolicyd	Received state update for 89735 (app<application.com.nexy.assistant.54571778.54571787(501)>, running-active-NotVisible
default	22:08:31.459976-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	22:08:31.460880-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f406b","name":"Nexy(89735)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	22:08:31.460992-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	22:08:31.461026-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f406b, Nexy(89735), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	22:08:31.461067-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	22:08:31.461112-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f406b, Nexy(89735), 'prim'', AudioCategory changed to 'MediaPlayback'
default	22:08:31.461138-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.461162-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	22:08:31.461173-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 108 starting playing
default	22:08:31.461240-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	22:08:31.461291-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	22:08:31.461287-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.461359-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f406b, Nexy(89735), 'prim'', displayID:'com.nexy.assistant'}
default	22:08:31.461426-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 108, PID = 89735, Name = sid:0x1f406b, Nexy(89735), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	22:08:31.461366-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.461462-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	22:08:31.461669-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	22:08:31.461711-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	22:08:31.461543-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f406b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":89735}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f406b, sessionType: 'prim', isRecording: false }, 
]
default	22:08:31.461734-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x10340001 category Not set
default	22:08:31.463440-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.463315-0500	audiomxd	UpdateAudioState CID 0x10340001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.463469-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	22:08:31.463484-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	22:08:31.463494-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	22:08:31.463505-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	22:08:31.463570-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	22:08:31.468318-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:32.692107-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	22:08:32.695489-0500	Nexy	[com.apple.controlcenter:D515A7FB-80B8-4865-B3BD-6EC232742B29] Sending action(s) in update: NSSceneFenceAction
default	22:08:34.180483-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
