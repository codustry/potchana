![Potchana Logo](https://github.com/codustry/potchana/raw/master/Design%20materials/potchana-ogp.png)
https://www.codustry.com/potchana/images/potchana-ogp.png
# Potchana
An open source worldwide languages dictionary plug-in for Mac.

The name **“Potchana”** comes from a full name **“Potchananukrom (พจนานุกรม)”** which means dictionary in the Thai language. It is Thai-based dictionary plug-in for dictionary.app which means it’s translate from and to Thai from languages around the world.

Potchana was designed to works on dictionary.app which developed by Apple so its only works on Macintosh computer. We are using a bunch of database of the dictionary from many sources in different formats. We translate that format and make it clean. Then we create an installer which includes all of the languages for the user to install the dictionary on their computer easily.

The problem that makes us want to do Thai-based dictionary for Mac is because many of us are users of StarDict in Linux and they have great dictionaries but in macOS, there is none who can get this language on Mac. The only dictionary that works but not as good as it should be is developed by NECTEC called “Lexitron” which provides Thai-English & English-Thai dictionaries.

We have expands our view to not focusing on the Thai language itself but worldwide languages to make Potchana one of the best dictionary plug-ins in Apple environment.

## Dictionary Resources
- Thai-Thai by Thai Royal Institution. http://rirs3.royin.go.th/
- Thai-Japanese JTDIct (Paitoon Sae Tung). http://www.jtdic.com/
- Thai-English by NECTEC, Thailand’s national technology agency. http://www.nectec.or.th
- Thai-Korean by Korean-Thai Organization. https://sites.google.com/site/thaidictproject/
- Thai-ChineseDic2U. http://dict2u.com
- Thai-German by German-Thai Organization. http://www.german-thai.org
- Thai-Russian by ThaiDictProject. https://sites.google.com/site/thaidictproject/o-transkripcii
- Thai-French Charles Degnau. http://www.francais-thai.com/

## To build this yourself
Look at the readme of pyglossary repo.(e.g. Format-specific Requirements)
You may use `utils/*` to help and guide you.

```
pyglossary INPUT_FILE OUTPUT_FILE -v3
mydic.ifo txt
```

## License & Credits
**Codustry Laboratory** is not the owner of the dictionary database.
We are only converter and distributer of the dictionary. We do not own any dictionary licenses.

We’re using dictionary database from these developers
-	https://sites.google.com/site/thaidictproject/
-	http://www.babylon-software.com/free-dictionaries/

We’re using dictionary converter from this developer
-	https://github.com/ilius/pyglossary

We’re using installer tools from this developer
- http://s.sudre.free.fr/Packaging.html

Anymore questions regarding to license please contact us at [support@codustry.com](support@codustry.com)

## Developers
- Thunpisit Amnuaikiatloet - Developer & UI/UX Designer
- Nutchanon Ninyawee - Software Engineer
- Harit Chokthananuchit - Requiment Engineer

Any questions or suggestions please contact us via [hello@codustry.com](hello@codustry.com)
