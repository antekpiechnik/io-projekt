io-dokumentacja.pdf: io-dokumentacja.tex
	texi2pdf -c io-dokumentacja.tex

clean:
	rm -rf io-dokumentacja.pdf
