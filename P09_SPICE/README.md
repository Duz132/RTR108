# Shēmas zīmēšana un simulācija
Nodarbībā Nr.9 es iepazinos ar GScchem, gnetlist un NGSpice.

## Shēmas zīmēšana (GSchem)
Izmantojot GSchem, es uzzīmēju sprieguma dalītāja shēmu. Ar "Add component" palīdzību, es ievietoju komponentes, pēc tam savienoju tos ar vadiem, ievietoju zemi un katram komponentam norādīju vērtības, pievienojot "Value" vērtību.  

## Elementu-mezglu faila veidošana (gnetlist)
Šīs fails mums ir vajadzīgs, lai veiktu shēmas simulāciju. Fails saturēs elementu vērtības un mezglus pie kuriem šie elementi ir savienoti. Lai izveidotu šo failu es izmantoju gnetlist komandu :  
> gnetlist -g spice -o voltage_divider.net voltage_divider.sch  
voltage_divider.net - fails ar elementu-mezglu sarakstu  
voltage_divider.sch - shēmas fails  

## Shēmas simulācija
Izmantojot NGSpice, es varēju veikt shēmas simulāciju.  
Lai veiktu simulāciju, pirmkārt, vajag konsolē uzrakstīt "ngspice", lai to palaist.  
Otrkārt, vajag uzrakstīt šo komandu :  
> source voltage_divider.net tran solis beigas sākums  
Komanda "tran" veiks transient simulāciju laika posmā.  
Pēc simulācijas veikšanas, vajag izvadīt simulācijas grafikus :
> plot "mezgls"  
> hardcopy faila_nosaukums "mezgls"  
Komanda plot parādīs grafiku, bet komanda hardcopy izvadīs grafiku failā.
