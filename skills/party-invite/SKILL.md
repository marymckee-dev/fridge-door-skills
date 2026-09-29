---
name: party-invite
description: Make a custom digital party invitation, the kind that feels like Paperless Post but is fully yours. It's a sealed envelope with each guest's name on it that opens to a designed card with the details, add-to-calendar buttons, and an RSVP form, published free on Netlify with a link to text or email. Use this whenever someone wants to invite people to a birthday, shower, holiday party, kids' party, dinner, or any event with a link instead of paper, asks to "make an invite," "send a digital invitation," "do an Evite," or wants RSVPs collected, even if they don't mention websites or hosting.
---

# Party invite

You're helping someone, usually not a developer, make a beautiful one-page invitation they can text to guests. The finished product is a folder with an `index.html` (plus any images), which they drag onto Netlify Drop to get a free link. RSVPs land in their Netlify dashboard and can be emailed to them.

The template in `assets/invite-template.html` already works: envelope that opens on tap, the guest's name on the envelope from the link, a card, Google and Apple/Outlook calendar buttons, a map link, and an RSVP form wired to Netlify Forms. Your job is to make it *theirs*: the details, the look, the words. Don't rebuild it from scratch, and don't add a backend, logins, or paid services. The whole point is that a non-technical host can publish and run it alone.

## 1. Get the details (one message, only what's missing)

Pull whatever is already in the conversation first. Then ask for the rest in a single friendly message:

- What's the occasion and whose party (name, and age if it's a birthday)?
- Date, start and end time
- Venue name and address
- Anything guests need to know (costumes, waivers, parking, what to bring, gifts or no gifts)
- RSVP-by date
- How it should be signed ("Love, the Smiths")
- The vibe or theme (colors, a character, "cozy fall," "Pusheen," "elegant"), and any photo or art they want on the card
- Optional: a phone number to show if the RSVP form ever fails

If they don't know the end time, pick a sensible two hours and say so.

## 2. Make it

1. Create a folder named for the party (e.g. `maya-6th-birthday-invite/`) and copy the template into it as `index.html`. The file must be named `index.html` for the link to work.
2. Fill in the `PARTY` block at the top of the script. That's where every detail lives. Change `id` to something unique to this party (it keeps saved RSVPs separate if they reuse the template later).
3. Update the `<title>` and the `og:` tags in the `<head>`. That text is what shows up as the link preview in iMessage. Keep `og:description` under about 85 characters so it doesn't get cut off.
4. Set the look in the `:root` tokens: backdrop, envelope, liner, seal, card, ink and accent colors, plus a display and body font from Google Fonts (update the `<link>` too). Make the palette fit the theme, and check that the text is easy to read on the card. The seal letter is usually the guest of honor's initial.
5. If they gave you art, put the image file in the folder and uncomment the `<img class="art">` line. For a link preview image, a 1200x630 `preview.jpg` plus the `og:image` line makes the text preview look designed; skip it if they don't have one.
6. Words matter more than decoration. Write the details list the way the host talks. Short lines, one idea each.

Preview it by opening `index.html` in a browser. Adding `#open` to the end of the address skips straight to the opened card, and `?to=The+Smith+Family` shows a personalized envelope. The RSVP button won't actually send until it's on Netlify; that's expected.

## 3. Publish it

Walk them through `references/publishing.md` step by step. It covers the free Netlify account, dragging the folder onto Netlify Drop, turning on form detection (easy to miss: without it, RSVPs silently go nowhere), getting RSVP emails, and naming the link. Give them the steps in plain words, not the whole file at once. Stay with them until they've sent one test RSVP and seen it arrive.

## 4. Personal links for each guest

Ask for the guest list early; it's what makes this feel personal. Take it in whatever form they have: pasted names, a spreadsheet, a screenshot of a class list or a group text. For each household you want a **name for the envelope** ("The Rivera Family"), and if they have them, an **email**, a **phone** and the **first name** to greet ("Sam"). Tidy it into a `guests.csv` with the columns `name,first,email,phone`. Don't make them retype anything you can read.

Once the site has its link, run:

```bash
python3 scripts/make_links.py guests.csv https://maya-turns-6.netlify.app "Maya's 6th Birthday"
```

It writes two files next to the CSV:

- `guest-links.csv`: every household with its personal link.
- `send-invites.html`: open it in a browser. Each guest has **Copy link**, **Text** and **Email** buttons that open Messages or Mail with a short note and their link already filled in, and the row fades once sent. This is the easiest way for a host to send thirty invites without copying anything by hand.

Each personal link puts the family's name on the envelope and fills in the RSVP. If you have their email, it's carried in the link too, so the email box disappears and they never type it. Let the host know that means each link is personal: fine to text to that family, not one to post in a group chat. For a group chat, use the plain link with no `?to=`; the envelope says "Friends" and guests type their own details.

## 5. After it's out

- **Who's coming:** Netlify dashboard → their site → **Forms** → **rsvp**. Each reply shows the name, yes/no, how many, email and note. There's a CSV download there too.
- **Changing a detail:** edit `index.html`, then drag the folder onto the site's **Deploys** page again. The link stays the same.
- **A guest changes their answer:** they reopen the link and tap "Change my answer." Both replies will be in the list; the newest one counts.

## Working in the Claude desktop app

Most hosts will be in the Claude desktop app, either in a regular chat or in Cowork. Either way they shouldn't have to touch code, a terminal or file paths.

- **Cowork:** save the invite folder straight into the folder they picked for the session, and tell them its name. Run `make_links.py` yourself.
- **Regular chat:** build the folder, then zip it (`maya-invite.zip`) so they download one file. Tell them to double-click the zip to unzip it, then drag the *folder* onto Netlify Drop. Give them `send-invites.html` as its own download.
- **Show, don't describe.** Once the invite is built, show them what it looks like (a screenshot of the envelope and the opened card) before you talk about publishing. The envelope is the moment that sells it.
- **One step per message** while publishing. Wait for "done" before the next step. If a screen doesn't match the instructions, ask what they see; Netlify moves buttons around.
- **If they have Claude in Chrome**, offer to do the Netlify clicks with them watching. The drag onto Netlify Drop is still theirs to do.
- **Their own email or phone** should never be pre-filled into the invite for guests. That's the host's, and browsers may autofill it on the host's own computer; that's expected and won't show for guests.

## The credit line

The template ends with a small "Made with Fridge Door Skills" line under the card. Leave it in by default; it's how other hosts find the free skill. If the host asks to remove it, remove it, no fuss.

## Things that trip people up

- Netlify Drop sites made without an account disappear after an hour. Have them sign up (free) first.
- Form detection is off on new sites. Turn it on, then redeploy. The test RSVP proves it worked.
- Message apps cache link previews. If they change the preview image, rename it (`preview-2.jpg`) and update the tag.
- Keep it to one page and one folder. Everything the page needs should sit next to `index.html`.
