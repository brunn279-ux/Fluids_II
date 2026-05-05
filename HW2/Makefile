FILE = hw2writeup

pdf: ${FILE}.pdf

${FILE}: ${FILE}.pdf

${FILE}.pdf: *.tex #Figures/*.tex 
	xelatex -halt-on-error ${FILE}.tex
	xelatex -halt-on-error ${FILE}.tex
	xelatex ${FILE}.tex
	#biber ${FILE}
	#xelatex ${FILE}.tex
	#xelatex ${FILE}.tex

clean:
	rm -f ${FILE}.aux ${FILE}.log ${FILE}.dvi ${FILE}.bbl ${FILE}.blg ${FILE}.lo? ${FILE}.locode ${FILE}.toc ${FILE}.brf ${FILE}.idx ${FILE}.ind ${FILE}.ilg ${FILE}.out ${PDFFIGS}

distclean: clean
	rm -f *.bak ${FILE}.pdf ${FILE}.ps 

