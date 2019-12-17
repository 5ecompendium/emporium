# Emporium

Emporium is a searchable, mobile-friendly 5e magic item shop that organizes items by rarity.

See the latest compiled build here: [https://5ecompendium.github.io/emporium/](https://5ecompendium.github.io/emporium/)

Emporium is forked from [thebombzen/grimoire](https://github.com/thebombzen/grimoire/).

## Structure
Items can be found inside `_items/`. Each item gets its own post, written and stored as a [Markdown](https://daringfireball.net/projects/markdown/basics) file.

To add items, make a new file inside `_items/` for each new item, and copy the formatting from another item.

To add tags, make a new file inside `_tags/` for each new tag, and copy the formatting from another tag.

## Build Instructions
If you've got [Jekyll](https://jekyllrb.com) set up locally, the following should create the build from your friendly command line terminal:
`jekyll serve`