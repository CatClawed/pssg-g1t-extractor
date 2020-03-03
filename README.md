# pssg-g1t-extractor
Extracts G1T files from a PSSG file. Works for very specific games.

* Atelier Rorona DX
* Atelier Totori DX
* Atelier Meruru DX
* Atelier Ayesha DX

These games are all ports of games previously made in PhyreEngine. They maintain the PSSG format, but ditch the DDS files that were previously inside in favor of Koei Tecmo's proprietary G1T texture format.

This is a very dumb, specialized extractor; use Ego PSSG Editor for anything with DDS files inside. It's frankly not designed with failure in mind. If you want to repack for modding, Ego will probably do it for you.

I only vaguely understand what I'm doing. Which is to say, I skip the entire beginning of the PSSG and don't bother interpreting it at all, but I learned how to extract what I want.
