def viivanleveys(x_list, y_list, first=True):
    """
    Laskee kaksi maksimia sisältävän funktion ensimmäisen tai toisen piikin viivanleveyden, 
    jos piikit ovat jakautuneet x-akselin keskipisteen molemmille puolille.
    
    TODO: Muokkaa siten että molemmille puolille jakautumista ei tarvita

    Parameters
    ----------
    x_list : List
        Funktion x-akselin pisteet
    y_list : List
        Funktion y-akselin pisteet
    first : Boolean
        True jos halutaan ensimmäisen piikin viivanleveys muutoin false

    Returns
    -------
    fullwidthathalfmax : Double
        FWHM viivanleveys ja paikka y-akselilla

    """
    n = len(x_list) 
    x_1, x_2 = np.split(x_list, 2)
    y_1, y_2 = np.split(y_list, 2)
    if first == False:
        y = y_1
        x = x_1
        position = 0
    else:
        y = y_2
        x = x_2
        position = int(n/2)
    
    if y[np.abs(y).argmax()] < 0:
        halfmax_y = y.min() / 2
        maxpos_y = y.argmin()
        leftpos_y = (np.abs(y[:maxpos_y] - halfmax_y)).argmin()
        rightpos_y = (np.abs(y[maxpos_y:] - halfmax_y)).argmin() + maxpos_y
        FWHM = x[rightpos_y] - x[leftpos_y]
    else:
        halfmax_y = y.max() / 2
        maxpos_y = y.argmax()
        leftpos_y = (np.abs(y[:maxpos_y] - halfmax_y)).argmin()
        rightpos_y = (np.abs(y[maxpos_y:] - halfmax_y)).argmin() + maxpos_y
        FWHM = x[rightpos_y] - x[leftpos_y]
    return FWHM, x_list[position+maxpos_y]