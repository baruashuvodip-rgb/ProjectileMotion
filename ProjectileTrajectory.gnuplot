set term pdfcairo color enhanced font "Times-New-Roman,14" size 5,3
set output "projectileTrajectoryGNU.pdf"
set xlabel "{/Times-New-Roman-Italic x} (m)"
set ylabel "{/Times-New-Roman-Italic y} (m)"
plot "Pmotion_output.txt" using 2:3 notitle with lines lw 2
unset output