#!/usr/bin/env python3

import sys
import os

wd = os.path.dirname(os.path.realpath(__file__))
p  = os.path.dirname(wd)
sys.path.append(p)

import chess
import chess.pgn

import ankichess

def test_get_game_1():
	print("Testing ankichess.get_game(../pgn/mates.pgn, 1): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "mates.pgn")
	game = ankichess.get_game(file_name, 1)
	expected = ["f3", "e6", "g4", "Qh4#"]
	for e, n in zip(expected, ankichess.iterate(game, True)):
		if e != n.san():
			print("Failed")
			return
	print("Passed")

def test_get_game_2():
	print("Testing ankichess.get_game(../pgn/mates.pgn, 2): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "mates.pgn")
	game = ankichess.get_game(file_name, 2)
	expected = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7#"]
	for e, n in zip(expected, ankichess.iterate(game, True)):
		if e != n.san():
			print("Failed")
			return
	print("Passed")

def test_iterate_mainline():
	print("Testing ankichess.iterate(italian_game, mainline=True): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "italian.pgn")
	game = ankichess.get_game(file_name, 1)
	moves = list(ankichess.iterate(game, mainline=True))
	if len(moves) != 17:
		print("Failed")
		return
	print("Passed")

def test_iterate():
	print("Testing ankichess.iterate(italian_game, mainline=False): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "italian.pgn")
	game = ankichess.get_game(file_name, 1)
	moves = list(ankichess.iterate(game, mainline=False))
	if len(moves) != 23: # the heads of alt lines are popped off
		print("Failed")
		return
	print("Passed")

def test_notation_data():
	print("Testing ankichess.notation_data(fools_mate): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "mates.pgn")
	game = ankichess.get_game(file_name, 1)
	expected = ( ("1. ?", "1.f3"), ("1... ?", "1... e6"),
	             ("2. ?", "2.g4"), ("2... ?", "2... Qh4#") )
	cards = list(ankichess.notation_data(game))
	if len(expected) != len(cards):
		print("Failed")
		return
	for e, c in zip(expected, cards):
		if e != c:
			print("Failed")
			return
	print("Passed")

def test_image_data():
	print("Testing ankichess.image_data(fools_mate): ", end="", flush=True)
	def write_svg(game_node):
		test_image_data.h+=1
		return test_image_data.h
	ankichess.write_svg = write_svg
	file_name = os.path.join(p, "pgn", "mates.pgn")
	game = ankichess.get_game(file_name, 1)
	expected = ( (1,2), (3,4), (5,6), (7,8) )
	cards = list(ankichess.image_data(game, mainline=True))
	if len(expected) != len(cards):
		print("Failed")
	for e, c in zip(expected, cards):
		if e != c:
			print("Failed")
			return
	print("Passed")
test_image_data.h=0

def test_mainline_forced():
	print("Testing ankichess.iterate(fools_mate, mainline=False) (only mainline exists): ", end="", flush=True)
	file_name = os.path.join(p, "pgn", "mates.pgn")
	game = ankichess.get_game(file_name, 1)
	moves = list(ankichess.iterate(game, mainline=False))
	if len(moves) != 4:
		print("Failed")
		return
	print("Passed")

def test_get_game_bounds():
	print("Testing ankichess.get_game(../pgn/mates.pgn, [-1,0,3]) :", end="", flush=True)
	file_name = os.path.join(p, "pgn", "mates.pgn")
	values = [ -1, 0, 3]
	for i in values:
		try:
			game = ankichess.get_game(file_name, i)
			print("Failed")
			return
		except RuntimeError:
			pass
	print("Passed")

if __name__ == "__main__":
	test_get_game_bounds()
	test_get_game_1()
	test_get_game_2()
	test_iterate_mainline()
	test_iterate()
	test_notation_data()
	test_image_data()
	test_mainline_forced()
