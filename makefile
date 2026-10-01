

# Variables
CC = gcc
CFLAGS = -Wall -Wextra -O2
LDLIBS = -lm
TARGET = myprogram
SRC = Nbody/Nbody/compare_gal_files/compare_gal_files.c

# Define the 5 specific pairs of files you want to run together.
# Each line is one run, containing "file_from_folder1 file_from_folder2".
# Keep the quotes around each pair so the loop treats them as a single unit!
FILE_PAIRS = \
    "10 Nbody/Nbody/ref_output_data/ellipse_N_00010_after200steps.gal Nbody/Nbody/result_output/ellipse_N_00010_output.gal" \
	"100 Nbody/Nbody/ref_output_data/ellipse_N_00100_after200steps.gal Nbody/Nbody/result_output/ellipse_N_00100_output.gal" \
	"500 Nbody/Nbody/ref_output_data/ellipse_N_00500_after200steps.gal Nbody/Nbody/result_output/ellipse_N_00500_output.gal" \
	"1000 Nbody/Nbody/ref_output_data/ellipse_N_01000_after200steps.gal Nbody/Nbody/result_output/ellipse_N_01000_output.gal" \
#	"2000 Nbody/Nbody/ref_output_data/ellipse_N_02000_after200steps.gal Nbody/Nbody/result_output/ellipse_N_02000_output.gal"

# Default target
all: $(TARGET)

# Compile the C program
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDLIBS)

# Run the program 5 times with specific pairs
run-specific: $(TARGET)
	@echo "Running the 5 specific file pairs..."
	@for pair in $(FILE_PAIRS); do \
		echo "----------------------------------------"; \
		echo "Executing: ./$(TARGET) $$pair"; \
		./$(TARGET) $$pair; \
	done

# Clean up compiled files
clean:
	rm -f $(TARGET)