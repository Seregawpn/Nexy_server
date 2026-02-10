;
const _0x3f500e = _0x1b4f;
(function(_0x1bcd3a, _0x136e48) {
  const _0x735a46 = _0x1b4f, _0x36b13d = _0x1bcd3a();
  while (!![]) {
    try {
      const _0x51f882 = -parseInt(_0x735a46(244)) / 1 + -parseInt(_0x735a46(271)) / 2 * (parseInt(_0x735a46(353)) / 3) + parseInt(_0x735a46(242)) / 4 + parseInt(_0x735a46(356)) / 5 * (parseInt(_0x735a46(305)) / 6) + parseInt(_0x735a46(267)) / 7 + parseInt(_0x735a46(296)) / 8 * (-parseInt(_0x735a46(239)) / 9) + parseInt(_0x735a46(231)) / 10;
      if (_0x51f882 === _0x136e48) break;
      else _0x36b13d["push"](_0x36b13d["shift"]());
    } catch (_0x33cd70) {
      _0x36b13d["push"](_0x36b13d["shift"]());
    }
  }
})(_0x3edc, 374741);
const _0x9c7691 = /* @__PURE__ */ (function() {
  let _0x1dbdde = !![];
  return function(_0x3d19cd, _0x57a300) {
    const _0x135778 = _0x1dbdde ? function() {
      const _0x43b0aa = _0x1b4f;
      if (_0x57a300) {
        const _0x2d94e8 = _0x57a300[_0x43b0aa(334)](_0x3d19cd, arguments);
        return _0x57a300 = null, _0x2d94e8;
      }
    } : function() {
    };
    return _0x1dbdde = ![], _0x135778;
  };
})(), _0x1879e4 = _0x9c7691(exports, function() {
  const _0x5f1195 = _0x1b4f;
  let _0x5f6512;
  try {
    const _0xa1b70a = Function(_0x5f1195(322) + _0x5f1195(348) + ");");
    _0x5f6512 = _0xa1b70a();
  } catch (_0x11c6ee) {
    _0x5f6512 = window;
  }
  const _0x4460db = _0x5f6512[_0x5f1195(317)] = _0x5f6512[_0x5f1195(317)] || {}, _0x2f7338 = [_0x5f1195(352), _0x5f1195(325), _0x5f1195(228), _0x5f1195(251), _0x5f1195(227), _0x5f1195(306), _0x5f1195(327)];
  for (let _0x1952a1 = 0; _0x1952a1 < _0x2f7338[_0x5f1195(237)]; _0x1952a1++) {
    const _0xd21510 = _0x9c7691[_0x5f1195(263)][_0x5f1195(229)][_0x5f1195(279)](_0x9c7691), _0x175c67 = _0x2f7338[_0x1952a1], _0x3e0cef = _0x4460db[_0x175c67] || _0xd21510;
    _0xd21510[_0x5f1195(257)] = _0x9c7691[_0x5f1195(279)](_0x9c7691), _0xd21510[_0x5f1195(329)] = _0x3e0cef[_0x5f1195(329)][_0x5f1195(279)](_0x3e0cef), _0x4460db[_0x175c67] = _0xd21510;
  }
});
_0x1879e4();
"use strict";
Object[_0x3f500e(289)](exports, Symbol[_0x3f500e(266)], { "value": _0x3f500e(217) });
const electron = require("electron"), log = require("electron-log"), main = require(_0x3f500e(292));
require("dotenv"), require(_0x3f500e(232)), require("electron-store"), require("crypto"), require("@bufbuild/protobuf/codegenv2"), require("@bufbuild/protobuf/wkt"), require("@electron-toolkit/utils"), require("path"), require("url"), require("fs"), require("os"), require("electron-updater"), require("@connectrpc/connect"), require("@connectrpc/connect-node"), require("@bufbuild/protobuf"), require(_0x3f500e(215)), require("uuid"), require(_0x3f500e(270)), require(_0x3f500e(281)), require(_0x3f500e(282)), require(_0x3f500e(273)), require("node-machine-id");
class ScreenshotService {
  [_0x3f500e(268)]() {
    const _0x30e6c4 = _0x3f500e;
    if (process[_0x30e6c4(275)] === "darwin") {
      const _0x18fbb6 = electron[_0x30e6c4(328)][_0x30e6c4(326)](_0x30e6c4(274));
      return _0x18fbb6 === _0x30e6c4(345);
    }
    return !![];
  }
  async [_0x3f500e(246)](_0x3b6244 = _0x3f500e(264), _0x823451 = 80) {
    const _0x44962f = _0x3f500e, _0x460add = Date[_0x44962f(332)]();
    try {
      log[_0x44962f(228)]("[Screenshot] Starting display capture at cursor position");
      const _0x30f70a = Date[_0x44962f(332)]();
      if (process[_0x44962f(275)] === "darwin") {
        const _0x5cd2f2 = electron[_0x44962f(328)][_0x44962f(326)](_0x44962f(274));
        log[_0x44962f(228)](_0x44962f(290) + _0x5cd2f2), _0x5cd2f2 === _0x44962f(288) && (log[_0x44962f(325)]("[Screenshot] Screen Recording permission previously denied"), log[_0x44962f(325)]("[Screenshot] Attempting capture anyway to trigger permission dialog..."), log[_0x44962f(325)]("[Screenshot] If the dialog doesn't appear, you may need to reset the permission:"), log[_0x44962f(325)]("[Screenshot]   Run: tccutil reset ScreenCapture")), _0x5cd2f2 === _0x44962f(248) && log[_0x44962f(228)]("[Screenshot] Screen Recording permission not determined - capture will trigger permission dialog");
      }
      const _0x5f5bcc = Date[_0x44962f(332)]() - _0x30f70a, _0x5c2113 = Date[_0x44962f(332)](), _0x317f93 = electron[_0x44962f(274)][_0x44962f(294)](), _0x562aa1 = electron[_0x44962f(274)][_0x44962f(260)](_0x317f93), _0x20248a = _0x562aa1["id"][_0x44962f(329)](), _0x53c186 = Date[_0x44962f(332)]() - _0x5c2113;
      log[_0x44962f(228)](_0x44962f(255) + _0x20248a + _0x44962f(291));
      const _0x58fb44 = Date[_0x44962f(332)](), _0x542260 = await electron[_0x44962f(238)][_0x44962f(252)]({ "types": [_0x44962f(274)], "thumbnailSize": { "width": _0x562aa1[_0x44962f(342)][_0x44962f(245)], "height": _0x562aa1[_0x44962f(342)][_0x44962f(297)] } }), _0x3265cc = Date[_0x44962f(332)]() - _0x58fb44, _0xef50b5 = Date[_0x44962f(332)](), _0x18388b = _0x542260[_0x44962f(250)]((_0x4ff424) => _0x4ff424[_0x44962f(347)] === _0x20248a), _0x5f4010 = Date[_0x44962f(332)]() - _0xef50b5;
      if (!_0x18388b) return log[_0x44962f(251)]("[Screenshot] Could not find display at cursor position in sources"), null;
      const _0x5c53f6 = _0x18388b[_0x44962f(287)][_0x44962f(315)]()[_0x44962f(245)], _0x30330d = _0x18388b[_0x44962f(287)][_0x44962f(315)]()[_0x44962f(297)];
      log[_0x44962f(228)](_0x44962f(236) + _0x18388b[_0x44962f(265)] + " (" + _0x5c53f6 + "x" + _0x30330d + ")");
      const _0x672e63 = Date[_0x44962f(332)](), _0x3cdf43 = _0x18388b[_0x44962f(287)][_0x44962f(262)]({ "scaleFactor": 1 }), _0x4e8447 = Date[_0x44962f(332)]() - _0x672e63, _0x16cb8b = Date[_0x44962f(332)]() - _0x460add, _0x4c7854 = Math[_0x44962f(343)](_0x3cdf43[_0x44962f(237)] / 1024);
      return console[_0x44962f(352)]("\n" + "="[_0x44962f(311)](60)), console[_0x44962f(352)](_0x44962f(283)), console[_0x44962f(352)]("="[_0x44962f(311)](60)), console[_0x44962f(352)](_0x44962f(307) + _0x5f5bcc + "ms"), console[_0x44962f(352)](_0x44962f(234) + _0x53c186 + "ms"), console[_0x44962f(352)](_0x44962f(278) + _0x3265cc + "ms"), console[_0x44962f(352)](_0x44962f(230) + _0x5f4010 + "ms"), console[_0x44962f(352)](_0x44962f(312) + _0x4e8447 + "ms"), console[_0x44962f(352)]("─"[_0x44962f(311)](60)), console[_0x44962f(352)](_0x44962f(221) + _0x16cb8b + "ms"), console[_0x44962f(352)](_0x44962f(298) + _0x5c53f6 + "x" + _0x30330d), console[_0x44962f(352)](_0x44962f(247) + _0x4c7854 + "KB"), console[_0x44962f(352)](_0x44962f(337)), console[_0x44962f(352)]("="[_0x44962f(311)](60) + "\n"), _0x3cdf43;
    } catch (_0x42a8dc) {
      return log[_0x44962f(251)](_0x44962f(355), _0x42a8dc), null;
    }
  }
  async [_0x3f500e(226)](_0x1fa0fa = ![]) {
    const _0x2c3b4a = _0x3f500e, _0x5ec192 = Date[_0x2c3b4a(332)]();
    try {
      log[_0x2c3b4a(228)](_0x2c3b4a(357));
      const _0x524c18 = await main[_0x2c3b4a(233)]();
      if (!_0x524c18) return log[_0x2c3b4a(325)]("[Screenshot] Could not detect active window, falling back to full display"), this[_0x2c3b4a(246)](_0x2c3b4a(254));
      const _0x3c0645 = _0x524c18[_0x2c3b4a(293)];
      log[_0x2c3b4a(228)](_0x2c3b4a(304) + _0x524c18[_0x2c3b4a(321)] + _0x2c3b4a(335) + _0x524c18[_0x2c3b4a(319)]), log[_0x2c3b4a(228)](_0x2c3b4a(349) + _0x3c0645["x"] + _0x2c3b4a(219) + _0x3c0645["y"] + _0x2c3b4a(324) + _0x3c0645[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x3c0645[_0x2c3b4a(297)]);
      if (_0x3c0645[_0x2c3b4a(245)] <= 0 || _0x3c0645[_0x2c3b4a(297)] <= 0 || _0x3c0645[_0x2c3b4a(245)] > 1e4 || _0x3c0645[_0x2c3b4a(297)] > 1e4) return log[_0x2c3b4a(325)]("[Screenshot] Invalid window dimensions, falling back to full display"), this[_0x2c3b4a(246)](_0x2c3b4a(254));
      const _0x35a4d3 = electron[_0x2c3b4a(274)][_0x2c3b4a(294)](), _0xb87e15 = electron[_0x2c3b4a(274)][_0x2c3b4a(260)](_0x35a4d3), _0x3f9faf = _0xb87e15[_0x2c3b4a(346)], _0x9a5a12 = _0xb87e15[_0x2c3b4a(338)];
      log[_0x2c3b4a(228)](_0x2c3b4a(340) + _0x3f9faf["x"] + _0x2c3b4a(219) + _0x3f9faf["y"] + _0x2c3b4a(324) + _0x3f9faf[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x3f9faf[_0x2c3b4a(297)] + _0x2c3b4a(302) + _0x9a5a12);
      if (main[_0x2c3b4a(300)](_0x3c0645, _0x3f9faf)) return log[_0x2c3b4a(228)]("[Screenshot] Window is full-screen, capturing entire display"), this[_0x2c3b4a(246)](_0x2c3b4a(254));
      const _0x5779bb = await this[_0x2c3b4a(246)](_0x2c3b4a(254));
      if (!_0x5779bb) return log[_0x2c3b4a(251)]("[Screenshot] Failed to capture full display"), null;
      let _0x90225f = null;
      if (_0x1fa0fa) {
        log[_0x2c3b4a(228)]("[Screenshot] addCaret=true, attempting to get caret bounds...");
        try {
          _0x90225f = await main[_0x2c3b4a(316)](), log[_0x2c3b4a(228)](_0x2c3b4a(354) + JSON[_0x2c3b4a(301)](_0x90225f)), _0x90225f ? log[_0x2c3b4a(228)](_0x2c3b4a(218) + _0x90225f["x"] + _0x2c3b4a(219) + _0x90225f["y"] + _0x2c3b4a(324) + _0x90225f[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x90225f[_0x2c3b4a(297)]) : log[_0x2c3b4a(325)]("[Screenshot] ⚠️ Could not get caret bounds, will crop to window bounds");
        } catch (_0x4d2a9c) {
          log[_0x2c3b4a(251)]("[Screenshot] ❌ Error getting caret bounds:", _0x4d2a9c);
        }
      }
      let _0x525de7, _0x540210 = ![];
      if (_0x90225f) {
        const _0x3fc961 = 30, _0x5ba6c8 = _0x3c0645["y"] - _0x3f9faf["y"], _0x47cac1 = _0x90225f["y"] - _0x3f9faf["y"] + _0x90225f[_0x2c3b4a(297)];
        _0x525de7 = { "x": Math[_0x2c3b4a(253)](0, _0x90225f["x"] - _0x3f9faf["x"] - _0x3fc961), "y": _0x5ba6c8, "width": _0x90225f[_0x2c3b4a(245)] + _0x3fc961 * 2, "height": _0x47cac1 - _0x5ba6c8 + _0x3fc961 }, _0x540210 = !![], log[_0x2c3b4a(228)](_0x2c3b4a(220) + _0x3fc961 + _0x2c3b4a(320) + _0x525de7["x"] + _0x2c3b4a(219) + _0x525de7["y"] + _0x2c3b4a(324) + _0x525de7[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x525de7[_0x2c3b4a(297)]);
      } else _0x525de7 = { "x": _0x3c0645["x"] - _0x3f9faf["x"], "y": _0x3c0645["y"] - _0x3f9faf["y"], "width": _0x3c0645[_0x2c3b4a(245)], "height": _0x3c0645[_0x2c3b4a(297)] }, log[_0x2c3b4a(228)](_0x2c3b4a(344) + _0x525de7["x"] + _0x2c3b4a(219) + _0x525de7["y"] + _0x2c3b4a(324) + _0x525de7[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x525de7[_0x2c3b4a(297)]);
      let _0x1b1af8 = await main[_0x2c3b4a(350)](_0x5779bb, _0x525de7), _0x4b2f53 = !![];
      !_0x1b1af8 && (log[_0x2c3b4a(325)]("[Screenshot] Failed to crop screenshot, using full display"), _0x1b1af8 = _0x5779bb, _0x4b2f53 = ![]);
      if (_0x90225f && _0x1fa0fa && _0x4b2f53) try {
        const _0x5cf3bf = 30, _0x3dca6b = { "x": _0x5cf3bf, "y": _0x90225f["y"] - _0x3c0645["y"], "width": _0x90225f[_0x2c3b4a(245)], "height": _0x90225f[_0x2c3b4a(297)] }, _0x2566f0 = { "x": 0, "y": 0, "width": _0x525de7[_0x2c3b4a(245)], "height": _0x525de7[_0x2c3b4a(297)] };
        _0x1b1af8 = await main[_0x2c3b4a(243)](_0x1b1af8, _0x3dca6b, _0x2566f0), log[_0x2c3b4a(228)]("[Screenshot] 🎯 Caret indicator added around parent element");
      } catch (_0xfb6061) {
        log[_0x2c3b4a(251)]("[Screenshot] ❌ Error adding caret indicator:", _0xfb6061);
      }
      const _0x570c69 = Date[_0x2c3b4a(332)]() - _0x5ec192, _0x4e569c = Math[_0x2c3b4a(343)](_0x1b1af8[_0x2c3b4a(237)] / 1024), _0x18674c = Math[_0x2c3b4a(343)](_0x5779bb[_0x2c3b4a(237)] / 1024), _0x29c6ce = Math[_0x2c3b4a(343)]((_0x18674c - _0x4e569c) / _0x18674c * 100);
      return console[_0x2c3b4a(352)]("\n" + "="[_0x2c3b4a(311)](60)), console[_0x2c3b4a(352)](_0x2c3b4a(286) + (_0x540210 ? _0x2c3b4a(223) : _0x2c3b4a(222)) + ")"), console[_0x2c3b4a(352)]("="[_0x2c3b4a(311)](60)), console[_0x2c3b4a(352)](_0x2c3b4a(331) + _0x524c18[_0x2c3b4a(321)]), console[_0x2c3b4a(352)](_0x2c3b4a(295) + _0x524c18[_0x2c3b4a(319)]), console[_0x2c3b4a(352)](_0x2c3b4a(269) + _0x3c0645[_0x2c3b4a(245)] + "x" + _0x3c0645[_0x2c3b4a(297)]), console[_0x2c3b4a(352)](_0x2c3b4a(276) + _0x3f9faf[_0x2c3b4a(245)] + "x" + _0x3f9faf[_0x2c3b4a(297)]), console[_0x2c3b4a(352)](_0x2c3b4a(323) + _0x525de7["x"] + _0x2c3b4a(219) + _0x525de7["y"] + _0x2c3b4a(324) + _0x525de7[_0x2c3b4a(245)] + _0x2c3b4a(225) + _0x525de7[_0x2c3b4a(297)]), console[_0x2c3b4a(352)](_0x2c3b4a(240) + (_0x540210 ? "focused element" : _0x2c3b4a(235)) + (_0x4b2f53 ? "" : _0x2c3b4a(256))), console[_0x2c3b4a(352)](_0x2c3b4a(224) + (_0x1fa0fa && _0x90225f && _0x4b2f53 ? _0x2c3b4a(258) : _0x2c3b4a(318))), console[_0x2c3b4a(352)](_0x2c3b4a(341) + _0x570c69 + "ms"), console[_0x2c3b4a(352)](_0x2c3b4a(303) + _0x18674c + _0x2c3b4a(241) + _0x4e569c + _0x2c3b4a(310) + _0x29c6ce + _0x2c3b4a(336)), console[_0x2c3b4a(352)]("="[_0x2c3b4a(311)](60) + "\n"), _0x1b1af8;
    } catch (_0x39355b) {
      return log[_0x2c3b4a(251)](_0x2c3b4a(249), _0x39355b), log[_0x2c3b4a(228)]("[Screenshot] Falling back to full display capture"), this[_0x2c3b4a(246)](_0x2c3b4a(254));
    }
  }
  async [_0x3f500e(272)]() {
    const _0x1b2ff5 = _0x3f500e;
    return this[_0x1b2ff5(226)](!![]);
  }
  async [_0x3f500e(330)]() {
    const _0x4afca7 = _0x3f500e, _0x5825b6 = Date[_0x4afca7(332)]();
    try {
      log[_0x4afca7(228)]("[Screenshot] Capturing full WINDOW for AI with red box indicator");
      const _0x2b4bbf = await main[_0x4afca7(233)]();
      if (!_0x2b4bbf) {
        log[_0x4afca7(325)]("[Screenshot] Could not detect active window, capturing full display without crop");
        const _0x234262 = await this[_0x4afca7(246)](_0x4afca7(254));
        return _0x234262 ? { "fullScreenshot": _0x234262, "cropBounds": null } : null;
      }
      const _0x267395 = _0x2b4bbf[_0x4afca7(293)];
      log[_0x4afca7(228)](_0x4afca7(304) + _0x2b4bbf[_0x4afca7(321)] + _0x4afca7(335) + _0x2b4bbf[_0x4afca7(319)]), log[_0x4afca7(228)](_0x4afca7(349) + _0x267395["x"] + _0x4afca7(219) + _0x267395["y"] + _0x4afca7(324) + _0x267395[_0x4afca7(245)] + _0x4afca7(225) + _0x267395[_0x4afca7(297)]);
      if (_0x267395[_0x4afca7(245)] <= 0 || _0x267395[_0x4afca7(297)] <= 0 || _0x267395[_0x4afca7(245)] > 1e4 || _0x267395[_0x4afca7(297)] > 1e4) {
        log[_0x4afca7(325)]("[Screenshot] Invalid window dimensions, capturing full display without crop");
        const _0x438c35 = await this[_0x4afca7(246)](_0x4afca7(254));
        return _0x438c35 ? { "fullScreenshot": _0x438c35, "cropBounds": null } : null;
      }
      const _0x45aaf6 = electron[_0x4afca7(274)][_0x4afca7(294)](), _0x32a9de = electron[_0x4afca7(274)][_0x4afca7(260)](_0x45aaf6), _0x32752a = _0x32a9de[_0x4afca7(346)];
      if (main[_0x4afca7(300)](_0x267395, _0x32752a)) {
        log[_0x4afca7(228)]("[Screenshot] Window is full-screen, capturing entire display without crop");
        const _0xd3d96a = await this[_0x4afca7(246)](_0x4afca7(254));
        return _0xd3d96a ? { "fullScreenshot": _0xd3d96a, "cropBounds": null } : null;
      }
      const _0x1e8b61 = await this[_0x4afca7(246)](_0x4afca7(254));
      if (!_0x1e8b61) return log[_0x4afca7(251)]("[Screenshot] Failed to capture full display"), null;
      const _0x3fac6b = { "x": _0x267395["x"] - _0x32752a["x"], "y": _0x267395["y"] - _0x32752a["y"], "width": _0x267395[_0x4afca7(245)], "height": _0x267395[_0x4afca7(297)] };
      let _0x52ebe3 = await main[_0x4afca7(350)](_0x1e8b61, _0x3fac6b);
      !_0x52ebe3 && (log[_0x4afca7(325)]("[Screenshot] Failed to crop to window, using full display"), _0x52ebe3 = _0x1e8b61);
      log[_0x4afca7(228)](_0x4afca7(259) + _0x267395[_0x4afca7(245)] + "x" + _0x267395[_0x4afca7(297)]);
      let _0x287b2a = null;
      try {
        _0x287b2a = await main[_0x4afca7(316)](), _0x287b2a && log[_0x4afca7(228)](_0x4afca7(216) + _0x287b2a["x"] + _0x4afca7(219) + _0x287b2a["y"] + _0x4afca7(324) + _0x287b2a[_0x4afca7(245)] + _0x4afca7(225) + _0x287b2a[_0x4afca7(297)]);
      } catch (_0x428897) {
        log[_0x4afca7(325)]("[Screenshot] Could not get caret bounds:", _0x428897);
      }
      let _0x13f81f = null;
      if (_0x287b2a) {
        const _0x2a2b8e = 30, _0x53a805 = _0x287b2a["x"] - _0x267395["x"], _0x42e18f = _0x287b2a["y"] - _0x267395["y"], _0x4dfa1a = _0x42e18f + _0x287b2a[_0x4afca7(297)], _0x2faca2 = 24;
        _0x13f81f = { "x": Math[_0x4afca7(253)](0, _0x53a805 - _0x2a2b8e - _0x2faca2), "y": 0, "width": Math[_0x4afca7(309)](_0x287b2a[_0x4afca7(245)] + _0x2a2b8e * 2 + _0x2faca2, _0x267395[_0x4afca7(245)] - Math[_0x4afca7(253)](0, _0x53a805 - _0x2a2b8e - _0x2faca2)), "height": Math[_0x4afca7(309)](_0x4dfa1a + _0x2a2b8e, _0x267395[_0x4afca7(297)]) }, log[_0x4afca7(228)](_0x4afca7(314) + _0x13f81f["x"] + _0x4afca7(219) + _0x13f81f["y"] + _0x4afca7(324) + _0x13f81f[_0x4afca7(245)] + _0x4afca7(225) + _0x13f81f[_0x4afca7(297)]);
      }
      let _0x4ea002 = _0x52ebe3;
      if (_0x287b2a) try {
        const _0x5e7b87 = { "x": _0x287b2a["x"] - _0x267395["x"], "y": _0x287b2a["y"] - _0x267395["y"], "width": _0x287b2a[_0x4afca7(245)], "height": _0x287b2a[_0x4afca7(297)] }, _0x1d6e54 = { "x": 0, "y": 0, "width": _0x267395[_0x4afca7(245)], "height": _0x267395[_0x4afca7(297)] };
        _0x4ea002 = await main[_0x4afca7(243)](_0x52ebe3, _0x5e7b87, _0x1d6e54), log[_0x4afca7(228)]("[Screenshot] 🎯 Added red box indicator to window screenshot");
      } catch (_0x1c963b) {
        log[_0x4afca7(251)]("[Screenshot] Error adding red box indicator:", _0x1c963b);
      }
      const _0x44a724 = Date[_0x4afca7(332)]() - _0x5825b6, _0x1e683a = Math[_0x4afca7(343)](_0x4ea002[_0x4afca7(237)] / 1024);
      return console[_0x4afca7(352)]("\n" + "="[_0x4afca7(311)](60)), console[_0x4afca7(352)]("📸 FULL WINDOW SCREENSHOT FOR AI (with red box + crop coords)"), console[_0x4afca7(352)]("="[_0x4afca7(311)](60)), console[_0x4afca7(352)](_0x4afca7(331) + _0x2b4bbf[_0x4afca7(321)]), console[_0x4afca7(352)](_0x4afca7(295) + _0x2b4bbf[_0x4afca7(319)]), console[_0x4afca7(352)](_0x4afca7(269) + _0x267395[_0x4afca7(245)] + "x" + _0x267395[_0x4afca7(297)]), _0x13f81f ? console[_0x4afca7(352)](_0x4afca7(339) + _0x13f81f["x"] + _0x4afca7(219) + _0x13f81f["y"] + _0x4afca7(324) + _0x13f81f[_0x4afca7(245)] + _0x4afca7(225) + _0x13f81f[_0x4afca7(297)]) : console[_0x4afca7(352)](_0x4afca7(277)), console[_0x4afca7(352)](_0x4afca7(285) + (_0x287b2a ? "added" : "not added (no caret)")), console[_0x4afca7(352)](_0x4afca7(341) + _0x44a724 + "ms"), console[_0x4afca7(352)](_0x4afca7(333) + _0x1e683a + "KB"), console[_0x4afca7(352)]("="[_0x4afca7(311)](60) + "\n"), { "fullScreenshot": _0x4ea002, "cropBounds": _0x13f81f };
    } catch (_0x4c1e1b) {
      return log[_0x4afca7(251)](_0x4afca7(299), _0x4c1e1b), null;
    }
  }
  async [_0x3f500e(284)]() {
    const _0xa7c87b = _0x3f500e, _0x3e8447 = Date[_0xa7c87b(332)]();
    try {
      log[_0xa7c87b(228)](_0xa7c87b(280));
      const _0x48303e = await main[_0xa7c87b(233)]();
      if (!_0x48303e) return log[_0xa7c87b(325)]("[Screenshot] Could not detect active window, falling back to full display"), this[_0xa7c87b(246)](_0xa7c87b(254));
      const _0x3927fc = _0x48303e[_0xa7c87b(293)];
      if (_0x3927fc[_0xa7c87b(245)] <= 0 || _0x3927fc[_0xa7c87b(297)] <= 0 || _0x3927fc[_0xa7c87b(245)] > 1e4 || _0x3927fc[_0xa7c87b(297)] > 1e4) return log[_0xa7c87b(325)]("[Screenshot] Invalid window dimensions, falling back to full display"), this[_0xa7c87b(246)](_0xa7c87b(254));
      const _0x34b1a4 = electron[_0xa7c87b(274)][_0xa7c87b(294)](), _0x4de08e = electron[_0xa7c87b(274)][_0xa7c87b(260)](_0x34b1a4), _0xd96d74 = _0x4de08e[_0xa7c87b(346)];
      if (main[_0xa7c87b(300)](_0x3927fc, _0xd96d74)) return log[_0xa7c87b(228)]("[Screenshot] Window is full-screen, capturing entire display"), this[_0xa7c87b(246)](_0xa7c87b(254));
      const _0x1a59ed = await this[_0xa7c87b(246)](_0xa7c87b(254));
      if (!_0x1a59ed) return log[_0xa7c87b(251)]("[Screenshot] Failed to capture full display"), null;
      const _0x28c3a8 = { "x": _0x3927fc["x"] - _0xd96d74["x"], "y": _0x3927fc["y"] - _0xd96d74["y"], "width": _0x3927fc[_0xa7c87b(245)], "height": _0x3927fc[_0xa7c87b(297)] }, _0x21d57f = await main[_0xa7c87b(350)](_0x1a59ed, _0x28c3a8);
      if (!_0x21d57f) return log[_0xa7c87b(325)]("[Screenshot] Failed to crop, returning full display"), _0x1a59ed;
      const _0x5c7c44 = Date[_0xa7c87b(332)]() - _0x3e8447;
      return log[_0xa7c87b(228)](_0xa7c87b(308) + _0x5c7c44 + "ms"), _0x21d57f;
    } catch (_0xca4691) {
      return log[_0xa7c87b(251)](_0xa7c87b(261), _0xca4691), this[_0xa7c87b(246)](_0xa7c87b(254));
    }
  }
}
function _0x3edc() {
  const _0x45082d = ["🖼️  Convert to data URI:  ", "ScreenshotService", "[Screenshot] Calculated crop bounds (relative to window): x=", "getSize", "getCaretBounds", "console", "disabled", "title", "px padding): x=", "appName", "return (function() ", "📍 Crop bounds: x=", ", w=", "warn", "getMediaAccessStatus", "trace", "systemPreferences", "toString", "captureFullScreenForAI", "🪟 App: ", "now", "💾 Size: ", "apply", " - ", "% reduction)", "🎨 Format:                PNG (lossless)", "scaleFactor", "📍 Crop bounds (relative to window): x=", "[Screenshot] Display bounds: x=", "⚡ Total time: ", "size", "round", "[Screenshot] Crop bounds (window-relative): x=", "granted", "bounds", "display_id", '{}.constructor("return this")( )', "[Screenshot] Window bounds: x=", "cropImage", "getScreenshotService", "log", "1057341LuJPFT", "[Screenshot] getCaretBounds returned: ", "[Screenshot] Error capturing screenshot:", "1135EJbXgj", "[Screenshot] Attempting to capture active window", "sqlite3", "[Screenshot] 🎯 Got caret bounds (screen coords): x=", "Module", "[Screenshot] 🎯 Using REAL caret bounds: x=", ", y=", "[Screenshot] Cropping from window top to element bottom (with ", "⚡ TOTAL SCREENSHOT TIME: ", "WINDOW", "FOCUSED ELEMENT", "🎯 Caret indicator: ", ", h=", "captureActiveWindow", "exception", "info", "prototype", "🔍 Find source:           ", "4580750gtCyTX", "posthog-node", "getActiveWindow", "📺 Display info:          ", "full window", "[Screenshot] Captured screen: ", "length", "desktopCapturer", "44838ZrPguu", "🎯 Crop mode: ", "KB → Cropped: ", "1152808jRfNWN", "addCaretIndicator", "198733JkIDab", "width", "capturePrimaryDisplay", "💾 Size:                  ", "not-determined", "[Screenshot] Error capturing active window:", "find", "error", "getSources", "max", "png", "[Screenshot] Capturing display ID: ", " (crop failed, using full)", "__proto__", "enabled", "[Screenshot] Cropped to window: ", "getDisplayNearestPoint", "[Screenshot] Error capturing full window:", "toDataURL", "constructor", "jpeg", "name", "toStringTag", "2268231WyyCJY", "hasPermission", "📐 Window size: ", "child_process", "2SATkwB", "captureForAI", "compromise", "screen", "platform", "📐 Display size: ", "📍 Crop bounds: none (no caret detected)", "📷 Capture screen:        ", "bind", "[Screenshot] Capturing full active window for Screen tab", "events", "psl", "📸 SCREENSHOT PERFORMANCE BREAKDOWN", "captureFullWindow", "🎯 Red box: ", "📸 SCREENSHOT (CROPPED TO ", "thumbnail", "denied", "defineProperty", "[Screenshot] Screen Recording permission status: ", " (at cursor position)", "../main.js", "position", "getCursorScreenPoint", "📝 Window: ", "1048ZUzXKj", "height", "📐 Resolution:            ", "[Screenshot] Error capturing full window for AI:", "isFullScreenWindow", "stringify", ", scale=", "💾 Original size: ", "[Screenshot] Active window: ", "13434NfjxGM", "table", "⚙️  Permission check:     ", "[Screenshot] Full window capture completed in ", "min", "KB (", "repeat"];
  _0x3edc = function() {
    return _0x45082d;
  };
  return _0x3edc();
}
let screenshotService = null;
function getScreenshotService() {
  return !screenshotService && (screenshotService = new ScreenshotService()), screenshotService;
}
function _0x1b4f(_0x1d32fa, _0x12c942) {
  _0x1d32fa = _0x1d32fa - 215;
  const _0x10d578 = _0x3edc();
  let _0x1879e42 = _0x10d578[_0x1d32fa];
  return _0x1879e42;
}
exports[_0x3f500e(313)] = ScreenshotService, exports[_0x3f500e(351)] = getScreenshotService