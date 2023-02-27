#!usr/bin/perl


sub clear {
    system("clear")
}

sub geoscan {
    print "What is the IP address you would like to scan:\n";
        my $ip = <>;
        chomp ($ip);
    system("curl ipinfo.io/$ip > scrp/tmp/geooutput1.csv");
    clear();
    system("awk 'NR>3' scrp/tmp/geooutput1.csv | head -n -2 | sed 's/://' | sed 's/,//' > scrp/tmp/geooutput.csv");
    system("rm -rf scrp/tmp/geooutput1.csv");
    system("cat scrp/tmp/geooutput.csv");
        print "\nWould you like to save this output? (y/n)"
            my $choice = <>;
            chomp ($choice);
            my $choicelower = lc($choice);
            if ($choicelower = "y"){
                system("cp -r scrp/geooutput.csv backups/");
                system("rm -rf scrp/geoouput.csv");
            }else{
                system("rm -rf scrp/geoouput.csv");
            }
}

geoscan();