import pytest
from streamingjson import lexer_helper
from streamingjson import lexer_tokens


class TestMatchStack:

    def test_match_stack_0(self):
        stack = [lexer_tokens.TOKEN_LEFT_BRACE]
        tokens = [lexer_tokens.TOKEN_LEFT_BRACE]
        match_result = lexer_helper.match_stack(stack, tokens)
        assert match_result == True

    def test_match_stack_1(self):
        stack = [
            lexer_tokens.TOKEN_RIGHT_BRACE,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_L,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_L,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_U,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_N,
            lexer_tokens.TOKEN_COLON,
        ]
        tokens = [
            lexer_tokens.TOKEN_RIGHT_BRACE,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_L,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_L,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_U,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_N,
            lexer_tokens.TOKEN_COLON,
        ]
        match_result = lexer_helper.match_stack(stack, tokens)
        assert match_result == True

    def test_match_stack_2(self):
        stack = [
            lexer_tokens.TOKEN_LEFT_BRACE,
            lexer_tokens.TOKEN_QUOTE,
            lexer_tokens.TOKEN_QUOTE,
            lexer_tokens.TOKEN_COLON,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_N,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_U,
        ]
        tokens = [
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_N,
            lexer_tokens.TOKEN_ALPHABET_LOWERCASE_U,
        ]
        match_result = lexer_helper.match_stack(stack, tokens)
        assert match_result == True
