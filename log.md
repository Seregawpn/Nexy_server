# Nexy Permission Restart & Menu Bar Icon Fix - Test Results

**Date:** 2025-11-06 14:35:32  
**Test:** Full permission restart flow with icon display  
**Status:** ✅ SUCCESS

## Problem Fixed

**Issue:** Menu bar icon не відображалася після permission restart.

**Root Cause:** `os.execv()` НЕ передає environment variables в новий процес.

**Solution:** Замінено `os.execv()` на `os.execve()` з env variable `NEXY_FIRST_RUN_RESTARTED=1`.

## Test Results

✅ Process running (PID 59151)
✅ Restart via execve successful  
✅ Env variable passed correctly  
✅ Delayed icon setting triggered  
✅ **Icon set successfully on attempt #1**

## Timeline

```
14:34:52 - First run detected
14:35:32 - execve restart with NEXY_FIRST_RUN_RESTARTED=1
14:35:35 - New process recognized restart via env
14:35:38 - Icon set successfully
```

---

default	14:10:19.404406-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1c5019","name":"Nexy(53377)"}, "details":null }
default	14:10:19.404465-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1c5019 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":53377})
default	14:10:19.404500-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":53377})
default	14:10:19.402374-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x195195 (Nexy) connectionID: DCAE3 pid: 53377 in session 0x101
default	14:10:19.402436-0500	WindowServer	<BSCompoundAssertion:0x7c9011500> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x195195 (Nexy) acq:0x7c6fac320 count:1
default	14:10:19.404855-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 53377, Name = sid:0x1c5019, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:19.404963-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 53377, Name = sid:0x1c5019, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:19.405746-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:19.405863-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:19.405436-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:19.405592-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:19.405894-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x195195 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x195195 (Nexy)"
)}
default	14:10:19.407306-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xd081 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x195195 (Nexy)"
)}
default	14:10:19.409964-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:19.410206-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
error	14:10:19.411164-0500	runningboardd	NOTE: unexpected exec event for [anon<Nexy>(501):53377] after 43.951084 seconds - hoping it is a delayed xpcproxy exec notification
default	14:10:19.413134-0500	runningboardd	XPC connection invalidated: [anon<Nexy>(501):53377]
default	14:10:19.413764-0500	kernel	Nexy[53377] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x91c9b188a96df9c5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:10:19.413791-0500	kernel	Nexy[53377] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x91c9b188a96df9c5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:10:19.477246-0500	Nexy	[0x100eb46e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	14:10:19.477319-0500	Nexy	[0x100eb4c20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	14:10:19.604106-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb9adec1c0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:10:19.604341-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb9adec1c0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:10:19.604542-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb9adec1c0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:10:19.604743-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb9adec1c0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:10:19.605802-0500	Nexy	[0x100ea00c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:10:19.606441-0500	Nexy	[0xb9af54000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:10:19.606726-0500	Nexy	[0xb9af54140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:10:19.607183-0500	Nexy	[0xb9af54280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:10:19.607774-0500	Nexy	Received configuration update from daemon (initial)
default	14:10:19.609181-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:10:19.609503-0500	Nexy	[0xb9af543c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:10:19.610661-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.1, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:19.634015-0500	Nexy	[0xb9af543c0] invalidated after the last release of the connection object
default	14:10:19.634269-0500	Nexy	server port 0x0000330b, session port 0x0000330b
default	14:10:19.635297-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.1040, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:10:19.635325-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:10:19.656387-0500	Nexy	New connection 0xcc73b main
default	14:10:19.659028-0500	Nexy	CHECKIN: pid=53377
default	14:10:19.666507-0500	launchservicesd	CHECKIN:0x0-0x195195 53377 com.nexy.assistant
default	14:10:19.666615-0500	Nexy	CHECKEDIN: pid=53377 asn=0x0-0x195195 foreground=0
default	14:10:19.667259-0500	Nexy	[0xb9af543c0] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	14:10:19.667510-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:10:19.667642-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:10:19.667675-0500	Nexy	[0xb9af54500] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:10:19.667684-0500	Nexy	[0xb9af54500] Connection returned listener port: 0x4603
default	14:10:19.667798-0500	Nexy	[0xb9b880300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb9af54500.peer[361].0xb9b880300
default	14:10:19.668608-0500	Nexy	FRONTLOGGING: version 1
default	14:10:19.668615-0500	Nexy	Registered, pid=53377 ASN=0x0,0x195195
default	14:10:19.668744-0500	WindowServer	cc73b[CreateApplication]: Process creation: 0x0-0x195195 (Nexy) connectionID: CC73B pid: 53377 in session 0x101
default	14:10:19.668940-0500	Nexy	[0xb9af54780] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:10:19.669591-0500	Nexy	[0xb9af54500] Connection returned listener port: 0x4603
default	14:10:19.669939-0500	Nexy	BringForward: pid=53377 asn=0x0-0x195195 bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	14:10:19.670444-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:10:19.672343-0500	Nexy	No persisted cache on this platform.
default	14:10:19.673537-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:10:19.674243-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:10:19.676059-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	14:10:19.676069-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	14:10:19.676155-0500	Nexy	Initializing connection
default	14:10:19.676201-0500	Nexy	Removing all cached process handles
default	14:10:19.676220-0500	Nexy	Sending handshake request attempt #1 to server
default	14:10:19.676228-0500	Nexy	Creating connection to com.apple.runningboard
default	14:10:19.676234-0500	Nexy	[0xb9af54640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:10:19.676553-0500	runningboardd	Setting client for [anon<Nexy>(501):53377] as ready
default	14:10:19.676589-0500	Nexy	[0xb9af54500] Connection returned listener port: 0x4603
default	14:10:19.677174-0500	Nexy	Handshake succeeded
default	14:10:19.677191-0500	Nexy	Identity resolved as anon<Nexy>(501)
default	14:10:19.677309-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 53377
default	14:10:19.679594-0500	Nexy	[0xb9af54500] Connection returned listener port: 0x4603
default	14:10:19.682758-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:10:19.682781-0500	Nexy	[0xb9af54a00] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:10:19.682889-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:10:19.682941-0500	Nexy	[0xb9af54b40] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:10:19.684581-0500	Nexy	[0xb9af54b40] Connection returned listener port: 0x6c03
default	14:10:19.685260-0500	Nexy	Registered process with identifier 53377-120210
default	14:10:19.686989-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:19.687067-0500	WindowServer	cc73b[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x195195 (Nexy) mainConnectionID: CC73B;
} for reason: updated frontmost process
default	14:10:19.687169-0500	WindowServer	cc73b[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x195195 (Nexy) -> <pid: 53377>
default	14:10:19.687289-0500	WindowServer	new deferring rules for pid:391: [
    [391-C44]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C43]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C42]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:19.687329-0500	WindowServer	[keyboardFocus 0x7c9406b20] setRules:forPID(391): [
    [391-C44]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C43]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C42]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:19.687556-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:19.687870-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 391>,
    <token: Nexy:0x0-0x195195; pid: 391>,
    <pid: 53377>
]
default	14:10:19.821932-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:10:19.824327-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:10:19.825949-0500	Nexy	[0xb9af54c80] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	14:10:19.827931-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:10:19.829322-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-todesktop-230313mzl4w4u92/AUVoiceIOChatFlavor, translatedBundleID com.todesktop.230313mzl4w4u92, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:10:19.829457-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-todesktop-230313mzl4w4u92/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.todesktop.230313mzl4w4u92, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:10:19.829576-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:10:19.829586-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:10:19.829613-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:10:19.829727-0500	Nexy	[0xb9af54dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:10:19.830542-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.2, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:19.855402-0500	Nexy	[0xb9af54dc0] invalidated after the last release of the connection object
default	14:10:19.855568-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:10:19.855604-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:10:19.857003-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.487, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
error	14:10:19.875617-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=404, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:10:19.876530-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.489, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:10:19.892288-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:10:19.892952-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb9ade1d60> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	14:10:19.906306-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:10:21.353688-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 649E6EAD-364A-45C2-BD0E-AE048EF2628E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52136,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x76fd8aad tp_proto=0x06"
default	14:10:21.353775-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52136<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366042 t_state: SYN_SENT process: Nexy:53377 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x826a3005
default	14:10:21.354492-0500	kernel	tcp connected: [<IPv4-redacted>:52136<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366042 t_state: ESTABLISHED process: Nexy:53377 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x826a3005
default	14:10:21.354760-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52136<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366042 t_state: FIN_WAIT_1 process: Nexy:53377 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x826a3005
default	14:10:21.354770-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52136<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366042 t_state: FIN_WAIT_1 process: Nexy:53377 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:10:21.370790-0500	Nexy	[0xb9af54dc0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:10:21.383202-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb9bf50740) Selecting device 71 from constructor
default	14:10:21.383214-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:21.383224-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:21.383229-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb9bf50740) nothing to teardown
default	14:10:21.383235-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb9bf50740) connecting device 71
default	14:10:21.383332-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb9bf50740) Device ID: 71 (Input:No | Output:Yes): true
default	14:10:21.383985-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb9bf50740) created ioproc 0xa for device 71
default	14:10:21.384074-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 7 device listeners to device 71
default	14:10:21.384222-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 71
default	14:10:21.384231-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb9bf50740)
default	14:10:21.384299-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:21.384306-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:10:21.384313-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:21.384319-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:10:21.384325-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:10:21.384407-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:10:21.384417-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:10:21.384422-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:10:21.384426-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device listeners from device 0
default	14:10:21.384430-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 0
default	14:10:21.384434-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:21.384458-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:10:21.384546-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb9bf50740) caller requesting device change from 71 to 78
default	14:10:21.384555-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:21.384558-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:21.384562-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb9bf50740) disconnecting device 71
default	14:10:21.384566-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb9bf50740) destroying ioproc 0xa for device 71
default	14:10:21.384623-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:10:21.385111-0500	Nexy	[0xb9af55040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:10:21.385994-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":{"PID":53377,"session_type":"Primary"} }
default	14:10:21.386086-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":53377}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c501a, sessionType: 'prim', isRecording: false }, 
]
default	14:10:21.386447-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb9ae012a0 with ID: 0x1c501a
default	14:10:21.387320-0500	Nexy	[0xb9af55180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	14:10:21.387710-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=229252469358593 }
default	14:10:21.387726-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	14:10:21.387778-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:10:21.387850-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb9bf50740) connecting device 78
default	14:10:21.387918-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb9bf50740) Device ID: 78 (Input:Yes | Output:No): true
default	14:10:21.389338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.490, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:10:21.410393-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb9bf50740) created ioproc 0xa for device 78
default	14:10:21.410537-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 7 device listeners to device 78
default	14:10:21.410727-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 78
default	14:10:21.410737-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb9bf50740)
default	14:10:21.410744-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:10:21.410754-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:10:21.410881-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:10:21.410890-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:10:21.410896-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:10:21.410981-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:10:21.410991-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:10:21.410996-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:10:21.411004-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 7 device listeners from device 71
default	14:10:21.411160-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 71
default	14:10:21.411169-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:21.411562-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:10:21.412731-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.491, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:10:21.430999-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:10:21.431977-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.492, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:10:21.449949-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:10:21.451644-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.493, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:10:21.471483-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:21.496763-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	14:10:21.497654-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:10:21.497759-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:10:21.497812-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:21.497867-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c501a, Nexy(53377), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:10:21.497914-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:21.497920-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:21.498003-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:21.498053-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:21.498070-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:10:21.498081-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c501a, Nexy(53377), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 27 starting recording
default	14:10:21.498090-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:21.498147-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:21.498199-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:21.498290-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
fault	14:10:21.498279-0500	runningboardd	Two equal instances have unequal identities. <anon<Nexy>(501) pid=53377 AUID=501> and <anon<Nexy>(501)(0) pid=53377>
default	14:10:21.498589-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:21.498625-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:10:21.498646-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c501a, Nexy(53377), 'prim'', displayID:'com.nexy.assistant'}
default	14:10:21.498722-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:10:21.498733-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:10:21.498718-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:21.498831-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:21.498852-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:21.498866-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:10:21.498873-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:10:21.498883-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:10:21.498913-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	14:10:21.499769-0500	runningboardd	Two equal instances have unequal identities. <anon<Nexy>(501) pid=53377 AUID=501> and <anon<Nexy>(501)(0) pid=53377>
default	14:10:21.810436-0500	spindump	Nexy [53377]: spin: not sampling due to conditions 0x400000000
default	14:10:22.374428-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:10:22.481940-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:10:22.489037-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:10:22.489554-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:10:22.489777-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:22.489888-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:10:22.489960-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c501a, Nexy(53377), 'prim'', displayID:'com.nexy.assistant'}
default	14:10:22.490084-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c501a, Nexy(53377), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 27 stopping recording
default	14:10:22.490088-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:22.490143-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:10:22.490209-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:22.490298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:22.490405-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:22.490348-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:22.490432-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:10:22.490515-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:10:22.490490-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:10:22.490540-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:10:22.490592-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:22.490638-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:10:22.490672-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:22.490716-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:10:22.592322-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb9bf50740) Selecting device 0 from destructor
default	14:10:22.592353-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:22.592367-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:22.592381-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb9bf50740) disconnecting device 78
default	14:10:22.592396-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb9bf50740) destroying ioproc 0xa for device 78
default	14:10:22.592447-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:10:22.592514-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:10:22.592811-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb9bf50740) nothing to setup
default	14:10:22.592835-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device listeners to device 0
default	14:10:22.592849-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 0
default	14:10:22.592863-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 7 device listeners from device 78
default	14:10:22.593364-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 78
default	14:10:22.593391-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:22.859638-0500	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x195195 (Nexy) mainConnectionID: CC73B;
} for reason: deferringPolicyEvaluationSuppression
default	14:10:22.859730-0500	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x195195 (Nexy) -> <pid: 53377>
default	14:10:22.859854-0500	WindowServer	new deferring rules for pid:391: [
    [391-C47]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C46]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C45]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:22.859899-0500	WindowServer	[keyboardFocus 0x7c9406b20] setRules:forPID(391): [
    [391-C47]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C46]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C45]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:22.860578-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 391>,
    <token: Nexy:0x0-0x195195; pid: 391>,
    <pid: 53377>
]
default	14:10:23.942373-0500	Nexy	[0xb9af55540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:10:23.943125-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:10:23.943336-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.3, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:23.964765-0500	Nexy	[0xb9af55540] invalidated after the last release of the connection object
default	14:10:23.965182-0500	Nexy	[0xb9af55540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:10:23.965719-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.4, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:23.985641-0500	Nexy	[0xb9af55540] invalidated after the last release of the connection object
default	14:10:23.995065-0500	Nexy	server port 0x0000d327, session port 0x0000330b
default	14:10:23.997833-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 20DC01F9-2BF4-42AC-99CE-57AA9338E4C5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52138,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x7efc0f8c tp_proto=0x06"
default	14:10:23.997911-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52138<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366055 t_state: SYN_SENT process: Nexy:53377 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa716f5f3
default	14:10:23.998502-0500	kernel	tcp connected: [<IPv4-redacted>:52138<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366055 t_state: ESTABLISHED process: Nexy:53377 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa716f5f3
default	14:10:24.005975-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52138<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366055 t_state: FIN_WAIT_1 process: Nexy:53377 Duration: 0.008 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa716f5f3
default	14:10:24.005990-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52138<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366055 t_state: FIN_WAIT_1 process: Nexy:53377 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:10:24.006207-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 25DAF6D0-872F-49E7-A3B5-3EB53AC74F0D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52139,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf071e0a9 tp_proto=0x06"
default	14:10:24.006225-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52139<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366056 t_state: SYN_SENT process: Nexy:53377 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa6420410
default	14:10:24.006261-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:10:24.006392-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:10:24.006639-0500	kernel	tcp connected: [<IPv4-redacted>:52139<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366056 t_state: ESTABLISHED process: Nexy:53377 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa6420410
default	14:10:24.006824-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52139<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366056 t_state: FIN_WAIT_1 process: Nexy:53377 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa6420410
default	14:10:24.006835-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52139<-><IPv4-redacted>:53] interface: utun6 (skipped: 0)
so_gencnt: 366056 t_state: FIN_WAIT_1 process: Nexy:53377 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:10:24.007266-0500	Nexy	nw_path_libinfo_path_check [75C2AE97-C711-4072-942A-E84965722B49 IPv4#601b9664:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:10:24.007694-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B611B974-F5B2-49D3-898B-1BECC7238AB1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52140,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xa386ec01 tp_proto=0x06"
default	14:10:24.007719-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52140<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366057 t_state: SYN_SENT process: Nexy:53377 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86d975be
default	14:10:24.007970-0500	kernel	tcp connected: [<IPv4-redacted>:52140<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366057 t_state: ESTABLISHED process: Nexy:53377 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86d975be
default	14:10:24.139211-0500	Nexy	[0xb9af55540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:10:24.140063-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.5, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:24.161243-0500	Nexy	[0xb9af55540] invalidated after the last release of the connection object
default	14:10:24.174487-0500	Nexy	[0xb9af55540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:10:24.175220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.6, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:24.199543-0500	Nexy	[0xb9af55540] invalidated after the last release of the connection object
default	14:10:24.545902-0500	kernel	udp connect: [<IPv4-redacted>:60198<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 366061 so_state: 0x0002 process: Nexy:53377 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb91ae7be
default	14:10:24.545917-0500	kernel	udp_connection_summary [<IPv4-redacted>:60198<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 366061 so_state: 0x0002 process: Nexy:53377 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb91ae7be flowctl: 0us (0x)
default	14:10:24.547785-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 02EF049A-6210-47C5-8384-E8CE5CF49E9E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52142,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x57eb39cf tp_proto=0x06"
default	14:10:24.547842-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52142<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366063 t_state: SYN_SENT process: Nexy:53377 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa3707e64
default	14:10:24.548398-0500	kernel	tcp connected: [<IPv4-redacted>:52142<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366063 t_state: ESTABLISHED process: Nexy:53377 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa3707e64
default	14:10:24.598825-0500	Nexy	[0xb9af557c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:10:24.599697-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.7, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:24.624674-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53377.8, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:10:24.645626-0500	Nexy	[0xb9af557c0] invalidated after the last release of the connection object
default	14:10:24.645703-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:10:24.646101-0500	Nexy	[0xb9af557c0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	14:10:24.646215-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	14:10:24.646682-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	14:10:24.649205-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=41237.5, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=41237, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:10:24.649233-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=41237, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:10:24.682626-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.1046, attribution={responsible={TCCDProcess: identifier=com.todesktop.230313mzl4w4u92, pid=6362, auid=501, euid=501, responsible_path=/Applications/Cursor.app/Contents/MacOS/Cursor, binary_path=/Applications/Cursor.app/Contents/MacOS/Cursor}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:10:24.682652-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:10:24.704588-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:10:25.177846-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb9bf50740) Selecting device 71 from constructor
default	14:10:25.177870-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:25.177890-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:25.177897-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb9bf50740) nothing to teardown
default	14:10:25.177902-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb9bf50740) connecting device 71
default	14:10:25.178050-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb9bf50740) Device ID: 71 (Input:No | Output:Yes): true
default	14:10:25.178209-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb9bf50740) created ioproc 0xb for device 71
default	14:10:25.178344-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 7 device listeners to device 71
default	14:10:25.178599-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 71
default	14:10:25.178611-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb9bf50740)
default	14:10:25.178710-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:25.178725-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:10:25.178735-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:25.178745-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:10:25.178756-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:10:25.178873-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:10:25.178885-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:10:25.178894-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:10:25.178900-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device listeners from device 0
default	14:10:25.178905-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 0
default	14:10:25.178911-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:25.178927-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb9bf50740) caller requesting device change from 71 to 71
default	14:10:25.178934-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:25.178939-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb9bf50740) exiting with nothing to do
default	14:10:25.179363-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:10:25.179689-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:10:25.183022-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb9bf50740) Selecting device 0 from destructor
default	14:10:25.183038-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:25.183047-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:25.183053-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb9bf50740) disconnecting device 71
default	14:10:25.183060-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb9bf50740) destroying ioproc 0xb for device 71
default	14:10:25.183099-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xb}
default	14:10:25.183142-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:10:25.183309-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb9bf50740) nothing to setup
default	14:10:25.183325-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device listeners to device 0
default	14:10:25.183331-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 0
default	14:10:25.183340-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 7 device listeners from device 71
default	14:10:25.183597-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 71
default	14:10:25.183617-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:25.185221-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb9bf50740) Selecting device 71 from constructor
default	14:10:25.185235-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:25.185242-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb9bf50740) not already running
default	14:10:25.185247-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb9bf50740) nothing to teardown
default	14:10:25.185252-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb9bf50740) connecting device 71
default	14:10:25.185496-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb9bf50740) Device ID: 71 (Input:No | Output:Yes): true
default	14:10:25.185636-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb9bf50740) created ioproc 0xc for device 71
default	14:10:25.185774-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 7 device listeners to device 71
default	14:10:25.186021-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb9bf50740) adding 0 device delegate listeners to device 71
default	14:10:25.186033-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb9bf50740)
default	14:10:25.186140-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:25.186151-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:10:25.186158-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:10:25.186170-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:10:25.186180-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:10:25.186304-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:10:25.186320-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb9bf50740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:10:25.186326-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:10:25.186332-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device listeners from device 0
default	14:10:25.186337-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb9bf50740) removing 0 device delegate listeners from device 0
default	14:10:25.186342-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb9bf50740)
default	14:10:25.186361-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb9bf50740) caller requesting device change from 71 to 71
default	14:10:25.186366-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb9bf50740)
default	14:10:25.186371-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb9bf50740) exiting with nothing to do
default	14:10:25.186379-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:10:25.186887-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:10:25.187213-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:10:25.190957-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:25.216882-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	14:10:25.217945-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:10:25.218061-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:10:25.218097-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1c501a, Nexy(53377), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:10:25.218139-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:25.218185-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c501a, Nexy(53377), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:10:25.218213-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.218256-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:10:25.218295-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 27 starting playing
default	14:10:25.218425-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.218522-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.218446-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:25.218544-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:10:25.218612-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c501a, Nexy(53377), 'prim'', displayID:'com.nexy.assistant'}
default	14:10:25.218697-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:10:25.218928-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	14:10:25.218951-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:10:25.218822-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c501a to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":53377}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c501a, sessionType: 'prim', isRecording: false }, 
]
default	14:10:25.218825-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:10:25.219151-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	14:10:25.219444-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.219475-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.219489-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:10:25.219362-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:10:25.219497-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:10:25.219516-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	14:10:25.219554-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:10:25.374402-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	14:10:26.148662-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:26.148850-0500	WindowServer	cc73b[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x195195 (Nexy) mainConnectionID: CC73B;
} for reason: updated frontmost process
default	14:10:26.148978-0500	WindowServer	cc73b[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x195195 (Nexy) -> <pid: 53377>
default	14:10:26.149137-0500	WindowServer	new deferring rules for pid:391: [
    [391-C50]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C4F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C4E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:26.149188-0500	WindowServer	[keyboardFocus 0x7c9406b20] setRules:forPID(391): [
    [391-C50]; <keyboardFocus; Nexy:0x0-0x195195>; () -> <pid: 53377>; reason: frontmost PSN --> outbound target,
    [391-C4F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x195195; pid: 391>; reason: frontmost PSN,
    [391-C4E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	14:10:26.149806-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:26.150125-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 391>,
    <token: Nexy:0x0-0x195195; pid: 391>,
    <pid: 53377>
]
default	14:10:26.154503-0500	Nexy	[0xb9af55a40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	14:10:26.175652-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 53377
default	14:10:26.182766-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	14:10:26.189146-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xb9adf0780
 (
    "<NSAquaAppearance: 0xb9adf08c0>",
    "<NSSystemAppearance: 0xb9adf0820>"
)>
default	14:10:26.192286-0500	Nexy	[0xb9af55f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	14:10:26.192559-0500	Nexy	[0xb9af56080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	14:10:26.196902-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	14:10:26.197263-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	14:10:26.197274-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	14:10:26.197289-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	14:10:26.197323-0500	Nexy	[0xb9af56300] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	14:10:26.197330-0500	Nexy	[0xb9af561c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:10:26.197395-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:26.198126-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:26.198344-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	14:10:26.198523-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec43c0 <private>> attempting immediate handshake from activate
default	14:10:26.198568-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec43c0 <private>> sent handshake
default	14:10:26.198663-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	14:10:26.199103-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	14:10:26.199398-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec43c0 <private>> was invalidated
default	14:10:26.199417-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:26.200527-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	14:10:26.201474-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	14:10:26.202003-0500	Nexy	Requesting scene <FBSScene: 0xb98ec46e0; com.apple.controlcenter:59B60A7B-A999-4A55-A8D4-FD557F6E9BFB> from com.apple.controlcenter.statusitems
error	14:10:26.202264-0500	Nexy	Error creating <FBSScene: 0xb98ec46e0; com.apple.controlcenter:59B60A7B-A999-4A55-A8D4-FD557F6E9BFB>: <NSError: 0xb9a46d380; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:10:26.202334-0500	Nexy	Request for <FBSScene: 0xb98ec46e0; com.apple.controlcenter:59B60A7B-A999-4A55-A8D4-FD557F6E9BFB> complete!
default	14:10:26.209444-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	14:10:26.221841-0500	Nexy	Registering for test daemon availability notify post.
default	14:10:26.221982-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:10:26.222089-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:10:26.222204-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:10:26.223917-0500	Nexy	[0xb9af566c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	14:10:26.224769-0500	Nexy	[0xb9af54500] Connection returned listener port: 0x4603
default	14:10:26.225126-0500	Nexy	SignalReady: pid=53377 asn=0x0-0x195195
default	14:10:26.225579-0500	Nexy	SIGNAL: pid=53377 asn=0x0x-0x195195
default	14:10:26.226603-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
error	14:10:26.237754-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	14:10:26.245861-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:10:26.245907-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	14:10:26.246006-0500	Nexy	[0xb9af55680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	14:10:26.246156-0500	Nexy	[0xb9af55680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:10:26.247647-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
error	14:10:26.252326-0500	kernel	Sandbox: WindowManager(580) deny(1) mach-task-name others [Nexy(53377)]
default	14:10:26.252105-0500	Nexy	[C:2] Alloc <private>
default	14:10:26.252172-0500	Nexy	[0xb9af55540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:10:26.264926-0500	Nexy	[0xb9af56800] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:10:26.264940-0500	Nexy	[0xb9af56800] Connection returned listener port: 0x1fd07
default	14:10:26.265733-0500	Nexy	[0xb9af55680] invalidated after the last release of the connection object
default	14:10:26.266989-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:26.267033-0500	runningboardd	Acquiring assertion targeting 53377 from originator [anon<Nexy>(501):53377] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-53377-28431 target:53377 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:10:26.267478-0500	runningboardd	ignoring [anon<Nexy>(501):53377] as candidate for concrete target as it is terminating
default	14:10:26.267535-0500	runningboardd	Acquiring assertion targeting 53377 from originator [anon<Nexy>(501):53377] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-53377-28432 target:53377 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:10:26.254194-0500	WindowManager	Connection activated | (53377) Nexy
error	14:10:26.267282-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 53377 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 53377 does not exist}>
error	14:10:26.267293-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 53377 with code: 2 - RBSAssertionErrorDomain
error	14:10:26.267728-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 53377 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 53377 does not exist}>
error	14:10:26.267736-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 53377 with code: 2 - RBSAssertionErrorDomain
default	14:10:26.362519-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	14:10:26.366777-0500	Nexy	Start service name com.apple.spotlightknowledged
default	14:10:26.367686-0500	Nexy	[GMS] availability notification token 75
default	14:10:26.516668-0500	Nexy	[0xb9af55680] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	14:10:26.519728-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	14:10:26.520222-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	14:10:26.523389-0500	Nexy	[0xb9af56a80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:10:26.524570-0500	Nexy	[0xb9af56bc0] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:10:26.525155-0500	Nexy	[0xb9af56d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:10:26.525329-0500	Nexy	[0xb9af56f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:10:26.549232-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:10:26.549187-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1c501a, Nexy(53377), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1c501b, DictationIM(52910), 'prim'', displayID:'com.apple.inputmethod.ironwood'} but will use session={clientName:'(null)', displayID:'(null)'}
default	14:10:26.549283-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:10:26.549346-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:10:26.549401-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:10:26.562258-0500	DictationIM	setting current input controller = com.nexy.assistant
default	14:10:26.563098-0500	Nexy	[0xb9af56e40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:10:26.563925-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=53377, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:10:26.564049-0500	Nexy	[0xb9af56e40] invalidated after the last release of the connection object
default	14:10:26.569792-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	14:10:27.239433-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:27.239495-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:27.239629-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:27.239675-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:27.240189-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:7772683D-1C7E-4BD9-BD98-F9FAAE3CE6A0> from com.apple.controlcenter.statusitems
default	14:10:27.240355-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:27.240428-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:27.240499-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:7772683D-1C7E-4BD9-BD98-F9FAAE3CE6A0> complete!
error	14:10:27.240582-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:7772683D-1C7E-4BD9-BD98-F9FAAE3CE6A0>: <NSError: 0xb9ac07d50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:27.240638-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7772683D-1C7E-4BD9-BD98-F9FAAE3CE6A0
error	14:10:27.240690-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	14:10:28.241291-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:28.241323-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:28.241410-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> attempting immediate handshake from activate
default	14:10:28.241439-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> sent handshake
default	14:10:28.241765-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7> from com.apple.controlcenter.statusitems
default	14:10:28.242185-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> was invalidated
default	14:10:28.242221-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:28.242238-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7> complete!
error	14:10:28.242290-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7>: <NSError: 0xb9ac075a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:28.242314-0500	Nexy	No scene exists for identity: com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7
default	14:10:28.242393-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	14:10:28.244133-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:28.244151-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:28.244210-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:28.244230-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
default	14:10:28.244316-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	14:10:28.244718-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	14:10:28.244802-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:28.244815-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:28.245089-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	14:10:28.245135-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	14:10:28.245542-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5680; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:10:28.245711-0500	Nexy	Error creating <FBSScene: 0xb98ec5680; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7-Aux[1]-NSStatusItemView>: <NSError: 0xb9ac07480; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:10:28.245759-0500	Nexy	Request for <FBSScene: 0xb98ec5680; com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7-Aux[1]-NSStatusItemView> complete!
error	14:10:28.246121-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:28.246140-0500	Nexy	[com.apple.controlcenter:857FBB4A-3BBB-472B-B571-5A7DBB596BE7] No matching scene to invalidate for this identity.
error	14:10:28.246165-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:28.246216-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:28.246329-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:28.375936-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 3
default	14:10:28.430324-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	14:10:28.487629-0500	DictationIM	setting current input controller = com.nexy.assistant
default	14:10:29.156562-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:10:29.156629-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:10:29.247623-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:29.247658-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:29.247745-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> attempting immediate handshake from activate
default	14:10:29.247776-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> sent handshake
default	14:10:29.248086-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A> from com.apple.controlcenter.statusitems
default	14:10:29.248373-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A> complete!
default	14:10:29.248456-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> was invalidated
default	14:10:29.248480-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:29.248542-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A>: <NSError: 0xb9ac074e0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:29.248562-0500	Nexy	No scene exists for identity: com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A
default	14:10:29.248699-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:29.248717-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:29.248758-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> attempting immediate handshake from activate
default	14:10:29.248775-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> sent handshake
default	14:10:29.248888-0500	Nexy	Requesting scene <FBSScene: 0xb98ec48c0; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:29.249136-0500	Nexy	Request for <FBSScene: 0xb98ec48c0; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView> complete!
default	14:10:29.249155-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec45a0 <private>> was invalidated
default	14:10:29.249176-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:29.249218-0500	Nexy	Error creating <FBSScene: 0xb98ec48c0; com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView>: <NSError: 0xb9ac07690; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:29.249233-0500	Nexy	No scene exists for identity: com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView
default	14:10:29.250061-0500	Nexy	[com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:29.250355-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:29.250382-0500	Nexy	[com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A] No matching scene to invalidate for this identity.
error	14:10:29.250407-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:29.250418-0500	Nexy	[com.apple.controlcenter:98CF2D00-DD14-4E79-8958-AEB30444076A-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:29.250965-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:29.251046-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:29.251112-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:29.251147-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:30.251969-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:30.252008-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:30.252094-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:30.252130-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:30.252432-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8> from com.apple.controlcenter.statusitems
default	14:10:30.252676-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8> complete!
default	14:10:30.253031-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:30.253060-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:30.253158-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8>: <NSError: 0xb9ac07d50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:30.253180-0500	Nexy	No scene exists for identity: com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8
default	14:10:30.253209-0500	Nexy	Requesting scene <FBSScene: 0xb98ec45a0; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:10:30.253314-0500	Nexy	Error creating <FBSScene: 0xb98ec45a0; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8-Aux[3]-NSStatusItemView>: <NSError: 0xb9ac07570; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:10:30.253350-0500	Nexy	Request for <FBSScene: 0xb98ec45a0; com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8-Aux[3]-NSStatusItemView> complete!
error	14:10:30.253523-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:30.253540-0500	Nexy	[com.apple.controlcenter:05760261-C4D7-43D8-B5BD-E7D2A29776D8] No matching scene to invalidate for this identity.
error	14:10:30.253561-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:30.253597-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:30.253657-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:30.594428-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	14:10:30.595031-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:10:30.595170-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 27 stopping playing
default	14:10:30.595233-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:10:30.595274-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:30.595343-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:30.595421-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:30.595482-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c501a to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":53377}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c501a, sessionType: 'prim', isRecording: false }, 
]
default	14:10:30.595582-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:10:30.595597-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:10:30.595592-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:30.595654-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:30.595678-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:10:31.255037-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:31.255072-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:31.255167-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> attempting immediate handshake from activate
default	14:10:31.255199-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> sent handshake
default	14:10:31.255513-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F> from com.apple.controlcenter.statusitems
default	14:10:31.255795-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F> complete!
default	14:10:31.255913-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> was invalidated
default	14:10:31.255939-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:31.256001-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F>: <NSError: 0xb9ac06f10; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:31.256017-0500	Nexy	No scene exists for identity: com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F
default	14:10:31.256113-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:31.256130-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:31.256181-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:31.256201-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:31.256314-0500	Nexy	Requesting scene <FBSScene: 0xb98ec48c0; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:31.256480-0500	Nexy	Request for <FBSScene: 0xb98ec48c0; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView> complete!
default	14:10:31.256587-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:31.256607-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:31.256654-0500	Nexy	Error creating <FBSScene: 0xb98ec48c0; com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView>: <NSError: 0xb9ac07660; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:31.256674-0500	Nexy	No scene exists for identity: com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView
default	14:10:31.256962-0500	Nexy	[com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:31.257153-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:31.257173-0500	Nexy	[com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F] No matching scene to invalidate for this identity.
error	14:10:31.257194-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:31.257206-0500	Nexy	[com.apple.controlcenter:79EA459E-97ED-4383-B89A-FABB083B825F-Aux[4]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:31.257530-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:31.257601-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:31.257651-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:31.257694-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:32.258687-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:32.258723-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:32.258804-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:32.258831-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:32.259135-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7> from com.apple.controlcenter.statusitems
default	14:10:32.259385-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7> complete!
default	14:10:32.259502-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:32.259529-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:32.259603-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7>: <NSError: 0xb9ac07d50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:32.259618-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7
default	14:10:32.259690-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:32.259706-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:32.259746-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:32.259763-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:32.259886-0500	Nexy	Requesting scene <FBSScene: 0xb98ec55e0; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:32.260036-0500	Nexy	Request for <FBSScene: 0xb98ec55e0; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView> complete!
default	14:10:32.260171-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:32.260191-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:32.260245-0500	Nexy	Error creating <FBSScene: 0xb98ec55e0; com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView>: <NSError: 0xb9ac077b0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:32.260260-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView
default	14:10:32.260531-0500	Nexy	[com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:32.260730-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:32.260745-0500	Nexy	[com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7] No matching scene to invalidate for this identity.
error	14:10:32.260768-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:32.260781-0500	Nexy	[com.apple.controlcenter:D4175060-71A3-4217-A790-AEB476BE72C7-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:32.261156-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:32.261226-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:32.261274-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:32.261301-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:33.262254-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:33.262290-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:33.262373-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:33.262401-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
default	14:10:33.262686-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53> from com.apple.controlcenter.statusitems
default	14:10:33.262919-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53> complete!
default	14:10:33.263086-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:33.263109-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:33.263176-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53>: <NSError: 0xb9ac07120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:33.263194-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53
default	14:10:33.263225-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:33.263237-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:33.263274-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:33.263293-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:33.263407-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5860; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:33.263550-0500	Nexy	Request for <FBSScene: 0xb98ec5860; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView> complete!
default	14:10:33.263669-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:33.263689-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:33.263729-0500	Nexy	Error creating <FBSScene: 0xb98ec5860; com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView>: <NSError: 0xb9ac07480; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:33.263741-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView
default	14:10:33.263994-0500	Nexy	[com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:33.264177-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:33.264204-0500	Nexy	[com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53] No matching scene to invalidate for this identity.
error	14:10:33.264226-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:33.264239-0500	Nexy	[com.apple.controlcenter:9BCA4127-3670-427F-A58F-7C8487AEFF53-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:33.264607-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:33.264683-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:33.264730-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:33.264755-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:34.265701-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:34.265738-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:34.265827-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:34.265858-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:34.266170-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3> from com.apple.controlcenter.statusitems
default	14:10:34.266448-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3> complete!
default	14:10:34.266940-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:34.266973-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:34.267082-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3>: <NSError: 0xb9ac078d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:34.267103-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3
default	14:10:34.267143-0500	Nexy	Requesting scene <FBSScene: 0xb98ec48c0; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:10:34.267277-0500	Nexy	Error creating <FBSScene: 0xb98ec48c0; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3-Aux[7]-NSStatusItemView>: <NSError: 0xb9ac07cc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:10:34.267323-0500	Nexy	Request for <FBSScene: 0xb98ec48c0; com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3-Aux[7]-NSStatusItemView> complete!
error	14:10:34.267489-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:34.267508-0500	Nexy	[com.apple.controlcenter:0DEC07A4-168D-422A-89EA-E981F27D4BE3] No matching scene to invalidate for this identity.
error	14:10:34.267534-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:34.267565-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:34.267635-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:35.269084-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:35.269140-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:35.269268-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:35.269319-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:35.269809-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154> from com.apple.controlcenter.statusitems
default	14:10:35.270220-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154> complete!
default	14:10:35.270580-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:35.270632-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:35.270760-0500	Nexy	LSExceptions shared instance invalidated for timeout.
error	14:10:35.270764-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154>: <NSError: 0xb9ac072a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:35.270819-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154
default	14:10:35.270889-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:35.270908-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:35.270967-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:35.270994-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
default	14:10:35.271177-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5860; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:35.271390-0500	Nexy	Request for <FBSScene: 0xb98ec5860; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView> complete!
default	14:10:35.271543-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:35.271567-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:35.271621-0500	Nexy	Error creating <FBSScene: 0xb98ec5860; com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView>: <NSError: 0xb9ac07a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:35.271640-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView
default	14:10:35.271882-0500	Nexy	[com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:35.272125-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:35.272149-0500	Nexy	[com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154] No matching scene to invalidate for this identity.
error	14:10:35.272181-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:35.272197-0500	Nexy	[com.apple.controlcenter:1B3F33B3-F0D1-4615-A08D-79C3200C8154-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:35.272521-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:35.272605-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:35.272658-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:35.272692-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:36.273643-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:36.273684-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:36.273813-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:36.273864-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:36.274307-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924> from com.apple.controlcenter.statusitems
default	14:10:36.274672-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924> complete!
default	14:10:36.275012-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:36.275054-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:36.275140-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:36.275171-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:36.275249-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:36.275289-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
error	14:10:36.275403-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924>: <NSError: 0xb9ac07cf0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:36.275440-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924
default	14:10:36.275559-0500	Nexy	Requesting scene <FBSScene: 0xb98ec48c0; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:36.275841-0500	Nexy	Request for <FBSScene: 0xb98ec48c0; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView> complete!
default	14:10:36.276055-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:36.276087-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:36.276148-0500	Nexy	Error creating <FBSScene: 0xb98ec48c0; com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView>: <NSError: 0xb9ac07570; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:36.276173-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView
default	14:10:36.276328-0500	Nexy	[com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:36.276582-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:36.276602-0500	Nexy	[com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924] No matching scene to invalidate for this identity.
error	14:10:36.276638-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:36.276655-0500	Nexy	[com.apple.controlcenter:C104E367-C041-4873-BC1F-39072636C924-Aux[9]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:36.277009-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:36.277081-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:36.277134-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:36.277170-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:37.278072-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:37.278110-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:37.278211-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:37.278247-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:37.278570-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A> from com.apple.controlcenter.statusitems
default	14:10:37.278847-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A> complete!
default	14:10:37.279300-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:37.279345-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:37.279418-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:37.279443-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:37.279512-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:37.279540-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
error	14:10:37.279633-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A>: <NSError: 0xb9ac07750; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:37.279664-0500	Nexy	No scene exists for identity: com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A
default	14:10:37.279752-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5860; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:37.280003-0500	Nexy	Request for <FBSScene: 0xb98ec5860; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView> complete!
default	14:10:37.280239-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:37.280272-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:37.280349-0500	Nexy	Error creating <FBSScene: 0xb98ec5860; com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView>: <NSError: 0xb9ac07a80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:37.280370-0500	Nexy	No scene exists for identity: com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView
default	14:10:37.280564-0500	Nexy	[com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:37.280869-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:37.280889-0500	Nexy	[com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A] No matching scene to invalidate for this identity.
error	14:10:37.280921-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:37.280941-0500	Nexy	[com.apple.controlcenter:22E71443-FE25-4AE7-8D98-17B605E3EF8A-Aux[10]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:37.281327-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:37.281409-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:37.281467-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:37.281506-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:38.282499-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:38.282557-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:38.282694-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:38.282742-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:38.283221-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69> from com.apple.controlcenter.statusitems
default	14:10:38.283654-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69> complete!
default	14:10:38.284138-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:38.284198-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:38.284343-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69>: <NSError: 0xb9ac07090; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:38.284382-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69
default	14:10:38.284436-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:38.284457-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:38.284518-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> attempting immediate handshake from activate
default	14:10:38.284543-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> sent handshake
default	14:10:38.284754-0500	Nexy	Requesting scene <FBSScene: 0xb98ec57c0; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:38.284993-0500	Nexy	Request for <FBSScene: 0xb98ec57c0; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView> complete!
default	14:10:38.285243-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec48c0 <private>> was invalidated
default	14:10:38.285278-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:38.285343-0500	Nexy	Error creating <FBSScene: 0xb98ec57c0; com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView>: <NSError: 0xb9ac07780; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:38.285363-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView
default	14:10:38.285545-0500	Nexy	[com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:38.285815-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:38.285836-0500	Nexy	[com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69] No matching scene to invalidate for this identity.
error	14:10:38.285872-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:38.285892-0500	Nexy	[com.apple.controlcenter:0C99A277-0F7C-474A-A122-7CAB57767A69-Aux[11]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:38.286334-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:38.286421-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:38.286474-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:38.286510-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:39.287429-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:39.287482-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:39.287601-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec57c0 <private>> attempting immediate handshake from activate
default	14:10:39.287647-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec57c0 <private>> sent handshake
default	14:10:39.288077-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5> from com.apple.controlcenter.statusitems
default	14:10:39.288450-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5> complete!
default	14:10:39.288822-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec57c0 <private>> was invalidated
default	14:10:39.288870-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:39.288945-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:39.288975-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:39.289057-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> attempting immediate handshake from activate
default	14:10:39.289093-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> sent handshake
error	14:10:39.289187-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5>: <NSError: 0xb9ac07510; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:39.289216-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5
default	14:10:39.289311-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5860; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:39.289575-0500	Nexy	Request for <FBSScene: 0xb98ec5860; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView> complete!
default	14:10:39.289808-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> was invalidated
default	14:10:39.289840-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:39.289907-0500	Nexy	Error creating <FBSScene: 0xb98ec5860; com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView>: <NSError: 0xb9ac074b0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:39.289927-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView
default	14:10:39.290160-0500	Nexy	[com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:39.290437-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:39.290458-0500	Nexy	[com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5] No matching scene to invalidate for this identity.
error	14:10:39.290494-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:39.290514-0500	Nexy	[com.apple.controlcenter:7DB18820-1FC7-4514-85AB-06C6E76EB0B5-Aux[12]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:39.291002-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:39.291112-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:39.291187-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:39.291237-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:40.292030-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:40.292083-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:40.292192-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:40.292233-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:40.292620-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94> from com.apple.controlcenter.statusitems
default	14:10:40.292960-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94> complete!
default	14:10:40.293126-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:40.293165-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:40.293271-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94>: <NSError: 0xb9ac070c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:40.293297-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94
default	14:10:40.293402-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:40.293432-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:40.293519-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> attempting immediate handshake from activate
default	14:10:40.293549-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> sent handshake
default	14:10:40.293737-0500	Nexy	Requesting scene <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:40.293973-0500	Nexy	Request for <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView> complete!
default	14:10:40.294183-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> was invalidated
default	14:10:40.294217-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:40.294280-0500	Nexy	Error creating <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView>: <NSError: 0xb9ac07780; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:40.294312-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView
default	14:10:40.294573-0500	Nexy	[com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:40.294835-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:40.294855-0500	Nexy	[com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94] No matching scene to invalidate for this identity.
error	14:10:40.294889-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:40.294908-0500	Nexy	[com.apple.controlcenter:7A987968-DBE5-4946-B208-655CC0184E94-Aux[13]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:40.295342-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:40.295418-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:40.295481-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:40.295519-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:41.296499-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:41.296554-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:41.296689-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> attempting immediate handshake from activate
default	14:10:41.296736-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> sent handshake
default	14:10:41.297199-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85> from com.apple.controlcenter.statusitems
default	14:10:41.297611-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85> complete!
default	14:10:41.298015-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> was invalidated
default	14:10:41.298051-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:41.298120-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:41.298141-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:41.298198-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> attempting immediate handshake from activate
default	14:10:41.298223-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> sent handshake
error	14:10:41.298297-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85>: <NSError: 0xb9ac07120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:41.298321-0500	Nexy	No scene exists for identity: com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85
default	14:10:41.298402-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5860; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:41.298609-0500	Nexy	Request for <FBSScene: 0xb98ec5860; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView> complete!
default	14:10:41.298733-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5680 <private>> was invalidated
default	14:10:41.298759-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:41.298825-0500	Nexy	Error creating <FBSScene: 0xb98ec5860; com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView>: <NSError: 0xb9ac07300; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:41.298842-0500	Nexy	No scene exists for identity: com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView
default	14:10:41.299129-0500	Nexy	[com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:41.299376-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:41.299395-0500	Nexy	[com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85] No matching scene to invalidate for this identity.
error	14:10:41.299431-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:41.299462-0500	Nexy	[com.apple.controlcenter:4E3E65E7-2B19-4480-9D6B-7F64F4D2BC85-Aux[14]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:41.299880-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:41.299948-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:41.300002-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:41.300039-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:42.299834-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:42.299858-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:42.299916-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:42.299938-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:42.300128-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3> from com.apple.controlcenter.statusitems
default	14:10:42.300301-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3> complete!
default	14:10:42.300569-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:42.300616-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:42.300700-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:42.300734-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:42.300820-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:42.300857-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
error	14:10:42.300961-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3>: <NSError: 0xb9ac075a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:42.300997-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3
default	14:10:42.301116-0500	Nexy	Requesting scene <FBSScene: 0xb98ec52c0; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:42.301414-0500	Nexy	Request for <FBSScene: 0xb98ec52c0; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView> complete!
default	14:10:42.301626-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:42.301666-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:42.301748-0500	Nexy	Error creating <FBSScene: 0xb98ec52c0; com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView>: <NSError: 0xb9ac07cc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:42.301776-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView
default	14:10:42.301985-0500	Nexy	[com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:42.302161-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:42.302179-0500	Nexy	[com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3] No matching scene to invalidate for this identity.
error	14:10:42.302203-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:42.302218-0500	Nexy	[com.apple.controlcenter:B3323501-A188-4ECD-973C-A267B7B437E3-Aux[15]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:42.302442-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:42.302498-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:42.302536-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:42.302563-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:43.303047-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:43.303087-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:43.303184-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> attempting immediate handshake from activate
default	14:10:43.303220-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> sent handshake
default	14:10:43.303561-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781> from com.apple.controlcenter.statusitems
default	14:10:43.303854-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781> complete!
default	14:10:43.304122-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec52c0 <private>> was invalidated
default	14:10:43.304156-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:43.304239-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781>: <NSError: 0xb9ac07750; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:43.304263-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781
default	14:10:43.304302-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:43.304322-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:43.304379-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:43.304404-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
default	14:10:43.304567-0500	Nexy	Requesting scene <FBSScene: 0xb98ec55e0; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:43.304764-0500	Nexy	Request for <FBSScene: 0xb98ec55e0; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView> complete!
default	14:10:43.304904-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:43.304933-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:43.304992-0500	Nexy	Error creating <FBSScene: 0xb98ec55e0; com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView>: <NSError: 0xb9ac06fa0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:43.305013-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView
default	14:10:43.305269-0500	Nexy	[com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:43.305531-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:43.305552-0500	Nexy	[com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781] No matching scene to invalidate for this identity.
error	14:10:43.305584-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:43.305600-0500	Nexy	[com.apple.controlcenter:1262D529-92C6-4B07-9EFE-86636532A781-Aux[16]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:43.305985-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:43.306072-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:43.306128-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:43.306165-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:44.307101-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:44.307157-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:44.307291-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> attempting immediate handshake from activate
default	14:10:44.307339-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> sent handshake
default	14:10:44.307790-0500	Nexy	Requesting scene <FBSScene: 0xb98ec5720; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF> from com.apple.controlcenter.statusitems
default	14:10:44.308202-0500	Nexy	Request for <FBSScene: 0xb98ec5720; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF> complete!
default	14:10:44.308607-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec55e0 <private>> was invalidated
default	14:10:44.308661-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:10:44.308768-0500	Nexy	FBSWorkspace registering source: <private>
default	14:10:44.308803-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:10:44.308893-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> attempting immediate handshake from activate
default	14:10:44.308933-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> sent handshake
error	14:10:44.309046-0500	Nexy	Error creating <FBSScene: 0xb98ec5720; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF>: <NSError: 0xb9ac07540; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:44.309082-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF
default	14:10:44.309199-0500	Nexy	Requesting scene <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:10:44.309520-0500	Nexy	Request for <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView> complete!
default	14:10:44.309781-0500	Nexy	<FBSWorkspaceScenesClient:0xb98ec5860 <private>> was invalidated
default	14:10:44.309825-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:10:44.309901-0500	Nexy	Error creating <FBSScene: 0xb98ec52c0; com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView>: <NSError: 0xb9ac075a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:10:44.309920-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView
default	14:10:44.310152-0500	Nexy	[com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:10:44.310398-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:44.310416-0500	Nexy	[com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF] No matching scene to invalidate for this identity.
error	14:10:44.310450-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:10:44.310467-0500	Nexy	[com.apple.controlcenter:7ADF0614-2090-4C28-A908-52A742E67ECF-Aux[17]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:10:44.310867-0500	Nexy	Unhandled disconnected scene <private>
error	14:10:44.310950-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:10:44.311009-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:10:44.311047-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:10:44.501044-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x195195 (Nexy) connectionID: CC73B pid: 53377 in session 0x101
default	14:10:44.501070-0500	WindowServer	<BSCompoundAssertion:0x7c9011500> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x195195 (Nexy) acq:0x7c627aa00 count:1
default	14:10:44.502530-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1c501a","name":"Nexy(53377)"}, "details":null }
default	14:10:44.502563-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1c501a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":53377})
default	14:10:44.502574-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":53377})
default	14:10:44.502765-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:10:44.502819-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 53377, Name = sid:0x1c501a, Nexy(53377), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:10:44.503134-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.503190-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.503210-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.503052-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x195195 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x195195 (Nexy)"
)}
default	14:10:44.502938-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.503053-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.504308-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xd081 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x195195 (Nexy)"
)}
default	14:10:44.503458-0500	WindowManager	Connection invalidated | (53377) Nexy
default	14:10:44.505980-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:10:44.508779-0500	runningboardd	XPC connection invalidated: [anon<Nexy>(501):53377]
default	14:10:44.520792-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52142<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366063 t_state: FIN_WAIT_1 process: Nexy:53377 Duration: 19.973 sec Conn_Time: 0.001 sec bytes in/out: 510194/897 pkts in/out: 60/6 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 44 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.187 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa3707e64
default	14:10:44.520817-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52142<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366063 t_state: FIN_WAIT_1 process: Nexy:53377 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:10:44.520979-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52140<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366057 t_state: FIN_WAIT_1 process: Nexy:53377 Duration: 20.513 sec Conn_Time: 0.000 sec bytes in/out: 4769/1875 pkts in/out: 4/5 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.250 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x86d975be
default	14:10:44.520994-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52140<-><IPv4-redacted>:443] interface: utun6 (skipped: 0)
so_gencnt: 366057 t_state: FIN_WAIT_1 process: Nexy:53377 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:10:44.521255-0500	runningboardd	[anon<Nexy>(501):53377] termination reported by proc_exit
default	14:10:44.526766-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x195195} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:10:44.526812-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 1659285
default	14:10:44.526882-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:10:44.528002-0500	runningboardd	Invalidating assertion 397-361-28135 (target:[anon<Nexy>(501):53377]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	14:10:44.624130-0500	runningboardd	Removing process: [anon<Nexy>(501):53377]
default	14:10:44.624337-0500	runningboardd	removeJobWithInstance called for identity without existing job [anon<Nexy>(501):53377]
default	14:10:44.624351-0500	runningboardd	Removing assertions for terminated process: [anon<Nexy>(501):53377]
default	14:10:44.628628-0500	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 53377, name = Nexy
default	14:10:44.628835-0500	gamepolicyd	Received state update for 53377 (anon<Nexy>(501), none-NotVisible
error	14:10:44.634061-0500	runningboardd	RBSStateCapture remove item called for untracked item 397-361-28135 (target:[anon<Nexy>(501):53377])
