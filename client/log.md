default	21:50:46.289947-0500	dmd	Requested application com.nexy.assistant has policy OK, associated categories:DH1005 associated sites:(null) equivalent bundle identifiers:com.nexy.assistant
default	21:50:48.220593-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	21:50:48.220781-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	21:50:48.223176-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	21:50:48.232713-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	21:50:48.235486-0500	runningboardd	Launch request for app<application.com.nexy.assistant.58107047.58107056(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	21:50:48.235588-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.58107047.58107056(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:65373] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-65373-48771 target:app<application.com.nexy.assistant.58107047.58107056(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:50:48.235683-0500	runningboardd	Assertion 394-65373-48771 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) will be created as active
default	21:50:48.238575-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	21:50:48.238624-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.58107047.58107056(501)>
default	21:50:48.238642-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	21:50:48.238734-0500	runningboardd	app<application.com.nexy.assistant.58107047.58107056(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	21:50:48.280520-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] is not RunningBoard jetsam managed.
default	21:50:48.280538-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] This process will not be managed.
default	21:50:48.280551-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:50:48.280730-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:50:48.281599-0500	gamepolicyd	Hit the server for a process handle 1873c7da0000baf5 that resolved to: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:50:48.281641-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:50:48.284096-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:50:48.284182-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-48772 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:50:48.284337-0500	runningboardd	Assertion 394-394-48772 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:50:48.284559-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:50:48.284581-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:50:48.284605-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Set darwin role to: UserInteractive
default	21:50:48.284615-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:50:48.284636-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:50:48.284722-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] reported to RB as running
default	21:50:48.286473-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:47861" ID:394-357-48773 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:50:48.286648-0500	runningboardd	Assertion 394-357-48773 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:50:48.286676-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x256256 com.nexy.assistant starting stopped process.
default	21:50:48.288072-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:50:48.288285-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae62105a0: Nexy> state 2
default	21:50:48.288312-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	21:50:48.289136-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:50:48.289222-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:50:48.289252-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:50:48.289351-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:50:48.289532-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:50:48.290499-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:50:48.290844-0500	runningboardd	Invalidating assertion 394-65373-48771 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:65373]
default	21:50:48.290883-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:50:48.290895-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:50:48.290971-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:50:48.291018-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:50:48.291420-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:50:48.294186-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:50:48.396904-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:50:48.397954-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:50:48.397969-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:50:48.397977-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:50:48.397995-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:50:48.402560-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:50:48.402995-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:50:52.493441-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: bdc8e848b00a8952), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant), 0, 0, 1, 0, 4, 4, 1
default	21:50:52.494333-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.27, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	21:50:52.501040-0500	tccd	AUTHREQ_SUBJECT: msgID=489.27, subject=com.nexy.assistant,
default	21:50:52.501909-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:50:52.517848-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: bdc8e848b00a8952), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant)
default	21:50:53.126791-0500	kernel	Nexy[47861] triggered unnest of range 0x202000000->0x204000000 of DYLD shared region in VM map 0x82acd8f80e690b5f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	21:50:53.126816-0500	kernel	Nexy[47861] triggered unnest of range 0x204000000->0x206000000 of DYLD shared region in VM map 0x82acd8f80e690b5f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	21:50:53.338092-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-48772 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861])
default	21:50:53.538642-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:50:53.538662-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:50:53.538675-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:50:53.538708-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:50:53.541915-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:50:53.542581-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:50:53.740643-0500	Nexy	[0x1029d2700] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	21:50:53.740744-0500	Nexy	[0x1029e2d70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	21:50:54.243320-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1029c8100 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:50:54.243550-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1029c8100 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:50:54.243766-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1029c8100 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:50:54.243963-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1029c8100 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	21:50:54.245265-0500	Nexy	[0x1029e9570] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	21:50:54.246014-0500	Nexy	[0xcb063c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	21:50:54.246313-0500	Nexy	[0xcb063c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	21:50:54.246841-0500	Nexy	[0xcb063c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	21:50:54.248903-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	21:50:54.249836-0500	Nexy	[0xcb063c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:50:54.250488-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:50:54.251699-0500	Nexy	Received configuration update from daemon (initial)
default	21:50:54.252139-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.1, subject=com.nexy.assistant,
default	21:50:54.253165-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:50:54.267129-0500	Nexy	[0xcb063c3c0] invalidated after the last release of the connection object
default	21:50:54.267469-0500	Nexy	server port 0x00003013, session port 0x00003013
default	21:50:54.268652-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1513, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:50:54.268682-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:50:54.269560-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1513, subject=com.nexy.assistant,
default	21:50:54.270359-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:50:54.290062-0500	Nexy	New connection 0xe72e3 main
default	21:50:54.293174-0500	Nexy	CHECKIN: pid=47861
default	21:50:54.301459-0500	launchservicesd	CHECKIN:0x0-0x256256 47861 com.nexy.assistant
default	21:50:54.301595-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:47861" ID:394-357-48778 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:50:54.301704-0500	runningboardd	Assertion 394-357-48778 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:50:54.301588-0500	Nexy	CHECKEDIN: pid=47861 asn=0x0-0x256256 foreground=0
default	21:50:54.302205-0500	runningboardd	Invalidating assertion 394-357-48773 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	21:50:54.301954-0500	Nexy	[0xcb063c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:50:54.301971-0500	Nexy	[0xcb063c3c0] Connection returned listener port: 0x4303
default	21:50:54.302155-0500	Nexy	[0xcb1690180] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xcb063c3c0.peer[357].0xcb1690180
default	21:50:54.303672-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:50:54.303802-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	21:50:54.304961-0500	Nexy	FRONTLOGGING: version 1
default	21:50:54.304970-0500	Nexy	Registered, pid=47861 ASN=0x0,0x256256
default	21:50:54.305258-0500	WindowServer	e72e3[CreateApplication]: Process creation: 0x0-0x256256 (Nexy) connectionID: E72E3 pid: 47861 in session 0x101
default	21:50:54.305447-0500	Nexy	[0xcb063c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	21:50:54.307311-0500	Nexy	[0xcb063c3c0] Connection returned listener port: 0x4303
default	21:50:54.308001-0500	Nexy	BringForward: pid=47861 asn=0x0-0x256256 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	21:50:54.308154-0500	Nexy	BringFrontModifier: pid=47861 asn=0x0-0x256256 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	21:50:54.309072-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	21:50:54.312330-0500	Nexy	No persisted cache on this platform.
default	21:50:54.313325-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	21:50:54.314096-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	21:50:54.317462-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	21:50:54.317473-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	21:50:54.317532-0500	Nexy	Initializing connection
default	21:50:54.317572-0500	Nexy	Removing all cached process handles
default	21:50:54.317599-0500	Nexy	Sending handshake request attempt #1 to server
default	21:50:54.317610-0500	Nexy	Creating connection to com.apple.runningboard
default	21:50:54.317620-0500	Nexy	[0xcb063c640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	21:50:54.318152-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] as ready
default	21:50:54.318895-0500	Nexy	Handshake succeeded
default	21:50:54.318912-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.58107047.58107056(501)>
default	21:50:54.319633-0500	Nexy	[0xcb063c3c0] Connection returned listener port: 0x4303
default	21:50:54.320722-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 47861
default	21:50:54.328120-0500	Nexy	[0xcb063c3c0] Connection returned listener port: 0x4303
default	21:50:54.332268-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	21:50:54.332290-0500	Nexy	[0xcb063c780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	21:50:54.332381-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	21:50:54.332451-0500	Nexy	[0xcb063ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:50:54.335694-0500	Nexy	[0xcb063ca00] Connection returned listener port: 0x6a03
default	21:50:54.336524-0500	Nexy	Registered process with identifier 47861-1029399
default	21:50:57.940509-0500	Electron	defer invalidatation: (
    "<ElectronNSWindow: 0x10403674a40, Nexy_v1.6.1.27 \U2014 Walkthrough>",
    "<ElectronNSWindow: 0x1040367e440, client \U2014 main.py>",
    "<ElectronNSWindow: 0x10404ac4200, server \U2014 main.py>",
    "<_NSFullScreenMouseDetectionWindow: 0x10406aeea80, >",
    "<_NSFullScreenMouseDetectionWindow: 0x10406aee3c0, >",
    "<_NSFullScreenMouseDetectionWindow: 0x10406aee840, >"
)
default	21:50:58.675163-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B3166C24-A92E-4CF9-97B9-D39DB8EC7AFD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51233,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xefcad482 tp_proto=0x06"
default	21:50:58.675302-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51233<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062691 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0e91ad1
default	21:50:58.950938-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	21:51:03.676707-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51233<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062691 t_state: SYN_SENT process: Nexy:47861 Duration: 5.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb0e91ad1
default	21:51:03.676739-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51233<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062691 t_state: SYN_SENT process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:51:03.677824-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4864BB07-905B-4CB2-A300-585A8B91DD11 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51235,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x224de58c tp_proto=0x06"
default	21:51:03.677982-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51235<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062707 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa23e5a83
default	21:51:05.313133-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	21:51:08.677470-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51235<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062707 t_state: SYN_SENT process: Nexy:47861 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa23e5a83
default	21:51:08.677493-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51235<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062707 t_state: SYN_SENT process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:51:08.682750-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:51:08.684426-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:51:08.687531-0500	Nexy	nw_path_libinfo_path_check [8DA7DA8D-F11D-49B0-9178-AD9EBE0E153A Hostname#9713b326:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:51:08.688338-0500	mDNSResponder	[R80591] DNSServiceCreateConnection START PID[47861](Nexy)
default	21:51:08.688431-0500	mDNSResponder	[R80592] DNSServiceQueryRecord START -- qname: <mask.hash: 'UScWDXXJU+z4Xf3lW2QKnQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 47861 (Nexy), name hash: f92d5498
default	21:51:08.689224-0500	mDNSResponder	[R80593] DNSServiceQueryRecord START -- qname: <mask.hash: 'UScWDXXJU+z4Xf3lW2QKnQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 47861 (Nexy), name hash: f92d5498
default	21:51:08.700522-0500	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 32FFFDD5-0EB7-4E92-A1B9-CCBF35D14FB5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51236,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6907da3b tp_proto=0x06"
default	21:51:08.700639-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51236<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062741 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabce56e6
default	21:51:13.679183-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51236<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062741 t_state: SYN_SENT process: Nexy:47861 Duration: 4.978 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xabce56e6
default	21:51:13.679219-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51236<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062741 t_state: SYN_SENT process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:51:15.392772-0500	Nexy	[0xcb063cdc0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	21:51:15.411988-0500	usernoted	Connection com.nexy.assistant with path: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:15.413156-0500	NotificationCenter	Looking up app info for com.nexy.assistant
default	21:51:15.426970-0500	NotificationCenter	Found info for com.nexy.assistant at <private>. app name: Nexy
default	21:51:15.429914-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.002 sec]: Request: Starting
default	21:51:15.430104-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.003 sec]: Running step 'Step: UserNotificationsCore.OneTimeCodeActor, index: 0'. Remaining steps after this step: 2'
default	21:51:15.430229-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.003 sec]: Starting step 'Step: UserNotificationsCore.OneTimeCodeActor, index: 0'
default	21:51:15.431154-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.004 sec]: Calling out to completion with success([id=, time=2026-02-17 02:51:15, bundle=com.nexy.assistant]) from 'run(_:_:completion:)'
default	21:51:15.431407-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.004 sec]: Success for 'Step: UserNotificationsCore.OneTimeCodeActor, index: 0'.
default	21:51:15.431651-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.004 sec]: Running step 'Step: UserNotificationsCore.IntelligenceActor, index: 1'. Remaining steps after this step: 1'
default	21:51:15.431940-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.004 sec]: Starting step 'Step: UserNotificationsCore.IntelligenceActor, index: 1'
default	21:51:15.432694-0500	usernoted	Indexing: [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant]
default	21:51:15.432818-0500	usernoted	[[id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant]] Adding notification index
default	21:51:15.442256-0500	suggestd	HVDonationReceiver: received 1 searchableItems for com.apple.usernotificationsd ((
    "com.nexy.assistant:"
))
error	21:51:15.442334-0500	suggestd	HVDonationReceiver: HVBiomeConversions biomeEventFromSearchableItem bid:com.apple.usernotificationsd uid:com.nexy.assistant: did:com.apple.usernotifications failed: (null)
default	21:51:15.442770-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.00s] Pipeline started
default	21:51:15.448844-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.01s] AvailabilityManager: Fetching model availability for: ["summarization.summarizeUserNotification", "summarization.summarizeUserNotificationThread", "classification.classifyUserNotification"]
default	21:51:15.471318-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	21:51:15.472387-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	21:51:15.474119-0500	Nexy	[0xcb063cf00] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	21:51:15.476632-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
default	21:51:15.481313-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	21:51:15.482956-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:51:15.483109-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:51:15.483262-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	21:51:15.483273-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	21:51:15.483305-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:51:15.483437-0500	Nexy	[0xcb063d040] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:51:15.483951-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:51:15.484101-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	21:51:15.490675-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.2, subject=com.nexy.assistant,
default	21:51:15.491383-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:15.505382-0500	Nexy	[0xcb063d040] invalidated after the last release of the connection object
default	21:51:15.505450-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:51:15.508419-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	21:51:15.509646-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1145, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:15.510751-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1145, subject=com.nexy.assistant,
default	21:51:15.511389-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:51:15.524554-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	21:51:15.525468-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1147, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:15.526607-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1147, subject=com.nexy.assistant,
default	21:51:15.527264-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:15.530635-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.09s] Enqueued: <private>
default	21:51:15.530672-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.09s] Started processing: <private>; request type: Summarization and Urgency
default	21:51:15.530797-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.09s] Processing notification; communication: false
default	21:51:15.536554-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.10s] Not fetching context for notification
default	21:51:15.543526-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	21:51:15.543554-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xcb37c98e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	21:51:15.547796-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.11s] Ineligible for urgency (urgencyFilter notification urgency disabled)
default	21:51:15.547859-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.11s] Ineligible for summarization (summarizationFilter notification not communication)
default	21:51:15.549621-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.11s] Finished processing (<private>)
default	21:51:15.549864-0500	usernoted	[id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant] Got inference NotificationInference(summaryLength: nil, priority: nil, summaryStatus: ineligible, priorityStatus: ineligible
default	21:51:15.550214-0500	usernoted	com.nexy.assistant systemSummarization 1, sourceSummarization 1, systemPrioritization 0, sourcePrioritization 0,
default	21:51:15.550360-0500	usernoted	[id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant] canSummarize true, canPrioritize false, summaryStatus: 4, hasSummary: 0, priorityStatus: 5, priority: false
default	21:51:15.550503-0500	suggestd	[kind: notification | app: com.nexy.assistant | id-hash: 7ee19e619aee3f55 | rcvd: 792989475.439839 | pos: 0 | qos: 17 | t: 0.11s] Finished processing: <private>; request type: Summarization and Urgency
default	21:51:15.553426-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.126 sec]: Calling out to completion with success([id=, time=2026-02-17 02:51:15, bundle=com.nexy.assistant]) from 'run(_:_:completion:)'
default	21:51:15.553642-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.126 sec]: Success for 'Step: UserNotificationsCore.IntelligenceActor, index: 1'.
default	21:51:15.553776-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.126 sec]: Running step 'Step: UserNotificationsCore.BehaviorResolutionActor, index: 2'. Remaining steps after this step: 0'
default	21:51:15.553890-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.126 sec]: Starting step 'Step: UserNotificationsCore.BehaviorResolutionActor, index: 2'
default	21:51:15.554012-0500	usernoted	[com.apple.usernotifications.pipeline:B42354B8-3B72-4D80-A3FD-725FD50FFB3F] Resolving behavior for event, details=<DNDMutableClientEventDetails: 0x7a4d0e280; identifier: ''; bundleIdentifier: com.nexy.assistant; platform: unknown; type: Default; urgency: Default; sender: (null); threadIdentifier: 0; filterCritera: (null); notifyAnyway: 0; behavior: Default; forwardingBehavior: (null); title: (null); subtitle: (null); body: (null); shouldAdjustEventBehaviorForMirroring: 0>
default	21:51:15.555422-0500	donotdisturbd	Event was resolved: resolution=<DNDSEventBehaviorResolution: 0x841321440; UUID: 4C1175CB-21E9-4114-BADC-BBFAD85E6126; date: 2026-02-17 02:51:15 +0000; eventBehavior: <DNDClientEventBehavior: 0x841325ad0; eventDetails: <DNDClientEventDetails: 0x8412e4780; identifier: ''; bundleIdentifier: com.nexy.assistant; platform: unknown; type: Default; urgency: Default; sender: (null); threadIdentifier: 0; filterCritera: (null); notifyAnyway: 0; behavior: Default; forwardingBehavior: (null); title: (null); subtitle: (null); body: (null); shouldAdjustEventBehaviorForMirroring: 0>; interruptionSuppression: none; intelligentBehavior: unused; resolutionReason: disabled; activeModeUUID: (null)>; clientIdentifier: 'com.apple.usernotifications.pipeline'; outcome: allowed; reason: disabled>
default	21:51:15.555672-0500	usernoted	[com.apple.usernotifications.pipeline:B42354B8-3B72-4D80-A3FD-725FD50FFB3F] Resolved event, details=<DNDMutableClientEventDetails: 0x7a4d0e280; identifier: ''; bundleIdentifier: com.nexy.assistant; platform: unknown; type: Default; urgency: Default; sender: (null); threadIdentifier: 0; filterCritera: (null); notifyAnyway: 0; behavior: Default; forwardingBehavior: (null); title: (null); subtitle: (null); body: (null); shouldAdjustEventBehaviorForMirroring: 0> behavior=<DNDClientEventBehavior: 0x7a5736fd0; eventDetails: <DNDClientEventDetails: 0x7a4d0e700; identifier: ''; bundleIdentifier: com.nexy.assistant; platform: unknown; type: Default; urgency: Default; sender: (null); threadIdentifier: 0; filterCritera: (null); notifyAnyway: 0; behavior: Default; forwardingBehavior: (null); title: (null); subtitle: (null); body: (null); shouldAdjustEventBehaviorForMirroring: 0>; interruptionSuppression: none; intelligentBehavior: unused; resolutionReason: disabled; activeModeUUID: (null)>
default	21:51:15.556006-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.129 sec]: Calling out to completion with success([id=, time=2026-02-17 02:51:15, bundle=com.nexy.assistant]) from 'run(_:_:completion:)'
default	21:51:15.556128-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.129 sec]: Success for 'Step: UserNotificationsCore.BehaviorResolutionActor, index: 2'.
default	21:51:15.556236-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.129 sec]: Request: Completed
default	21:51:15.556442-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.129 sec]: Request: Calling completion delegate
default	21:51:15.556629-0500	usernoted	[create, [id=DA39-A3EE, time=2026-02-17 02:51:15, bundle=com.nexy.assistant], Time elapsed=0.129 sec]: Request: Calling pipeline completion with success
default	21:51:15.556782-0500	usernoted	<NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>"> successfully processed by pipeline, scheduled for delivery.
error	21:51:15.558048-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	21:51:15.558059-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	21:51:15.558552-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	21:51:15.562289-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:15.562414-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:15.567248-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:51:15.573210-0500	Nexy	[0xcb063d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	21:51:15.583302-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xcb28d6340) Selecting device 85 from constructor
default	21:51:15.583314-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:15.583323-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:15.583331-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xcb28d6340) nothing to teardown
default	21:51:15.583339-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xcb28d6340) connecting device 85
default	21:51:15.583450-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xcb28d6340) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:15.583530-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xcb28d6340) created ioproc 0xa for device 85
default	21:51:15.583656-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 7 device listeners to device 85
default	21:51:15.583836-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 85
default	21:51:15.583848-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xcb28d6340)
default	21:51:15.583930-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:15.583939-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:15.583945-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:15.583950-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:15.583959-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:15.584069-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:15.584079-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:15.584084-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:15.584089-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device listeners from device 0
default	21:51:15.584093-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 0
default	21:51:15.584095-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:15.584109-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:51:15.584188-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xcb28d6340) caller requesting device change from 85 to 91
default	21:51:15.584194-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:15.584201-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:15.584207-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xcb28d6340) disconnecting device 85
default	21:51:15.584211-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xcb28d6340) destroying ioproc 0xa for device 85
default	21:51:15.584259-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	21:51:15.585629-0500	Nexy	[0xcb063d2c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	21:51:15.586342-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":{"PID":47861,"session_type":"Primary"} }
default	21:51:15.586417-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":47861}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea041, sessionType: 'prim', isRecording: false }, 
]
default	21:51:15.587017-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 47861, name = Nexy
default	21:51:15.587285-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xcb154f980 with ID: 0x1ea041
default	21:51:15.588009-0500	Nexy	[0xcb063d400] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	21:51:15.588300-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=205561429753857 }
default	21:51:15.588318-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:15.588366-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:51:15.588452-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xcb28d6340) connecting device 91
default	21:51:15.588588-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xcb28d6340) Device ID: 91 (Input:Yes | Output:No): true
default	21:51:15.589844-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1148, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:15.591610-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1148, subject=com.nexy.assistant,
default	21:51:15.592755-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:15.613286-0500	tccd	AUTHREQ_PROMPTING: msgID=399.1148, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy},
default	21:51:15.658395-0500	usernoted	Delivering <NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>"> to [ .alert .lockScreen .notificationCenter ]: updatedExisting: false
default	21:51:15.658642-0500	usernoted	Presenting <NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>"> as banner (["badge", "sound", "alert"])
default	21:51:15.659369-0500	NotificationCenter	record <NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>"> is not intelligentlyBrokethrough
default	21:51:15.659459-0500	NotificationCenter	addOrUpdate listItem: com.nexy.assistant:2614F06D from app com.nexy.assistant, canDisplayWhileCenterIsClosed: true, visibility: [history, alert, lockscreen, allowsScreenWake], readCount: 0
default	21:51:15.659470-0500	NotificationCenter	Adding notification to storage: com.nexy.assistant:2614F06D
default	21:51:15.659544-0500	NotificationCenter	[com.nexy.assistant:2614F06D][record: <NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>">] displaying as banner, body: <private>, summary: <private>
default	21:51:15.659625-0500	NotificationCenter	Playing notification sound { nam: NSUserNotificationDefaultSoundName } for com.nexy.assistant
default	21:51:15.686193-0500	suggestd	[kind: notificationStack | app: com.nexy.assistant | id: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | rcvd: 792989475.686017 | pos: 0 | qos: 17 | t: 0.00s] Pipeline started
default	21:51:15.686389-0500	suggestd	[kind: notificationStack | app: com.nexy.assistant | id: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | rcvd: 792989475.686017 | pos: 0 | qos: 17 | t: 0.00s] Invalid (notification stack already summarized)
default	21:51:15.686417-0500	suggestd	[kind: notificationStack | app: com.nexy.assistant | id: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | rcvd: 792989475.686017 | pos: 0 | qos: 17 | t: 0.00s] Can't enter pipeline
default	21:51:15.711985-0500	NotificationCenter	record <NotificationRecord app:"com.nexy.assistant" ident:"DA39-A3EE" req:"" uuid:"2614F06D" source:"276CB6F2" staticCategory:"<LEGACY options=(legacyBehavior, hiddenPreviewShowsTitle) actions=[
    <ACTION style=button title=''>
  ]>"> is not intelligentlyBrokethrough
