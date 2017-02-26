#!/usr/bin/env python
from django.shortcuts import render
from django.contrib import messages
from .forms import NumberForm

def primes(n):
	""" Returns  a list of primes < n """
	sieve = [True] * n
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in range(3,n,2) if sieve[i]]

def index(request):
	count_primes = 0
	list_primes = []
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NumberForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			inputs = form.cleaned_data['input_number']
			try:
				list_primes = primes(inputs)
				count_primes = len(list_primes)
			except (MemoryError, OverflowError) as e:
				messages.warning(request, 'The number is too large. Maximum allowed 10,000,000.')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NumberForm()

	return render(request, 'primes/home.html', {'Count_Primes': count_primes, 'List_Primes': list_primes, 'form': form})