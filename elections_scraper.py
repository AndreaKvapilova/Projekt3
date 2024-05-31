import csv
import sys
import threading
from queue import Queue
import function

def main():
    #control arguments: the number -> arg[0] - script name, arg[1] - territorial unit url, arg[2] - name of csv file
    if len(sys.argv) != 3: #control number of argument
        print("The script needs two arguments! The first is the url of the territorial unit, the second is <filename>.csv")
        return
    
    # get arguments to variable from the command line
    url = sys.argv[1]
    file_name = sys.argv[2]

    if not file_name.endswith(".csv"): #control format if it is csv file
        print("Output file input error. Specify the required file name and .csv extension. E. g. prostejov.csv ")
        return
    elif not url.startswith("http"): # control format of url address
        print('Problem with url parameter. Insert like e. g. "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103"')
        return

    #getting the source url
    response = function.get_html_content(url)

    #create soup
    list_municipality_names = function.create_bs_findall_list(response, 'td', 'class','overflow_name')
    code_list = function.create_bs_findall_list(response, 'td', 'class', 'cislo')
    base_url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    print("Preparing beautiful soup, please wait.")

    #creating treads to speed up downloading of municipalities
    threads = []
    result_queue = Queue() #for saving results from threads

    for index, municipality_name in enumerate(list_municipality_names):
        thread = threading.Thread(target=function.process_municipality_soup, args=(municipality_name, code_list[index], base_url, result_queue))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    #saving the results of individual municipalities from threads to csv
    try:
        with open(file_name, mode='a', newline='', encoding='utf-8-sig') as csvfile:
            while not result_queue.empty():
                municipality_record = result_queue.get()    
                values = [item[1] for item in municipality_record] #prepare values for write
                writer = csv.writer(csvfile)

                if csvfile.tell() == 0: 
                    headers = [item[0] for item in municipality_record] #prepare headers for write
                    writer.writerow(headers)

                writer.writerow(values)
        print(f"File {file_name} was successfully created.")
    except IOError as e: 
        print(f"Error writing to file {e}")        

if __name__ == '__main__':
    main()
