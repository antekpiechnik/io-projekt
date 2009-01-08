io-dokumentacja.pdf: io-dokumentacja.tex
	texi2pdf -q -c io-dokumentacja.tex

clean:
	rm -rf io-dokumentacja.pdf
	rm -rf io-dokumentacja.log
