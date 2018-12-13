## BETA COMMIT MARKDOWN TABLE SINCE 2018-11-26 21:45:13.184847

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|20|Boris Zbarsky |Bug 1511232 - Adjust test expectations of test_window_define_nonconfigurable.html for non-Trunk trees. a=test-only|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=e9b94ebee2e7)|2018-12-03 17:08:37
|19|Sebastian Hengst |Backed out changeset 8461e2f532ed (bug 1488554) to prevent talos xperf permafailures on 65 beta. a=backout|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=f9bba4d1865f)|2018-10-16 17:26:55
|18|Ryan VanderMeulen |Bug 1500274 - Bump the timeout for Windows opt builds to 3hr to match other PGO-enabled builds. r=me, a=release|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=c9f6bd2a826d)|2018-10-22 12:47:37
|17|Ursula Sarracini |Bug 1510678 - Change recommended addons for Firefox 64 CFR release. r=k88hudson	a=jcristau on a CLOSED TREE  Differential Revision: https://phabricator.services.mozilla.com/D13437|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=e6d60ab6b013)|2018-11-29 17:43:06
|16|André Bargull |Bug 1502530 - Part 2: Update tzdata in ICU data files to 2018g. r=Waldo a=jcristau|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=32d14aa23dce)|2018-11-06 13:18:26
|15|André Bargull |Bug 1502530 - Part 1: Update tzdata updater to use new location. r=Waldo a=jcristau|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9fa720c74bbc)|2018-11-06 10:48:56
|14|Ted Campbell |Bug 1507433 - Avoid shape teleporting if any uncacheable prototypes. r=jandem a=jcristau  These cases are rare and uncacheable prototype shapes are tricky to get right so simplify code instead. The impact is that accessing non-own properties of an object that mutates its prototype will have a few more shape / group guards than are strictly needed.  Differential Revision: https://phabricator.services.mozilla.com/D12806|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=3adefdb368ae)|2018-11-27 13:10:49
|13|Kate Hudson |Bug 1509810 - ASR Snippets: FxA signup template issues. r=ursula a=jcristau  Differential Revision: https://phabricator.services.mozilla.com/D13445|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=41d8ca0ac756)|2018-11-29 17:49:59
|12|Masayuki Nakano |Bug 1510985 - Remove Event.returnValue temporarily in 64. r=smaug a=jcristau  Event.returnValue causes breaking a bank application.  The reason of the breakage is, the web app assumes that Event.returnValue is available only on IE and it hits same incompatibility issue with window.event (bug 1479964). Additionally, the app may be used in various domains including in intranet. Therefore, we cannot disable it with blacklist of domains like other similar changes.  Fortunately, we can ship new keypress event behaviors which is tracked by bug 1479964 in 65.  So, for backward compatibility with 62 or earlier, we should temporarily disable Event.returnValue in 64.  But unfortunately, this was introduced in 63.  So, if some web apps have started to use this legacy attribute, we need to contact their vendors, though.|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=71f7e3ce93e2)|2018-12-03 16:23:38
|11|L10n Bumper Bot |no bug - Bumping Firefox l10n changesets r=release a=l10n-bump CLOSED TREE  ach -> 54d298962cc1 af -> 2daa1b157967 an -> ec236d89eb28 ar -> 964bc00f6186 as -> fed1c0d23345 ast -> 23b736a157f3 az -> c66b02f405b1 be -> 678398ac238d bg -> ed6c844d69f8 bn-BD -> a8d19a066b4b bn-IN -> 42ebfdcd815d br -> 228e1368f405 bs -> 50f26e1e31b3 ca -> 59ca77968770 cak -> 86717f451b28 crh -> removed cs -> 632316dc3720 cy -> cabc3feb28b0 da -> b3ff273f3eea de -> 3d8de7aaf36b dsb -> 4d038664189d el -> 86a3c77b6bb3 en-CA -> 74af9d928404 en-GB -> 27c6db9a76b5 en-ZA -> 87752859e8ce eo -> 979ac6e49f6f es-AR -> 57b14b6ebd69 es-CL -> 13c705a36908 es-ES -> a3404316cfa7 es-MX -> b7bf9308aa06 et -> 844cfe03fb48 eu -> 2ac2cf8943de fa -> 32cda4e06b60 ff -> f5df5ae2ed04 fi -> 1585d5ffd39d fr -> 2f4e31bee6be fy-NL -> 466fb0faecd6 ga-IE -> 8fdfdff5d124 gd -> 70e9447e53aa gl -> 91d52ebf4594 gn -> c15a2dfb7b0e gu-IN -> 65395abb8d3f he -> e82be8609e5c hi-IN -> 3076b2d509e7 hr -> 7a5d889f1aac hsb -> 091136f610b0 hu -> f89d3894545c hy-AM -> a7c08fc03463 ia -> f9b117cb81ad id -> c653179b87ca is -> e9aeb5ac44ed it -> 12bd244ad87a ja -> b08599d9deb8 ja-JP-mac -> 6ab41927967b ka -> f022f1156c33 kab -> 151bb4be90ab kk -> 9568b77c964e km -> c1e0e7fbedf0 kn -> 6dcafc758e3b ko -> 6eaf0fdf1a25 lij -> c23fa6752e4a lo -> removed lt -> ce9ca32dd21a ltg -> removed lv -> d102a9c6cbfa mai -> 5bffe11cc007 mk -> 302a54c71d4e ml -> 5848b2fc2259 mr -> 0393b66a90e0 ms -> 447edd41851e my -> 5483951a9472 nb-NO -> 3ea05cc325d6 ne-NP -> 007654b1710d nl -> e344985f0fb3 nn-NO -> 43d0073c1228 oc -> 396b8174110a or -> 9a9fb050074d pa-IN -> f67a6eddf1b0 pl -> b0fa22405368 pt-BR -> f6921dd61384 pt-PT -> c604ae8a2e4c rm -> 9d623e715f6b ro -> ac56ad2ca3d5 ru -> 109d0a53ca4b si -> 819a515bf6c1 sk -> 7324d7c44ddc sl -> 3f288cbaea3d son -> 2f41bda75b44 sq -> 22288a70d3d5 sr -> 873f1f351b2a sv-SE -> 529f87bf8fe6 ta -> c16d3caf2931 te -> b2b27ade8497 th -> c008316ad61e tl -> removed tr -> 57d07e15f12f trs -> removed uk -> 2057edb7ff1e ur -> 13dc89b098eb uz -> 21bd31fdcc47 vi -> 2d7ffe5defbb wo -> removed xh -> 11f1f1b7fd39 zh-CN -> 4462a11284d9 zh-TW -> e83f0c1dfb7c|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=4d52300fd105)|2018-12-03 16:45:46
|10|L10n Bumper Bot |no bug - Bumping Fennec l10n changesets r=release a=l10n-bump CLOSED TREE  ach -> removed an -> ec236d89eb28 ar -> 2a9a26421acc as -> fed1c0d23345 ast -> 23b736a157f3 az -> 94ea5c5ebddc be -> 678398ac238d bg -> ed6c844d69f8 bn-BD -> a55c8e19f64b bn-IN -> 42ebfdcd815d br -> a23513677e62 bs -> 50f26e1e31b3 ca -> 56c0b7b80bc4 cak -> 86717f451b28 cs -> 1b73602c507b cy -> cabc3feb28b0 da -> d8212826666c de -> f12cddde4128 dsb -> 4d038664189d el -> 86a3c77b6bb3 en-CA -> 74af9d928404 en-GB -> 27c6db9a76b5 en-ZA -> 87752859e8ce eo -> e68fab6e3170 es-AR -> 57b14b6ebd69 es-CL -> 13c705a36908 es-ES -> a3404316cfa7 es-MX -> b7bf9308aa06 et -> 844cfe03fb48 eu -> 3ab606912eee fa -> 32cda4e06b60 ff -> f5df5ae2ed04 fi -> 8c07f989cd32 fr -> 50589eb7144e fy-NL -> 7a077eb453e7 ga-IE -> 8fdfdff5d124 gd -> 7057e1b30fbe gl -> 6698015ca4d7 gn -> c15a2dfb7b0e gu-IN -> 65395abb8d3f he -> e82be8609e5c hi-IN -> 2bfcb7be7b10 hr -> 7a5d889f1aac hsb -> ba155aa11618 hu -> 8014326648c8 hy-AM -> a7c08fc03463 ia -> removed id -> 7fcff9d98ce1 is -> e9aeb5ac44ed it -> 527cef28bac8 ja -> 01d2c65a9ab0 ka -> 23c4fe8080a2 kab -> 0009c05c7b37 kk -> 9568b77c964e km -> removed kn -> 6dcafc758e3b ko -> 6136ee5d3e66 lij -> c23fa6752e4a lo -> 430048d07990 lt -> ce9ca32dd21a ltg -> removed lv -> d102a9c6cbfa mai -> 5bffe11cc007 meh -> removed mix -> removed ml -> 237843b00ffd mr -> 0393b66a90e0 ms -> 3f967b049ed1 my -> b991aa7f72f6 nb-NO -> 3ea05cc325d6 ne-NP -> 007654b1710d nl -> a21d015a8410 nn-NO -> a5dc87c405a2 oc -> 609dc711c007 or -> 9a9fb050074d pa-IN -> f67a6eddf1b0 pl -> b0fa22405368 pt-BR -> f6921dd61384 pt-PT -> 97dab5b5c90f rm -> 9d623e715f6b ro -> 4e9d03685276 ru -> 109d0a53ca4b sk -> 7324d7c44ddc sl -> 3f288cbaea3d son -> 2f41bda75b44 sq -> 22288a70d3d5 sr -> 873f1f351b2a sv-SE -> 3b67ddd7dfd7 ta -> c16d3caf2931 te -> 5a75601675e9 th -> c008316ad61e tl -> removed tr -> b07e2b04c0dd trs -> 3352dad7a578 uk -> 2057edb7ff1e ur -> 13dc89b098eb uz -> 21bd31fdcc47 vi -> 2d7ffe5defbb wo -> 39b918b03c90 xh -> 11f1f1b7fd39 zam -> d89b7e142704 zh-CN -> 4462a11284d9 zh-TW -> 0856f4e244d5|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=dab58e610b02)|2018-12-03 16:45:38
|9|ffxbld |Update configs. IGNORE BROKEN CHANGESETS CLOSED TREE NO BUG a=release ba=release|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=700bed2445e6)|2018-12-03 16:09:57
|8|ffxbld |No bug - Tagging mozilla-beta 36afbf7b676c904b00ec0f032148d98655267c37 with FIREFOX_BETA_64_END a=release DONTBUILD CLOSED TREE|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=cfa5fdffe402)|2018-12-03 16:00:59
|7|ffxbld |Preserve old tags after debugsetparents. CLOSED TREE DONTBUILD a=release|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=7e61c96d2cb3)|2018-12-03 16:00:56
|6|ffxbld |Merge old head via \|hg debugsetparents 60b122ce38e6f529db79fd61db75ee8a8c6f3011 36afbf7b676c904b00ec0f032148d98655267c37\|. CLOSED TREE DONTBUILD a=release|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=bd20cd829604)|2018-12-03 16:00:51
|5|ffxbld |No bug - Tagging mozilla-central 9ad82455dcee2bc1d438e46016b8db00e88758a8 with FIREFOX_BETA_65_BASE a=release DONTBUILD CLOSED TREE|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=60b122ce38e6)|2018-12-03 15:59:35
|4|Boris Zbarsky |Bug 1510689.  Only define IsNonConfigurableReadonlyPrimitiveGlobalProp if we plan to use it.  r=peterv a=Aryx,beta-fix|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9ad82455dcee)|2018-12-03 14:14:15
|3|Margareta Eliza Balazs |Merge inbound to mozilla-central.  a=merge|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=01d0813d8203)|2018-12-03 09:30:40
|2|Daniel Holbert |Bug 1452527: Un-skip reftest svg/outline.html on mac/linux, and mark it as fuzzy in general. (no review, just adjusting test annotation)  The fuzzy() annotation here is using the max-difference from the Windows failures in bug 1452527, and the number-of-mismatching-pixels from mac/linux failures in bug 1503525.|[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=290a2b092c01)|2018-12-03 01:09:25
|1|Jason Laster |Revert "Backed out changeset d0fb1493b28b (bug 1511717) for devtools failures in browser_webconsole_eval_in_debugger_stackframe.js"  This reverts commit fd12a44e915d4e06f4509588ff4667dd9646e2dd. |[URL](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=016950978d66)|2018-12-03 00:33:06

