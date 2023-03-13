# LingueeFront
Alternative Native Frontend for Linguee. Made by a Vim lover.

The code is not great (I know, maybe someday I will put more effort, it was also my first time using QT, so maybe some solutions are a bit janky), but it just works and for anyone who despises Linguee's web interface it is a considerable step up.
## Credits to imankulov who made Linguee-api
https://github.com/imankulov/linguee-api
This is the heart behind the app that does all the query fetching, caching, stuff like that, there are only slight modifications made, so that if the query gets corrected, there is information about it on the command output.
## Modes:
Browse activated by escape (basically equivalent to normal mode)
Search activated by i or a or d+(i/a) for deleting the current query beforehand

## Keybindings:
### Browse mode:
- j/k — up/down
- G — bottom
- gg — top
- c — change colorscheme black/white, black by default

### Search mode:
- you can use Ctrl+a to select whole query and type in something to substitute it haha
