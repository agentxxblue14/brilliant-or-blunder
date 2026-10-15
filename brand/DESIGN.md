# Brilliant or Blunder design system

Read this whole file before designing anything for this brand. Every colour, font, radius and motion value comes from here or from `tokens.css`. If something is not covered, ask Judah instead of choosing. This file sets the look, not the ambition.

- Brand: Brilliant or Blunder (renamed from Checkmate Cinema on 11 Oct 2026 after the client, Isaac, chose the name). YouTube channel reviewing famous movie and TV scenes (later also courtroom and interrogation scenes) like chess games, every line graded Brilliant to Blunder. Handle @BrilliantOrBlunderTV (@brilliantorblunder is taken). Tagline: "Movie and TV scenes, graded move by move like chess."
- Source: set 11 Oct 2026 from the brand kit (`Videos\analysed-like-chess\CHECKMATE CINEMA - Brand Kit.txt`) and the reference channel @analysedlikechess (avatar, banner, thumbnails and videos studied 10 Oct). No website. Values are chosen, not sampled; the grade colours are the ones used in EP01.

## Colour
| Role | Hex | Use |
|---|---|---|
| Night | #141312 | deepest ground, banner edges |
| Ink | #262421 | brand charcoal: avatar disc, panels |
| Panel | #2C2925 | spotlight centre, raised surfaces |
| Gold (the one accent) | #E8B04A | "or" in the wordmark, knight, highlights |
| White | #FFFFFF | wordmark, white king, badge symbols |
| Mist | #B9B4AC | tagline and secondary text on dark |
| Brilliant | #26C2A3 | the !! badge (winner) |
| Blunder | #D63A2F | the ?? badge (loser) |

Other grade colours (in video only): Great #5C8BB0, Best #81B64C, Excellent #96BC4B, Good #95AF8A, Book #A88764, Inaccuracy #F0C15C, Mistake #E58F2A.
Always dark grounds. Measured 11 Oct: Gold on Ink 7.9:1, White on Ink 15.5:1, Mist on Night 9.0:1, Mist on Ink 7.5:1 (all AA at any size). White on Brilliant is only 2.3:1 and White on Blunder 4.7:1, so the badges carry big graphic symbols only, never small text.

## Type
- Display: Anton, uppercase only, letter spacing about 0.015em. Wordmark, video titles on cards, end cards.
- Text: Inter 400 to 700. Tagline, move cards, subtitles.
- Badge symbols (!!, ??): Anton in the logo and banner; Arial Bold on thumbnails.
- 1920x1080 video: subtitles Inter 700 52px; card title Inter 700 38px; body Inter 400 31px.
- 2560x1440 banner: wordmark Anton 120px on two lines (CHECKMATE / CINEMA); tagline Inter 500 36px.

## Shape, space, elevation
Round is the brand shape: circular avatar, circular grade badges. Cards radius 14px. Soft drop shadow only (0 8px 24px black at 45 to 60%). Warm glow behind the wordmark (gold at 20 to 35%), no other glows.

## Components
- Grade badge: circle, grade colour, white symbol, thin Night ring when it sits on an image.
- Move card (video): mid-right, Panel at 94%, 7px left bar in the grade colour, title "[Move] is brilliant", grey line "N Name · Move", body, theme tag.
- Thumbnail: two faces split by a white line, !! badge on the winner, ?? badge on the loser, no text.

## Imagery
Real frames from the scene being reviewed, brightened slightly. Never stock photos, never generated faces of real actors.

## Logo (11 Oct 2026, v1)
Files in `logo\` (copy in `Videosnalysed-like-chessrand-brilliant-or-blunder`, and in Downloads as "AVATAR - Brilliant or Blunder 800x800.png" and "BANNER - Brilliant or Blunder 2560x1440.jpg"):
- `brilliant-or-blunder-avatar.svg/.png` (800x800): Ink disc in a soft spotlight with a thin gold rim, gold knight (kept from Checkmate Cinema), outer ring split teal (upper right, Brilliant) and red (lower left, Blunder), teal !! badge at 1:30 and red ?? badge at 7:30.
- `brilliant-or-blunder-mark-plain.svg`: same without badges.
- `brilliant-or-blunder-banner-2560x1440.jpg` and editable `.html`: one-line Anton wordmark, BRILLIANT teal, "or" gold, BLUNDER red, tagline in Mist with the gold half, !! and ?? badges either side, faint checkerboard fading to the edges. Everything inside the 1546x423 safe area.
- Builders: `_srcvatar.py` and `_srcanner.html`, rendered with headless Chrome (needs a fresh --user-data-dir per run or it silently keeps the old PNG).
The old Checkmate Cinema logo and banner stay in `Documents\Design Systems\checkmate-cinema`.
Never use the reference channel's "subscribe (it's your only legal move.)" pixel banner.

## Motion
Badges pop in with a slight overshoot (back.out), cards slide 40px from the right in 0.3s, the scene dims to 50% on a freeze. Signature move: freeze plus dim plus badge pop on every graded move.

## Voice
Plain, sharp, a little playful, chess words used literally: "Brilliant", "Blunder", "the engine line", "Lecter wins on the board". Main call to action: "Which move would you grade differently?" Never: "Analysed like Chess" (the other channel's name), hype words like "insane" or "mind-blowing".

## Never
- Their teal !!-only avatar or their "subscribe" banner.
- Light or cream grounds.
- All caps eyebrow labels above headings, middle dot chains as decoration, pill buttons.
- More than one accent colour outside the grade badges.
- Em dashes or en dashes in any rendered text.

## References
- @analysedlikechess avatar: one bold game-review symbol is the whole identity (we keep the badge, add the knight and film ring).
- @analysedlikechess banner: dark ground, two kings, soft glow (we keep the kings, add the verdict badges and the wordmark).
- Chess game-review screens: grade colours and the !! / ?? language.
- Cinema: spotlight from above, the film strip, the poster wordmark stacked on two lines.
