from text_analysis import analyze_text
from file_operations import read_text_from_file, write_results_to_file, archive_results

def main():
    source_filename = 'source_text.txt'
    output_filename = 'analysis_results.txt'

    text = read_text_from_file(source_filename)
    results = analyze_text(text)
    write_results_to_file(output_filename, results)
    info = archive_results(output_filename)

    print("Analysis and archiving completed successfully.")

if __name__ == "__main__":
    main()