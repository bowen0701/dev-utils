# Utility to list and sort PDF files by page count in descending order
.PHONY: count-pages

count-pages:
	@for f in *.pdf; do \
		pages=$$(mdls -name kMDItemNumberOfPages "$$f" | awk -F" = " '{print $$2}'); \
		if [ "$$pages" != "(null)" ] && [ -n "$$pages" ]; then \
			printf "%s\t%s\n" "$$pages" "$$f"; \
		fi; \
	done | sort -rn | awk -F"\t" '{printf "%-4s | %s\n", $$1, $$2}'
