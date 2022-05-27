import pandas as pd
import os

def GDC(request_json):
    try:
        response = {}
        weight = request_json['Cattle_Weight']
        Milking_ltrs=request_json['Milking_ltrs']
        #response["DMI"] = round((weight*2.5/100)+(0.1* Milking_ltrs),3)
        response["DMI"] = round((weight*3/100),3)
        response["per kg milk"]=round((0.5*Milking_ltrs),3)
        response["DMreq"]= round((response["DMI"])+(response["per kg milk"]),3)


        #response["CFML"]=round(1.5+(0.4*Milking_ltrs),3)
        #response["REMDMI"]=round(response["DMI"]-response["CFML"])
        response["CDMI"]= round(response["DMreq"]*1/3,2)
        response["DGDMI"]= round(response["DMreq"]*2/3,2)
        response['DDMI'] = round(response["DGDMI"] * 2/3,2)
        response['GDMI'] =round( response["DGDMI"] * 1/3,2)
        response["Green"] =round(response["GDMI"]/0.2,2)
        response["Dry"] =round(response["DDMI"]/0.90,2)
        response["Concentrate"] =round(response["CDMI"]/0.9,2)
        response["Total_kgs"]=round(response["Green"]+response["Dry"]+response["Concentrate"],3)
        # response["final_concentrate"]=round(response["Total_kgs"]-response["CFML"],3)
        # response["REMKG"]=round(response["Total_kgs"]-response["final_concentrate"],3)
        # response["final_Green"]=round(1/3*(response["REMKG"]),3)
        # response["final_Dry"]=round(2/3*(response["REMKG"]),3)
        

        
        
        response["CA"] =round((0.6/100)* response["DMI"], 2)
        response["P"]  = round(1/3*response["CA"], 2)

        return response
    except Exception as e:
        return str(e)
    