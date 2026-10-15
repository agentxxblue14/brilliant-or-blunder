# Brilliant or Blunder avatar: ink disc, ring split teal (brilliant) / red (blunder), gold knight, !! and ?? badges.
import re, math
src = open(r'../../checkmate-cinema/logo/checkmate-cinema-avatar.svg', encoding='utf-8').read()
knight = re.search(r'<g transform="translate\(98.0,635.6\) scale\(0.62,-0.62\)">.*?</g>', src, re.S).group(0)
def arc(r, a0, a1):
    p = lambda a: (400 + r*math.cos(math.radians(a)), 400 + r*math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}'
def badge(cx, cy, r, col, sym):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#141312" stroke-width="14"/>'
    if sym == '!!':
        for dx in (-26, 26):
            s += f'<path d="M{cx+dx-14} {cy-58} h28 l-4 74 h-20 z" fill="#fff"/><rect x="{cx+dx-13}" y="{cy+28}" width="26" height="26" rx="5" fill="#fff"/>'
    else:
        s += f'<text x="{cx}" y="{cy+40}" text-anchor="middle" font-family="Anton" font-size="128" fill="#fff" letter-spacing="-4">??</text>'
    return s
def svg(badges=True):
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">',
           '<defs><style>@font-face{font-family:Anton;src:url(Anton-Regular.ttf)}</style>'
           '<radialGradient id="spot" cx="50%" cy="38%" r="55%"><stop offset="0" stop-color="#3a352d"/><stop offset=".6" stop-color="#262421"/><stop offset="1" stop-color="#141312"/></radialGradient></defs>',
           '<circle cx="400" cy="400" r="400" fill="#141312"/>',
           # split ring: teal upper-right half, red lower-left half, thin gold seams
           f'<path d="{arc(365, -135, 45)}" stroke="#26C2A3" stroke-width="70" fill="none"/>',
           f'<path d="{arc(365, 45, 225)}" stroke="#D63A2F" stroke-width="70" fill="none"/>',
           '<circle cx="400" cy="400" r="330" fill="url(#spot)" stroke="#E8B04A" stroke-width="8"/>',
           knight,
           '<ellipse cx="400" cy="642" rx="150" ry="14" fill="#000" opacity=".35"/>']
    if badges:
        out.append(badge(612.1, 187.9, 105, '#26C2A3', '!!'))
        out.append(badge(187.9, 612.1, 105, '#D63A2F', '??'))
    out.append('</svg>')
    return '\n'.join(out)
open('../logo/brilliant-or-blunder-avatar.svg', 'w', encoding='utf-8').write(svg(True))
open('../logo/brilliant-or-blunder-mark-plain.svg', 'w', encoding='utf-8').write(svg(False))
open('avatar.html', 'w', encoding='utf-8').write('<html><body style="margin:0;background:transparent">' + svg(True).replace('url(Anton-Regular.ttf)', 'url(Anton-Regular.ttf)') + '</body></html>')
