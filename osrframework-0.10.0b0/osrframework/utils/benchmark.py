# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import time
# global issues
from multiprocessing import Pool

import logging
import urllib2

def testFunctionWeb():
	'''
		Benchmarcking function...
	'''
	#print p
	resp = urllib2.urlopen('http://www.i3visio.com')
	html = resp.read()
	return 
	
def testFunction2():
	'''
		Benchmarcking function...
	'''
	a = 1
	for i in range(1000):
		a+=1
	return
	
def multi_run_wrapper(args):
	''' 
	Wrapper for being able to launch all the threads of getPageWrapper. 
	Parameters:
		We receive the parameters for getPageWrapper as a tuple.
	'''
	#print args
	return testFunctionWeb(*args)	
	
def doBenchmark(plats):
	'''
		Perform the benchmark...
	'''
	logger = logging.getLogger("osrframework.utils")
	# defining the results dict
	res = {}
	
	# args
	args = []
	
	#for p in plats:
	#	args.append( (str(p),) )
	
	# selecting the number of tries to be performed
	tries = [1, 4, 8 ,16, 24, 32, 40, 48, 56, 64]
	
	#for i in range(1, len(plats)/10):
	#	tries.append(i*10)
	
	logger.info("The test is starting recovering webpages by creating the following series of threads: " + str(tries))
	
	for i in tries:
		print "Testing creating " + str(i) + " simultaneous threads..."
		# starting 
		t0 = time.clock()
		pool = Pool(i)
		# We call the wrapping function with all the args previously generated
		poolResults = pool.map(multi_run_wrapper, args)  
		
		t1 = time.clock()
		# storing the results
		res[i] = t1 - t0
		print str(i) + "\t" + str(res[i]) + "\n"
	
	return res
