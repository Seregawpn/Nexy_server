default	14:48:18.530098-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8714
default	14:48:18.530644-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8714
default	14:48:23.297759-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8716
default	14:48:23.298171-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8716
default	14:48:31.156099-0500	loginwindow	VoiceOverDebug: _ScreenReaderToggleEnabled with option 72
default	14:48:31.158691-0500	loginwindow	VoiceOverDebug: after boostrap_look_up succeeded
default	14:48:31.158746-0500	loginwindow	VoiceOverDebug: calling _SCRStartup returned 0
default	14:48:31.172931-0500	UIKitSystem	Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001bc4e216c _AXSApplicationAccessibilitySetEnabled + 84
	1   libAccessibility.dylib              0x00000001bc4faa40 _AXSVoiceOverTouchSetEnabled + 368
	2   FuseBoard                           0x000000029abff42c -[FUAccessibilityServer _queue_applySettingWithKey:] + 696
	3   FuseBoard                           0x000000029ac013ec __76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke + 708
	4   libdispatch.dylib                   0x0000000196bb0b5c _dispatch_call_block_and_release + 32
	5   libdispatch.dylib                   0x0000000196bcaad4 _dispatch_client_callout + 16
	6   libdispatch.dylib                   0x0000000196bb94e8 _dispatch_lane_serial_drain + 740
	7   libdispatch.dylib                   0x0000000196bb9ff8 _dispatch_lane_invoke + 440
	8   libdispatch.dylib                   0x0000000196bbb308 _dispatch_workloop_invoke + 1612
	9   libdispatch.dylib                   0x0000000196bc4474 _dispa
