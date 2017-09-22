# text-chains
quick and dirty converter of text into a graph of vocabluary in it


uasge:
```
html2text -width 10000 all_text.htm | sed 's/[\\s_]+/ /g' | sed 's/[.|] /.\n/g' | sort | uniq > all_text.txt
time rm -f graph.dot; python ../make_markov_chain.py < all_text.txt > graph.dot; rm -f graph.png; time dot -Tpng graph.dot > graph.png
```
