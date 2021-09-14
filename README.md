# Newsched Example OOT

## Dependencies

```
meson
ninja
```

## Building
```
meson setup build
cd build
ninja
ninja install
ninja test
```
Currently ninja test won't work without first installing due to the relative import from the newsched package.  Newsched needs some python magic to make the disjoint relative import work
