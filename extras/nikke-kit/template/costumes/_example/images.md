# <Name> image & asset sources (this costume/variant only)
> Links only — never commit images/models. List EVERY known source: full-body, portrait, cover pose, aim pose, sprite icon, gallery, wiki image pages, Live2D/Spine raw files (.skel/.atlas/.png + model id) and viewer link.
> Bot fetch rule: 1) check the local cache path; 2) if missing, download to it (`/workspace/<franchise>-assets/<char>/<costume>/`, Live2D under `live2d/<costume>/`); 3) add/update the row in `/workspace/<franchise>-assets/MANIFEST.md` and the Fetched date here; 4) keep the cache, never commit it.
> Live2D/Spine and datamined assets are a legal/ToS gray area: list as options; download only if the user decided to.

| Type | Pose | URL | Local cache path | Fetched |
|---|---|---|---|---|
| official art | full-body | <direct URL> | /workspace/<franchise>-assets/<char>/<costume>/<file> | <YYYY-MM-DD> |
| official art | portrait | <url> | — | — |
| official art | cover pose | <url> | — | — |
| official art | aim pose | <url> | — | — |
| sprite icon | icon | <url> | — | — |
| wiki page | page | <url> | — | — |
| gallery | various | <url> | — | — |
| Live2D/Spine <model-id> | main/cover/aim | <raw .skel/.atlas/.png URL> | /workspace/<franchise>-assets/<char>/live2d/<costume>/<file> | — |
| Spine viewer | interactive | <url> | — | — |

> Live2D/Spine: community viewer `<viewer_url>` (check for deep links; else "select in UI"). Model id cXXX_NN; main + cover/ + aim/ each .skel/.atlas/.png; Spine 4.0 or 4.1 (version in .skel header). Gray zone, download only on user decision. See GUIDE.md.
> Online viewers: list each `<viewer_url>` and whether it deep-links. See sources.md.
