default	21:50:41.672193-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 47821
default	21:50:43.280860-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 47830
default	21:50:54.314204-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 47861
default	21:50:54.314723-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 47861
default	21:50:57.811866-0500	loginwindow	VoiceOverDebug: _ScreenReaderToggleEnabled with option 72
default	21:50:57.829889-0500	UIKitSystem	Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001c22da16c _AXSApplicationAccessibilitySetEnabled + 84
	1   libAccessibility.dylib              0x00000001c22f2a40 _AXSVoiceOverTouchSetEnabled + 368
	2   FuseBoard                           0x00000002a09f742c -[FUAccessibilityServer _queue_applySettingWithKey:] + 696
	3   FuseBoard                           0x00000002a09f93ec __76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke + 708
	4   libdispatch.dylib                   0x000000019c9a8b5c _dispatch_call_block_and_release + 32
	5   libdispatch.dylib                   0x000000019c9c2ad4 _dispatch_client_callout + 16
	6   libdispatch.dylib                   0x000000019c9b14e8 _dispatch_lane_serial_drain + 740
	7   libdispatch.dylib                   0x000000019c9b1ff8 _dispatch_lane_invoke + 440
	8   libdispatch.dylib                   0x000000019c9b3308 _dispatch_workloop_invoke + 1612
	9   libdispatch.dylib                   0x000000019c9bc474 _dispa
