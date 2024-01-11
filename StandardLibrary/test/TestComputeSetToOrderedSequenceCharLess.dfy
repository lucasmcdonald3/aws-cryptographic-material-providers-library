// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/Sets.dfy"
  // Just to make sure we don't conflict with dafny-lang/libraries' Sets.dfy
include "../../libraries/src/Collections/Sets/Sets.dfy"


// This function is commonly used for sorting
// But there are also subtle order effects
// that are important for cryptographic libraries.
// These order functions and externs MUST
// be interoperable across runtimes
// to be used for canonical ordering

module TestComputeSetToOrderedSequenceCharLess {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened SortedSets

  predicate method CharLess(x : char, y : char)
  {
    x < y
  }

  predicate method CharGreater(x : char, y : char) {
    y < x
  }

  method {:test} TestSetToOrderedSequenceEmpty() {
    var output := ComputeSetToOrderedSequence({}, CharLess);
    var output2 := ComputeSetToOrderedSequence2({}, CharLess);
    var expected := [];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceOneItem() {
    var a := {"a"};
    var output := ComputeSetToOrderedSequence(a, CharLess);
    var output2 := ComputeSetToOrderedSequence2(a, CharLess);
    var expected := ["a"];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceSimple() {
    var a := {"ac", "ab"};
    var output := ComputeSetToOrderedSequence(a, CharLess);
    var output2 := ComputeSetToOrderedSequence2(a, CharLess);
    var expected := ["ab", "ac"];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequencePrefix() {
    var a := {"abc", "ab"};
    var output := ComputeSetToOrderedSequence(a, CharLess);
    var output2 := ComputeSetToOrderedSequence2(a, CharLess);
    var expected := ["ab", "abc"];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceComplex() {
    var a := {"abc", "bbc", "ab"};
    var output := ComputeSetToOrderedSequence(a, CharLess);
    var output2 := ComputeSetToOrderedSequence2(a, CharLess);
    var expected := ["ab", "abc", "bbc"];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceComplexReverse() {
    var a := {"abc", "bbc", "ab"};
    var output := ComputeSetToOrderedSequence(a, CharGreater);
    var output2 := ComputeSetToOrderedSequence2(a, CharGreater);
    var expected := ["bbc", "ab", "abc"];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetSequence() {
    var a :=  {"abc", "bbc", "ab"};
    var output := ComputeSetToSequence(a);
    expect multiset(output) == multiset(a);
  }

  method {:test} TestSetToOrderedComplexUnicode() {
    var a := {"𐐷", "&", "Љ", "ᝀ", "🂡", "｡", "𐀂"};
    var output := ComputeSetToOrderedSequence(a, CharLess);
    var output2 := ComputeSetToOrderedSequence2(a, CharLess);
    var expected := ["&", "Љ", "ᝀ", "𐀂", "𐐷", "🂡", "｡"];
    // This is the pure logographic order
    // however this function is used in the DB-ESDK
    // to canonicalized sets and needs to remain the same.
    // This order is kept here so that it is clear that this order is incorrect in this case
    // var expected := ["&", "Љ", "ᝀ", "｡", "𐀂", "𐐷", "🂡"];

    /*

      &	046	38	0x26	&amp;
      Љ	02011	1033	0x409	&#1033;
      ᝀ 013500	5952	0x1740	&#5952;
      ｡	0177541	65377	0xFF61	&#65377;
      𐀂 0200002	65538	0x10002	&#65538;
      🂡 0370241	127137	0x1F0A1	&#127137;

    */
    expect output == expected;
    expect output2 == expected;
  }


}