default	14:48:31.681366-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78754.12, attribution={responsible={TCCDProcess: identifier=com.apple.VoiceOver, pid=8724, auid=501, euid=501, responsible_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, accessing={TCCDProcess: identifier=com.apple.LegacyUserDefaultsConverter, pid=8725, auid=501, euid=501, binary_path=/System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/Resources/LegacyUserDefaultsConverter}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78754, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	14:48:31.712743-0500	tccd	AUTHREQ_SUBJECT: msgID=78754.12, subject=com.apple.VoiceOver,
error	14:48:31.724858-0500	kernel	System Policy: LegacyUserDefaultsConverter(8725) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences/com.apple.VoiceOver4
error	14:48:31.725028-0500	kernel	System Policy: LegacyUserDefaultsConverter(8725) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
error	14:48:31.772263-0500	kernel	1 duplicate report for System Policy: LegacyUserDefaultsConverter(8725) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	14:48:31.847738-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	14:48:31.923691-0500	VoiceOver	[0x81b0503c0] activating connection: mach=false listener=false peer=false name=com.apple.carboncore.csnameddata
default	14:48:31.936435-0500	VoiceOver	VoiceOverDebug: ArgumentParser _initializeStartupOptions 72
default	14:48:31.938424-0500	VoiceOver	[0x81b050500] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:48:31.939136-0500	VoiceOver	[0x81b050640] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:48:31.940229-0500	VoiceOver	Received configuration update from daemon (initial)
default	14:48:31.961142-0500	VoiceOver	VoiceOverDebug: SCRWorkspace init
default	14:48:31.962126-0500	VoiceOver	[0x81b050a00] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:48:31.962668-0500	VoiceOver	[0x81b050b40] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:48:31.966085-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:48:31.966640-0500	VoiceOver	[0x81b050c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:31.967597-0500	VoiceOver	[0x81b050c80] invalidated after the last release of the connection object
default	14:48:31.967900-0500	VoiceOver	server port 0x00007f0b, session port 0x00007f0b
default	14:48:31.974114-0500	VoiceOver	New connection 0xcd95f main
default	14:48:31.977150-0500	VoiceOver	CHECKIN: pid=8724
default	14:48:31.982598-0500	runningboardd	Resolved pid 8724 to [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:31.982923-0500	runningboardd	_bundleMatchesProcessWithExecutablePath using realpath and comparing /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver and /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOverStarter
default	14:48:31.983030-0500	launchservicesd	CHECKIN:0x0-0x166166 8724 com.apple.VoiceOver
default	14:48:31.983175-0500	VoiceOver	CHECKEDIN: pid=8724 asn=0x0-0x166166 foreground=0
default	14:48:31.983311-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] is not RunningBoard jetsam managed.
default	14:48:31.983333-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] This process will not be managed.
default	14:48:31.983342-0500	runningboardd	Now tracking process: [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:31.983681-0500	VoiceOver	[0x81b050c80] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	14:48:31.983949-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	14:48:31.984116-0500	VoiceOver	[0x81b050dc0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:48:31.984124-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:31.984183-0500	loginwindow	-[Application setState:] | enter: <Application: 0xa9f9d1f40: VoiceOver> state 2
default	14:48:31.984281-0500	VoiceOver	[0x81a84d680] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x81b050dc0.peer[366].0x81a84d680
default	14:48:31.984206-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : VoiceOver
default	14:48:31.985495-0500	VoiceOver	FRONTLOGGING: version 1
default	14:48:31.985503-0500	VoiceOver	Registered, pid=8724 ASN=0x0,0x166166
default	14:48:31.985892-0500	WindowServer	cd95f[CreateApplication]: Process creation: 0x0-0x166166 (VoiceOver) connectionID: CD95F pid: 8724 in session 0x101
default	14:48:31.986934-0500	VoiceOver	[0x81b050f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:48:31.990230-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:8724" ID:404-366-33098 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:48:31.990318-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] reported to RB as running
default	14:48:31.990334-0500	runningboardd	Assertion 404-366-33098 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:31.990681-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:31.990696-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:31.990699-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:8724" ID:404-366-33099 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:48:31.990720-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Set darwin role to: UserInteractive
default	14:48:31.990739-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:31.990756-0500	runningboardd	Assertion 404-366-33099 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:31.990784-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:31.990818-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:31.992429-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:31.993180-0500	VoiceOver	BringForward: pid=8724 asn=0x0-0x166166 bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	14:48:31.993882-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:48:31.994600-0500	runningboardd	Invalidating assertion 404-366-33098 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	14:48:31.994798-0500	gamepolicyd	Hit the server for a process handle 1f79e0a700002214 that resolved to: [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:31.994899-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:31.995611-0500	VoiceOver	No persisted cache on this platform.
default	14:48:31.996273-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:48:31.997003-0500	VoiceOver	Post-registration system appearance: (HLTB: 1)
default	14:48:31.997121-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8724
default	14:48:31.997629-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8724
default	14:48:31.998841-0500	VoiceOver	FBSWorkspace: endpoint monitoring is disabled.
default	14:48:31.998852-0500	VoiceOver	FBSWorkspace: default shell endpoint is disabled.
default	14:48:31.998924-0500	VoiceOver	Initializing connection
default	14:48:31.998975-0500	VoiceOver	Removing all cached process handles
default	14:48:31.998999-0500	VoiceOver	Sending handshake request attempt #1 to server
default	14:48:31.999007-0500	VoiceOver	Creating connection to com.apple.runningboard
default	14:48:31.999017-0500	VoiceOver	[0x81b051180] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:48:32.999681-0500	runningboardd	Setting client for [osservice<com.apple.VoiceOver(501)>:8724] as ready
default	14:48:32.000354-0500	VoiceOver	Handshake succeeded
default	14:48:32.000370-0500	VoiceOver	Identity resolved as osservice<com.apple.VoiceOver(501)>
default	14:48:32.000732-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:32.001686-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.apple.VoiceOver token: 1e0000001d pid: 8724
default	14:48:32.002454-0500	VoiceOver	[0x81b051040] activating connection: mach=true listener=false peer=false name=com.apple.bird.token
default	14:48:32.007093-0500	VoiceOver	[0x81b051040] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:48:32.007325-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:32.008979-0500	VoiceOver	[0x81b0512c0] activating connection: mach=true listener=false peer=false name=com.apple.bird
default	14:48:32.009893-0500	VoiceOver	Created a new Process Instance Registry XPC connection (inactive)
default	14:48:32.009908-0500	VoiceOver	[0x81b051400] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:48:32.009996-0500	VoiceOver	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:48:32.010046-0500	VoiceOver	[0x81b051540] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:48:32.011044-0500	VoiceOver	[0x81b051540] Connection returned listener port: 0x9d03
default	14:48:32.012373-0500	VoiceOver	Registered process with identifier 8724-1183013
default	14:48:32.014046-0500	VoiceOver	[0x81b051680] activating connection: mach=true listener=false peer=false name=com.apple.AccessibilityVisualsAgent
default	14:48:32.029448-0500	VoiceOver	[C:1] Alloc <private>
default	14:48:32.029531-0500	VoiceOver	[0x81b051900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:48:32.031620-0500	WindowManager	Connection activated | (8724) VoiceOver
default	14:48:32.047543-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.apple.VoiceOver token: 2100000023 pid: 8724
default	14:48:32.047708-0500	VoiceOver	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x81ac5d360
 (
    "<NSAquaAppearance: 0x81ac5d220>",
    "<NSSystemAppearance: 0x81ac5d2c0>"
)>
default	14:48:32.052289-0500	VoiceOver	[0x81b051e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	14:48:32.055439-0500	VoiceOver	[0x81b051f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	14:48:32.095310-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:32.111140-0500	VoiceOver	New connection 0xf8513 secondary
default	14:48:32.115802-0500	distnoted	register name: kVoiceOverSpeechBecameActiveNotification object: kCFNotificationAnyObject token: 270000002a pid: 8724
default	14:48:32.115914-0500	distnoted	register name: kVoiceOverSpeechBecameIdleNotification object: kCFNotificationAnyObject token: 2800000029 pid: 8724
default	14:48:32.117006-0500	VoiceOver	[0x81b053200] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:48:32.123256-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:48:32.124280-0500	VoiceOver	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.apple.VoiceOver (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:48:32.125524-0500	VoiceOver	[0x81b053340] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	14:48:32.128038-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver>
default	14:48:32.132364-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:48:32.134614-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOChatFlavor, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	14:48:32.134841-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	14:48:32.135129-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:48:32.135145-0500	VoiceOver	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:48:32.135191-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:48:32.135334-0500	VoiceOver	[0x81b053480] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:48:32.136090-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=8724.2, attribution={requesting={TCCDProcess: identifier=com.apple.VoiceOver, pid=8724, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, },
default	14:48:32.142460-0500	tccd	AUTHREQ_SUBJECT: msgID=8724.2, subject=com.apple.VoiceOver,
default	14:48:32.145595-0500	VoiceOver	[0x81b053480] invalidated after the last release of the connection object
default	14:48:32.145638-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:48:32.147110-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.627, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=8724, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:32.147583-0500	tccd	AUTHREQ_SUBJECT: msgID=409.627, subject=com.apple.VoiceOver,
default	14:48:32.149538-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x8fcd7cc00 at /System/Library/CoreServices/VoiceOver.app
error	14:48:32.159275-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.apple.VoiceOver, pid=8724, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=409, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:48:32.160572-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.629, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=8724, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:48:32.161226-0500	tccd	AUTHREQ_SUBJECT: msgID=409.629, subject=com.apple.VoiceOver,
default	14:48:32.162131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x8fcd7cc00 at /System/Library/CoreServices/VoiceOver.app
default	14:48:32.170439-0500	VoiceOver	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:48:32.170461-0500	VoiceOver	AddInstanceForFactory: No factory registered for id <CFUUID 0x81b08c520> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	14:48:32.185213-0500	VoiceOver	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	14:48:32.185225-0500	VoiceOver	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	14:48:32.187906-0500	coreaudiod	>>> SIMULATE [com.apple.VoiceOver]
default	14:48:32.188035-0500	coreaudiod	<<< SIMULATE [com.apple.VoiceOver]
default	14:48:32.192435-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:48:32.192980-0500	VoiceOver	                AUHAL.cpp:420   AUHAL: (0x81a428040) Selecting device 85 from constructor
default	14:48:32.192992-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x81a428040)
default	14:48:32.192998-0500	VoiceOver	                AUHAL.cpp:681   SelectDevice: (0x81a428040) not already running
default	14:48:32.193006-0500	VoiceOver	                AUHAL.cpp:757   SelectDevice: (0x81a428040) nothing to teardown
default	14:48:32.193008-0500	VoiceOver	                AUHAL.cpp:762   SelectDevice: (0x81a428040) connecting device 85
default	14:48:32.193083-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:32.193164-0500	VoiceOver	                AUHAL.cpp:774   SelectDevice: (0x81a428040) created ioproc 0xa for device 85
default	14:48:32.193269-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x81a428040) adding 7 device listeners to device 85
default	14:48:32.193449-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x81a428040) adding 0 device delegate listeners to device 85
default	14:48:32.193458-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:48:32.193525-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:32.193536-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:48:32.193541-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:48:32.193552-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:48:32.193561-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:48:32.193654-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:32.193666-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:32.193671-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:32.193675-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x81a428040) removing 0 device listeners from device 0
default	14:48:32.193681-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x81a428040) removing 0 device delegate listeners from device 0
default	14:48:32.193684-0500	VoiceOver	                AUHAL.cpp:916   SelectDevice: <- (0x81a428040)
default	14:48:32.211124-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x81a428040) caller requesting device change from 85 to 85
default	14:48:32.211133-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x81a428040)
default	14:48:32.211138-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x81a428040) exiting with nothing to do
default	14:48:32.226368-0500	VoiceOver	[0x81b7704b0] Session created.
default	14:48:32.226380-0500	VoiceOver	[0x81b7704b0] Session created with Mach Service: <private>
default	14:48:32.226404-0500	VoiceOver	[0x81b053480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	14:48:32.226481-0500	VoiceOver	[0x81b7704b0] Session activated
default	14:48:33.028826-0500	VoiceOver	[0x81b770b40] Session created.
default	14:48:33.028836-0500	VoiceOver	[0x81b770b40] Session created with Mach Service: <private>
default	14:48:33.028846-0500	VoiceOver	[0x81c28b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	14:48:33.028963-0500	VoiceOver	[0x81b770b40] Session activated
default	14:48:33.047214-0500	VoiceOver	[0x81b770b90] Session created.
default	14:48:33.047224-0500	VoiceOver	[0x81b770b90] Session created with Mach Service: <private>
default	14:48:33.047252-0500	VoiceOver	[0x81c270140] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	14:48:33.047319-0500	VoiceOver	[0x81b770b90] Session activated
error	14:48:33.168354-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.178030-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.178071-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.182545-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.182570-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
default	14:48:33.211833-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	14:48:33.264394-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.264424-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.316334-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	14:48:33.316374-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
default	14:48:33.329148-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:33.329770-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:33.330317-0500	VoiceOver	       ACv2Workarounds.mm:51    com.apple.VoiceOver: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	14:48:33.330360-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:48:33.330491-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c3207b0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:48:33.330514-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:33.331490-0500	VoiceOver	[0x81c27c280] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	14:48:33.334166-0500	VoiceOver	LFSMCopySessionAgentEndpoint: enter
default	14:48:33.334341-0500	VoiceOver	[0x81c27c000] activating connection: mach=true listener=false peer=false name=com.apple.logind
default	14:48:33.334916-0500	VoiceOver	LFSMCopySessionAgentEndpoint: exit: result = 0
default	14:48:33.335083-0500	VoiceOver	[0x81c27c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:48:33.335644-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:33.335613-0500	VoiceOver	[SCROBrailleClient setDelegate:<SCROutputBrailleComponent: 0x81ac61000>]
default	14:48:33.335645-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	14:48:33.335724-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:33.337341-0500	VoiceOver	[0x81c27c640] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	14:48:33.337985-0500	VoiceOver	[0x81c27c8c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:33.338511-0500	VoiceOver	[0x81c27c8c0] invalidated after the last release of the connection object
default	14:48:33.340586-0500	VoiceOver	server port 0x0001f213, session port 0x00007f0b
default	14:48:33.342817-0500	VoiceOver	[0x81c27c8c0] activating connection: mach=true listener=false peer=false name=com.apple.backlightd
default	14:48:33.347899-0500	WindowServer	Connection added: IOHIDEventSystemConnection uuid:C9B825B8-7B2E-492C-BD2F-E36A2017F41A pid:8724 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x0 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	14:48:33.350428-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	14:48:33.350500-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	14:48:33.350513-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:33.350940-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:33.351010-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:33.355613-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 6700000061 pid: 8724
default	14:48:33.357970-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	14:48:33.358083-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	14:48:33.358097-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:33.358462-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:33.358524-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:33.358575-0500	VoiceOver	'Dock' is running
default	14:48:33.358835-0500	VoiceOver	'Setup Assistant' is not running
default	14:48:33.361377-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x81a428040) caller requesting device change from 85 to 85
default	14:48:33.361386-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x81a428040)
default	14:48:33.361392-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x81a428040) exiting with nothing to do
default	14:48:33.375790-0500	VoiceOver	[0x81c27d040] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:48:33.376945-0500	VoiceOver	[0x81c27d040] invalidated after the last release of the connection object
default	14:48:33.404834-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:33.405400-0500	VoiceOver	[0x81c27d040] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	14:48:33.405805-0500	VoiceOver	SignalReady: pid=8724 asn=0x0-0x166166
default	14:48:33.406227-0500	VoiceOver	SIGNAL: pid=8724 asn=0x0x-0x166166
default	14:48:33.407330-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	14:48:33.417609-0500	distnoted	register name: AXSSVoiceOverPunctuationCloudKitUpdateNotification object: kCFNotificationAnyObject token: 6800000060 pid: 8724
default	14:48:33.418186-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	14:48:33.418205-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	14:48:33.427593-0500	VoiceOver	[0x81b050dc0] Connection returned listener port: 0x7903
default	14:48:33.457042-0500	VoiceOver	[SCROBrailleClient handleCallback:] for key CallbackConnect
default	14:48:33.457299-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	14:48:33.504333-0500	VoiceOver	IOMainPort returned 0
default	14:48:33.526912-0500	VoiceOver	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	14:48:33.533066-0500	VoiceOver	Start service name com.apple.spotlight.IndexAgent
default	14:48:33.533780-0500	VoiceOver	[0x81c27d680] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	14:48:33.611795-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppVisible" ID:404-396-33102 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:33.611928-0500	runningboardd	Assertion 404-396-33102 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:33.613161-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:33.613228-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:33.613250-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:33.613317-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:33.613356-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:33.847332-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:33.978389-0500	VoiceOver	New connection 0x9b2fb secondary
default	14:48:34.029506-0500	VoiceOver	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	14:48:34.031984-0500	VoiceOver	Start service name com.apple.spotlightknowledged
default	14:48:34.045244-0500	VoiceOver	[GMS] availability notification token 312
default	14:48:34.099834-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.apple.VoiceOver: <private>
default	14:48:34.513544-0500	VoiceOver	[0x81c27cb40] activating connection: mach=true listener=false peer=false name=com.apple.pbs.fetch_services
default	14:48:34.514549-0500	VoiceOver	[0x81c27cb40] invalidated after the last release of the connection object
default	14:48:34.538794-0500	VoiceOver	No list of permitted front apps returned
default	14:48:34.540492-0500	VoiceOver	No list of permitted front apps returned
default	14:48:34.540606-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:34.541394-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:34.541604-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:34.573072-0500	VoiceOver	[0x81c6bfed0] Session created.
default	14:48:34.573092-0500	VoiceOver	[0x81c6bfed0] Session created with Mach Service: <private>
default	14:48:34.573108-0500	VoiceOver	[0x81c27db80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	14:48:34.573287-0500	VoiceOver	[0x81c6bfed0] Session activated
default	14:48:34.666728-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870194 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:48:34.667201-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33103 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:34.667301-0500	runningboardd	Assertion 404-337-33103 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:34.667747-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:34.667763-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:34.667777-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:34.667850-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:34.667865-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:34.668807-0500	VoiceOver	[0x81c758140] Session created.
default	14:48:34.668819-0500	VoiceOver	[0x81c758140] Session created with Mach Service: <private>
default	14:48:34.668829-0500	VoiceOver	[0x81c27cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	14:48:34.668939-0500	VoiceOver	[0x81c758140] Session activated
default	14:48:34.674469-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:48:34.675215-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:34.755927-0500	VoiceOver	AudioComponentPluginMgr.mm:114   registrationsChanged
default	14:48:34.760870-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	14:48:34.760920-0500	VoiceOver	AudioComponentPluginMgr.mm:906   First wildcard component search: 0/0/0
default	14:48:34.761862-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.765415-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	14:48:34.794660-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.795348-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.795571-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.795624-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.795890-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.795983-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.796175-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.796295-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.796494-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.796591-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.796773-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.796835-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.797023-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.797092-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.797274-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.797322-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.797518-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.797662-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.797990-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.798094-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.798264-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.798362-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.798553-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.798641-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.798818-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.798868-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.799077-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.799146-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.799452-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.799506-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.799721-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.799793-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.799998-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.800055-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.800280-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.800340-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.800571-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.800638-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.800812-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.800868-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.801044-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.801120-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.801315-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.801366-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.801533-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.801568-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.801785-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.801836-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.802093-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.802161-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.802331-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.802362-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.802580-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.802624-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.802890-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.803020-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.803205-0500	VoiceOver	[0x81c27c3c0] invalidated after the last release of the connection object
default	14:48:34.803256-0500	VoiceOver	[0x81c27d180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.803412-0500	VoiceOver	[0x81c27d180] invalidated after the last release of the connection object
default	14:48:34.803472-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.803626-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.803670-0500	VoiceOver	[0x81c27c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.803849-0500	VoiceOver	[0x81c27c780] invalidated after the last release of the connection object
default	14:48:34.803878-0500	VoiceOver	[0x81c27d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.804109-0500	VoiceOver	[0x81c27d2c0] invalidated after the last release of the connection object
default	14:48:34.804137-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.804286-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.804311-0500	VoiceOver	[0x81c27d7c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.804506-0500	VoiceOver	[0x81c27d7c0] invalidated after the last release of the connection object
default	14:48:34.804542-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.804697-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.804771-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.804976-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.805001-0500	VoiceOver	[0x81c27d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.805207-0500	VoiceOver	[0x81c27d2c0] invalidated after the last release of the connection object
default	14:48:34.805289-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.805555-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.805598-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.805831-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.805872-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.806063-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.806102-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.806319-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.806356-0500	VoiceOver	[0x81c27d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.806615-0500	VoiceOver	[0x81c27d2c0] invalidated after the last release of the connection object
default	14:48:34.806653-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.806909-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.806953-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.807152-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.807185-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.807403-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.807497-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.807679-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.807728-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.807894-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.807965-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.808132-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.808161-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.808341-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.808381-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.808543-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.808583-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.808751-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.808778-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.809092-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.809138-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.809307-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.809339-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.809504-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.809551-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.809708-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.809758-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.809957-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.810017-0500	VoiceOver	[0x81c27d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.810235-0500	VoiceOver	[0x81c27d400] invalidated after the last release of the connection object
default	14:48:34.810290-0500	VoiceOver	[0x81c27d540] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.810467-0500	VoiceOver	[0x81c27d540] invalidated after the last release of the connection object
default	14:48:34.812131-0500	VoiceOver	Class EXGetExtensionClass(void) returning EXConcreteExtension
default	14:48:34.812186-0500	VoiceOver	[0x81c27d540] activating connection: mach=true listener=false peer=false name=com.apple.pluginkit.pkd
default	14:48:34.812383-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Beginning discovery for flags: 1024, point: (null)
default	14:48:34.814538-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Completed discovery. Final # of matches: 1
default	14:48:34.815926-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.816143-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.816205-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Beginning discovery for flags: 1024, point: (null)
default	14:48:34.817318-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Completed discovery. Final # of matches: 1
default	14:48:34.819813-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.820003-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.820065-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Beginning discovery for flags: 1024, point: (null)
default	14:48:34.820996-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Completed discovery. Final # of matches: 1
default	14:48:34.822783-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.822985-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.823035-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Beginning discovery for flags: 1024, point: (null)
default	14:48:34.824136-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Completed discovery. Final # of matches: 1
default	14:48:34.825150-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.825736-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.825792-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Beginning discovery for flags: 1024, point: (null)
default	14:48:34.826796-0500	VoiceOver	[d <private>] <PKHost:0x81a141f00> Completed discovery. Final # of matches: 1
default	14:48:34.827898-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.828208-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.837001-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.837239-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.841274-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.841592-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.841739-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.841970-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.845148-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.845350-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.845415-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.845607-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.845678-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	14:48:34.845988-0500	VoiceOver	[0x81c27d900] invalidated after the last release of the connection object
default	14:48:34.849967-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Ready plugins sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	14:48:34.859786-0500	runningboardd	Launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}[0] is using uid 501 (divined from auid 501 euid 501)
default	14:48:34.859931-0500	runningboardd	Executing launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]} (Launching extension com.apple.ax.MauiTTSSupport.MauiAUSP(14844CB3-B750-5F5A-987A-D4BBC31613B5) for host 8724) from requestor: [osservice<com.apple.pluginkit.pkd(501)>:85446]
default	14:48:34.860066-0500	runningboardd	Creating and launching job for: xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	14:48:34.860243-0500	runningboardd	'(null)' Submitting extension overlay (host PID 8724, path /System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP):
<dictionary: 0xc9e94c8a0> { count = 3, transaction: 0, voucher = 0x0, contents =
	"XPCService" => <dictionary: 0xc9ee3c060> { count = 11, transaction: 0, voucher = 0x0, contents =
		"_ManagedBy" => <string: 0xc9f8387b0> { string cache = 0x0, length = 22, contents = "com.apple.runningboard" }
		"RunLoopType" => <string: 0xc9f83bf30> { string cache = 0x0, length = 9, contents = "NSRunLoop" }
		"Platform" => <int64: 0x914e65d49b1b40a7>: 1
		"JoinExistingSession" => <bool: 0x205277830>: true
		"_SandboxProfile" => <string: 0xc9f839fe0> { string cache = 0x0, length = 6, contents = "plugin" }
		"_AdditionalSubServices" => <dictionary: 0xc9ee3d080> { count = 1, transaction: 0, voucher = 0x0, contents =
			"apple-extension-service" => <bool: 0x205277830>: true
		}
		"PersonaEnterprise" => <int64: 0x914e65d49b1b5fe7>: 1001
		"_AdditionalProperties" => <dictionary: 0xc9ee3d680> { count = 1, transaction: 0, voucher = 0x0, contents =
			"RunningBoard" => <dictionary: 0xc9ee3e280> { count = 2, transaction: 0, voucher = 0x0, contents =
				"RunningBoardLaunchedIdentity" => <dictionary: 0xc9ee3c420> { count = 6, transaction: 0, voucher = 0x0, contents =
					"e" => <int64: 0x914e65d49b1b4f07>: 501
					"TYPE" => <int64: 0x914e65d49b1b408f>: 4
					"h" => <int64: 0x914e65d49b1a500f>: 8724
					"i" => <string: 0xc9f8399b0> { string cache = 0x0, length = 36, contents = "com.apple.ax.MauiTTSSupport.MauiAUSP" }
					"r" => <int64: 0x914e65d49b1b40bf>: 2
					"H" => <dictionary: 0xc9ee3d260> { count = 5, transaction: 0, voucher = 0x0, contents =
						"l" => <string: 0xc9f839740> { string cache = 0x0, length = 19, contents = "com.apple.VoiceOver" }
						"t" => <int64: 0x914e65d49b1b40bf>: 2
						"TYPE" => <int64: 0x914e65d49b1b409f>: 6
						"a" => <int64: 0x914e65d49b1b4f07>: 501
						"p" => <int64: 0x914e65d49b1b40af>: 0
					}
				}
				"RunningBoardLaunched" => <bool: 0x205277830>: true
			}
		}
		"_OmitSandboxParameters" => <bool: 0x205277830>: true
		"ServiceType" => <string: 0xc9f83b000> { string cache = 0x0, length = 11, contents = "Application" }
		"ProgramArguments" => <array: 0xc9f83a6d0> { count = 3, capacity = 8, contents =
			0: <string: 0xc9f839470> { string cache = 0x0, length = 125, contents = "/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP" }
			1: <string: 0xc9f8380c0> { string cache = 0x0, length = 15, contents = "-AppleLanguages" }
			2: <string: 0xc9f838390> { string cache = 0x0, length = 27, contents = "("en-CA", "ru-CA", "fr-CA")" }
		}
	}
	"RunningBoard" => <dictionary: 0xc9e94f960> { count = 1, transaction: 0, voucher = 0x0, contents =
		"Managed" => <bool: 0x205277830>: true
	}
	"CFBundlePackageType" => <string: 0xc9f838f90> { string cache = 0x0, length = 4, contents = "XPC!" }
}
default	14:48:34.875706-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Memory Limits: active 0 inactive 0
 <private>
default	14:48:34.875735-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] This process will be managed.
error	14:48:34.875766-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Memorystatus failed with unexpected error: Invalid argument (22)
default	14:48:34.875782-0500	runningboardd	Now tracking process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:34.875987-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-suspended (role: None) (endowments: (null))
default	14:48:34.876295-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] reported to RB as running
default	14:48:34.876616-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] got pid from ready request: 8729
default	14:48:34.876931-0500	WindowServer	Hit the server for a process handle 1c38727000002219 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:34.876995-0500	WindowServer	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	14:48:34.877172-0500	UIKitSystem	Hit the server for a process handle 1c38727000002219 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:34.877312-0500	UIKitSystem	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	14:48:34.877445-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:404-8724-33104 target:8729 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	14:48:34.877535-0500	runningboardd	Assertion 404-8724-33104 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]) will be created as active
default	14:48:34.878031-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Set jetsam priority to 40 [0] flag[1]
default	14:48:34.878055-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Resuming task.
default	14:48:34.878086-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Result 45 setting darwin role to UserInteractiveNonFocal: Operation not supported, falling back to setting priority
default	14:48:34.878113-0500	gamepolicyd	Hit the server for a process handle 1c38727000002219 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:34.878118-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Set darwin priority to: PRIO_DEFAULT
default	14:48:34.878241-0500	gamepolicyd	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	14:48:34.878410-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] prevented from droping Memory Limits from 0 to -1
default	14:48:34.881791-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-active (role: UserInteractiveNonFocal) (endowments: (null))
default	14:48:34.882004-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] acquired startup assertion
default	14:48:34.882313-0500	UIKitSystem	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	14:48:34.882395-0500	WindowServer	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	14:48:34.882461-0500	VoiceOver	Creating side-channel connection to com.apple.runningboard
default	14:48:34.882471-0500	VoiceOver	[0x81c27d400] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:48:34.883070-0500	VoiceOver	Hit the server for a process handle 1c38727000002219 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:34.883132-0500	gamepolicyd	Received state update for 8729 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	14:48:34.883248-0500	VoiceOver	[0x81c27d900] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP
default	14:48:34.883424-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Prepare using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	14:48:34.883444-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5] [<private>(<private>)] Sending prepareUsing to managed extension; this should launch it if not already running.
default	14:48:34.910010-0500	runningboardd	Setting client for [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] as ready
default	14:48:34.910852-0500	MauiAUSP	Identity resolved as xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	14:48:34.918323-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Begin using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	14:48:34.918627-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin loaded and ready for host
default	14:48:34.919121-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:404-8724-33105 target:8729 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown WantsForegroundResourcePriority )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	14:48:34.919194-0500	runningboardd	Assertion 404-8724-33105 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]) will be created as active
default	14:48:34.919760-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] Set jetsam priority to 100 [0] flag[1]
default	14:48:34.919869-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] prevented from droping Memory Limits from 0 to -1
default	14:48:34.923223-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] invalidating startup assertion
default	14:48:34.923383-0500	runningboardd	Invalidating assertion 404-8724-33104 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:34.923651-0500	VoiceOver	Class EXGetExtensionContextInternalClass(void) returning EXExtensionContextImplementation
default	14:48:34.930418-0500	VoiceOver	[0x81c27d2c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:48:34.930998-0500	VoiceOver	[0x81a146b80] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service
default	14:48:34.931216-0500	VoiceOver	[0x81c27d2c0] Connection returned listener port: 0x38e23
default	14:48:34.991908-0500	VoiceOver	[0x81a146d00] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x81c27d2c0.peer[8729].0x81a146d00
default	14:48:34.992366-0500	VoiceOver	[0x81c27d7c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.AUCrashHandlerService
default	14:48:35.006707-0500	VoiceOver	   AUOOPRenderPipePool.mm:167   Host obtained render pipe 35754169
default	14:48:35.007107-0500	VoiceOver	       AUOOPWorkgroups.mm:66    AUOOPWorkgroupManager: mutating workgroups.
default	14:48:35.007493-0500	VoiceOver	       AUOOPWorkgroups.mm:308   AUOOPWorkgroupManager: propagating workgroups.
default	14:48:35.007507-0500	VoiceOver	       AUOOPWorkgroups.mm:343   AUOOPWorkgroupManager: notifying workgroup listeners. Added :10, removed: 0
default	14:48:35.041779-0500	VoiceOver	[0x81c27d7c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	14:48:35.041826-0500	VoiceOver	        AUCrashHandler.mm:126   invalidated
default	14:48:35.370088-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:404-8729-33106 target:8729 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	14:48:35.370160-0500	runningboardd	Assertion 404-8729-33106 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]) will be created as inactive as start-time-defining assertions exist
default	14:48:35.375231-0500	runningboardd	Invalidating assertion 404-8729-33106 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:8724])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:8729]
default	14:48:35.506040-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c68a430, from  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32) to  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32)
default	14:48:35.506071-0500	VoiceOver	     AudioQueueObject.cpp:487   AudioQueueObject: aq@0x81b49a800: New output; format  1 ch,  22050 Hz, Float32 (passthrough? no)
default	14:48:35.506675-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0x81a20f200 created for movie spatialization.
default	14:48:35.506680-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0x81a20f2a0 created for music spatialization.
default	14:48:35.507569-0500	VoiceOver	           AQMEIO_HAL.cpp:2218  [AddSpatialPropertiesListener] objectID=85
default	14:48:35.507630-0500	VoiceOver	           AQMEIO_HAL.cpp:2240  aqmeio@0x81a9b6a18: [AddSpatialPropertiesListener] Installed listener 0x81b76e480
default	14:48:35.507790-0500	VoiceOver	          AQMixEngine.cpp:733   AQMEDevice (0x81a9d11d8) has neither a defaultOutStreamClient nor a defaultInStreamClient
default	14:48:35.508646-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	14:48:35.508691-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	14:48:35.508754-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c68a400, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:48:35.511907-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x81b49a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	14:48:35.511931-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x81b49a800:
default	14:48:35.511960-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	14:48:35.511965-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	14:48:35.511976-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	14:48:35.512793-0500	VoiceOver	       LoudnessManager.mm:1257  GetHardwarePlatformKey: found acoustic ID: 37
default	14:48:35.512803-0500	VoiceOver	       LoudnessManager.mm:1387  GetHardwarePlatformKey: GetHardwarePlatformKey(): hardware platform key is Mac
default	14:48:35.512819-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	14:48:35.512835-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	14:48:35.519078-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:35.519619-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:48:35.519804-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:35.521349-0500	VoiceOver	SpatializationManager.cpp:1418  Loaded preset file /System/Library/Audio/Tunings/AID37/AU/aid37-aumx-3dem-appl.aupreset
default	14:48:35.521739-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:35.522176-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:48:35.522198-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:35.522238-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:35.522531-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:35.522634-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	14:48:35.523017-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33107 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:48:35.523152-0500	runningboardd	Assertion 404-8724-33107 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:35.523777-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:35.524004-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:35.524055-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:35.524169-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:35.524200-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:35.527308-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:35.753393-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:48:35.795166-0500	VoiceOver	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:48:35.795834-0500	VoiceOver	[0x81c27c780] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:48:35.797945-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"PID":8724,"session_type":"Primary"} }
default	14:48:35.798038-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:48:35.798886-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 8724, name = VoiceOver
default	14:48:35.799236-0500	VoiceOver	    SessionCore_Create.mm:99    Created session 0x81a0b22e0 with ID: 0x1f501a
error	14:48:35.799796-0500	VoiceOver	Reporter disconnected. { function=sendMessage, reporterID=37469294690306 }
default	14:48:35.799833-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:35.800486-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:48:35.800576-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:48:35.800638-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:35.800678-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f501a, VoiceOver(8724), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:48:35.800700-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.800734-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:48:35.800746-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:48:35.800812-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:35.800841-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:48:35.800868-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'}
default	14:48:35.800863-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.800918-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.800909-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	14:48:35.801007-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:48:35.801021-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:35.800930-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:48:35.801049-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:35.801101-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	14:48:35.801290-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.801354-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.801378-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:35.801393-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	14:48:35.801407-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	14:48:35.801417-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
error	14:48:35.801469-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:48:35.801537-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:48:35.812705-0500	VoiceOver	           AQMEIO_HAL.cpp:1922  user headtracking mode for app com.apple.VoiceOver: 1
default	14:48:35.816241-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 3936 ioTS st: 3936 ht: 39284.270847
error	14:48:35.846620-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:37.048547-0500	VoiceOver	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	14:48:37.748117-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870194 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:48:37.750093-0500	VoiceOver	HIDAnalytics Set Value Send event com.apple.iokituser.hid.iohidpostevent
default	14:48:37.750123-0500	VoiceOver	HIDAnalytics Timer Send event com.apple.iokituser.hid.iohidpostevent
default	14:48:37.750211-0500	VoiceOver	HIDAnalytics Unregister Send event com.apple.iokituser.hid.iohidpostevent
default	14:48:37.803419-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:48:37.955044-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:48:38.344997-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	14:48:38.355518-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:38.355640-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:40.445672-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:48:40.445696-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:40.446314-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:48:40.446485-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 stopping playing
default	14:48:40.446552-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:48:40.446604-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:40.446703-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:48:40.446814-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:40.446868-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:48:40.446954-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:48:40.446969-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:40.447045-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:40.447119-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:40.447145-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	14:48:40.451670-0500	runningboardd	Invalidating assertion 404-8724-33107 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:40.451877-0500	runningboardd	Invalidating assertion 404-337-33103 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.powerd>:337]
default	14:48:40.554230-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:40.554243-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:40.554255-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:40.554312-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:40.554341-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:40.557634-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:42.539578-0500	VoiceOver	LSExceptions shared instance invalidated for timeout.
default	14:48:43.915088-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:43.915143-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:43.915153-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:43.919691-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:48:43.919733-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:48:43.919739-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:48:43.926672-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:48:43.926703-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:48:43.927498-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:43.927534-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:48:43.927544-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:48:43.929656-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:43.929687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:43.931452-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:43.933053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:48:43.933068-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:48:43.933105-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:48:43.933155-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:48:43.933192-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:43.933234-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:48:43.933269-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:43.933293-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:43.934407-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:43.935138-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:48:43.935380-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:48:43.935436-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:48:43.936378-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:48:43.936430-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:48:43.951664-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:48:43.951699-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:48:43.951796-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:43.956578-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:43.956985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:48:43.956998-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:48:43.957149-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:43.958971-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:43.959636-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:48:43.959654-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:48:43.960061-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:43.960215-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:48:43.960266-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:43.960290-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:43.960338-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:43.960367-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:48:43.960411-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:43.960458-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:43.960501-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:43.960589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:48:43.963056-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f4690, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:48:43.963181-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:43.963740-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:43.969044-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f4690, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:48:43.969213-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:43.969661-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:43.969677-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:43.969688-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:43.970192-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:44.528215-0500	VoiceOver	[0x81c27c3c0] activating connection: mach=true listener=false peer=false name=mul-xpc (Apple)_OpenStep
default	14:48:44.528579-0500	VoiceOver	[0x81c27da40] activating connection: mach=true listener=false peer=false name=com.apple.naturallanguaged
default	14:48:44.658591-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b496dc0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:44.658623-0500	VoiceOver	AudioConverter -> 0x81b496dc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:44.658637-0500	VoiceOver	AudioConverter -> 0x81b496dc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:44.664603-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33119 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:48:44.664779-0500	runningboardd	Assertion 404-8724-33119 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:44.666110-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:48:44.667599-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:48:44.667819-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:48:44.667834-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:48:44.668015-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:48:44.668147-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:48:44.668261-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'}
default	14:48:44.668669-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:48:44.668744-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:48:44.668427-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:48:44.668447-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	14:48:44.668968-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	14:48:44.669037-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:48:44.669202-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:44.669296-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:44.669327-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:48:44.669344-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	14:48:44.669353-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	14:48:44.669365-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
error	14:48:44.669419-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:48:44.669497-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:48:44.670968-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:44.670974-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33120 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:48:44.671010-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:44.671072-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:44.671153-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:44.671086-0500	runningboardd	Assertion 404-337-33120 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:44.671181-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:44.674326-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:48:44.674340-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:48:44.674372-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:48:44.674420-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:48:44.674448-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:48:44.675025-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:44.677512-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:48:45.978319-0500	VoiceOver	No list of permitted front apps returned
default	14:48:46.080343-0500	VoiceOver	No list of permitted front apps returned
default	14:48:46.282392-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8743
default	14:48:46.282860-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8743
default	14:48:46.289979-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:46.290721-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:46.290839-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:46.325118-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:46.325393-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:48:46.347410-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870368 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	14:48:46.452564-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:46.538522-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:46.538585-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:48:46.539093-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
fault	14:48:46.539294-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:46.539109-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:48:46.539114-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:48:46.542546-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:46.542589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:46.542757-0500	runningboardd	Invalidating assertion 404-8724-33119 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:46.550749-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:48:46.550765-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:48:46.552063-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:46.552089-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:48:46.552097-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:48:46.553555-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:46.553702-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:48:46.553828-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:48:46.554948-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:48:46.554965-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:48:46.554970-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:48:46.555617-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:48:46.557534-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33131 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:48:46.555627-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:48:46.555677-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:48:46.555725-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:48:46.555771-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:46.558650-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:48:46.557610-0500	runningboardd	Assertion 404-8724-33131 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
error	14:48:46.558780-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:48:46.562057-0500	runningboardd	Invalidating assertion 404-8724-33131 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:46.756221-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:48:47.054002-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:48:47.097297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2724 called from <private>
default	14:48:47.097335-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2724 called from <private>
fault	14:48:47.098078-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:47.099884-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:47.099905-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:47.101458-0500	runningboardd	Invalidating assertion 404-8724-33132 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:47.101727-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33134 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:48:47.101835-0500	runningboardd	Assertion 404-8724-33134 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:47.100547-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b4659e0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
error	14:48:47.105773-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:48:47.101253-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:47.116538-0500	VoiceOver	No list of permitted front apps returned
default	14:48:47.116786-0500	VoiceOver	No list of permitted front apps returned
default	14:48:47.116894-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:47.117650-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:47.117749-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:47.294605-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8746
default	14:48:47.295958-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8746
default	14:48:47.333062-0500	VoiceOver	No list of permitted front apps returned
default	14:48:47.351686-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8747
default	14:48:47.667623-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:48:47.711937-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2724 called from <private>
default	14:48:47.711982-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2724 called from <private>
default	14:48:47.712167-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:48:47.714284-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:48:47.714301-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:48:47.714412-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:47.714945-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:47.714960-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:47.714988-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:47.715500-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:48:47.715776-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:48:47.715995-0500	runningboardd	Invalidating assertion 404-8724-33134 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:48:47.716226-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33146 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:48:47.716336-0500	runningboardd	Assertion 404-8724-33146 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:48:48.273447-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2724 called from <private>
default	14:48:48.273668-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:48.274137-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b4cb9c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:48:48.274173-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:48:48.274255-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:48:48.274599-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:48.274713-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:48:48.274730-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:48:48.274739-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:48:48.274756-0500	VoiceOver	           AQMEIO_HAL.cpp:3593  0x81a9b6a18 (1C-77-54-18-C8-A3:output): lock contended, setting stream format change pending
error	14:48:48.283672-0500	VoiceOver	1C-77-54-18-C8-A3:output: Abandoning I/O cycle because reconfig pending
default	14:48:48.284092-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:48.284188-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:48.284218-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:48:48.284235-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:48:48.284928-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b4cb9f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:48:48.285141-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x81b49a800:
default	14:48:48.285195-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	14:48:48.285202-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	14:48:48.285224-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	14:48:48.285252-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	14:48:48.285275-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	14:48:48.285775-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x81b49a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	14:48:48.291837-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870368 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:48:48.292515-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870538 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:48:48.321314-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:48.321830-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:48.322393-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:48.322801-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	14:48:48.322662-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:48.322845-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:48.322890-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:48.323218-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:48.323338-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:48.323400-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:48.323949-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:48.323970-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:48:48.370004-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:49.335858-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8764
default	14:48:49.347727-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8764
default	14:48:49.483293-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8765
default	14:48:49.663281-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8766
default	14:48:49.664558-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8766
default	14:48:49.850156-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870538 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:48:50.058619-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:48:50.444596-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:50.454123-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:50.454267-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:50.622709-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54d440, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:50.623270-0500	VoiceOver	AudioConverter -> 0x81c54d440: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:50.623341-0500	VoiceOver	AudioConverter -> 0x81c54d440: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:50.701260-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: c0000000c pid: 8762
default	14:48:50.710051-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1600000012 pid: 8762
default	14:48:50.750432-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:50.750585-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:48:50.765223-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b452e20, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:50.765249-0500	VoiceOver	AudioConverter -> 0x81b452e20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:50.765259-0500	VoiceOver	AudioConverter -> 0x81b452e20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:50.796135-0500	VoiceOver	[0x81c27e080] invalidated after the last release of the connection object
default	14:48:50.924640-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:48:50.924706-0500	VoiceOver	CoreText note: Set a breakpoint on CTFontLogSystemFontNameRequest to debug.
default	14:48:51.092351-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870542 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:48:51.144094-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:48:51.144905-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:51.145154-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:48:51.145180-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:51.145215-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:51.145425-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
fault	14:48:51.145164-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:51.145545-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:51.145649-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:51.145925-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:51.145967-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:51.163727-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 342332 ioTS st: 342332 ht: 39299.617561
fault	14:48:51.145629-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:51.300066-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:48:51.457088-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:52.054680-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 8781
default	14:48:52.083456-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 2c00000025 pid: 8769
default	14:48:52.083894-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 360000002d pid: 8769
default	14:48:52.806242-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:48:52.861047-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8784
default	14:48:53.521680-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:53.521842-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:48:53.583322-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:53.583584-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:53.583812-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:48:53.584342-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:53.584486-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:53.590593-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:48:53.593653-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474870542 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:53.595396-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870559 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:53.605390-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:53.605607-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:48:53.638710-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:53.639280-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:53.639292-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:53.639513-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	14:48:53.639503-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:53.639535-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:53.639566-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:53.639719-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:53.639774-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:53.639800-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:53.639982-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:53.639993-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:53.653726-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 397237 ioTS st: 397237 ht: 39302.107561
error	14:48:53.679963-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:54.204492-0500	audioaccessoryd	MetricLog 'com.apple.bluetooth.SmartRouting.RouteCheck' : { "OnDemandCategory" : "NA", "WxBuildVersion" : "8B21", "WxStreamState" : "A2DP", "OtherTipiAudioCategory" : 100, "ProactiveRoutingWxRSSI" : -49, "BannerAction" : "NA", "WxProductID" : 8219, "LocalAudioCategory" : 201, "Trigger" : "NA", "Type" : "HijackFalseRoute", "OtherTipiDeviceIdleTime" : 0, "HijackScore" : 200, "BluetoothState" : "PoweredOn", "IsPlaying" : true, "Reason" : "NA", "Route" : "Bluetooth", "HijackAnswer" : "Accepted", "OtherTipiDevicePlayingApp" : "Unknown", "IsConnected" : true, "OtherTipiDevice" : "iPhone", "ActivePlayingApp" : "com.apple.VoiceOver", "InEar" : "YES", "HijackVersion" : "V2", "ProactiveRoutingTrigger" : "", }
default	14:48:54.797956-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:54.804162-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:54.804306-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:54.806292-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870559 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:54.867952-0500	VoiceOver	No list of permitted front apps returned
default	14:48:54.868164-0500	VoiceOver	No list of permitted front apps returned
default	14:48:54.868901-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:54.868999-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:48:54.878885-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:54.878993-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:48:54.888084-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:54.888222-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:48:54.891273-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:54.891355-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:48:54.893233-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870561 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:54.915191-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c7108a0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:54.915215-0500	VoiceOver	AudioConverter -> 0x81c7108a0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:54.915225-0500	VoiceOver	AudioConverter -> 0x81c7108a0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:54.926327-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:54.926901-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:54.926937-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:54.927181-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	14:48:54.927201-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:54.927206-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:54.927237-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:54.927377-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:54.927438-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:54.927468-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:54.927690-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:54.927705-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:54.937761-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:54.937963-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:48:54.943727-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 425682 ioTS st: 425682 ht: 39303.397561
default	14:48:54.947243-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:54.954138-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:54.954165-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:54.955384-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870561 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:54.955996-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870562 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
error	14:48:54.984039-0500	VoiceOver	     AudioQueueObject.cpp:5805  buffersCreatedAndDestroyed: aq@0x81b49a800: error allocating buffer
error	14:48:54.984956-0500	VoiceOver	     AudioQueueObject.cpp:5818  buffersCreatedAndDestroyed: aq@0x81b49a800: invalid buffer ID
default	14:48:54.991027-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:54.991383-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:54.991676-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:48:54.991820-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:54.991873-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:48:54.991894-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:54.991923-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:54.992063-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:54.992125-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:54.992155-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:54.992376-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:54.992392-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:55.003705-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 427006 ioTS st: 427006 ht: 39303.457561
error	14:48:55.023838-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:55.806269-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:48:56.283097-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54ddd0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:56.283118-0500	VoiceOver	AudioConverter -> 0x81c54ddd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:56.283129-0500	VoiceOver	AudioConverter -> 0x81c54ddd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:56.304001-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:48:56.304598-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54e280, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:56.304617-0500	VoiceOver	AudioConverter -> 0x81c54e280: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:56.304629-0500	VoiceOver	AudioConverter -> 0x81c54e280: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:56.318917-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:56.324208-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:56.324270-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:56.325551-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870562 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:56.325860-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870563 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:56.355381-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:48:56.356280-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:48:56.356507-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:48:56.356565-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	14:48:56.356441-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:56.356657-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:56.356846-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
fault	14:48:56.356929-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:56.356930-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:56.357050-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:56.357335-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:56.357348-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:56.369013-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:56.369261-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:48:56.373840-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 457215 ioTS st: 457215 ht: 39304.827561
error	14:48:56.436625-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	14:48:56.860660-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:56.900269-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:56.900367-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:48:56.993689-0500	VoiceOver	No list of permitted front apps returned
default	14:48:56.994230-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:48:56.994779-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:48:56.994858-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:48:57.001956-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:57.002109-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:48:57.029099-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:48:57.029319-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:48:57.031996-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b135c20, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:48:57.032025-0500	VoiceOver	AudioConverter -> 0x81b135c20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:48:57.032037-0500	VoiceOver	AudioConverter -> 0x81b135c20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:48:57.040980-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:48:57.048650-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:48:57.054476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:48:57.054557-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:48:57.059714-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870563 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:57.061383-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870564 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:48:57.091260-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:48:57.091943-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:57.092185-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:48:57.092338-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:48:57.092415-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:48:57.092447-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:48:57.092502-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:48:57.092684-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:48:57.092752-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:48:57.092792-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:48:57.093018-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:48:57.093035-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:48:57.103812-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 473312 ioTS st: 473312 ht: 39305.557561
error	14:48:57.153693-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:48:58.803622-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:00.055213-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474870564 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:00.264453-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:00.604729-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870566 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:00.612236-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:49:00.695158-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:01.769983-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:04.769926-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:06.305494-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474870566 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:06.516594-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:06.904602-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:06.914532-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:06.914649-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:07.786617-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:09.013909-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:49:09.013935-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:09.014373-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:10.803313-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:13.769979-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:14.689163-0500	VoiceOver	No list of permitted front apps returned
default	14:49:14.764455-0500	VoiceOver	No list of permitted front apps returned
default	14:49:14.795264-0500	VoiceOver	No list of permitted front apps returned
default	14:49:14.798062-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b135ad0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:14.798094-0500	VoiceOver	AudioConverter -> 0x81b135ad0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:14.798104-0500	VoiceOver	AudioConverter -> 0x81b135ad0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:14.808063-0500	VoiceOver	No list of permitted front apps returned
default	14:49:14.810884-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:14.811594-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:14.811691-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:14.832519-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:14.832698-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:14.875900-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:14.876048-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:49:14.878038-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54f270, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:14.878087-0500	VoiceOver	AudioConverter -> 0x81c54f270: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:14.878099-0500	VoiceOver	AudioConverter -> 0x81c54f270: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:14.883672-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:14.890065-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:14.894655-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870570 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:14.901777-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:49:14.930639-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:14.931147-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:14.931250-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:49:14.931348-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:14.931448-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:14.931472-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:14.931499-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:14.931643-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:14.931696-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:14.931742-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:14.931957-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:14.931972-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:14.943730-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 866685 ioTS st: 866685 ht: 39323.397561
error	14:49:15.069900-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:16.806189-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:17.366655-0500	VoiceOver	No list of permitted front apps returned
fault	14:49:17.375272-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:17.384422-0500	VoiceOver	No list of permitted front apps returned
default	14:49:17.417927-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:17.418895-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:17.418800-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:17.433186-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:17.433362-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:17.456459-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:17.456618-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:49:17.458620-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c713de0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:17.458658-0500	VoiceOver	AudioConverter -> 0x81c713de0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:17.458677-0500	VoiceOver	AudioConverter -> 0x81c713de0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:17.466653-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:17.467557-0500	VoiceOver	No list of permitted front apps returned
default	14:49:17.472186-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:17.474479-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:17.474560-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:17.488015-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474870570 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:17.488420-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870571 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:17.537702-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:17.537949-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:49:17.538254-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:17.538383-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:49:17.538561-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:17.538580-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:17.538610-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:17.538743-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:17.538798-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:17.538826-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:17.539016-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:17.539030-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:49:17.586430-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:19.786798-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:20.505000-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870571 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:20.711575-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:21.023550-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870572 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:21.023916-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:49:21.123792-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:22.803203-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:25.769866-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:27.705193-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474870572 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:27.913894-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:28.304913-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:28.314636-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:28.314745-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:28.539339-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:49:28.539410-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:49:28.810286-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:29.896295-0500	VoiceOver	No list of permitted front apps returned
default	14:49:29.972258-0500	VoiceOver	No list of permitted front apps returned
default	14:49:29.984617-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c713330, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:29.984637-0500	VoiceOver	AudioConverter -> 0x81c713330: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:29.984647-0500	VoiceOver	AudioConverter -> 0x81c713330: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:29.992065-0500	VoiceOver	No list of permitted front apps returned
default	14:49:29.995198-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:29.995690-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:29.995759-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:29.997792-0500	VoiceOver	No list of permitted front apps returned
default	14:49:30.000895-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:30.001003-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:49:30.033927-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:30.034003-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:30.041376-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:30.046325-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:30.052062-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870575 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:30.052336-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:49:30.063987-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8807
default	14:49:30.067956-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8807
default	14:49:30.078986-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:30.079547-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:30.079595-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:49:30.079799-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:30.079823-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:30.079857-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:49:30.079812-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:30.080022-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:30.080081-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:30.080110-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:30.080324-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:30.080339-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:30.093766-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1200743 ioTS st: 1200743 ht: 39338.547561
error	14:49:30.323478-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:31.514657-0500	VoiceOver	No list of permitted front apps returned
fault	14:49:31.522414-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:31.539442-0500	VoiceOver	No list of permitted front apps returned
default	14:49:31.562062-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:31.562728-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:31.562856-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:31.609078-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:31.609397-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:49:31.615978-0500	VoiceOver	No list of permitted front apps returned
default	14:49:31.622309-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:31.622482-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:31.624926-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c710ed0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:31.624954-0500	VoiceOver	AudioConverter -> 0x81c710ed0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:31.624963-0500	VoiceOver	AudioConverter -> 0x81c710ed0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:31.632949-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:31.637830-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:31.644500-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:31.644582-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:31.669097-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870575 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:31.669481-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870576 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:31.719670-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:31.719944-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:49:31.720212-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:31.720252-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:49:31.720453-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:31.720479-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:31.720514-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:31.720674-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:31.720730-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:31.720753-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:31.720942-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:31.720957-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:31.733757-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1236906 ioTS st: 1236906 ht: 39340.187561
error	14:49:31.764019-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:31.803045-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:34.685208-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870576 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:34.803098-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:34.896012-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:35.211261-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870577 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:35.211636-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:49:35.311614-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:35.330389-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:35.330518-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:49:37.803127-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:40.769973-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:41.885373-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474870577 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:42.088888-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:42.484946-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:42.494609-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:42.494736-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:43.803138-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:44.593962-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:49:44.594027-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:44.594866-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:45.016756-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c717d50, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:45.016788-0500	VoiceOver	AudioConverter -> 0x81c717d50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:45.016803-0500	VoiceOver	AudioConverter -> 0x81c717d50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:45.845428-0500	VoiceOver	No list of permitted front apps returned
default	14:49:45.946386-0500	VoiceOver	No list of permitted front apps returned
default	14:49:45.947356-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:45.948131-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:45.948254-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:46.093350-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.099216-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:46.099415-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:49:46.108179-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:46.108293-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8814
default	14:49:46.108351-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:46.108697-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8814
default	14:49:46.113097-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:46.113248-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:49:46.114468-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.114526-0500	VoiceOver	Application set focus not permitted for (null)
default	14:49:46.114981-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.115463-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.118077-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:46.119046-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:46.119268-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:46.181955-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f2b50, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:46.182140-0500	VoiceOver	AudioConverter -> 0x81c6f2b50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:46.182199-0500	VoiceOver	AudioConverter -> 0x81c6f2b50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
error	14:49:46.337898-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:46.803081-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:46.822689-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.822971-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:49:46.822999-0500	VoiceOver	No list of permitted front apps returned
default	14:49:46.823699-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:49:46.823817-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:49:46.841345-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:46.844661-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:46.844753-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:46.848112-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870580 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:46.849021-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870581 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:46.867449-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:46.867743-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:49:46.867995-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:46.868113-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:49:46.868311-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:46.868335-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:46.868381-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:46.868613-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:46.868671-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:46.868706-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:46.868957-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:46.868974-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:46.883788-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1570964 ioTS st: 1570964 ht: 39355.337561
error	14:49:46.905581-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:46.962539-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8817
default	14:49:48.384557-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870581 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:48.615298-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8823
default	14:49:48.615793-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8823
default	14:49:48.975485-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8827
default	14:49:48.981448-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8827
default	14:49:49.193217-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8829
default	14:49:49.803998-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:50.072319-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f3030, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:50.072344-0500	VoiceOver	AudioConverter -> 0x81c6f3030: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:50.072354-0500	VoiceOver	AudioConverter -> 0x81c6f3030: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:50.157453-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:50.157664-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:50.175770-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:49:50.193629-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:50.193932-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:50.208340-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:49:50.395162-0500	VoiceOver	[0x81b0503c0] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	14:49:50.519206-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:50.519339-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:49:50.562100-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:50.566972-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:50.574398-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:50.574443-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:50.589512-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870589 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:50.590094-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870590 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:50.634666-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:50.635360-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:50.635554-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:49:50.635727-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:50.635772-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:50.635808-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:50.635852-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:50.636033-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:50.636109-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:50.636151-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:50.636554-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:50.636574-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:49:50.680641-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:51.724057-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:51.724317-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:49:51.778336-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:51.778619-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:51.778821-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:49:51.780446-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:51.784598-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:51.784650-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:51.786307-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870590 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:51.787417-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870593 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:51.799794-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
error	14:49:51.853343-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:52.802983-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:53.076261-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:53.084316-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:53.084362-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:53.085880-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870593 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:53.129734-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:53.129859-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:49:53.147586-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870594 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:53.147794-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b15f960, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:53.147815-0500	VoiceOver	AudioConverter -> 0x81b15f960: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:53.147826-0500	VoiceOver	AudioConverter -> 0x81b15f960: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:53.169523-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:53.169713-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:49:53.170909-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54cea0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:53.170928-0500	VoiceOver	AudioConverter -> 0x81c54cea0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:53.170958-0500	VoiceOver	AudioConverter -> 0x81c54cea0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:53.174274-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:53.174449-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:53.181427-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:49:53.181998-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:49:53.182044-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:53.182200-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:53.182228-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:53.182255-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:49:53.182374-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:53.182403-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:53.182480-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:53.182509-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:53.182730-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:53.182745-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:53.193808-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1710102 ioTS st: 1710102 ht: 39361.647561
error	14:49:53.216285-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:53.217813-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:53.217911-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:49:53.222688-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:53.224179-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:53.224215-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:53.226690-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870594 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:53.226970-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870595 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:53.259792-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:53.260097-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:49:53.260360-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:53.260399-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:49:53.260595-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:53.260615-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:53.260641-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:53.260771-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:53.260828-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:53.260854-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:53.261046-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:53.261059-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:53.273777-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1711867 ioTS st: 1711867 ht: 39361.727561
error	14:49:53.297542-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:54.573286-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:54.573673-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:49:54.584462-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54f3c0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:49:54.584491-0500	VoiceOver	AudioConverter -> 0x81c54f3c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:49:54.584502-0500	VoiceOver	AudioConverter -> 0x81c54f3c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:49:54.598267-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:49:54.604631-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:54.614244-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:54.614290-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:54.615751-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870595 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:54.616106-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870596 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	14:49:54.650624-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:54.651242-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:54.651349-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:49:54.651465-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:54.651559-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:54.651585-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:54.651623-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:54.651783-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:54.651839-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:54.651871-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:54.652060-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:54.652075-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:49:54.663783-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1742517 ioTS st: 1742517 ht: 39363.117561
error	14:49:54.724600-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	14:49:55.372385-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:55.384808-0500	VoiceOver	No list of permitted front apps returned
default	14:49:55.502444-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:49:55.502587-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:49:55.517328-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:49:55.524471-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:49:55.524550-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:49:55.560051-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:49:55.560681-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:55.560975-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:49:55.561094-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:49:55.561227-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:49:55.561258-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:49:55.561320-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:49:55.561501-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:49:55.561568-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:49:55.561610-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:49:55.561836-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:49:55.561852-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:49:55.630779-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:49:55.806138-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:56.433204-0500	VoiceOver	[0x81b053200] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	14:49:56.433237-0500	VoiceOver	AudioComponentPluginMgr.mm:326   registration server connection interrupted
default	14:49:58.769764-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:49:59.145374-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870597 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:49:59.355698-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:49:59.697468-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870598 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:49:59.697772-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:49:59.788800-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:00.049233-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f2cd0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:00.049263-0500	VoiceOver	AudioConverter -> 0x81c6f2cd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:00.049272-0500	VoiceOver	AudioConverter -> 0x81c6f2cd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:01.429167-0500	VoiceOver	No list of permitted front apps returned
fault	14:50:01.435159-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:01.530816-0500	VoiceOver	No list of permitted front apps returned
default	14:50:01.531651-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:01.532314-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:01.532464-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
fault	14:50:01.666160-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:50:01.672132-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:01.673424-0500	VoiceOver	No list of permitted front apps returned
default	14:50:01.678056-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:01.678272-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:50:01.683880-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8836
default	14:50:01.684175-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:01.684406-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:50:01.684376-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8836
default	14:50:01.692961-0500	VoiceOver	No list of permitted front apps returned
default	14:50:01.693732-0500	VoiceOver	No list of permitted front apps returned
default	14:50:01.704859-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:01.704981-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:01.745455-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:50:01.764080-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:01.764113-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:01.764904-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870601 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:01.765300-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870602 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
fault	14:50:01.792212-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:01.792511-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:01.792536-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:01.792701-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:01.792723-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:01.792762-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:01.792901-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:01.792956-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:01.792984-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:01.793184-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:01.793195-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:01.803836-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1899955 ioTS st: 1899955 ht: 39370.257561
error	14:50:01.827936-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:02.325081-0500	VoiceOver	No list of permitted front apps returned
default	14:50:02.327877-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:02.327950-0500	VoiceOver	No list of permitted front apps returned
default	14:50:02.328691-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:02.328855-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:02.343334-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:02.344516-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:02.344579-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:02.347332-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870602 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:02.347709-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870603 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:02.365536-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:02.365799-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:02.366178-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:02.366163-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:02.366394-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:02.366417-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:02.366452-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:02.366588-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:02.366648-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:02.366676-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:02.366872-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:02.366887-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:02.383774-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1912744 ioTS st: 1912744 ht: 39370.837561
error	14:50:02.410942-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:02.687438-0500	VoiceOver	No list of permitted front apps returned
default	14:50:03.884495-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870603 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:04.096981-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:04.161534-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8844
default	14:50:04.495943-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:04.496009-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:04.576247-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8847
default	14:50:04.903364-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8849
default	14:50:05.846496-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b496d60, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:05.846527-0500	VoiceOver	AudioConverter -> 0x81b496d60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:05.846541-0500	VoiceOver	AudioConverter -> 0x81b496d60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:05.896565-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:05.896789-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:05.903816-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b134db0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:05.903845-0500	VoiceOver	AudioConverter -> 0x81b134db0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:05.903861-0500	VoiceOver	AudioConverter -> 0x81b134db0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:05.914406-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:05.917670-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:05.917927-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:50:05.929677-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870604 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:05.930948-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:05.931122-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:05.931183-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:50:05.959891-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:05.960562-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:05.960629-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:05.960793-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:05.960869-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:05.960894-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:05.960942-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:05.961112-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:05.961179-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:05.961219-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:05.961472-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:05.961488-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:05.973788-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 1991904 ioTS st: 1991904 ht: 39374.427561
error	14:50:06.048536-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:06.940856-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8853
default	14:50:06.944258-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8853
default	14:50:07.519213-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:07.519387-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:50:07.540530-0500	VoiceOver	[0x81c27da40] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	14:50:07.564577-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:07.564735-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:07.564855-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:50:07.567089-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:07.572120-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:07.572319-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:07.574539-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:07.574614-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:07.583288-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870604 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:07.584157-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870605 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:07.618026-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:50:07.618637-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:07.618690-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:07.618854-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:07.618877-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:07.618908-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:50:07.618908-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:07.619080-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:07.619141-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:07.619168-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:07.619390-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:07.619407-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:07.633781-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2028507 ioTS st: 2028507 ht: 39376.087561
error	14:50:07.657022-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:07.806052-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:08.685446-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:08.694843-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:08.694928-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:08.696870-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870605 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:08.784252-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:08.784467-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:08.792438-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c712160, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:08.792483-0500	VoiceOver	AudioConverter -> 0x81c712160: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:08.792496-0500	VoiceOver	AudioConverter -> 0x81c712160: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:08.793963-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:08.809330-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870606 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:08.847332-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:08.847757-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:50:08.848048-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:08.848185-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:08.848396-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:08.848424-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:08.848464-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:08.848622-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:08.848686-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:08.848721-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:08.848941-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:08.848957-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:08.863828-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2055629 ioTS st: 2055629 ht: 39377.317561
error	14:50:08.927747-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:10.806010-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:12.930279-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:12.930459-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
fault	14:50:12.941097-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:12.939414-0500	VoiceOver	No list of permitted front apps returned
default	14:50:13.002046-0500	VoiceOver	No list of permitted front apps returned
default	14:50:13.018629-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:13.019031-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:13.019102-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:13.040287-0500	VoiceOver	No list of permitted front apps returned
default	14:50:13.040556-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:13.040688-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:50:13.053277-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:13.054555-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:13.054639-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:13.089317-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:13.089920-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:13.090255-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:13.090322-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:13.090497-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:13.090543-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:13.090598-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:13.090776-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:13.090851-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:13.090887-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:13.091144-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:13.091161-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:50:13.149770-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:13.772608-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	14:50:15.288136-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:15.294388-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8858
default	14:50:15.295042-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8858
default	14:50:16.111557-0500	VoiceOver	No list of permitted front apps returned
default	14:50:16.111814-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:16.111836-0500	VoiceOver	No list of permitted front apps returned
default	14:50:16.112423-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:16.112534-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:16.133892-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:16.144517-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:16.144704-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:16.145689-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870607 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:16.146609-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870608 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:16.174638-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:16.175033-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:50:16.175415-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:16.175493-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:16.175795-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:16.175832-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:16.175910-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:16.176223-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:16.176325-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:16.176393-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:16.176716-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:16.176743-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:16.193876-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2217257 ioTS st: 2217257 ht: 39384.647561
error	14:50:16.238862-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:17.694339-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870608 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:17.904117-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:18.294545-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:18.401468-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8870
default	14:50:18.415343-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8870
default	14:50:18.832628-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 8873
default	14:50:18.844440-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8873
default	14:50:19.805881-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:19.821326-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54e1c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:19.821372-0500	VoiceOver	AudioConverter -> 0x81c54e1c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:19.821392-0500	VoiceOver	AudioConverter -> 0x81c54e1c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:19.868966-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:19.869110-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:50:19.883069-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:19.883227-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:50:19.886814-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:19.896071-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:19.896188-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:50:19.900651-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870611 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:19.901010-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:50:19.937585-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:50:19.938231-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:19.938262-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:19.938438-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:19.938460-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:19.938488-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:50:19.938704-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:19.938744-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:19.938838-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:19.938864-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:19.939085-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:19.939100-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:19.953872-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2300166 ioTS st: 2300166 ht: 39388.407561
error	14:50:20.049084-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:20.430032-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 8876
default	14:50:21.034348-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:21.034573-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:50:21.063810-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:21.063986-0500	VoiceOver	[0x81c27ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:21.064224-0500	VoiceOver	[0x81c27ebc0] invalidated after the last release of the connection object
default	14:50:21.064964-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:21.065031-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:21.067723-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:21.075035-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:21.075349-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:21.079128-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870611 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:21.080101-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870612 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:21.111598-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:21.111949-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:50:21.112226-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:21.112287-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:21.112493-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:21.112519-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:21.112557-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:21.112704-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:21.112756-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:21.112783-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:21.112981-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:21.112996-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:21.123859-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2325965 ioTS st: 2325965 ht: 39389.577561
error	14:50:21.149908-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:22.454368-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:22.464881-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:22.464966-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:22.466535-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870612 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:22.523972-0500	VoiceOver	No list of permitted front apps returned
default	14:50:22.524178-0500	VoiceOver	No list of permitted front apps returned
default	14:50:22.525095-0500	VoiceOver	[0x81c27e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:22.525206-0500	VoiceOver	[0x81c27e800] invalidated after the last release of the connection object
default	14:50:22.536771-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:22.536883-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:22.547497-0500	VoiceOver	[0x81c27de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:22.547651-0500	VoiceOver	[0x81c27de00] invalidated after the last release of the connection object
default	14:50:22.551069-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:22.551141-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:50:22.552237-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870613 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:22.578217-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b137e40, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:22.578238-0500	VoiceOver	AudioConverter -> 0x81b137e40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:22.578246-0500	VoiceOver	AudioConverter -> 0x81b137e40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:22.589222-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:50:22.589824-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:22.589916-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:22.590039-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:22.590063-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:22.590095-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:50:22.590197-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:22.590254-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:22.590336-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:22.590367-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:22.590615-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:22.590631-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:22.603928-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2358599 ioTS st: 2358599 ht: 39391.057561
default	14:50:22.608082-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:22.608227-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:50:22.617000-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:22.624218-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:22.624243-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:22.626182-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870613 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:22.626836-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870614 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:22.655293-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:22.655572-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:50:22.655822-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:22.655934-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:22.656094-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:22.656115-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:22.656141-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:22.656270-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:22.656327-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:22.656351-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:22.656526-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:22.656538-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:22.673851-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2360143 ioTS st: 2360143 ht: 39391.127561
error	14:50:22.694478-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:22.723639-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:23.889503-0500	VoiceOver	No list of permitted front apps returned
default	14:50:23.889849-0500	VoiceOver	No list of permitted front apps returned
default	14:50:23.911006-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:23.911267-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:50:23.923995-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c54dc80, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:23.924036-0500	VoiceOver	AudioConverter -> 0x81c54dc80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:23.924072-0500	VoiceOver	AudioConverter -> 0x81c54dc80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:23.945930-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:23.947777-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f39f0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:23.947805-0500	VoiceOver	AudioConverter -> 0x81c6f39f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:23.947822-0500	VoiceOver	AudioConverter -> 0x81c6f39f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:23.966125-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:23.974456-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:23.974562-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:23.976640-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870614 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:23.977106-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870616 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:24.009855-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:24.010678-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:24.010701-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:24.010915-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:24.010946-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:24.010989-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:50:24.011023-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:24.011166-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:24.011231-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:24.011269-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:24.011513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:24.011533-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:24.023821-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2389911 ioTS st: 2389911 ht: 39392.477561
error	14:50:24.076014-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:24.970889-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:24.971024-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
fault	14:50:24.974035-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:24.982779-0500	VoiceOver	No list of permitted front apps returned
default	14:50:25.055454-0500	VoiceOver	No list of permitted front apps returned
default	14:50:25.126516-0500	VoiceOver	[0x81c27df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:25.126746-0500	VoiceOver	[0x81c27df40] invalidated after the last release of the connection object
default	14:50:25.140866-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:25.144798-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:25.144882-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:25.149483-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474870616 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:25.149990-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870617 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:25.176578-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:25.177099-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:25.177439-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:25.177499-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:25.177704-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:25.177736-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:25.177793-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:25.177990-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:25.178056-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:25.178106-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:25.178375-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:25.178395-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:50:25.236675-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:25.786274-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:28.275425-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870617 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:28.487590-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:28.803023-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:28.827264-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870620 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:28.827604-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:50:28.917980-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:29.607115-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:29.607345-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:50:29.992106-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:29.992342-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:50:31.802932-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:32.301260-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:32.301343-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:32.301374-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:32.301414-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:34.525804-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474870620 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:34.739373-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:34.772517-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:35.124926-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:35.134521-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:35.134625-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:35.527854-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	14:50:35.628304-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8915
default	14:50:35.628689-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8915
default	14:50:35.850841-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8916
default	14:50:37.234091-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:50:37.234108-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:37.234513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:37.802931-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:38.063815-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:50:38.064220-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:50:38.064320-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 stopping playing
default	14:50:38.064377-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:50:38.064410-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:38.064475-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:50:38.064543-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:38.064639-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:50:38.064577-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:50:38.064651-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:50:38.064709-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:38.064762-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:38.064781-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	14:50:38.067101-0500	runningboardd	Invalidating assertion 404-8724-33146 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:50:38.067224-0500	runningboardd	Invalidating assertion 404-337-33120 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.powerd>:337]
default	14:50:38.173511-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:50:38.173527-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:50:38.173541-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:50:38.173559-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:50:38.173571-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:50:38.184669-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:50:38.195885-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.296915-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.299612-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.314572-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c712b50, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:38.314589-0500	VoiceOver	AudioConverter -> 0x81c712b50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.314599-0500	VoiceOver	AudioConverter -> 0x81c712b50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:38.316159-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33494 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:50:38.316258-0500	runningboardd	Assertion 404-8724-33494 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:50:38.318522-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33495 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:38.318530-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:50:38.318592-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:50:38.318607-0500	runningboardd	Assertion 404-337-33495 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:50:38.318615-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:50:38.318702-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:50:38.318736-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:50:38.323131-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:50:38.323157-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:50:38.323189-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:50:38.323241-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:50:38.323271-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:50:38.328110-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:50:38.328649-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:50:38.330877-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.343760-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:38.344322-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:38.344393-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:38.359555-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:38.359647-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:50:38.379970-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.380130-0500	VoiceOver	No list of permitted front apps returned
default	14:50:38.382033-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:38.382097-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:50:38.384787-0500	VoiceOver	[0x81c27cc80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:38.384859-0500	VoiceOver	[0x81c27cc80] invalidated after the last release of the connection object
default	14:50:38.392436-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:38.396929-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:38.405288-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870641 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:38.439416-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8935
default	14:50:38.629817-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:50:38.673667-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:50:38.674581-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:50:38.674819-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:50:38.674983-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:50:38.675003-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:50:38.675082-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:38.675137-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:50:38.675164-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'}
default	14:50:38.675304-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:50:38.675225-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	14:50:38.675316-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:50:38.675242-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:50:38.675570-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
fault	14:50:38.675544-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:38.675504-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:50:38.675884-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:38.675601-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:50:38.676042-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:38.676078-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
fault	14:50:38.676048-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:38.676095-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	14:50:38.676105-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	14:50:38.676115-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
error	14:50:38.676162-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:50:38.676224-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:38.676866-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:38.676892-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:38.676943-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:38.677221-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:38.677320-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:38.677392-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:38.677617-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:38.677634-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:50:38.679239-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:50:38.679430-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:50:38.688792-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f2d30, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:38.688843-0500	VoiceOver	AudioConverter -> 0x81c6f2d30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.688936-0500	VoiceOver	AudioConverter -> 0x81c6f2d30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:50:38.694111-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 2713386 ioTS st: 2713386 ht: 39407.147621
default	14:50:38.695065-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:38.695820-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:38.695934-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:38.706526-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f1290, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:50:38.706804-0500	VoiceOver	AudioConverter -> 0x81c6f1290: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:50:38.706897-0500	VoiceOver	AudioConverter -> 0x81c6f1290: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
error	14:50:38.926632-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:40.802973-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:42.413319-0500	VoiceOver	No list of permitted front apps returned
fault	14:50:42.485125-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:42.487674-0500	VoiceOver	No list of permitted front apps returned
default	14:50:42.601768-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:50:42.607985-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:42.614582-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:42.614671-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:42.631043-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870643 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:42.689097-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:50:42.689698-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:42.690037-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:50:42.690082-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:50:42.690288-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:50:42.690321-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:50:42.690385-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:50:42.690593-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:50:42.690666-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:50:42.690710-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:42.690943-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:42.690963-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:50:42.748439-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:43.802885-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:45.506591-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:45.505819-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:45.507376-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:45.602087-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:45.601351-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:45.602345-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:45.655292-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474870643 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:45.862085-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:46.003685-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:46.004864-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:46.004400-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:46.129164-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:46.128362-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:46.129549-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:46.176475-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870645 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:50:46.176856-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:50:46.292752-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:50:46.786328-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:50:47.686564-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:47.686608-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:47.686640-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:47.687211-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:47.687256-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:49.053358-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:49.052666-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:49.055532-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:49.102302-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:49.101603-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:49.102442-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:49.802871-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:50:49.829278-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:49.828557-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:49.829581-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:49.928987-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:50:49.928239-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:50:49.929338-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:50:52.803330-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:50:52.855633-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474870645 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:50:53.067771-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:50:53.454790-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:50:53.464854-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:50:53.464972-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:50:55.212259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.213745-0500	runningboardd	Invalidating assertion 404-8724-33494 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:50:55.212949-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:50:55.212960-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:50:55.214629-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:50:55.216809-0500	runningboardd	Invalidating assertion 404-337-33495 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.powerd>:337]
default	14:50:55.214652-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:50:55.214952-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:50:55.223304-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:50:55.223320-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:50:55.223809-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.223830-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:50:55.223838-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:50:55.225789-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:50:55.225879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:50:55.227180-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.227798-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:50:55.227843-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:50:55.227876-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:50:55.227911-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.227946-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:50:55.232357-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:50:55.232777-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:50:55.233277-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:50:55.234627-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:50:55.234752-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
error	14:50:55.234795-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:50:55.234858-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.234894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:50:55.234898-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.234965-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:50:55.235064-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33515 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:50:55.235152-0500	runningboardd	Assertion 404-8724-33515 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:50:55.239378-0500	runningboardd	Invalidating assertion 404-8724-33515 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:50:55.235793-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:50:55.235831-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:50:55.235977-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:50:55.236051-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.238092-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.245470-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:50:55.245497-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:50:55.245616-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:50:55.250279-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:50:55.250463-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:50:55.250473-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.250504-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:50:55.250539-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:50:55.250627-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:50:55.250655-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:50:55.250855-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.250931-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:50:55.250988-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:50:55.251199-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	14:50:55.251300-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:50:55.251394-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	14:50:55.251490-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:50:55.251569-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	14:50:55.252047-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	14:50:55.252089-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:50:55.252172-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:50:55.252473-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:50:55.252610-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:50:55.252901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:50:55.253068-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:50:55.253576-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:50:55.255242-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b15e670, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:50:55.255336-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:50:55.255465-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:50:55.256025-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:55.256216-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:50:55.256264-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:50:55.256361-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:50:55.272869-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:50:55.272907-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:50:55.272942-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:50:55.272986-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:50:55.273021-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:50:55.273910-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.274286-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.274243-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c712ac0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:50:55.274629-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:55.281064-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x81b49a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	14:50:55.294737-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	14:50:55.294770-0500	audioaccessoryd	Updating local audio category 501 -> 201 app com.apple.VoiceOver
error	14:50:55.294938-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	14:50:55.295186-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:55.295283-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:55.295533-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:55.295639-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:55.295938-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:55.300975-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33520 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:50:55.301037-0500	runningboardd	Assertion 404-337-33520 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:50:55.568396-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:50:55.568407-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:50:55.568768-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:50:55.806963-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:50:58.809081-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:50:58.868195-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:50:58.871503-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:58.871582-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:58.871649-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:50:58.871752-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:50:59.848376-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:50:59.848973-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:50:59.849142-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 stopping playing
default	14:50:59.849235-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:50:59.849309-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:50:59.849425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:50:59.849545-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:59.849644-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:50:59.849773-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:50:59.849802-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:50:59.849822-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:59.849920-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:50:59.849961-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	14:50:59.854156-0500	runningboardd	Invalidating assertion 404-8724-33518 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:50:59.854345-0500	runningboardd	Invalidating assertion 404-337-33520 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.powerd>:337]
default	14:50:59.956672-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:50:59.956687-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:50:59.956701-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:50:59.956753-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:50:59.956804-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:50:59.960715-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:51:01.093348-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:01.093426-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:01.093446-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:01.095741-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:51:01.095772-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:51:01.095779-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:51:01.103404-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:01.103435-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:01.104290-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:01.104321-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:01.104329-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:01.106431-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:01.106472-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:01.107345-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:01.107650-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:01.107829-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:01.108315-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:01.108601-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:51:01.108912-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:01.108987-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:51:01.109066-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:01.109251-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:51:01.109409-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:01.109889-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:01.110088-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:01.113562-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:01.114362-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:01.114598-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:01.127445-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:01.127475-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:01.127589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:01.131104-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:01.131351-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:01.131366-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:01.131547-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:01.133521-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:01.133995-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:01.134007-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:01.134069-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:01.134078-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:01.134087-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:01.134093-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:01.134277-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:01.134404-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:01.134533-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:01.134680-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:01.134871-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:01.135061-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:01.140399-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:01.140446-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:51:01.140595-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.140609-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:01.140618-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.140642-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:01.140654-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:01.141331-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b15e670, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.141383-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:01.142148-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:01.142164-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:01.142195-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:01.144443-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:01.144475-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:51:01.145045-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.145064-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:01.145071-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.145097-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:01.145108-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:01.145947-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b15e670, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.145975-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:01.146457-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:01.146482-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:01.146491-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:01.146514-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:51:01.149339-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b15dbf0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:51:01.149625-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x81b49a800:
default	14:51:01.149693-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	14:51:01.149745-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	14:51:03.509150-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:51:05.261285-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:51:05.262367-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:51:05.262573-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:51:05.306294-0500	VoiceOver	No list of permitted front apps returned
default	14:51:05.400073-0500	VoiceOver	No list of permitted front apps returned
default	14:51:05.408026-0500	VoiceOver	No list of permitted front apps returned
default	14:51:05.478815-0500	VoiceOver	No list of permitted front apps returned
default	14:51:05.482436-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:51:05.483004-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:51:05.483102-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:51:05.500510-0500	VoiceOver	[0x81c27cc80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:51:05.500650-0500	VoiceOver	[0x81c27cc80] invalidated after the last release of the connection object
default	14:51:05.516381-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:51:05.516509-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:51:05.521682-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33538 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:51:05.521770-0500	runningboardd	Assertion 404-8724-33538 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:51:05.522212-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:51:05.522224-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:51:05.522213-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33539 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:05.522255-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:51:05.522311-0500	runningboardd	Assertion 404-337-33539 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:51:05.522392-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:51:05.522429-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:51:05.526664-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:51:05.526926-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:51:05.526963-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:51:05.527008-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:51:05.527038-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:51:05.527893-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:05.528995-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:51:05.529134-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:51:05.529149-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:51:05.529222-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:05.529370-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:51:05.529439-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:51:05.529891-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	14:51:05.529558-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	14:51:05.529587-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:51:05.530317-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:05.530344-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:05.530358-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	14:51:05.530366-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:51:05.529999-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:51:05.530194-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:05.530040-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:05.530544-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:51:05.531420-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:51:05.537996-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:51:05.538738-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:51:05.542989-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474870980 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:51:05.579807-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:51:05.580544-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:51:05.580617-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:51:05.580869-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:51:05.580894-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:51:05.580931-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	14:51:05.581010-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:51:05.581182-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:51:05.581259-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:51:05.581321-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:51:05.581604-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:05.581624-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	14:51:05.710890-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:51:06.762064-0500	VoiceOver	[0x81c27e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:51:06.762404-0500	VoiceOver	[0x81c27e6c0] invalidated after the last release of the connection object
default	14:51:07.802815-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:51:08.452656-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:51:08.455738-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:51:08.455835-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:51:08.465379-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474870980 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:51:08.679754-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:51:10.554872-0500	VoiceOver	aqmeio@0x81a9b6a18 Stop id=85
default	14:51:10.554910-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:51:10.555670-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:51:10.808007-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:51:13.802808-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	14:51:16.194668-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:51:16.195084-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:16.195198-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 stopping playing
default	14:51:16.195255-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:16.195290-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:16.195379-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:16.195661-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:51:16.195779-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:16.195797-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:16.196702-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:16.196501-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:16.196760-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	14:51:16.196703-0500	runningboardd	Invalidating assertion 404-8724-33538 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.VoiceOver(501)>:8724]
default	14:51:16.196779-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	14:51:16.196830-0500	runningboardd	Invalidating assertion 404-337-33539 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.powerd>:337]
default	14:51:16.304478-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:51:16.304512-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:51:16.304539-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:51:16.304721-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:51:16.304816-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:51:16.309544-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:51:38.523528-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:38.523559-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:38.523566-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:38.526128-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:51:38.526156-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:51:38.526164-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:51:38.534101-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:38.534145-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:38.534564-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:38.534723-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:38.534936-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:38.539365-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:38.539623-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:51:38.539935-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:38.540071-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:51:38.540570-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:51:38.542933-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:38.542977-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:38.543016-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:38.543054-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:38.543133-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:38.543169-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:38.543206-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:38.543262-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:38.543308-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:38.546484-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:38.546523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:38.555741-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:38.555763-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:38.555918-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:38.560447-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:38.560662-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:38.560765-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:38.560808-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:38.564202-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:38.564505-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:38.564646-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:38.564760-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:38.564846-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:38.564905-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:38.564960-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:38.564981-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:38.565005-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:51:38.565059-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:38.565259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:38.565335-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:38.565392-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:38.565439-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	14:51:38.565630-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:38.565809-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	14:51:38.565892-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:38.566001-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:38.567760-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b1364c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:41.659924-0500	runningboardd	Invalidating assertion 404-396-33101 (target:[osservice<com.apple.VoiceOver(501)>:8724]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	14:51:41.762439-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:51:41.762449-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:51:41.762456-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:51:41.762499-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:51:41.762522-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:51:41.766047-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:51:43.763916-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.763962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:43.763972-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:43.766220-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:51:43.766259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:51:43.766274-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:51:43.780452-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:43.780486-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:43.781595-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.781634-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:43.781641-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:43.782357-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.782387-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.782398-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.784569-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:51:43.784610-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:51:43.784616-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:51:43.784842-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:43.784852-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:43.784868-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:43.784879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:43.784918-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:43.785002-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:43.785053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:43.785162-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:43.789839-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:43.789874-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:43.802002-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:43.802032-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:43.802125-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.808317-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.808691-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:43.808726-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:43.808851-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.814311-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.814675-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:43.814687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:43.814840-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:43.814850-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:43.814857-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:43.814865-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:43.814980-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:43.815131-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.815193-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:43.815386-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:43.815423-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:43.815562-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:51:43.815723-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:43.815413-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:43.816010-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:43.816246-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:43.816351-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:43.816428-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:43.816453-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:43.816548-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:43.816708-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:43.816808-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:43.816941-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:43.818381-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:43.818725-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:43.820931-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:43.822784-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:43.822885-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:43.822941-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:44.407399-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x81b49a800:
default	14:51:44.409038-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	14:51:44.409106-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	14:51:44.409231-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	14:51:44.409333-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	14:51:44.409415-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	14:51:44.415090-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x81b49a800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	14:51:44.416074-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:51:45.046029-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:51:45.586235-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:51:51.653381-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 8955
default	14:51:58.395854-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:51:58.769207-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:58.769232-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:58.769241-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:58.773814-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:51:58.773840-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:51:58.773848-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:51:58.777637-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:58.777686-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:58.777867-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:58.777921-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:51:58.777961-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:51:58.784188-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:58.784214-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:58.784225-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:51:58.784235-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:51:58.784243-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:58.784249-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:58.784647-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:58.784737-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:58.787471-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:58.787523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:58.787642-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:58.787700-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:51:58.787789-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:51:58.791352-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:58.791755-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:58.794426-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:51:58.794687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:51:58.797933-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:51:58.797952-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:51:58.797969-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:58.797985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:58.797991-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:58.797997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:58.798003-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:51:58.798008-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:51:58.798048-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:51:58.798120-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:51:58.798398-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:51:58.798417-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:51:58.798424-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:51:58.816585-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b1364c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	14:51:58.816646-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:51:58.819715-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:58.819792-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:58.819956-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:51:58.822685-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:51:58.822745-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:51:58.822907-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	14:51:58.822973-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:58.823009-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	14:52:02.053710-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2725)
default	14:52:02.053757-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2725 called from <private>
default	14:52:02.053766-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2725 called from <private>
default	14:52:02.054985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.055011-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:52:02.055018-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:52:02.059066-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:52:02.059120-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:52:02.059309-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.059386-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:52:02.059416-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:52:02.064409-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.064469-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.064510-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.066339-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:52:02.066395-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:52:02.066416-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:52:02.066427-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:52:02.066436-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:52:02.066443-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:52:02.066450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2724 called from <private>
default	14:52:02.066478-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2724 called from <private>
default	14:52:02.071362-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:52:02.071391-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:52:02.071985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.072010-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2725)
default	14:52:02.072022-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2724 called from <private>
default	14:52:02.072031-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2724 called from <private>
default	14:52:02.072031-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2725 called from <private>
default	14:52:02.072041-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2725 called from <private>
default	14:52:02.073642-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.073694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.073709-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.073708-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2724 called from <private>
default	14:52:02.073743-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2724 called from <private>
default	14:52:02.073854-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:52:02.073988-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:52:02.074095-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:52:02.074197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:52:02.075942-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:52:02.076019-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:52:02.089802-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:52:02.089852-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:52:02.090003-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.095838-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.096051-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:52:02.096062-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:52:02.096111-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2724 called from <private>
default	14:52:02.096118-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2724 called from <private>
default	14:52:02.096127-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2724 called from <private>
default	14:52:02.096133-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2724 called from <private>
default	14:52:02.096298-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:52:02.096362-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:52:02.096569-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.096642-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:02.096735-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.096934-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:02.097083-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.098001-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b1364c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.098030-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:02.098360-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.098371-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.098377-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:52:02.098557-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x81a428040) Device ID: 85 (Input:No | Output:Yes): true
default	14:52:02.098633-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x81a428040)
default	14:52:02.098824-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.098890-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:02.098958-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.099003-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:02.099291-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.101532-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b1364c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.101562-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:02.102731-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.102758-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x81a428040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.102766-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	14:52:02.102801-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:52:02.102809-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x81a9b6a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	14:52:02.106452-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2724)
default	14:52:02.106487-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2724 called from <private>
default	14:52:02.106496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2724 called from <private>
default	14:52:02.106602-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2724)
default	14:52:02.791714-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:52:03.350646-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:52:03.377094-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:52:03.377538-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:52:03.377635-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:52:03.390356-0500	VoiceOver	No list of permitted front apps returned
default	14:52:03.420095-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppDrawing" ID:404-396-33595 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:03.420171-0500	runningboardd	Assertion 404-396-33595 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:52:03.420444-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:52:03.420455-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:52:03.420464-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:52:03.420484-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:52:03.420500-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:52:03.423424-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:52:03.492397-0500	VoiceOver	No list of permitted front apps returned
default	14:52:03.496345-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:52:03.496854-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:52:03.496937-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:52:03.512825-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:03.513034-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:52:03.524934-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:03.525082-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:52:03.529452-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.VoiceOver(501)>:8724] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-8724-33596 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:52:03.529558-0500	runningboardd	Assertion 404-8724-33596 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:52:03.529994-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:52:03.530091-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:52:03.530160-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:52:03.530251-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:52:03.530281-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:52:03.533693-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:52:03.537127-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	14:52:03.544234-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871649 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:03.544858-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:8724] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-33597 target:8724 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:52:03.544974-0500	runningboardd	Assertion 404-337-33597 (target:[osservice<com.apple.VoiceOver(501)>:8724]) will be created as active
default	14:52:03.545339-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring jetsam update because this process is not memory-managed
default	14:52:03.545351-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring suspend because this process is not lifecycle managed
default	14:52:03.545361-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring GPU update because this process is not GPU managed
default	14:52:03.545439-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Ignoring memory limit update because this process is not memory-managed
default	14:52:03.545469-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:8724] Skipping AppNap state - not lifecycle managed
default	14:52:03.562001-0500	gamepolicyd	Received state update for 8724 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	14:52:03.598877-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 8958
default	14:52:03.599320-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 8958
default	14:52:03.914822-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	14:52:03.954906-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	14:52:03.955410-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:52:03.956289-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f501a","name":"VoiceOver(8724)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:52:03.956492-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:52:03.956509-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:52:03.956686-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.956625-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:52:03.956788-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 8724, Name = sid:0x1f501a, VoiceOver(8724), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:03.956954-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f501b, Nexy(8916), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f501a, VoiceOver(8724), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:52:03.956911-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:52:03.956984-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:52:03.957103-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:52:03.957324-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	14:52:03.957179-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f501a to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":8724}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f501a, sessionType: 'prim', isRecording: false }, 
]
default	14:52:03.957351-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.957474-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:52:03.957782-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
fault	14:52:03.957238-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:03.957381-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	14:52:03.957586-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	14:52:03.957636-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:03.958117-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:52:03.958144-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:52:03.958161-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	14:52:03.958170-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:52:03.957772-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	14:52:03.958018-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	14:52:03.957881-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:52:03.958240-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:52:03.959165-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:03.959192-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:52:03.966644-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:52:03.966715-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:52:03.975064-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 4593833 ioTS st: 4593833 ht: 39492.428631
error	14:52:04.015779-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:04.810452-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	14:52:04.995065-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:04.998059-0500	VoiceOver	No list of permitted front apps returned
default	14:52:05.099617-0500	VoiceOver	No list of permitted front apps returned
default	14:52:05.099756-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:52:05.100253-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:52:05.100322-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:52:05.773753-0500	VoiceOver	[0x81c27cc80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:05.773920-0500	VoiceOver	[0x81c27cc80] invalidated after the last release of the connection object
default	14:52:05.788758-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:52:05.795866-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:52:05.795926-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:52:05.798404-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474871649 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:05.799123-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871651 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:05.840044-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:52:05.840384-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:52:05.840616-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:05.840728-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:52:05.840892-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:52:05.840918-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:52:05.840950-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:52:05.841150-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:52:05.841206-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:52:05.841233-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:52:05.841445-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:05.841460-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:52:05.855125-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 4635287 ioTS st: 4635287 ht: 39494.308632
error	14:52:05.918657-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:09.377834-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:52:09.482294-0500	VoiceOver	No list of permitted front apps returned
default	14:52:09.505873-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:09.506110-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:52:09.517688-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871653 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:09.518070-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:52:09.562165-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:09.583945-0500	VoiceOver	No list of permitted front apps returned
default	14:52:09.584552-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:52:09.585586-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:52:09.585738-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:52:09.592988-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:09.593133-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:52:09.599767-0500	VoiceOver	[0x81c27cc80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:09.599867-0500	VoiceOver	[0x81c27cc80] invalidated after the last release of the connection object
default	14:52:09.601346-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81b453090, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:52:09.601370-0500	VoiceOver	AudioConverter -> 0x81b453090: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:52:09.601377-0500	VoiceOver	AudioConverter -> 0x81b453090: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:52:09.610397-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:52:09.615653-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:52:09.615691-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:52:09.617996-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871653 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:09.618424-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871654 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:09.653469-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	14:52:09.654314-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	14:52:09.654290-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:09.654510-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:52:09.654537-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:52:09.654591-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:52:09.654779-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
fault	14:52:09.654779-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:09.654858-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:52:09.654898-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:52:09.655158-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:09.655183-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:52:09.665029-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 4719299 ioTS st: 4719299 ht: 39498.118632
error	14:52:09.724396-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:10.147252-0500	VoiceOver	No list of permitted front apps returned
default	14:52:10.188025-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f9080, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:52:10.188060-0500	VoiceOver	AudioConverter -> 0x81c6f9080: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:52:10.188077-0500	VoiceOver	AudioConverter -> 0x81c6f9080: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:52:10.188404-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:10.188611-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:52:10.199659-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	14:52:10.205404-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	14:52:10.205451-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 0
default	14:52:10.213747-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871654 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:10.214476-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871655 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:10.238464-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	14:52:10.238749-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	14:52:10.239031-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	14:52:10.239099-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	14:52:10.239274-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	14:52:10.239298-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	14:52:10.239327-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x81b49a800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	14:52:10.239464-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x81b49a800; ; [8724]; play>; running count now 1
default	14:52:10.239511-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	14:52:10.239540-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	14:52:10.239716-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	14:52:10.239729-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x81a9b6a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	14:52:10.248771-0500	VoiceOver	No list of permitted front apps returned
default	14:52:10.255059-0500	VoiceOver	AQSTL aq(0x81b49a800) start time resolved to: 4732309 ioTS st: 4732309 ht: 39498.708632
error	14:52:10.275196-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:10.810461-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:52:11.866278-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474871655 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:12.001118-0500	VoiceOver	No list of permitted front apps returned
default	14:52:12.010653-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:52:12.105299-0500	VoiceOver	No list of permitted front apps returned
default	14:52:12.106128-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	14:52:12.106833-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 8724, name: VoiceOver
default	14:52:12.106966-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	14:52:12.112869-0500	VoiceOver	[0x81c27cc80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:12.113018-0500	VoiceOver	[0x81c27cc80] invalidated after the last release of the connection object
default	14:52:12.124555-0500	VoiceOver	[0x81c27e580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:12.124743-0500	VoiceOver	[0x81c27e580] invalidated after the last release of the connection object
default	14:52:12.126936-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x81c6f82d0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	14:52:12.126969-0500	VoiceOver	AudioConverter -> 0x81c6f82d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	14:52:12.126985-0500	VoiceOver	AudioConverter -> 0x81c6f82d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	14:52:12.141410-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871656 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:12.141671-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:52:12.243690-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:13.810424-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:52:14.035568-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:52:14.035650-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:52:14.037611-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	14:52:14.037971-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	14:52:14.042506-0500	VoiceOver	[0x81c27e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	14:52:14.042988-0500	VoiceOver	[0x81c27e940] invalidated after the last release of the connection object
default	14:52:16.810395-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:52:17.867053-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474871656 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:17.881309-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871657 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	14:52:17.934544-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:19.356199-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474871657 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:19.367320-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871658 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	14:52:19.426351-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	14:52:19.810403-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	14:52:21.586823-0500	powerd	Process VoiceOver.8724 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474871658 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	14:52:21.794826-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	14:52:22.102225-0500	powerd	Process VoiceOver.8724 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474871659 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	14:52:22.102624-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	14:52:22.216933-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
