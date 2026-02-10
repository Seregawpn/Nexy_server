;
"use strict";
const _0xb21196 = _0x4ba3;
(function(_0x326882, _0x80c5ac) {
  const _0x34edf8 = _0x4ba3, _0x2c10b0 = _0x326882();
  while (!![]) {
    try {
      const _0xdd2de8 = -parseInt(_0x34edf8(407)) / 1 + parseInt(_0x34edf8(403)) / 2 + -parseInt(_0x34edf8(446)) / 3 * (parseInt(_0x34edf8(460)) / 4) + -parseInt(_0x34edf8(410)) / 5 * (-parseInt(_0x34edf8(457)) / 6) + parseInt(_0x34edf8(458)) / 7 * (parseInt(_0x34edf8(438)) / 8) + -parseInt(_0x34edf8(424)) / 9 + -parseInt(_0x34edf8(425)) / 10 * (-parseInt(_0x34edf8(441)) / 11);
      if (_0xdd2de8 === _0x80c5ac) break;
      else _0x2c10b0["push"](_0x2c10b0["shift"]());
    } catch (_0x2e834b) {
      _0x2c10b0["push"](_0x2c10b0["shift"]());
    }
  }
})(_0x3fa0, 573589);
function _0x4ba3(_0x1efee9, _0x5157bd) {
  _0x1efee9 = _0x1efee9 - 402;
  const _0x2a4f83 = _0x3fa0();
  let _0x110f46 = _0x2a4f83[_0x1efee9];
  return _0x110f46;
}
const electron = require("electron"), preload = require("@electron-toolkit/preload"), log = require("electron-log/renderer");
function _interopNamespaceDefault(_0x45cbd5) {
  const _0x276fe0 = _0x4ba3, _0x4c3075 = /* @__PURE__ */ (function() {
    let _0x34be63 = !![];
    return function(_0x1b0dfb, _0x4c2ced) {
      const _0x99632 = _0x34be63 ? function() {
        const _0x546185 = _0x4ba3;
        if (_0x4c2ced) {
          const _0xbcf170 = _0x4c2ced[_0x546185(461)](_0x1b0dfb, arguments);
          return _0x4c2ced = null, _0xbcf170;
        }
      } : function() {
      };
      return _0x34be63 = ![], _0x99632;
    };
  })(), _0x2ce81d = _0x4c3075(this, function() {
    const _0x2480c7 = _0x4ba3, _0x4e143b = function() {
      const _0x3f5c48 = _0x4ba3;
      let _0x296475;
      try {
        _0x296475 = Function(_0x3f5c48(437) + _0x3f5c48(436) + ");")();
      } catch (_0x31bd2e) {
        _0x296475 = window;
      }
      return _0x296475;
    }, _0x2f983f = _0x4e143b(), _0x2a9e2a = _0x2f983f[_0x2480c7(414)] = _0x2f983f[_0x2480c7(414)] || {}, _0x144514 = [_0x2480c7(416), _0x2480c7(422), _0x2480c7(440), _0x2480c7(415), _0x2480c7(419), _0x2480c7(408), _0x2480c7(459)];
    for (let _0x16ac9a = 0; _0x16ac9a < _0x144514[_0x2480c7(405)]; _0x16ac9a++) {
      const _0x4b9300 = _0x4c3075[_0x2480c7(435)][_0x2480c7(420)][_0x2480c7(434)](_0x4c3075), _0x55604e = _0x144514[_0x16ac9a], _0x41be03 = _0x2a9e2a[_0x55604e] || _0x4b9300;
      _0x4b9300[_0x2480c7(439)] = _0x4c3075[_0x2480c7(434)](_0x4c3075), _0x4b9300[_0x2480c7(445)] = _0x41be03[_0x2480c7(445)][_0x2480c7(434)](_0x41be03), _0x2a9e2a[_0x55604e] = _0x4b9300;
    }
  });
  _0x2ce81d();
  const _0x157f73 = Object[_0x276fe0(452)](null, { [Symbol[_0x276fe0(448)]]: { "value": _0x276fe0(430) } });
  if (_0x45cbd5) for (const _0x2352bb in _0x45cbd5) {
    if (_0x2352bb !== _0x276fe0(444)) {
      const _0x59ab3f = Object[_0x276fe0(412)](_0x45cbd5, _0x2352bb);
      Object[_0x276fe0(429)](_0x157f73, _0x2352bb, _0x59ab3f[_0x276fe0(411)] ? _0x59ab3f : { "enumerable": !![], "get": () => _0x45cbd5[_0x2352bb] });
    }
  }
  return _0x157f73[_0x276fe0(444)] = _0x45cbd5, Object[_0x276fe0(462)](_0x157f73);
}
const log__namespace = _interopNamespaceDefault(log), api = { "send": (_0x252477, ..._0x5225f5) => {
  const _0x575d99 = _0x4ba3;
  electron[_0x575d99(409)][_0x575d99(442)](_0x252477, ..._0x5225f5);
}, "on": (_0x6c63da, _0x2410c2) => {
  const _0x6d12d4 = _0x4ba3, _0x5ba07d = (_0x16a0b3, ..._0xe9f3d8) => {
    _0x2410c2(..._0xe9f3d8);
  };
  return electron[_0x6d12d4(409)]["on"](_0x6c63da, _0x5ba07d), () => {
    const _0x496c6b = _0x6d12d4;
    electron[_0x496c6b(409)][_0x496c6b(406)](_0x6c63da, _0x5ba07d);
  };
}, "receive": (_0x307377, _0x2c44b3) => {
  const _0x2efc74 = _0x4ba3;
  electron[_0x2efc74(409)]["on"](_0x307377, (_0x4b38be, ..._0x461cc7) => _0x2c44b3(..._0x461cc7));
}, "invoke": (_0x3c8b15, ..._0x138303) => {
  const _0x8829f8 = _0x4ba3;
  return electron[_0x8829f8(409)][_0x8829f8(454)](_0x3c8b15, ..._0x138303);
}, "removeAllListeners": (_0x339f7e) => electron[_0xb21196(409)][_0xb21196(404)](_0x339f7e), "startKeyListener": () => electron[_0xb21196(409)][_0xb21196(454)]("start-key-listener-service"), "stopKeyListener": () => electron[_0xb21196(409)][_0xb21196(454)]("stop-key-listener"), "registerHotkeys": () => electron[_0xb21196(409)][_0xb21196(454)]("register-hotkeys"), "startNativeRecording": () => electron[_0xb21196(409)][_0xb21196(454)]("start-native-recording"), "stopNativeRecording": () => electron[_0xb21196(409)][_0xb21196(454)]("stop-native-recording"), "getNativeAudioDevices": () => electron[_0xb21196(409)][_0xb21196(454)]("get-native-audio-devices"), "onVolumeUpdate": (_0x1ed27a) => {
  const _0x266412 = _0xb21196, _0x227029 = (_0x4a1171, _0x7d339b) => _0x1ed27a(_0x7d339b);
  return electron[_0x266412(409)]["on"]("volume-update", _0x227029), () => electron[_0x266412(409)][_0x266412(406)]("volume-update", _0x227029);
}, "blockKeys": (_0x25b590) => electron[_0xb21196(409)][_0xb21196(454)]("block-keys", _0x25b590), "unblockKey": (_0x55fc70) => electron[_0xb21196(409)][_0xb21196(454)]("unblock-key", _0x55fc70), "getBlockedKeys": () => electron[_0xb21196(409)][_0xb21196(454)]("get-blocked-keys"), "onKeyEvent": (_0x5568f3) => {
  const _0x4456eb = _0xb21196, _0x52746b = (_0x53ac8d, _0x172dff) => _0x5568f3(_0x172dff);
  return electron[_0x4456eb(409)]["on"]("key-event", _0x52746b), () => electron[_0x4456eb(409)][_0x4456eb(406)]("key-event", _0x52746b);
}, "generateNewAuthState": () => electron[_0xb21196(409)][_0xb21196(454)]("generate-new-auth-state"), "exchangeAuthCode": (_0x205c0c) => electron[_0xb21196(409)][_0xb21196(454)]("exchange-auth-code", _0x205c0c), "logout": () => electron[_0xb21196(409)][_0xb21196(454)]("logout"), "setPillMouseEvents": (_0x5cef06, _0x490a09) => electron[_0xb21196(409)][_0xb21196(454)]("pill-set-mouse-events", _0x5cef06, _0x490a09), "setPillFocusable": (_0x17bfe7) => electron[_0xb21196(409)][_0xb21196(454)]("pill-set-focusable", _0x17bfe7), "pillStartDrag": (_0x9dc5e0, _0x1bcaca) => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(427), _0x9dc5e0, _0x1bcaca), "pillDragMove": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(456)), "pillStopDrag": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(418)), "pillUnpin": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(450)), "pillRestorePosition": () => electron[_0xb21196(409)][_0xb21196(454)]("pill-restore-position"), "init-window": () => electron[_0xb21196(409)][_0xb21196(454)]("init-window"), "is-window-minimizable": () => electron[_0xb21196(409)][_0xb21196(454)]("is-window-minimizable"), "is-window-maximizable": () => electron[_0xb21196(409)][_0xb21196(454)]("is-window-maximizable"), "window-minimize": () => electron[_0xb21196(409)][_0xb21196(454)]("window-minimize"), "window-maximize": () => electron[_0xb21196(409)][_0xb21196(454)]("window-maximize"), "window-close": () => electron[_0xb21196(409)][_0xb21196(454)]("window-close"), "window-maximize-toggle": () => electron[_0xb21196(409)][_0xb21196(454)]("window-maximize-toggle"), "web-undo": () => electron[_0xb21196(409)][_0xb21196(454)]("web-undo"), "web-redo": () => electron[_0xb21196(409)][_0xb21196(454)]("web-redo"), "web-cut": () => electron[_0xb21196(409)][_0xb21196(454)]("web-cut"), "web-copy": () => electron[_0xb21196(409)][_0xb21196(454)]("web-copy"), "web-paste": () => electron[_0xb21196(409)][_0xb21196(454)]("web-paste"), "web-delete": () => electron[_0xb21196(409)][_0xb21196(454)]("web-delete"), "web-select-all": () => electron[_0xb21196(409)][_0xb21196(454)]("web-select-all"), "web-reload": () => electron[_0xb21196(409)][_0xb21196(454)]("web-reload"), "web-force-reload": () => electron[_0xb21196(409)][_0xb21196(454)]("web-force-reload"), "web-toggle-devtools": () => electron[_0xb21196(409)][_0xb21196(454)]("web-toggle-devtools"), "web-actual-size": () => electron[_0xb21196(409)][_0xb21196(454)]("web-actual-size"), "web-zoom-in": () => electron[_0xb21196(409)][_0xb21196(454)]("web-zoom-in"), "web-zoom-out": () => electron[_0xb21196(409)][_0xb21196(454)]("web-zoom-out"), "web-toggle-fullscreen": () => electron[_0xb21196(409)][_0xb21196(454)]("web-toggle-fullscreen"), "web-open-url": (_0x535a80) => electron[_0xb21196(409)][_0xb21196(454)]("web-open-url", _0x535a80), "openExternal": (_0x5b6105) => electron[_0xb21196(409)][_0xb21196(454)]("web-open-url", _0x5b6105), "check-accessibility-permission": (_0x4f3913) => electron[_0xb21196(409)][_0xb21196(454)]("check-accessibility-permission", _0x4f3913), "get-accessibility-permission-status": () => electron[_0xb21196(409)][_0xb21196(454)]("get-accessibility-permission-status"), "openAccessibilitySettings": () => electron[_0xb21196(409)][_0xb21196(454)]("open-accessibility-settings"), "check-microphone-permission": (_0x509f71) => electron[_0xb21196(409)][_0xb21196(454)]("check-microphone-permission", _0x509f71), "get-microphone-permission-status": () => electron[_0xb21196(409)][_0xb21196(454)]("get-microphone-permission-status"), "check-screen-recording-permission": (_0x5b4e68) => electron[_0xb21196(409)][_0xb21196(454)]("check-screen-recording-permission", _0x5b4e68), "openScreenRecordingSettings": () => electron[_0xb21196(409)][_0xb21196(454)]("open-screen-recording-settings"), "triggerScreenCaptureConsent": () => electron[_0xb21196(409)][_0xb21196(454)]("trigger-screen-capture-consent"), "restartApp": () => electron[_0xb21196(409)][_0xb21196(454)]("restart-app"), "start-native-recording": () => electron[_0xb21196(409)][_0xb21196(442)]("start-native-recording"), "stop-native-recording": () => electron[_0xb21196(409)][_0xb21196(442)]("stop-native-recording"), "pill": { "startGenMode": () => electron[_0xb21196(409)][_0xb21196(454)]("start-gen-mode-from-pill"), "startDictation": () => electron[_0xb21196(409)][_0xb21196(454)]("start-dictation-from-pill"), "stopRecording": () => electron[_0xb21196(409)][_0xb21196(454)]("stop-recording-from-pill"), "cancelRecording": () => electron[_0xb21196(409)][_0xb21196(454)]("cancel-recording-from-pill"), "undoKeyword": (_0xe0946f) => electron[_0xb21196(409)][_0xb21196(454)]("dictionary:delete", _0xe0946f), "startVoiceFollowUp": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(428)), "stopVoiceFollowUp": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(423)), "sendFollowUp": (_0x4e966e) => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(426), _0x4e966e), "endChatSession": () => electron[_0xb21196(409)][_0xb21196(442)]("end-chat-session"), "checkFocusedEditable": () => electron[_0xb21196(409)][_0xb21196(454)]("check-focused-editable"), "pasteOutputText": (_0x665840) => electron[_0xb21196(409)][_0xb21196(454)]("paste-output-text", _0x665840) }, "handsFree": { "stopRecording": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(402)), "cancelRecording": () => electron[_0xb21196(409)][_0xb21196(454)](_0xb21196(447)) }, "dev": { "revertLastMigration": () => electron[_0xb21196(409)][_0xb21196(454)]("dev:revert-last-migration"), "wipeDatabase": () => electron[_0xb21196(409)][_0xb21196(454)]("dev:wipe-database"), "checkSchema": () => electron[_0xb21196(409)][_0xb21196(454)]("debug:check-schema") }, "dictionary": { "getAll": () => electron[_0xb21196(409)][_0xb21196(454)]("dictionary:get-all"), "add": (_0xa15bb7) => electron[_0xb21196(409)][_0xb21196(454)]("dictionary:add", _0xa15bb7), "update": (_0x5ca719, _0xbbdc14, _0x8a138d, _0x4144d4) => electron[_0xb21196(409)][_0xb21196(454)]("dictionary:update", { "id": _0x5ca719, "text": _0xbbdc14, "description": _0x8a138d, "app_identifiers": _0x4144d4 }), "delete": (_0x557b71) => electron[_0xb21196(409)][_0xb21196(454)]("dictionary:delete", _0x557b71) }, "knowledge": { "getAll": () => electron[_0xb21196(409)][_0xb21196(454)]("knowledge:get-all"), "add": (_0x3ffa80, _0xf0af49) => electron[_0xb21196(409)][_0xb21196(454)]("knowledge:add", { "title": _0x3ffa80, "content": _0xf0af49 }), "update": (_0x2b2e9d, _0x4b5a9f, _0x1d2e4a) => electron[_0xb21196(409)][_0xb21196(454)]("knowledge:update", { "id": _0x2b2e9d, "title": _0x4b5a9f, "content": _0x1d2e4a }), "delete": (_0x2cd36d) => electron[_0xb21196(409)][_0xb21196(454)]("knowledge:delete", _0x2cd36d), "syncToGrpc": (_0x40484a) => electron[_0xb21196(409)][_0xb21196(454)]("knowledge:sync-to-grpc", _0x40484a) }, "customInstructions": { "getAll": () => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:get-all"), "add": (_0x110886, _0x35cf1d) => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:add", { "appIdentifier": _0x110886, "instruction": _0x35cf1d }), "update": (_0x13a3fb, _0x313045, _0x2469d4) => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:update", { "id": _0x13a3fb, "appIdentifier": _0x313045, "instruction": _0x2469d4 }), "delete": (_0x4b3427) => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:delete", _0x4b3427), "syncToGrpc": () => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:sync-to-grpc"), "getUsedApps": () => electron[_0xb21196(409)][_0xb21196(454)]("custom-instructions:get-used-apps") }, "voiceSessions": { "getAll": () => electron[_0xb21196(409)][_0xb21196(454)]("voice-sessions:get-all"), "delete": (_0x29d37a) => electron[_0xb21196(409)][_0xb21196(454)]("voice-sessions:delete", _0x29d37a) }, "appIcons": { "getAll": () => electron[_0xb21196(409)][_0xb21196(454)]("app-icons:get-all"), "getByName": (_0x312974) => electron[_0xb21196(409)][_0xb21196(454)]("app-icons:get-by-name", _0x312974) }, "loginItem": { "setSettings": (_0xf88fd0) => electron[_0xb21196(409)][_0xb21196(454)]("set-login-item-settings", _0xf88fd0), "getSettings": () => electron[_0xb21196(409)][_0xb21196(454)]("get-login-item-settings") }, "dock": { "setVisibility": (_0x4e5847) => electron[_0xb21196(409)][_0xb21196(454)]("set-dock-visibility", _0x4e5847), "getVisibility": () => electron[_0xb21196(409)][_0xb21196(454)]("get-dock-visibility") }, "notifySettingsUpdate": (_0x326477) => electron[_0xb21196(409)][_0xb21196(442)]("settings-update", _0x326477), "notifyOnboardingUpdate": (_0x2306ef) => electron[_0xb21196(409)][_0xb21196(442)]("onboarding-update", _0x2306ef), "notifyUserAuthUpdate": (_0x2a442f) => electron[_0xb21196(409)][_0xb21196(442)]("user-auth-update", _0x2a442f), "analytics:get-device-id": () => electron[_0xb21196(409)][_0xb21196(454)]("analytics:get-device-id"), "getOnboardingState": () => electron[_0xb21196(409)][_0xb21196(454)]("get-onboarding-state"), "notifyLoginSuccess": (_0x42fde2, _0x564343, _0x19f67c) => {
  const _0x5529ac = _0xb21196;
  return electron[_0x5529ac(409)][_0x5529ac(454)]("notify-login-success", { "profile": _0x42fde2, "idToken": _0x564343, "accessToken": _0x19f67c });
}, "deleteUserData": () => {
  const _0x19e757 = _0xb21196;
  return electron[_0x19e757(409)][_0x19e757(454)]("delete-user-data");
}, "checkServerHealth": () => {
  const _0x5261e8 = _0xb21196;
  return electron[_0x5261e8(409)][_0x5261e8(454)]("check-server-health");
}, "updater": { "onUpdateAvailable": (_0x450f9d) => {
  const _0x5615e3 = _0xb21196, _0x233774 = () => _0x450f9d();
  return electron[_0x5615e3(409)]["on"]("update-available", _0x233774), () => electron[_0x5615e3(409)][_0x5615e3(406)]("update-available", _0x233774);
}, "onUpdateDownloaded": (_0x2beeb5) => {
  const _0x5b2a68 = _0xb21196, _0x1bea72 = () => _0x2beeb5();
  return electron[_0x5b2a68(409)]["on"]("update-downloaded", _0x1bea72), () => electron[_0x5b2a68(409)][_0x5b2a68(406)]("update-downloaded", _0x1bea72);
}, "onUpdateError": (_0x5df7cc) => {
  const _0xba2e55 = _0xb21196, _0x4c3b3a = (_0x1a8641, _0x52b08e) => _0x5df7cc(_0x52b08e);
  return electron[_0xba2e55(409)]["on"]("update-error", _0x4c3b3a), () => electron[_0xba2e55(409)][_0xba2e55(406)]("update-error", _0x4c3b3a);
}, "installUpdate": () => electron[_0xb21196(409)][_0xb21196(442)]("install-update"), "getUpdateStatus": () => electron[_0xb21196(409)][_0xb21196(454)]("get-update-status") }, "getPlatform": () => electron[_0xb21196(409)][_0xb21196(454)]("get-platform"), "getSystemTheme": () => electron[_0xb21196(409)][_0xb21196(454)]("get-system-theme"), "onSystemThemeChanged": (_0x132371) => {
  const _0x2aa55c = _0xb21196, _0x3c91a6 = (_0x21f3d7, _0x56cabb) => _0x132371(_0x56cabb);
  return electron[_0x2aa55c(409)]["on"]("system-theme-changed", _0x3c91a6), () => electron[_0x2aa55c(409)][_0x2aa55c(406)]("system-theme-changed", _0x3c91a6);
}, "selectedText": { "get": (_0x574c0d) => electron[_0xb21196(409)][_0xb21196(454)]("get-selected-text", _0x574c0d), "getString": (_0x1c8200) => electron[_0xb21196(409)][_0xb21196(454)]("get-selected-text-string", _0x1c8200), "hasSelected": () => electron[_0xb21196(409)][_0xb21196(454)]("has-selected-text") }, "openai": { "getToken": () => electron[_0xb21196(409)][_0xb21196(454)]("openai:get-token") }, "subscription": { "getStatus": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:get-status"), "getUsageStats": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:get-usage-stats"), "createCheckoutSession": (_0x5b863c = "yearly") => electron[_0xb21196(409)][_0xb21196(454)]("subscription:create-checkout-session", _0x5b863c), "createPortalSession": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:create-portal-session"), "activateReferral": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:activate-referral"), "activateTrial": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:activate-trial"), "createTeamCheckoutSession": (_0x20836a = 3, _0x3bf7bf = "yearly") => electron[_0xb21196(409)][_0xb21196(454)]("subscription:create-team-checkout-session", _0x20836a, _0x3bf7bf), "getTeamStatus": () => electron[_0xb21196(409)][_0xb21196(454)]("subscription:get-team-status"), "linkTeamSubscription": (_0x21fc8f) => electron[_0xb21196(409)][_0xb21196(454)]("subscription:link-team-subscription", _0x21fc8f), "getPrices": (_0x417e64) => electron[_0xb21196(409)][_0xb21196(454)]("subscription:get-prices", _0x417e64) }, "playground": { "setAppContext": (_0x16103e, _0x46bec3, _0x49bee6) => electron[_0xb21196(409)][_0xb21196(454)]("set-override-app-context", _0x16103e, _0x46bec3, _0x49bee6), "clearAppContext": () => electron[_0xb21196(409)][_0xb21196(454)]("clear-override-app-context") }, "onboarding": { "forceBuiltinMicrophone": () => electron[_0xb21196(409)][_0xb21196(454)]("force-builtin-microphone-for-onboarding"), "restoreOriginalMicrophone": () => electron[_0xb21196(409)][_0xb21196(454)]("restore-original-microphone-after-onboarding") }, "userProfile": { "get": () => electron[_0xb21196(409)][_0xb21196(454)]("user-profile:get"), "update": (_0x4bc20d) => electron[_0xb21196(409)][_0xb21196(454)]("user-profile:update", _0x4bc20d) }, "getAppVersion": () => electron[_0xb21196(409)][_0xb21196(454)]("get-app-version"), "copyToClipboard": (_0x365354) => {
  const _0x1809b2 = _0xb21196;
  electron[_0x1809b2(431)][_0x1809b2(453)](_0x365354);
} };
Object[_0xb21196(413)](console, log__namespace[_0xb21196(417)]);
function _0x3fa0() {
  const _0x125c72 = ["__proto__", "info", "11JGpiWZ", "send", "sendSync", "default", "toString", "3336207YYYAqS", "cancel-handsfree-recording", "toStringTag", "contextBridge", "pill-unpin", "exposeInMainWorld", "create", "writeText", "invoke", "electronAPI", "pill-drag-move", "24zjcolX", "73780kqFRbA", "trace", "4lJjtAi", "apply", "freeze", "stop-handsfree-recording", "801828hOVfBA", "removeAllListeners", "length", "removeListener", "690300vdDSch", "table", "ipcRenderer", "711065xQrqik", "get", "getOwnPropertyDescriptor", "assign", "console", "error", "log", "functions", "pill-stop-drag", "exception", "prototype", "contextIsolated", "warn", "stop-voice-follow-up-from-pill", "6853338RXhDTc", "10715140QYfPUz", "chat-follow-up", "pill-start-drag", "start-voice-follow-up-from-pill", "defineProperty", "Module", "clipboard", "electron", "api", "bind", "constructor", '{}.constructor("return this")( )', "return (function() ", "832nlCDOb"];
  _0x3fa0 = function() {
    return _0x125c72;
  };
  return _0x3fa0();
}
if (process[_0xb21196(421)]) try {
  electron[_0xb21196(449)][_0xb21196(451)]("electron", { ...preload[_0xb21196(455)], "store": { "get"(_0x3c4ff4) {
    const _0x1d6190 = _0xb21196;
    return electron[_0x1d6190(409)][_0x1d6190(443)]("electron-store-get", _0x3c4ff4);
  }, "set"(_0x5670c5, _0x4448d1) {
    const _0x3f8953 = _0xb21196;
    electron[_0x3f8953(409)][_0x3f8953(442)]("electron-store-set", _0x5670c5, _0x4448d1);
  } } }), electron[_0xb21196(449)][_0xb21196(451)]("api", api);
} catch (_0x172b10) {
  console[_0xb21196(415)](_0x172b10);
}
else window[_0xb21196(432)] = { ...preload[_0xb21196(455)], "store": { "get"(_0x4b5487) {
  const _0x32e5e6 = _0xb21196;
  return electron[_0x32e5e6(409)][_0x32e5e6(443)]("electron-store-get", _0x4b5487);
}, "set"(_0x16a2e4, _0x4dc949) {
  const _0x173735 = _0xb21196;
  electron[_0x173735(409)][_0x173735(442)]("electron-store-set", _0x16a2e4, _0x4dc949);
} } }, window[_0xb21196(433)] = api