default	21:50:57.813949-0500	loginwindow	VoiceOverDebug: after boostrap_look_up succeeded
default	21:50:57.813997-0500	loginwindow	VoiceOverDebug: calling _SCRStartup returned 0
default	21:50:58.062953-0500	VoiceOver	Requesting app group container lookup; personaid = 4294967295, type = NOPERSONA, name = <unknown>, origin [pid = 0, personaid = 0], proximate [pid = 0, personaid = 0], identifier = <private>, euid = 501, uid = 501, platform = 1
default	21:50:58.071417-0500	VoiceOver	Consumed sandbox extension; path = [<private>], handle = 0
default	21:50:58.071438-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	21:50:58.075336-0500	VoiceOver	[0x1010c2b40] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	21:50:58.075458-0500	VoiceOver	[0x1010c3080] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	21:50:58.448833-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=42732.9, attribution={responsible={TCCDProcess: identifier=com.apple.VoiceOver, pid=47902, auid=501, euid=501, responsible_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, accessing={TCCDProcess: identifier=com.apple.LegacyUserDefaultsConverter, pid=47903, auid=501, euid=501, binary_path=/System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/Resources/LegacyUserDefaultsConverter}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=42732, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	21:50:58.461200-0500	tccd	AUTHREQ_SUBJECT: msgID=42732.9, subject=com.apple.VoiceOver,
error	21:50:58.469084-0500	kernel	System Policy: LegacyUserDefaultsConverter(47903) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences/com.apple.VoiceOver4
error	21:50:58.469222-0500	kernel	System Policy: LegacyUserDefaultsConverter(47903) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	21:50:58.593312-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	21:50:58.668593-0500	VoiceOver	[0xb3ac683c0] activating connection: mach=false listener=false peer=false name=com.apple.carboncore.csnameddata
default	21:50:58.682982-0500	VoiceOver	VoiceOverDebug: ArgumentParser _initializeStartupOptions 72
default	21:50:58.686513-0500	VoiceOver	[0xb3ac68500] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	21:50:58.688852-0500	VoiceOver	[0xb3ac68640] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	21:50:58.704749-0500	VoiceOver	Received configuration update from daemon (initial)
default	21:50:58.712712-0500	VoiceOver	VoiceOverDebug: SCRWorkspace init
default	21:50:58.713620-0500	VoiceOver	[0xb3ac68a00] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	21:50:58.714349-0500	VoiceOver	[0xb3ac68b40] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	21:50:58.717864-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	21:50:58.718472-0500	VoiceOver	[0xb3ac68c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:50:58.719230-0500	VoiceOver	[0xb3ac68c80] invalidated after the last release of the connection object
default	21:50:58.719542-0500	VoiceOver	server port 0x00007f0b, session port 0x00007f0b
default	21:50:58.728600-0500	VoiceOver	New connection 0xfa7ef main
default	21:50:58.736025-0500	VoiceOver	CHECKIN: pid=47902
default	21:50:58.742230-0500	runningboardd	Resolved pid 47902 to [osservice<com.apple.VoiceOver(501)>:47902]
default	21:50:58.742938-0500	runningboardd	_bundleMatchesProcessWithExecutablePath using realpath and comparing /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver and /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOverStarter
default	21:50:58.743041-0500	VoiceOver	CHECKEDIN: pid=47902 asn=0x0-0x257257 foreground=0
default	21:50:58.743782-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] is not RunningBoard jetsam managed.
default	21:50:58.743803-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] This process will not be managed.
default	21:50:58.743844-0500	runningboardd	Now tracking process: [osservice<com.apple.VoiceOver(501)>:47902]
default	21:50:58.743583-0500	VoiceOver	[0xb3ac68c80] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	21:50:58.742830-0500	launchservicesd	CHECKIN:0x0-0x257257 47902 com.apple.VoiceOver
default	21:50:58.744668-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:47902" ID:394-357-48780 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:50:58.744766-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] reported to RB as running
default	21:50:58.744847-0500	runningboardd	Assertion 394-357-48780 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:50:58.744236-0500	VoiceOver	[0xb3ac68dc0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:50:58.744285-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:50:58.745640-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:47902" ID:394-357-48781 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:50:58.744766-0500	VoiceOver	[0xb3b49d680] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb3ac68dc0.peer[357].0xb3b49d680
default	21:50:58.745652-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:50:58.745788-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:50:58.745865-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Set darwin role to: UserInteractive
default	21:50:58.745920-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:50:58.746085-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:50:58.745805-0500	runningboardd	Assertion 394-357-48781 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:50:58.746131-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:50:58.746890-0500	VoiceOver	FRONTLOGGING: version 1
default	21:50:58.746901-0500	VoiceOver	Registered, pid=47902 ASN=0x0,0x257257
default	21:50:58.747308-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	21:50:58.747587-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae6211f40: VoiceOver> state 2
default	21:50:58.747628-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : VoiceOver
default	21:50:58.747910-0500	WindowServer	fa7ef[CreateApplication]: Process creation: 0x0-0x257257 (VoiceOver) connectionID: FA7EF pid: 47902 in session 0x101
default	21:50:58.748755-0500	VoiceOver	[0xb3ac68f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	21:50:58.750389-0500	gamepolicyd	Hit the server for a process handle 1cd190f30000bb1e that resolved to: [osservice<com.apple.VoiceOver(501)>:47902]
default	21:50:58.750446-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:50:58.750408-0500	runningboardd	Invalidating assertion 394-357-48780 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	21:50:58.752804-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:50:58.753515-0500	VoiceOver	BringForward: pid=47902 asn=0x0-0x257257 bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	21:50:58.754218-0500	VoiceOver	Current system appearance, (HLTB: 2), (SLS: 1)
default	21:50:58.755744-0500	VoiceOver	No persisted cache on this platform.
default	21:50:58.761044-0500	VoiceOver	Current system appearance, (HLTB: 2), (SLS: 1)
default	21:50:58.761590-0500	VoiceOver	Post-registration system appearance: (HLTB: 2)
default	21:50:58.761758-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 47902
default	21:50:58.762248-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 47902
default	21:50:58.762788-0500	VoiceOver	FBSWorkspace: endpoint monitoring is disabled.
default	21:50:58.762799-0500	VoiceOver	FBSWorkspace: default shell endpoint is disabled.
default	21:50:58.762881-0500	VoiceOver	Initializing connection
default	21:50:58.762932-0500	VoiceOver	Removing all cached process handles
default	21:50:58.762958-0500	VoiceOver	Sending handshake request attempt #1 to server
default	21:50:58.762965-0500	VoiceOver	Creating connection to com.apple.runningboard
default	21:50:58.762975-0500	VoiceOver	[0xb3ac69040] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	21:50:58.763741-0500	runningboardd	Setting client for [osservice<com.apple.VoiceOver(501)>:47902] as ready
default	21:50:58.764491-0500	VoiceOver	Handshake succeeded
default	21:50:58.764508-0500	VoiceOver	Identity resolved as osservice<com.apple.VoiceOver(501)>
default	21:50:58.764836-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:50:58.765868-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.apple.VoiceOver token: 1e0000001d pid: 47902
default	21:50:58.766215-0500	VoiceOver	[0xb3ac692c0] activating connection: mach=true listener=false peer=false name=com.apple.bird.token
default	21:50:58.769248-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:50:58.772430-0500	VoiceOver	Created a new Process Instance Registry XPC connection (inactive)
default	21:50:58.772543-0500	VoiceOver	[0xb3ac69180] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	21:50:58.772819-0500	VoiceOver	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	21:50:58.772924-0500	VoiceOver	[0xb3ac692c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:50:58.773264-0500	VoiceOver	[0xb3ac69540] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:50:58.774547-0500	VoiceOver	[0xb3ac69540] Connection returned listener port: 0x680f
default	21:50:58.775845-0500	VoiceOver	Registered process with identifier 47902-1029482
default	21:50:58.780066-0500	VoiceOver	[0xb3ac69680] activating connection: mach=true listener=false peer=false name=com.apple.AccessibilityVisualsAgent
default	21:50:58.782330-0500	VoiceOver	[0xb3ac692c0] activating connection: mach=true listener=false peer=false name=com.apple.bird
default	21:50:58.797418-0500	VoiceOver	[C:1] Alloc <private>
default	21:50:58.797502-0500	VoiceOver	[0xb3ac69900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:50:58.800055-0500	WindowManager	Connection activated | (47902) VoiceOver
default	21:50:58.815713-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.apple.VoiceOver token: 2100000023 pid: 47902
default	21:50:58.816294-0500	VoiceOver	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xb3b055360
 (
    "<NSDarkAquaAppearance: 0xb3b055220>",
    "<NSSystemAppearance: 0xb3b0552c0>"
)>
default	21:50:58.820638-0500	VoiceOver	[0xb3ac69e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	21:50:58.824204-0500	VoiceOver	[0xb3ac69f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	21:50:58.866664-0500	VoiceOver	[0xb3ac6a800] activating connection: mach=true listener=false peer=false name=com.apple.inputanalyticsd
default	21:50:58.897438-0500	VoiceOver	New connection 0xebc27 secondary
default	21:50:58.904227-0500	distnoted	register name: kVoiceOverSpeechBecameActiveNotification object: kCFNotificationAnyObject token: 270000002a pid: 47902
default	21:50:58.904383-0500	distnoted	register name: kVoiceOverSpeechBecameIdleNotification object: kCFNotificationAnyObject token: 2800000029 pid: 47902
default	21:50:58.913441-0500	VoiceOver	[0xb3ac6b200] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	21:50:58.950160-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	21:50:59.214721-0500	kernel	1 duplicate report for System Policy: LegacyUserDefaultsConverter(47903) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	21:50:59.548993-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	21:50:59.550684-0500	VoiceOver	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.apple.VoiceOver (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	21:50:59.552918-0500	VoiceOver	[0xb3ac6b340] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	21:50:59.560544-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver>
default	21:50:59.569986-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	21:50:59.572246-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOChatFlavor, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	21:50:59.572813-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	21:50:59.573113-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	21:50:59.573127-0500	VoiceOver	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	21:50:59.573468-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:50:59.574069-0500	VoiceOver	[0xb3ac6b480] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:50:59.574845-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=47902.2, attribution={requesting={TCCDProcess: identifier=com.apple.VoiceOver, pid=47902, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, },
default	21:50:59.584197-0500	tccd	AUTHREQ_SUBJECT: msgID=47902.2, subject=com.apple.VoiceOver,
default	21:50:59.587135-0500	VoiceOver	[0xb3ac6b480] invalidated after the last release of the connection object
default	21:50:59.587214-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:50:59.590790-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1142, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=47902, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:50:59.591581-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1142, subject=com.apple.VoiceOver,
default	21:50:59.592482-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x9bb288f00 at /System/Library/CoreServices/VoiceOver.app
error	21:50:59.606097-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.apple.VoiceOver, pid=47902, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	21:50:59.607629-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.1144, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=47902, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:50:59.608504-0500	tccd	AUTHREQ_SUBJECT: msgID=399.1144, subject=com.apple.VoiceOver,
default	21:50:59.609302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x9bb288f00 at /System/Library/CoreServices/VoiceOver.app
default	21:50:59.620884-0500	VoiceOver	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	21:50:59.621423-0500	VoiceOver	AddInstanceForFactory: No factory registered for id <CFUUID 0xb3b70a680> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	21:50:59.638849-0500	VoiceOver	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	21:50:59.638868-0500	VoiceOver	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	21:50:59.644351-0500	coreaudiod	>>> SIMULATE [com.apple.VoiceOver]
default	21:50:59.644798-0500	coreaudiod	<<< SIMULATE [com.apple.VoiceOver]
default	21:50:59.650410-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:50:59.652292-0500	VoiceOver	                AUHAL.cpp:420   AUHAL: (0x1010e4d40) Selecting device 85 from constructor
default	21:50:59.652304-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x1010e4d40)
default	21:50:59.652316-0500	VoiceOver	                AUHAL.cpp:681   SelectDevice: (0x1010e4d40) not already running
default	21:50:59.652323-0500	VoiceOver	                AUHAL.cpp:757   SelectDevice: (0x1010e4d40) nothing to teardown
default	21:50:59.652328-0500	VoiceOver	                AUHAL.cpp:762   SelectDevice: (0x1010e4d40) connecting device 85
default	21:50:59.652436-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:50:59.652543-0500	VoiceOver	                AUHAL.cpp:774   SelectDevice: (0x1010e4d40) created ioproc 0xa for device 85
default	21:50:59.652668-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x1010e4d40) adding 7 device listeners to device 85
default	21:50:59.652842-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x1010e4d40) adding 0 device delegate listeners to device 85
default	21:50:59.652852-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:50:59.652932-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:50:59.652944-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:50:59.652951-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:50:59.652964-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:50:59.652977-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:50:59.653090-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:50:59.653103-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:50:59.653109-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:50:59.653112-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x1010e4d40) removing 0 device listeners from device 0
default	21:50:59.653120-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x1010e4d40) removing 0 device delegate listeners from device 0
default	21:50:59.653126-0500	VoiceOver	                AUHAL.cpp:916   SelectDevice: <- (0x1010e4d40)
default	21:50:59.677959-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x1010e4d40) caller requesting device change from 85 to 85
default	21:50:59.677970-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x1010e4d40)
default	21:50:59.677974-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x1010e4d40) exiting with nothing to do
default	21:50:59.685467-0500	VoiceOver	[0xb3a4d0820] Session created.
default	21:50:59.685477-0500	VoiceOver	[0xb3a4d0820] Session created with Mach Service: <private>
default	21:50:59.685499-0500	VoiceOver	[0xb3ac6b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	21:50:59.685570-0500	VoiceOver	[0xb3a4d0820] Session activated
default	21:51:00.489145-0500	VoiceOver	[0xb3a4d0eb0] Session created.
default	21:51:00.489157-0500	VoiceOver	[0xb3a4d0eb0] Session created with Mach Service: <private>
default	21:51:00.489168-0500	VoiceOver	[0xb3a71b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	21:51:00.489299-0500	VoiceOver	[0xb3a4d0eb0] Session activated
default	21:51:00.510075-0500	VoiceOver	[0xb3a4d0f00] Session created.
default	21:51:00.510088-0500	VoiceOver	[0xb3a4d0f00] Session created with Mach Service: <private>
default	21:51:00.510097-0500	VoiceOver	[0xb3a700140] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	21:51:00.510179-0500	VoiceOver	[0xb3a4d0f00] Session activated
error	21:51:00.633874-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.646235-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.646281-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.650795-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.650827-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.746417-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.746454-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.805305-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	21:51:00.805350-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
default	21:51:00.820943-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:00.822556-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:00.823283-0500	VoiceOver	       ACv2Workarounds.mm:51    com.apple.VoiceOver: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	21:51:00.823349-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	21:51:00.823504-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3a787390, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:00.823556-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:00.824135-0500	VoiceOver	[0xb3a70c280] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	21:51:00.829345-0500	VoiceOver	LFSMCopySessionAgentEndpoint: enter
default	21:51:00.829535-0500	VoiceOver	[0xb3a70c000] activating connection: mach=true listener=false peer=false name=com.apple.logind
default	21:51:00.830609-0500	VoiceOver	LFSMCopySessionAgentEndpoint: exit: result = 0
default	21:51:00.830750-0500	VoiceOver	[0xb3a70c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:51:00.831235-0500	VoiceOver	[SCROBrailleClient setDelegate:<SCROutputBrailleComponent: 0xb3b058f00>]
default	21:51:00.831278-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	21:51:00.831619-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:00.831726-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:00.833262-0500	VoiceOver	[0xb3a70c640] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	21:51:00.834487-0500	VoiceOver	[0xb3a70c8c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:51:00.835206-0500	VoiceOver	[0xb3a70c8c0] invalidated after the last release of the connection object
default	21:51:00.835350-0500	VoiceOver	server port 0x0001ec13, session port 0x00007f0b
default	21:51:00.837826-0500	VoiceOver	[0xb3a70c8c0] activating connection: mach=true listener=false peer=false name=com.apple.backlightd
default	21:51:00.844985-0500	WindowServer	Connection added: IOHIDEventSystemConnection uuid:E981861D-2254-4508-B4D2-6E05614B1063 pid:47902 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x0 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	21:51:00.847763-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	21:51:00.847842-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	21:51:00.847858-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:00.848304-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:00.848381-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:00.853512-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 6700000061 pid: 47902
default	21:51:00.854032-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	21:51:00.854098-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	21:51:00.854111-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:00.854500-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:00.854561-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:00.854676-0500	VoiceOver	'Dock' is running
default	21:51:00.854933-0500	VoiceOver	'Setup Assistant' is not running
default	21:51:00.857769-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x1010e4d40) caller requesting device change from 85 to 85
default	21:51:00.857779-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x1010e4d40)
default	21:51:00.857788-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x1010e4d40) exiting with nothing to do
default	21:51:00.872931-0500	VoiceOver	[0xb3a70d040] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:51:00.873941-0500	VoiceOver	[0xb3a70d040] invalidated after the last release of the connection object
default	21:51:00.900100-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:51:00.900636-0500	VoiceOver	[0xb3a70d040] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	21:51:00.901297-0500	VoiceOver	SignalReady: pid=47902 asn=0x0-0x257257
default	21:51:00.901755-0500	VoiceOver	SIGNAL: pid=47902 asn=0x0x-0x257257
default	21:51:00.902570-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	21:51:00.914170-0500	distnoted	register name: AXSSVoiceOverPunctuationCloudKitUpdateNotification object: kCFNotificationAnyObject token: 6800000060 pid: 47902
default	21:51:00.914762-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	21:51:00.914783-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	21:51:00.924120-0500	VoiceOver	[0xb3ac68dc0] Connection returned listener port: 0x7603
default	21:51:00.952780-0500	VoiceOver	[SCROBrailleClient handleCallback:] for key CallbackConnect
default	21:51:00.953095-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	21:51:01.000801-0500	VoiceOver	IOMainPort returned 0
default	21:51:01.001785-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	21:51:01.001816-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	21:51:01.010608-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:51:01.010617-0500	VoiceOver	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	21:51:01.010632-0500	VoiceOver	[0xb3a70d680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	21:51:01.010703-0500	VoiceOver	[0xb3a70d680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:51:01.011046-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:51:01.030945-0500	VoiceOver	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	21:51:01.031608-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) No windows open yet
default	21:51:01.044931-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-48783 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:01.045010-0500	runningboardd	Assertion 394-387-48783 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:01.037961-0500	VoiceOver	sConnectionName: com.apple.spotlight.IndexAgent
default	21:51:01.042292-0500	VoiceOver	Start service name com.apple.spotlight.IndexAgent
default	21:51:01.042431-0500	VoiceOver	[0xb3a70d540] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	21:51:01.047441-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:51:01.047632-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:51:01.047801-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:51:01.047965-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:51:01.048012-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:51:01.052512-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppVisible" ID:394-387-48784 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:01.052575-0500	runningboardd	Assertion 394-387-48784 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:01.052656-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:51:01.052830-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:51:01.052840-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:51:01.052850-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:51:01.052887-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:51:01.052913-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:51:01.053642-0500	VoiceOver	registering darwin observer for name: com.apple.gms.availability.notification
default	21:51:01.053674-0500	VoiceOver	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	21:51:01.053697-0500	VoiceOver	registering darwin observer for name: com.apple.language.changed
default	21:51:01.053723-0500	VoiceOver	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	21:51:01.120424-0500	VoiceOver	New connection 0x853a3 secondary
default	21:51:01.128520-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.apple.VoiceOver: <private>
default	21:51:01.157527-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:51:01.390722-0500	VoiceOver	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	21:51:01.393114-0500	VoiceOver	Start service name com.apple.spotlightknowledged
default	21:51:01.394464-0500	VoiceOver	[GMS] availability notification token 312
default	21:51:01.910386-0500	VoiceOver	No list of permitted front apps returned
default	21:51:01.911370-0500	VoiceOver	No list of permitted front apps returned
default	21:51:01.911456-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:01.912137-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:01.912312-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:01.928426-0500	VoiceOver	[0xb39c91f90] Session created.
default	21:51:01.928437-0500	VoiceOver	[0xb39c91f90] Session created with Mach Service: <private>
default	21:51:01.928447-0500	VoiceOver	[0xb3a70db80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	21:51:01.928536-0500	VoiceOver	[0xb39c91f90] Session activated
default	21:51:02.009038-0500	VoiceOver	[0xb3a70c780] activating connection: mach=true listener=false peer=false name=com.apple.pbs.fetch_services
default	21:51:02.009601-0500	VoiceOver	[0xb3a70c780] invalidated after the last release of the connection object
default	21:51:02.027852-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:02.027939-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.031640-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39dd0540, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:02.031682-0500	VoiceOver	AudioConverter -> 0xb39dd0540: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:02.031691-0500	VoiceOver	AudioConverter -> 0xb39dd0540: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:02.032766-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48785 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:02.032835-0500	runningboardd	Assertion 394-47902-48785 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:02.033569-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:51:02.033626-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:51:02.033670-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:51:02.033814-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48786 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:02.033817-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:51:02.033896-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:51:02.033912-0500	runningboardd	Assertion 394-328-48786 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:02.036442-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:51:02.036454-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:51:02.036490-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:51:02.036536-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:51:02.036562-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:51:02.036773-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:51:02.039190-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:51:02.067336-0500	VoiceOver	[0xb39e603c0] Session created.
default	21:51:02.067343-0500	VoiceOver	[0xb39e603c0] Session created with Mach Service: <private>
default	21:51:02.067353-0500	VoiceOver	[0xb3a70d680] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	21:51:02.067429-0500	VoiceOver	[0xb39e603c0] Session activated
default	21:51:02.068516-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474872718 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:02.130094-0500	VoiceOver	AudioComponentPluginMgr.mm:114   registrationsChanged
default	21:51:02.132508-0500	VoiceOver	AudioComponentPluginMgr.mm:906   First wildcard component search: 0/0/0
default	21:51:02.135267-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.151698-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.152240-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.152374-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.152398-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.152539-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.152594-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.152731-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.152812-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.152930-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153016-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.153137-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153175-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.153290-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153328-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.153465-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153502-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.153624-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153732-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.153847-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.153907-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154015-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154069-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154175-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154227-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154347-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154391-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154499-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154546-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154655-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154692-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154808-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154855-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.154961-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.154998-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155105-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155145-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155256-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155301-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155407-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155440-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155548-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155607-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155720-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155755-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.155863-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.155884-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156003-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156064-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156168-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156208-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156313-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156336-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156444-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156478-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156598-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156637-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156747-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156783-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.156893-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.156933-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157042-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.157077-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157187-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.157210-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157318-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.157345-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157459-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.157483-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157587-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.157610-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157716-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.157766-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157872-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.157893-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.157999-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158051-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158150-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158180-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158287-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158313-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158426-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158453-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158556-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158585-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158687-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158716-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158824-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158857-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.158967-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.158987-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159096-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159152-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159255-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159286-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159395-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159445-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159545-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159568-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159671-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159699-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159805-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159832-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.159934-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.159951-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160054-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.160085-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160196-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.160217-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160325-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.160360-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160469-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.160502-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160609-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.160645-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160762-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.160794-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.160901-0500	VoiceOver	[0xb3a70c3c0] invalidated after the last release of the connection object
default	21:51:02.162116-0500	VoiceOver	Class EXGetExtensionClass(void) returning EXConcreteExtension
default	21:51:02.162147-0500	VoiceOver	[0xb3a70c3c0] activating connection: mach=true listener=false peer=false name=com.apple.pluginkit.pkd
default	21:51:02.162295-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Beginning discovery for flags: 1024, point: (null)
default	21:51:02.163773-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Completed discovery. Final # of matches: 1
default	21:51:02.164700-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.164813-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.164849-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Beginning discovery for flags: 1024, point: (null)
default	21:51:02.165518-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Completed discovery. Final # of matches: 1
default	21:51:02.166943-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.167062-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.167104-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Beginning discovery for flags: 1024, point: (null)
default	21:51:02.167788-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Completed discovery. Final # of matches: 1
default	21:51:02.169204-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.169342-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.169382-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Beginning discovery for flags: 1024, point: (null)
default	21:51:02.170017-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Completed discovery. Final # of matches: 1
default	21:51:02.170866-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.170990-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.171031-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Beginning discovery for flags: 1024, point: (null)
default	21:51:02.171845-0500	VoiceOver	[d <private>] <PKHost:0xb39c58e00> Completed discovery. Final # of matches: 1
default	21:51:02.172492-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.172625-0500	VoiceOver	[0xb3a70d2c0] invalidated after the last release of the connection object
default	21:51:02.188719-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Ready plugins sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	21:51:02.194011-0500	runningboardd	Launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}[0] is using uid 501 (divined from auid 501 euid 501)
default	21:51:02.194057-0500	runningboardd	Executing launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]} (Launching extension com.apple.ax.MauiTTSSupport.MauiAUSP(14844CB3-B750-5F5A-987A-D4BBC31613B5) for host 47902) from requestor: [osservice<com.apple.pluginkit.pkd(501)>:47466]
default	21:51:02.194116-0500	runningboardd	Creating and launching job for: xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	21:51:02.194279-0500	runningboardd	'(null)' Submitting extension overlay (host PID 47902, path /System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP):
<dictionary: 0x7bd307540> { count = 3, transaction: 0, voucher = 0x0, contents =
	"XPCService" => <dictionary: 0x7bd307600> { count = 11, transaction: 0, voucher = 0x0, contents =
		"_ManagedBy" => <string: 0x7bd9fcf90> { string cache = 0x0, length = 22, contents = "com.apple.runningboard" }
		"RunLoopType" => <string: 0x7bd9fd0e0> { string cache = 0x0, length = 9, contents = "NSRunLoop" }
		"Platform" => <int64: 0x8a1fe6cfd66b5eff>: 1
		"JoinExistingSession" => <bool: 0x20b06f830>: true
		"_SandboxProfile" => <string: 0x7bd9fd620> { string cache = 0x0, length = 6, contents = "plugin" }
		"_AdditionalSubServices" => <dictionary: 0x7bdab5b00> { count = 1, transaction: 0, voucher = 0x0, contents =
			"apple-extension-service" => <bool: 0x20b06f830>: true
		}
		"PersonaEnterprise" => <int64: 0x8a1fe6cfd66b41bf>: 1001
		"_AdditionalProperties" => <dictionary: 0x7bdab54a0> { count = 1, transaction: 0, voucher = 0x0, contents =
			"RunningBoard" => <dictionary: 0x7bdab5da0> { count = 2, transaction: 0, voucher = 0x0, contents =
				"RunningBoardLaunchedIdentity" => <dictionary: 0x7bdab6be0> { count = 6, transaction: 0, voucher = 0x0, contents =
					"e" => <int64: 0x8a1fe6cfd66b515f>: 501
					"TYPE" => <int64: 0x8a1fe6cfd66b5ed7>: 4
					"h" => <int64: 0x8a1fe6cfd66e8607>: 47902
					"i" => <string: 0x7bd9fd410> { string cache = 0x0, length = 36, contents = "com.apple.ax.MauiTTSSupport.MauiAUSP" }
					"r" => <int64: 0x8a1fe6cfd66b5ee7>: 2
					"H" => <dictionary: 0x7bdad94a0> { count = 5, transaction: 0, voucher = 0x0, contents =
						"l" => <string: 0x7bd9fc750> { string cache = 0x0, length = 19, contents = "com.apple.VoiceOver" }
						"t" => <int64: 0x8a1fe6cfd66b5ee7>: 2
						"TYPE" => <int64: 0x8a1fe6cfd66b5ec7>: 6
						"a" => <int64: 0x8a1fe6cfd66b515f>: 501
						"p" => <int64: 0x8a1fe6cfd66b5ef7>: 0
					}
				}
				"RunningBoardLaunched" => <bool: 0x20b06f830>: true
			}
		}
		"_OmitSandboxParameters" => <bool: 0x20b06f830>: true
		"ServiceType" => <string: 0x7bd9fe6d0> { string cache = 0x0, length = 11, contents = "Application" }
		"ProgramArguments" => <array: 0x7bd9ff900> { count = 3, capacity = 8, contents =
			0: <string: 0x7bd9fca20> { string cache = 0x0, length = 125, contents = "/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP" }
			1: <string: 0x7bd9fc4b0> { string cache = 0x0, length = 15, contents = "-AppleLanguages" }
			2: <string: 0x7bd9fc390> { string cache = 0x0, length = 27, contents = "("en-CA", "ru-CA", "fr-CA")" }
		}
	}
	"RunningBoard" => <dictionary: 0x7bd304900> { count = 1, transaction: 0, voucher = 0x0, contents =
		"Managed" => <bool: 0x20b06f830>: true
	}
	"CFBundlePackageType" => <string: 0x7bd9ffb70> { string cache = 0x0, length = 4, contents = "XPC!" }
}
default	21:51:02.204976-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Memory Limits: active 0 inactive 0
 <private>
default	21:51:02.204996-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] This process will be managed.
error	21:51:02.205017-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Memorystatus failed with unexpected error: Invalid argument (22)
default	21:51:02.205027-0500	runningboardd	Now tracking process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.205204-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-suspended (role: None) (endowments: (null))
default	21:51:02.205404-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] reported to RB as running
default	21:51:02.205593-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] got pid from ready request: 47925
default	21:51:02.205950-0500	WindowServer	Hit the server for a process handle 6d7259b0000bb35 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.206002-0500	WindowServer	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	21:51:02.206351-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:394-47902-48787 target:47925 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	21:51:02.206402-0500	gamepolicyd	Hit the server for a process handle 6d7259b0000bb35 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.206412-0500	runningboardd	Assertion 394-47902-48787 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]) will be created as active
default	21:51:02.206470-0500	gamepolicyd	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	21:51:02.206790-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Set jetsam priority to 40 [0] flag[1]
default	21:51:02.206804-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Resuming task.
default	21:51:02.206825-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Result 45 setting darwin role to UserInteractiveNonFocal: Operation not supported, falling back to setting priority
default	21:51:02.206842-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Set darwin priority to: PRIO_DEFAULT
default	21:51:02.206989-0500	UIKitSystem	Hit the server for a process handle 6d7259b0000bb35 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.207077-0500	UIKitSystem	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	21:51:02.207027-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] prevented from droping Memory Limits from 0 to -1
default	21:51:02.209801-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-active (role: UserInteractiveNonFocal) (endowments: (null))
default	21:51:02.209955-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] acquired startup assertion
default	21:51:02.210074-0500	WindowServer	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	21:51:02.210158-0500	UIKitSystem	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	21:51:02.210269-0500	VoiceOver	Creating side-channel connection to com.apple.runningboard
default	21:51:02.210221-0500	gamepolicyd	Received state update for 47925 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	21:51:02.210278-0500	VoiceOver	[0xb3a70d180] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	21:51:02.210735-0500	VoiceOver	Hit the server for a process handle 6d7259b0000bb35 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.210877-0500	VoiceOver	[0xb3a70d2c0] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP
default	21:51:02.210933-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Prepare using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	21:51:02.210952-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5] [<private>(<private>)] Sending prepareUsing to managed extension; this should launch it if not already running.
default	21:51:02.229652-0500	runningboardd	Setting client for [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] as ready
default	21:51:02.230345-0500	MauiAUSP	Identity resolved as xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	21:51:02.236577-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Begin using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	21:51:02.236815-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin loaded and ready for host
default	21:51:02.237104-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:394-47902-48788 target:47925 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown WantsForegroundResourcePriority )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	21:51:02.237163-0500	runningboardd	Assertion 394-47902-48788 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]) will be created as active
default	21:51:02.237562-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] Set jetsam priority to 100 [0] flag[1]
default	21:51:02.237709-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] prevented from droping Memory Limits from 0 to -1
default	21:51:02.240550-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] invalidating startup assertion
default	21:51:02.240660-0500	runningboardd	Invalidating assertion 394-47902-48787 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:02.241008-0500	VoiceOver	Class EXGetExtensionContextInternalClass(void) returning EXExtensionContextImplementation
default	21:51:02.247960-0500	VoiceOver	[0xb3a70cb40] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:51:02.248519-0500	VoiceOver	[0xb3c532e80] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service
default	21:51:02.248677-0500	VoiceOver	[0xb3a70cb40] Connection returned listener port: 0x2d833
default	21:51:02.296101-0500	VoiceOver	[0xb3c533000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb3a70cb40.peer[47925].0xb3c533000
default	21:51:02.296576-0500	VoiceOver	[0xb3a70c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.AUCrashHandlerService
default	21:51:02.309446-0500	VoiceOver	   AUOOPRenderPipePool.mm:167   Host obtained render pipe 196300985
default	21:51:02.309508-0500	VoiceOver	       AUOOPWorkgroups.mm:66    AUOOPWorkgroupManager: mutating workgroups.
default	21:51:02.334650-0500	VoiceOver	[0xb3a70c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	21:51:02.334691-0500	VoiceOver	        AUCrashHandler.mm:126   invalidated
default	21:51:02.473547-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:51:02.518690-0500	VoiceOver	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	21:51:02.518883-0500	VoiceOver	       AUOOPWorkgroups.mm:308   AUOOPWorkgroupManager: propagating workgroups.
default	21:51:02.518901-0500	VoiceOver	       AUOOPWorkgroups.mm:343   AUOOPWorkgroupManager: notifying workgroup listeners. Added :10, removed: 0
default	21:51:02.519323-0500	VoiceOver	[0xb3a70d7c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	21:51:02.521486-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"PID":47902,"session_type":"Primary"} }
default	21:51:02.521620-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:51:02.522628-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 47902, name = VoiceOver
default	21:51:02.523001-0500	VoiceOver	    SessionCore_Create.mm:99    Created session 0xb3ad34520 with ID: 0x1ea040
error	21:51:02.523482-0500	VoiceOver	Reporter disconnected. { function=sendMessage, reporterID=205737523412994 }
default	21:51:02.523521-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:02.524398-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:51:02.524525-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:51:02.524589-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:51:02.524637-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea040, VoiceOver(47902), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:51:02.524708-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:51:02.524708-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.524719-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 starting playing
default	21:51:02.525316-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:51:02.525358-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:51:02.525387-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'}
default	21:51:02.525474-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:51:02.525610-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:51:02.525628-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:51:02.525496-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	21:51:02.526017-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.526088-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.526169-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:51:02.526665-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	21:51:02.526961-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.527072-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.527100-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:51:02.527115-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	21:51:02.527122-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	21:51:02.527133-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
error	21:51:02.527199-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:02.527273-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:51:02.539144-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	21:51:02.539513-0500	VoiceOver	[0xb3a70d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.539921-0500	VoiceOver	[0xb3a70d900] invalidated after the last release of the connection object
default	21:51:02.540039-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.540276-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.540431-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.540718-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.540841-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	21:51:02.541101-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.541256-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.541430-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.541656-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.541754-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.541940-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.542141-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.542108-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3a1ca610, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:02.542294-0500	VoiceOver	AudioConverter -> 0xb3a1ca610: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:02.542320-0500	VoiceOver	AudioConverter -> 0xb3a1ca610: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:02.542371-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.542520-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.542885-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.542917-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.543123-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.543381-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.543576-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.543673-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.543847-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.543905-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.544064-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.544188-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.544327-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.544358-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.544522-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.544549-0500	VoiceOver	[0xb3a70df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	21:51:02.544697-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:02.826833-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:394-47925-48790 target:47925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	21:51:02.826930-0500	runningboardd	Assertion 394-47925-48790 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]) will be created as inactive as start-time-defining assertions exist
default	21:51:02.832449-0500	runningboardd	Invalidating assertion 394-47925-48790 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925]
default	21:51:02.973251-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3a1c9ce0, from  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32) to  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32)
default	21:51:02.973437-0500	VoiceOver	     AudioQueueObject.cpp:487   AudioQueueObject: aq@0xb3ac8a800: New output; format  1 ch,  22050 Hz, Float32 (passthrough? no)
default	21:51:02.975306-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0xb3c302120 created for movie spatialization.
default	21:51:02.975317-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0xb3c3035c0 created for music spatialization.
default	21:51:02.977108-0500	VoiceOver	           AQMEIO_HAL.cpp:2218  [AddSpatialPropertiesListener] objectID=85
default	21:51:02.977174-0500	VoiceOver	           AQMEIO_HAL.cpp:2240  aqmeio@0xb3aa2e418: [AddSpatialPropertiesListener] Installed listener 0xb3a802e80
default	21:51:02.977566-0500	VoiceOver	          AQMixEngine.cpp:733   AQMEDevice (0xb3c51c058) has neither a defaultOutStreamClient nor a defaultInStreamClient
default	21:51:02.979681-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	21:51:02.979777-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	21:51:02.980015-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3a1c9500, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:02.983113-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xb3ac8a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	21:51:02.983135-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xb3ac8a800:
default	21:51:02.983161-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	21:51:02.983167-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	21:51:02.983177-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	21:51:02.984473-0500	VoiceOver	       LoudnessManager.mm:1257  GetHardwarePlatformKey: found acoustic ID: 37
default	21:51:02.984483-0500	VoiceOver	       LoudnessManager.mm:1387  GetHardwarePlatformKey: GetHardwarePlatformKey(): hardware platform key is Mac
default	21:51:02.984556-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	21:51:02.984571-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	21:51:02.990370-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:51:02.990909-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:02.991123-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:02.993133-0500	VoiceOver	SpatializationManager.cpp:1418  Loaded preset file /System/Library/Audio/Tunings/AID37/AU/aid37-aumx-3dem-appl.aupreset
default	21:51:02.993582-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:02.993828-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:02.993849-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:02.993963-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:02.994879-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:02.995047-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	21:51:02.995090-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:02.995286-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:02.995374-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:02.998909-0500	VoiceOver	           AQMEIO_HAL.cpp:1922  user headtracking mode for app com.apple.VoiceOver: 1
default	21:51:03.009524-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 26472 ioTS st: 26472 ht: 47601.428521
error	21:51:03.080176-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:03.817640-0500	VoiceOver	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	21:51:04.029902-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:07.029911-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:09.336900-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:07  id:21474872718 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:09.336253-0500	VoiceOver	LSExceptions shared instance invalidated for timeout.
default	21:51:09.339631-0500	VoiceOver	HIDAnalytics Set Value Send event com.apple.iokituser.hid.iohidpostevent
default	21:51:09.339656-0500	VoiceOver	HIDAnalytics Timer Send event com.apple.iokituser.hid.iohidpostevent
default	21:51:09.339756-0500	VoiceOver	HIDAnalytics Unregister Send event com.apple.iokituser.hid.iohidpostevent
default	21:51:09.548136-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:51:09.861700-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474872722 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:09.862030-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:51:09.974359-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:10.029731-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:12.022295-0500	VoiceOver	[0xb3a70d900] activating connection: mach=true listener=false peer=false name=mul-xpc (Apple)_OpenStep
default	21:51:12.022661-0500	VoiceOver	[0xb3a70de00] activating connection: mach=true listener=false peer=false name=com.apple.naturallanguaged
default	21:51:13.029810-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:14.747463-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:14.747616-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
fault	21:51:15.769351-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:15.771430-0500	VoiceOver	No list of permitted front apps returned
default	21:51:15.864700-0500	VoiceOver	No list of permitted front apps returned
default	21:51:15.875751-0500	VoiceOver	No list of permitted front apps returned
default	21:51:15.880085-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cdf9c0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:15.880108-0500	VoiceOver	AudioConverter -> 0xb39cdf9c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:15.880120-0500	VoiceOver	AudioConverter -> 0xb39cdf9c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:15.883907-0500	VoiceOver	No list of permitted front apps returned
default	21:51:15.886014-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:15.886672-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:15.886754-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:15.909476-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:15.909638-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:15.944905-0500	VoiceOver	[0xb3a70df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:15.945029-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:15.947213-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39e54690, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:15.947238-0500	VoiceOver	AudioConverter -> 0xb39e54690: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:15.947288-0500	VoiceOver	AudioConverter -> 0xb39e54690: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:15.953033-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:15.953067-0500	VoiceOver	CoreText note: Set a breakpoint on CTFontLogSystemFontNameRequest to debug.
default	21:51:15.961935-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:15.965948-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	21:51:15.970395-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:15.970431-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:15.972484-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474872722 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:15.973042-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474872740 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:16.013695-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:51:16.013988-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:16.014267-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:16.014327-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:16.014508-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:16.014534-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:16.014564-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:16.014739-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:16.014791-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	21:51:16.014820-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:16.015029-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:16.015047-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:16.029712-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:16.033456-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 313651 ioTS st: 313651 ht: 47614.452521
error	21:51:16.153506-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:17.698827-0500	VoiceOver	No list of permitted front apps returned
fault	21:51:17.701992-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:17.723937-0500	VoiceOver	No list of permitted front apps returned
default	21:51:17.724217-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:17.725368-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:17.725513-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:17.759226-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	21:51:17.761836-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:17.761904-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:17.800066-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:17.800388-0500	VoiceOver	No list of permitted front apps returned
fault	21:51:17.800350-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
error	21:51:17.821851-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:17.903997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
fault	21:51:17.904659-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:17.905880-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:17.907645-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:51:17.908452-0500	runningboardd	Invalidating assertion 394-47902-48785 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:17.907675-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:51:17.907681-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:51:17.907818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:17.907881-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:17.919508-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:17.919533-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:17.919962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:17.920068-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:17.920118-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:17.921530-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:17.921127-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:17.921612-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:17.921627-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:17.921675-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:17.921698-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:17.921993-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:51:17.922873-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:51:17.923121-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:51:17.931406-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:17.931472-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:17.932563-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:2894 called from <private>
default	21:51:17.932605-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:2894 called from <private>
default	21:51:17.932686-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:17.936764-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:17.936999-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:2894 called from <private>
default	21:51:17.937041-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:2894 called from <private>
default	21:51:17.937120-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:17.944896-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:17.945209-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:17.945219-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:17.945256-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:17.945269-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:17.945296-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:17.946322-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:17.946372-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:17.946583-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:17.946645-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:17.946683-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:17.946737-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:17.946765-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:17.947326-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
error	21:51:17.947326-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:17.947434-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:51:17.947586-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:17.947689-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:17.947763-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:17.947808-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:17.947846-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccf690, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	21:51:17.947894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:17.947942-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:17.947943-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:17.947971-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:17.948015-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:17.948046-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:17.948075-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:17.948121-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:17.949064-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:17.947808-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48802 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:17.950764-0500	runningboardd	Assertion 394-47902-48802 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:17.949110-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
error	21:51:17.950427-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:17.953495-0500	runningboardd	Invalidating assertion 394-47902-48802 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:17.950787-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:51:17.950951-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:17.951137-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:17.953756-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48803 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:17.953847-0500	runningboardd	Assertion 394-47902-48803 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:17.954516-0500	runningboardd	Invalidating assertion 394-47902-48803 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
fault	21:51:17.972798-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:17.969074-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
error	21:51:17.971615-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:17.969101-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:17.969130-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:17.981295-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:51:17.982080-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccebb0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	21:51:17.982701-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:17.983011-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:17.986238-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:17.986373-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:17.981466-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:51:17.981930-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:51:18.040026-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
fault	21:51:18.564066-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:18.564598-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:18.565701-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:18.566149-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:18.901726-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474872741 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:19.031505-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:19.114355-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:51:19.501158-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:19.520957-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:19.521080-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:20.698430-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.699810-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:51:20.699860-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:51:20.699875-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:51:20.702147-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:20.702228-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:20.703790-0500	runningboardd	Invalidating assertion 394-47902-48806 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:20.703994-0500	runningboardd	Invalidating assertion 394-328-48786 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:51:20.708970-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:20.712697-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:51:20.712755-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:51:20.712764-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:51:20.713216-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:20.713231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:20.713783-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.713814-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:20.713820-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:20.716872-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.716922-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.716937-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.717130-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:20.717144-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:20.728390-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:20.728427-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:20.730097-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:2894 called from <private>
default	21:51:20.730120-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:2894 called from <private>
default	21:51:20.730227-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.734901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.735224-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:2894 called from <private>
default	21:51:20.735235-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:2894 called from <private>
default	21:51:20.735435-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.744292-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.744684-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:20.744709-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:20.744813-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:20.744822-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:20.745337-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
error	21:51:20.746237-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:20.746273-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:51:20.746329-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:20.746376-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:20.746462-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:20.746540-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:20.746547-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:20.746575-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:20.746608-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:20.746690-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:20.746962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:20.747101-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:20.748743-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.749227-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.749232-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:20.749589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.753343-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48808 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:20.750104-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:20.753500-0500	runningboardd	Assertion 394-47902-48808 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:20.750616-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:20.752648-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:20.752948-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:20.755341-0500	runningboardd	Invalidating assertion 394-47902-48808 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:20.755670-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:20.756761-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48809 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:20.756948-0500	runningboardd	Assertion 394-47902-48809 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:20.755795-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:20.755853-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:20.756261-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:20.756334-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	21:51:20.797544-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:21.215400-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:51:21.260519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:51:21.260545-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2894 called from <private>
default	21:51:21.261956-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:21.261970-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:21.262336-0500	runningboardd	Invalidating assertion 394-47902-48809 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:21.262933-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48819 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:21.263001-0500	runningboardd	Assertion 394-47902-48819 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:21.263767-0500	runningboardd	Invalidating assertion 394-328-48810 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:51:21.264348-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48820 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:21.264436-0500	runningboardd	Assertion 394-328-48820 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:21.262475-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccf450, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:21.262902-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
error	21:51:21.265640-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:21.832201-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:51:21.875087-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:51:21.875241-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2894 called from <private>
default	21:51:21.875442-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:21.877403-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:21.877422-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:21.877547-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:21.878253-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:21.878268-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:21.878277-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:21.878906-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:21.879137-0500	runningboardd	Invalidating assertion 394-47902-48819 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:21.878937-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:21.879055-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:21.879235-0500	runningboardd	Invalidating assertion 394-328-48820 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:51:21.879473-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48821 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:21.879623-0500	runningboardd	Assertion 394-47902-48821 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:21.880415-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-48822 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:51:21.880526-0500	runningboardd	Assertion 394-328-48822 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:21.879089-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:21.879117-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
error	21:51:21.881947-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:21.879218-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:21.879252-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:21.946644-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:22.391196-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:51:22.435388-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:51:22.436233-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccf450, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:22.436271-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:22.436383-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:22.436724-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:22.436858-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:22.436881-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:22.436891-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:22.436913-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:51:22.436925-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:51:22.437546-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccebb0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:22.437812-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xb3ac8a800:
default	21:51:22.437870-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	21:51:22.437880-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	21:51:22.437897-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	21:51:22.437927-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	21:51:22.437951-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	21:51:22.438312-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xb3ac8a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	21:51:22.445774-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:22.445794-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:51:22.446208-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:25.029742-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:27.963937-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:29.121979-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ccdef0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:29.122009-0500	VoiceOver	AudioConverter -> 0xb39ccdef0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:29.122030-0500	VoiceOver	AudioConverter -> 0xb39ccdef0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:29.127722-0500	VoiceOver	[0xb3a70df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:29.127934-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:51:29.133775-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39c14180, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:29.133797-0500	VoiceOver	AudioConverter -> 0xb39c14180: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:29.133810-0500	VoiceOver	AudioConverter -> 0xb39c14180: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:29.147855-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873062 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:29.160125-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:51:29.176357-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:29.177314-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:29.177768-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:29.177807-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:29.177850-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:51:29.178002-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:29.178128-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:29.178198-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:29.178277-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:29.178648-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:29.178683-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	21:51:29.178477-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:29.195796-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 603864 ioTS st: 603864 ht: 47627.614103
error	21:51:29.262989-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:31.029654-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:31.414135-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:31.414450-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
fault	21:51:33.270090-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:33.268465-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.275341-0500	runningboardd	Invalidating assertion 394-47902-48821 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:33.271543-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:51:33.271595-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:51:33.271604-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:51:33.272485-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:33.272532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:33.279143-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.279202-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.280169-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.280241-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:33.280270-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:33.282304-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:33.282391-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:33.282532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.285461-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:33.285559-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:33.285649-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.285715-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.285742-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:33.286053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:51:33.286952-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:51:33.287231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:51:33.288247-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:33.288367-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
error	21:51:33.288450-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:33.288492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.288530-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.289195-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48826 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:33.289573-0500	runningboardd	Assertion 394-47902-48826 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:33.290065-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:33.288563-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.288665-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.289390-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:33.289441-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.289495-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:33.289928-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.289957-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.301292-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.301493-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.301779-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:33.305628-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:33.305807-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.305867-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.305968-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.306055-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.306186-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.306242-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.306355-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.306391-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.306421-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.306449-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.306510-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:33.306531-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:33.306566-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:33.306652-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:33.307566-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:33.307631-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:33.307991-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:33.308072-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:33.308109-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:33.308228-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:33.308293-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:33.309300-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39e55fe0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	21:51:33.309441-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:33.309653-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:33.310717-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:33.311635-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:33.311819-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:33.312006-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:33.313041-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:33.313086-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:33.313473-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:33.313592-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:33.313700-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:51:33.313905-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:33.314016-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:33.330100-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:33.330341-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:33.330364-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:33.330795-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xb3ac8a800:
error	21:51:33.330662-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:33.330857-0500	runningboardd	Invalidating assertion 394-47902-48828 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:33.330854-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:51:33.330965-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	21:51:33.331022-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	21:51:33.331098-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	21:51:33.336015-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xb3ac8a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	21:51:33.336780-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:33.646938-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea041, Nexy(47861), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:51:33.647716-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:51:33.648695-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:51:33.648977-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:51:33.649113-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
fault	21:51:33.997682-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:33.998184-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:34.000173-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:34.000850-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:34.035547-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:34.099129-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39e54ed0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:34.099159-0500	VoiceOver	AudioConverter -> 0xb39e54ed0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:34.099173-0500	VoiceOver	AudioConverter -> 0xb39e54ed0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:34.558834-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:34.558948-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:51:34.689724-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474873062 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:35.288311-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:35.308428-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:35.308514-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:35.345750-0500	VoiceOver	No list of permitted front apps returned
default	21:51:35.447122-0500	VoiceOver	No list of permitted front apps returned
default	21:51:35.562850-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 48076
default	21:51:35.563296-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48076
default	21:51:35.568984-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:35.569426-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:35.569488-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:35.576904-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:35.577066-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:35.587033-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873236 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:35.608459-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:35.609437-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:35.609735-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:35.609759-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:35.609894-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:35.610136-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:35.610259-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	21:51:35.609726-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:35.610380-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	21:51:35.610279-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:35.610665-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:35.610681-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	21:51:35.690256-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:36.128726-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.129192-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:51:36.129251-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:51:36.129272-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
fault	21:51:36.129910-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:36.131519-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:51:36.134844-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:36.134942-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:36.145297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:51:36.145354-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:51:36.150113-0500	runningboardd	Invalidating assertion 394-47902-48829 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:36.145361-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:51:36.147764-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:36.147882-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:36.160654-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:36.160681-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:36.160818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.165709-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.166073-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:36.166083-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:36.166205-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.169461-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.169816-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:36.169827-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:36.169858-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:36.169869-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:36.169874-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:36.169879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:36.169884-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:36.169924-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:36.169977-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:36.169986-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:36.170150-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:51:36.170187-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:51:36.170397-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:51:36.170535-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.171967-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:51:36.172092-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:51:36.172341-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:51:36.173479-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.173604-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.176175-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:51:36.176234-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:51:36.176323-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:51:36.176402-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:51:36.176548-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
error	21:51:36.177578-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:36.177623-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:51:36.177872-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.178150-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:36.178389-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:36.183173-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.183212-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:51:36.183315-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.183414-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:36.183433-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:51:36.183442-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:51:36.183468-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:51:36.183624-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:51:36.183732-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:51:36.183854-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:51:36.185317-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
error	21:51:36.185492-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:51:36.185502-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:51:36.185508-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:51:36.185746-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:51:36.197547-0500	runningboardd	Assertion 394-47902-48845 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:36.197915-0500	runningboardd	Invalidating assertion 394-47902-48845 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:36.198113-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48846 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:36.198193-0500	runningboardd	Assertion 394-47902-48846 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:36.198664-0500	runningboardd	Invalidating assertion 394-47902-48846 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:51:36.198870-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-48847 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:51:36.198956-0500	runningboardd	Assertion 394-47902-48847 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:51:36.278886-0500	VoiceOver	No list of permitted front apps returned
default	21:51:36.279321-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:36.279381-0500	VoiceOver	No list of permitted front apps returned
default	21:51:36.279963-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:36.280055-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:36.374996-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:51:36.440627-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48084
default	21:51:36.447278-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48084
default	21:51:36.508080-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48085
default	21:51:36.510524-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48085
default	21:51:36.579874-0500	VoiceOver	No list of permitted front apps returned
error	21:51:37.009361-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:51:37.533991-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:51:37.579140-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:51:37.579366-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:37.579813-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39c15e00, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:51:37.579843-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:51:37.579932-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:51:37.580245-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:37.580351-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:51:37.580367-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:51:37.580375-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:51:37.580390-0500	VoiceOver	           AQMEIO_HAL.cpp:3593  0xb3aa2e418 (1C-77-54-18-C8-A3:output): lock contended, setting stream format change pending
default	21:51:37.598268-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873400 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:37.609740-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:51:37.624136-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:37.625062-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:37.625799-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:37.625830-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:37.625874-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:51:37.624952-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:37.626094-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
fault	21:51:37.625518-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:37.626180-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:37.626219-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:37.626521-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:37.626538-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	21:51:37.671782-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:38.887953-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48109
default	21:51:38.890254-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48109
default	21:51:39.094677-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:39.100250-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:39.100702-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:39.380446-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48115
default	21:51:39.320218-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:51:40.030144-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:40.086420-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: c0000000c pid: 48107
default	21:51:40.087383-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1600000012 pid: 48107
default	21:51:40.139750-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cda1c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:40.139780-0500	VoiceOver	AudioConverter -> 0xb39cda1c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:40.139792-0500	VoiceOver	AudioConverter -> 0xb39cda1c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:40.236390-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:40.236607-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:40.259654-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:40.262897-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:40.295361-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:40.299491-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:40.368841-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:40.532253-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873405 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:40.573935-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:40.575422-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:40.575746-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:40.575845-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:40.575956-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:40.576245-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:40.576353-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:40.576482-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:40.576831-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:40.576874-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:40.589708-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 855095 ioTS st: 855095 ht: 47639.007777
fault	21:51:40.591631-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
error	21:51:40.884794-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:41.270179-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 2c00000025 pid: 48119
default	21:51:41.270813-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 360000002d pid: 48119
default	21:51:41.437295-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48134
default	21:51:41.889908-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48139
default	21:51:42.297100-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:42.297677-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:42.297808-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:51:42.300228-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:42.300241-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:42.300306-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:42.311053-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873405 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	21:51:42.311992-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873418 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	21:51:42.324429-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:42.324645-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:51:42.355492-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:42.356327-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:42.356580-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:42.356617-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:42.356678-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:51:42.356509-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:42.356965-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:42.357057-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:42.357172-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:42.357218-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:42.357522-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:42.357543-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	21:51:42.405706-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:43.022630-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:43.577439-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:43.580204-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:43.580286-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:43.584685-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873418 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	21:51:43.756704-0500	VoiceOver	No list of permitted front apps returned
default	21:51:43.756989-0500	VoiceOver	No list of permitted front apps returned
default	21:51:43.758375-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:43.758508-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:51:43.778878-0500	VoiceOver	[0xb3a70e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:43.779066-0500	VoiceOver	[0xb3a70e580] invalidated after the last release of the connection object
default	21:51:43.802462-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:43.802578-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:51:43.808041-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:43.808152-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:51:43.810883-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873444 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	21:51:43.827105-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cd9bc0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:43.827131-0500	VoiceOver	AudioConverter -> 0xb39cd9bc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:43.827172-0500	VoiceOver	AudioConverter -> 0xb39cd9bc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:43.842330-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:43.843401-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:43.843764-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:43.843805-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:43.843858-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:43.844197-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:43.844305-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:43.844357-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:43.844702-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:43.844722-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	21:51:43.846041-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:43.846570-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:43.890830-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:43.900305-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:43.900360-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:43.940326-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
error	21:51:43.992019-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:45.760612-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873445 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	21:51:45.761326-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:45.773797-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:45.779088-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873448 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
error	21:51:45.907788-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:46.029683-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:46.627276-0500	VoiceOver	No list of permitted front apps returned
default	21:51:46.627542-0500	VoiceOver	No list of permitted front apps returned
default	21:51:46.652369-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:46.652576-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:51:46.666291-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d610e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:46.666318-0500	VoiceOver	AudioConverter -> 0xb39d610e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:46.666333-0500	VoiceOver	AudioConverter -> 0xb39d610e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:46.685216-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:46.689420-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60420, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:46.689452-0500	VoiceOver	AudioConverter -> 0xb39d60420: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:46.689466-0500	VoiceOver	AudioConverter -> 0xb39d60420: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:46.701972-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:46.710256-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:46.710354-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:46.721824-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873448 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:46.722340-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873449 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:46.776680-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:51:46.777359-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:51:46.777384-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:46.777565-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:46.777589-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:46.777630-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:51:46.777734-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:46.777780-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:46.777843-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:46.777874-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:46.778057-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:46.778076-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:46.789474-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 991807 ioTS st: 991807 ht: 47645.207777
default	21:51:46.799014-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:46.799251-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
error	21:51:46.841341-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	21:51:49.016163-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:49.023631-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.033277-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:49.110152-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:49.110285-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:51:49.121565-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.121634-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:49.121731-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:51:49.127721-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.138000-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cdf6c0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:49.138025-0500	VoiceOver	AudioConverter -> 0xb39cdf6c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:49.138040-0500	VoiceOver	AudioConverter -> 0xb39cdf6c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:49.143862-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.148885-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:49.151802-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:49.152056-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:49.175595-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:49.175739-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:51:49.227366-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.227618-0500	VoiceOver	No list of permitted front apps returned
default	21:51:49.231271-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:49.231434-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:51:49.235366-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:49.235454-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:51:49.237283-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cd9110, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:49.237303-0500	VoiceOver	AudioConverter -> 0xb39cd9110: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:49.237310-0500	VoiceOver	AudioConverter -> 0xb39cd9110: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:49.244056-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:49.247749-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:49.252502-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:49.260138-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:49.260204-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:49.265006-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474873449 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:49.265547-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873450 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:49.306062-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:51:49.306569-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:49.306775-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:51:49.306868-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:49.306999-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:49.307023-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:49.307060-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:49.307254-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:49.307307-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:49.307358-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:49.307732-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:49.307749-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:49.319413-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 1047594 ioTS st: 1047594 ht: 47647.737777
error	21:51:49.641045-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:52.029562-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:52.353946-0500	VoiceOver	No list of permitted front apps returned
fault	21:51:52.356566-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:52.372144-0500	VoiceOver	No list of permitted front apps returned
default	21:51:52.442209-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:51:52.443039-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:51:52.443166-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:51:52.459906-0500	VoiceOver	No list of permitted front apps returned
default	21:51:52.484546-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:52.484803-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:51:52.533761-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:52.533893-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:51:52.546030-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5c840, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:51:52.546056-0500	VoiceOver	AudioConverter -> 0xb39d5c840: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:51:52.546066-0500	VoiceOver	AudioConverter -> 0xb39d5c840: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:51:52.557544-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:51:52.570056-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:51:52.579931-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:51:52.579976-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:51:52.603432-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474873450 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:51:52.603909-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873452 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:51:52.663469-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:51:52.663763-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:51:52.664027-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:51:52.664068-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:51:52.664268-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:51:52.664294-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:51:52.664328-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:51:52.664472-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:51:52.664530-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:51:52.664556-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:51:52.664762-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:51:52.664777-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:51:52.679429-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 1121682 ioTS st: 1121682 ht: 47651.097777
error	21:51:52.781614-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:51:55.005758-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:51:55.590821-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:51:55.591061-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:51:58.029562-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:00.800988-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:08  id:21474873452 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:01.014772-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:52:01.029709-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:01.400125-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:01.409953-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:01.410028-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:03.511208-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:52:03.511293-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:03.512049-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:04.031546-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:04.109405-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:52:04.112452-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:52:04.112869-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 stopping playing
default	21:52:04.113027-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:52:04.113141-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:52:04.113301-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:52:04.113477-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:04.113571-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:52:04.113720-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:52:04.113749-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:52:04.113775-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:04.113868-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:04.113910-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	21:52:04.122518-0500	runningboardd	Invalidating assertion 394-47902-48860 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:52:04.122734-0500	runningboardd	Invalidating assertion 394-328-48822 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:52:04.224216-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:52:04.224248-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:52:04.224275-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:52:04.224328-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:52:04.224385-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:52:04.232094-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:52:05.572684-0500	VoiceOver	No list of permitted front apps returned
default	21:52:05.704476-0500	VoiceOver	No list of permitted front apps returned
default	21:52:05.752633-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:05.752744-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:05.760515-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:05.764118-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:05.768600-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873459 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:05.908515-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:52:05.954214-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:52:05.954674-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:05.955080-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:52:05.955244-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:52:05.955264-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 starting playing
default	21:52:05.955383-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:52:05.955434-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:52:05.955470-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'}
default	21:52:05.955538-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	21:52:05.955560-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:52:05.955524-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:05.955632-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:05.955621-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:52:05.955629-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:52:05.955748-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:05.955775-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:05.955847-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:52:05.955887-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:52:05.956013-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:05.956120-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:05.956202-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:05.956252-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:05.956393-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	21:52:05.956648-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:05.956809-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:05.956846-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:52:05.956865-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	21:52:05.956876-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	21:52:05.956891-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
default	21:52:05.956978-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
error	21:52:05.956960-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:52:05.956993-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:05.957052-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:52:05.974580-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 1414837 ioTS st: 1414837 ht: 47664.392788
error	21:52:06.160305-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:06.161612-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:06.161758-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:52:06.164561-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:06.165093-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:06.165174-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:06.167444-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cda280, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:06.167474-0500	VoiceOver	AudioConverter -> 0xb39cda280: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:06.167484-0500	VoiceOver	AudioConverter -> 0xb39cda280: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
fault	21:52:06.950623-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:06.953181-0500	VoiceOver	No list of permitted front apps returned
default	21:52:06.993305-0500	VoiceOver	No list of permitted front apps returned
default	21:52:06.994900-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:06.995531-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:06.995434-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:07.031982-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:07.036134-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:07.036242-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:07.054183-0500	VoiceOver	No list of permitted front apps returned
default	21:52:07.058212-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873459 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:07.058609-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873461 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:07.088303-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:07.088676-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:07.088911-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:07.089091-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
error	21:52:07.120215-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:08.606378-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873461 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:08.816684-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:52:09.205279-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:09.215159-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:09.215251-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:10.029844-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:11.314647-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:52:11.314668-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:11.315258-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:12.282371-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	21:52:13.029545-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:16.029597-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:18.960546-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:20.829602-0500	VoiceOver	No list of permitted front apps returned
default	21:52:20.931194-0500	VoiceOver	No list of permitted front apps returned
default	21:52:20.952325-0500	VoiceOver	No list of permitted front apps returned
default	21:52:20.977771-0500	VoiceOver	No list of permitted front apps returned
default	21:52:20.980422-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:20.981025-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:20.981105-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:21.007191-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:21.007385-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:52:21.045767-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:21.045921-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:52:21.047878-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cd8660, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:21.047908-0500	VoiceOver	AudioConverter -> 0xb39cd8660: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:21.047916-0500	VoiceOver	AudioConverter -> 0xb39cd8660: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:21.053751-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:21.059156-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:21.063837-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873465 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:21.070569-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:52:21.091137-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:21.091675-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:21.091744-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:21.091936-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:21.091960-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	21:52:21.091959-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:21.091989-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:21.092159-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:21.092220-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:21.092267-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:21.092479-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:21.092494-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:21.104510-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 1748455 ioTS st: 1748455 ht: 47679.522788
error	21:52:21.302164-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:22.029813-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	21:52:22.346427-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:22.351712-0500	VoiceOver	No list of permitted front apps returned
default	21:52:22.397572-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:22.418943-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:22.424933-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:22.424979-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:22.447096-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873465 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:22.453325-0500	VoiceOver	No list of permitted front apps returned
default	21:52:22.485424-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:22.485697-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:22.485968-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:22.486021-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:22.486229-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:22.486254-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:22.486284-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:22.504479-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 1779325 ioTS st: 1779325 ht: 47680.922788
error	21:52:22.519151-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:24.005350-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873466 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:24.206671-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:52:24.605509-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:24.615114-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:24.615209-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:25.029786-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:26.714612-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:52:26.714636-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:26.715372-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:28.029515-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:31.029438-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:34.029462-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:36.177280-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:36.177731-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:36.177814-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:36.179538-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5e7f0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:36.179570-0500	VoiceOver	AudioConverter -> 0xb39d5e7f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:36.179585-0500	VoiceOver	AudioConverter -> 0xb39d5e7f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:37.029470-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:37.899899-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873470 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:37.910799-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:52:37.920588-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:37.921386-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:37.921406-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:37.921736-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:37.921771-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	21:52:37.921751-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:37.921813-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:37.922024-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:37.922097-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:37.922159-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:37.922403-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:37.922422-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	21:52:37.962733-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	21:52:39.057858-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:39.061793-0500	VoiceOver	No list of permitted front apps returned
default	21:52:39.163178-0500	VoiceOver	No list of permitted front apps returned
fault	21:52:39.171463-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:39.174566-0500	VoiceOver	No list of permitted front apps returned
default	21:52:39.201868-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:39.202299-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:39.202383-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:39.208646-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:39.208758-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:52:39.209687-0500	VoiceOver	No list of permitted front apps returned
default	21:52:39.209825-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:39.210278-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:39.210351-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:39.217175-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:39.225265-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:39.225328-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:39.228652-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873470 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:39.229545-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873471 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:39.258802-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:39.259200-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:39.259408-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:39.259562-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:39.259588-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:39.259610-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:39.259641-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:39.259782-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:39.259836-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:39.259862-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:39.260054-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:39.260071-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:39.274483-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2149105 ioTS st: 2149105 ht: 47697.692788
default	21:52:39.275320-0500	VoiceOver	No list of permitted front apps returned
error	21:52:39.318789-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:40.030805-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:40.079124-0500	VoiceOver	[0xb3a70e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:40.079485-0500	VoiceOver	[0xb3a70e580] invalidated after the last release of the connection object
default	21:52:40.079880-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d6a5e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:40.079916-0500	VoiceOver	AudioConverter -> 0xb39d6a5e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:40.079929-0500	VoiceOver	AudioConverter -> 0xb39d6a5e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:40.091588-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d69830, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:40.091622-0500	VoiceOver	AudioConverter -> 0xb39d69830: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:40.091631-0500	VoiceOver	AudioConverter -> 0xb39d69830: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:40.096879-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:40.097170-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:52:40.101162-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:40.103306-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5cae0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:40.103326-0500	VoiceOver	AudioConverter -> 0xb39d5cae0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:40.103339-0500	VoiceOver	AudioConverter -> 0xb39d5cae0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:40.114660-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:40.128431-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873471 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:40.173536-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:40.173880-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:40.174165-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:40.174221-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:40.174433-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:40.174458-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:40.174488-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:40.174854-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:40.174917-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:40.174945-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:40.175165-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:40.175185-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:40.194561-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2169391 ioTS st: 2169391 ht: 47698.612788
error	21:52:40.299731-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:40.375806-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:40.375941-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:52:41.608288-0500	VoiceOver	No list of permitted front apps returned
default	21:52:41.608675-0500	VoiceOver	No list of permitted front apps returned
default	21:52:41.683394-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:41.683610-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:52:41.703990-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:41.704180-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:41.718121-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:41.718296-0500	VoiceOver	[0xb3a70e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:41.718482-0500	VoiceOver	[0xb3a70e580] invalidated after the last release of the connection object
default	21:52:41.722691-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:41.722870-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:41.725301-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:41.725358-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:41.736351-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873473 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:41.737018-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873475 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:41.753763-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5dd40, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:41.754256-0500	VoiceOver	AudioConverter -> 0xb39d5dd40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:41.754292-0500	VoiceOver	AudioConverter -> 0xb39d5dd40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:41.778980-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:41.779687-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:41.779748-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:41.779891-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:41.779917-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:41.779951-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:52:41.780009-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:41.780107-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:41.780164-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:41.780194-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:41.780396-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:41.780412-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:41.794569-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2204672 ioTS st: 2204672 ht: 47700.212788
error	21:52:41.816358-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:42.749310-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:42.755179-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:42.759023-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:42.765317-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:42.765398-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:42.767374-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873475 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:42.767824-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873476 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:42.795506-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:42.795969-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:42.796232-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:42.796247-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:42.796555-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:42.796585-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:42.796622-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:42.796786-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:42.796838-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:42.796875-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:42.797072-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:42.797087-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:42.814490-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2227164 ioTS st: 2227164 ht: 47701.232788
error	21:52:42.897933-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:43.031426-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:44.152595-0500	runningboardd	Resolved pid 47927 to [xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:47927:47927]
default	21:52:44.152965-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:47927:47927] is not RunningBoard jetsam managed.
default	21:52:44.152987-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:47927:47927] This process will not be managed.
default	21:52:44.154429-0500	runningboardd	Resolved pid 47926 to [xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:47926:47926]
default	21:52:44.154892-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:47926:47926] is not RunningBoard jetsam managed.
default	21:52:44.154911-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:47925])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:47926:47926] This process will not be managed.
default	21:52:44.156810-0500	runningboardd	Resolved pid 47924 to [xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:47924:47924]
default	21:52:44.157186-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:47924:47924] is not RunningBoard jetsam managed.
default	21:52:44.157227-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:47902])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:47924:47924] This process will not be managed.
default	21:52:44.698525-0500	VoiceOver	No list of permitted front apps returned
default	21:52:44.698803-0500	VoiceOver	No list of permitted front apps returned
default	21:52:44.728699-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:44.728976-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:52:44.764781-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:44.765892-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5f060, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:44.765925-0500	VoiceOver	AudioConverter -> 0xb39d5f060: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:44.765938-0500	VoiceOver	AudioConverter -> 0xb39d5f060: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:44.779467-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:44.785326-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:44.785438-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:44.794697-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474873476 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:44.795608-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873477 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:44.845782-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:44.846630-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:44.846863-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:44.846890-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:44.846936-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:52:44.846823-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:44.847286-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:44.847407-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:44.847453-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	21:52:44.847296-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:44.847718-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:44.847734-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:44.908380-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cdb8a0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:44.908655-0500	VoiceOver	AudioConverter -> 0xb39cdb8a0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:44.908762-0500	VoiceOver	AudioConverter -> 0xb39cdb8a0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:44.945350-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:44.945404-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:44.997124-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:44.997600-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:44.998064-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:44.998125-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:44.998400-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:44.998435-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:44.998482-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:44.998663-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:44.998732-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:44.998774-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:44.999041-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:44.999063-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:45.014646-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2275675 ioTS st: 2275675 ht: 47703.432788
error	21:52:45.092310-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:45.973239-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:49.029397-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:49.955488-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474873478 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:50.164285-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:52:50.396661-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873479 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:50.396898-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:52:50.405703-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:50.414864-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:50.414907-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:50.415797-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873479 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:50.416515-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873480 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:50.433056-0500	VoiceOver	No list of permitted front apps returned
default	21:52:50.435911-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:50.436099-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:52:50.444490-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:50.445444-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:50.445688-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:50.445806-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:50.445972-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:50.446121-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:50.446182-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:50.446280-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	21:52:50.450802-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:50.451459-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:50.446568-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:50.446613-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:50.464577-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2395848 ioTS st: 2395848 ht: 47708.882788
default	21:52:50.603605-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:50.604199-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:50.604295-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:50.637708-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:50.637881-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:52:50.682060-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:50.682326-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:50.696902-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:50.700572-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:50.705259-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:50.705316-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:50.712296-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873480 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:50.712930-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873481 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:50.740921-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:50.741724-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:50.742070-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:50.742316-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	21:52:50.742274-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:50.742347-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:50.742410-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:50.742660-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:50.742752-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:50.742795-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:50.743077-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:50.743123-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:50.754756-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2402243 ioTS st: 2402243 ht: 47709.172788
error	21:52:50.807903-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:50.935863-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5cc90, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:50.935883-0500	VoiceOver	AudioConverter -> 0xb39d5cc90: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:50.935911-0500	VoiceOver	AudioConverter -> 0xb39d5cc90: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:52.006515-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:52.948234-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:52.955179-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:52.955241-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:52.958348-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474873481 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:52.958642-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873482 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:52.985630-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:52.986407-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:52.986427-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:52.986680-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:52.986715-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:52.986757-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:52:52.986849-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:52.986951-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:52.987020-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:52.987054-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:52.987294-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:52.987313-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:53.004590-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2451856 ioTS st: 2451856 ht: 47711.422788
error	21:52:53.027571-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	21:52:53.708710-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:53.712379-0500	VoiceOver	No list of permitted front apps returned
default	21:52:53.813829-0500	VoiceOver	No list of permitted front apps returned
fault	21:52:53.933070-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:53.941742-0500	VoiceOver	No list of permitted front apps returned
fault	21:52:53.943504-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:53.946440-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:53.947549-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:53.947758-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:53.952964-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 48462
default	21:52:53.953588-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48462
default	21:52:53.960325-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:53.960947-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
error	21:52:54.080224-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:54.110068-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:54.110394-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:54.110454-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:54.124903-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:54.125042-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:54.127003-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d63ba0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:54.127027-0500	VoiceOver	AudioConverter -> 0xb39d63ba0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:54.127037-0500	VoiceOver	AudioConverter -> 0xb39d63ba0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:54.133486-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:54.134952-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:54.134989-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:54.172563-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:54.172871-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:54.173177-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:54.173203-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:54.173404-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:54.173425-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:54.173453-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:54.173590-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:54.173654-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:54.173680-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:54.173899-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:54.173914-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	21:52:54.212354-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:54.830708-0500	VoiceOver	No list of permitted front apps returned
default	21:52:54.833699-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:52:54.833761-0500	VoiceOver	No list of permitted front apps returned
default	21:52:54.834337-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:52:54.834444-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:52:54.851654-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:54.855412-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:54.855490-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:54.859139-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873484 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:54.859760-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873485 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:54.881238-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:52:54.881787-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:54.881886-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:54.882328-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:54.882359-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	21:52:54.882174-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:54.882412-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:54.882656-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:54.882723-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:54.882761-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:54.883001-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:54.883021-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:54.894675-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2493532 ioTS st: 2493532 ht: 47713.312788
error	21:52:54.916363-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:54.967341-0500	VoiceOver	No list of permitted front apps returned
default	21:52:55.045752-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48470
default	21:52:56.393547-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48482
default	21:52:56.471935-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48483
default	21:52:56.995120-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:57.004908-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:57.004962-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:57.391174-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cde280, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:57.391230-0500	VoiceOver	AudioConverter -> 0xb39cde280: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:57.391253-0500	VoiceOver	AudioConverter -> 0xb39cde280: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:57.512770-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:57.521996-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cda820, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:52:57.522020-0500	VoiceOver	AudioConverter -> 0xb39cda820: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:52:57.522031-0500	VoiceOver	AudioConverter -> 0xb39cda820: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:52:57.533904-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:57.534113-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:52:57.534140-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:57.552875-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:57.553755-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873490 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:57.553958-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:57.592927-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:57.594240-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:52:57.594670-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:57.594820-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:57.595139-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:52:57.595844-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:57.595977-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:57.596142-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:57.596657-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:57.596812-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	21:52:57.597980-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:52:57.598861-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:57.614891-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2553509 ioTS st: 2553509 ht: 47716.032788
error	21:52:57.806937-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:52:58.021512-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:52:59.153804-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48499
default	21:52:59.157640-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48499
default	21:52:59.736716-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:59.736948-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:59.782484-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:52:59.782607-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:59.782799-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:52:59.784075-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:52:59.785319-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:52:59.785377-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:52:59.790929-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:52:59.791203-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:52:59.793294-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474873490 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:52:59.793872-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873492 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:52:59.827714-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:52:59.828314-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:52:59.828327-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:59.828505-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:52:59.828536-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:52:59.828567-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:52:59.828567-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:52:59.828733-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:52:59.828794-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:52:59.828825-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:52:59.829013-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:52:59.829025-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:52:59.844537-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2602681 ioTS st: 2602681 ht: 47718.262788
error	21:52:59.871583-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:01.030392-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:01.287306-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:01.295017-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:01.295069-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:01.296514-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873492 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:01.385087-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:01.385314-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:53:01.393371-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3a999d40, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:01.393414-0500	VoiceOver	AudioConverter -> 0xb3a999d40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:01.393426-0500	VoiceOver	AudioConverter -> 0xb3a999d40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:01.395231-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:53:01.408123-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873493 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:01.447423-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:53:01.448332-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:01.448582-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:01.448613-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:01.448657-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:53:01.448755-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:01.448868-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:01.448932-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:01.448971-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	21:53:01.449054-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:01.449249-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:01.449270-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:01.464591-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2638403 ioTS st: 2638403 ht: 47719.882788
error	21:53:01.537882-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:04.029495-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:05.469494-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:05.469809-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:53:06.405694-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474873493 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:06.614115-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:53:06.927181-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873494 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:06.927566-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:53:07.021728-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:07.029310-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:08.700159-0500	VoiceOver	No list of permitted front apps returned
default	21:53:08.700520-0500	VoiceOver	No list of permitted front apps returned
default	21:53:08.775585-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:08.775798-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:53:08.799766-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:08.800007-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:53:08.813031-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:08.813250-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:08.813368-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:53:08.815309-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:08.815371-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:08.817540-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:08.817920-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:53:08.822037-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873494 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:08.823380-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cdbc30, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:08.823416-0500	VoiceOver	AudioConverter -> 0xb39cdbc30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:08.823446-0500	VoiceOver	AudioConverter -> 0xb39cdbc30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:08.823822-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873496 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:08.840063-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cd9230, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:08.840081-0500	VoiceOver	AudioConverter -> 0xb39cd9230: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:08.840115-0500	VoiceOver	AudioConverter -> 0xb39cd9230: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:08.856988-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:53:08.857582-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:08.857722-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:53:08.857805-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:08.857980-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:08.858010-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:08.858043-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:53:08.858208-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:08.858277-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:08.858308-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:08.858544-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:08.858566-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:08.874610-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2801794 ioTS st: 2801794 ht: 47727.292788
error	21:53:08.894670-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:09.847959-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:53:09.853615-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:53:09.858655-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:09.865170-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:09.865241-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:09.866868-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873496 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:09.868284-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873497 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:09.895183-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:53:09.895836-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:09.895869-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:09.896070-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:09.896100-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:09.896146-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:53:09.896126-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:09.896357-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:09.896425-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:09.896461-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:09.896703-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:09.896723-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:09.914513-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2824727 ioTS st: 2824727 ht: 47728.332788
error	21:53:09.988655-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:10.029333-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:11.530569-0500	VoiceOver	No list of permitted front apps returned
default	21:53:11.530986-0500	VoiceOver	No list of permitted front apps returned
default	21:53:11.552325-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:11.552514-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:53:11.579035-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:53:11.579979-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39c1ad30, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:11.580005-0500	VoiceOver	AudioConverter -> 0xb39c1ad30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:11.580025-0500	VoiceOver	AudioConverter -> 0xb39c1ad30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:11.596208-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:11.605355-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:11.605432-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:11.612534-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873497 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:11.613326-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873498 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:11.657262-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:53:11.657852-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:11.657933-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:11.658137-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:11.658164-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	21:53:11.658152-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:11.658205-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:53:11.658354-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:11.658415-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:11.658442-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:11.658667-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:11.658682-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:11.671312-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:11.671473-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:53:11.674541-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2863536 ioTS st: 2863536 ht: 47730.092788
default	21:53:11.682586-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d63f90, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:11.682713-0500	VoiceOver	AudioConverter -> 0xb39d63f90: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:11.682770-0500	VoiceOver	AudioConverter -> 0xb39d63f90: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:11.684600-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	21:53:11.699107-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:11.704922-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:11.704947-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:11.707777-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873498 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:11.751507-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:53:11.751760-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:53:11.752017-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:11.752129-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:11.752298-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:11.752321-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:11.752346-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:53:11.752481-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:11.752537-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:11.752562-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:11.752743-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:11.752756-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:11.764529-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2865521 ioTS st: 2865521 ht: 47730.182788
error	21:53:11.813313-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:13.020869-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:14.827155-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:14.827301-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
fault	21:53:14.851946-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:14.918368-0500	VoiceOver	No list of permitted front apps returned
default	21:53:14.944371-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:53:14.956854-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:14.965194-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:14.965255-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:14.968354-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474873499 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:14.968811-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873500 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:14.978584-0500	VoiceOver	No list of permitted front apps returned
default	21:53:14.995839-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:53:14.996222-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:53:14.996556-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:14.996613-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:14.996822-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:14.996848-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:14.996885-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:53:14.997021-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:14.997077-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:53:14.997113-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:14.997306-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:14.997320-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:15.014606-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 2937184 ioTS st: 2937184 ht: 47733.432788
error	21:53:15.076348-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:16.025151-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:18.585954-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474873500 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:18.789187-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:53:18.955657-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:19.131747-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873501 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:19.132086-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:53:19.222579-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:22.029381-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:23.233542-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:53:23.233633-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:53:23.233668-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:53:23.233716-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:53:24.826133-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474873501 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:25.029298-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:25.039176-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:53:25.425199-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:25.434912-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:25.434979-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:26.533268-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:26.533381-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:53:26.805277-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48645
default	21:53:27.534749-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:53:27.534771-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:27.535164-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:27.554603-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:53:27.555077-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:53:27.555180-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 stopping playing
default	21:53:27.555238-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:53:27.555280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:53:27.555345-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:53:27.555445-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:27.555468-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:53:27.555541-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:53:27.555552-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:53:27.555643-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:27.555706-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:27.555727-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	21:53:27.558811-0500	runningboardd	Invalidating assertion 394-47902-48950 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:53:27.559009-0500	runningboardd	Invalidating assertion 394-328-48951 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:53:27.660465-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:53:27.660480-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:53:27.660490-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:53:27.660509-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:53:27.660521-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:53:27.664385-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:53:29.306528-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:29.306737-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:53:37.657730-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:37.657953-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:53:41.669169-0500	VoiceOver	No list of permitted front apps returned
default	21:53:41.770601-0500	VoiceOver	No list of permitted front apps returned
default	21:53:41.775654-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:53:41.779196-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:53:41.779589-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:53:41.794213-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48718
default	21:53:42.484213-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:42.484344-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:53:42.486443-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49102 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:53:42.486946-0500	runningboardd	Assertion 394-47902-49102 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:53:42.492135-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:53:42.492309-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:53:42.492408-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:53:42.492517-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:53:42.492568-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:53:42.492630-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49103 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:53:42.492695-0500	runningboardd	Assertion 394-328-49103 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:53:42.495976-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:53:42.495989-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:53:42.496000-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:53:42.496020-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:53:42.496040-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:53:42.496783-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:53:42.499548-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:53:42.504584-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873515 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:42.742530-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:53:42.784606-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:53:42.785023-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:53:42.785562-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:53:42.785754-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:53:42.785773-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 starting playing
default	21:53:42.785876-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:53:42.785926-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:53:42.785954-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'}
default	21:53:42.785976-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:53:42.786133-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:53:42.786143-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:53:42.786245-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:53:42.786313-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:53:42.786525-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	21:53:42.786043-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:53:42.786014-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	21:53:42.786920-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:42.786422-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:53:42.786993-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:42.787019-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	21:53:42.786439-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:53:42.786809-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:53:42.787029-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
fault	21:53:42.786003-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:42.786886-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
error	21:53:42.787091-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
fault	21:53:42.786395-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:53:42.787082-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
error	21:53:42.787236-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:53:42.786780-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:42.787440-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:53:42.787715-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:42.787755-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:53:42.789304-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60f00, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:53:42.789352-0500	VoiceOver	AudioConverter -> 0xb39d60f00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:53:42.789365-0500	VoiceOver	AudioConverter -> 0xb39d60f00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:53:42.804929-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 3549959 ioTS st: 3549959 ht: 47761.223040
error	21:53:42.896383-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:43.030782-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:44.405159-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:53:44.405276-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:53:46.029232-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:49.029292-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:49.366583-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474873515 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:49.576543-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:53:49.890592-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873535 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:53:49.891069-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:53:50.006506-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:53:52.030262-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:53:53.398313-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:53:53.398396-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:53:53.398468-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:53:53.398902-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:53:53.398941-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:53:53.454843-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:53:53.455307-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:53:55.029258-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:53:56.996727-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:07  id:21474873535 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:53:57.205887-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:53:57.595487-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:53:57.605165-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:53:57.605268-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:53:58.029279-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:53:59.704852-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:53:59.704876-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:53:59.705214-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:53:59.705328-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 stopping playing
default	21:53:59.705406-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:53:59.705468-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:53:59.705569-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:53:59.706093-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:53:59.706108-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:53:59.705933-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:53:59.706769-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:59.706856-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:59.706743-0500	runningboardd	Invalidating assertion 394-47902-49102 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:53:59.706886-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	21:53:59.706530-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:53:59.706895-0500	runningboardd	Invalidating assertion 394-328-49103 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:53:59.814263-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:53:59.814291-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:53:59.814315-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:53:59.814362-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:53:59.814455-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:53:59.820921-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:54:00.229203-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.229231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:00.229238-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:00.230232-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:00.230252-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:00.230258-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:54:00.237737-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:00.237754-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:00.237863-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.237879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:00.237885-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:00.245510-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:00.245718-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:00.245779-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:00.245817-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:00.245852-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:00.247294-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:00.247358-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:00.247503-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.247554-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:00.247607-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:00.250368-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:00.250591-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:00.254365-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.255306-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:00.255321-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:00.255336-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:00.255347-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:00.255354-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:00.255366-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:00.255373-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:00.255436-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:00.255450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:00.255595-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:00.255664-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.255775-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:00.255990-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:00.256047-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:00.259572-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:54:00.259605-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:54:00.259614-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:54:00.272465-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:00.272489-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:00.272620-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:00.284054-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	21:54:00.284462-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:00.285164-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:05.508105-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:05.508162-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.508184-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:05.508194-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:54:05.508208-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:05.508218-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:05.513891-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:05.513921-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:05.514054-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.514081-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:05.514106-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:05.517215-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.517256-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.517271-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.517528-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:05.517543-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:05.517561-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:05.517574-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:05.517612-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:05.517666-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:05.517771-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:05.517817-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:05.520806-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:05.520829-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:05.520976-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.520999-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:05.521008-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:05.525573-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.528291-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:05.528317-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:05.528351-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:05.528363-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:05.530303-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.530657-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:05.530905-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:05.530922-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.532411-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.537185-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:54:05.537235-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:54:05.537240-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:54:05.546957-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:05.546984-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:05.547116-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:05.551119-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:05.551543-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:05.551557-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:05.551609-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:05.551620-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:05.551628-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:05.551634-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:05.551662-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:05.551753-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:05.551834-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:05.551882-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:05.551968-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:05.552102-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:05.553080-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.553097-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:05.553105-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.553145-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:05.553157-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:05.555797-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.555856-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:05.556374-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:05.556392-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:05.556401-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:05.556721-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:05.556737-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:05.556917-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.556932-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:05.556941-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.556952-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:05.556963-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:05.560200-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:05.560225-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:05.560549-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:05.560566-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:05.560575-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:05.560595-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:05.560607-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:10.387551-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:54:15.164222-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.164248-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:15.164257-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:15.166057-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:15.166079-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:15.166086-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:54:15.173938-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:15.175004-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:15.176732-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.176762-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:15.176769-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:15.178307-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:15.178339-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:15.178347-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:15.178371-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:15.178554-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:15.178669-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:15.178761-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:15.178818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:15.179399-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.179476-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:15.179508-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:15.181552-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:15.181658-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:15.181925-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.182205-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:15.182281-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:15.185492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:15.185632-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:15.185722-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:15.185745-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:15.185827-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:15.185894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:15.185955-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:15.185997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:15.186991-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.187103-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:15.187150-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:15.195668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:54:15.195826-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:54:15.196160-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:54:15.203747-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:15.203767-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:15.203880-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:15.209979-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:15.210844-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.807600-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.807667-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:21.807686-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:21.809748-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:21.809778-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:21.809787-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:54:21.812431-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:21.812457-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:21.812627-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.812685-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:21.812817-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:21.818973-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.819027-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.819045-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:21.819052-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:21.819062-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:21.819071-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:21.819163-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.820322-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:21.820338-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:21.820344-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:21.820590-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:21.823023-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:21.823159-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:21.823337-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.823668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:54:21.824067-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:21.824112-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:54:21.824290-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:21.824487-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:54:21.826998-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.827250-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:21.827297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:21.827364-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:21.827529-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:21.837496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.837547-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.841439-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.853928-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:21.853962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:21.854127-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:21.854769-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:21.854948-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:21.854959-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:21.854995-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:21.855001-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:21.855272-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:21.855453-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:21.855668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:21.855838-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:21.855998-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:21.856117-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:21.856215-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:21.856282-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:21.857547-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:21.857579-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:21.860558-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.860591-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:21.860601-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.860624-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:21.860635-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:21.861800-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.861834-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:21.862052-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:21.862066-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:21.862072-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:21.862417-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:21.862432-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:21.862859-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.862876-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:21.862884-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.862898-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	21:54:21.862909-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:54:21.863517-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d60720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.863534-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:21.863780-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:21.863796-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:21.863806-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:21.863830-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:21.863840-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:21.865020-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d62610, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:21.865304-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xb3ac8a800:
default	21:54:24.150696-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:54:26.099909-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 48905
default	21:54:26.100404-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48905
default	21:54:26.981203-0500	runningboardd	Invalidating assertion 394-387-48783 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.WindowServer(88)>:387]
default	21:54:26.994441-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 48919
default	21:54:26.994860-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48919
default	21:54:27.090327-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:54:27.090336-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:54:27.090348-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:54:27.090394-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:54:27.090415-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:54:27.094676-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:54:27.311064-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48924
default	21:54:27.311113-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48923
default	21:54:27.891509-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 48928
default	21:54:27.899313-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 48928
default	21:54:28.313333-0500	VoiceOver	No list of permitted front apps returned
default	21:54:28.313539-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	21:54:28.313558-0500	VoiceOver	No list of permitted front apps returned
default	21:54:28.313966-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 47902, name: VoiceOver
default	21:54:28.314069-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	21:54:28.348588-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:28.348730-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:54:28.355309-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-49153 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:28.355400-0500	runningboardd	Assertion 394-387-49153 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:28.355773-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:54:28.355791-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:54:28.355803-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:54:28.355844-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:54:28.355886-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:54:28.359344-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:54:28.396718-0500	VoiceOver	No list of permitted front apps returned
default	21:54:28.396955-0500	VoiceOver	No list of permitted front apps returned
default	21:54:28.401204-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 48934
default	21:54:28.401570-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48934
default	21:54:28.412381-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:28.412491-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:54:28.416281-0500	VoiceOver	[0xb3a70e080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:28.416414-0500	VoiceOver	[0xb3a70e080] invalidated after the last release of the connection object
default	21:54:28.417944-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb3ad14c00, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:28.417973-0500	VoiceOver	AudioConverter -> 0xb3ad14c00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:28.417983-0500	VoiceOver	AudioConverter -> 0xb3ad14c00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:54:28.419631-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49156 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:28.419740-0500	runningboardd	Assertion 394-47902-49156 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:28.420337-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:54:28.420413-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:54:28.420471-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:54:28.420331-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-49157 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:54:28.420594-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:54:28.420612-0500	runningboardd	Assertion 394-328-49157 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:28.420660-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:54:28.428822-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:54:28.428870-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:54:28.428916-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:54:28.428973-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:54:28.428983-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:54:28.462388-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:54:28.462616-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:54:28.462634-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 starting playing
default	21:54:28.462768-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:28.462877-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:54:28.462944-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:28.461327-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:28.463213-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:54:28.463228-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:28.523291-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:54:28.525111-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:28.525562-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:28.525644-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:28.525779-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:28.526288-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:28.526432-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:28.526729-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:28.527160-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:28.527216-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:28.545249-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4558514 ioTS st: 4558514 ht: 47806.962498
fault	21:54:28.528353-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:28.528983-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
error	21:54:28.740911-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:28.789305-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48937
default	21:54:28.789351-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48938
default	21:54:28.843137-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:28.845046-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:28.845091-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:28.866327-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874214 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:28.928462-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:28.928838-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:28.929251-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:28.929373-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:28.929702-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:28.929734-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:28.929781-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:28.930156-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:28.930242-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
error	21:54:28.982940-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:29.422144-0500	VoiceOver	[0xb3a70e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:29.422358-0500	VoiceOver	[0xb3a70e940] invalidated after the last release of the connection object
default	21:54:31.032279-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:54:31.246033-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874215 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:31.456547-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:54:31.767782-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874216 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:31.768136-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:54:32.011583-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:32.609009-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:32.614943-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:32.614989-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:32.625695-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48957
default	21:54:32.643119-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874216 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:32.643440-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874218 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:32.692322-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:54:32.693172-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:32.693393-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:32.693474-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:32.693568-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:32.693782-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:32.693835-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:32.693862-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:32.694098-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:32.694130-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	21:54:32.693170-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:32.704405-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4650243 ioTS st: 4650243 ht: 47811.122498
error	21:54:32.708496-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:33.175551-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874218 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:33.304677-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 48960
default	21:54:33.388499-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:54:33.774939-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:33.785434-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:33.785486-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:33.909377-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874222 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:33.909634-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:54:33.976591-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:33.977277-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:33.977555-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:33.978671-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:33.979182-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:33.979213-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:33.979257-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:33.979463-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:33.979567-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:33.979600-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:33.980191-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:33.980215-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:33.994420-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4678688 ioTS st: 4678688 ht: 47812.412498
default	21:54:35.073999-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:35.074064-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:35.074911-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:35.074975-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:35.197623-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:35.204922-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:35.204977-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:35.208728-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874222 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:35.210426-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874239 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:35.237217-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:35.237674-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:35.237958-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:54:35.238106-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:35.238229-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:35.238253-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:35.238286-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:35.238431-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:35.238491-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:35.238517-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:35.238738-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:35.238754-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:35.254395-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4706472 ioTS st: 4706472 ht: 47813.672498
error	21:54:35.258945-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:35.493745-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 48973
default	21:54:35.494714-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 48973
default	21:54:35.895157-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874239 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:35.986633-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874256 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	21:54:36.023055-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:36.525233-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874256 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:36.559614-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:36.559856-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:54:36.605866-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d69260, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:36.605895-0500	VoiceOver	AudioConverter -> 0xb39d69260: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:36.605910-0500	VoiceOver	AudioConverter -> 0xb39d69260: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:54:36.606167-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:54:36.615230-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874257 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:36.615503-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	21:54:36.621623-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39dd10b0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:36.621645-0500	VoiceOver	AudioConverter -> 0xb39dd10b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:36.621656-0500	VoiceOver	AudioConverter -> 0xb39dd10b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
error	21:54:36.677670-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:36.997920-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 3
default	21:54:38.785455-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874257 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:38.809828-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:38.810070-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:54:38.849189-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39ce94d0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:38.849211-0500	VoiceOver	AudioConverter -> 0xb39ce94d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:38.849208-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874259 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:38.849220-0500	VoiceOver	AudioConverter -> 0xb39ce94d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
error	21:54:38.883930-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
error	21:54:39.118980-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:40.033056-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 3
default	21:54:40.077048-0500	VoiceOver	No list of permitted front apps returned
default	21:54:40.077244-0500	VoiceOver	No list of permitted front apps returned
default	21:54:40.094067-0500	VoiceOver	[0xb3a70e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:40.094180-0500	VoiceOver	[0xb3a70e800] invalidated after the last release of the connection object
default	21:54:40.136244-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:40.144834-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:40.144872-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:40.146575-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874259 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.147021-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874260 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.152152-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874260 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.155301-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874261 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.174943-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874261 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.183242-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874262 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.207690-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874262 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.208333-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874263 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.209074-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874263 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.209369-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874264 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.231247-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:40.232021-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.232012-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:40.232269-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:40.232296-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:40.232331-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	21:54:40.232336-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.232501-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:40.232577-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:40.232608-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:40.232860-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:40.232884-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:40.244419-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4816502 ioTS st: 4816502 ht: 47818.662498
error	21:54:40.248451-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:40.253865-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cec300, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:40.253887-0500	VoiceOver	AudioConverter -> 0xb39cec300: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:40.253900-0500	VoiceOver	AudioConverter -> 0xb39cec300: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:54:40.341981-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:40.344995-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:40.345032-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:40.346090-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874264 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.346993-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874265 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.348064-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874265 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.348404-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874266 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.375000-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:40.375350-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:40.375710-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.375778-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:40.376063-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:40.376090-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:40.376128-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:40.376297-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:40.376367-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:40.376403-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:40.376667-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:40.376693-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:40.384999-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:40.394943-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:40.394996-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:40.395843-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874266 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.396240-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874267 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.422828-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:40.423310-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.423660-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:54:40.423728-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.423885-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:40.423916-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:40.423957-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:40.424119-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:40.424206-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:40.424242-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:40.424535-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:40.424552-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:40.444494-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4820912 ioTS st: 4820912 ht: 47818.862498
error	21:54:40.445780-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:40.552124-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:40.554846-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:40.554878-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:40.555874-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874267 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:40.629688-0500	VoiceOver	No list of permitted front apps returned
default	21:54:40.629930-0500	VoiceOver	No list of permitted front apps returned
default	21:54:40.635232-0500	VoiceOver	[0xb3a70df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:40.635371-0500	VoiceOver	[0xb3a70df40] invalidated after the last release of the connection object
default	21:54:40.637485-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39cedd10, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:40.637515-0500	VoiceOver	AudioConverter -> 0xb39cedd10: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:40.637526-0500	VoiceOver	AudioConverter -> 0xb39cedd10: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:54:40.645998-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874268 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:40.683489-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:40.683787-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.684056-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:54:40.684047-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:40.684240-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:40.684264-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:40.684293-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:40.684431-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:40.684482-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:40.684511-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:40.684742-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:40.684758-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:40.704459-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4826646 ioTS st: 4826646 ht: 47819.122498
error	21:54:40.715830-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:41.350879-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:41.355035-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:41.355227-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:41.357172-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874268 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:41.358247-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874271 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:41.376458-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874271 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:41.376801-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874272 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:41.408004-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:41.408345-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:41.408627-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:41.408732-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:41.408931-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:41.408960-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:41.408994-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:41.409146-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:41.409214-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:41.409249-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:41.409459-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:41.409476-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:41.424478-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4842523 ioTS st: 4842523 ht: 47819.842498
error	21:54:41.430716-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:41.437926-0500	VoiceOver	No list of permitted front apps returned
default	21:54:41.444931-0500	VoiceOver	No list of permitted front apps returned
default	21:54:41.452606-0500	VoiceOver	[0xb3a70da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:41.452868-0500	VoiceOver	[0xb3a70da40] invalidated after the last release of the connection object
default	21:54:41.494426-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:41.504914-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:41.504962-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:41.507250-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874272 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:41.509357-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874274 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:41.536931-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:41.537245-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:41.537643-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	21:54:41.537636-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:41.537863-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:41.537890-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:41.537926-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:41.538083-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:41.538146-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:41.538177-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:41.538671-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:41.538687-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:41.554429-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4845390 ioTS st: 4845390 ht: 47819.972498
error	21:54:41.585920-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:41.668956-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39e1e700, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	21:54:41.669008-0500	VoiceOver	AudioConverter -> 0xb39e1e700: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	21:54:41.669018-0500	VoiceOver	AudioConverter -> 0xb39e1e700: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	21:54:41.683691-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:41.685111-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:41.685146-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:41.693082-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874274 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:41.697048-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874275 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:41.724812-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:41.725183-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:41.725569-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:41.725572-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:41.725833-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:41.725861-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:41.725895-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:41.726049-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:41.726125-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:41.726169-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:41.726429-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:41.726454-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:41.745016-0500	VoiceOver	AQSTL aq(0xb3ac8a800) start time resolved to: 4849580 ioTS st: 4849580 ht: 47820.162498
error	21:54:41.795886-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:41.799702-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 49001
default	21:54:42.176718-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:42.177916-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:42.177931-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:42.180893-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:42.182842-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:42.183058-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
default	21:54:42.188996-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:42.189667-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:42.189970-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:42.190017-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:42.190073-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:42.199388-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:42.199466-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:42.199522-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:42.199578-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:42.199718-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:42.199793-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:42.200587-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:42.201014-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:42.203243-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:42.203437-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
error	21:54:42.203507-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:42.203556-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:42.206448-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:42.206492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:42.206784-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:42.206831-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
fault	21:54:42.179244-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:42.206964-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:42.211899-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:42.216986-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:42.217012-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:42.217031-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:42.217044-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:42.179686-0500	runningboardd	Invalidating assertion 394-47902-49156 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:54:42.219197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:42.219310-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:42.219310-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
error	21:54:42.229211-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:42.229227-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2894 called from <private>
default	21:54:42.228497-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49178 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:42.228840-0500	runningboardd	Assertion 394-47902-49178 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:42.229238-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:42.229284-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:42.282464-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	21:54:42.316682-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xb3ac8a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	21:54:42.317512-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	21:54:42.320545-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:42.325808-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:42.347524-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:42.765985-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:42.766159-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:42.766278-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:42.766470-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:42.767890-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:42.768064-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
fault	21:54:42.963090-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:42.963500-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:42.964662-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:42.965202-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:43.000649-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 3
default	21:54:43.789201-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874275 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:44.001607-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:54:44.317226-0500	powerd	Process VoiceOver.47902 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874458 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	21:54:44.317682-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	21:54:44.427186-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	21:54:45.087894-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:45.088025-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:46.030318-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:54:48.047235-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:48.049782-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:48.049904-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:48.050117-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:48.050209-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:49.030425-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:54:50.186053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.187326-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2895)
default	21:54:50.187357-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2895 called from <private>
default	21:54:50.187366-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2895 called from <private>
fault	21:54:50.187314-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:50.188440-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:54:50.193840-0500	runningboardd	Invalidating assertion 394-47902-49182 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:54:50.190668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:50.190685-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:50.203233-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2895)
default	21:54:50.203293-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2895 called from <private>
default	21:54:50.203300-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2895 called from <private>
default	21:54:50.203304-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:50.203318-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:50.203481-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.203500-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2894 called from <private>
default	21:54:50.204008-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2894 called from <private>
default	21:54:50.209768-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:50.209821-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:50.211071-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.212352-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2894 called from <private>
default	21:54:50.212377-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2894 called from <private>
default	21:54:50.213969-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49194 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:50.212400-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:50.214081-0500	runningboardd	Assertion 394-47902-49194 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:50.212412-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:50.212419-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:50.214607-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2894 called from <private>
default	21:54:50.214848-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
error	21:54:50.214993-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	21:54:50.215871-0500	runningboardd	Invalidating assertion 394-47902-49194 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:54:50.215106-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:50.215156-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:50.215197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:50.215254-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.216584-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:50.216793-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:50.216803-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:50.218137-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:50.218173-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.230513-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:50.230552-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:50.230684-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2894)
default	21:54:50.236855-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2894)
default	21:54:50.237093-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2894 called from <private>
default	21:54:50.237104-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2894 called from <private>
default	21:54:50.237160-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2894 called from <private>
default	21:54:50.237170-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2894 called from <private>
default	21:54:50.245549-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x1010e4d40) Device ID: 85 (Input:No | Output:Yes): true
default	21:54:50.245634-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x1010e4d40)
default	21:54:50.247221-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49196 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:50.247422-0500	runningboardd	Assertion 394-47902-49196 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:50.245878-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:54:50.245913-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	21:54:50.245933-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
error	21:54:50.476872-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:54:50.895097-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:54:50.939738-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:54:50.939798-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2894 called from <private>
fault	21:54:50.940534-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:50.942652-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2894 called from <private>
default	21:54:50.942672-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2894 called from <private>
default	21:54:50.943104-0500	runningboardd	Invalidating assertion 394-47902-49196 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:54:50.944024-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:47902] from originator [osservice<com.apple.VoiceOver(501)>:47902] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-47902-49198 target:47902 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:54:50.944128-0500	runningboardd	Assertion 394-47902-49198 (target:[osservice<com.apple.VoiceOver(501)>:47902]) will be created as active
default	21:54:50.943742-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5f570, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
error	21:54:50.947792-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	21:54:50.943849-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:54:51.428905-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	21:54:51.475460-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2894 called from <private>
default	21:54:51.475663-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:51.476067-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:51.476212-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:54:51.476237-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x1010e4d40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:54:51.476246-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	21:54:51.476269-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:51.476279-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xb3aa2e418 (1C-77-54-18-C8-A3:output): Output stream format changed
default	21:54:51.477302-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb39d5c870, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	21:54:51.477793-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:51.478063-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:51.478457-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:51.478761-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:51.478857-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:51.479130-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:51.479166-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:51.479501-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xb3ac8a800:
default	21:54:51.479564-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	21:54:51.479572-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	21:54:51.479589-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	21:54:51.479619-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	21:54:51.479643-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	21:54:51.480104-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:51.480143-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:51.480278-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xb3ac8a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	21:54:51.480604-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	21:54:51.480886-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	21:54:51.481165-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	21:54:51.481362-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	21:54:51.481616-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	21:54:51.481651-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	21:54:51.481728-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xb3ac8a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	21:54:51.482049-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 1
default	21:54:51.482145-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	21:54:51.482208-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:51.482534-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:51.482563-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xb3aa2e418, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	21:54:51.498579-0500	powerd	Process VoiceOver.47902 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:07  id:21474874458 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	21:54:51.676572-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	21:54:51.686681-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	21:54:51.686832-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xb3ac8a800; ; [47902]; play>; running count now 0
default	21:54:51.705946-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	21:54:52.029159-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	21:54:52.596703-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea042, Nexy(48645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea040, VoiceOver(47902), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:54:52.596772-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:52.596838-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:52.597397-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	21:54:52.597569-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	21:54:53.785947-0500	VoiceOver	aqmeio@0xb3aa2e418 Stop id=85
default	21:54:53.785955-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	21:54:53.786429-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	21:54:55.033169-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:54:58.032815-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	21:54:58.679548-0500	VoiceOver	[0xb3a70e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	21:54:58.679708-0500	VoiceOver	[0xb3a70e6c0] invalidated after the last release of the connection object
default	21:54:59.365854-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	21:54:59.366414-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea040","name":"VoiceOver(47902)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:54:59.366573-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 64 stopping playing
default	21:54:59.366673-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:54:59.366750-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:54:59.366888-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 47902, Name = sid:0x1ea040, VoiceOver(47902), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:54:59.367625-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:54:59.367644-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:54:59.367423-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea040 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":47902}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea040, sessionType: 'prim', isRecording: false }, 
]
default	21:54:59.369869-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:54:59.369606-0500	runningboardd	Invalidating assertion 394-47902-49198 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.VoiceOver(501)>:47902]
default	21:54:59.369940-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:54:59.369966-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	21:54:59.369611-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	21:54:59.369751-0500	runningboardd	Invalidating assertion 394-328-49157 (target:[osservice<com.apple.VoiceOver(501)>:47902]) from originator [osservice<com.apple.powerd>:328]
default	21:54:59.475187-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring jetsam update because this process is not memory-managed
default	21:54:59.475208-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring suspend because this process is not lifecycle managed
default	21:54:59.475225-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring GPU update because this process is not GPU managed
default	21:54:59.475263-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Ignoring memory limit update because this process is not memory-managed
default	21:54:59.475282-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:47902] Skipping AppNap state - not lifecycle managed
default	21:54:59.480613-0500	gamepolicyd	Received state update for 47902 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	21:55:01.265964-0500	VoiceOver	No list of permitted front apps returned