default	21:51:15.712042-0500	NotificationCenter	[com.nexy.assistant:2614F06D] updating existing notification with content from 2614F06D
default	21:51:15.712093-0500	NotificationCenter	Adding notification to storage: com.nexy.assistant:2614F06D
default	21:51:17.706531-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    465 = "<TCCDEventSubscriber: token=465, state=Initial, csid=(null)>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.photolibraryd>";
    463 = "<TCCDEventSubscriber: token=463, state=Passed, csid=com.apple.chronod>";
}
default	21:51:17.707469-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xcb28d6340) created ioproc 0xa for device 91
default	21:51:17.707709-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 7 device listeners to device 91
default	21:51:17.707943-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 91
default	21:51:17.707957-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xcb28d6340)
default	21:51:17.707973-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	21:51:17.707989-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:17.708180-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:51:17.708194-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	21:51:17.708201-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:51:17.708348-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:17.708362-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:17.708370-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:17.708379-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 7 device listeners from device 85
default	21:51:17.708991-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 85
default	21:51:17.709084-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:17.709757-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:51:17.713114-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1149, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:17.715828-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1149, subject=com.nexy.assistant,
default	21:51:17.718307-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb155b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:17.723037-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	21:51:17.741651-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	21:51:17.741795-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	21:51:17.741960-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xcb3875110, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	21:51:17.742300-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:51:17.744076-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1150, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:17.745779-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1150, subject=com.nexy.assistant,
default	21:51:17.746856-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:17.767590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1151, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:17.768731-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1151, subject=com.nexy.assistant,
default	21:51:17.769391-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:17.789602-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:51:17.789984-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:51:17.794414-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2904.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:51:17.901710-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:51:17.903371-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:51:17.903345-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2904 called from <private>
default	21:51:17.904100-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:17.904313-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:17.904330-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2904 called from <private>
default	21:51:17.904336-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2904 called from <private>
default	21:51:17.905426-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48801 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:17.905550-0500	runningboardd	Assertion 394-328-48801 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
fault	21:51:17.906790-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
default	21:51:17.907020-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:17.908169-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:17.908369-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:17.908221-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:17.909164-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:17.908608-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:17.907644-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:17.907660-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:17.907665-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:17.911603-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:17.911621-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:17.911631-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:17.911633-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2904 called from <private>
default	21:51:17.911639-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:17.911690-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2904 called from <private>
default	21:51:17.911761-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2904 called from <private>
fault	21:51:17.912615-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
default	21:51:17.917303-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	21:51:17.917948-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:51:17.918704-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:17.920247-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:17.920423-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:17.920567-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	21:51:17.920615-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea041, Nexy(47861), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 65 starting recording
default	21:51:17.920850-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:17.911868-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2904 called from <private>
default	21:51:17.911906-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2904 called from <private>
default	21:51:17.911977-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2904 called from <private>
default	21:51:17.912017-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2904 called from <private>
default	21:51:17.912072-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2904 called from <private>
default	21:51:17.920943-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:51:17.912400-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2904 called from <private>
default	21:51:17.921127-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:17.920823-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea041, Nexy(47861), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	21:51:17.912441-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2904 called from <private>
default	21:51:17.921271-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:17.921315-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:17.921256-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	21:51:17.923306-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:51:17.921447-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:51:17.921911-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:17.922893-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2904 called from <private>
default	21:51:17.925064-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1152, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:17.936609-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:17.936728-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:17.936753-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:17.944449-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:17.944793-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:17.944801-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:17.944962-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:17.948230-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:17.948613-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:17.948625-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:17.949193-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:17.949331-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:17.949646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:17.949773-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:17.950261-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:17.950545-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:17.950742-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:17.952768-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:51:17.954297-0500	runningboardd	Invalidating assertion 394-328-48801 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) from originator [osservice<com.apple.powerd>:328]
default	21:51:17.950925-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:17.951117-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:17.951258-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:17.966548-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:17.966684-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:17.966790-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:17.966893-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:17.981494-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:51:17.988111-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:51:18.008883-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:18.008981-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:18.009018-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:18.009690-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:18.012190-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:18.012208-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:18.012219-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:18.012242-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:18.012577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.012610-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.012649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:18.012671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.012681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:18.012686-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:18.036427-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:51:18.036586-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:51:18.038389-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2904 called from <private>
default	21:51:18.038454-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2904 called from <private>
default	21:51:18.039027-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:18.039313-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:18.039341-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2904 called from <private>
default	21:51:18.039350-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2904 called from <private>
default	21:51:18.039458-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:51:18.039542-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48807 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:18.039666-0500	runningboardd	Assertion 394-328-48807 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:51:18.039815-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:51:18.039936-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:18.039982-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:18.039993-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:51:18.040026-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:18.040070-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea041, Nexy(47861), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 65 stopping recording
default	21:51:18.040087-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:51:18.040090-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:18.040115-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:18.040111-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:51:18.040103-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:18.040184-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:18.040241-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:18.040235-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:18.049010-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:18.049071-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:18.049117-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:18.049217-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:18.050071-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.050100-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.050123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:18.050137-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:18.050229-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:18.050240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:18.050318-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:18.149182-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:18.149200-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:18.149219-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:18.149249-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:18.152178-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:51:18.152878-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:51:18.153266-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xcb28d6340) Selecting device 0 from destructor
default	21:51:18.153281-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:18.153287-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:18.153292-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xcb28d6340) disconnecting device 91
default	21:51:18.153297-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xcb28d6340) destroying ioproc 0xa for device 91
default	21:51:18.153328-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:51:18.153358-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:51:18.153502-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xcb28d6340) nothing to setup
default	21:51:18.153517-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device listeners to device 0
default	21:51:18.153522-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 0
default	21:51:18.153528-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 7 device listeners from device 91
default	21:51:18.153723-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 91
default	21:51:18.153738-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:18.594052-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:51:18.594526-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:51:18.595356-0500	node	nw_path_libinfo_path_check [91B3CB7C-1B04-43EC-A03E-4A146618D0A6 Hostname#505485b8:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:51:18.707607-0500	node	nw_path_libinfo_path_check [CD42D4B6-DBC6-4490-95C8-8E5941DD169D Hostname#01db788e:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:51:20.699814-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:20.699873-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2904 called from <private>
default	21:51:20.699887-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:20.701488-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.701536-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:20.701550-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:20.712737-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:20.712794-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2904 called from <private>
default	21:51:20.712800-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2904 called from <private>
default	21:51:20.717783-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:20.717817-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:20.728563-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:20.728600-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:20.728817-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.732253-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.732490-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:20.732501-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:20.732692-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.734973-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.735341-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:20.735482-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:20.736601-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:20.736676-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:20.736717-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:20.736771-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:20.736829-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:20.736928-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.736967-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:20.737135-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:20.737207-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:20.737375-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:20.737489-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:20.737555-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:20.737612-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:20.742867-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.742909-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:20.742918-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:20.743201-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:20.743216-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:20.744652-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.745425-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.745434-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:20.745693-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:20.745790-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:20.745866-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:20.748990-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.749406-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.749413-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:20.749789-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.750132-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:20.750413-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:20.750562-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:20.750694-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:20.750847-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:20.752460-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:20.752772-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:20.753032-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:20.753303-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:20.753539-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:20.753741-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:23.406385-0500	Nexy	[0xcb063d540] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	21:51:23.406960-0500	Nexy	[0xcb063d540] invalidated after the last release of the connection object
default	21:51:23.408016-0500	kernel	udp connect: [<IPv4-redacted>:63644<-><IPv4-redacted>:53] interface:  (skipped: 0)
so_gencnt: 1062848 so_state: 0x0102 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8b5f0d8f
default	21:51:23.431129-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1062850 so_state: 0x0000 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	21:51:23.431165-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1062850 so_state: 0x0000 process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	21:51:23.437803-0500	kernel	udp connect: [<IPv4-redacted>:57807<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1062851 so_state: 0x0002 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb7c9a2f2
default	21:51:23.437829-0500	kernel	udp_connection_summary [<IPv4-redacted>:57807<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1062851 so_state: 0x0002 process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb7c9a2f2 flowctl: 0us (0x)
default	21:51:23.437922-0500	kernel	udp_connection_summary [<IPv4-redacted>:63644<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1062848 so_state: 0x0132 process: Nexy:47861 Duration: 0.030 sec Conn_Time: 0.029 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8b5f0d8f flowctl: 0us (0x)
default	21:51:23.439487-0500	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 62DFA593-D8B5-4C38-A01A-C6527608557C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51240,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x43d5c8ee tp_proto=0x06"
default	21:51:23.439558-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51240<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1062852 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88d90c12
default	21:51:23.451004-0500	kernel	tcp connected: [<IPv4-redacted>:51240<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1062852 t_state: ESTABLISHED process: Nexy:47861 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88d90c12
default	21:51:33.158329-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xcb28d6340) Selecting device 85 from constructor
default	21:51:33.158354-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:33.158371-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:33.158384-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xcb28d6340) nothing to teardown
default	21:51:33.158390-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xcb28d6340) connecting device 85
default	21:51:33.158529-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xcb28d6340) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:33.158683-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xcb28d6340) created ioproc 0xb for device 85
default	21:51:33.158840-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 7 device listeners to device 85
default	21:51:33.159276-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 85
default	21:51:33.159303-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xcb28d6340)
default	21:51:33.159502-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:33.159531-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:33.159547-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:33.159565-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:33.159585-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:33.159887-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:33.159920-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:33.159938-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:33.159950-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device listeners from device 0
default	21:51:33.159962-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 0
default	21:51:33.159974-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:33.160006-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:51:33.160155-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xcb28d6340) caller requesting device change from 85 to 91
default	21:51:33.160171-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:33.160183-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:33.160197-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xcb28d6340) disconnecting device 85
default	21:51:33.160208-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xcb28d6340) destroying ioproc 0xb for device 85
default	21:51:33.160258-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:33.160332-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:51:33.160520-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xcb28d6340) connecting device 91
default	21:51:33.160722-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xcb28d6340) Device ID: 91 (Input:Yes | Output:No): true
default	21:51:33.164371-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1153, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.167745-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1153, subject=com.nexy.assistant,
default	21:51:33.169513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.195622-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xcb28d6340) created ioproc 0xb for device 91
default	21:51:33.195764-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 7 device listeners to device 91
default	21:51:33.196295-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 91
default	21:51:33.196305-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xcb28d6340)
default	21:51:33.196316-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	21:51:33.196327-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:33.196469-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:51:33.196485-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	21:51:33.196491-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:51:33.196605-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:33.196615-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xcb28d6340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:33.196620-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:33.196625-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 7 device listeners from device 85
default	21:51:33.196835-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 85
default	21:51:33.196846-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:33.196856-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	21:51:33.197324-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:51:33.198468-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1154, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.199891-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1154, subject=com.nexy.assistant,
default	21:51:33.200623-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb155b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.219537-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xcb38745d0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	21:51:33.219790-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:51:33.221081-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1155, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.222649-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1155, subject=com.nexy.assistant,
default	21:51:33.223681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.243666-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1156, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.245282-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1156, subject=com.nexy.assistant,
default	21:51:33.246037-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb155b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.264555-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:51:33.264714-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:51:33.266829-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2904 called from <private>
default	21:51:33.266887-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:51:33.266941-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:33.267931-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:33.269651-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48825 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:33.269814-0500	runningboardd	Assertion 394-328-48825 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:51:33.268119-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:33.268136-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2904 called from <private>
default	21:51:33.270658-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:33.270740-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:33.270803-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:33.271028-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:33.268142-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2904 called from <private>
default	21:51:33.276505-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:33.277064-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:33.268393-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:33.268568-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:33.268620-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:33.283730-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:33.283761-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:33.283771-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:33.283777-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2904 called from <private>
default	21:51:33.283781-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:33.283832-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2904 called from <private>
default	21:51:33.283925-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2904 called from <private>
default	21:51:33.283962-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2904 called from <private>
default	21:51:33.283998-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2904 called from <private>
default	21:51:33.284034-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2904 called from <private>
default	21:51:33.287208-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	21:51:33.287959-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:51:33.288132-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ea041, Nexy(47861), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:51:33.288376-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:33.289000-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:33.289138-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:33.289283-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	21:51:33.289324-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea041, Nexy(47861), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 65 starting recording
default	21:51:33.284066-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2904 called from <private>
default	21:51:33.289743-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:33.289871-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:51:33.284104-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2904 called from <private>
default	21:51:33.285926-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2904 called from <private>
default	21:51:33.286036-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:33.286556-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2904 called from <private>
default	21:51:33.287154-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2904 called from <private>
default	21:51:33.290065-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:33.289887-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea041, Nexy(47861), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	21:51:33.294332-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1157, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.296278-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:51:33.290252-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	21:51:33.290306-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:51:33.292046-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:51:33.296910-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:33.296926-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:33.300004-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:33.300057-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:33.300156-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:33.304354-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:33.304586-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:33.304622-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:33.304752-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:33.309609-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:33.310040-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:33.310192-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:33.310291-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:33.310389-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:33.310446-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:33.310620-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:33.310758-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:33.310848-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:33.311387-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:33.311674-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:33.311851-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:33.312064-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:33.312283-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:33.312377-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:33.312521-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:33.316498-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:33.316781-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:33.316948-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:33.317153-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:33.317421-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:33.329027-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:51:33.330466-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.330606-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.330718-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:51:33.330785-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.336726-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1157, subject=com.nexy.assistant,
default	21:51:33.353223-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:33.353332-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:33.353496-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.353702-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.354165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.354182-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.354219-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.370356-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:51:33.370518-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:51:33.372471-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2904 called from <private>
default	21:51:33.373497-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:33.373873-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48830 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
error	21:51:33.373527-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	21:51:33.373539-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2904 called from <private>
default	21:51:33.373634-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:33.373648-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2904 called from <private>
default	21:51:33.373655-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2904 called from <private>
default	21:51:33.373954-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:33.374028-0500	runningboardd	Assertion 394-328-48830 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:51:33.374377-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:33.374676-0500	runningboardd	Invalidating assertion 394-328-48830 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) from originator [osservice<com.apple.powerd>:328]
default	21:51:33.374747-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:33.378818-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1158, subject=com.nexy.assistant,
default	21:51:33.380270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb155b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.381275-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:33.381350-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:33.382515-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:33.382543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.382574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.382810-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.382858-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.382905-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.383034-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.402174-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:51:33.404798-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2904.2663.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:51:33.404860-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2904.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:51:33.473247-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:51:33.474795-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48831 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:33.474910-0500	runningboardd	Assertion 394-328-48831 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:51:33.475157-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2904 called from <private>
default	21:51:33.475248-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2904 called from <private>
default	21:51:33.476572-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:33.476861-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:33.476876-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:33.476887-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:33.476936-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:33.476711-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:33.476732-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2904 called from <private>
default	21:51:33.476738-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2904 called from <private>
default	21:51:33.476743-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:33.477550-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:51:33.477739-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:51:33.478425-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:33.478657-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2904 called from <private>
default	21:51:33.478669-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2904 called from <private>
default	21:51:33.478683-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2904 called from <private>
default	21:51:33.480488-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1159, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:51:33.482067-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1159, subject=com.nexy.assistant,
default	21:51:33.482322-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:51:33.482677-0500	runningboardd	Invalidating assertion 394-328-48831 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) from originator [osservice<com.apple.powerd>:328]
default	21:51:33.483042-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289b00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.483105-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:51:33.486088-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:33.486172-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:33.486227-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.486361-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.486939-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.486953-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.486967-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.486975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.486984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.486991-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.487092-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:33.506004-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2904 called from <private>
default	21:51:33.506247-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:47861] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48832 target:47861 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:33.506356-0500	runningboardd	Assertion 394-328-48832 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) will be created as active
default	21:51:33.514569-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:33.514657-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:51:33.514718-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.515221-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515249-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.515259-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.515275-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.515294-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515312-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.515402-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.515412-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.515419-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.515863-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:33.519216-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.519232-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.519248-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.519256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.519263-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.519268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.519403-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:51:33.646327-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:51:33.646739-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:51:33.646852-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:33.646908-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:51:33.646938-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:33.646981-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea041, Nexy(47861), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 65 stopping recording
default	21:51:33.647001-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:51:33.647006-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:51:33.647037-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:33.647075-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:33.647221-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:51:33.647238-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:51:33.647334-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:51:33.647552-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:51:33.647639-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:51:33.647699-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:51:33.647727-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:51:33.647741-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.648910-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.649127-0500	runningboardd	Invalidating assertion 394-328-48832 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:47861]) from originator [osservice<com.apple.powerd>:328]
default	21:51:33.648931-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	21:51:33.647595-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:51:33.650602-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:51:33.653064-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.653076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.653090-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.653096-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:33.653105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:33.653110-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:33.653212-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:33.748075-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xcb28d6340) Selecting device 0 from destructor
default	21:51:33.748090-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xcb28d6340)
default	21:51:33.748097-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xcb28d6340) not already running
default	21:51:33.748104-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xcb28d6340) disconnecting device 91
default	21:51:33.748111-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xcb28d6340) destroying ioproc 0xb for device 91
default	21:51:33.748152-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:51:33.748188-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:51:33.748352-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xcb28d6340) nothing to setup
default	21:51:33.748366-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device listeners to device 0
default	21:51:33.748373-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xcb28d6340) adding 0 device delegate listeners to device 0
default	21:51:33.748393-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 7 device listeners from device 91
default	21:51:33.748610-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xcb28d6340) removing 0 device delegate listeners from device 91
default	21:51:33.748625-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xcb28d6340)
default	21:51:33.755815-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring jetsam update because this process is not memory-managed
default	21:51:33.755826-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring suspend because this process is not lifecycle managed
default	21:51:33.755841-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring GPU update because this process is not GPU managed
default	21:51:33.755903-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] Ignoring memory limit update because this process is not memory-managed
default	21:51:33.756167-0500	Nexy	[0xcb063d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:51:33.757416-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:51:33.759313-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:51:33.759845-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.3, subject=com.nexy.assistant,
default	21:51:33.760109-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:51:33.761342-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110ad00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:33.782187-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[47861], responsiblePID[47861], responsiblePath: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app to UID: 501
default	21:51:33.782525-0500	Nexy	[0xcb063d540] invalidated after the last release of the connection object
default	21:51:33.975735-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1b0a400 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:34.004745-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1b0ad00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:34.010660-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:51:36.129211-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2904)
default	21:51:36.129291-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2904 called from <private>
default	21:51:36.129308-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2904 called from <private>
default	21:51:36.134716-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.134759-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:36.134767-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:36.138982-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:36.139003-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:36.139177-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.139199-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:36.139517-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:36.143420-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.143477-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.143496-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:36.143922-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:36.144490-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:36.144768-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:36.145330-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2904)
default	21:51:36.145929-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.146253-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2904 called from <private>
default	21:51:36.146470-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2904 called from <private>
default	21:51:36.147903-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:36.148050-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:36.148307-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:36.148415-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:36.149245-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:36.149302-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:36.162236-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2903 called from <private>
default	21:51:36.162271-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2903 called from <private>
default	21:51:36.162381-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.170075-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.170711-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2903 called from <private>
default	21:51:36.170727-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2903 called from <private>
default	21:51:36.170842-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.175044-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.175604-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:36.175617-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:36.175658-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:36.175736-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:36.175899-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:36.176075-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:36.176163-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2903 called from <private>
default	21:51:36.176224-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2903 called from <private>
default	21:51:36.176275-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2903 called from <private>
default	21:51:36.176309-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2903 called from <private>
default	21:51:36.179442-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.179563-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:36.179562-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.179822-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:36.180342-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:36.180644-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:36.183655-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.183691-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2903)
default	21:51:36.183701-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:36.183742-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
default	21:51:36.183764-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2903 called from <private>
default	21:51:36.183777-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2903 called from <private>
default	21:51:36.185338-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2903)
default	21:51:36.185390-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2903 called from <private>
default	21:51:36.185399-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2903 called from <private>
error	21:51:38.692671-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	21:51:38.695748-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	21:51:38.818284-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:51:42.908085-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b6700 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:42.937927-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:42.951455-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:51:43.328255-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:51:43.328798-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:51:44.218969-0500	kernel	Sandbox: ScreenTimeAgent(48154) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:45.331470-0500	ScreenTimeAgent	Looking up cloud object (app) matching ID: app:com.nexy.assistant-uds:12142191747:E03D2455-8EF1-5270-AA03-13B5771C7CB2
default	21:51:45.331490-0500	ScreenTimeAgent	Corresponding cloud object (app) now being created: app:com.nexy.assistant-uds:12142191747:E03D2455-8EF1-5270-AA03-13B5771C7CB2
default	21:51:45.332427-0500	ScreenTimeAgent	Mirroring change: Updated cloud object (STInstalledApp) app:com.nexy.assistant-uds:12142191747:E03D2455-8EF1-5270-AA03-13B5771C7CB2
default	21:51:48.795125-0500	Nexy	[0xcb063d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:51:48.797221-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:51:48.800529-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.4, subject=com.nexy.assistant,
default	21:51:48.802436-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b6100 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:48.829827-0500	Nexy	[0xcb063d540] invalidated after the last release of the connection object
default	21:51:48.832850-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	21:51:48.835895-0500	Nexy	[0xcb063d540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	21:51:48.836086-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	21:51:48.836724-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:51:48.846391-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:51:48.846419-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:51:48.847601-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.2, subject=com.nexy.assistant,
default	21:51:48.848407-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1109500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:51:48.871813-0500	kernel	Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:48.879647-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1554, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:51:48.879690-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:51:48.880754-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1554, subject=com.nexy.assistant,
default	21:51:48.881495-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b6100 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:51:48.903081-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	21:51:48.912034-0500	kernel	udp connect: [<IPv4-redacted>:57945<-><IPv4-redacted>:80] interface:  (skipped: 0)
so_gencnt: 1063154 so_state: 0x0102 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xbb93669c
default	21:51:48.912132-0500	kernel	udp_connection_summary [<IPv4-redacted>:57945<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1063154 so_state: 0x0102 process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xbb93669c flowctl: 0us (0x)
default	21:51:48.913177-0500	Nexy	nw_path_libinfo_path_check [75EC24A0-A471-4C92-8E6C-BA6590BC028A IPv4#4e6fe95d:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:51:48.915107-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6E3FE4A0-49E6-44E1-98A3-DFB424EE1712 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51264,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc57b78e5 tp_proto=0x06"
default	21:51:48.915133-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51264<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063155 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb24391d8
default	21:51:48.970324-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:48.970541-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:51:48.970632-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:51:48.976902-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:48.976927-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:48.976958-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:48.976967-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:51:48.976974-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:51:48.976984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:51:48.977333-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:51:49.916260-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51264<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063155 t_state: SYN_SENT process: Nexy:47861 Duration: 1.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb24391d8
default	21:51:49.916281-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51264<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063155 t_state: SYN_SENT process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/2 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:51:49.921386-0500	kernel	tcp listen: [<IPv4-redacted>:51265<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063159 t_state: LISTEN process: Nexy:47861 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	21:51:49.921608-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51265<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063159 t_state: LISTEN process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	21:51:49.921619-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51265<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063159 t_state: LISTEN process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:51:54.128010-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:54.128144-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:51:54.651741-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:51:54.651846-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:51:59.034238-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	21:52:04.928538-0500	Nexy	nw_path_libinfo_path_check [E88B52C3-3644-49E6-B3CA-20F4AA5FBA0C IPv4#4e6fe95d:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:52:04.929337-0500	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 11D39FE0-1B0C-4100-B347-20B4A3229D17 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51266,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x9ac99074 tp_proto=0x06"
default	21:52:04.929411-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51266<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063187 t_state: SYN_SENT process: Nexy:47861 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb1c8db75
default	21:52:05.430521-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51266<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063187 t_state: SYN_SENT process: Nexy:47861 Duration: 0.502 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb1c8db75
default	21:52:05.430546-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51266<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063187 t_state: SYN_SENT process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:52:05.499327-0500	Nexy	[0xcb063d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:52:05.500325-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:52:05.502226-0500	Nexy	[0xcb063d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:52:05.503073-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:52:05.503555-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.5, subject=com.nexy.assistant,
default	21:52:05.504954-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.6, subject=com.nexy.assistant,
default	21:52:05.505934-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:05.506213-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28b900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:05.521752-0500	Nexy	[0xcb063d7c0] invalidated after the last release of the connection object
default	21:52:05.521857-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	21:52:05.523751-0500	Nexy	[0xcb063d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:52:05.524183-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:52:05.525407-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.7, subject=com.nexy.assistant,
default	21:52:05.526165-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb156a00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:05.527164-0500	Nexy	[0xcb063d680] invalidated after the last release of the connection object
default	21:52:05.542078-0500	tccd	AUTHREQ_PROMPTING: msgID=47861.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy},
default	21:52:06.962868-0500	Nexy	[0xcb063d7c0] invalidated after the last release of the connection object
default	21:52:06.962249-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    465 = "<TCCDEventSubscriber: token=465, state=Initial, csid=(null)>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.photolibraryd>";
    463 = "<TCCDEventSubscriber: token=463, state=Passed, csid=com.apple.chronod>";
}
default	21:52:06.967176-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
error	21:52:07.023967-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
default	21:52:07.076345-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.12, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
error	21:52:07.093158-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:52:07.093339-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:52:07.107069-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.13, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:52:07.177231-0500	Nexy	[0xcb063d680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	21:52:07.181009-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	21:52:07.181061-0500	Nexy	<private> 0xcb1016f00: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	21:52:07.181085-0500	Nexy	<private> 0xcb1016f00: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	21:52:07.181875-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	21:52:07.196923-0500	Nexy	[0xcb063d900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:52:07.202617-0500	Nexy	[0xcb063d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.202686-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:52:07.202930-0500	Nexy	Will add XPC store with options: <private> <private>
default	21:52:07.206312-0500	Nexy	[0xcb0e6c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.207755-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.736, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.207797-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.209609-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.736, subject=com.nexy.assistant,
default	21:52:07.210509-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.237374-0500	Nexy	[0xcb0e6c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.237518-0500	Nexy	[0xcb0e6c3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.237626-0500	Nexy	[0xcb0e6c500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.239001-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.737, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.239041-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.240798-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.737, subject=com.nexy.assistant,
default	21:52:07.241727-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.268508-0500	Nexy	[0xcb0e6c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.268593-0500	Nexy	[0xcb0e6c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.268673-0500	Nexy	[0xcb0e6c640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.269769-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.738, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.269818-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.271871-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.738, subject=com.nexy.assistant,
default	21:52:07.272938-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.298830-0500	Nexy	[0xcb0e6c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.298902-0500	Nexy	[0xcb0e6c640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.298962-0500	Nexy	[0xcb0e6c780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.303456-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.739, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.303512-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.306099-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.739, subject=com.nexy.assistant,
default	21:52:07.307333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb156a00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.332695-0500	Nexy	[0xcb0e6c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.332804-0500	Nexy	[0xcb0e6c780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.346888-0500	Nexy	Did add XPC store
default	21:52:07.346919-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:52:07.351253-0500	Nexy	0xcb1754680: Using cached account information
default	21:52:07.352477-0500	Nexy	[0xcb16e7750] Session created.
default	21:52:07.352489-0500	Nexy	[0xcb16e7750] Session created with Mach Service: <private>
default	21:52:07.352503-0500	Nexy	[0xcb0e6cdc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	21:52:07.352674-0500	Nexy	[0xcb16e7750] Session activated
default	21:52:07.360765-0500	Nexy	[0xcb0e6cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.360775-0500	Nexy	[0xcb16e7750] Session canceled.
default	21:52:07.360791-0500	Nexy	[0xcb16e7750] Disposing of session
default	21:52:07.361356-0500	Nexy	[0xcb0e6cdc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:52:07.362210-0500	Nexy	[0xcb0e6cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.362251-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	21:52:07.362277-0500	Nexy	Will add XPC store with options: <private> <private>
default	21:52:07.365483-0500	Nexy	[0xcb0e6f840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.366945-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.740, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.367003-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.369044-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.740, subject=com.nexy.assistant,
default	21:52:07.369950-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.400595-0500	Nexy	[0xcb0e6f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.400726-0500	Nexy	[0xcb0e6f840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.400896-0500	Nexy	[0xcb0e6f980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.402379-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.741, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.402442-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.404355-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.741, subject=com.nexy.assistant,
default	21:52:07.406208-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb155e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.436527-0500	Nexy	[0xcb0e6f980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.436738-0500	Nexy	[0xcb0e6f980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.436889-0500	Nexy	[0xcb0e6fac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.438103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.742, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.438141-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.439867-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.742, subject=com.nexy.assistant,
default	21:52:07.440825-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.468024-0500	Nexy	[0xcb0e6fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.468122-0500	Nexy	[0xcb0e6fac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.468206-0500	Nexy	[0xcb0e6fc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.469466-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.743, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.469506-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.471366-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.743, subject=com.nexy.assistant,
default	21:52:07.472368-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.498478-0500	Nexy	[0xcb0e6fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.498569-0500	Nexy	[0xcb0e6fc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.509915-0500	Nexy	Did add XPC store
default	21:52:07.509960-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	21:52:07.510104-0500	Nexy	[0xcb0e6fe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:52:07.510868-0500	Nexy	[0xcb0e6fe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.510890-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:52:07.510905-0500	Nexy	Will add XPC store with options: <private> <private>
default	21:52:07.515732-0500	Nexy	[0xcb0e96940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.517267-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.744, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.517308-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.519386-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.744, subject=com.nexy.assistant,
default	21:52:07.520323-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.550301-0500	Nexy	[0xcb0e96940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.550401-0500	Nexy	[0xcb0e96940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.550488-0500	Nexy	[0xcb0e96a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.551773-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.745, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.551810-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.553569-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.745, subject=com.nexy.assistant,
default	21:52:07.554465-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.580600-0500	Nexy	[0xcb0e96a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.580769-0500	Nexy	[0xcb0e96a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.580867-0500	Nexy	[0xcb0e96bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.582139-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.746, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.582187-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.583959-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.746, subject=com.nexy.assistant,
default	21:52:07.584886-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.611259-0500	Nexy	[0xcb0e96bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.611365-0500	Nexy	[0xcb0e96bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.611438-0500	Nexy	[0xcb0e96d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:52:07.612322-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.747, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.612359-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.614404-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.747, subject=com.nexy.assistant,
default	21:52:07.615432-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb156d00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.651479-0500	Nexy	[0xcb0e96d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.651575-0500	Nexy	[0xcb0e96d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:52:07.653171-0500	Nexy	Did add XPC store
default	21:52:07.653203-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:52:07.693624-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.748, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.693746-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.696510-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.748, subject=com.nexy.assistant,
default	21:52:07.697906-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.729254-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.749, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:52:07.729305-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:07.731287-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.749, subject=com.nexy.assistant,
default	21:52:07.732393-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:07.783483-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	21:52:07.807007-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	21:52:07.807038-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	21:52:07.807084-0500	Nexy	<private> 0xcb1016f00: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	21:52:07.814102-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	21:52:07.814166-0500	Nexy	[0xcb0e6c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.814186-0500	Nexy	[0xcb0e6c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.814193-0500	Nexy	[0xcb0e6c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:07.814201-0500	Nexy	[0xcb0e6c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:10.073359-0500	Nexy	[0xcb0e970c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	21:52:14.360722-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:52:14.361540-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:52:14.363248-0500	node	nw_path_libinfo_path_check [B72D44A9-D567-47D3-ADB4-1BC6E9BA1E1F Hostname#97147f91:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:52:14.487430-0500	node	nw_path_libinfo_path_check [82C72B44-B675-4E8E-BF5C-587F5CC4BFE3 Hostname#32ad235b:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:52:15.307168-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:52:15.307707-0500	node	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:52:15.308725-0500	node	nw_path_libinfo_path_check [0C295446-D812-4BA3-B628-CE9C7DBA8E6B Hostname#db5dda29:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:52:15.379368-0500	node	nw_path_libinfo_path_check [D82A6151-34D9-41BE-BE52-86AF25DDD180 Hostname#93e2ba56:0 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:52:20.662621-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48319.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=48319, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	21:52:20.665106-0500	tccd	AUTHREQ_SUBJECT: msgID=48319.1, subject=com.nexy.assistant,
default	21:52:20.665992-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108f00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:20.682718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1571, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=48319, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:52:20.683788-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1571, subject=com.nexy.assistant,
default	21:52:20.684607-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108f00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:20.730031-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:20.756690-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 67080: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b6860100 02b90f00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	21:52:20.776707-0500	tccd	target_executable_path_URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:20.786701-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb156a00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:20.804061-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	21:52:22.360749-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28aa00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:22.367969-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	21:52:22.367361-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    465 = "<TCCDEventSubscriber: token=465, state=Initial, csid=(null)>";
    466 = "<TCCDEventSubscriber: token=466, state=Passed, csid=com.apple.photolibraryd>";
    463 = "<TCCDEventSubscriber: token=463, state=Passed, csid=com.apple.chronod>";
}
error	21:52:22.414557-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:52:22.441387-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:52:22.498779-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
default	21:52:35.642966-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48381.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=48381, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	21:52:35.645514-0500	tccd	AUTHREQ_SUBJECT: msgID=48381.1, subject=com.nexy.assistant,
default	21:52:35.646398-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b5500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.662292-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1580, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=48381, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:52:35.663276-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1580, subject=com.nexy.assistant,
default	21:52:35.664058-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108f00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.701960-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.731599-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 67080: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b6860100 7fb90f00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	21:52:35.750253-0500	tccd	target_executable_path_URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:52:35.763012-0500	Nexy	[0xcb0e97200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:52:35.763732-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:52:35.764924-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.8, subject=com.nexy.assistant,
default	21:52:35.765743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b5500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.780802-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[47861], responsiblePID[47861], responsiblePath: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app to UID: 501
default	21:52:35.781080-0500	Nexy	[0xcb0e97200] invalidated after the last release of the connection object
default	21:52:35.824280-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.844753-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b6700 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:35.849217-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:52:35.905980-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:52:35.907358-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	21:52:35.908019-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:52:35.952476-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:52:35.952478-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:52:35.952872-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:52:35.952873-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:52:35.954082-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:52:35.954628-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:52:41.056271-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:41.081427-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b10b6700 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:41.093791-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:52:41.259901-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:52:41.260586-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:52:41.262763-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:52:41.263402-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:52:41.305615-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:52:41.305634-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:52:41.305977-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:52:41.305994-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:52:41.307279-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:52:41.307622-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:52:41.531919-0500	Nexy	[0xcb0e97200] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	21:52:41.532618-0500	Nexy	[0xcb0e97200] invalidated after the last release of the connection object
default	21:52:41.532421-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:51240<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1062852 t_state: LAST_ACK process: Nexy:47861 Duration: 78.093 sec Conn_Time: 0.011 sec bytes in/out: 764638/1592 pkts in/out: 149/12 pkt rxmit: 0 ooo pkts: 15 dup bytes in: 0 ACKs delayed: 1 delayed ACKs sent: 0
rtt: 22.281 ms rttvar: 9.875 ms base rtt: 10 ms so_error: 0 svc/tc: 0 flow: 0x88d90c12
default	21:52:41.532444-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51240<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1062852 t_state: LAST_ACK process: Nexy:47861 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:52:41.533603-0500	kernel	udp connect: [<IPv4-redacted>:62684<-><IPv4-redacted>:53] interface:  (skipped: 0)
so_gencnt: 1063463 so_state: 0x0102 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x968a84ba
default	21:52:42.534640-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063517 so_state: 0x0000 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	21:52:42.534676-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063517 so_state: 0x0000 process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	21:52:43.535449-0500	kernel	udp connect: [<IPv4-redacted>:53786<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1063533 so_state: 0x0002 process: Nexy:47861 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb86fef95
default	21:52:43.535486-0500	kernel	udp_connection_summary [<IPv4-redacted>:53786<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1063533 so_state: 0x0002 process: Nexy:47861 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb86fef95 flowctl: 0us (0x)
default	21:52:43.535562-0500	kernel	udp_connection_summary [<IPv4-redacted>:62684<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063463 so_state: 0x0132 process: Nexy:47861 Duration: 2.002 sec Conn_Time: 2.001 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x968a84ba flowctl: 0us (0x)
default	21:52:50.791030-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1601, subject=com.nexy.assistant,
default	21:52:50.828733-0500	Nexy	[0xcb0e97200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:52:50.829740-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:52:50.830894-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.9, subject=com.nexy.assistant,
default	21:52:50.831674-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1b0b000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:50.847851-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[47861], responsiblePID[47861], responsiblePath: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app to UID: 501
default	21:52:50.848145-0500	Nexy	[0xcb0e97200] invalidated after the last release of the connection object
default	21:52:50.873728-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1b0b900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:50.895531-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1b0b600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:52:50.899636-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:52:52.812593-0500	Nexy	[0xcb063d680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:52:52.812629-0500	Nexy	"The connection to ACDAccountStore was invalidated."
default	21:52:55.169874-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	21:52:55.681291-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	21:52:55.700715-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	21:52:56.236326-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	21:52:56.236684-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:52:56.236886-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	21:52:56.325409-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:52:56.325489-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	21:53:01.042006-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11ebc00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:01.065185-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e9e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:01.095705-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:53:01.151731-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:01.152050-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:01.152762-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:53:01.152892-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:01.156550-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:01.156856-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:01.157107-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:53:01.157680-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:01.187923-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:01.188266-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:01.189625-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:53:01.191705-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:01.192001-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:01.193259-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:53:05.981005-0500	Nexy	[0xcb0e97200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	21:53:05.981652-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	21:53:05.981836-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47861.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:05.983566-0500	tccd	AUTHREQ_SUBJECT: msgID=47861.10, subject=com.nexy.assistant,
default	21:53:05.984354-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1109e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:06.003218-0500	Nexy	[0xcb0e97200] invalidated after the last release of the connection object
default	21:53:06.009913-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.15, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:53:06.027796-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.15, subject=com.nexy.assistant,
default	21:53:06.029620-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e9e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:06.055248-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:53:06.056293-0500	kernel	System Policy: Nexy(47861) deny(1) file-read-data /Users/sergiyzasorin/Library/Messages/chat.db
error	21:53:06.108691-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:06.108990-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:06.109235-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
default	21:53:06.109438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e9e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:53:06.109653-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	21:53:06.109839-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:06.110512-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:06.110815-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:06.111315-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	21:53:06.111548-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:53:06.111673-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:06.150918-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:06.151350-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:06.151873-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:06.152384-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:06.153021-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:53:06.154221-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:53:08.124258-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11ebc00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:08.167313-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e9e00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:08.177870-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	21:53:08.352433-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:08.352781-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:08.353312-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	21:53:08.353557-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:53:08.353676-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:08.354809-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:08.355118-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	21:53:08.355392-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	21:53:08.355813-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	21:53:08.356012-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	21:53:08.387105-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:08.387430-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:08.388798-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	21:53:08.393122-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	21:53:08.393449-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	21:53:08.394835-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	21:53:21.144165-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.17, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=47861, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:53:21.146078-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.17, subject=com.nexy.assistant,
default	21:53:21.147345-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11ea100 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:23.224252-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1ea041","name":"Nexy(47861)"}, "details":null }
default	21:53:23.224323-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ea041 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":47861})
default	21:53:23.222147-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x256256 (Nexy) connectionID: E72E3 pid: 47861 in session 0x101
default	21:53:23.224348-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":47861})
default	21:53:23.222176-0500	WindowServer	<BSCompoundAssertion:0x9dac19580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x256256 (Nexy) acq:0x9dcffd280 count:1
default	21:53:23.224833-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:53:23.225131-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 65, PID = 47861, Name = sid:0x1ea041, Nexy(47861), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:53:23.225408-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.225594-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.225663-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.225768-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.226521-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x256256 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x256256 (Nexy)"
)}
default	21:53:23.227790-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xbaf5 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x256256 (Nexy)"
)}
default	21:53:23.233521-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.233654-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:23.238831-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:53:23.239196-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:53:23.243254-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.245064-0500	mDNSResponder	[R80591] DNSServiceCreateConnection STOP PID[47861](Nexy)
default	21:53:23.246319-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:47861] termination reported by launchd (0, 0, 0)
default	21:53:23.246366-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.246545-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.246712-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.246742-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.250834-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: none (role: None) (endowments: (null))
default	21:53:23.250996-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: none (role: None) (endowments: (null))
default	21:53:23.251101-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 47861, name = Nexy
default	21:53:23.251571-0500	launchservicesd	Hit the server for a process handle 1873c7da0000baf5 that resolved to: [app<application.com.nexy.assistant.58107047.58107056(501)>:47861]
default	21:53:23.251596-0500	gamepolicyd	Received state update for 47861 (app<application.com.nexy.assistant.58107047.58107056(501)>, none-NotVisible
default	21:53:23.256162-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x256256} for bundle path: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app with URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:53:23.256187-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae62105a0: Nexy> state 3
default	21:53:23.256200-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	21:53:23.256419-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae62105a0: Nexy> state 4
default	21:53:23.256428-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	21:53:23.263601-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2904.2663.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	21:53:23.263614-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2904.2663.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	21:53:26.362184-0500	logger	launching: /usr/bin/open -a /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:26.452306-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	21:53:26.452486-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	21:53:26.454360-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	21:53:26.460581-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	21:53:26.464900-0500	runningboardd	Launch request for app<application.com.nexy.assistant.58107047.58107056(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	21:53:26.464962-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.58107047.58107056(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:65373] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-65373-49072 target:app<application.com.nexy.assistant.58107047.58107056(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:53:26.465030-0500	runningboardd	Assertion 394-65373-49072 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) will be created as active
default	21:53:26.467494-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	21:53:26.467524-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.58107047.58107056(501)>
default	21:53:26.467535-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	21:53:26.467601-0500	runningboardd	app<application.com.nexy.assistant.58107047.58107056(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	21:53:26.477861-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] is not RunningBoard jetsam managed.
default	21:53:26.477880-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] This process will not be managed.
default	21:53:26.477890-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:26.478028-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:26.478590-0500	gamepolicyd	Hit the server for a process handle 59406ee0000be05 that resolved to: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:26.478626-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:26.480756-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:26.480814-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-49073 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:53:26.480937-0500	runningboardd	Assertion 394-394-49073 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:26.481095-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:26.481110-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:26.481127-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Set darwin role to: UserInteractive
default	21:53:26.481137-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:26.481154-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:26.481204-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] reported to RB as running
default	21:53:26.482492-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:48645" ID:394-357-49074 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:53:26.482566-0500	runningboardd	Assertion 394-357-49074 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:26.482707-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x270270 com.nexy.assistant starting stopped process.
default	21:53:26.483494-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:53:26.483644-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae62105a0: Nexy> state 2
default	21:53:26.483664-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	21:53:26.483675-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:26.483711-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:26.483733-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:26.483777-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:26.483845-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:26.485157-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:26.485389-0500	runningboardd	Invalidating assertion 394-65373-49072 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:65373]
default	21:53:26.485421-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:26.485579-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:26.485467-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:26.485523-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:26.485615-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:26.488337-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:26.492382-0500	logger	verifying new process for /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:53:26.525604-0500	logger	detected new pid 48645 for /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:53:26.578490-0500	Nexy	[0x104e2da10] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	21:53:26.578560-0500	Nexy	[0x104e2df90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	21:53:26.588560-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:26.588576-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:26.588598-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:26.588745-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:26.588651-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:26.595338-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:26.595741-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:26.709961-0500	Nexy	[0x104e34fc0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	21:53:26.710745-0500	Nexy	[0x94c680000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	21:53:26.715153-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48645.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:26.744508-0500	Nexy	[0x94c6803c0] invalidated after the last release of the connection object
default	21:53:26.744852-0500	Nexy	server port 0x00003907, session port 0x00003907
default	21:53:26.748783-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108f00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:26.788717-0500	Nexy	[0x94c6803c0] Connection returned listener port: 0x4d03
default	21:53:26.789237-0500	Nexy	[0x94d6f0000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x94c6803c0.peer[357].0x94d6f0000
default	21:53:26.789695-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:53:26.789841-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	21:53:26.796355-0500	Nexy	[0x94c6803c0] Connection returned listener port: 0x4d03
default	21:53:26.801533-0500	Nexy	No persisted cache on this platform.
default	21:53:26.810647-0500	Nexy	Handshake succeeded
default	21:53:26.810666-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.58107047.58107056(501)>
default	21:53:26.811300-0500	Nexy	[0x94c6803c0] Connection returned listener port: 0x4d03
default	21:53:26.815954-0500	Nexy	[0x94c6803c0] Connection returned listener port: 0x4d03
default	21:53:26.820483-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	21:53:26.820521-0500	Nexy	[0x94c680780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	21:53:26.820668-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	21:53:26.820756-0500	Nexy	[0x94c680a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:53:26.823940-0500	Nexy	Registered process with identifier 48645-1031084
default	21:53:27.969737-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 17225AEF-EEA4-4EBA-8B19-FD2A99589106 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51299,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x2113703a tp_proto=0x06"
default	21:53:27.969841-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51299<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063758 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb789e299
default	21:53:31.493520-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-49073 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645])
default	21:53:31.688648-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:31.688663-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:31.688673-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:31.688685-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:31.691718-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:31.692316-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:32.972454-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51299<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063758 t_state: SYN_SENT process: Nexy:48645 Duration: 5.003 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb789e299
default	21:53:32.972489-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51299<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063758 t_state: SYN_SENT process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:53:32.973886-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D9FA2CB2-8D8F-4150-A333-F493553B30EA flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51304,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5c1cdb98 tp_proto=0x06"
default	21:53:32.974036-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51304<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063800 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb3f4479c
default	21:53:37.179169-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	21:53:37.804701-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	21:53:37.973465-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51304<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063800 t_state: SYN_SENT process: Nexy:48645 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb3f4479c
default	21:53:37.973493-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51304<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063800 t_state: SYN_SENT process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:53:37.982568-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:53:37.982877-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:53:37.984985-0500	Nexy	nw_path_libinfo_path_check [F664FBDA-70A0-41EB-A2C6-7AFF1B369EC6 Hostname#c8477840:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:53:37.985416-0500	mDNSResponder	[R80839] DNSServiceCreateConnection START PID[48645](Nexy)
default	21:53:37.985534-0500	mDNSResponder	[R80840] DNSServiceQueryRecord START -- qname: <mask.hash: 'UScWDXXJU+z4Xf3lW2QKnQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: f92d5498
default	21:53:37.986381-0500	mDNSResponder	[R80841] DNSServiceQueryRecord START -- qname: <mask.hash: 'UScWDXXJU+z4Xf3lW2QKnQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: f92d5498
default	21:53:38.000714-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2F371022-D7A6-4D05-B7B8-083A0EBB4F92 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51310,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd1c691dc tp_proto=0x06"
default	21:53:38.000871-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51310<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063868 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x931f50f6
default	21:53:42.974541-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:51310<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063868 t_state: SYN_SENT process: Nexy:48645 Duration: 4.974 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x931f50f6
default	21:53:42.974560-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51310<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063868 t_state: SYN_SENT process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:53:44.054538-0500	Nexy	[0x94c680dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:53:44.055362-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48645.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:44.056969-0500	tccd	AUTHREQ_SUBJECT: msgID=48645.2, subject=com.nexy.assistant,
default	21:53:44.057740-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:44.078773-0500	Nexy	[0x94c680dc0] invalidated after the last release of the connection object
default	21:53:44.079097-0500	Nexy	server port 0x00002913, session port 0x00003907
default	21:53:44.080020-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1637, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:53:44.080056-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:53:44.080929-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1637, subject=com.nexy.assistant,
default	21:53:44.081599-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:44.112386-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	21:53:44.113831-0500	Nexy	[0x94c681040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	21:53:44.114924-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"PID":48645,"session_type":"Primary"} }
default	21:53:44.115010-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":48645}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea042, sessionType: 'prim', isRecording: false }, 
]
default	21:53:44.115825-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 48645, name = Nexy
default	21:53:44.116173-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x94d758480 with ID: 0x1ea042
default	21:53:44.116991-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	21:53:44.118881-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	21:53:44.124699-0500	Nexy	[0x94c681180] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	21:53:44.127589-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
default	21:53:44.132093-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	21:53:44.133688-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:53:44.133842-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:53:44.133968-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	21:53:44.133977-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	21:53:44.134365-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:53:44.134500-0500	Nexy	[0x94c6812c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:53:44.134747-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	21:53:44.135076-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48645.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:44.143053-0500	tccd	AUTHREQ_SUBJECT: msgID=48645.3, subject=com.nexy.assistant,
default	21:53:44.143934-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:44.160516-0500	Nexy	[0x94c6812c0] invalidated after the last release of the connection object
default	21:53:44.160653-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:53:44.160693-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:53:44.160923-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	21:53:44.162003-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1163, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:53:44.163043-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1163, subject=com.nexy.assistant,
default	21:53:44.163671-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28ad00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:53:44.179972-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	21:53:44.180866-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1165, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:53:44.181844-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1165, subject=com.nexy.assistant,
default	21:53:44.182441-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb156a00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:44.196562-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	21:53:44.196576-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x94f366900> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	21:53:44.211283-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	21:53:44.211294-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	21:53:44.211770-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	21:53:44.215003-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:53:44.215128-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:53:44.219377-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:53:44.221054-0500	Nexy	[0x94c6812c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	21:53:44.221374-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=208928684113921 }
default	21:53:44.221589-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	21:53:44.221625-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	21:53:44.221656-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	21:53:44.233148-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:53:44.233277-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:53:44.237485-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 123
default	21:53:44.249757-0500	Nexy	[0x94c681400] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	21:53:44.250142-0500	Nexy	[0x94c681400] invalidated after the last release of the connection object
default	21:53:44.250585-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayAndRecord, requires reconfiguration?: NO
default	21:53:44.250627-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	21:53:44.250770-0500	kernel	udp connect: [<IPv4-redacted>:55447<-><IPv4-redacted>:53] interface:  (skipped: 0)
so_gencnt: 1063971 so_state: 0x0102 process: Nexy:48645 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9790aeca
default	21:53:44.258618-0500	Nexy	[0x94c681400] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	21:53:44.271301-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063972 so_state: 0x0000 process: Nexy:48645 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	21:53:44.271311-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 1063972 so_state: 0x0000 process: Nexy:48645 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	21:53:44.273929-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x94f3d9540) Selecting device 85 from constructor
default	21:53:44.273938-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f3d9540)
default	21:53:44.273945-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f3d9540) not already running
default	21:53:44.273951-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x94f3d9540) nothing to teardown
default	21:53:44.273957-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x94f3d9540) connecting device 85
default	21:53:44.274034-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f3d9540) Device ID: 85 (Input:No | Output:Yes): true
default	21:53:44.274107-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x94f3d9540) created ioproc 0xa for device 85
default	21:53:44.274198-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f3d9540) adding 7 device listeners to device 85
default	21:53:44.274348-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f3d9540) adding 0 device delegate listeners to device 85
default	21:53:44.274355-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f3d9540)
default	21:53:44.274418-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.274426-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:53:44.274431-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.274437-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:53:44.274445-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:53:44.274523-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:53:44.274532-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:53:44.274535-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:53:44.274539-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f3d9540) removing 0 device listeners from device 0
default	21:53:44.274544-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f3d9540) removing 0 device delegate listeners from device 0
default	21:53:44.274548-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f3d9540)
default	21:53:44.274641-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:53:44.274904-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.275990-0500	kernel	udp connect: [<IPv4-redacted>:50864<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1063973 so_state: 0x0002 process: Nexy:48645 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8840cf23
default	21:53:44.276005-0500	kernel	udp_connection_summary [<IPv4-redacted>:50864<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 1063973 so_state: 0x0002 process: Nexy:48645 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8840cf23 flowctl: 0us (0x)
default	21:53:44.276032-0500	kernel	udp_connection_summary [<IPv4-redacted>:55447<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063971 so_state: 0x0132 process: Nexy:48645 Duration: 0.025 sec Conn_Time: 0.025 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9790aeca flowctl: 0us (0x)
default	21:53:44.276020-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	21:53:44.276065-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	21:53:44.276305-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F609BEF7-9C83-4D85-B593-B4EB1F63A5A8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51322,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xe3a5a006 tp_proto=0x06"
default	21:53:44.276346-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51322<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1063974 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa457829e
default	21:53:44.276386-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94f47b930, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.276410-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.278007-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.278217-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.282077-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.282275-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.283731-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94f479290, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.283745-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.284040-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.284570-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94f47bc90, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.284580-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94f47bc90: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:44.284584-0500	Nexy	AudioConverter -> 0x94f47bc90: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:53:44.284586-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.284590-0500	Nexy	AudioConverter -> 0x94f47bc90: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:53:44.284596-0500	Nexy	AudioConverter -> 0x94f47bc90: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:53:44.285399-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94f479290, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:53:44.285408-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94f479290: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:44.285410-0500	Nexy	AudioConverter -> 0x94f479290: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:53:44.285413-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:53:44.285418-0500	Nexy	AudioConverter -> 0x94f479290: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:53:44.285422-0500	Nexy	AudioConverter -> 0x94f479290: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:53:44.285548-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94f479290: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:44.287120-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid CA88286C-46F5-472C-A140-29D9EE53EB93 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51323,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x20b7d223 tp_proto=0x06"
default	21:53:44.287152-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51323<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063975 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa4baf598
default	21:53:44.287362-0500	Nexy	nw_path_libinfo_path_check [C759B2FD-0831-435B-A5B0-D7DDB75898F3 Hostname#3438e56c:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:53:44.287446-0500	mDNSResponder	[R80860] DNSServiceQueryRecord START -- qname: <mask.hash: 'zM6NfbtezcK6l1UgxpL4AQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: 2d50b096
default	21:53:44.287817-0500	mDNSResponder	[R80861] DNSServiceQueryRecord START -- qname: <mask.hash: 'zM6NfbtezcK6l1UgxpL4AQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: 2d50b096
default	21:53:44.288985-0500	kernel	tcp connected: [<IPv4-redacted>:51322<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1063974 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa457829e
default	21:53:44.340325-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6A4FE0DA-22A9-4FB9-BE86-B8FD32FAD9A1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51324,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xf27e625c tp_proto=0x06"
default	21:53:44.340357-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51324<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1063985 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xae43fc6d
default	21:53:44.356405-0500	kernel	tcp connected: [<IPv4-redacted>:51324<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1063985 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xae43fc6d
default	21:53:44.413620-0500	spindump	Nexy [48645]: spin: not sampling due to conditions 0x400000000
default	21:53:45.407660-0500	Nexy	[0x94c681900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	21:53:45.426403-0500	usernoted	Connection com.nexy.assistant with path: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:45.437396-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 48645
default	21:53:45.449980-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x94c5606e0
 (
    "<NSDarkAquaAppearance: 0x94c560640>",
    "<NSSystemAppearance: 0x94c560780>"
)>
default	21:53:45.455665-0500	Nexy	[0x94c681e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	21:53:45.457583-0500	Nexy	[0x94c681f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	21:53:45.460910-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	21:53:45.461447-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	21:53:45.461456-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	21:53:45.461481-0500	Nexy	[0x94c682080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	21:53:45.461822-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	21:53:45.461894-0500	Nexy	[0x94c6821c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:53:45.461961-0500	Nexy	FBSWorkspace registering source: <private>
default	21:53:45.462614-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	21:53:45.464206-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	21:53:45.464291-0500	Nexy	<FBSWorkspaceScenesClient:0x94c563160 <private>> attempting immediate handshake from activate
default	21:53:45.464545-0500	Nexy	<FBSWorkspaceScenesClient:0x94c563160 <private>> sent handshake
default	21:53:45.464795-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	21:53:45.465527-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.465857-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.465820-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	21:53:45.466312-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Registering event dispatcher at init
default	21:53:45.467075-0500	ControlCenter	Created <FBWorkspace: 0x7569e5680; <FBApplicationProcess: 0x752d5b180; app<application.com.nexy.assistant.58107047.58107056>:48645(vFBBAC)>>
default	21:53:45.467096-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.58107047.58107056> with intent background
default	21:53:45.467197-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	21:53:45.467784-0500	runningboardd	Launch request for app<application.com.nexy.assistant.58107047.58107056(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	21:53:45.467935-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.58107047.58107056(501)> from originator [osservice<com.apple.controlcenter(501)>:627] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-627-49104 target:app<application.com.nexy.assistant.58107047.58107056(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	21:53:45.468099-0500	runningboardd	Assertion 394-627-49104 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) will be created as active
default	21:53:45.468133-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-627-49104 target:app<application.com.nexy.assistant.58107047.58107056(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.468482-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:45.468494-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:45.468688-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	21:53:45.468503-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:45.468893-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:45.469703-0500	Nexy	Requesting scene <FBSScene: 0x94c563520; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2> from com.apple.controlcenter.statusitems
default	21:53:45.471498-0500	Nexy	Request for <FBSScene: 0x94c563520; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2> complete!
default	21:53:45.471594-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	21:53:45.471905-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:45.472970-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:45.473318-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	21:53:45.473562-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	21:53:45.473797-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	21:53:45.473834-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	21:53:45.474118-0500	Nexy	Requesting scene <FBSScene: 0x94c5635c0; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	21:53:45.474320-0500	Nexy	Request for <FBSScene: 0x94c5635c0; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView> complete!
default	21:53:45.475583-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Bootstrap success!
default	21:53:45.476171-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Setting process visibility to: Background
default	21:53:45.476221-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.476241-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	21:53:45.476264-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] No launch watchdog for this process, dropping initial assertion in 2.0s
default	21:53:45.476702-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.controlcenter(501)>:627] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-627-49105 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	21:53:45.476783-0500	runningboardd	Assertion 394-627-49105 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:45.477149-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:45.477163-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:45.477174-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:45.477202-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:45.479796-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:45.480230-0500	ControlCenter	Adding: <FBApplicationProcess: 0x752d5b180; app<application.com.nexy.assistant.58107047.58107056>:48645(vFBBAC)>
default	21:53:45.480489-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:45.480730-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Connection established.
default	21:53:45.480803-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:45.480845-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x7588ee370>
default	21:53:45.480871-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Connection to remote process established!
default	21:53:45.481164-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.481187-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	21:53:45.481287-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	21:53:45.489089-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.489120-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x752d5b180; app<application.com.nexy.assistant.58107047.58107056>:48645(vFBBAC)>
default	21:53:45.489317-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Registered new scene: <FBWorkspaceScene: 0x758e721c0; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2> (fromRemnant = 0)
default	21:53:45.489365-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Workspace interruption policy did change: reconnect
default	21:53:45.489809-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.controlcenter(501)>:627] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-627-49106 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	21:53:45.489918-0500	runningboardd	Assertion 394-627-49106 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as inactive as originator process has not exited
default	21:53:45.490108-0500	ControlCenter	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Client process connected: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.490122-0500	Nexy	Request for <FBSScene: 0x94c563520; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2> complete!
default	21:53:45.490489-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.controlcenter(501)>:627] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-627-49107 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	21:53:45.490585-0500	runningboardd	Assertion 394-627-49107 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:45.490660-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	21:53:45.490911-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:45.490927-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.490928-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:45.490947-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x752d5b180; app<application.com.nexy.assistant.58107047.58107056>:48645(vFBBAC)>
default	21:53:45.490943-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:45.491013-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Registered new scene: <FBWorkspaceScene: 0x758e70180; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	21:53:45.490974-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:45.491298-0500	ControlCenter	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:53:45.491401-0500	Nexy	<FBSWorkspaceScenesClient:0x94c563160 <private>> Reconnecting scene com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2
default	21:53:45.491730-0500	Nexy	<FBSWorkspaceScenesClient:0x94c563160 <private>> Reconnecting scene com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView
default	21:53:45.491873-0500	Nexy	Request for <FBSScene: 0x94c5635c0; com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView> complete!
default	21:53:45.494174-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:45.494707-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:45.494946-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:45.521724-0500	Nexy	Registering for test daemon availability notify post.
default	21:53:45.521931-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	21:53:45.522056-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	21:53:45.522154-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	21:53:45.526103-0500	Nexy	[0x94c682580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	21:53:45.537587-0500	Nexy	[0x94c6803c0] Connection returned listener port: 0x4d03
default	21:53:45.538203-0500	Nexy	SignalReady: pid=48645 asn=0x0-0x270270
default	21:53:45.538779-0500	Nexy	SIGNAL: pid=48645 asn=0x0x-0x270270
default	21:53:45.539074-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108f00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:45.539815-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/
default	21:53:45.551683-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.554667-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.556592-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:53:45.556601-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	21:53:45.556629-0500	Nexy	[0x94c681540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	21:53:45.556732-0500	Nexy	[0x94c681540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:53:45.560432-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:53:45.563219-0500	Nexy	[C:2] Alloc <private>
default	21:53:45.563258-0500	Nexy	[0x94c681540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:53:45.565073-0500	Nexy	[0x94c682800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:53:45.565082-0500	WindowManager	Connection activated | (48645) Nexy
default	21:53:45.565797-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-48645). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
error	21:53:45.565818-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	21:53:45.565913-0500	Nexy	[0x94c682800] invalidated after the last release of the connection object
default	21:53:45.567646-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-48645)
default	21:53:45.568284-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(F01FBFEF, (bid:com.nexy.assistant-Item-0-48645)) for (bid:com.nexy.assistant-Item-0-48645)
default	21:53:45.569258-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	21:53:45.569308-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-48645)]
default	21:53:45.570146-0500	ControlCenter	Created instance DisplayableId(D56FAC6D) in .menuBar for DisplayableAppStatusItemType(F01FBFEF, (bid:com.nexy.assistant-Item-0-48645)) .menuBar
default	21:53:45.574039-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.574960-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.577637-0500	ControlCenter	Created ephemaral instance DisplayableId(D56FAC6D) for (bid:com.nexy.assistant-Item-0-48645) with positioning .ephemeral
default	21:53:45.583669-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	21:53:45.585196-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.929538-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.930490-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:53:45.962265-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	21:53:45.969929-0500	Nexy	Start service name com.apple.spotlightknowledged
default	21:53:45.970890-0500	Nexy	[GMS] availability notification token 98
default	21:53:46.037650-0500	ControlCenter	[app<application.com.nexy.assistant.58107047.58107056>:48645] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	21:53:46.037751-0500	runningboardd	Invalidating assertion 394-627-49107 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.controlcenter(501)>:627]
default	21:53:46.058232-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-49108 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:53:46.058337-0500	runningboardd	Assertion 394-387-49108 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:46.058649-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:46.058660-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:46.058670-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:46.058687-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:46.061224-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:46.061635-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:46.061770-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:46.138598-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:46.138612-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:46.138622-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:46.138642-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:46.143868-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:46.163405-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:46.163638-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:47.571628-0500	runningboardd	Invalidating assertion 394-627-49104 (target:app<application.com.nexy.assistant.58107047.58107056(501)>) from originator [osservice<com.apple.controlcenter(501)>:627]
default	21:53:47.674474-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.58107047.58107056(501)>
default	21:53:47.675371-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:47.675393-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:47.675412-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:47.675448-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:47.679980-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:47.687844-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:47.688163-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:50.439960-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	21:53:52.761331-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:53:52.809899-0500	Nexy	[0x94c682a80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:53:52.811111-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48645.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:52.813026-0500	tccd	AUTHREQ_SUBJECT: msgID=48645.5, subject=com.nexy.assistant,
default	21:53:52.815011-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:52.838207-0500	Nexy	[0x94c682a80] invalidated after the last release of the connection object
default	21:53:52.838490-0500	Nexy	[0x94c682bc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:53:52.839040-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48645.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, },
default	21:53:52.840018-0500	tccd	AUTHREQ_SUBJECT: msgID=48645.6, subject=com.nexy.assistant,
default	21:53:52.840717-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:52.858917-0500	Nexy	[0x94c682bc0] invalidated after the last release of the connection object
default	21:53:52.858994-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:53:52.859637-0500	Nexy	[0x94c682bc0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	21:53:52.859796-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	21:53:52.859930-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:53:52.863082-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:53:52.863109-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:53:52.864077-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.3, subject=com.nexy.assistant,
default	21:53:52.864787-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:53:52.884952-0500	kernel	Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:52.891033-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1639, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:53:52.891062-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:53:52.891958-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1639, subject=com.nexy.assistant,
default	21:53:52.892647-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108000 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:52.940988-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	21:53:52.961338-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
fault	21:53:52.966895-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.58107047.58107056 AUID=501> and <type=Application identifier=application.com.nexy.assistant.58107047.58107056>
default	21:53:52.993088-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:53:52.993248-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:53:52.993309-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:53:53.346400-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94f479290: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:53.346506-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94f479290: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:53.346656-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x94c6d8650: start, was running 0
default	21:53:53.347505-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49109 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:53:53.347611-0500	runningboardd	Assertion 394-48645-49109 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:53.350795-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:53.350806-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:53.350816-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:53.350878-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:53.351098-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49110 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:53:53.351160-0500	runningboardd	Assertion 394-328-49110 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:53:53.353741-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:53.354047-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:53:53.354067-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:53:53.354084-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:53:53.354159-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:53:53.354329-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:53.354707-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:53.356774-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:53:53.357270-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:53.357363-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:53:53.396234-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:53:53.397685-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:53:53.397876-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:53:53.397957-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:53:53.398077-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:53:53.398085-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:53:53.398102-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 66 starting playing
default	21:53:53.398145-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398240-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:53:53.398279-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:53:53.398313-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:53:53.398334-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398380-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398372-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:53:53.398550-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:53:53.398415-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea042 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":48645}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea042, sessionType: 'prim', isRecording: false }, 
]
default	21:53:53.398562-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:53:53.398576-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:53:53.398792-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398861-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398885-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:53:53.398895-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	21:53:53.398909-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	21:53:53.399070-0500	kernel	3 duplicate reports for Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:53:56.429148-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	21:53:59.300764-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:53:59.706907-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:53:59.707093-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:00.017282-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:00.018167-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x94f391540) Selecting device 85 from constructor
default	21:54:00.018178-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:00.018186-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:00.018191-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x94f391540) nothing to teardown
default	21:54:00.018194-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x94f391540) connecting device 85
default	21:54:00.018276-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f391540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:00.018554-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x94f391540) created ioproc 0xb for device 85
default	21:54:00.018826-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 7 device listeners to device 85
default	21:54:00.019005-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 85
default	21:54:00.019015-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f391540)
default	21:54:00.019125-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:00.019134-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:00.019143-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:00.019150-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:00.019165-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:00.019269-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:00.019280-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:00.019288-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:00.019293-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device listeners from device 0
default	21:54:00.019298-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 0
default	21:54:00.019303-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:00.019318-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:54:00.019367-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x94f391540) caller requesting device change from 85 to 91
default	21:54:00.019375-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:00.019380-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:00.019383-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x94f391540) disconnecting device 85
default	21:54:00.019388-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x94f391540) destroying ioproc 0xb for device 85
default	21:54:00.019409-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:00.019632-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:00.020004-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x94f391540) connecting device 91
default	21:54:00.020085-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f391540) Device ID: 91 (Input:Yes | Output:No): true
default	21:54:00.021823-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1166, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.023597-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1166, subject=com.nexy.assistant,
default	21:54:00.023772-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:00.023802-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:54:00.024743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.025433-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:00.025464-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:00.026777-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.4, subject=com.nexy.assistant,
default	21:54:00.027643-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.044778-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x94f391540) created ioproc 0xa for device 91
default	21:54:00.044886-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 7 device listeners to device 91
default	21:54:00.045046-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 91
default	21:54:00.045053-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f391540)
default	21:54:00.045061-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	21:54:00.045069-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:00.045175-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:54:00.045181-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	21:54:00.045187-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:54:00.045263-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:00.045269-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:00.045274-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:00.045278-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 7 device listeners from device 85
default	21:54:00.045411-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 85
default	21:54:00.045418-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:00.045929-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:00.046843-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1167, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.047928-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1167, subject=com.nexy.assistant,
error	21:54:00.048486-0500	kernel	Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.048607-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289200 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.061660-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:00.061687-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:54:00.071367-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:00.072330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:00.072357-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:00.073304-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.5, subject=com.nexy.assistant,
default	21:54:00.074024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.074269-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:00.075242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1168, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.076266-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1168, subject=com.nexy.assistant,
default	21:54:00.076872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.100889-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1169, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.102044-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1169, subject=com.nexy.assistant,
default	21:54:00.102806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28bc00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.123498-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:00.124376-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:54:00.124510-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:54:00.125226-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:54:00.127252-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:00.127311-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:00.226654-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:54:00.228046-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:54:00.228645-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:00.228859-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:00.229109-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.229127-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:00.229373-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:00.229753-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:00.229773-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:00.229782-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:00.231079-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:00.231105-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:00.231465-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:00.231487-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:00.231518-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:00.232773-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:00.234967-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:00.231281-0500	runningboardd	Invalidating assertion 394-48645-49109 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:00.236932-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:00.236951-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:00.236946-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:00.236962-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:00.236972-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:00.236979-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:00.236983-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:00.236990-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:00.237045-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:00.237380-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:00.237423-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:00.237493-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:00.232660-0500	runningboardd	Invalidating assertion 394-328-49110 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:00.239084-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49111 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:00.239147-0500	runningboardd	Assertion 394-48645-49111 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:00.237557-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:00.237623-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:00.237714-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:00.237776-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:00.243268-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:00.243278-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:00.243419-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.243499-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:00.243563-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:00.247488-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:00.247735-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:00.247848-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:00.247955-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:00.248081-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:00.253277-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1170, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.248646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:00.248697-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:00.248850-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.248917-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:00.248996-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:00.252202-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:00.254547-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:00.255013-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.255182-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:00.255392-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:00.255513-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:00.255572-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:00.255644-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:00.255791-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:00.255916-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.259552-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:00.259576-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
error	21:54:00.259731-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:00.259742-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:00.259748-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:00.259754-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:00.259759-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:00.261734-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:00.261743-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:00.261862-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
error	21:54:00.262177-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:00.262187-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:00.262192-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:00.262198-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:00.263489-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:00.263883-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1170, subject=com.nexy.assistant,
default	21:54:00.264291-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:00.265002-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:00.265022-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:00.265033-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:00.265043-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:00.265091-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:00.265445-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:00.265456-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:00.265480-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:00.265487-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:00.265496-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:00.265501-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:00.265506-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:00.265531-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:00.265605-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:00.265661-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:00.265733-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:00.265800-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:00.265872-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:00.265913-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:00.265948-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:00.266525-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:00.265980-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:00.266391-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.272241-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:00.272254-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:00.272356-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:00.272660-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94d6df990, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:00.272675-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94d6df990: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:00.272718-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:00.272775-0500	Nexy	AudioConverter -> 0x94d6df990: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:54:00.273025-0500	Nexy	AudioConverter -> 0x94d6df990: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:54:00.273169-0500	Nexy	AudioConverter -> 0x94d6df990: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:54:00.285972-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}
default	21:54:00.286171-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)}
default	21:54:00.286185-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:00.281862-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	21:54:00.286204-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:00.286043-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	21:54:00.297643-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:54:00.297674-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:00.298177-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:00.297782-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:00.298511-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.298297-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94d6df990, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	21:54:00.298564-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.298398-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:00.298367-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.298583-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:00.298432-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.298496-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:00.298589-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.298706-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	21:54:00.298821-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.299129-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [1, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output",
    "1C-77-54-18-C8-A3:input"
)} Server update was not required.
default	21:54:00.298877-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:00.299241-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:00.298966-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.299257-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:00.299041-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:00.299268-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:00.299304-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.299372-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:00.299420-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:00.299469-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:00.299616-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	21:54:00.299674-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:00.313584-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:00.313385-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:00.313810-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:54:00.313935-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:00.314326-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:00.314219-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:00.314363-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:00.314260-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:00.314389-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 1
default	21:54:00.314291-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:00.314407-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	21:54:00.314446-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	21:54:00.315133-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
error	21:54:00.315470-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	21:54:00.336256-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49116 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:00.336335-0500	runningboardd	Assertion 394-48645-49116 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:00.336823-0500	runningboardd	Invalidating assertion 394-48645-49116 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:00.336067-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:00.336086-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:00.336100-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:00.337039-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49117 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:00.337106-0500	runningboardd	Assertion 394-48645-49117 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:00.344247-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:00.346713-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1171, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.347060-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:00.357503-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1171, subject=com.nexy.assistant,
default	21:54:00.375413-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:00.375504-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:00.375598-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:00.375665-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:00.389626-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.389641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.389652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.389658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.389666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.389673-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:00.389766-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:00.404325-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:00.404414-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:00.421835-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x94c6d8650: iounit configuration changed > posting notification
default	21:54:00.456166-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:54:00.461010-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:00.461092-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:00.461718-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49118 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:00.461162-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:00.461837-0500	runningboardd	Assertion 394-328-49118 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:00.462307-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:00.462338-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:00.462642-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:00.463783-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:00.463709-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:00.463879-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:00.463905-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:00.463912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:00.464021-0500	runningboardd	Invalidating assertion 394-48645-49117 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:00.465118-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:00.465312-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:00.466301-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:00.467348-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49119 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:00.466605-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:00.466619-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:00.466636-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:00.467504-0500	runningboardd	Assertion 394-48645-49119 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:00.469237-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1172, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:00.470623-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:00.471084-0500	runningboardd	Invalidating assertion 394-328-49118 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:00.471628-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:00.472436-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:00.475641-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:00.485867-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:00.485963-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:00.486027-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:00.486608-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486630-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486673-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486684-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:00.486707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486742-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486752-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486761-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:00.486783-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486794-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486812-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.486821-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.486850-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:00.486830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:00.486965-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:00.493519-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:00.493587-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:00.493630-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:00.493648-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:00.513858-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.513881-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.513943-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.514034-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:00.514118-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:00.514250-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:00.526331-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:00.984570-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
error	21:54:00.999280-0500	kernel	7 duplicate reports for Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:01.078802-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:01.082284-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:01.082353-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	21:54:02.458920-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:03.277535-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:54:03.278083-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:54:03.278220-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:03.278279-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:54:03.278312-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}
default	21:54:03.278362-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea042, Nexy(48645), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 66 stopping recording
default	21:54:03.278374-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:54:03.278393-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:54:03.278439-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:03.278487-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:03.278764-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:03.278707-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:54:03.278769-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:03.279077-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:03.279135-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:03.279201-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:03.279251-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:03.279284-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:03.279314-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:03.279407-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	21:54:03.279428-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:03.279443-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	21:54:03.280853-0500	runningboardd	Invalidating assertion 394-48645-49119 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:03.281152-0500	runningboardd	Invalidating assertion 394-328-49120 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:03.291533-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:03.291654-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:03.291733-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:03.291755-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:03.292470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:03.292489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:03.292504-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:03.292512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:03.292521-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:03.292541-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:03.292664-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:03.338094-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:03.338138-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:03.338165-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:03.338224-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:03.340781-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:03.341279-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:03.341622-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:03.381697-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x94f391540) Selecting device 0 from destructor
default	21:54:03.381711-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:03.381720-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:03.381726-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x94f391540) disconnecting device 91
default	21:54:03.381738-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x94f391540) destroying ioproc 0xa for device 91
default	21:54:03.381798-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:54:03.381836-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:54:03.381992-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x94f391540) nothing to setup
default	21:54:03.382008-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device listeners to device 0
default	21:54:03.382014-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 0
default	21:54:03.382021-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 7 device listeners from device 91
default	21:54:03.382241-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 91
default	21:54:03.382255-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:03.582146-0500	Nexy	nw_path_libinfo_path_check [24DDE92C-8A1F-4FDC-8CEC-BE0351205CB1 Hostname#63bd6588:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:54:03.582345-0500	mDNSResponder	[R80880] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:03.583247-0500	mDNSResponder	[R80881] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:03.585164-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8E74BAC6-B178-4AC3-946A-63AEDCC06AC3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51325,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x840df876 tp_proto=0x06"
default	21:54:03.585300-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51325<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064021 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7aaf722
default	21:54:03.592737-0500	kernel	tcp connected: [<IPv4-redacted>:51325<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064021 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7aaf722
default	21:54:04.262829-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:51325<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064021 t_state: LAST_ACK process: Nexy:48645 Duration: 0.678 sec Conn_Time: 0.008 sec bytes in/out: 811/55237 pkts in/out: 3/13 pkt rxmit: 1 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 9.468 ms rttvar: 6.937 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0xb7aaf722
default	21:54:04.262864-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51325<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064021 t_state: LAST_ACK process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:54:05.508119-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:05.508167-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:05.508192-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.508218-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:05.508228-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:05.508236-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:05.508244-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:05.508327-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:05.508270-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:05.508891-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2928 called from <private>
default	21:54:05.508912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:05.508932-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:05.514019-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:05.514050-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:05.514193-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.514221-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:05.514230-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:05.517011-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.517050-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.517307-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.517394-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:05.517407-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:05.517430-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:05.517442-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:05.517487-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:05.517549-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:05.517641-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:05.517684-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:05.521137-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:05.521166-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:05.521327-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.521354-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:05.521372-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:05.526073-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.528398-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:05.528419-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:05.528454-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:05.528975-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:05.530071-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.530458-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:05.530705-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.530754-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:05.531240-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:05.531322-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:05.531944-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:05.531991-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:05.532331-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:05.532390-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.532501-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:05.532720-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:05.533044-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:05.535666-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:05.536194-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:05.536952-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:05.536995-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:05.537199-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:05.537224-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:05.537230-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2928 called from <private>
default	21:54:05.537430-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:05.537441-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:05.537659-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:05.537724-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:05.537775-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:05.537820-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:05.537950-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:05.538068-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:05.538203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:05.538414-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:05.550925-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:05.550959-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:05.551178-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:05.553817-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:05.554172-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:05.554184-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:05.554224-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:05.554233-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:05.554240-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:05.554249-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:05.556730-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f3d9540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:05.556768-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f3d9540)
default	21:54:05.556951-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.556967-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:05.556974-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.556983-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:05.556993-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:05.557241-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:05.557265-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:05.557272-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:05.560838-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f3d9540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:05.560870-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f3d9540)
default	21:54:05.561058-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.561074-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:05.561083-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.561093-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:05.561103-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:05.561269-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:05.561291-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:05.561301-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:05.665426-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x94c6d8650: iounit configuration changed > posting notification
default	21:54:10.103631-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94d1382d0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:10.103666-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94d1382d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:10.103682-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:10.103681-0500	Nexy	AudioConverter -> 0x94d1382d0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:54:10.103703-0500	Nexy	AudioConverter -> 0x94d1382d0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:54:10.103710-0500	Nexy	AudioConverter -> 0x94d1382d0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:54:10.104446-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94d1382d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:10.104923-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x94c6d8650: start, was running 0
default	21:54:10.106762-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49124 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:10.106868-0500	runningboardd	Assertion 394-48645-49124 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:10.107305-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:10.107300-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49125 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:10.107405-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:10.107454-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:10.107479-0500	runningboardd	Assertion 394-328-49125 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:10.107548-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:10.111226-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:10.111639-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:10.111682-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:10.111717-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:10.111780-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:10.111958-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:10.114892-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:10.115055-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:10.115710-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:10.116625-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:10.433644-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:10.434576-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:54:10.434716-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:54:10.434758-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ea042, Nexy(48645), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:54:10.434801-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:10.434845-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:54:10.434878-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.434900-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:54:10.434912-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 66 starting playing
default	21:54:10.434987-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:10.435017-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:54:10.435040-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}
default	21:54:10.435062-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	21:54:10.435058-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.435115-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.435098-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:54:10.435270-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:54:10.435283-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:10.435137-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea042 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":48645}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea042, sessionType: 'prim', isRecording: false }, 
]
default	21:54:10.435288-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:10.435487-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.435574-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.435600-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:10.435612-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	21:54:10.435621-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	21:54:10.435631-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	21:54:10.435681-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:54:10.435745-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:13.000283-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:13.029273-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	21:54:13.100917-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:13.102577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:13.102610-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:13.102638-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:13.102654-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:13.102675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:13.102693-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:13.102994-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.066251-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:15.066876-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x94f391540) Selecting device 85 from constructor
default	21:54:15.066895-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:15.066905-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:15.066912-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x94f391540) nothing to teardown
default	21:54:15.066919-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x94f391540) connecting device 85
default	21:54:15.067034-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f391540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:15.067363-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x94f391540) created ioproc 0xc for device 85
default	21:54:15.067682-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 7 device listeners to device 85
default	21:54:15.067964-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 85
default	21:54:15.067977-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f391540)
default	21:54:15.068139-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:15.068152-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:15.068161-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:15.068171-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:15.068181-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:15.068316-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:15.068342-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:15.068351-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:15.068358-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device listeners from device 0
default	21:54:15.068365-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 0
default	21:54:15.068371-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:15.068393-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:54:15.068474-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x94f391540) caller requesting device change from 85 to 91
default	21:54:15.068484-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:15.068490-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:15.068496-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x94f391540) disconnecting device 85
default	21:54:15.068502-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x94f391540) destroying ioproc 0xc for device 85
default	21:54:15.068522-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	21:54:15.068845-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:15.069252-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x94f391540) connecting device 91
default	21:54:15.069395-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f391540) Device ID: 91 (Input:Yes | Output:No): true
default	21:54:15.071726-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1173, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.074038-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1173, subject=com.nexy.assistant,
default	21:54:15.075256-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:15.075311-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:54:15.075719-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28a100 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.077855-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:15.077918-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:15.079674-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.6, subject=com.nexy.assistant,
default	21:54:15.081043-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.096723-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x94f391540) created ioproc 0xb for device 91
default	21:54:15.096870-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 7 device listeners to device 91
default	21:54:15.097048-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 91
default	21:54:15.097064-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f391540)
default	21:54:15.097073-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	21:54:15.097083-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:15.097208-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:54:15.097218-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	21:54:15.097223-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:54:15.097311-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:15.097325-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f391540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:15.097331-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:15.097336-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 7 device listeners from device 85
default	21:54:15.097491-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 85
default	21:54:15.097497-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:15.097506-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	21:54:15.098031-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:15.099044-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1174, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.100172-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1174, subject=com.nexy.assistant,
default	21:54:15.100837-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:15.102370-0500	kernel	Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.104602-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:15.104626-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:54:15.117459-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:15.118407-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1175, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.119493-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1175, subject=com.nexy.assistant,
default	21:54:15.120131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28aa00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.133013-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:15.133831-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:15.133857-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:15.134788-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.7, subject=com.nexy.assistant,
default	21:54:15.135518-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.139029-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1176, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.140518-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1176, subject=com.nexy.assistant,
default	21:54:15.141237-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.149631-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.149687-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:15.149718-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:15.149733-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:15.150398-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.150408-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.150427-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.150434-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.150440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.150448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.150665-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.160820-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:54:15.160957-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:54:15.162278-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:15.162286-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:54:15.163594-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:15.163692-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:15.163708-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:15.163714-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:15.164145-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:15.164161-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:15.164172-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:15.164402-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:15.164426-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:15.166862-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:15.167659-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:15.166343-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:15.166352-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:15.166533-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:15.166547-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:15.166589-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:15.169693-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:15.169974-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:15.170093-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:15.170130-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:15.170131-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:15.166488-0500	runningboardd	Invalidating assertion 394-48645-49124 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:15.170232-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:15.170291-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:15.169147-0500	runningboardd	Invalidating assertion 394-328-49125 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:15.171418-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49127 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:15.171621-0500	runningboardd	Assertion 394-48645-49127 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:15.170346-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:15.170377-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:15.170422-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:15.170464-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:15.178478-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:15.178488-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:15.178615-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:15.178634-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:15.178641-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:15.179260-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:15.180876-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:15.181005-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:15.181060-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:15.181102-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:15.181128-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:15.182049-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:15.182368-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:15.182370-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
error	21:54:15.183300-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:15.183427-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:15.183737-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:15.183976-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:15.184082-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:15.184222-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:15.184454-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:15.184520-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:15.184596-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:15.187463-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:15.189968-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:15.190002-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:15.190077-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:15.190162-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:15.190402-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:15.190417-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:15.194896-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
error	21:54:15.194963-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:15.195013-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:15.195061-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:15.180587-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1177, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.195115-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:15.195677-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:15.195720-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:15.199525-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:15.201107-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:15.199536-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:15.199665-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:15.201565-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:15.202547-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:15.202563-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:15.202574-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:15.202581-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:15.202591-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:15.202755-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:15.202764-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:15.202792-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:15.202872-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:15.202927-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:15.202996-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:15.203044-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:15.203113-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:15.203176-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:15.203249-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:15.203316-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:15.203347-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:15.210951-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:15.211366-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:15.211709-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:15.211901-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:15.211081-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:15.212225-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:15.212395-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:15.222971-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:54:15.223172-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:15.222646-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:15.223926-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	21:54:15.224241-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:15.228269-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.228372-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0x94c6d8650: iounit configuration changed > stopping the engine
default	21:54:15.241729-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:15.241911-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	21:54:15.241966-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:15.242037-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:15.242208-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	21:54:15.241225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.243446-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.250180-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.250257-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:15.250300-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:15.250315-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:15.254570-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.260981-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:54:15.261197-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:54:15.263766-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:15.263792-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:15.276860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:15.284672-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.284784-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:15.284841-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:15.285177-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285197-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.285227-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285237-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.285248-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.285283-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285296-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285309-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.285316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.285336-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.285384-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:15.285399-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.285618-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.285624-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.292037-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.292135-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:15.292197-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:15.292213-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:15.305102-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:54:15.306261-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 issue_detected_sample_time=66240.000000 ] -- [ rms:[-27.483080], peaks:[-13.844627] ]
default	21:54:15.306296-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-35.846584], peaks:[-19.751659] ]
default	21:54:15.306579-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:15.306658-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:15.386585-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:54:15.391149-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49132 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:15.391243-0500	runningboardd	Assertion 394-328-49132 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:15.392374-0500	runningboardd	Invalidating assertion 394-48645-49131 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:15.392437-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:15.392525-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:15.392589-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:15.392635-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49133 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:15.392736-0500	runningboardd	Assertion 394-48645-49133 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:15.392729-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:15.389539-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:15.389611-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:2928 called from <private>
default	21:54:15.390717-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:15.391746-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:15.391762-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:15.395186-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1179, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:15.400110-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:15.406049-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.412765-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.412851-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:15.412908-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:15.413302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.413378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413400-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413444-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.413464-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413525-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:15.413516-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413600-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.413770-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.413793-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.413809-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.419142-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.419229-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:15.419287-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:15.419306-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:15.439340-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49134 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:15.438210-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:15.439534-0500	runningboardd	Assertion 394-328-49134 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:15.438257-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:15.438333-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:15.463078-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.463212-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:15.463318-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:15.463879-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.463900-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.463921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.463932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.463951-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.463963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.463992-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464051-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464092-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.464102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464113-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.464123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.464140-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464147-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:15.464165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.464202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:15.464212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:15.464221-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:15.464328-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:15.472012-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.472076-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:15.472130-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:15.472150-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:15.491950-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:15.494699-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49136 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:15.494868-0500	runningboardd	Assertion 394-328-49136 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:15.519947-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:15.520028-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:15.520078-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:16.030349-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
error	21:54:16.308690-0500	kernel	7 duplicate reports for Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:19.032649-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	21:54:19.293915-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:19.294692-0500	Nexy	nw_path_libinfo_path_check [B92112F7-5FC1-490B-ACB2-ABC3E936D690 Hostname#63bd6588:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:54:19.294873-0500	mDNSResponder	[R80882] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:19.295989-0500	mDNSResponder	[R80883] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:19.297547-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0E6179A2-A6AA-4136-8F45-FD42F72DF9F3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51326,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x0faa050d tp_proto=0x06"
default	21:54:19.297632-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51326<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064080 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa263df6d
default	21:54:19.303678-0500	kernel	tcp connected: [<IPv4-redacted>:51326<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064080 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa263df6d
default	21:54:19.581753-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:54:19.582097-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:54:19.582248-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:19.582329-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:54:19.582369-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}
default	21:54:19.582432-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:54:19.582434-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea042, Nexy(48645), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 66 stopping recording
default	21:54:19.582465-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:54:19.582505-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:19.582544-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:19.582693-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:54:19.582705-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:19.582783-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:19.583162-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:19.583053-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:19.583199-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:19.583098-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:19.583218-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:19.583240-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:19.583355-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	21:54:19.583422-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:19.583472-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	21:54:19.585530-0500	runningboardd	Invalidating assertion 394-48645-49135 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:19.586039-0500	runningboardd	Invalidating assertion 394-328-49136 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:19.596956-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:19.597060-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:19.597125-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:19.597146-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:19.597655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:19.597667-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:19.597688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:19.597696-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:19.597702-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:19.597709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:19.597803-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:19.685791-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x94f391540) Selecting device 0 from destructor
default	21:54:19.685825-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x94f391540)
default	21:54:19.685838-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x94f391540) not already running
default	21:54:19.685847-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x94f391540) disconnecting device 91
default	21:54:19.685859-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x94f391540) destroying ioproc 0xb for device 91
default	21:54:19.685914-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:54:19.685966-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:54:19.686193-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x94f391540) nothing to setup
default	21:54:19.686219-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device listeners to device 0
default	21:54:19.686230-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x94f391540) adding 0 device delegate listeners to device 0
default	21:54:19.686242-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 7 device listeners from device 91
default	21:54:19.686608-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x94f391540) removing 0 device delegate listeners from device 91
default	21:54:19.686630-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x94f391540)
default	21:54:19.688703-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:19.688714-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:19.688724-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:19.688751-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:19.691859-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:19.692503-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:19.692764-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:19.767502-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:51326<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064080 t_state: LAST_ACK process: Nexy:48645 Duration: 0.471 sec Conn_Time: 0.007 sec bytes in/out: 821/73177 pkts in/out: 4/19 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.156 ms rttvar: 1.812 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0xa263df6d
default	21:54:19.767527-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51326<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1064080 t_state: LAST_ACK process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:54:21.807054-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:21.807147-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:21.807168-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:21.807656-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.807703-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:21.807723-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:21.809830-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:21.809838-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:21.809884-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:21.809921-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2928 called from <private>
default	21:54:21.809941-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:21.809951-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:21.820827-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:21.820863-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:21.821027-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.821054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:21.821062-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:21.823678-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:21.823718-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:21.823724-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:21.824126-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:21.824301-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:21.824515-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2928 called from <private>
default	21:54:21.824753-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:21.824558-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.825171-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:21.825299-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:21.825341-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:21.827210-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:21.827280-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:21.827477-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.827513-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:21.827547-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:21.832151-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.834726-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:21.834748-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:21.834791-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:21.834804-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:21.836546-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:21.836565-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:21.836811-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.836832-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:21.836863-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:21.837208-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.837227-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:21.837234-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:21.837542-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:21.837824-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.837886-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:21.838043-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.838125-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:21.838397-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:21.838612-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:21.840383-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:21.840588-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:21.841413-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:21.841465-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:21.841490-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.841514-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:21.841521-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:21.841846-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:21.841859-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:21.841911-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:21.841922-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:21.841931-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:21.841954-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:21.842160-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:21.842268-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:21.860717-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:21.860758-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:21.860924-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:21.861603-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:21.861778-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:21.861798-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:21.861828-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:21.861835-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:21.861851-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:21.861859-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:21.862432-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f3d9540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:21.862462-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f3d9540)
default	21:54:21.862879-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.862893-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:21.862900-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.862914-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:21.862926-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:21.863086-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:21.863116-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:21.863126-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:21.863671-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x94f3d9540) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:21.863687-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x94f3d9540)
default	21:54:21.864531-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.864550-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:21.864558-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.864573-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:21.864583-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:21.864748-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:21.864768-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x94f3d9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:21.864780-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:21.970690-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x94c6d8650: iounit configuration changed > posting notification
default	21:54:23.924655-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x94d138510, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:23.924684-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94d138510: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:23.924695-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:23.924700-0500	Nexy	AudioConverter -> 0x94d138510: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:54:23.924719-0500	Nexy	AudioConverter -> 0x94d138510: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:54:23.924727-0500	Nexy	AudioConverter -> 0x94d138510: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:54:23.925266-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x94d138510: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:23.925513-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x94c6d8650: start, was running 0
default	21:54:23.927702-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49138 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:23.927853-0500	runningboardd	Assertion 394-48645-49138 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:23.928339-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49139 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:23.928344-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:23.928416-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:23.928451-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:23.928455-0500	runningboardd	Assertion 394-328-49139 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:23.928512-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:23.932132-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:23.932410-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:23.932425-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:23.932436-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:23.932460-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:23.932742-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:23.933064-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:23.935548-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:23.935986-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:23.936139-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:24.194237-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:24.195023-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:54:24.195123-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:54:24.195151-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ea042, Nexy(48645), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:54:24.195185-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:24.195230-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:54:24.195250-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195271-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:54:24.195282-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 66 starting playing
default	21:54:24.195347-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:24.195383-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:54:24.195359-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195394-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195405-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}
default	21:54:24.195426-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	21:54:24.195576-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:54:24.195588-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:24.195457-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:54:24.195480-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea042 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":48645}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea042, sessionType: 'prim', isRecording: false }, 
]
default	21:54:24.195693-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:24.195877-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195946-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195975-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:24.195991-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	21:54:24.196002-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	21:54:24.196012-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	21:54:24.196052-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:54:24.196109-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:25.029171-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	21:54:25.651915-0500	Nexy	nw_path_libinfo_path_check [1F5D04F3-ABDB-45DC-802E-89FBD9E398F2 Hostname#9ef6a1a1:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:54:25.652090-0500	mDNSResponder	[R80884] DNSServiceQueryRecord START -- qname: <mask.hash: 'A7k48ORuTxZhAI6MeQRfGQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: 17e34662
default	21:54:25.653004-0500	mDNSResponder	[R80885] DNSServiceQueryRecord START -- qname: <mask.hash: 'A7k48ORuTxZhAI6MeQRfGQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: 17e34662
default	21:54:25.664727-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8DCDEC85-0F31-49C3-BDDC-565212A9C368 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51327,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xae9f8914 tp_proto=0x06"
default	21:54:25.664803-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51327<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064131 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xafb656b1
default	21:54:25.678138-0500	kernel	tcp connected: [<IPv4-redacted>:51327<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064131 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xafb656b1
default	21:54:25.727946-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:51327<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064131 t_state: FIN_WAIT_1 process: Nexy:48645 Duration: 0.063 sec Conn_Time: 0.013 sec bytes in/out: 46511/766 pkts in/out: 7/3 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.562 ms rttvar: 3.562 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xafb656b1
default	21:54:25.727957-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51327<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064131 t_state: FIN_WAIT_1 process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:54:26.008582-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:26.010416-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.1, subject=com.nexy.assistant,
default	21:54:26.011370-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.033330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1643, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:26.034348-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1643, subject=com.nexy.assistant,
default	21:54:26.035028-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.106468-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.21, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:54:26.115936-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.21, subject=com.nexy.assistant,
default	21:54:26.116813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.543131-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:26.550386-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.2, subject=com.nexy.assistant,
default	21:54:26.551331-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28b900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.569993-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:26.571100-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.3, subject=com.nexy.assistant,
default	21:54:26.571765-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:26.583808-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:26.584558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:26.585750-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.4, subject=com.nexy.assistant,
default	21:54:26.586440-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:26.598731-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:26.599942-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:26.601027-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.5, subject=com.nexy.assistant,
default	21:54:26.601763-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.807826-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1644, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper, pid=48915, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper.app/Contents/MacOS/Google Chrome Helper}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:26.809420-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1644, subject=com.nexy.assistant,
default	21:54:26.810142-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1109500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.921737-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48919.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome.framework.AlertNotificationService, pid=48919, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Alerts).app/Contents/MacOS/Google Chrome Helper (Alerts)}, },
default	21:54:26.923214-0500	tccd	AUTHREQ_SUBJECT: msgID=48919.1, subject=com.nexy.assistant,
default	21:54:26.923901-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e8600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:26.946707-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1645, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.framework.AlertNotificationService, pid=48919, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Alerts).app/Contents/MacOS/Google Chrome Helper (Alerts)}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:26.947686-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1645, subject=com.nexy.assistant,
default	21:54:26.948359-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1109500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.018162-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.158454-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.6, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:27.159660-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.6, subject=com.nexy.assistant,
default	21:54:27.160334-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:27.173475-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:27.174108-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.7, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:27.175131-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.7, subject=com.nexy.assistant,
default	21:54:27.175755-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:27.187613-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:27.188419-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.8, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:27.189528-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.8, subject=com.nexy.assistant,
default	21:54:27.190186-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:27.201858-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:27.202456-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.9, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:27.203470-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.9, subject=com.nexy.assistant,
default	21:54:27.204083-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:27.215832-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:27.216505-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.10, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:27.217603-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.10, subject=com.nexy.assistant,
default	21:54:27.218287-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb157300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.352897-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1109500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.609230-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:27.609313-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:27.812859-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48928.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	21:54:27.814949-0500	tccd	AUTHREQ_SUBJECT: msgID=48928.1, subject=com.nexy.assistant,
default	21:54:27.815915-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110aa00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.844172-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1646, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:27.845318-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1646, subject=com.nexy.assistant,
default	21:54:27.846107-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11e8600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:27.930291-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b1108300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:28.012253-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	21:54:28.217145-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1647, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:28.218203-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1647, subject=com.nexy.assistant,
default	21:54:28.218915-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11ebc00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:28.243463-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.13, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:28.244899-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.13, subject=com.nexy.assistant,
default	21:54:28.245712-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:28.258930-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:28.259629-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.14, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:28.260730-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.14, subject=com.nexy.assistant,
default	21:54:28.261365-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
error	21:54:28.273385-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	21:54:28.274137-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.15, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:28.275259-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.15, subject=com.nexy.assistant,
default	21:54:28.275954-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288c00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:28.424959-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.16, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:28.426809-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.16, subject=com.nexy.assistant,
default	21:54:28.427854-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:28.462944-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:28.604825-0500	tccd	AUTHREQ_SUBJECT: msgID=48905.17, subject=com.nexy.assistant,
default	21:54:28.606790-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:28.668694-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48905.19, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=48905, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	21:54:28.922476-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48928.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	21:54:28.925446-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48928.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	21:54:28.935338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48928.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	21:54:28.983985-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48928.6, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	21:54:29.006036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.903, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.009465-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.904, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.012089-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.905, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.016587-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.906, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.029099-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.907, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.033746-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.908, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.034229-0500	Nexy	nw_path_libinfo_path_check [CB0D7DA3-2B20-4FEA-AB08-AFD8A55ED11F Hostname#a81b0a92:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:54:29.034373-0500	mDNSResponder	[R80898] DNSServiceQueryRecord START -- qname: <mask.hash: 'UlvAWzU0CnfVLqkSkVE5tQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: d5fa343
default	21:54:29.035006-0500	mDNSResponder	[R80899] DNSServiceQueryRecord START -- qname: <mask.hash: 'UlvAWzU0CnfVLqkSkVE5tQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: d5fa343
default	21:54:29.037192-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.909, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.039585-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.910, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.049771-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 90BCF3BB-A2B3-462A-9E49-7735519ED0F6 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51364,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x55b9970b tp_proto=0x06"
default	21:54:29.049959-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51364<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064311 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x801904bb
default	21:54:29.054512-0500	kernel	tcp connected: [<IPv4-redacted>:51364<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 1064311 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x801904bb
default	21:54:29.067822-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.911, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.070481-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.912, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.072650-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.913, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.074960-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.914, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.087244-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.915, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.090563-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.916, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.093373-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.917, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.096888-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.918, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.123523-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.919, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:29.125370-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.920, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=48928, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:33.932389-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1181, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper, pid=48963, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper.app/Contents/MacOS/Google Chrome Helper}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:33.939591-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1181, subject=com.nexy.assistant,
default	21:54:33.940675-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154300 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:33.959925-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1183, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper, pid=48963, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper.app/Contents/MacOS/Google Chrome Helper}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:33.961055-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1183, subject=com.nexy.assistant,
default	21:54:33.961704-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb28bc00 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.074009-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:35.074919-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:35.317977-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:35.318790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:35.318804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:35.318887-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:35.318897-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:35.318903-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:35.318909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:35.319091-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:35.402067-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48973.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome.helper.plugin, pid=48973, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app/Contents/MacOS/Google Chrome Helper (Plugin)}, },
default	21:54:35.403695-0500	tccd	AUTHREQ_SUBJECT: msgID=48973.1, subject=com.nexy.assistant,
default	21:54:35.404702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.426685-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1649, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper.plugin, pid=48973, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app/Contents/MacOS/Google Chrome Helper (Plugin)}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:35.427774-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1649, subject=com.nexy.assistant,
default	21:54:35.428483-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110a700 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.538012-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110a100 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.564069-0500	Google Chrome Helper (Plugin)	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.google.Chrome.helper.plugin"
)}
default	21:54:35.564275-0500	Google Chrome Helper (Plugin)	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.google.Chrome.helper.plugin"
)}
default	21:54:35.564764-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	21:54:35.565320-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=48973.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome.helper.plugin, pid=48973, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app/Contents/MacOS/Google Chrome Helper (Plugin)}, },
default	21:54:35.573189-0500	tccd	AUTHREQ_SUBJECT: msgID=48973.3, subject=com.nexy.assistant,
default	21:54:35.574153-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb288600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.601285-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	21:54:35.602441-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1184, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper.plugin, pid=48973, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app/Contents/MacOS/Google Chrome Helper (Plugin)}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:35.603598-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1184, subject=com.nexy.assistant,
default	21:54:35.604423-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.626800-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1186, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper.plugin, pid=48973, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app/Contents/MacOS/Google Chrome Helper (Plugin)}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:35.628266-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1186, subject=com.nexy.assistant,
default	21:54:35.629136-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289800 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:35.670331-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/reactions-enabled newValue: 1
default	21:54:35.671462-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/gestures-enabled newValue: (null)
error	21:54:35.727039-0500	kernel	Sandbox: UVCAssistant(519) deny(1) process-info-pidinfo others [Nexy(48645)]
default	21:54:35.917720-0500	Google Chrome Helper (Plugin)	<<<< AVCaptureDALDevice >>>> +[WombatDeviceFilter _isFilteringWombatDevices]_block_invoke: Could not find bundle for AVCaptureClientPreferencesDomain() = com.nexy.assistant, falling back to main bundle com.google.Chrome.helper.plugin (/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Plugin).app)
default	21:54:35.924046-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-unavailablereasons newValue: 0
default	21:54:35.927213-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-unavailablereasons newValue: 0
default	21:54:35.930094-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/studiolighting-unavailablereasons newValue: 0
default	21:54:39.597702-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:40.498557-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:42.007117-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:42.009758-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x950c20740) Selecting device 85 from constructor
default	21:54:42.009769-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x950c20740)
default	21:54:42.009776-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x950c20740) not already running
default	21:54:42.009778-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x950c20740) nothing to teardown
default	21:54:42.009785-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x950c20740) connecting device 85
default	21:54:42.009885-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x950c20740) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:42.010354-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x950c20740) created ioproc 0xd for device 85
default	21:54:42.010612-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 7 device listeners to device 85
default	21:54:42.010927-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 0 device delegate listeners to device 85
default	21:54:42.010941-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x950c20740)
default	21:54:42.011044-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:42.011066-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:42.011077-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:42.011085-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:42.011097-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:42.011209-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x950c20740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:42.011219-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x950c20740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:42.011226-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:42.011231-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 0 device listeners from device 0
default	21:54:42.011235-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 0 device delegate listeners from device 0
default	21:54:42.011240-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x950c20740)
default	21:54:42.011255-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:54:42.011312-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x950c20740) caller requesting device change from 85 to 91
default	21:54:42.011317-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x950c20740)
default	21:54:42.011323-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x950c20740) not already running
default	21:54:42.011328-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x950c20740) disconnecting device 85
default	21:54:42.011333-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x950c20740) destroying ioproc 0xd for device 85
default	21:54:42.011344-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	21:54:42.011645-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:42.011852-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x950c20740) connecting device 91
default	21:54:42.012054-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x950c20740) Device ID: 91 (Input:Yes | Output:No): true
default	21:54:42.014004-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1187, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:42.016930-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1187, subject=com.nexy.assistant,
default	21:54:42.018481-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289800 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.018982-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:42.019027-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	21:54:42.021425-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.8, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:42.021461-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:42.024079-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.8, subject=com.nexy.assistant,
default	21:54:42.027894-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110a400 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.042525-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x950c20740) created ioproc 0xc for device 91
default	21:54:42.042679-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 7 device listeners to device 91
default	21:54:42.042860-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 0 device delegate listeners to device 91
default	21:54:42.042869-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x950c20740)
default	21:54:42.042876-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	21:54:42.042887-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:42.043020-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:54:42.043028-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	21:54:42.043032-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:54:42.043131-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x950c20740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:42.043158-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x950c20740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:42.043165-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:42.043173-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 7 device listeners from device 85
default	21:54:42.043355-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 0 device delegate listeners from device 85
default	21:54:42.043366-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x950c20740)
default	21:54:42.043375-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	21:54:42.043991-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:42.045073-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1188, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:42.046258-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1188, subject=com.nexy.assistant,
default	21:54:42.047246-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.049879-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:54:42.049911-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
error	21:54:42.051124-0500	kernel	Sandbox: replayd(42383) deny(1) file-read-data /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.072324-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:54:42.073909-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1189, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:42.074481-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:42.076261-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1189, subject=com.nexy.assistant,
default	21:54:42.076411-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42383.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:54:42.076441-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=42383, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:42.078322-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289800 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.079202-0500	tccd	AUTHREQ_SUBJECT: msgID=42383.9, subject=com.nexy.assistant,
default	21:54:42.081269-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110a400 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.109025-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.109113-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:42.109163-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:42.115667-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1190, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:42.119637-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1190, subject=com.nexy.assistant,
default	21:54:42.126543-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.151009-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:54:42.173000-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:54:42.173227-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:54:42.176502-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.176542-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:42.176553-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:42.177784-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:42.177820-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:42.178616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:42.178638-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:42.180895-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:42.182046-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.183109-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:42.183136-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2928 called from <private>
default	21:54:42.183171-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:42.183207-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:42.180910-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:42.188736-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:42.189599-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:42.189925-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:42.190082-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:42.190119-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:42.197422-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:42.197752-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:42.198324-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:42.198476-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:42.198554-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:42.199464-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:42.199606-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:42.199608-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
error	21:54:42.201368-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:42.201420-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:42.201463-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:42.201494-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:42.202728-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:42.202884-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:42.203191-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:42.203322-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:42.203438-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:42.210170-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:42.214771-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:42.215024-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:42.215050-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:42.215070-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:42.219067-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:42.224198-0500	runningboardd	Invalidating assertion 394-48645-49138 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:42.219105-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:42.219896-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:42.222939-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:42.222955-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:42.227174-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
error	21:54:42.229557-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:42.229614-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:42.230438-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:42.231096-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:42.231554-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:42.229675-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:42.232037-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:42.229718-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:42.230015-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:42.230057-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:42.230365-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.232325-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:42.232366-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:42.232409-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:42.232583-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:42.232681-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:42.232837-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:42.232881-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:42.232939-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:42.233000-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:42.233076-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:42.233155-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:42.233222-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:42.233258-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:42.233263-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:42.233314-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.233306-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:42.234391-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:42.233448-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:42.234692-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:42.234848-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:42.234553-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:42.234918-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.234545-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:42.234944-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:42.234977-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:42.234988-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:42.234994-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:42.235021-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:42.235044-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:42.235064-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:42.235078-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:42.235112-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:42.235186-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:42.235248-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2934 called from <private>
default	21:54:42.235280-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2934 called from <private>
default	21:54:42.235346-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:42.235383-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:42.235486-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:42.232949-0500	runningboardd	Invalidating assertion 394-328-49139 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:42.235496-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:42.235503-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2934 called from <private>
default	21:54:42.235510-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2934 called from <private>
default	21:54:42.318166-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49184 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:42.318327-0500	runningboardd	Assertion 394-328-49184 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.319123-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:42.319189-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:42.319252-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:42.319386-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:42.330573-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49186 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:42.330718-0500	runningboardd	Assertion 394-48645-49186 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.331497-0500	runningboardd	Invalidating assertion 394-48645-49186 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:42.331537-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:42.331641-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:42.331733-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:42.331782-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:42.331815-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49187 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:42.331892-0500	runningboardd	Assertion 394-48645-49187 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.336261-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:42.345356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.345374-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.345391-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.345397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.345406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.345428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.345829-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:42.346491-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:54:42.346565-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 66 stopping playing
default	21:54:42.346607-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:54:42.346638-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:42.346745-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:42.347445-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.347491-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.346211-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:42.347440-0500	runningboardd	Invalidating assertion 394-328-49184 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:42.347512-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	21:54:42.347266-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:54:42.347285-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:42.347088-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.355222-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.355289-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:42.355340-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:42.355356-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:42.384928-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.384946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.384959-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.384968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.384975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.384982-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.385243-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:42.404732-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:42.418277-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:42.418322-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:42.418381-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:42.435100-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:42.435599-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:42.436070-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.449860-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.449982-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:42.450052-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:42.450607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450644-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450670-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450679-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.450705-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450720-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450731-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450741-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450757-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.450778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450793-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450810-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450858-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:42.450854-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.450944-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.450990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.451111-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:42.459695-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:42.459887-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:42.459918-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:42.468317-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x94c6d8650: iounit configuration changed > posting notification
default	21:54:42.472383-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1192, subject=com.nexy.assistant,
default	21:54:42.481414-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb154900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.492121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.492141-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.492156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.492166-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.492176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.492185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.546649-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:54:42.550263-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 issue_detected_sample_time=97920.000000 ] -- [ rms:[-25.518419], peaks:[-13.253941] ]
default	21:54:42.550328-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-34.105740], peaks:[-17.867210] ]
default	21:54:42.550900-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:42.550988-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x95ccbfc00] Created node ADM::com.nexy.assistant_2928.2663.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:54:42.656344-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:54:42.659193-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:42.659255-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2928 called from <private>
default	21:54:42.660758-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49190 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:42.663119-0500	runningboardd	Assertion 394-328-49190 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.663867-0500	runningboardd	Invalidating assertion 394-48645-49189 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:42.663950-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:42.664174-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:42.664252-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:42.660147-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:42.664329-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:42.664429-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:42.662750-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:42.662923-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:42.662946-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2928 called from <private>
default	21:54:42.664951-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:42.662955-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2928 called from <private>
default	21:54:42.665970-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:42.667239-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49191 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:42.667407-0500	runningboardd	Assertion 394-48645-49191 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.666254-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2928 called from <private>
default	21:54:42.666275-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2928 called from <private>
default	21:54:42.666289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:42.670663-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1193, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:54:42.672774-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:42.673324-0500	runningboardd	Invalidating assertion 394-328-49190 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:42.673777-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:42.675710-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1193, subject=com.nexy.assistant,
default	21:54:42.676644-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:42.678155-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289800 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:42.680135-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.686758-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.686912-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:42.686990-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:42.687448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687467-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687547-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687555-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.687572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687586-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687596-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687611-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687617-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.687658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687679-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:42.687694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.687777-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.687798-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.687808-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:42.694240-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.694399-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:42.694498-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:42.694519-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:42.709126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.709145-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.709156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.709163-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.709171-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.709177-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.709427-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:42.715677-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49192 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:42.715984-0500	runningboardd	Assertion 394-328-49192 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:42.714108-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2928 called from <private>
default	21:54:42.729114-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.739682-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.739875-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	21:54:42.739959-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	21:54:42.740500-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740555-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740576-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740587-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.740608-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740622-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740659-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.740684-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740744-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:54:42.740756-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740803-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:42.740871-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:42.740886-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:42.741070-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
error	21:54:42.763710-0500	Nexy	        HALB_IOThread.cpp:327    HALB_IOThread::_Start: there already is a thread
default	21:54:42.763818-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	21:54:42.765217-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	21:54:42.765361-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:54:42.765409-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ea042, Nexy(48645), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:54:42.765458-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:42.765531-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	21:54:42.765611-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:42.765614-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.765661-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:42.765743-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	21:54:42.765753-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.765760-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea042, Nexy(48645), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 66 starting recording
default	21:54:42.765887-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:42.765870-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.765929-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:54:42.765954-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.766052-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.766180-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:42.766172-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:54:42.766527-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	21:54:42.766558-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:42.766797-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:42.767672-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:42.767800-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:42.767838-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:42.767868-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 3
default	21:54:42.767904-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:42.909250-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.914562-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:42.914695-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	21:54:45.087946-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:47.539192-0500	Nexy	[com.apple.controlcenter:08FD4860-E601-49E0-8E89-9516B9018BC2] Sending action(s) in update: NSSceneFenceAction
default	21:54:48.046580-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	21:54:48.046988-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:54:48.047127-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:48.047195-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:54:48.047235-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:48.047327-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ea042, Nexy(48645), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 66 stopping recording
default	21:54:48.047339-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:54:48.047357-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:54:48.047395-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:48.047445-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:48.047645-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:54:48.047683-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:48.047867-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:48.048300-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:48.048355-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:48.048413-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:48.048468-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:48.049726-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:54:48.049793-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:54:48.049196-0500	runningboardd	Invalidating assertion 394-48645-49191 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645]
default	21:54:48.050075-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:48.050090-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	21:54:48.050005-0500	runningboardd	Invalidating assertion 394-328-49192 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) from originator [osservice<com.apple.powerd>:328]
default	21:54:48.055980-0500	Nexy	nw_path_libinfo_path_check [2D0BE4F9-74F1-4D45-9030-55D640924D4D Hostname#63bd6588:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:54:48.056180-0500	mDNSResponder	[R80959] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:48.057085-0500	mDNSResponder	[R80960] DNSServiceQueryRecord START -- qname: <mask.hash: 'JBdY3Np+KY/jfsiVj+G9MQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 48645 (Nexy), name hash: b360ab20
default	21:54:48.063563-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:48.063703-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:54:48.063792-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:54:48.063819-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:54:48.064704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:48.064719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:48.064737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:48.064747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:54:48.064754-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:54:48.064760-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:54:48.064877-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:54:48.068592-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 7BB7CB03-77EE-4499-89E8-449E390BF288 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51421,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x4d85097f tp_proto=0x06"
default	21:54:48.068715-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51421<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1065843 t_state: SYN_SENT process: Nexy:48645 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x961a509c
default	21:54:48.074217-0500	kernel	tcp connected: [<IPv4-redacted>:51421<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1065843 t_state: ESTABLISHED process: Nexy:48645 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x961a509c
default	21:54:48.152357-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x950c20740) Selecting device 0 from destructor
default	21:54:48.152375-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x950c20740)
default	21:54:48.152381-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x950c20740) not already running
default	21:54:48.152390-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x950c20740) disconnecting device 91
default	21:54:48.152400-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x950c20740) destroying ioproc 0xc for device 91
default	21:54:48.152434-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	21:54:48.152467-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:54:48.152614-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x950c20740) nothing to setup
default	21:54:48.152627-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 0 device listeners to device 0
default	21:54:48.152635-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x950c20740) adding 0 device delegate listeners to device 0
default	21:54:48.152641-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 7 device listeners from device 91
default	21:54:48.152842-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x950c20740) removing 0 device delegate listeners from device 91
default	21:54:48.152861-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x950c20740)
default	21:54:48.155147-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:48.155158-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:48.155169-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:48.155188-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:48.157809-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:48.158289-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:48.158482-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:49.431665-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:51421<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1065843 t_state: LAST_ACK process: Nexy:48645 Duration: 1.364 sec Conn_Time: 0.006 sec bytes in/out: 924/165470 pkts in/out: 4/63 pkt rxmit: 41 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 8.218 ms rttvar: 5.750 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0x961a509c
default	21:54:49.431701-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51421<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 1065843 t_state: LAST_ACK process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:54:50.185939-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:50.185996-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:50.186006-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:50.187464-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:50.187479-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2928)
default	21:54:50.187494-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:50.187498-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2928 called from <private>
default	21:54:50.187501-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:50.187549-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2928 called from <private>
default	21:54:50.190417-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.190458-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:50.190465-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:50.203248-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:50.203248-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2928)
default	21:54:50.203304-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:50.203304-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2928 called from <private>
default	21:54:50.203330-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:50.203334-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2928 called from <private>
default	21:54:50.203453-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:50.203835-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:50.204169-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.204231-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:50.204330-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:50.208312-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:50.208400-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:50.210047-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:50.210062-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:50.210079-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:50.210093-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:50.210099-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:50.210104-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:50.210155-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.210235-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:50.210310-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:50.213892-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:50.213903-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:50.214083-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:50.215523-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:50.215533-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:50.215642-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.215663-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2927 called from <private>
default	21:54:50.215671-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2927 called from <private>
default	21:54:50.216367-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:50.216526-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2927 called from <private>
default	21:54:50.216536-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2927 called from <private>
default	21:54:50.216612-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:54:50.216567-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2927 called from <private>
default	21:54:50.216578-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2927 called from <private>
default	21:54:50.217117-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:54:50.218090-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:50.218106-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:50.218127-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:50.218143-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2927)
default	21:54:50.218157-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2927 called from <private>
default	21:54:50.218162-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2927 called from <private>
default	21:54:50.218209-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.218218-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2934)
default	21:54:50.218230-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2927 called from <private>
default	21:54:50.218236-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2934)
default	21:54:50.218308-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2927 called from <private>
default	21:54:50.218388-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:50.218472-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:50.218563-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2934 called from <private>
default	21:54:50.218626-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2934 called from <private>
default	21:54:50.218672-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2934 called from <private>
default	21:54:50.218708-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2934 called from <private>
default	21:54:50.218748-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:50.218779-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:50.218843-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:50.218885-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:50.218910-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2934 called from <private>
default	21:54:50.218954-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2934 called from <private>
default	21:54:50.219019-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2934 called from <private>
default	21:54:50.219064-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2934 called from <private>
default	21:54:50.233535-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2927 called from <private>
default	21:54:50.233562-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2927 called from <private>
default	21:54:50.233715-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2927)
default	21:54:50.245548-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:50.245645-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:50.245676-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:50.355464-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x94c6d8650: iounit configuration changed > posting notification
default	21:54:52.577740-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x950bbe0d0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:52.577807-0500	Nexy	AudioConverter -> 0x950bbe0d0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	21:54:52.577825-0500	Nexy	AudioConverter -> 0x950bbe0d0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	21:54:52.577831-0500	Nexy	AudioConverter -> 0x950bbe0d0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	21:54:52.577794-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x950bbe0d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:52.577850-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:52.578255-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x950bbe0d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:52.578337-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x94c6d8650: start, was running 0
default	21:54:52.580287-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-48645-49199 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:52.580410-0500	runningboardd	Assertion 394-48645-49199 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:52.581034-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:52.581038-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.58107047.58107056(501)>:48645] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49200 target:48645 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:52.581069-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:52.581137-0500	runningboardd	Assertion 394-328-49200 (target:[app<application.com.nexy.assistant.58107047.58107056(501)>:48645]) will be created as active
default	21:54:52.581106-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:52.581173-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:52.585201-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:52.585649-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring jetsam update because this process is not memory-managed
default	21:54:52.585709-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring suspend because this process is not lifecycle managed
default	21:54:52.585792-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring GPU update because this process is not GPU managed
default	21:54:52.585863-0500	runningboardd	[app<application.com.nexy.assistant.58107047.58107056(501)>:48645] Ignoring memory limit update because this process is not memory-managed
default	21:54:52.585932-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:52.586344-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:52.588793-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.58107047.58107056(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:54:52.589370-0500	ControlCenter	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:52.589551-0500	gamepolicyd	Received state update for 48645 (app<application.com.nexy.assistant.58107047.58107056(501)>, running-active-NotVisible
default	21:54:52.595015-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:52.596159-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea042","name":"Nexy(48645)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:54:52.596298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:54:52.596339-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ea042, Nexy(48645), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:54:52.596375-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:52.596426-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea042, Nexy(48645), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:54:52.596478-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.596513-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:54:52.596540-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 66 starting playing
default	21:54:52.596628-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:52.596671-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 66, PID = 48645, Name = sid:0x1ea042, Nexy(48645), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:54:52.596703-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:52.596697-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.596755-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.596748-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:54:52.596925-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:54:52.596951-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:52.596954-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x19BF0001 category Not set
default	21:54:52.596780-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea042 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":48645}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea042, sessionType: 'prim', isRecording: false }, 
]
default	21:54:52.597215-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.597340-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.597373-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:54:52.597388-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	21:54:52.597491-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:53.163397-0500	find_contacts_by_name_swift	[0x100bb90b0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:54:53.164175-0500	find_contacts_by_name_swift	[0x100bb9cb0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	21:54:53.164261-0500	find_contacts_by_name_swift	[0x100bba220] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	21:54:53.164719-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49310.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	21:54:53.166670-0500	find_contacts_by_name_swift	[0x100bb9940] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	21:54:53.166971-0500	find_contacts_by_name_swift	[0xa3cc5c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:54:53.167665-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49310.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	21:54:53.207047-0500	tccd	AUTHREQ_SUBJECT: msgID=49310.2, subject=com.nexy.assistant,
default	21:54:53.208769-0500	tccd	AUTHREQ_SUBJECT: msgID=49310.1, subject=com.nexy.assistant,
default	21:54:53.214514-0500	find_contacts_by_name_swift	[0xa3cc5c000] invalidated after the last release of the connection object
default	21:54:53.214649-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	21:54:53.215919-0500	find_contacts_by_name_swift	[0x100bb90b0] invalidated after the last release of the connection object
default	21:54:53.215939-0500	find_contacts_by_name_swift	[0xa3cc5c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:54:53.216074-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	21:54:53.216280-0500	find_contacts_by_name_swift	[0xa3cc5c140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:54:53.216351-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49310.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	21:54:53.216756-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49310.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	21:54:53.217581-0500	tccd	AUTHREQ_SUBJECT: msgID=49310.3, subject=com.nexy.assistant,
default	21:54:53.218056-0500	tccd	AUTHREQ_SUBJECT: msgID=49310.4, subject=com.nexy.assistant,
default	21:54:53.218283-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.218887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.237257-0500	find_contacts_by_name_swift	[0xa3cc5c000] invalidated after the last release of the connection object
default	21:54:53.240869-0500	find_contacts_by_name_swift	[0xa3cc5c140] invalidated after the last release of the connection object
default	21:54:53.241089-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	21:54:53.241108-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	21:54:53.241122-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	21:54:53.242594-0500	find_contacts_by_name_swift	[0xa3cc5c000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:54:53.244719-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.25, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:54:53.246141-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.25, subject=com.nexy.assistant,
default	21:54:53.247067-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb289500 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.271075-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.26, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:54:53.272396-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.26, subject=com.nexy.assistant,
default	21:54:53.273946-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.299395-0500	find_contacts_by_name_swift	[0xa3cc5c140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	21:54:53.300620-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	21:54:53.300676-0500	find_contacts_by_name_swift	<private> 0xa3d01c640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	21:54:53.300698-0500	find_contacts_by_name_swift	<private> 0xa3d01c640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	21:54:53.301470-0500	find_contacts_by_name_swift	[0xa3cc5c280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:54:53.302139-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49310.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	21:54:53.303384-0500	tccd	AUTHREQ_SUBJECT: msgID=49310.5, subject=com.nexy.assistant,
default	21:54:53.304076-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.321815-0500	find_contacts_by_name_swift	[0xa3cc5c280] invalidated after the last release of the connection object
default	21:54:53.321887-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	21:54:53.330159-0500	find_contacts_by_name_swift	[0xa3cc5c280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:54:53.331856-0500	find_contacts_by_name_swift	[0xa3cc5c280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.331898-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:54:53.332072-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	21:54:53.334456-0500	find_contacts_by_name_swift	[0xa3cc5ed00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.335412-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.921, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.335445-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.336764-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.921, subject=com.nexy.assistant,
default	21:54:53.337464-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.361619-0500	find_contacts_by_name_swift	[0xa3cc5ed00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.361702-0500	find_contacts_by_name_swift	[0xa3cc5ed00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.361773-0500	find_contacts_by_name_swift	[0xa3cc5ee40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.362654-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.922, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.362704-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.364051-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.922, subject=com.nexy.assistant,
default	21:54:53.364734-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.383512-0500	find_contacts_by_name_swift	[0xa3cc5ee40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.383569-0500	find_contacts_by_name_swift	[0xa3cc5ee40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.383615-0500	find_contacts_by_name_swift	[0xa3cc5ef80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.384349-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.923, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.384378-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.385637-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.923, subject=com.nexy.assistant,
default	21:54:53.386409-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.405040-0500	find_contacts_by_name_swift	[0xa3cc5ef80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.405107-0500	find_contacts_by_name_swift	[0xa3cc5ef80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.405157-0500	find_contacts_by_name_swift	[0xa3cc5f0c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.405929-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.924, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.405961-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.407104-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.924, subject=com.nexy.assistant,
default	21:54:53.407766-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.427176-0500	find_contacts_by_name_swift	[0xa3cc5f0c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.427231-0500	find_contacts_by_name_swift	[0xa3cc5f0c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.440555-0500	find_contacts_by_name_swift	Did add XPC store
default	21:54:53.440570-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:54:53.440668-0500	find_contacts_by_name_swift	[0xa3cc5f700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	21:54:53.442646-0500	find_contacts_by_name_swift	0xa3d0345e0: Using cached account information
default	21:54:53.442862-0500	find_contacts_by_name_swift	[0xa3cce14a0] Session created.
default	21:54:53.442871-0500	find_contacts_by_name_swift	[0xa3cce14a0] Session created with Mach Service: <private>
default	21:54:53.442877-0500	find_contacts_by_name_swift	[0xa3cc5f840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	21:54:53.442946-0500	find_contacts_by_name_swift	[0xa3cce14a0] Session activated
default	21:54:53.443003-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	21:54:53.448748-0500	find_contacts_by_name_swift	[0xa3cc5f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.448755-0500	find_contacts_by_name_swift	[0xa3cce14a0] Session canceled.
default	21:54:53.448771-0500	find_contacts_by_name_swift	[0xa3cce14a0] Disposing of session
default	21:54:53.449033-0500	find_contacts_by_name_swift	[0xa3cc5f840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:54:53.449701-0500	find_contacts_by_name_swift	[0xa3cc5f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.449717-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	21:54:53.449759-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	21:54:53.451910-0500	find_contacts_by_name_swift	[0xa3cdd6300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.457324-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.925, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.457355-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.459780-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.925, subject=com.nexy.assistant,
default	21:54:53.461216-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.480582-0500	find_contacts_by_name_swift	[0xa3cdd6300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.480638-0500	find_contacts_by_name_swift	[0xa3cdd6300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.480719-0500	find_contacts_by_name_swift	[0xa3cdd6440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.481692-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.926, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.481724-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.482935-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.926, subject=com.nexy.assistant,
default	21:54:53.483596-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.501559-0500	find_contacts_by_name_swift	[0xa3cdd6440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.501616-0500	find_contacts_by_name_swift	[0xa3cdd6440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.501672-0500	find_contacts_by_name_swift	[0xa3cdd6580] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.502451-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.927, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.502482-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.503612-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.927, subject=com.nexy.assistant,
default	21:54:53.504264-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.521447-0500	find_contacts_by_name_swift	[0xa3cdd6580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.521497-0500	find_contacts_by_name_swift	[0xa3cdd6580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.521542-0500	find_contacts_by_name_swift	[0xa3cdd66c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.522286-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.928, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.522326-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.523416-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.928, subject=com.nexy.assistant,
default	21:54:53.524075-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.542759-0500	find_contacts_by_name_swift	[0xa3cdd66c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.542821-0500	find_contacts_by_name_swift	[0xa3cdd66c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.548989-0500	find_contacts_by_name_swift	Did add XPC store
default	21:54:53.549017-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	21:54:53.549088-0500	find_contacts_by_name_swift	[0xa3cdd6940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	21:54:53.549633-0500	find_contacts_by_name_swift	[0xa3cdd6940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.549657-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:54:53.549671-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	21:54:53.551769-0500	find_contacts_by_name_swift	[0xa3cde9400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.552647-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.929, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.552690-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.554073-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.929, subject=com.nexy.assistant,
default	21:54:53.554788-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.573874-0500	find_contacts_by_name_swift	[0xa3cde9400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.573936-0500	find_contacts_by_name_swift	[0xa3cde9400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.573991-0500	find_contacts_by_name_swift	[0xa3cde9540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.574845-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.930, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.574877-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.576040-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.930, subject=com.nexy.assistant,
default	21:54:53.576714-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.598308-0500	find_contacts_by_name_swift	[0xa3cde9540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.598377-0500	find_contacts_by_name_swift	[0xa3cde9540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.598448-0500	find_contacts_by_name_swift	[0xa3cde9680] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.599493-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.931, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.599525-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.600913-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.931, subject=com.nexy.assistant,
default	21:54:53.601635-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.620486-0500	find_contacts_by_name_swift	[0xa3cde9680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.620553-0500	find_contacts_by_name_swift	[0xa3cde9680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.620613-0500	find_contacts_by_name_swift	[0xa3cde97c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	21:54:53.621476-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.932, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.621509-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.622756-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.932, subject=com.nexy.assistant,
default	21:54:53.623439-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.641211-0500	find_contacts_by_name_swift	[0xa3cde97c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.641257-0500	find_contacts_by_name_swift	[0xa3cde9900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:54:53.642244-0500	find_contacts_by_name_swift	Did add XPC store
default	21:54:53.642261-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	21:54:53.653529-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.933, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.653565-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.654931-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.933, subject=com.nexy.assistant,
default	21:54:53.655639-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.676666-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=29526.934, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	21:54:53.676698-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=29526, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=49310, auid=501, euid=501, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	21:54:53.678026-0500	tccd	AUTHREQ_SUBJECT: msgID=29526.934, subject=com.nexy.assistant,
default	21:54:53.678745-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x9bb307600 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.737566-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	21:54:53.737581-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	21:54:53.737684-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	21:54:53.745306-0500	find_contacts_by_name_swift	decoratedContacts called with 1 contacts
default	21:54:53.745326-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	21:54:53.745347-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	21:54:53.745352-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	21:54:53.745357-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	21:54:53.745373-0500	find_contacts_by_name_swift	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	21:54:53.745493-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	21:54:53.745527-0500	find_contacts_by_name_swift	0000 Time spent in client code: 105 µs
default	21:54:53.745543-0500	find_contacts_by_name_swift	0000 FINISH (504 ms)
default	21:54:53.745647-0500	find_contacts_by_name_swift	Entering exit handler.
default	21:54:53.745656-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	21:54:53.745697-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	21:54:53.745703-0500	find_contacts_by_name_swift	[0xa3cc5f700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:54:53.745713-0500	find_contacts_by_name_swift	Exiting exit handler.
default	21:54:53.745729-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	21:54:53.846550-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=49315.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=49315, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	21:54:53.849868-0500	tccd	AUTHREQ_SUBJECT: msgID=49315.1, subject=com.nexy.assistant,
default	21:54:53.850795-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110a700 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.872036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1650, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=48645, auid=501, euid=501, responsible_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy, binary_path=/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=49315, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:54:53.873064-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1650, subject=com.nexy.assistant,
default	21:54:53.873779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b11eb900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.953907-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b110b900 at /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app
default	21:54:53.987261-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 67080: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b6860100 b3c00f00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	21:54:54.006208-0500	tccd	target_executable_path_URL: file:///Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.app/Contents/MacOS/Nexy
default	21:54:59.287878-0500	kernel	tcp_connection_summary (tcp_drop:1453)[<IPv4-redacted>:51323<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063975 t_state: SYN_SENT process: Nexy:48645 Duration: 75.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 60 svc/tc: 0 flow: 0xa4baf598
default	21:54:59.287902-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51323<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 1063975 t_state: SYN_SENT process: Nexy:48645 flowctl: 0us (0x) SYN in/out: 0/11 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:54:59.369980-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:54:59.370115-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	21:54:59.914448-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:54:59.914717-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:55:01.029016-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
