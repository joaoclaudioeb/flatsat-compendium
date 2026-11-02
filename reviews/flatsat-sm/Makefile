SRC=report
TARGET=flatsat-sm-2023

ifndef BUILD_DIR
	BUILD_DIR=build
endif

all:
	mkdir -p $(BUILD_DIR)
	latexmk -pdf -jobname=$(BUILD_DIR)/$(TARGET) $(SRC).tex
	cp $(BUILD_DIR)/$(TARGET).pdf .

view:
	evince $(TARGET).pdf &

clean:
	rm -rf $(BUILD_DIR)
