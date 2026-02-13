default	20:21:06.941087-0500	VoiceOver	No list of permitted front apps returned
default	20:21:06.941266-0500	VoiceOver	No list of permitted front apps returned
default	20:21:06.971580-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:06.971702-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:06.974128-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf23ff180, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:06.974670-0500	VoiceOver	AudioConverter -> 0xbf23ff180: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:06.974684-0500	VoiceOver	AudioConverter -> 0xbf23ff180: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:06.980930-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:06.985264-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:06.985507-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:06.987306-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf23ff000, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:06.987322-0500	VoiceOver	AudioConverter -> 0xbf23ff000: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:06.987330-0500	VoiceOver	AudioConverter -> 0xbf23ff000: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:06.998805-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875775 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:06.999176-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875776 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:07.038582-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:07.039391-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:07.039611-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:07.039634-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:07.039669-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:07.039808-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:07.039865-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
fault	20:21:07.040231-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:07.039894-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	20:21:07.040503-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:07.040529-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:07.040545-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:07.059020-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6411703 ioTS st: 6411703 ht: 138086.662458
error	20:21:07.074090-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:07.319688-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:07.320874-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:07.323133-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:08.500497-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875776 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:08.506486-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875777 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:21:08.556746-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:09.061531-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:09.062340-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:09.062465-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:09.145215-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:09.150484-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:09.150582-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:09.153830-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875777 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.154325-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875778 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.176189-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:09.177059-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:21:09.177160-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:09.177349-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:09.177376-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:09.177413-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:09.177577-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
fault	20:21:09.177556-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:09.177644-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:09.177681-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:09.177927-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:09.177947-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:09.185643-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:09.186240-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:09.186333-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:09.192290-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6458744 ioTS st: 6458744 ht: 138088.795792
error	20:21:09.210226-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:09.237956-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:09.246036-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:09.246062-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:09.248270-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875778 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.248845-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875779 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.285182-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:09.285464-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:09.285718-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:09.285834-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:09.286010-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:09.286032-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:09.286060-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:09.286184-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:09.286236-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:09.286267-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:09.286473-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:09.286487-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:21:09.297410-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:09.298939-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6461096 ioTS st: 6461096 ht: 138088.902458
default	20:21:09.393220-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:09.393723-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:09.393806-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:09.406411-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:09.417217-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:09.417309-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:09.418697-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875779 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.419604-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875780 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.436925-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:09.437253-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:09.437500-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:09.437555-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:09.437992-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:09.438015-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:09.438045-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:09.438174-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:09.438237-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:09.438262-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:09.438462-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:09.438474-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:09.459086-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6464625 ioTS st: 6464625 ht: 138089.062458
error	20:21:09.461370-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:09.704067-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:09.704850-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:09.704991-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:09.727478-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:09.737036-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:09.737128-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:09.738471-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875780 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.739789-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875781 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.757085-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:09.757633-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:09.758035-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:09.758502-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:09.758819-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:09.758857-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:09.758920-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:09.759159-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:09.759248-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:09.759294-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:09.759574-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:09.759596-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:09.779139-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6471682 ioTS st: 6471682 ht: 138089.382458
error	20:21:09.783334-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:09.892729-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:09.893394-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:09.893513-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:09.962043-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:09.971301-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:09.971337-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:09.972460-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875781 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:09.973251-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875782 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:10.000278-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:10.000585-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:10.000859-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:21:10.000849-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:10.001041-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:10.001065-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:10.001094-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:10.001219-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:10.001272-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:10.001302-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:10.001490-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:10.001506-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:10.013663-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6476857 ioTS st: 6476857 ht: 138089.617125
error	20:21:10.018456-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:10.729912-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875782 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:10.937985-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:21:11.259752-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875783 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:11.267659-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:21:11.506586-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:13.295332-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:13.295610-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:21:17.298116-0500	VoiceOver	No list of permitted front apps returned
default	20:21:17.346971-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:17.352726-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:17.352771-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:17.374742-0500	VoiceOver	No list of permitted front apps returned
default	20:21:17.380295-0500	VoiceOver	No list of permitted front apps returned
default	20:21:17.411438-0500	VoiceOver	No list of permitted front apps returned
default	20:21:17.450330-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf23fed30, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:17.450359-0500	VoiceOver	AudioConverter -> 0xbf23fed30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:17.450373-0500	VoiceOver	AudioConverter -> 0xbf23fed30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:17.450572-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:21:17.471271-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875788 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:17.471725-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:21:17.538762-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:17.539828-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:17.540152-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:17.540236-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:17.540354-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
error	20:21:17.755784-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:18.245421-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:18.245712-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:18.468322-0500	VoiceOver	No list of permitted front apps returned
default	20:21:18.468734-0500	VoiceOver	No list of permitted front apps returned
default	20:21:18.483342-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:18.483525-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:18.509485-0500	VoiceOver	No list of permitted front apps returned
default	20:21:18.511049-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:21:18.516612-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:18.526120-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:18.526165-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:18.532414-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875788 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:18.532907-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875793 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:18.568037-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:18.568624-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:18.568809-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:18.568835-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:18.568867-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:18.569046-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:18.569108-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:18.569140-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:18.569359-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:18.569374-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	20:21:18.570521-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:18.570851-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:18.666219-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:18.675606-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:18.686389-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:18.686446-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:18.694441-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875801 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:18.724102-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:21:18.724245-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:18.724328-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:18.724361-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:18.724412-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:18.724602-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:18.724684-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:18.724723-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:18.724961-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:18.724977-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:18.739124-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6669252 ioTS st: 6669252 ht: 138098.342458
error	20:21:18.753572-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:19.468875-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98220
default	20:21:19.469300-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98220
default	20:21:19.839113-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875801 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:20.436208-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:20.447074-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:20.447213-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:20.510144-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:21:22.536556-0500	VoiceOver	aqmeio@0xbf0a97618 Stop id=85
default	20:21:22.536560-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:22.537090-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:31.589662-0500	VoiceOver	No list of permitted front apps returned
default	20:21:31.694704-0500	VoiceOver	No list of permitted front apps returned
default	20:21:31.695008-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:31.696600-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:31.696810-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:31.941731-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28754d0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:31.941788-0500	VoiceOver	AudioConverter -> 0xbf28754d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:31.941804-0500	VoiceOver	AudioConverter -> 0xbf28754d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:31.942184-0500	VoiceOver	[0xbf066a6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:31.942420-0500	VoiceOver	[0xbf066a6c0] invalidated after the last release of the connection object
default	20:21:31.954926-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28753e0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:31.954957-0500	VoiceOver	AudioConverter -> 0xbf28753e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:31.954972-0500	VoiceOver	AudioConverter -> 0xbf28753e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:31.962083-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:21:31.971573-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:21:31.981730-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875809 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:31.982765-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:21:32.055588-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:32.056339-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:32.056556-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:32.056591-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:32.056677-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:21:32.056775-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:32.056965-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:32.057038-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
fault	20:21:32.057071-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:32.057133-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:32.057385-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:32.057404-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:32.072319-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 6963252 ioTS st: 6963252 ht: 138111.675792
error	20:21:32.166301-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:32.581331-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:32.581607-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
fault	20:21:32.615900-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:32.624205-0500	VoiceOver	No list of permitted front apps returned
default	20:21:32.731554-0500	VoiceOver	No list of permitted front apps returned
default	20:21:32.742714-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:32.743309-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:32.743405-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:32.759931-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:32.760081-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:32.782655-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:32.787734-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:32.787802-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:32.799432-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875812 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:32.839344-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:32.839662-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:32.839984-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:32.840060-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:32.840287-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:32.840310-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:32.840339-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:32.840606-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:32.840670-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:32.840702-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:32.840920-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:32.840934-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:21:32.916202-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:21:35.425308-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:35.418859-0500	VoiceOver	No list of permitted front apps returned
default	20:21:35.524024-0500	VoiceOver	No list of permitted front apps returned
default	20:21:35.524230-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:35.524920-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:35.525011-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:36.041017-0500	VoiceOver	[0xbf066a6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:36.041330-0500	VoiceOver	[0xbf066a6c0] invalidated after the last release of the connection object
default	20:21:36.106292-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:36.106514-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:21:36.109250-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2875230, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:36.109281-0500	VoiceOver	AudioConverter -> 0xbf2875230: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:36.109297-0500	VoiceOver	AudioConverter -> 0xbf2875230: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:36.120564-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28757d0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:36.120608-0500	VoiceOver	AudioConverter -> 0xbf28757d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:36.120625-0500	VoiceOver	AudioConverter -> 0xbf28757d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:36.135850-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:36.137027-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:36.137068-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:36.139874-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474875812 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:36.141436-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875814 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:36.174910-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:36.175204-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:36.175497-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:36.175566-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:36.175734-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:36.175757-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:36.175791-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:36.175913-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:36.175968-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:36.175997-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:36.176177-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:36.176192-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:36.189690-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7054040 ioTS st: 7054040 ht: 138115.793125
error	20:21:36.254838-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:36.926810-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:36.927023-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
fault	20:21:37.504992-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:37.510675-0500	VoiceOver	No list of permitted front apps returned
default	20:21:37.611723-0500	VoiceOver	No list of permitted front apps returned
default	20:21:37.669593-0500	VoiceOver	No list of permitted front apps returned
default	20:21:37.686378-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf292f7e0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:37.686399-0500	VoiceOver	AudioConverter -> 0xbf292f7e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:37.686418-0500	VoiceOver	AudioConverter -> 0xbf292f7e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:37.691576-0500	VoiceOver	No list of permitted front apps returned
default	20:21:37.692806-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:37.693170-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:37.693227-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:37.714975-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:37.715085-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:21:37.752465-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:37.752552-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:21:37.763940-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:21:37.767103-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:21:37.771001-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	20:21:37.779700-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:37.779725-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:37.784260-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875814 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:37.784650-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875831 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:37.816476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:37.816752-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:37.817034-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:37.817147-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:37.817307-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:37.817331-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:37.817362-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:37.817492-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:37.817542-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	20:21:37.817572-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:37.817743-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:37.817755-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:37.832356-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7090261 ioTS st: 7090261 ht: 138117.435792
error	20:21:37.952009-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:21:38.999394-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:39.001331-0500	VoiceOver	No list of permitted front apps returned
default	20:21:39.038827-0500	VoiceOver	No list of permitted front apps returned
default	20:21:39.044352-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:39.045600-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:39.045327-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:39.103209-0500	VoiceOver	No list of permitted front apps returned
fault	20:21:39.258065-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:39.257061-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:39.259774-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:39.265583-0500	runningboardd	Invalidating assertion 400-98203-143790 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:39.264022-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:21:39.264059-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:21:39.264101-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:21:39.264904-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:21:39.264945-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:39.280617-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:21:39.280649-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:21:39.280658-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:21:39.283463-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:39.283492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:39.297223-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:21:39.297241-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:21:39.297380-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:39.301105-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:39.301292-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:21:39.301302-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:21:39.327743-0500	runningboardd	Assertion 400-98203-143892 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:39.339067-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf10aa4f0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:21:39.350018-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:39.350552-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:39.350646-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:39.351488-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:39.351535-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:39.360930-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:39.865367-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:39.865581-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
fault	20:21:39.892033-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:39.892532-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:39.893610-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:39.894270-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:39.915699-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:39.915931-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:39.922816-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874cc0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:39.922857-0500	VoiceOver	AudioConverter -> 0xbf2874cc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:39.922869-0500	VoiceOver	AudioConverter -> 0xbf2874cc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:39.932766-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:39.933032-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:21:39.938056-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:39.938235-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:21:39.950026-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:39.955389-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:39.955502-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:39.968672-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474875831 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:39.969558-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876012 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:40.022937-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:40.023204-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:40.023538-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:40.023617-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:40.023782-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:40.023807-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:40.023838-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:40.023964-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:40.024019-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:40.024043-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:40.024245-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:40.024264-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:21:40.113528-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:40.688457-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98228
default	20:21:40.688672-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98227
default	20:21:41.959894-0500	runningboardd	Resolved pid 98211 to [xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:98211:98211]
default	20:21:41.961369-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:98211:98211] is not RunningBoard jetsam managed.
default	20:21:41.961452-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:98211:98211] This process will not be managed.
default	20:21:41.971888-0500	runningboardd	Resolved pid 98210 to [xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:98210:98210]
default	20:21:41.972873-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:98210:98210] is not RunningBoard jetsam managed.
default	20:21:41.972949-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:98210:98210] This process will not be managed.
default	20:21:41.978316-0500	runningboardd	Resolved pid 98208 to [xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:98208:98208]
default	20:21:41.981448-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:98208:98208] is not RunningBoard jetsam managed.
default	20:21:41.981481-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:98208:98208] This process will not be managed.
default	20:21:42.025814-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:21:42.025871-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.025886-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:21:42.025892-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:21:42.028505-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
fault	20:21:42.028702-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:42.033807-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:21:42.034837-0500	runningboardd	Invalidating assertion 400-98203-143893 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:42.033884-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:42.044536-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:21:42.044562-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:21:42.044568-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:21:42.048049-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:42.048060-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:42.062191-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:21:42.062217-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:21:42.062325-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.068751-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.069348-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:21:42.069363-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:21:42.069561-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.076519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.076745-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:42.076769-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:42.076844-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:42.076855-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:42.076863-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:42.076869-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:42.076878-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:42.076899-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:42.076932-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:42.076987-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:42.077158-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:42.077284-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:42.077372-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104e25b10) Device ID: 85 (Input:No | Output:Yes): true
default	20:21:42.077404-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104e25b10)
default	20:21:42.077518-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.077581-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:21:42.077617-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:21:42.079163-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.079616-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:21:42.079775-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:21:42.079921-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:42.080070-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:42.083026-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.083081-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:21:42.083091-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.083142-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:21:42.083154-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:42.084095-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28754d0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.084153-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:21:42.084291-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:21:42.084780-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.085405-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.085412-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:21:42.085835-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.086643-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:42.086967-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.087245-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
error	20:21:42.088913-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:21:42.092473-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-143900 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:21:42.089241-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7655 called from <private>
default	20:21:42.092612-0500	runningboardd	Assertion 400-98203-143900 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:42.089411-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:21:42.089550-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:42.089765-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:21:42.089934-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:42.091398-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:42.092844-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:42.092912-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:42.092983-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:42.094573-0500	runningboardd	Invalidating assertion 400-98203-143900 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:42.095328-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-143901 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:21:42.095495-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104e25b10) Device ID: 85 (Input:No | Output:Yes): true
default	20:21:42.095478-0500	runningboardd	Assertion 400-98203-143901 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:42.095520-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104e25b10)
default	20:21:42.096031-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.096045-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:21:42.096054-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.096076-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:21:42.096086-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:42.297362-0500	VoiceOver	[0xbf066a940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:42.297677-0500	VoiceOver	[0xbf066a940] invalidated after the last release of the connection object
default	20:21:42.629184-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:21:42.672477-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:21:42.672512-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7655 called from <private>
fault	20:21:42.673635-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:42.675611-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:42.675630-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:21:42.678232-0500	runningboardd	Invalidating assertion 400-98203-143901 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:42.678453-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-143903 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:21:42.678548-0500	runningboardd	Assertion 400-98203-143903 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:42.676969-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876b20, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:21:42.678939-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:42.677006-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:21:43.243782-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:21:43.288265-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:21:43.288314-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7655 called from <private>
default	20:21:43.288451-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:21:43.289182-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:43.289199-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:21:43.290290-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:43.290538-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:43.290558-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:43.290612-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:43.291673-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:21:43.292150-0500	runningboardd	Invalidating assertion 400-98203-143903 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:43.291769-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:21:43.292412-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:21:43.292387-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-143905 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:21:43.292490-0500	runningboardd	Assertion 400-98203-143905 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:43.292797-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28754a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:21:43.293483-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:43.341782-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:21:43.342695-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:43.342987-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:43.343389-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:43.343735-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:43.344168-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:43.344475-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:43.344523-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:43.344846-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xbefc3c000:
default	20:21:43.344924-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	20:21:43.344932-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	20:21:43.344949-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	20:21:43.344980-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	20:21:43.345000-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	20:21:43.345315-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:43.345367-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:43.345690-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xbefc3c000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	20:21:43.346081-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:43.346430-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:43.346709-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:43.346973-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:43.347245-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:43.347295-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:43.347362-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:43.347584-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:43.347673-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:43.347733-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:43.348048-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:43.348082-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:45.314619-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876012 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:45.530257-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:21:45.913177-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:45.922708-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:45.922832-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:48.022245-0500	VoiceOver	aqmeio@0xbf0a97618 Stop id=85
default	20:21:48.022656-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:48.023308-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:52.148612-0500	VoiceOver	No list of permitted front apps returned
default	20:21:52.241488-0500	VoiceOver	No list of permitted front apps returned
default	20:21:52.243141-0500	VoiceOver	No list of permitted front apps returned
default	20:21:52.243263-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874e10, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:52.243285-0500	VoiceOver	AudioConverter -> 0xbf2874e10: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:52.243295-0500	VoiceOver	AudioConverter -> 0xbf2874e10: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:52.244016-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:52.244462-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:52.244523-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:52.249463-0500	VoiceOver	No list of permitted front apps returned
default	20:21:52.258934-0500	VoiceOver	[0xbf066a080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:52.259057-0500	VoiceOver	[0xbf066a080] invalidated after the last release of the connection object
default	20:21:52.270411-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876189 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:52.282723-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:21:52.291903-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:52.292615-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:21:52.292980-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:52.293075-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:52.293128-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:52.293222-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:21:52.293344-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:52.293445-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:52.293510-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:52.293576-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:52.293821-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:52.293838-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:52.312100-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7409525 ioTS st: 7409525 ht: 138131.914864
default	20:21:53.390393-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:53.392497-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:53.392560-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:53.396635-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876189 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:53.397583-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876191 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:53.432080-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:53.432393-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:53.432674-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:53.432790-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:53.433017-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:53.433039-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:53.433074-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:53.433221-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:53.433280-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:53.433311-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:53.433523-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:53.433540-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:53.452092-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7434662 ioTS st: 7434662 ht: 138133.054864
error	20:21:53.483787-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:54.619487-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
fault	20:21:54.620378-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:54.624100-0500	runningboardd	Invalidating assertion 400-98203-143905 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:54.622724-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:21:54.622936-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:54.627140-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:21:54.627185-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:21:54.627338-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:21:54.640126-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:54.642484-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:54.642503-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:54.643661-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:54.643683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:21:54.643691-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:21:54.644867-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:21:54.644893-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:21:54.644901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:21:54.645596-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:54.645621-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:21:54.645632-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:21:54.645638-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:21:54.645668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:54.645694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:54.645698-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:54.645739-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:21:54.645761-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:21:54.647424-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:21:54.647463-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:21:54.999106-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:54.999409-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
fault	20:21:55.255844-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:55.256313-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:55.257277-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:55.257775-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:55.768806-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876191 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
fault	20:21:56.191745-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:56.194813-0500	VoiceOver	No list of permitted front apps returned
default	20:21:56.296426-0500	VoiceOver	No list of permitted front apps returned
default	20:21:56.367785-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:56.387620-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:56.387706-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:56.446124-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:56.465713-0500	VoiceOver	[0xbf066a6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:56.465852-0500	VoiceOver	[0xbf066a6c0] invalidated after the last release of the connection object
default	20:21:56.469189-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf292c810, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:21:56.469223-0500	VoiceOver	AudioConverter -> 0xbf292c810: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:21:56.469233-0500	VoiceOver	AudioConverter -> 0xbf292c810: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:21:56.510061-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:56.513120-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:56.513559-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:56.513591-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:56.547452-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7503132 ioTS st: 7503132 ht: 138136.160059
error	20:21:56.603538-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:56.725776-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:56.726706-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:21:56.751924-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:56.758894-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:56.759664-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:56.759772-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:56.767740-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:56.767807-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:56.772020-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876374 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:56.802289-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:21:56.802478-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:21:56.818659-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:56.819050-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:56.819396-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:56.819432-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:56.829307-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:56.847580-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:56.847630-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:56.848450-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876374 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:56.849241-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876375 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:21:56.881448-0500	VoiceOver	     AudioQueueObject.cpp:5805  buffersCreatedAndDestroyed: aq@0xbefc3c000: error allocating buffer
error	20:21:56.881623-0500	VoiceOver	     AudioQueueObject.cpp:5818  buffersCreatedAndDestroyed: aq@0xbefc3c000: invalid buffer ID
default	20:21:56.887317-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:56.887852-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:56.888237-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:56.888242-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:56.888848-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:56.888878-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:56.888916-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:56.889097-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:56.889179-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:56.889218-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:56.889518-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:56.889539-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:56.927598-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7511511 ioTS st: 7511511 ht: 138136.540059
error	20:21:57.093334-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:21:57.244062-0500	VoiceOver	No list of permitted front apps returned
default	20:21:57.246190-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:21:57.246207-0500	VoiceOver	No list of permitted front apps returned
default	20:21:57.246969-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:21:57.247070-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:21:57.256236-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:57.267728-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:57.267788-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:57.283154-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876375 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:57.283957-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876376 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:21:57.332693-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:57.333344-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:57.333548-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:57.333574-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:57.333611-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:57.333767-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:57.333838-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:57.333869-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:57.334109-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:57.334126-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:21:57.380789-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:21:57.397161-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:57.396152-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:57.396203-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:57.397713-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:21:57.397732-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:21:57.397742-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:21:57.472938-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98237
default	20:21:57.456218-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:21:57.482058-0500	VoiceOver	No list of permitted front apps returned
default	20:21:57.578172-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:21:58.070782-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:21:58.113840-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:21:58.113877-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7655 called from <private>
default	20:21:58.114140-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:21:58.114492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:21:58.114541-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:21:58.115983-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:58.116375-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:58.116470-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:58.117585-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:58.117795-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104e25b10) Device ID: 85 (Input:No | Output:Yes): true
default	20:21:58.117836-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104e25b10)
default	20:21:58.118227-0500	runningboardd	Invalidating assertion 400-98203-143953 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:21:58.118535-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-143962 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:21:58.118611-0500	runningboardd	Assertion 400-98203-143962 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:21:58.118244-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:58.118282-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:21:58.118318-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:58.118360-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:21:58.120388-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:58.118401-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:58.167053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:21:58.168042-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876f40, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:21:58.168064-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:21:58.168148-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:21:58.168477-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:58.168591-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:58.168606-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:58.168613-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:58.168632-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:21:58.168642-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:21:58.169042-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:21:58.169478-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876c70, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:21:58.170039-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:58.170663-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:21:58.171663-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:58.171941-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:58.171998-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:58.172449-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xbefc3c000:
default	20:21:58.172688-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	20:21:58.172720-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	20:21:58.172800-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	20:21:58.172200-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:21:58.172879-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
fault	20:21:58.172188-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:58.172955-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
fault	20:21:58.172843-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:58.174168-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:58.174206-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:58.174818-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xbefc3c000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	20:21:58.175205-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:21:58.175435-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:21:58.175718-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:21:58.176086-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:21:58.176362-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:21:58.176397-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:21:58.176439-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:21:58.176625-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:21:58.176732-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:21:58.176791-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:58.177129-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:21:58.177155-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:21:59.478279-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:21:59.487705-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:21:59.487783-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:21:59.669635-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98245
default	20:21:59.677719-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98245
default	20:21:59.852416-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98246
default	20:22:00.134107-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: c0000000c pid: 98244
default	20:22:00.135121-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1600000012 pid: 98244
default	20:22:01.182755-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.182987-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:01.194698-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874360, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:01.194734-0500	VoiceOver	AudioConverter -> 0xbf2874360: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:01.194746-0500	VoiceOver	AudioConverter -> 0xbf2874360: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:01.203552-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.203840-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:22:01.207705-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:01.227920-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.228250-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:22:01.239115-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876556 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:01.240109-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:22:01.244256-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.244662-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:01.265887-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.266611-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:01.285516-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:01.285434-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:01.286760-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:01.286775-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:01.287216-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:01.287283-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	20:22:01.288224-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:01.287535-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:22:01.289009-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:01.287925-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:01.288065-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:01.288151-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:01.288825-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:01.288888-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:01.307399-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7607869 ioTS st: 7607869 ht: 138140.910033
error	20:22:01.581237-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:02.348457-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98253
default	20:22:02.355458-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98253
default	20:22:03.150433-0500	VoiceOver	[0xbf066b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:03.150636-0500	VoiceOver	[0xbf066b200] invalidated after the last release of the connection object
default	20:22:03.232450-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:03.232662-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:03.232897-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:22:03.234854-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:03.238187-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:03.238277-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:03.268487-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf10aa790, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:03.268526-0500	VoiceOver	AudioConverter -> 0xbf10aa790: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:03.268608-0500	VoiceOver	AudioConverter -> 0xbf10aa790: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:03.317359-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:03.337464-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7652631 ioTS st: 7652631 ht: 138142.940033
error	20:22:03.381289-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:04.317298-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:04.327866-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:04.327974-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:04.330796-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876560 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:04.471223-0500	VoiceOver	No list of permitted front apps returned
default	20:22:04.471498-0500	VoiceOver	No list of permitted front apps returned
default	20:22:04.475440-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:04.475626-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:04.488629-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:04.488826-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:04.501553-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:04.501775-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:04.505918-0500	VoiceOver	[0xbf066b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:04.506105-0500	VoiceOver	[0xbf066b200] invalidated after the last release of the connection object
default	20:22:04.509735-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876562 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:04.516901-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf23fdef0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:04.516927-0500	VoiceOver	AudioConverter -> 0xbf23fdef0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:04.516966-0500	VoiceOver	AudioConverter -> 0xbf23fdef0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:04.539697-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:04.540208-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:04.540554-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:04.540477-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:04.540771-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:04.540819-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:04.540884-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:04.541214-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:04.541292-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:04.541335-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:04.541668-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:04.541687-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:04.557411-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7679532 ioTS st: 7679532 ht: 138144.160033
default	20:22:04.563251-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:04.563554-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:04.577379-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:04.577639-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:04.577677-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:04.580473-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876562 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:04.581516-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876563 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:04.613378-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:04.613847-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:04.614156-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:04.614224-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:04.614442-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:04.614470-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:04.614511-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:04.614737-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:04.614809-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:04.614851-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:04.615086-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:04.615104-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:04.627398-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7681076 ioTS st: 7681076 ht: 138144.230033
error	20:22:04.651484-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:05.699384-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:05.700303-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:05.700438-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:06.097038-0500	VoiceOver	No list of permitted front apps returned
default	20:22:06.097357-0500	VoiceOver	No list of permitted front apps returned
default	20:22:06.123193-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:06.123461-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:06.139929-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874840, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:06.139977-0500	VoiceOver	AudioConverter -> 0xbf2874840: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:06.140007-0500	VoiceOver	AudioConverter -> 0xbf2874840: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:06.159244-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:06.165889-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28743c0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:06.165925-0500	VoiceOver	AudioConverter -> 0xbf28743c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:06.165968-0500	VoiceOver	AudioConverter -> 0xbf28743c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:06.179881-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:06.187779-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:06.187846-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:06.189063-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876563 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:06.189892-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876564 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:06.217046-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:06.217747-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:06.217704-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:06.218007-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:06.218035-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	20:22:06.218015-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:06.218069-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:06.218230-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:06.218293-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:06.218322-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:06.218540-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:06.218561-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:06.237281-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7716577 ioTS st: 7716577 ht: 138145.840033
default	20:22:06.249423-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:06.249627-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
error	20:22:06.288070-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:22:07.575931-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:07.615544-0500	VoiceOver	No list of permitted front apps returned
default	20:22:07.671243-0500	VoiceOver	No list of permitted front apps returned
default	20:22:07.716504-0500	VoiceOver	No list of permitted front apps returned
default	20:22:07.819099-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:07.819780-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:07.819866-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:07.884135-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:07.884263-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:07.898468-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:07.898550-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:07.902179-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2875110, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:07.902199-0500	VoiceOver	AudioConverter -> 0xbf2875110: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:07.902208-0500	VoiceOver	AudioConverter -> 0xbf2875110: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:07.913958-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:07.917753-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:07.917810-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:07.921828-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876564 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	20:22:07.922297-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876567 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:07.969944-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:07.970277-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:07.970674-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:07.970838-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:07.971086-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:07.971111-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:07.971153-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:07.971329-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:07.971395-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:07.971425-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:07.971647-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:07.971659-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:07.987451-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7755165 ioTS st: 7755165 ht: 138147.590033
error	20:22:08.362452-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:08.596003-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:08.596290-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
fault	20:22:09.323415-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:09.342112-0500	VoiceOver	No list of permitted front apps returned
default	20:22:09.450637-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:09.451514-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:09.467154-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:09.467319-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:09.475862-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:09.476051-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:09.484344-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:09.487612-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:09.487679-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
error	20:22:09.729633-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:09.735069-0500	VoiceOver	[0xbf066b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:09.735189-0500	VoiceOver	[0xbf066b200] invalidated after the last release of the connection object
default	20:22:09.740786-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf23fd980, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:09.740823-0500	VoiceOver	AudioConverter -> 0xbf23fd980: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:09.740835-0500	VoiceOver	AudioConverter -> 0xbf23fd980: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:09.754703-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:09.757510-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:09.757550-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:09.769381-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876569 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:09.823952-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:09.824367-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:09.824836-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:09.824832-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:09.825045-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:09.825071-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:09.825115-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:09.825292-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:09.825361-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:09.825406-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:09.825633-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:09.825649-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:22:09.982621-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:10.696908-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:10.697670-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:10.697732-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:10.715430-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876570 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:10.716001-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876571 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:10.756974-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:10.757467-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:10.757791-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:10.757771-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:10.758008-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:10.758039-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:10.758081-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:10.758233-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:10.758290-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:10.758327-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:10.758538-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:10.758563-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:10.777406-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7816685 ioTS st: 7816685 ht: 138150.380033
error	20:22:10.812434-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:11.785324-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2c2a0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:11.785353-0500	VoiceOver	AudioConverter -> 0xbf2a2c2a0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:11.785365-0500	VoiceOver	AudioConverter -> 0xbf2a2c2a0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:11.798434-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:11.807993-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:11.808093-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:11.810981-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876571 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:11.811948-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876572 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:11.834558-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:11.835022-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:11.835324-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:11.835398-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:11.835603-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:11.835644-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:11.835700-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:11.835958-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:11.836026-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:11.836086-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:11.836313-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:11.836325-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:11.847271-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7840279 ioTS st: 7840279 ht: 138151.450033
error	20:22:11.892488-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:12.619009-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2e4c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:12.619045-0500	VoiceOver	AudioConverter -> 0xbf2a2e4c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:12.619056-0500	VoiceOver	AudioConverter -> 0xbf2a2e4c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:13.277929-0500	VoiceOver	No list of permitted front apps returned
default	20:22:13.278409-0500	VoiceOver	No list of permitted front apps returned
default	20:22:13.291647-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:13.292088-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:13.292169-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:13.301085-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:13.301275-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:13.317887-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:13.318115-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:13.320935-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2ecd0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:13.320962-0500	VoiceOver	AudioConverter -> 0xbf2a2ecd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:13.320981-0500	VoiceOver	AudioConverter -> 0xbf2a2ecd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:13.333859-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2e490, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:13.333884-0500	VoiceOver	AudioConverter -> 0xbf2a2e490: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:13.333893-0500	VoiceOver	AudioConverter -> 0xbf2a2e490: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:13.338803-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:13.347567-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:13.347609-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:13.350892-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876572 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:13.351398-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876573 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:13.387428-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:13.388158-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:13.388230-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:13.388359-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:13.388386-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:13.388427-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:13.388576-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
fault	20:22:13.388619-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:13.388634-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:13.388669-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:13.388926-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:13.388945-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:13.407444-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7874677 ioTS st: 7874677 ht: 138153.010033
error	20:22:13.484857-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:16.350850-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:16.357836-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:16.357914-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:16.365725-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474876573 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:16.399363-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:16.399600-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:16.424521-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:16.424639-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:16.425019-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:16.425807-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:22:16.431041-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876575 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:16.431277-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:22:16.446316-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:16.446484-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:16.463442-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:16.464021-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:16.464133-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:16.464266-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:16.464365-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:16.464392-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:16.464431-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:16.464575-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:16.464633-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:16.464663-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:16.464893-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:16.464909-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:16.477344-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7942371 ioTS st: 7942371 ht: 138156.080033
error	20:22:16.492865-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:17.588624-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876575 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.146985-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876577 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.148535-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:18.148840-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:18.159698-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:18.160603-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:18.160747-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:22:18.167639-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:18.167680-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:18.168574-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876577 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.169712-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876578 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.184360-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876578 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.186453-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876579 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:18.229006-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:18.229532-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:18.229645-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:18.229758-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:18.229831-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:18.229855-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:18.229883-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:18.230016-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:18.230073-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:18.230102-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:18.230293-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:18.230307-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:18.247263-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 7981400 ioTS st: 7981400 ht: 138157.850033
error	20:22:18.280836-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:19.195039-0500	powerd	Process VoiceOver.98203 Summary PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876579 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:20.998817-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876579 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:21.212590-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:22:21.528412-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876581 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:21.536653-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:22:21.691001-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:22:26.907167-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:26.911330-0500	VoiceOver	No list of permitted front apps returned
default	20:22:27.012552-0500	VoiceOver	No list of permitted front apps returned
default	20:22:27.056729-0500	VoiceOver	No list of permitted front apps returned
default	20:22:27.076555-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2e130, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:27.076591-0500	VoiceOver	AudioConverter -> 0xbf2a2e130: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:27.076605-0500	VoiceOver	AudioConverter -> 0xbf2a2e130: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:27.081991-0500	VoiceOver	No list of permitted front apps returned
default	20:22:27.083983-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:27.084965-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:27.085087-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:27.102833-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:27.102973-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:27.129199-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:27.129354-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:22:27.131855-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad52c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:27.131880-0500	VoiceOver	AudioConverter -> 0xbf2ad52c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:27.131896-0500	VoiceOver	AudioConverter -> 0xbf2ad52c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:27.137407-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:27.140260-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:27.144434-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:27.147785-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:27.147836-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:27.156678-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876581 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:27.157048-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876584 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:27.197040-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:27.197325-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:27.197576-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:27.197693-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:27.197864-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:27.197885-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:27.197913-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:27.198467-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:27.198524-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:27.198549-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:27.198740-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:27.198755-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:27.217257-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8179189 ioTS st: 8179189 ht: 138166.820033
error	20:22:27.349668-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:28.768001-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:28.768909-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:28.769062-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:28.897296-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:28.897566-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:28.898061-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:28.898730-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:28.898839-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:28.902513-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2e5b0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:28.902549-0500	VoiceOver	AudioConverter -> 0xbf2a2e5b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:28.902590-0500	VoiceOver	AudioConverter -> 0xbf2a2e5b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:29.262048-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:29.262702-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:29.262851-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:29.691766-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:29.692615-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:29.692768-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:29.784272-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:29.785177-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:29.785382-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:31.717998-0500	VoiceOver	No list of permitted front apps returned
fault	20:22:31.718959-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:31.746709-0500	VoiceOver	No list of permitted front apps returned
default	20:22:31.763822-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:31.765299-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:31.765466-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:31.780555-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:31.780709-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:31.791841-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:31.791990-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:31.808954-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:31.817821-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:31.817912-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:31.819813-0500	VoiceOver	No list of permitted front apps returned
default	20:22:31.834388-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474876584 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:31.834995-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876589 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:31.878309-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:31.878627-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:31.878907-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:31.878931-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:31.879142-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:31.879167-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:31.879195-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:31.879326-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:31.879385-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:31.879415-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:31.879626-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:31.879638-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:22:31.949167-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:36.538842-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474876589 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:36.749428-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:22:37.075695-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876595 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:37.085839-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:22:37.244038-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:40.662286-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98281
fault	20:22:42.167422-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:42.168919-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.274352-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.274914-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:42.275576-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:42.275681-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:42.369007-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.369203-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.370929-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:42.371059-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:42.374624-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:42.374705-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:22:42.376385-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf201d650, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:42.376419-0500	VoiceOver	AudioConverter -> 0xbf201d650: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:42.376429-0500	VoiceOver	AudioConverter -> 0xbf201d650: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:42.382816-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:42.384403-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.386643-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:42.386744-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:22:42.388020-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:42.392390-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:42.397458-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf201edf0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:42.397480-0500	VoiceOver	AudioConverter -> 0xbf201edf0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:42.397490-0500	VoiceOver	AudioConverter -> 0xbf201edf0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:42.398158-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:42.398200-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:42.408152-0500	VoiceOver	No list of permitted front apps returned
default	20:22:42.409991-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876595 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.411026-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876596 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.412889-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:42.413007-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:42.440851-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876596 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.441147-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876597 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.466121-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876597 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.466435-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876598 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:42.518137-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:42.518385-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:22:42.518637-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:42.518745-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:42.518954-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:42.518976-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:42.519002-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:42.519140-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:42.519201-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:42.519226-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:42.519442-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:42.519455-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:22:42.556840-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:43.974138-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:43.975184-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:43.975358-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:44.459137-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876598 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:44.657313-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:44.658236-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:44.658401-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:44.670552-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:22:44.943198-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:44.943818-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:44.943941-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:44.969660-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876599 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:44.981311-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:22:45.071870-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:45.321374-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:45.322112-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:45.322242-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:45.806252-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:45.807209-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:45.807405-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:46.330462-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:46.331434-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:46.331618-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:46.351620-0500	VoiceOver	No list of permitted front apps returned
fault	20:22:46.370379-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:46.392666-0500	VoiceOver	No list of permitted front apps returned
default	20:22:46.401346-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:46.402132-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:46.402257-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:46.419661-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:46.419910-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:46.440174-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:46.440347-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:46.453357-0500	VoiceOver	No list of permitted front apps returned
default	20:22:46.459367-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:46.468581-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:46.468676-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:46.474425-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876599 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:46.475003-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876600 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:46.506627-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:46.506655-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:46.506696-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:46.506864-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:46.506933-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:46.506966-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:46.507193-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:46.507211-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:46.518042-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8604755 ioTS st: 8604755 ht: 138186.120033
error	20:22:46.569820-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:22:50.794464-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:50.800266-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98287
default	20:22:50.800709-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98287
default	20:22:51.111852-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98290
default	20:22:51.121402-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98290
default	20:22:51.159801-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474876600 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:51.371846-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:22:51.684626-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876604 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:51.699891-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:22:51.862474-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:52.092345-0500	VoiceOver	No list of permitted front apps returned
default	20:22:52.092596-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:52.092612-0500	VoiceOver	No list of permitted front apps returned
default	20:22:52.093221-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:52.093313-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:52.161257-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:52.168855-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:52.168909-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:52.185787-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876604 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:52.186574-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876605 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:52.218760-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:52.219341-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:52.219513-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:52.219635-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:52.219809-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:52.219835-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:52.219870-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:52.220045-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:52.220120-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:52.220148-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:52.220567-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:52.220592-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:22:52.259396-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:52.274818-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98291
default	20:22:52.724076-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98294
default	20:22:53.056986-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98297
default	20:22:53.059493-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98297
default	20:22:53.649873-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:53.650162-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:22:53.667614-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad5470, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:53.667649-0500	VoiceOver	AudioConverter -> 0xbf2ad5470: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:53.667675-0500	VoiceOver	AudioConverter -> 0xbf2ad5470: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:53.687342-0500	VoiceOver	[0xbf066b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:53.687817-0500	VoiceOver	[0xbf066b200] invalidated after the last release of the connection object
default	20:22:53.691298-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:53.716006-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:53.716509-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:22:53.720998-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:53.733475-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876606 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:53.746213-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:22:53.775432-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:53.776559-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:22:53.776976-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:53.777009-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	20:22:53.776120-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:53.777050-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:53.777472-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:53.777605-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	20:22:53.776501-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:53.777693-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:53.778115-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:53.778139-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:53.788484-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8765060 ioTS st: 8765060 ht: 138193.390033
error	20:22:54.022701-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:54.822829-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:54.823061-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:22:56.610673-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:22:56.615089-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:56.618684-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:56.618722-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:56.623116-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876606 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:56.625439-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876614 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:56.649177-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:22:56.649682-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:56.649815-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:56.649950-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:56.650019-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:56.650041-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:56.650077-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:22:56.650281-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:56.650357-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:56.650388-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:56.650643-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:56.650659-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:56.668574-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8828565 ioTS st: 8828565 ht: 138196.270033
default	20:22:56.669331-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98300
error	20:22:56.710959-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:57.254479-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2c2a0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:57.254518-0500	VoiceOver	AudioConverter -> 0xbf2a2c2a0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:57.254528-0500	VoiceOver	AudioConverter -> 0xbf2a2c2a0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:58.499530-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876614 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	20:22:58.935439-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:22:58.935908-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:22:58.935992-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:22:58.937633-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2d500, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:22:58.937678-0500	VoiceOver	AudioConverter -> 0xbf2a2d500: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:22:58.937685-0500	VoiceOver	AudioConverter -> 0xbf2a2d500: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:22:59.099925-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:22:59.109347-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:22:59.109517-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:22:59.245951-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876619 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:22:59.268918-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:22:59.269840-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:22:59.269829-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:59.270057-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:22:59.270087-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:22:59.270132-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:22:59.270169-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:59.270356-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:22:59.270426-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:22:59.270468-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:22:59.270710-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:22:59.270729-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:22:59.288739-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8886336 ioTS st: 8886336 ht: 138198.890033
error	20:22:59.323542-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:22:59.610480-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:22:59.610794-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:22:59.682718-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98305
default	20:22:59.683109-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98305
fault	20:22:59.824856-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:22:59.828357-0500	VoiceOver	No list of permitted front apps returned
default	20:22:59.919394-0500	VoiceOver	No list of permitted front apps returned
fault	20:22:59.924757-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:00.020729-0500	VoiceOver	No list of permitted front apps returned
default	20:23:00.797709-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:00.799248-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:00.799357-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:00.802490-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876619 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:00.868346-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2c0c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:00.868381-0500	VoiceOver	AudioConverter -> 0xbf2a2c0c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:00.868393-0500	VoiceOver	AudioConverter -> 0xbf2a2c0c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:00.893460-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:00.893702-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:00.914891-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:00.925265-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:00.931469-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876620 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:00.969321-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:00.970194-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:00.970221-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:00.970381-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:00.970415-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:00.970453-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:23:00.970558-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:00.970654-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:00.970730-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:00.970767-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:00.971012-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:00.971028-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:00.988745-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8923822 ioTS st: 8923822 ht: 138200.590033
error	20:23:01.088128-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:01.677707-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 98306
default	20:23:01.681237-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 98306
default	20:23:02.274194-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:02.274476-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:02.325009-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:02.325179-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:02.325498-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:23:02.327790-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:02.329277-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:02.329350-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:02.335372-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:02.335649-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:02.340971-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876620 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:02.341780-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876621 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:02.380106-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:02.380714-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:02.380779-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:02.380975-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:02.381009-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:02.381035-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:02.381066-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:02.381226-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:02.381280-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:02.381308-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:02.381513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:02.381530-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:02.398782-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8954913 ioTS st: 8954913 ht: 138202.000033
error	20:23:02.423250-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:03.624830-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:03.629070-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:03.629132-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:03.636729-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876621 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:03.693607-0500	VoiceOver	No list of permitted front apps returned
default	20:23:03.693905-0500	VoiceOver	No list of permitted front apps returned
default	20:23:03.694724-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:03.694889-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:03.707297-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:03.707452-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:03.719865-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:03.720024-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:03.724679-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:03.724855-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:03.727773-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876622 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:03.748318-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf292f8a0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:03.748780-0500	VoiceOver	AudioConverter -> 0xbf292f8a0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:03.748811-0500	VoiceOver	AudioConverter -> 0xbf292f8a0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:03.761059-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:03.761661-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:03.761744-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:03.761859-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:03.761895-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:03.761934-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:23:03.762022-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:03.762085-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:03.762161-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:03.762192-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:03.762430-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:03.762445-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:03.769362-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:03.769470-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:03.778747-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8985343 ioTS st: 8985343 ht: 138203.380033
default	20:23:03.804470-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:03.809196-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:03.819099-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:03.819128-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:03.820569-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876622 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:03.821295-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876623 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:03.852456-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:03.852798-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:03.853106-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:03.853177-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:03.853424-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:03.853447-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:03.853483-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:03.853626-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:03.853696-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:03.853725-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:03.853956-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:03.853971-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:03.868792-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 8987328 ioTS st: 8987328 ht: 138203.470033
error	20:23:03.893208-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:04.785197-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:04.789043-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:04.789108-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:04.791265-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876623 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:04.791845-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876624 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:04.814723-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:04.815269-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:04.815567-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:04.815680-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:04.815793-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:04.815823-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:04.815869-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:04.816041-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:04.816111-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:04.816148-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:04.816379-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:04.816395-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:04.828816-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9008496 ioTS st: 9008496 ht: 138204.430033
default	20:23:04.858809-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:04.869091-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:04.869143-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:04.873007-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876624 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:04.873537-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876625 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:04.901355-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:04.901675-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:04.907674-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:04.907957-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:04.908277-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:04.908395-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:04.908572-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:04.908596-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:04.908629-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:04.908768-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:04.908827-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:04.908854-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:04.909039-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:04.909053-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:04.928771-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9010702 ioTS st: 9010702 ht: 138204.530033
error	20:23:04.952050-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:06.729453-0500	VoiceOver	No list of permitted front apps returned
default	20:23:06.729914-0500	VoiceOver	No list of permitted front apps returned
default	20:23:06.735687-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:06.736061-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:06.745670-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2cf90, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:06.745706-0500	VoiceOver	AudioConverter -> 0xbf2a2cf90: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:06.745724-0500	VoiceOver	AudioConverter -> 0xbf2a2cf90: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:06.760627-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:06.769954-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2ccc0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:06.769989-0500	VoiceOver	AudioConverter -> 0xbf2a2ccc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:06.770005-0500	VoiceOver	AudioConverter -> 0xbf2a2ccc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:06.773231-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:06.778645-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:06.779143-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:06.779189-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:06.780247-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876625 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:06.780839-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876627 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:06.810663-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:06.811559-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:06.811625-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:06.811811-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:06.811847-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:06.811902-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:23:06.811976-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:06.812108-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:06.812200-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:06.812239-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:06.812503-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:06.812520-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:06.828902-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9052598 ioTS st: 9052598 ht: 138206.430033
error	20:23:06.898334-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:07.142227-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:07.142535-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:07.175507-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:07.182718-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:07.189044-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:07.189085-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:07.196572-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876627 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:07.197005-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876628 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:07.198162-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad5440, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:07.198195-0500	VoiceOver	AudioConverter -> 0xbf2ad5440: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:07.198230-0500	VoiceOver	AudioConverter -> 0xbf2ad5440: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:07.231249-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:07.231512-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:07.231767-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:07.231942-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:07.232117-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:07.232137-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:07.232167-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:07.232300-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:07.232357-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:07.232379-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:07.232573-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:07.232588-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:07.248781-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9061859 ioTS st: 9061859 ht: 138206.850033
error	20:23:07.312155-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:07.907522-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:07.907777-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:08.565943-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:08.566306-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:09.749088-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:09.749241-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:12.316181-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2dd10, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:12.316201-0500	VoiceOver	AudioConverter -> 0xbf2a2dd10: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:12.316211-0500	VoiceOver	AudioConverter -> 0xbf2a2dd10: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:12.375763-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:12.375925-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:12.967792-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:12.968019-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:13.022160-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876628 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:13.298269-0500	VoiceOver	No list of permitted front apps returned
fault	20:23:13.302066-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:13.392906-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:13.395450-0500	VoiceOver	No list of permitted front apps returned
default	20:23:13.497359-0500	VoiceOver	No list of permitted front apps returned
default	20:23:13.619322-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:13.629115-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:13.629163-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:13.674633-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876630 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:13.700067-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:13.700432-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:13.700728-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:13.700758-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:13.701018-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:13.701046-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:13.701078-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:13.701265-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:13.701323-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:13.701351-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:13.701581-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:13.701601-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:13.718955-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9204523 ioTS st: 9204523 ht: 138213.320033
default	20:23:14.049433-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:14.049572-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:14.070071-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:14.075165-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:14.079138-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:14.079176-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:14.102144-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876630 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:14.102480-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876631 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:14.102606-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc0d20, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:14.102623-0500	VoiceOver	AudioConverter -> 0xbf2bc0d20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:14.102648-0500	VoiceOver	AudioConverter -> 0xbf2bc0d20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:14.162415-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:14.162811-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:14.163022-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:14.163199-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:23:14.163182-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:14.163223-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:14.163252-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:14.163393-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:14.163449-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:14.163472-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:14.163657-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:14.163671-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:23:14.238857-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:19.950345-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876631 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:20.163532-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:20.549937-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:20.559822-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:20.560059-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:21.548044-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:21.548273-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:23:21.577568-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:21.586797-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876633 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:21.587167-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:23:21.628145-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:21.628803-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:21.628865-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:21.629012-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:21.629045-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:21.629086-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:23:21.629132-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:21.629266-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:21.629333-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:21.629371-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:21.629604-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:21.629622-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:21.649013-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9379380 ioTS st: 9379380 ht: 138221.250033
error	20:23:21.715931-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:23.098822-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:23.099112-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:27.419795-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876633 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:27.631661-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:27.960771-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:27.961014-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:27.992372-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:28.001003-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:23:28.001008-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876635 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:28.019619-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:28.029247-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:28.029278-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:28.041016-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:28.041687-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:28.041819-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:28.041894-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:28.041923-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:28.041949-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:28.042115-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
fault	20:23:28.042076-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:28.042203-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:28.042234-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:28.042455-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:28.042469-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:28.059061-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9520721 ioTS st: 9520721 ht: 138227.660033
error	20:23:28.124275-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:29.775813-0500	VoiceOver	No list of permitted front apps returned
default	20:23:29.776098-0500	VoiceOver	No list of permitted front apps returned
default	20:23:29.794473-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:29.794641-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:29.816710-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:29.816977-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:29.831017-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:29.831265-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:29.831443-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:29.835788-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:29.835942-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:29.839442-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:29.839519-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:29.845980-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876635 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:29.846556-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876637 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:29.847099-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28768e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:29.847189-0500	VoiceOver	AudioConverter -> 0xbf28768e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:29.847208-0500	VoiceOver	AudioConverter -> 0xbf28768e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:29.863830-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874f60, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:29.863848-0500	VoiceOver	AudioConverter -> 0xbf2874f60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:29.863868-0500	VoiceOver	AudioConverter -> 0xbf2874f60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:29.878263-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:29.878848-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:29.878950-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:29.879077-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:29.879160-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:29.879183-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:29.879216-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:29.879379-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:29.879439-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:29.879466-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:29.879650-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:29.879666-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:29.899104-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9561293 ioTS st: 9561293 ht: 138229.500033
error	20:23:29.917512-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:30.864945-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:30.870836-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:30.874360-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:30.879553-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:30.879642-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:30.882211-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876637 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:30.882853-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876638 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:30.906033-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:30.906501-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:30.906843-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:30.906939-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:30.907164-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:30.907195-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:30.907238-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:30.907427-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:30.907491-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:30.907529-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:30.907766-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:30.907783-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:30.919032-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9583784 ioTS st: 9583784 ht: 138230.520033
error	20:23:30.995837-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:31.539735-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:31.549474-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:31.549556-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:31.558835-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876638 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:31.559241-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876639 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:31.594499-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:31.594661-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:23:31.597779-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:31.598071-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:31.598444-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:31.598778-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:31.598973-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:31.599001-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:31.599039-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:31.599188-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:31.599251-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:31.599281-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:31.599478-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:31.599493-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:31.601526-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc0270, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:31.601557-0500	VoiceOver	AudioConverter -> 0xbf2bc0270: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:31.601566-0500	VoiceOver	AudioConverter -> 0xbf2bc0270: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:31.602652-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:31.609555-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:31.618072-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:31.619251-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:31.619282-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:31.620501-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876639 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:31.620867-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876640 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:31.653193-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:31.653507-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:31.653872-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:31.653901-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:31.654139-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:31.654164-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:31.654194-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:31.654334-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:31.654392-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:31.654427-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:31.654673-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:31.654689-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:31.669080-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9600323 ioTS st: 9600323 ht: 138231.270033
error	20:23:31.749033-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:34.710189-0500	VoiceOver	No list of permitted front apps returned
default	20:23:34.710405-0500	VoiceOver	No list of permitted front apps returned
default	20:23:34.717827-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:34.717998-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:34.734731-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2d080, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:34.734778-0500	VoiceOver	AudioConverter -> 0xbf2a2d080: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:34.734801-0500	VoiceOver	AudioConverter -> 0xbf2a2d080: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:34.748431-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2d3b0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:34.748461-0500	VoiceOver	AudioConverter -> 0xbf2a2d3b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:34.748477-0500	VoiceOver	AudioConverter -> 0xbf2a2d3b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:34.755382-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:34.759609-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:34.759680-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:34.767043-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474876640 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:34.767987-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876643 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:34.778486-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876be0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:34.778511-0500	VoiceOver	AudioConverter -> 0xbf2876be0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:34.778526-0500	VoiceOver	AudioConverter -> 0xbf2876be0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:34.790349-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2877720, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:34.790371-0500	VoiceOver	AudioConverter -> 0xbf2877720: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:34.790386-0500	VoiceOver	AudioConverter -> 0xbf2877720: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:34.795520-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:34.796214-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:34.796261-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:34.796473-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:23:34.796479-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:34.796505-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:34.796540-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:34.796772-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:34.796839-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:34.796890-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:34.797107-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:34.797125-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:34.809187-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9669561 ioTS st: 9669561 ht: 138234.410033
error	20:23:34.837049-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:35.403234-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:35.404287-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:35.404434-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:35.497483-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:35.501723-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:35.509423-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:35.509500-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:35.512181-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876643 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:35.513350-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876644 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:35.535073-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:35.535514-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:35.535815-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:35.535876-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:35.536062-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:35.536091-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:35.536133-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:35.536286-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:35.536341-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:35.536377-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:35.536586-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:35.536604-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:35.549242-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9685878 ioTS st: 9685878 ht: 138235.150033
error	20:23:35.550468-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:35.693855-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:35.694705-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:35.694866-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:35.745060-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:35.751594-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:35.759582-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:35.759644-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:35.761027-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876644 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:35.762002-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876645 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:35.787750-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:35.788055-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:35.788326-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:35.788429-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:35.788615-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:35.788639-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:35.788674-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:35.788829-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:35.788894-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:35.788924-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:35.789122-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:35.789135-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:35.809056-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9691611 ioTS st: 9691611 ht: 138235.410033
error	20:23:35.809525-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:36.120045-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876645 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:36.496783-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:36.497029-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:36.593290-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:36.593883-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:36.593992-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:36.642752-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:36.645646-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876646 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:23:36.670954-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:36.742858-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:36.743588-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:36.743717-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:36.800622-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:36.802639-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:36.809562-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:36.809649-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:36.811078-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876646 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:36.811569-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876647 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:36.828315-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:36.828675-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:36.828969-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:36.829056-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:36.829250-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:36.829276-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:36.829312-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:36.829452-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:36.829504-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:36.829534-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:36.829750-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:36.829772-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:36.849157-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9714544 ioTS st: 9714544 ht: 138236.450033
error	20:23:36.851938-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:36.913939-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:36.914680-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:36.914824-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:36.954735-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:36.956780-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:36.959605-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:36.959680-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:36.961201-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876647 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:36.962430-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876648 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:36.978270-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:36.978621-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:36.978914-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:36.978959-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:36.979166-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:36.979193-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:36.979228-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:36.979367-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:36.979418-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:36.979444-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:36.979641-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:36.979657-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:36.999247-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9717852 ioTS st: 9717852 ht: 138236.600033
error	20:23:37.000497-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:37.350079-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876648 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:37.563998-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:37.861860-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:37.862576-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:37.862699-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:37.902277-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:37.905424-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876649 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:37.907305-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:23:37.928809-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:38.040214-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:38.041029-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:38.041188-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:38.073791-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:38.075937-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:38.079921-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:38.080022-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:38.082756-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876649 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:38.084100-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876650 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:38.102653-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:38.103099-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:38.103389-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:38.103471-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:38.103679-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:38.103708-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:38.103748-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:38.103907-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:38.103961-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:38.103995-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:38.104237-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:38.104254-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:38.119170-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9742548 ioTS st: 9742548 ht: 138237.720033
error	20:23:38.119563-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:38.242108-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:38.242791-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:38.242917-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:38.274559-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:38.276524-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:38.279512-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:38.279597-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:38.280911-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876650 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:38.282056-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876651 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:38.299190-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:38.299592-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:38.299916-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:38.300069-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:38.300328-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:38.300362-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:38.300410-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:38.300734-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:38.300815-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:38.300862-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:38.301127-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:38.301148-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:38.319232-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9746958 ioTS st: 9746958 ht: 138237.920033
error	20:23:38.321414-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:38.710485-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876651 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:38.922513-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:39.226957-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:39.227649-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:39.227806-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:39.270703-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:39.274169-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876652 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.275562-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:23:39.303878-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:39.386850-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:39.387558-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:39.387680-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:39.424616-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:39.426964-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:39.429580-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:39.429711-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:39.431042-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876652 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.431902-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876653 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.453353-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:39.453784-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:39.454113-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:39.454175-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:39.454380-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:39.454411-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:39.454452-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:39.454632-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:39.454689-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:39.454734-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:39.454969-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:39.454987-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:39.469233-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9772316 ioTS st: 9772316 ht: 138239.070033
error	20:23:39.469460-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:39.541744-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:39.542428-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:39.542543-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:39.574940-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:39.577229-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:39.579540-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:39.579622-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:39.581020-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876653 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.582257-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876654 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.597965-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:39.598381-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:39.598671-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:39.598769-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:39.598983-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:39.599009-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:39.599071-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:39.599231-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:39.599292-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:39.599323-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:39.599534-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:39.599549-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:39.619216-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9775624 ioTS st: 9775624 ht: 138239.220033
error	20:23:39.619776-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:39.686928-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:39.687558-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:39.687730-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:39.724328-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:39.726517-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:39.729533-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:39.729612-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:39.731319-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876654 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.732319-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876655 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.755068-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:39.755507-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:39.755803-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:39.755873-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:39.756066-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:39.756092-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:39.756138-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:39.756298-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:39.756359-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:39.756396-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:39.756608-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:39.756625-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:39.769171-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9778932 ioTS st: 9778932 ht: 138239.370033
error	20:23:39.769387-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:39.836904-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:39.837635-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:39.837780-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:39.872543-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:39.874866-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:39.879493-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:39.879575-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:39.881043-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876655 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.882066-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876656 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:39.901510-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:39.901951-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:39.902256-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:39.902312-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:39.902533-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:39.902561-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:39.902601-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:39.902757-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:39.902812-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:39.902846-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:39.903073-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:39.903090-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:39.919167-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9782240 ioTS st: 9782240 ht: 138239.520033
error	20:23:39.921534-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:40.230945-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:40.231774-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:40.231911-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:40.267343-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:40.269684-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:40.279704-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:40.279841-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:40.281927-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876656 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.282613-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876657 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.305891-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:40.306350-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:40.306665-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.306790-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:40.307003-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:40.307032-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:40.307071-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:40.307224-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:40.307285-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:40.307328-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:40.307547-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:40.307564-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:40.319215-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9791060 ioTS st: 9791060 ht: 138239.920033
error	20:23:40.321741-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:40.550355-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:40.551325-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:40.551158-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:40.611885-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:40.615705-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:40.619579-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:40.619652-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:40.621721-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876657 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.622911-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876658 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.641587-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:40.642308-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.642795-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:40.642869-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.643131-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:40.643191-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:40.643264-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:40.643600-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:40.643702-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:40.643752-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:40.644433-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:40.644488-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:40.659240-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9798557 ioTS st: 9798557 ht: 138240.260033
error	20:23:40.664691-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:40.682838-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98313
default	20:23:40.692748-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:40.693456-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:40.693591-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:40.719841-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98316
default	20:23:40.744779-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:40.752752-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:40.759721-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:40.759803-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:40.761908-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876658 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.762581-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876659 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.780956-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:40.781307-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.781740-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:40.781744-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.781972-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:40.782000-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:40.782042-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:40.782248-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:40.782315-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:40.782347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:40.782619-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:40.782644-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:40.799071-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9801644 ioTS st: 9801644 ht: 138240.400033
error	20:23:40.801887-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:40.840230-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:40.840672-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:40.840755-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:40.872030-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:40.873620-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:40.881577-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:40.881663-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:40.889475-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876659 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.889889-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876660 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:40.909926-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:40.910425-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.910701-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:40.910783-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:40.910944-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:40.910974-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:40.911016-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:40.911202-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:40.911262-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:40.911294-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:40.911520-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:40.911536-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:40.929096-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9804511 ioTS st: 9804511 ht: 138240.530033
error	20:23:40.930849-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:41.280011-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876660 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:41.489353-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:41.879797-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:41.886498-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:41.889693-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:41.889797-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:41.896691-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876661 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:41.897769-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:23:41.916286-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:41.916668-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:41.916955-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:41.917010-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:41.917210-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:41.917233-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:41.917272-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:41.917416-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:41.917469-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:41.917500-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:41.917689-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:41.917704-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:41.929184-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9826561 ioTS st: 9826561 ht: 138241.530033
error	20:23:41.932157-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:42.390347-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876661 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:42.599735-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:42.990207-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:43.000076-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:43.000221-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:44.517028-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:23:44.535414-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:23:45.099282-0500	VoiceOver	aqmeio@0xbf0a97618 Stop id=85
default	20:23:45.099308-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:45.099797-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:46.019071-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:23:46.019793-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ad","name":"VoiceOver(98203)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:23:46.019988-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 173 stopping playing
default	20:23:46.020090-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:23:46.020165-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:23:46.020349-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:23:46.021992-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.022051-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.021961-0500	runningboardd	Invalidating assertion 400-332-143784 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.powerd>:332]
default	20:23:46.022365-0500	runningboardd	Invalidating assertion 400-98203-143962 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:23:46.021783-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.021910-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:23:46.021810-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40ad to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":98203}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40ad, sessionType: 'prim', isRecording: false }, 
]
default	20:23:46.021924-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:23:46.022078-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 2
default	20:23:46.072298-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:46.072308-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:46.072325-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:46.072366-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:46.072391-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:46.077224-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:23:46.081680-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:46.082417-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:46.082314-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:46.122807-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:46.125719-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876663 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:46.126116-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:23:46.126426-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144226 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:23:46.126564-0500	runningboardd	Assertion 400-332-144226 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:23:46.127064-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:46.127080-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:46.127094-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:46.127275-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:46.127338-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:46.148257-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:46.149029-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:46.149135-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:46.149279-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:46.149358-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:46.149394-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:46.149461-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:46.149636-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:46.149696-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:46.150059-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144227 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:23:46.150141-0500	runningboardd	Assertion 400-98203-144227 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:23:46.151804-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:46.151817-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:46.151850-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:46.151906-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:46.151962-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:46.168147-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:46.169061-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ad","name":"VoiceOver(98203)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:23:46.169270-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:23:46.169295-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 173 starting playing
default	20:23:46.169450-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:23:46.169522-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:23:46.169574-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:23:46.169637-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	20:23:46.169673-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40ad to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":98203}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40ad, sessionType: 'prim', isRecording: false }, 
]
default	20:23:46.169750-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:23:46.169764-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:23:46.169789-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:46.170089-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x91550001 category Not set
default	20:23:46.170351-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.170449-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.170479-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:46.170494-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 3
default	20:23:46.170507-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:23:46.181998-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:23:46.188328-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9920478 ioTS st: 9920478 ht: 138245.789283
error	20:23:46.190423-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:46.271738-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:46.272425-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:46.272557-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:46.311433-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:46.313493-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:46.318998-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:46.319084-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:46.320804-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876663 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:46.322813-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876664 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:46.341615-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:46.342108-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:46.342487-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:46.342691-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:46.342720-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:46.342803-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:46.343013-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:46.343092-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:46.343195-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:46.343450-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:46.343463-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	20:23:46.342398-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:46.358675-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 9924227 ioTS st: 9924227 ht: 138245.959283
error	20:23:46.359163-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:46.642986-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:23:46.643461-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:23:46.643554-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:23:46.669178-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876664 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:46.698798-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:46.701555-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876665 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:23:46.726677-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:47.159576-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876665 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:47.372246-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:47.709348-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:47.715881-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876666 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:47.716370-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:23:47.749502-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:47.769907-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:23:48.144047-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98347
default	20:23:48.144427-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98347
default	20:23:48.469316-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876666 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:48.683017-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:49.069072-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:49.078891-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:49.079014-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:51.178436-0500	VoiceOver	aqmeio@0xbf0a97618 Stop id=85
default	20:23:51.178936-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ad","name":"VoiceOver(98203)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:23:51.179111-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 173 stopping playing
default	20:23:51.179204-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:23:51.179279-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:23:51.179455-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:23:51.178435-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:51.181370-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.181436-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.180429-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:23:51.181454-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 2
default	20:23:51.180208-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40ad to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":98203}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40ad, sessionType: 'prim', isRecording: false }, 
]
default	20:23:51.180455-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:23:51.181361-0500	runningboardd	Invalidating assertion 400-98203-144227 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:23:51.181159-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.181473-0500	runningboardd	Invalidating assertion 400-332-144226 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.powerd>:332]
default	20:23:51.288105-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:51.288119-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:51.288130-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:51.288152-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:51.288166-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:51.292192-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:23:51.559423-0500	VoiceOver	No list of permitted front apps returned
default	20:23:51.559736-0500	VoiceOver	No list of permitted front apps returned
default	20:23:51.566082-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:51.566304-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:23:51.591978-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:51.593193-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2e850, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:51.593225-0500	VoiceOver	AudioConverter -> 0xbf2a2e850: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:51.593239-0500	VoiceOver	AudioConverter -> 0xbf2a2e850: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:51.595207-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144233 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:23:51.595366-0500	runningboardd	Assertion 400-98203-144233 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:23:51.595828-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144234 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:23:51.595838-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:51.595959-0500	runningboardd	Assertion 400-332-144234 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:23:51.595993-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:51.596040-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:51.596124-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:51.596162-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:51.601780-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:23:51.601821-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:23:51.601846-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:23:51.601931-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:23:51.601963-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:23:51.603436-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:23:51.606437-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:23:51.608807-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:51.609447-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:23:51.610385-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ad","name":"VoiceOver(98203)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:23:51.610574-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:23:51.610594-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 173 starting playing
default	20:23:51.610678-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:23:51.610733-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:23:51.610765-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:23:51.610804-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	20:23:51.610843-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40ad to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":98203}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40ad, sessionType: 'prim', isRecording: false }, 
]
default	20:23:51.610913-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:23:51.610927-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:23:51.611121-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x91550001 category Not set
default	20:23:51.611226-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:23:51.611393-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.611488-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.611521-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	20:23:51.611540-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 3
default	20:23:51.611551-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:23:51.616302-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876668 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:51.646461-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:23:51.647140-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:23:51.647217-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:51.647362-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:51.647389-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:51.647423-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:23:51.647449-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:51.647581-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:51.647639-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:51.647687-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:51.647902-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:51.647919-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:51.660036-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10041129 ioTS st: 10041129 ht: 138251.260950
default	20:23:51.669488-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:51.676640-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:51.680248-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:51.680282-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:51.711570-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:51.711783-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:51.712021-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:51.712193-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:51.712368-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:51.712393-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:51.712421-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:51.712555-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:51.712610-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:51.712640-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:51.712841-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:51.712855-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:53.210669-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876669 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:53.612924-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:23:53.732590-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876686 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:53.732970-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:23:53.831201-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:55.498789-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:55.499058-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:56.154412-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:56.159559-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:56.160370-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:56.160438-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:56.166887-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876686 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:56.167411-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876687 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:56.192578-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:56.193430-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:56.193456-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:56.193727-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:56.193759-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	20:23:56.193756-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:56.193828-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:56.194004-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:56.194062-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:56.194102-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:56.194307-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:56.194327-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:56.210180-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10141458 ioTS st: 10141458 ht: 138255.810950
error	20:23:56.228226-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:56.662151-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:56.662420-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:23:56.701620-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:23:56.710228-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:23:56.720572-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:23:56.720654-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:23:56.722712-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876687 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:56.724121-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876688 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:23:56.725143-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2cfc0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:23:56.725188-0500	VoiceOver	AudioConverter -> 0xbf2a2cfc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:23:56.725200-0500	VoiceOver	AudioConverter -> 0xbf2a2cfc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:23:56.763997-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:23:56.764437-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:23:56.764734-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:23:56.764853-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:23:56.765077-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:23:56.765108-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:23:56.765155-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:23:56.765331-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:23:56.765403-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:23:56.765444-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:23:56.765678-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:23:56.765696-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:23:56.780072-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10154027 ioTS st: 10154027 ht: 138256.380950
error	20:23:56.845525-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:23:59.898508-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:23:59.898822-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:23:59.982601-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98358
default	20:23:59.983108-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98358
default	20:24:02.131186-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876688 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:02.339376-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:02.556381-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:02.556663-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:02.592782-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:02.600935-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876689 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:02.601416-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:24:02.696772-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:24:05.729449-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:05.733325-0500	VoiceOver	No list of permitted front apps returned
default	20:24:05.775655-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 98362
default	20:24:05.776547-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 98362
default	20:24:05.846813-0500	VoiceOver	No list of permitted front apps returned
default	20:24:05.847995-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:05.848608-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:05.848771-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:06.027467-0500	VoiceOver	No list of permitted front apps returned
default	20:24:06.027703-0500	VoiceOver	No list of permitted front apps returned
default	20:24:06.030273-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:06.030508-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:06.038264-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:06.038414-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:24:06.041779-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2d3e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:06.041826-0500	VoiceOver	AudioConverter -> 0xbf2a2d3e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:06.041837-0500	VoiceOver	AudioConverter -> 0xbf2a2d3e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:06.054481-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:06.058763-0500	VoiceOver	No list of permitted front apps returned
default	20:24:06.061446-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:06.065366-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:06.065561-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:24:06.071810-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:06.080473-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:06.080535-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:06.093162-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474876689 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.094866-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876709 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.151979-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876709 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.152473-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876710 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.156964-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2cc60, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:06.157015-0500	VoiceOver	AudioConverter -> 0xbf2a2cc60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:06.157025-0500	VoiceOver	AudioConverter -> 0xbf2a2cc60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:06.196845-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:06.197732-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:06.198018-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:06.198287-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:06.198321-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:06.198358-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:06.198430-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:06.198833-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:06.198937-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:06.198991-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:06.199340-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:06.199368-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:06.210453-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10361959 ioTS st: 10361959 ht: 138265.810950
error	20:24:06.259087-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:06.263286-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:06.270778-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:06.270951-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:06.277657-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876710 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.278238-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876711 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:06.312742-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:06.313446-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:06.313816-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:06.314021-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:06.314246-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:06.314294-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:06.314347-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:06.315017-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:06.315109-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:06.315154-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:06.315458-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:06.315479-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:24:06.369246-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:06.595839-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:06.596676-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:07.452133-0500	VoiceOver	No list of permitted front apps returned
fault	20:24:07.461796-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:07.471071-0500	VoiceOver	No list of permitted front apps returned
default	20:24:07.553839-0500	VoiceOver	No list of permitted front apps returned
default	20:24:07.588721-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:07.588848-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:07.615595-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:07.615710-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:07.635886-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:07.642683-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:07.650296-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:07.650343-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:07.651676-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876711 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:07.652287-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876713 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:07.688106-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:07.688395-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:07.688657-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:07.688950-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:07.689125-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:07.689146-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:07.689176-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:07.689393-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:07.689455-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:07.689481-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:07.689722-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:07.689737-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:07.700076-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10394814 ioTS st: 10394814 ht: 138267.300950
error	20:24:07.797843-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:08.767488-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:08.767632-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
fault	20:24:08.770304-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:08.931819-0500	VoiceOver	No list of permitted front apps returned
default	20:24:08.968497-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:08.985394-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:08.985629-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:09.000778-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:09.010476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:09.010539-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:09.021549-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876713 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:09.022082-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876716 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:09.064589-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:09.065026-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:09.065356-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:09.065526-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:09.065720-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:09.065748-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:09.065783-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:09.065943-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:09.066014-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:09.066044-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:09.066243-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:09.066261-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:09.080108-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10425244 ioTS st: 10425244 ht: 138268.680950
error	20:24:09.144073-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:13.721429-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474876716 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:13.932708-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:14.252104-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876718 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:14.260898-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:24:14.421669-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:19.218561-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:19.219326-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:19.219495-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:19.247771-0500	VoiceOver	No list of permitted front apps returned
default	20:24:19.339634-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:19.340310-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:19.340348-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:19.352018-0500	VoiceOver	No list of permitted front apps returned
default	20:24:19.362977-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876718 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:19.426783-0500	VoiceOver	No list of permitted front apps returned
default	20:24:19.462404-0500	VoiceOver	No list of permitted front apps returned
default	20:24:19.521483-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2ce70, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:19.521505-0500	VoiceOver	AudioConverter -> 0xbf2a2ce70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:19.521521-0500	VoiceOver	AudioConverter -> 0xbf2a2ce70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:19.521853-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:19.545583-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876726 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:24:19.757664-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:21.044343-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.045129-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.045300-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.045511-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.045984-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.046104-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.047574-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.047214-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.047715-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.059238-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.060138-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.060298-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.111382-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.112220-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.112401-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.141161-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.142776-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.144135-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.144953-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.146792-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:21.150814-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:21.150904-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:21.159075-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.159123-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876726 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.159540-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876728 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.173940-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876728 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.174659-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876729 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.193456-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:21.194334-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:21.194530-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.194607-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:21.194637-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:21.194691-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:24:21.194840-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.194928-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:21.195004-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:21.195046-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:21.195297-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:21.195317-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:21.210053-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10692711 ioTS st: 10692711 ht: 138280.810950
error	20:24:21.211133-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:21.350333-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:21.350514-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:21.552537-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.552872-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.552937-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.567198-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.568672-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:21.570287-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:21.570430-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:21.571186-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876729 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.571547-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876731 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.587800-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:21.588155-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:21.588501-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.588526-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:21.588733-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:21.588759-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:21.588795-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:21.588938-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:21.589016-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:21.589046-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:21.589272-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:21.589286-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:21.600087-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10701311 ioTS st: 10701311 ht: 138281.200950
error	20:24:21.600878-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:21.747545-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.747883-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.747953-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.767141-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.768457-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:21.770262-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:21.770302-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:21.771634-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876731 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.773113-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876732 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.790108-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:21.790426-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:21.790801-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.790750-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:21.790967-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:21.790992-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:21.791023-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:21.791166-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:21.791225-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:21.791253-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:21.791480-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:21.791497-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:24:21.816801-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:21.924184-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:21.924695-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:21.924617-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:21.950541-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:21.952579-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:21.960383-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:21.960432-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:21.962341-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876732 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.965645-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:21.964301-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876733 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:21.980380-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:21.982959-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:21.983546-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.983655-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:21.983860-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:24:21.983836-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:21.983880-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:21.983952-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:21.984139-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:21.984231-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:21.984281-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:21.984554-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:21.984602-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:22.000078-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10710132 ioTS st: 10710132 ht: 138281.600950
error	20:24:22.005888-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:22.085472-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:22.085824-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:22.085886-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:22.099275-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:22.101150-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:22.110327-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:22.110374-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:22.111644-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876733 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:22.112185-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876734 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:22.128222-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:22.128884-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:22.129110-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:22.129136-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:22.129169-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:22.129494-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:22.129590-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:22.129654-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:22.129942-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:22.129980-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	20:24:22.128474-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:22.128690-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:22.241405-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:22.241882-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:22.241811-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:22.279314-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:22.279459-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:22.280303-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:22.280344-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:22.281197-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876734 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:22.281924-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876735 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:22.301553-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:22.301842-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:22.302084-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:22.302247-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:22.302407-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:22.302431-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:22.302469-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:22.302592-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:22.302654-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:22.302676-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:22.302859-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:22.302870-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:22.320084-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10717189 ioTS st: 10717189 ht: 138281.920950
error	20:24:22.322446-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:22.750766-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876735 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:22.963267-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:23.062838-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:23.063405-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:23.063535-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:23.074963-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:23.076770-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876738 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.077701-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:24:23.097640-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:23.213630-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:23.214092-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:23.214009-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:23.228413-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:23.233283-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:23.240377-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:23.240434-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:23.242458-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876738 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.244931-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876739 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.263015-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:23.263362-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:23.263643-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:23.263802-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:23.264067-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:23.264098-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:23.264137-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:23.264357-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:23.264439-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:23.264472-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:23.264811-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:23.264854-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:24:23.286043-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:23.527462-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:23.527961-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:23.528048-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:23.552316-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:23.553787-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:23.560426-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:23.560480-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:23.561570-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876739 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.562588-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876740 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.582896-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:23.583261-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:23.583616-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:23.583858-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:23.584158-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:23.584194-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:23.584242-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:23.584423-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:23.584505-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:23.584543-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:23.584882-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:23.584903-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:23.600056-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10745413 ioTS st: 10745413 ht: 138283.200950
error	20:24:23.603377-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:23.812576-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:23.813306-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:23.813456-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:23.830456-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:23.831969-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:23.840476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:23.840537-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:23.842919-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876740 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.843355-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876741 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:23.862588-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:23.863260-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:23.863699-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:23.863673-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:23.863995-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:23.864025-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:23.864072-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:23.864303-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:23.864396-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:23.864428-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:23.864778-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:23.864799-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:24.350563-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876741 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:24.563087-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:24.902621-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:24.907820-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876742 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:24.910389-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:25.109975-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:25.110140-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:24:25.348779-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:25.349221-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:25.349298-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:25.379899-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.382759-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:25.390331-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:25.390379-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:25.391310-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876742 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:25.392045-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876743 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:25.398417-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2df80, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:25.398436-0500	VoiceOver	AudioConverter -> 0xbf2a2df80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:25.398468-0500	VoiceOver	AudioConverter -> 0xbf2a2df80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:25.409343-0500	VoiceOver	No list of permitted front apps returned
default	20:24:25.409579-0500	VoiceOver	No list of permitted front apps returned
default	20:24:25.415363-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:25.415899-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:25.415987-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:25.416129-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:25.416188-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:25.416210-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:25.416240-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:25.416428-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:25.416486-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:25.416515-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:25.416743-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:25.416758-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:25.417618-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:25.417726-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:25.430125-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10785765 ioTS st: 10785765 ht: 138285.030950
error	20:24:25.433974-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:25.441097-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad63d0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:25.441118-0500	VoiceOver	AudioConverter -> 0xbf2ad63d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:25.441152-0500	VoiceOver	AudioConverter -> 0xbf2ad63d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:25.444639-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.444751-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.444809-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.444860-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.444915-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:25.451271-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:25.460352-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:25.460381-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:25.461827-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876743 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:25.462321-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876744 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:25.496176-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:25.496426-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:25.496661-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:25.496809-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:25.496989-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:25.497009-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:25.497042-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:25.497185-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:25.497239-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:25.497262-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:25.497546-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:25.497561-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:25.510117-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10787530 ioTS st: 10787530 ht: 138285.110950
default	20:24:25.515240-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:25.515566-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:25.603562-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:25.603960-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:25.604033-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:25.737524-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:25.740737-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:25.750511-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:25.750556-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:25.827400-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:25.827855-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:25.828298-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:25.828351-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:25.828577-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:25.828623-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:25.828669-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:25.828871-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:25.828954-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:25.828995-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:25.829297-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:25.829317-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:25.886907-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:25.964996-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:25.970290-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:25.970324-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:25.980421-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876745 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:25.981066-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876746 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:26.047295-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:26.047660-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.048022-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:26.048032-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.048294-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:26.048322-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:26.048367-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:26.048540-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:26.048609-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:26.048641-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:26.048899-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:26.048916-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:26.293687-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:26.294441-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:26.334433-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:26.341000-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:26.350655-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:26.350754-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:26.370500-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876746 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:26.371216-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876747 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:26.434428-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:26.434905-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.435271-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:26.435287-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.435574-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:26.435606-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:26.435651-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:26.435834-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:26.435902-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:26.435944-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:26.436412-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:26.436435-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:26.437114-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:26.437649-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:26.437745-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:26.450319-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10808259 ioTS st: 10808259 ht: 138286.050950
default	20:24:26.531167-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:26.540689-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:26.540761-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:26.592895-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:26.593354-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.593816-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:26.593894-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.594100-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:26.594135-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:26.594185-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:26.594392-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:26.594475-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:26.594515-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:26.594815-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:26.594835-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:26.610311-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10811788 ioTS st: 10811788 ht: 138286.210950
default	20:24:26.666652-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:26.780499-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:26.780586-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:26.790909-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876748 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:26.791359-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876749 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:26.863042-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:26.863564-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.863889-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:26.864135-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:24:26.864100-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:26.864168-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:26.864228-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:26.864460-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:26.864540-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:26.864588-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:26.864866-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:26.864886-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:26.880239-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10817742 ioTS st: 10817742 ht: 138286.480950
default	20:24:27.211127-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:27.211215-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
error	20:24:27.216938-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:27.262142-0500	VoiceOver	No list of permitted front apps returned
default	20:24:27.262408-0500	VoiceOver	No list of permitted front apps returned
default	20:24:27.301330-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:27.301599-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:27.341599-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:27.350716-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:27.350780-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:27.373461-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876749 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:27.373955-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876750 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:27.433126-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:27.433639-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:27.433945-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:27.434113-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:27.434360-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:27.434396-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:27.434457-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:27.434668-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:27.434746-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:27.434789-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:27.435082-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:27.435106-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:27.450253-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10830311 ioTS st: 10830311 ht: 138287.050950
error	20:24:27.472520-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:28.195915-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:28.198501-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:28.198134-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:28.250309-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:28.250432-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:28.253017-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874ed0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:28.253041-0500	VoiceOver	AudioConverter -> 0xbf2874ed0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:28.253053-0500	VoiceOver	AudioConverter -> 0xbf2874ed0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:28.256129-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:28.260279-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:28.260329-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:28.261535-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876750 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.261835-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876753 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.281733-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:28.281965-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:28.282191-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:28.282414-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:28.282603-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:28.282629-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:28.282656-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:28.282809-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:28.282871-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:28.282903-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:28.283106-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:28.283119-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:28.300081-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10849054 ioTS st: 10849054 ht: 138287.900950
error	20:24:28.307240-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:28.395675-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:28.396131-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:28.396230-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:28.444066-0500	VoiceOver	[0xbf0669a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:28.444181-0500	VoiceOver	[0xbf0669a40] invalidated after the last release of the connection object
default	20:24:28.450419-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:28.460339-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:28.460383-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:28.461931-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876753 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.462359-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876754 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.491111-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:28.491353-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:28.491602-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:28.491759-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:28.491947-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:28.491971-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:28.492003-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:28.492142-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:28.492202-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:28.492228-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:28.492430-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:28.492446-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:28.510108-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10853685 ioTS st: 10853685 ht: 138288.110950
error	20:24:28.516868-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:28.587284-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:28.587670-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:28.587744-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:28.638715-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:28.638839-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:28.644752-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:28.650335-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:28.650386-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:28.651781-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876754 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.652132-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876755 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:28.669188-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:28.669487-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:28.669756-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:28.669961-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:28.670201-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:28.670226-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:28.670264-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:28.670464-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:28.670537-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:28.670573-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:28.670840-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:28.670861-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:28.690076-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10857654 ioTS st: 10857654 ht: 138288.290950
error	20:24:28.694731-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:29.003962-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:29.004411-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:29.004503-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:29.059845-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:29.059984-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:29.066657-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:29.070322-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:29.070411-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:29.071676-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876755 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.072014-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876756 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.091305-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:29.091603-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:29.091856-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:29.091969-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:29.092133-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:29.092155-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:29.092186-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:29.092329-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:29.092386-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:29.092411-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:29.092592-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:29.092607-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:29.110110-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10866915 ioTS st: 10866915 ht: 138288.710950
error	20:24:29.115515-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:29.245819-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:29.246256-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:29.246335-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:29.282833-0500	VoiceOver	No list of permitted front apps returned
default	20:24:29.283019-0500	VoiceOver	No list of permitted front apps returned
default	20:24:29.316818-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:29.316941-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:29.343142-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.343267-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.343346-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.343408-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.343466-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.348274-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:29.350265-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:29.350297-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:29.351516-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876756 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.351798-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876757 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.383827-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:29.384119-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:29.384349-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:29.384488-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:29.384675-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:29.384699-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:29.384732-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:29.384871-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:29.384932-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:29.384962-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:29.385179-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:29.385191-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:29.400072-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10873310 ioTS st: 10873310 ht: 138289.000950
default	20:24:29.467345-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:29.467716-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:29.467777-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:29.513048-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.513436-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.514000-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.530291-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:29.530323-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:29.539431-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876758 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.595002-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:29.595294-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:29.595609-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:29.595630-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:29.595830-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:29.595851-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:29.595882-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:29.596031-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:29.596095-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:29.596120-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:29.596335-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:29.596350-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:29.610094-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10877941 ioTS st: 10877941 ht: 138289.210950
default	20:24:29.760683-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:29.770368-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:29.780349-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:29.780385-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:29.791946-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876758 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.792872-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876759 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:29.847862-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:29.848201-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:29.848480-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:29.848512-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:29.848715-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:29.848737-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:29.848766-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:29.848897-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:29.848953-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:29.848979-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:29.849189-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:29.849205-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:29.860084-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10883454 ioTS st: 10883454 ht: 138289.460950
default	20:24:29.909147-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:29.966121-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.966547-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:29.984913-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:29.990386-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:29.990422-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:30.999669-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876760 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:30.056246-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:30.056648-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:30.057068-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.057130-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:30.057662-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:30.057697-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:30.057745-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:30.057941-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:30.058021-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:30.058059-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:30.058362-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:30.058384-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:30.070220-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10888085 ioTS st: 10888085 ht: 138289.670950
default	20:24:30.137465-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:30.138206-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:30.230547-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:30.230595-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:30.302647-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:30.303153-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.303566-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:30.303654-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.303877-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:30.303908-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:30.303952-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:30.304140-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:30.304210-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:30.304249-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:30.304510-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:30.304527-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:30.320208-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10893598 ioTS st: 10893598 ht: 138289.920950
default	20:24:30.443669-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:30.450392-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:30.450434-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:30.517863-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:30.518399-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:30.518738-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.518783-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:30.519013-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:30.519042-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:30.519073-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:30.519234-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:30.519299-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:30.519340-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:30.519601-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:30.519618-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:30.530268-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10898229 ioTS st: 10898229 ht: 138290.130950
default	20:24:30.581760-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:30.581836-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:30.622433-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:30.622735-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:30.623056-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:30.633373-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:30.640270-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:30.640302-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:30.648994-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876762 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:30.649379-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876763 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:30.684560-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:30.684765-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:30.710818-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:30.711203-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:30.711565-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.711724-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:30.711963-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:30.711993-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:30.712044-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:30.712246-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:30.712327-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:30.712364-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:30.712656-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:30.712682-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:30.730218-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10902640 ioTS st: 10902640 ht: 138290.330950
default	20:24:30.860333-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:30.860367-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:30.935312-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:30.935666-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:30.935981-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:30.936033-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:30.936249-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:30.936276-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:30.936310-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:30.936458-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:30.936522-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:30.936554-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:30.936767-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:30.936784-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:30.950150-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10907492 ioTS st: 10907492 ht: 138290.550950
default	20:24:30.975775-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:30.975848-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:31.034692-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.035315-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.035698-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.036088-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.047175-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:31.050299-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.050329-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:31.116729-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:31.117111-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:31.117522-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.117645-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:31.117898-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:31.117929-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:31.117969-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:31.118151-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:31.118231-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:31.118271-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:31.118510-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:31.118525-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:31.130203-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10911461 ioTS st: 10911461 ht: 138290.730950
default	20:24:31.161556-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:31.162030-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:31.162111-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:31.217437-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.217925-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.258708-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:31.260370-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:31.260601-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:31.270282-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.270312-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:31.279223-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876765 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:31.280268-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876766 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:31.281332-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:31.338691-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:31.339164-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.339342-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:31.339521-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.339565-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:31.339591-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:31.339637-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:31.339797-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:31.339850-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:31.339884-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:31.340087-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:31.340105-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:31.343437-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:31.343805-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:31.343898-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:31.350128-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10916312 ioTS st: 10916312 ht: 138290.950950
default	20:24:31.393347-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.393749-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.410264-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.410290-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:31.416156-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876766 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:31.466681-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:31.467067-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:31.467468-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.467555-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:31.467797-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:31.467824-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:31.467863-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:31.468040-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:31.468116-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:31.468152-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:31.468404-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:31.468422-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:31.480108-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10919179 ioTS st: 10919179 ht: 138291.080950
default	20:24:31.586323-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.586630-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.587342-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.610414-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.610446-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:31.692958-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:31.693336-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:31.693806-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.693809-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:31.694037-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:31.694063-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:31.694112-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:31.694274-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:31.694349-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:31.694386-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:31.694633-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:31.694654-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:31.710310-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10924251 ioTS st: 10924251 ht: 138291.310950
default	20:24:31.714001-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:31.714637-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:31.714762-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:31.768292-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.768838-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.769368-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.769925-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.805262-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:31.810379-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:31.820247-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.820275-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:31.826992-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876768 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:31.827786-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876769 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:31.878155-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:31.878490-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:31.878771-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:31.878825-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:31.879009-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:31.879034-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:31.879074-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:31.879213-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:31.879264-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:31.879292-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:31.879503-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:31.879518-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:31.890069-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10928221 ioTS st: 10928221 ht: 138291.490950
default	20:24:31.893728-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:31.894176-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:31.894243-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:31.944400-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.944849-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.945113-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.945403-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:31.960233-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:31.960259-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
error	20:24:32.005119-0500	VoiceOver	     AudioQueueObject.cpp:5805  buffersCreatedAndDestroyed: aq@0xbefc3c000: error allocating buffer
error	20:24:32.011003-0500	VoiceOver	     AudioQueueObject.cpp:5818  buffersCreatedAndDestroyed: aq@0xbefc3c000: invalid buffer ID
default	20:24:32.016928-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:32.017261-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:32.017601-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.017724-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:32.017951-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:32.017978-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:32.018011-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:32.018167-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:32.018234-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:32.018265-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:32.018487-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:32.018511-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:32.030122-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10931309 ioTS st: 10931309 ht: 138291.630950
default	20:24:32.102529-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:32.165672-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.166043-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.166397-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.166768-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.167144-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.179708-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:32.203555-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:32.210474-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:32.220339-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:32.220376-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:32.229724-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876770 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.230204-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876772 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.231146-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:32.280569-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:32.280863-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:32.281176-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.281220-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:32.281407-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:32.281429-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:32.281454-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:32.281586-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:32.281642-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:32.281670-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:32.281872-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:32.281886-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:32.300060-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10937263 ioTS st: 10937263 ht: 138291.900950
default	20:24:32.309427-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:32.309807-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:32.309880-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:32.380285-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:32.380314-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:32.388102-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876772 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.437789-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:32.438088-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:32.438450-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.438519-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:32.438731-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:32.438755-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:32.438785-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:32.438939-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:32.439007-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:32.439035-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:32.439254-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:32.439270-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:32.450115-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10940571 ioTS st: 10940571 ht: 138292.050950
default	20:24:32.528085-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:32.610438-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:32.610476-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:32.622457-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876773 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.623785-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876774 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.676731-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:32.677194-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.677566-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:32.677608-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.677823-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:32.677849-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:32.677884-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:32.678062-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:32.678133-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:32.678165-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:32.678428-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:32.678447-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:32.788975-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.789514-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:32.809308-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876774 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.809668-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876775 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:32.857871-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:32.858261-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.858684-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:32.858639-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:32.858927-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:32.858959-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:32.858994-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:32.859174-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:32.859256-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:32.859292-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:32.859564-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:32.859582-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:24:32.924379-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:32.943384-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:32.943962-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:32.944037-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:32.994369-0500	VoiceOver	No list of permitted front apps returned
default	20:24:32.994885-0500	VoiceOver	No list of permitted front apps returned
default	20:24:32.997971-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:32.998083-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:33.001143-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc0390, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:33.001172-0500	VoiceOver	AudioConverter -> 0xbf2bc0390: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:33.001182-0500	VoiceOver	AudioConverter -> 0xbf2bc0390: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:33.005213-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:33.010164-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:33.010540-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:33.010581-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:33.014925-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc0090, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:33.015072-0500	VoiceOver	AudioConverter -> 0xbf2bc0090: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:33.015103-0500	VoiceOver	AudioConverter -> 0xbf2bc0090: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:33.017952-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876775 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:33.018821-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876776 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:33.041374-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:33.041594-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:33.052680-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:33.052942-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:33.053194-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:33.053317-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:33.053491-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:33.053509-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:33.053534-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:33.053667-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:33.053715-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:33.053741-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:33.053955-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:33.053970-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:33.070096-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10954243 ioTS st: 10954243 ht: 138292.670950
error	20:24:33.109307-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:33.661365-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:33.662162-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:33.662321-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:33.681827-0500	VoiceOver	No list of permitted front apps returned
default	20:24:33.783128-0500	VoiceOver	No list of permitted front apps returned
default	20:24:33.786812-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:33.787491-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:33.787611-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:33.798964-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:33.799220-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:33.808118-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:33.808305-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:33.826241-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:33.830661-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:33.830775-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:33.834523-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876776 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:33.835036-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876777 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:33.862945-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:33.863439-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:33.863730-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:33.863843-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:33.864038-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:33.864067-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:33.864114-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:33.864283-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:33.864345-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:33.864381-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:33.864584-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:33.864603-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:33.880099-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 10972104 ioTS st: 10972104 ht: 138293.480950
error	20:24:33.943295-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:34.898412-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:34.899446-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:34.899633-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:34.912472-0500	VoiceOver	No list of permitted front apps returned
default	20:24:34.978621-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:34.980386-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:34.980438-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:35.042285-0500	VoiceOver	No list of permitted front apps returned
default	20:24:35.062973-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:35.063425-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:35.063498-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:35.071105-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:35.071261-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:35.086536-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:35.086741-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:35.092561-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874d20, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:35.092582-0500	VoiceOver	AudioConverter -> 0xbf2874d20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:35.092590-0500	VoiceOver	AudioConverter -> 0xbf2874d20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:35.092758-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:35.101645-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:35.106142-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2a2cf30, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:35.106163-0500	VoiceOver	AudioConverter -> 0xbf2a2cf30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:35.106169-0500	VoiceOver	AudioConverter -> 0xbf2a2cf30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:35.107887-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876787 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:35.108310-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:35.144608-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:35.145025-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:35.145267-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:35.145266-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:35.145668-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:35.145697-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:35.145744-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:35.145903-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:35.145967-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:35.146033-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:35.146275-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:35.146291-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:24:35.243046-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:35.804784-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:35.805021-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:36.566059-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:36.566931-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:36.567054-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:36.642740-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:36.650895-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:36.651040-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:36.661950-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876787 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:36.663687-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876791 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:36.697093-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:36.697995-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:36.698241-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:24:36.698230-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:36.698271-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:36.698318-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:36.698496-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
fault	20:24:36.698498-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:36.698568-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:36.698611-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:36.698842-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:36.698859-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:36.710231-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11034506 ioTS st: 11034506 ht: 138296.310950
error	20:24:36.725577-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:36.899537-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:36.899828-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:37.318963-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:37.319211-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:37.811525-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:37.812522-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:37.812704-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:37.861458-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876791 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:38.072206-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:38.293725-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876792 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:38.294228-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:24:38.356280-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:39.547121-0500	VoiceOver	[0xbf066ad00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:39.547280-0500	VoiceOver	[0xbf066ad00] invalidated after the last release of the connection object
default	20:24:39.777076-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:24:39.777129-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:24:39.779200-0500	runningboardd	Invalidating assertion 400-98203-144233 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
fault	20:24:39.779917-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:39.777137-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:24:39.777754-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:39.778425-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:39.778435-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:24:39.797759-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:24:39.797777-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:24:39.798624-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:39.798648-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:24:39.798655-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:24:39.802802-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:39.802835-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:24:39.802843-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:24:39.802884-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:39.802901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:24:39.802908-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:24:39.803014-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:39.804900-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:24:39.804929-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:24:39.804935-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:24:39.807990-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144317 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:39.808176-0500	runningboardd	Assertion 400-98203-144317 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:24:39.806983-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:24:39.807251-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:39.807467-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
error	20:24:39.807481-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:39.807490-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:24:39.815345-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:39.840588-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:39.841140-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:24:39.841227-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc1350, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:24:39.841289-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:24:39.841420-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:39.844723-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:24:39.844875-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7655 called from <private>
default	20:24:39.844778-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:39.858612-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:39.858959-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:39.859344-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xbefc3c000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	20:24:39.859977-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:39.913726-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:40.185914-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876792 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:40.389254-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:40.547473-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98380
fault	20:24:40.700057-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:40.700473-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:40.701260-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:40.701845-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:40.710587-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876976 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:40.733891-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:24:40.859396-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:41.196769-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:41.197118-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:43.449590-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:43.451782-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:43.795337-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:43.796221-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:45.126395-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474876976 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:45.339241-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
fault	20:24:45.579699-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:45.578217-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:45.579135-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:24:45.579210-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:24:45.579216-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:24:45.582231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:45.582320-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:24:45.583112-0500	runningboardd	Invalidating assertion 400-98203-144320 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:24:45.586122-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:45.584002-0500	runningboardd	Invalidating assertion 400-332-144234 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.powerd>:332]
default	20:24:45.599292-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:24:45.599327-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:24:45.599484-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:45.599509-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:24:45.599519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:24:45.599658-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:24:45.599683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:24:45.599694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:24:45.603219-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:45.603569-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:24:45.603586-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:24:45.603604-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:24:45.603614-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:24:45.604872-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:45.607122-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144335 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:45.608112-0500	runningboardd	Assertion 400-98203-144335 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:24:45.604902-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:24:45.605458-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:45.610380-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:45.610445-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
error	20:24:45.610496-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:45.610548-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:24:45.610641-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:24:45.614401-0500	runningboardd	Invalidating assertion 400-98203-144335 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:24:45.610675-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:24:45.611754-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:45.612003-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:24:45.612035-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:24:45.614243-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:45.614316-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:24:45.614645-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:24:45.617259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:24:45.617297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:24:45.617315-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:24:45.617326-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:24:45.617336-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:24:45.619071-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144337 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:45.619379-0500	runningboardd	Assertion 400-98203-144337 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
error	20:24:45.618484-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:45.618515-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7655 called from <private>
default	20:24:45.618556-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:24:45.618585-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:24:45.621232-0500	runningboardd	Invalidating assertion 400-98203-144337 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:24:45.688915-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:24:45.688937-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:24:45.688961-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:24:45.689016-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:24:45.689032-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:24:45.692385-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:24:46.225519-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144343 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:46.225692-0500	runningboardd	Assertion 400-332-144343 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:24:46.226694-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:24:46.226766-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:24:46.226845-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:24:46.226979-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:24:46.227066-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:24:46.233047-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:24:46.239219-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	20:24:46.276401-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:24:46.276490-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7655 called from <private>
default	20:24:46.279444-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:24:46.279460-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
fault	20:24:46.277621-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:46.282995-0500	runningboardd	Invalidating assertion 400-98203-144339 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:24:46.283447-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144345 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:46.283559-0500	runningboardd	Assertion 400-98203-144345 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:24:46.285533-0500	runningboardd	Invalidating assertion 400-332-144343 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.powerd>:332]
default	20:24:46.287132-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144348 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:46.287246-0500	runningboardd	Assertion 400-332-144348 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:24:46.281030-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28768e0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.281091-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:46.849828-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:24:46.891637-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:24:46.891793-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:46.892319-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:46.892520-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:46.892533-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:46.892541-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:46.893184-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:46.892796-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104e25b10) Device ID: 85 (Input:No | Output:Yes): true
default	20:24:46.892808-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104e25b10)
default	20:24:46.892894-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.892919-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:24:46.892957-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.893001-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:24:46.893049-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:24:46.893559-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2875aa0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.893593-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:46.893712-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:46.894083-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:46.894231-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:46.894248-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:46.894264-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:46.894285-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:24:46.894295-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:24:46.895076-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28768e0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.895539-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:46.895803-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:46.896236-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:46.896575-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:46.896784-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:46.897056-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:46.897094-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:46.897524-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xbefc3c000:
default	20:24:46.897589-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	20:24:46.897598-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	20:24:46.897615-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	20:24:46.897640-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	20:24:46.897664-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	20:24:46.897910-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:46.897944-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:46.898189-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xbefc3c000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	20:24:46.898545-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:46.898823-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:46.899075-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:46.899313-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:46.899566-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:46.899600-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:46.899643-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:46.899816-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:46.899893-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:46.899940-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:46.900233-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:46.900254-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:46.903800-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:46.922415-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:46.932806-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:46.932889-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:46.945652-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:24:46.946516-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:24:48.933248-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:48.934392-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:48.934592-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:49.017754-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:49.031867-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:49.031874-0500	VoiceOver	aqmeio@0xbf0a97618 Stop id=85
default	20:24:49.032180-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:49.036024-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:49.036442-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:49.036381-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:49.066510-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877155 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:49.074332-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:49.087482-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:400-98203-144351 target:98209 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown WantsForegroundResourcePriority )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	20:24:49.087567-0500	runningboardd	Assertion 400-98203-144351 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]) will be created as active
default	20:24:49.088027-0500	VoiceOver	Aquired asertion <BKSProcessAssertion: 0xbefd19ef0> for running extension with pid 98209
default	20:24:49.088310-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin reference count incremented to 2, and ready for host.
default	20:24:49.089122-0500	VoiceOver	[0xbf0669a40] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:24:49.089293-0500	VoiceOver	[0xbf0d11800] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service
default	20:24:49.089559-0500	VoiceOver	[0xbf0669a40] Connection returned listener port: 0x3e1e3
default	20:24:49.091433-0500	VoiceOver	[0xbf0d12400] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xbf0669a40.peer[98209].0xbf0d12400
default	20:24:49.092406-0500	VoiceOver	[0xbf066ad00] activating connection: mach=false listener=false peer=false name=com.apple.audio.AUCrashHandlerService
default	20:24:49.096489-0500	VoiceOver	[0xbf066ad00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	20:24:49.096522-0500	VoiceOver	        AUCrashHandler.mm:126   invalidated
default	20:24:49.100950-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:49.102864-0500	VoiceOver	   AUOOPRenderPipePool.mm:167   Host obtained render pipe 402264251
default	20:24:49.280143-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:49.304157-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:49.304410-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:24:49.392266-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:400-98209-144352 target:98209 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	20:24:49.392411-0500	runningboardd	Assertion 400-98209-144352 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]) will be created as inactive as start-time-defining assertions exist
default	20:24:49.403589-0500	runningboardd	Invalidating assertion 400-98209-144352 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]
default	20:24:49.430365-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877155 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:49.436469-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877156 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:49.437541-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:49.453572-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:49.454183-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:49.454273-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:49.454494-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:49.454520-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:49.454561-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:24:49.454576-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:49.454756-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:49.454827-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:49.454879-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:49.455116-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:49.455135-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:49.471856-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11315903 ioTS st: 11315903 ht: 138309.072677
error	20:24:49.472279-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:49.782521-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877156 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:49.996857-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:50.370717-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:50.371028-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:24:50.382791-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:50.392563-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:50.392652-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:50.809808-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:50.810048-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:24:51.408694-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:51.409506-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:51.409615-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:51.487504-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877158 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:51.496078-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:51.514924-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:51.516052-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:51.516372-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:51.516514-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:51.516561-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:51.516609-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:24:51.516818-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:51.516927-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:51.517043-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:51.517096-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:51.517509-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:51.517533-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:51.531974-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11361326 ioTS st: 11361326 ht: 138311.132677
default	20:24:52.760910-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:52.761764-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:52.761929-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:53.091792-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:53.092580-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:53.092716-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:53.140391-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:53.142640-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:53.152221-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:53.152281-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:53.154347-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877158 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:53.155401-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877163 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:53.161789-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:53.162116-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:53.173773-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:24:53.174768-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:53.175031-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:53.175110-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:53.175200-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:53.175518-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:53.175656-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:53.175803-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:53.176208-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:53.176273-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	20:24:53.174539-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:53.191787-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11397929 ioTS st: 11397929 ht: 138312.792677
fault	20:24:53.175103-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
error	20:24:53.196980-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:53.353897-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:53.354259-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:53.354330-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:53.404114-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:53.405672-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:53.412029-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:53.412084-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:53.412961-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877163 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:53.413671-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877164 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:53.427321-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:53.427594-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:53.427867-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:53.427968-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:53.428158-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:53.428180-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:53.428215-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:53.428365-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:53.428426-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:53.428457-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:53.428674-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:53.428690-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:53.441991-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11403442 ioTS st: 11403442 ht: 138313.042677
error	20:24:53.442327-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:53.653080-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:53.653207-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:53.852921-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877164 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:54.066430-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:54.082154-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:54.082425-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:24:54.452397-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:54.460639-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:54.461489-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:54.461641-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:54.462349-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:54.462421-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:54.534791-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:54.537205-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877166 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:54.541762-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:54.553697-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:54.554009-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:54.554363-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:54.554578-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:54.554601-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	20:24:54.554267-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:54.554686-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:54.554881-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:54.554949-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:54.554977-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:54.555285-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:54.555301-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:54.571769-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11428359 ioTS st: 11428359 ht: 138314.172677
error	20:24:54.577867-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:54.922513-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877166 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:54.936858-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:54.937207-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:54.937282-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:54.981484-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:54.983540-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877167 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	20:24:55.010204-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:55.332739-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877167 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:55.546142-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:55.733767-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:55.733892-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:55.932272-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:55.942121-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:55.942183-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:56.136915-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:56.141926-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877168 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:56.142265-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:56.167701-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:56.168456-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:56.168807-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:56.168792-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:56.169167-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:56.169198-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:56.169244-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:56.169473-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:56.169569-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:56.169606-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:56.169962-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:56.169987-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:56.181871-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11463860 ioTS st: 11463860 ht: 138315.782677
error	20:24:56.189433-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:56.321120-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:56.321294-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:24:56.613668-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877168 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:56.757144-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:56.757649-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:56.824564-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:24:57.212260-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:57.222090-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:57.222150-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:57.684088-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:57.684961-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:57.685117-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:57.697835-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:57.704135-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877170 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:57.704809-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876a00, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:57.704914-0500	VoiceOver	AudioConverter -> 0xbf2876a00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:57.704930-0500	VoiceOver	AudioConverter -> 0xbf2876a00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:57.705178-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:57.705879-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:57.706172-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:24:57.723767-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:57.725264-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:57.725136-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:57.725425-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:57.725466-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:57.725583-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:57.725934-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
fault	20:24:57.725919-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:57.726028-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:57.726145-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:57.726604-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:57.726656-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:57.742377-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11498258 ioTS st: 11498258 ht: 138317.342677
error	20:24:57.752136-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:57.828591-0500	VoiceOver	No list of permitted front apps returned
default	20:24:57.828938-0500	VoiceOver	No list of permitted front apps returned
default	20:24:57.846040-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:24:57.846281-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:24:57.883413-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874330, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:24:57.883454-0500	VoiceOver	AudioConverter -> 0xbf2874330: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:57.883469-0500	VoiceOver	AudioConverter -> 0xbf2874330: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:24:57.891376-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:57.891599-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:57.898509-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:57.902446-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:57.902520-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:57.904026-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877170 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:57.904613-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877171 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:57.937827-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:57.938358-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:24:57.938916-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:57.939011-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:24:57.939310-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:57.939348-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:57.939410-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:57.939678-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:57.939765-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:57.939817-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:57.940130-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:57.940155-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:57.952131-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11502889 ioTS st: 11502889 ht: 138317.552677
error	20:24:58.064742-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:24:58.585680-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:24:58.586426-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:24:58.586555-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:24:58.671232-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:58.671452-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:24:58.679013-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:24:58.682400-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:24:58.682508-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:24:58.692689-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877171 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:58.693625-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877172 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:24:58.730978-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:24:58.731487-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:58.731740-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:24:58.731798-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:24:58.731961-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:24:58.731990-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:24:58.732032-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:24:58.732192-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:24:58.732253-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:24:58.732287-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:58.732693-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:58.732709-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:24:58.751998-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11520530 ioTS st: 11520530 ht: 138318.352677
error	20:24:58.806847-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:00.144211-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:00.144787-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:00.144896-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:00.232526-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.232785-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.232932-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.233062-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.233191-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.243031-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:00.252716-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:00.252826-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:00.257213-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877172 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:00.259447-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877173 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:00.294682-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:00.295758-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:00.295977-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:25:00.296107-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:00.296216-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:00.296250-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:00.296297-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:00.296466-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:00.296526-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:00.296569-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:00.296798-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:00.296818-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:00.311878-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11554928 ioTS st: 11554928 ht: 138319.912677
default	20:25:00.362934-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:00.363442-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:00.363513-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:00.423320-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.423636-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.423930-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.424273-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.424613-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:00.442037-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:00.442061-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:00.500632-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:00.500905-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:00.501153-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:00.501267-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:00.501439-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:00.501460-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:00.501492-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:00.501619-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:00.501677-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:00.501702-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:00.501893-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:00.501908-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:00.563925-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:00.564363-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:00.564435-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:00.663352-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:25:00.664663-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:00.672312-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:00.682082-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:00.682118-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:00.694412-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877174 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:00.695552-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877175 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:00.695825-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:25:00.749722-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:00.750013-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:00.750386-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:00.750523-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:00.750742-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:00.750770-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:00.750799-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:00.750957-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:00.751030-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:00.751060-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:00.751318-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:00.751342-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:00.761885-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11564852 ioTS st: 11564852 ht: 138320.362677
error	20:25:00.962423-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:01.028604-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:01.029464-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:01.029545-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:01.088310-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.088423-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.088484-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.088534-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.088582-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.093480-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:01.102252-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:01.102289-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:01.119013-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877175 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:01.120038-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877176 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:01.167617-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:01.167871-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:01.168091-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:01.168247-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:01.168406-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:01.168427-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:01.168452-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:01.168582-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:01.168636-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:01.168659-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:01.168834-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:01.168848-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:01.181873-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11574113 ioTS st: 11574113 ht: 138320.782677
error	20:25:01.367075-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:01.745743-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:01.746476-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:01.746675-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:01.826685-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.826878-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.826967-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.827048-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.827227-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:01.836697-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:01.842603-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:01.842669-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:01.872472-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877176 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:01.873522-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877177 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:01.927206-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:01.927529-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:01.927757-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:01.927881-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:01.928045-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:01.928067-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:01.928096-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:01.928227-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:01.928284-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:01.928314-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:01.928498-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:01.928513-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:01.932890-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:01.933454-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:01.933536-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:01.941981-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11590871 ioTS st: 11590871 ht: 138321.542677
default	20:25:02.012012-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:02.012033-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:02.018114-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877177 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.018769-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877178 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.055326-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:02.055598-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:02.055857-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:02.055974-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:02.056134-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:02.056155-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:02.056180-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:02.056313-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:02.056365-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:02.056391-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:02.056600-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:02.056612-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:02.071875-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11593738 ioTS st: 11593738 ht: 138321.672677
error	20:25:02.113423-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:02.141602-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:02.142065-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:02.142136-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:02.204844-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:02.204941-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:02.208064-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:02.212244-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:02.212279-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:02.218255-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877178 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.219080-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877179 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.257365-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:02.257745-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:02.258047-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:02.258126-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:02.258330-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:02.258356-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:02.258393-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:02.258538-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:02.258600-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:02.258634-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:02.258866-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:02.258882-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:02.271964-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11598148 ioTS st: 11598148 ht: 138321.872677
error	20:25:02.324426-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:02.335504-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:02.336127-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:02.336220-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:02.398363-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:02.398469-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:02.402281-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:02.412116-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:02.412146-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:02.419516-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877179 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.420447-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877180 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:02.459140-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:02.459470-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:02.459749-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:02.459820-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:02.460026-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:02.460052-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:02.460088-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:02.460244-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:02.460313-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:02.460349-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:02.460571-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:02.460587-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:02.471863-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11602558 ioTS st: 11602558 ht: 138322.072677
error	20:25:02.515266-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:04.857472-0500	VoiceOver	No list of permitted front apps returned
fault	20:25:04.883750-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:04.934560-0500	VoiceOver	No list of permitted front apps returned
default	20:25:05.036369-0500	VoiceOver	No list of permitted front apps returned
default	20:25:05.563086-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:05.572341-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:05.572446-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:05.575700-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474877180 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:05.579031-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877182 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:05.641083-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:05.641659-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:05.642205-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:25:05.642193-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:05.642569-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:05.642611-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:05.642659-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:05.642935-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:05.643042-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:05.643091-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:05.643501-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:05.643527-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:05.644131-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:05.718846-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:05.918312-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:05.918773-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
error	20:25:05.959995-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:06.008378-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98393
fault	20:25:06.605803-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:06.610183-0500	VoiceOver	No list of permitted front apps returned
default	20:25:06.711508-0500	VoiceOver	No list of permitted front apps returned
default	20:25:06.731571-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:06.732218-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:25:06.748816-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:06.749170-0500	VoiceOver	[0xbf066b340] invalidated after the last release of the connection object
default	20:25:06.902882-0500	VoiceOver	No list of permitted front apps returned
default	20:25:06.905296-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6e20, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:06.905323-0500	VoiceOver	AudioConverter -> 0xbf2ad6e20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:06.905333-0500	VoiceOver	AudioConverter -> 0xbf2ad6e20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:06.913628-0500	VoiceOver	No list of permitted front apps returned
default	20:25:06.921093-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:06.921560-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:06.921634-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:06.951055-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:06.951250-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:06.969216-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:06.969357-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:25:06.975461-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad47e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:06.975501-0500	VoiceOver	AudioConverter -> 0xbf2ad47e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:06.975512-0500	VoiceOver	AudioConverter -> 0xbf2ad47e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:06.995229-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:06.995446-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:25:07.000204-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:07.002216-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:07.002266-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:07.011601-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877182 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:07.012422-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877183 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:07.079899-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:25:07.081069-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:07.081398-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:07.081510-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:07.081688-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:07.082135-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:07.082310-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:07.082443-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:07.083004-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:07.083095-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	20:25:07.080455-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:07.081135-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:07.101948-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11704650 ioTS st: 11704650 ht: 138326.702677
error	20:25:07.336883-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:07.929130-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6d00, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:07.929188-0500	VoiceOver	AudioConverter -> 0xbf2ad6d00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:07.929203-0500	VoiceOver	AudioConverter -> 0xbf2ad6d00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:07.941961-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:07.952483-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:07.952584-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:07.972446-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877183 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:07.973174-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877184 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:07.993819-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877184 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:07.994297-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877185 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:08.031745-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:08.032011-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:08.032243-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:08.032370-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:08.032538-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:08.032562-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:08.032593-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:08.032761-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:08.032819-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:08.032845-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:08.033067-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:08.033083-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:08.051884-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11725598 ioTS st: 11725598 ht: 138327.652677
error	20:25:08.088924-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:08.385340-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:08.392466-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:08.392544-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:08.398106-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877185 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:08.399404-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877186 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:08.425825-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:08.426114-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:08.426352-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:08.426523-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:08.426687-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:08.426712-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:08.426745-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:08.426882-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:08.426928-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:08.426959-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:08.427169-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:08.427182-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:08.441939-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11734198 ioTS st: 11734198 ht: 138328.042677
error	20:25:08.465576-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:08.707221-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6b50, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:08.707266-0500	VoiceOver	AudioConverter -> 0xbf2ad6b50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:08.707288-0500	VoiceOver	AudioConverter -> 0xbf2ad6b50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:08.899554-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:08.902343-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:08.902405-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:08.906676-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877186 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:08.907280-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877187 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:08.933590-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:08.934056-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:08.934350-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:08.934473-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:08.934658-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:08.934684-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:08.934722-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:08.934881-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:08.934940-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:08.934976-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:08.935352-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:08.935380-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:08.951956-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11745444 ioTS st: 11745444 ht: 138328.552677
error	20:25:08.981385-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:09.296860-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98398
default	20:25:10.678337-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:10.679127-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:10.679282-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:10.679553-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:10.679934-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:10.680017-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:10.932898-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:10.933902-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:10.933749-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:11.043519-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877187 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:11.387847-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:25:11.563466-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877190 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:11.571142-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	20:25:11.578866-0500	VoiceOver	No list of permitted front apps returned
default	20:25:11.671149-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:11.671283-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:25:11.679889-0500	VoiceOver	No list of permitted front apps returned
default	20:25:11.710057-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:11.712179-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:11.722076-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:11.722105-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:11.729705-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877190 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:11.730113-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877191 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:11.772722-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:11.773271-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:11.773319-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:11.773509-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	20:25:11.773514-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:11.773529-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:11.773555-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:11.773699-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:11.773755-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:11.773782-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:11.773976-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:11.773991-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:11.791887-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11808067 ioTS st: 11808067 ht: 138331.392677
error	20:25:11.808943-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:12.562663-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:12.563256-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:12.563370-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:12.598176-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:12.598401-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:25:12.604305-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:12.612382-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:12.612463-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:12.614963-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877191 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:12.615519-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877192 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:12.646367-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:12.646752-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:12.647061-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:12.647110-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:12.647363-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:12.647388-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:12.647427-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:12.647566-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:12.647614-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:12.647644-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:12.647830-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:12.647845-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:12.661923-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11827251 ioTS st: 11827251 ht: 138332.262677
error	20:25:12.684936-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:12.794307-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:12.794867-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:12.794959-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:12.815311-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:12.815474-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:25:12.820529-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:12.822397-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:12.822473-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:12.825176-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877192 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:12.826396-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877193 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:12.853576-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:12.853929-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:12.854214-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:12.854283-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:12.854491-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:12.854515-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:12.854546-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:12.854677-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:12.854746-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:12.854780-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:12.855007-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:12.855021-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:12.872020-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11831882 ioTS st: 11831882 ht: 138332.472677
error	20:25:12.897978-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:12.966058-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:12.966662-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:12.966742-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:12.987257-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:12.987425-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:12.991534-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:12.992227-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:12.992264-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:12.995493-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877193 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:12.996202-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877194 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.031733-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:13.031971-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:13.032186-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:13.032372-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:13.032556-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:13.032577-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:13.032603-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:13.032742-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:13.032809-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:13.032844-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:13.033082-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:13.033097-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:13.051878-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11835851 ioTS st: 11835851 ht: 138332.652677
error	20:25:13.076277-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:13.107522-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:13.107892-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:13.107950-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:13.129692-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:13.129806-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:25:13.133266-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:13.142091-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:13.142118-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:13.145454-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877194 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.145785-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877195 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.181780-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:13.182035-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:13.182265-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:13.182377-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:13.182543-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:13.182564-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:13.182593-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:13.182723-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:13.182775-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:13.182800-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:13.183005-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:13.183021-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:13.201881-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11839159 ioTS st: 11839159 ht: 138332.802677
error	20:25:13.220206-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:13.258933-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:13.259336-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:13.259404-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:13.279961-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:13.280070-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:25:13.282170-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:13.292078-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:13.292112-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:13.295078-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877195 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.295747-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877196 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.325325-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:13.325650-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:13.325915-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:13.326045-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:13.326209-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:13.326234-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:13.326266-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:13.326409-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:13.326457-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:13.326483-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:13.326689-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:13.326703-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:13.341947-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 11842246 ioTS st: 11842246 ht: 138332.942677
error	20:25:13.344624-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:13.732711-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877196 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:13.947048-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	20:25:14.253693-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877197 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:14.258953-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	20:25:14.389858-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:19.799205-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:19.868223-0500	runningboardd	Invalidating assertion 400-98203-144345 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:19.866978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
fault	20:25:19.868733-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:19.867818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:19.867827-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:25:19.870207-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:25:19.870234-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:25:19.870275-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:25:19.884758-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:25:19.891165-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:25:19.891201-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:25:19.891208-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:25:19.894610-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:19.894629-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:25:19.895041-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:19.896337-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:19.896544-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:25:19.896574-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:19.898200-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:19.898255-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:19.906888-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:19.906912-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:25:19.907028-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:19.909809-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:19.910104-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:25:19.910115-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:19.911180-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:19.911195-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:25:19.911268-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:25:19.911324-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:25:19.911401-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:19.911442-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:25:19.911490-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:25:19.911521-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:25:19.911644-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:19.911709-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:19.947304-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:19.947339-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
fault	20:25:20.533509-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:20.534061-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:20.535306-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:20.535968-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:21.924254-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:21.924570-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:21.962771-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:21.963527-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:21.963430-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:21.965536-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:21.965742-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:25:22.312602-0500	VoiceOver	No list of permitted front apps returned
default	20:25:22.414414-0500	VoiceOver	No list of permitted front apps returned
default	20:25:22.417536-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:22.418257-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:22.418370-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:22.428628-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:22.428867-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:25:22.445728-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:22.445976-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:25:22.446665-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6ca0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:22.446703-0500	VoiceOver	AudioConverter -> 0xbf2ad6ca0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:22.446717-0500	VoiceOver	AudioConverter -> 0xbf2ad6ca0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:22.460481-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2bc1f50, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:22.460513-0500	VoiceOver	AudioConverter -> 0xbf2bc1f50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:22.460542-0500	VoiceOver	AudioConverter -> 0xbf2bc1f50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:22.466206-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:22.474430-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:22.474488-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:22.475914-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:08  id:21474877197 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:22.476363-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877394 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:22.512542-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:25:22.513183-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:25:22.513155-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:22.513385-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:22.513406-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:22.513439-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	20:25:22.513464-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:22.513557-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:22.513638-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:22.513663-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:22.513870-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:22.513885-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:22.534070-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12045154 ioTS st: 12045154 ht: 138342.144861
error	20:25:22.584422-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:24.048707-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.050266-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7656)
default	20:25:24.050301-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7656 called from <private>
default	20:25:24.050308-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7656 called from <private>
default	20:25:24.050462-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:24.050875-0500	runningboardd	Invalidating assertion 400-98203-144486 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:24.050518-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:25:24.051218-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
fault	20:25:24.052687-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:24.068624-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:24.068661-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:25:24.069477-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7656)
default	20:25:24.069505-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7656 called from <private>
default	20:25:24.069513-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7656 called from <private>
default	20:25:24.070913-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.070956-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7655 called from <private>
default	20:25:24.070967-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7655 called from <private>
default	20:25:24.072063-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:24.072089-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:24.072103-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7655 called from <private>
default	20:25:24.072391-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7655 called from <private>
default	20:25:24.076742-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144498 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:24.076941-0500	runningboardd	Assertion 400-98203-144498 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:24.072506-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:25:24.072635-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:24.073276-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:25:24.074450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.088542-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:24.088629-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
error	20:25:24.088649-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:24.088661-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:24.088774-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.089010-0500	runningboardd	Invalidating assertion 400-98203-144498 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:24.090492-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:24.090522-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:24.091641-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144499 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:24.091751-0500	runningboardd	Assertion 400-98203-144499 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:24.090771-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:25:24.093591-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:24.093655-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
error	20:25:24.093676-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:24.093961-0500	runningboardd	Invalidating assertion 400-98203-144499 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:24.093712-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:24.093843-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.099107-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7655)
default	20:25:24.099158-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7655)
default	20:25:24.099472-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:25:24.099967-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104e25b10) Device ID: 85 (Input:No | Output:Yes): true
default	20:25:24.099982-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104e25b10)
default	20:25:24.100668-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.100684-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:25:24.100722-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.100867-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:25:24.100960-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:25:24.101126-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:24.101281-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:25:24.101346-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7655 called from <private>
default	20:25:24.101440-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7655 called from <private>
default	20:25:24.102233-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144500 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:24.102344-0500	runningboardd	Assertion 400-98203-144500 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:24.101476-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7655 called from <private>
default	20:25:24.101543-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7655 called from <private>
default	20:25:24.101624-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
default	20:25:24.103018-0500	runningboardd	Invalidating assertion 400-98203-144500 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:24.103374-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6d00, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.103444-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
error	20:25:24.103573-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:24.103586-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7655 called from <private>
error	20:25:24.103621-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:24.103657-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7655 called from <private>
default	20:25:24.103351-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.VoiceOver(501)>:98203] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98203-144501 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:24.103760-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7655 called from <private>
default	20:25:24.103784-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7655 called from <private>
default	20:25:24.103823-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:25:24.103454-0500	runningboardd	Assertion 400-98203-144501 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:24.104080-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7655 called from <private>
error	20:25:24.105600-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:24.105679-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7655 called from <private>
default	20:25:24.122091-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.122113-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:25:24.122123-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.122157-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:25:24.122168-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:25:24.342222-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:24.342550-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:24.741889-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	20:25:24.781987-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7655 called from <private>
default	20:25:24.783763-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad5c80, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.783806-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:25:24.783920-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:25:24.785057-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:24.785197-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:25:24.785219-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104e25b10) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:25:24.785233-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:25:24.785259-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:25:24.785269-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xbf0a97618 (1C-77-54-18-C8-A3:output): Output stream format changed
default	20:25:24.786317-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad6d00, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.786968-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:24.787412-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:24.787720-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:24.788124-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:24.788439-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:24.788762-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:24.788810-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:24.789220-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xbefc3c000:
default	20:25:24.789309-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	20:25:24.789318-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	20:25:24.789340-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	20:25:24.789369-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	20:25:24.789392-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	20:25:24.789802-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:24.789853-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:24.790061-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xbefc3c000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	20:25:24.790750-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:24.791069-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:24.791450-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:24.791851-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:24.792233-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:24.792305-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:24.792407-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:24.792783-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:24.792889-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:24.792941-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:24.793373-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:24.793406-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:24.854090-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	20:25:24.890162-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f40ad, VoiceOver(98203), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f400c, Browser Helper(78232), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	20:25:24.891005-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
fault	20:25:25.920857-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:25.923635-0500	VoiceOver	No list of permitted front apps returned
default	20:25:26.025556-0500	VoiceOver	No list of permitted front apps returned
default	20:25:26.085910-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:26.086359-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:26.086436-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:26.095514-0500	VoiceOver	[0xbf066b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:26.095699-0500	VoiceOver	[0xbf066b480] invalidated after the last release of the connection object
default	20:25:26.112206-0500	VoiceOver	[0xbf066abc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:26.112363-0500	VoiceOver	[0xbf066abc0] invalidated after the last release of the connection object
default	20:25:26.117683-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad50b0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:26.117712-0500	VoiceOver	AudioConverter -> 0xbf2ad50b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:26.117732-0500	VoiceOver	AudioConverter -> 0xbf2ad50b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:26.137399-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:26.142501-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:26.142550-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:26.145176-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474877394 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:26.145668-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877573 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:26.193480-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:26.193876-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:26.194207-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	20:25:26.194261-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:26.194547-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:26.194581-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:26.194621-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:26.194820-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:26.194902-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:26.194941-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:26.195277-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:26.195302-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:26.212313-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12126039 ioTS st: 12126039 ht: 138345.813044
error	20:25:26.586047-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:25:26.641050-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:26.650620-0500	VoiceOver	No list of permitted front apps returned
default	20:25:26.752852-0500	VoiceOver	No list of permitted front apps returned
default	20:25:26.753197-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:26.754654-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:26.754825-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:27.110546-0500	VoiceOver	No list of permitted front apps returned
default	20:25:27.118400-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2874db0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:27.118438-0500	VoiceOver	AudioConverter -> 0xbf2874db0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:27.118451-0500	VoiceOver	AudioConverter -> 0xbf2874db0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:27.126336-0500	VoiceOver	No list of permitted front apps returned
default	20:25:27.141064-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:27.141832-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:27.141992-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:27.171408-0500	VoiceOver	[0xbf066af80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.171608-0500	VoiceOver	[0xbf066af80] invalidated after the last release of the connection object
default	20:25:27.225720-0500	VoiceOver	[0xbf066b5c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.226011-0500	VoiceOver	[0xbf066b5c0] invalidated after the last release of the connection object
default	20:25:27.244893-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2876070, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:27.244920-0500	VoiceOver	AudioConverter -> 0xbf2876070: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:27.244930-0500	VoiceOver	AudioConverter -> 0xbf2876070: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:27.291004-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:27.292861-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:27.292943-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:27.295876-0500	VoiceOver	[0xbf066b700] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.308393-0500	VoiceOver	[0xbf066b700] invalidated after the last release of the connection object
default	20:25:27.334949-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877573 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.336891-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877574 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.397043-0500	VoiceOver	[0xbf066bac0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.397706-0500	VoiceOver	[0xbf066bac0] invalidated after the last release of the connection object
default	20:25:27.414942-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:25:27.416538-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:27.417040-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:27.417130-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:27.417258-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:27.417680-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:27.417828-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	20:25:27.415570-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:27.417938-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:27.418342-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
fault	20:25:27.416614-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:27.418400-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:27.432454-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12152940 ioTS st: 12152940 ht: 138347.033044
default	20:25:27.686333-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.686592-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:27.691329-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:27.711677-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:27.712436-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:27.712590-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:27.714222-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:27.722994-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:27.723079-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:27.743702-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877574 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.744859-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877575 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.774666-0500	VoiceOver	[0xbf066bac0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:27.775355-0500	VoiceOver	[0xbf066bac0] invalidated after the last release of the connection object
default	20:25:27.792011-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:27.792573-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:27.793006-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:27.793205-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:27.793473-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:27.793507-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:27.793556-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:27.793845-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:27.793935-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:27.793981-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:27.794306-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:27.794322-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:27.802887-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:27.812952-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:27.813080-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:27.814454-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877575 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.815207-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877576 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:27.853492-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:27.854161-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:27.854681-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:27.854852-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:27.855129-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:27.855166-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:27.855233-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:27.855492-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:27.855592-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:27.855639-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:27.855933-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:27.855956-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:27.872478-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12162643 ioTS st: 12162643 ht: 138347.473044
error	20:25:27.921492-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	20:25:28.197942-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:28.209224-0500	VoiceOver	No list of permitted front apps returned
default	20:25:28.541443-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:28.542027-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:28.542114-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:28.561208-0500	VoiceOver	[0xbf066bc00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:28.561388-0500	VoiceOver	[0xbf066bc00] invalidated after the last release of the connection object
default	20:25:28.591048-0500	VoiceOver	[0xbf066bac0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:28.591279-0500	VoiceOver	[0xbf066bac0] invalidated after the last release of the connection object
default	20:25:28.601372-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad5440, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:28.601408-0500	VoiceOver	AudioConverter -> 0xbf2ad5440: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:28.601422-0500	VoiceOver	AudioConverter -> 0xbf2ad5440: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:28.622389-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:28.632774-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:28.632850-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:28.639229-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877576 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:28.640018-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877581 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:28.692884-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:28.693300-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:28.693825-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:28.694015-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:28.694679-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:28.694717-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
error	20:25:28.944158-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:29.043618-0500	VoiceOver	[0xbf066b0c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:29.043804-0500	VoiceOver	[0xbf066b0c0] invalidated after the last release of the connection object
default	20:25:29.354739-0500	VoiceOver	No list of permitted front apps returned
default	20:25:29.354937-0500	VoiceOver	No list of permitted front apps returned
default	20:25:29.398677-0500	VoiceOver	[0xbf066a580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:29.398854-0500	VoiceOver	[0xbf066a580] invalidated after the last release of the connection object
default	20:25:29.403747-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad60d0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:29.403769-0500	VoiceOver	AudioConverter -> 0xbf2ad60d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:29.403789-0500	VoiceOver	AudioConverter -> 0xbf2ad60d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:29.414726-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad56e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:29.414741-0500	VoiceOver	AudioConverter -> 0xbf2ad56e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:29.414752-0500	VoiceOver	AudioConverter -> 0xbf2ad56e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:29.415715-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:29.422487-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:29.422533-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:29.437051-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877581 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:29.437390-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877582 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:29.474786-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:29.475089-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:29.475428-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:29.475544-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:29.475722-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:29.475745-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:29.475779-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:29.475908-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:29.475955-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:29.475989-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:29.476196-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:29.476212-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:29.492337-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12198366 ioTS st: 12198366 ht: 138349.093044
default	20:25:29.537118-0500	VoiceOver	[0xbf066a6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:29.537256-0500	VoiceOver	[0xbf066a6c0] invalidated after the last release of the connection object
error	20:25:29.538647-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:29.540607-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf28753b0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:29.540628-0500	VoiceOver	AudioConverter -> 0xbf28753b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:29.540656-0500	VoiceOver	AudioConverter -> 0xbf28753b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:29.552108-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2877960, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:29.552129-0500	VoiceOver	AudioConverter -> 0xbf2877960: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:29.552144-0500	VoiceOver	AudioConverter -> 0xbf2877960: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:29.561041-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:29.566854-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:29.572563-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:29.572602-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:29.576605-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877582 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:29.576977-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877583 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:29.621304-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	20:25:29.621809-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	20:25:29.622236-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:29.622379-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	20:25:29.622638-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	20:25:29.622673-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	20:25:29.622725-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xbefc3c000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	20:25:29.622927-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 1
default	20:25:29.623007-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:29.623050-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:29.623322-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:29.623342-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:29.642363-0500	VoiceOver	AQSTL aq(0xbefc3c000) start time resolved to: 12201674 ioTS st: 12201674 ht: 138349.243044
default	20:25:29.779675-0500	VoiceOver	No list of permitted front apps returned
default	20:25:29.868367-0500	VoiceOver	[0xbf066a6c0] invalidated after the last release of the connection object
error	20:25:29.920048-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:30.137386-0500	VoiceOver	[0xbf066a940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:30.137572-0500	VoiceOver	[0xbf066a940] invalidated after the last release of the connection object
default	20:25:30.146408-0500	VoiceOver	No list of permitted front apps returned
default	20:25:30.157208-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad67f0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:30.157242-0500	VoiceOver	AudioConverter -> 0xbf2ad67f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:30.157259-0500	VoiceOver	AudioConverter -> 0xbf2ad67f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:30.170321-0500	VoiceOver	No list of permitted front apps returned
default	20:25:30.173567-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	20:25:30.174206-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:30.174336-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:30.183008-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:30.183209-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:25:30.185122-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:30.185302-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:25:30.195271-0500	VoiceOver	[0xbf0669f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	20:25:30.195475-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:25:30.202056-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbf2ad7e10, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	20:25:30.202109-0500	VoiceOver	AudioConverter -> 0xbf2ad7e10: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:30.202121-0500	VoiceOver	AudioConverter -> 0xbf2ad7e10: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	20:25:30.210627-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:30.212755-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:30.212836-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:30.230432-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877583 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:30.232286-0500	VoiceOver	[0xbf066a800] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	20:25:30.232847-0500	VoiceOver	[0xbf066a580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:25:30.233226-0500	VoiceOver	[0xbf066a080] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:25:30.233246-0500	VoiceOver	[0xbf066a080] Connection returned listener port: 0x28243
default	20:25:30.233984-0500	WindowServer	12ea7b[DoDeferredOrdering]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x741741 (VoiceOver) mainConnectionID: 12EA7B;
} for reason: updated frontmost process
default	20:25:30.234103-0500	WindowServer	12ea7b[DoDeferredOrdering]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x741741 (VoiceOver) -> <pid: 98203>
default	20:25:30.234240-0500	WindowServer	new deferring rules for pid:391: [
    [391-43F1]; <keyboardFocus; VoiceOver:0x0-0x741741>; () -> <pid: 98203>; reason: frontmost PSN --> outbound target,
    [391-43F0]; <keyboardFocus; <frontmost>>; () -> <token: VoiceOver:0x0-0x741741; pid: 391>; reason: frontmost PSN,
    [391-43EF]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	20:25:30.234289-0500	WindowServer	[keyboardFocus 0x830912b70] setRules:forPID(391): [
    [391-43F1]; <keyboardFocus; VoiceOver:0x0-0x741741>; () -> <pid: 98203>; reason: frontmost PSN --> outbound target,
    [391-43F0]; <keyboardFocus; <frontmost>>; () -> <token: VoiceOver:0x0-0x741741; pid: 391>; reason: frontmost PSN,
    [391-43EF]; <keyboardFocus>; () -> <token: <frontmost>; pid: 391>; reason: Deferring to <frontmost>
]
default	20:25:30.235095-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 391>,
    <token: VoiceOver:0x0-0x741741; pid: 391>,
    <pid: 98203>
]
default	20:25:30.237324-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "frontmost:98203" ID:400-361-144580 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	20:25:30.238177-0500	runningboardd	Assertion 400-361-144580 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:30.250601-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring jetsam update because this process is not memory-managed
default	20:25:30.250695-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring suspend because this process is not lifecycle managed
default	20:25:30.250900-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Set darwin role to: UserInteractiveFocal
default	20:25:30.250919-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring GPU update because this process is not GPU managed
default	20:25:30.250941-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Ignoring memory limit update because this process is not memory-managed
default	20:25:30.250956-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] Skipping AppNap state - not lifecycle managed
default	20:25:30.268477-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:98203] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "notification:98203" ID:400-361-144581 target:98203 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	20:25:30.268866-0500	runningboardd	Assertion 400-361-144581 (target:[osservice<com.apple.VoiceOver(501)>:98203]) will be created as active
default	20:25:30.285347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:30.285377-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	20:25:30.346093-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
error	20:25:30.349905-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:30.359031-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877584 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:30.373260-0500	VoiceOver	[0xbf0669f40] invalidated after the last release of the connection object
default	20:25:30.408327-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	20:25:31.092385-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:31.103923-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:31.104635-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:31.185666-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	20:25:31.402581-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:31.402646-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:31.417190-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877585 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:31.420732-0500	powerd	Process VoiceOver.98203 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877586 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:31.461966-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	20:25:31.462011-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:25:31.462452-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:25:31.462472-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xbf0a97618, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	20:25:31.490511-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	20:25:31.617835-0500	runningboardd	Invalidating assertion 400-361-144580 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
fault	20:25:31.619594-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:31.622824-0500	VoiceOver	No list of permitted front apps returned
default	20:25:31.625915-0500	runningboardd	Invalidating assertion 400-361-144581 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	20:25:31.656323-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 98203, name: VoiceOver
default	20:25:31.656502-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	20:25:31.666517-0500	VoiceOver	[0xbf0668140] invalidated after the last release of the connection object
default	20:25:31.724282-0500	VoiceOver	No list of permitted front apps returned
default	20:25:32.503480-0500	powerd	Process VoiceOver.98203 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877586 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	20:25:32.528151-0500	WindowServer	Connection removed: IOHIDEventSystemConnection uuid:E533B5E1-1F00-4951-8691-14A4F12C5DAB pid:98203 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x1 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	20:25:32.527767-0500	VoiceOver	Released connection: E533B5E1-1F00-4951-8691-14A4F12C5DAB
{
    UUID = "E533B5E1-1F00-4951-8691-14A4F12C5DAB";
    caller = "ScreenReader: -[SCREventFactory completeInitialization] + 1196";
    dispatchQueue = 0;
    eventCount = 0;
    eventMask = 0;
    port = 91907;
    resetCount = 0;
    runloop = 0;
    services =     (
        4294968852
    );
    virtualServices =     (
    );
}
default	20:25:32.527981-0500	VoiceOver	OSErr AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP, Boolean)(aevt,quit handler=0x807c800271c131c8 isSys=YES) err=0/noErr
default	20:25:32.850375-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
fault	20:25:32.891580-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	20:25:33.102987-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	20:25:33.113122-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	20:25:33.113256-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xbefc3c000; ; [98203]; play>; running count now 0
default	20:25:34.035701-0500	VoiceOver	[0xbf066b340] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	20:25:34.035764-0500	VoiceOver	Entering exit handler.
default	20:25:34.035799-0500	VoiceOver	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:25:34.035876-0500	VoiceOver	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:25:34.035883-0500	VoiceOver	[0xbf0810dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:25:34.035900-0500	VoiceOver	Exiting exit handler.
default	20:25:34.036966-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x741741 (VoiceOver) connectionID: 12EA7B pid: 98203 in session 0x101
default	20:25:34.036998-0500	WindowServer	<BSCompoundAssertion:0x830c11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x741741 (VoiceOver) acq:0x8344f9d00 count:1
default	20:25:34.037589-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x741741 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x741741 (VoiceOver)"
)}
default	20:25:34.045981-0500	WindowManager	Connection invalidated | (98203) VoiceOver
default	20:25:34.050405-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f40ad","name":"VoiceOver(98203)"}, "details":null }
default	20:25:34.050452-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f40ad from AudioApp, recording state unchanged (app: {"name":"[implicit] VoiceOver","pid":98203})
default	20:25:34.050467-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] VoiceOver","pid":98203})
default	20:25:34.051055-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 173 stopping playing
default	20:25:34.051145-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:25:34.051244-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:34.051470-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 98203, Name = sid:0x1f40ad, VoiceOver(98203), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:25:34.052433-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.052097-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.052275-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.052917-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.053545-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x17f9b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x741741 (VoiceOver)"
)}
default	20:25:34.057971-0500	runningboardd	Invalidating assertion 400-332-144348 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.powerd>:332]
default	20:25:34.062424-0500	runningboardd	XPC connection invalidated: [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:34.062704-0500	runningboardd	Invalidating assertion 400-391-143783 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.WindowServer(88)>:391]
default	20:25:34.065035-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.065053-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 2
default	20:25:34.065464-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	20:25:34.069641-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.apple.VoiceOver with asn: LSASN:{hi=0x0;lo=0x741741} for bundle path: /System/Library/CoreServices/VoiceOver.app with URL: file:///System/Library/CoreServices/VoiceOver.app/
default	20:25:34.069681-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121a440: VoiceOver> state 3
default	20:25:34.069703-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:VoiceOver, _appTrackingState = 2
default	20:25:34.070399-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121a440: VoiceOver> state 4
default	20:25:34.070470-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:VoiceOver, _appTrackingState = 2
default	20:25:34.071901-0500	runningboardd	XPC connection invalidated: [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:34.072154-0500	runningboardd	Invalidating assertion 400-361-143779 (target:[osservice<com.apple.VoiceOver(501)>:98203]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	20:25:34.072875-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:98203] termination reported by launchd (0, 0, 0)
default	20:25:34.072952-0500	runningboardd	Removing process: [osservice<com.apple.VoiceOver(501)>:98203]
error	20:25:34.073221-0500	runningboardd	RBSStateCapture remove item called for untracked item <RBConnectionClient| 98203 name:osservice<com.apple.VoiceOver(501)> entitlements:<RBEntitlements| [
			com.apple.assertiond.app-state-monitor,
			com.apple.private.security.container-required
			]> inheritanceManager:<RBClientInheritanceManager|  inheritances:[
	<RBSInheritance| environment:(none) name:com.apple.launchservices.userfacing origID:400-361-143779 0>
	]>>
default	20:25:34.073260-0500	runningboardd	removeJobWithInstance called for identity without existing job [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:34.073272-0500	runningboardd	Removing assertions for terminated process: [osservice<com.apple.VoiceOver(501)>:98203]
default	20:25:34.073328-0500	runningboardd	Removed last relative-start-date-defining assertion for process xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	20:25:34.077471-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209] termination reported by launchd (2, 15, 15)
default	20:25:34.077507-0500	runningboardd	Removing process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]
default	20:25:34.077660-0500	runningboardd	Removing assertions for terminated process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]
default	20:25:34.082439-0500	runningboardd	XPC connection invalidated: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:98209]
default	20:25:34.082554-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: none (role: None) (endowments: (null))
default	20:25:34.083208-0500	WindowServer	Received state update for 98209 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, none-NotVisible
default	20:25:34.083003-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 98203, name = VoiceOver
default	20:25:34.083172-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: none (role: None) (endowments: (null))
default	20:25:34.083276-0500	UIKitSystem	Received state update for 98209 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, none-NotVisible
default	20:25:34.083403-0500	WindowServer	Received state update for 98209 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, none-NotVisible
default	20:25:34.083540-0500	UIKitSystem	Received state update for 98209 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, none-NotVisible
default	20:25:34.083992-0500	gamepolicyd	Received state update for 98203 (osservice<com.apple.VoiceOver(501)>, none-NotVisible
default	20:25:34.084021-0500	gamepolicyd	Received state update for 98209 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:98203])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, none-NotVisible
error	20:25:34.164478-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-391-143783 (target:[osservice<com.apple.VoiceOver(501)>:98203])
error	20:25:34.164494-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-361-143779 (target:[osservice<com.apple.VoiceOver(501)>:98203])
error	20:25:34.164510-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-332-144348 (target:[osservice<com.apple.VoiceOver(501)>:98203])
default	20:25:40.544125-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98404
default	20:25:40.544239-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 98403
default	20:25:56.380863-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 99427
default	20:25:57.487449-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
