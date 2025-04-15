import pylab
x = scipy.linspace(-2,2,1000)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='red')
pylab.fill_between(x, y2, color='red')
pylab.xlim([-2.5, 2.5])
pylab.text(0, -0.4, 'Stack Overflow', fontsize=24, fontweight='bold',
           color='white', horizontalalignment='center')
pylab.savefig('results/heart.png')
plt.title("Sample Chart")
plt.savefig('results/d02d4e1c-5d00-4b73-960d-2d374c8366b7.png')