.NOTINTERMEDIATE:

SVGs=$(subst _pydoto.py,_pydoto.svg,$(shell find . -name "*_pydoto.py"))
all: ${SVGs}

%_pydoto.dot: %_pydoto.py
	python3 $<

%.svg: %.dot
	dot -Tsvg $< -o $@
	@# css can only recognize intrinsic size in px
	@# https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size
	sed -i 's/\([0-9]\+\)pt/\1px/g' $@
