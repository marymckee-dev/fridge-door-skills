#!/usr/bin/env python3
"""Turn a guest list into personal invite links and a one-click sending page.

Usage:
  python3 make_links.py guests.csv https://maya-turns-6.netlify.app "Maya's 6th Birthday"

guests.csv needs a "name" column (the household name for the envelope, e.g. "The Rivera Family").
Optional columns: "email", "phone", "first" (who the message greets, e.g. "Sam").

Writes, next to the CSV:
  guest-links.csv   name, email, phone, link
  send-invites.html open it in a browser: each guest gets Copy link, Text and Email buttons
"""
import base64, csv, html, json, sys, urllib.parse
from pathlib import Path

def link_for(base, name, email):
    q = {"to": name}
    if email:
        q["e"] = base64.urlsafe_b64encode(email.encode()).decode().rstrip("=")
    return base.rstrip("/") + "/?" + urllib.parse.urlencode(q).replace("%20", "+")

def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, base, title = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
    with src.open(newline="", encoding="utf-8-sig") as f:
        rows = [{k.strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]
    guests = []
    for r in rows:
        if not r.get("name"):
            continue
        g = {"name": r["name"], "email": r.get("email", ""), "phone": r.get("phone", ""),
             "first": r.get("first", "")}
        g["link"] = link_for(base, g["name"], g["email"])
        guests.append(g)

    out_csv = src.with_name("guest-links.csv")
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "email", "phone", "link"])
        for g in guests:
            w.writerow([g["name"], g["email"], g["phone"], g["link"]])

    page = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Send invites: %(t)s</title><style>
body{font:16px/1.5 system-ui,sans-serif;margin:0;background:#faf7f2;color:#2b2b2b;padding:28px 16px}
main{max-width:760px;margin:auto}h1{font-size:24px;margin:0 0 4px}p.sub{color:#666;margin:0 0 20px}
.row{background:#fff;border-radius:12px;padding:14px 16px;margin:10px 0;display:flex;flex-wrap:wrap;gap:10px;align-items:center;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.who{flex:1 1 220px}.who b{display:block}.who span{color:#777;font-size:14px}
a.b,button.b{border:0;border-radius:999px;padding:9px 14px;font:600 14px system-ui;cursor:pointer;text-decoration:none;background:#eee;color:#222}
.b.go{background:#222;color:#fff}.done{opacity:.45}
</style></head><body><main><h1>Send invites</h1><p class="sub">%(t)s &middot; %(n)d guests. Tap a button, send, and the row fades so you know who's done.</p>
<div id="list"></div></main><script>
var G=%(g)s, TITLE=%(tj)s;
function msg(g){return (g.first?"Hi "+g.first+"! ":"Hi! ")+"You're invited to "+TITLE+". Here's your invitation: "+g.link;}
var list=document.getElementById("list");
G.forEach(function(g,i){
  var r=document.createElement("div");r.className="row";
  var who=document.createElement("div");who.className="who";
  who.innerHTML="<b></b><span></span>";who.querySelector("b").textContent=g.name;
  who.querySelector("span").textContent=[g.email,g.phone].filter(Boolean).join(" \\u00b7 ");
  r.appendChild(who);
  var c=document.createElement("button");c.className="b";c.textContent="Copy link";
  c.onclick=function(){navigator.clipboard.writeText(g.link);c.textContent="Copied!";r.classList.add("done");};
  r.appendChild(c);
  if(g.phone){var t=document.createElement("a");t.className="b go";t.textContent="Text";
    t.href="sms:"+g.phone.replace(/[^0-9+]/g,"")+"?&body="+encodeURIComponent(msg(g));t.onclick=function(){r.classList.add("done");};r.appendChild(t);}
  if(g.email){var m=document.createElement("a");m.className="b go";m.textContent="Email";
    m.href="mailto:"+g.email+"?subject="+encodeURIComponent("You're invited: "+TITLE)+"&body="+encodeURIComponent(msg(g));
    m.onclick=function(){r.classList.add("done");};r.appendChild(m);}
  list.appendChild(r);
});
</script></body></html>""" % {"t": html.escape(title), "n": len(guests), "g": json.dumps(guests), "tj": json.dumps(title)}
    out_html = src.with_name("send-invites.html")
    out_html.write_text(page, encoding="utf-8")
    print(f"{len(guests)} guests -> {out_csv.name}, {out_html.name}")

if __name__ == "__main__":
    main()
