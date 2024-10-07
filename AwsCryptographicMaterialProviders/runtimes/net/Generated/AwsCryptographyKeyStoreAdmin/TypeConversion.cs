// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public static class TypeConversion
  {
    private const string ISO8601DateFormat = "yyyy-MM-dd\\THH:mm:ss.fff\\Z";

    private const string ISO8601DateFormatNoMS = "yyyy-MM-dd\\THH:mm:ss\\Z";

    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput)value; AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput(); converted.MutationToken = (AWS.Cryptography.KeyStoreAdmin.MutationToken)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(concrete._MutationToken);
      if (concrete._PageSize.is_Some) converted.PageSize = (int)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(concrete._PageSize);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(concrete._Strategy);
      converted.SystemKey = (AWS.Cryptography.KeyStoreAdmin.SystemKey)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(concrete._SystemKey); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput(AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput value)
    {
      value.Validate();
      int? var_pageSize = value.IsSetPageSize() ? value.PageSize : (int?)null;
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(value.MutationToken), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(var_pageSize), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(var_strategy), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(value.SystemKey));
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput(); converted.MutationResult = (AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(concrete._MutationResult);
      converted.MutatedBranchKeyItems = (System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(concrete._MutatedBranchKeyItems); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput(AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(value.MutationResult), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(value.MutatedBranchKeyItems));
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult(); if (value.is_ContinueMutation)
      {
        converted.ContinueMutation = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(concrete.dtor_ContinueMutation);
        return converted;
      }
      if (value.is_CompleteMutation)
      {
        converted.CompleteMutation = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(concrete.dtor_CompleteMutation);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult value)
    {
      value.Validate(); if (value.IsSetContinueMutation())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult.create_ContinueMutation(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(value.ContinueMutation));
      }
      if (value.IsSetCompleteMutation())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult.create_CompleteMutation(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(value.CompleteMutation));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyInput(); if (concrete._Identifier.is_Some) converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(concrete._Identifier);
      if (concrete._EncryptionContext.is_Some) converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(concrete._EncryptionContext);
      converted.KmsArn = (AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(concrete._KmsArn);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(concrete._Strategy); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(AWS.Cryptography.KeyStoreAdmin.CreateKeyInput value)
    {
      value.Validate();
      string var_identifier = value.IsSetIdentifier() ? value.Identifier : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_encryptionContext = value.IsSetEncryptionContext() ? value.EncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(var_identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(var_encryptionContext), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(var_strategy));
    }
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput)value; AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput(AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput(); if (concrete._Original.is_Some) converted.Original = (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Original(concrete._Original);
      if (concrete._Terminal.is_Some) converted.Terminal = (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Terminal(concrete._Terminal); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput(AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities var_original = value.IsSetOriginal() ? value.Original : (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)null;
      AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities var_terminal = value.IsSetTerminal() ? value.Terminal : (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Original(var_original), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Terminal(var_terminal));
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag(); if (value.is_Created)
      {
        converted.Created = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Created(concrete.dtor_Created);
        return converted;
      }
      if (value.is_Resumed)
      {
        converted.Resumed = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Resumed(concrete.dtor_Resumed);
        return converted;
      }
      if (value.is_ResumedWithoutIndex)
      {
        converted.ResumedWithoutIndex = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M19_ResumedWithoutIndex(concrete.dtor_ResumedWithoutIndex);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value)
    {
      value.Validate(); if (value.IsSetCreated())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_Created(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Created(value.Created));
      }
      if (value.IsSetResumed())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_Resumed(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Resumed(value.Resumed));
      }
      if (value.IsSetResumedWithoutIndex())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_ResumedWithoutIndex(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M19_ResumedWithoutIndex(value.ResumedWithoutIndex));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput)value; AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(concrete._Identifier);
      converted.Mutations = (AWS.Cryptography.KeyStoreAdmin.Mutations)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(concrete._Mutations);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(concrete._Strategy);
      converted.SystemKey = (AWS.Cryptography.KeyStoreAdmin.SystemKey)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(concrete._SystemKey); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput(AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(value.Mutations), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(var_strategy), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(value.SystemKey));
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput(); converted.MutationToken = (AWS.Cryptography.KeyStoreAdmin.MutationToken)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(concrete._MutationToken);
      converted.MutatedBranchKeyItems = (System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(concrete._MutatedBranchKeyItems);
      converted.InitializeMutationFlag = (AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(concrete._InitializeMutationFlag); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput(AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(value.MutationToken), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(value.MutatedBranchKeyItems), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(value.InitializeMutationFlag));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy(); if (value.is_AwsKmsReEncrypt)
      {
        converted.AwsKmsReEncrypt = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(concrete.dtor_AwsKmsReEncrypt);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      value.Validate(); if (value.IsSetAwsKmsReEncrypt())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy.create(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(value.AwsKmsReEncrypt));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig)value; AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig converted = new AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig(); converted.LogicalKeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(concrete._logicalKeyStoreName);
      converted.Storage = (AWS.Cryptography.KeyStore.Storage)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(concrete._storage); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(value.LogicalKeyStoreName), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(value.Storage));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier(); if (value.is_KmsKeyArn)
      {
        converted.KmsKeyArn = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M9_KmsKeyArn(concrete.dtor_KmsKeyArn);
        return converted;
      }
      if (value.is_KmsMRKeyArn)
      {
        converted.KmsMRKeyArn = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M11_KmsMRKeyArn(concrete.dtor_KmsMRKeyArn);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier value)
    {
      value.Validate(); if (value.IsSetKmsKeyArn())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier.create_KmsKeyArn(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M9_KmsKeyArn(value.KmsKeyArn));
      }
      if (value.IsSetKmsMRKeyArn())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier.create_KmsMRKeyArn(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M11_KmsMRKeyArn(value.KmsMRKeyArn));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationConflictException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationConflictException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(AWS.Cryptography.KeyStoreAdmin.MutationConflictException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationFromException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationFromException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(AWS.Cryptography.KeyStoreAdmin.MutationFromException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationInvalidException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationInvalidException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(AWS.Cryptography.KeyStoreAdmin.MutationInvalidException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationLockInvalidException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationLockInvalidException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException(AWS.Cryptography.KeyStoreAdmin.MutationLockInvalidException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationToException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(AWS.Cryptography.KeyStoreAdmin.MutationToException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationVerificationException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationVerificationException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(AWS.Cryptography.KeyStoreAdmin.MutationVerificationException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.SystemKey(); if (value.is_KmsAes)
      {
        converted.KmsAes = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M6_KmsAes(concrete.dtor_KmsAes);
        return converted;
      }
      if (value.is_TrustStorage)
      {
        converted.TrustStorage = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_TrustStorage(concrete.dtor_TrustStorage);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.SystemKey state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      value.Validate(); if (value.IsSetKmsAes())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey.create_KmsAes(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M6_KmsAes(value.KmsAes));
      }
      if (value.IsSetTrustStorage())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey.create_TrustStorage(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_TrustStorage(value.TrustStorage));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.SystemKey state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.VersionKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput)value; AWS.Cryptography.KeyStoreAdmin.VersionKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.VersionKeyInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(concrete._Identifier);
      converted.KmsArn = (AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(concrete._KmsArn);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(concrete._Strategy); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(AWS.Cryptography.KeyStoreAdmin.VersionKeyInput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(var_strategy));
    }
    public static AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_VersionKeyOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput)value; AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput converted = new AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_VersionKeyOutput(AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput();
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N6_smithy__N3_api__S7_Integer(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N6_smithy__N3_api__S7_Integer((int)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationComplete FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(AWS.Cryptography.KeyStoreAdmin.MutationComplete value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Original(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Original(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities((AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Terminal(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M8_Terminal(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities((AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Created(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Created(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Resumed(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M7_Resumed(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M19_ResumedWithoutIndex(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag__M19_ResumedWithoutIndex(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.Mutations FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(AWS.Cryptography.KeyStoreAdmin.Mutations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(software.amazon.cryptography.keystore.internaldafny.types._IStorage value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(AWS.Cryptography.KeyStore.Storage value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M9_KmsKeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M9_KmsKeyArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M11_KmsMRKeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier__M11_KmsMRKeyArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAes FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M6_KmsAes(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAes value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAes ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M6_KmsAes(AWS.Cryptography.KeyStoreAdmin.KmsAes value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.TrustStorage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_TrustStorage(software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_TrustStorage(AWS.Cryptography.KeyStoreAdmin.TrustStorage value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken)value; AWS.Cryptography.KeyStoreAdmin.MutationToken converted = new AWS.Cryptography.KeyStoreAdmin.MutationToken(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(concrete._Identifier);
      if (concrete._UUID.is_Some) converted.UUID = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(concrete._UUID);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(concrete._CreateTime); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      value.Validate();
      string var_uUID = value.IsSetUUID() ? value.UUID : (string)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(var_uUID), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(value.CreateTime));
    }
    public static int FromDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static int ToDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member).ToArray());
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationComplete FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete)value; AWS.Cryptography.KeyStoreAdmin.MutationComplete converted = new AWS.Cryptography.KeyStoreAdmin.MutationComplete(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(AWS.Cryptography.KeyStoreAdmin.MutationComplete value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete();
    }
    public static string FromDafny_N6_smithy__N3_api__S6_String(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N6_smithy__N3_api__S6_String(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return Dafny.Map<Dafny.ISequence<byte>, Dafny.ISequence<byte>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<byte>, Dafny.ISequence<byte>>(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(pair.Value))
     ));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyProperities concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyProperities)value; AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities converted = new AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities(); converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M6_KmsArn(concrete._KmsArn);
      converted.CustomEncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M23_CustomEncryptionContext(concrete._CustomEncryptionContext); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyProperities ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyProperities(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M23_CustomEncryptionContext(value.CustomEncryptionContext));
    }
    public static AWS.Cryptography.KeyStoreAdmin.Mutations FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations)value; AWS.Cryptography.KeyStoreAdmin.Mutations converted = new AWS.Cryptography.KeyStoreAdmin.Mutations(); if (concrete._TerminalKmsArn.is_Some) converted.TerminalKmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(concrete._TerminalKmsArn);
      if (concrete._TerminalEncryptionContext.is_Some) converted.TerminalEncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(concrete._TerminalEncryptionContext); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(AWS.Cryptography.KeyStoreAdmin.Mutations value)
    {
      value.Validate();
      string var_terminalKmsArn = value.IsSetTerminalKmsArn() ? value.TerminalKmsArn : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_terminalEncryptionContext = value.IsSetTerminalEncryptionContext() ? value.TerminalEncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(var_terminalKmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(var_terminalEncryptionContext));
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.AwsKms concrete = (software.amazon.cryptography.keystore.internaldafny.types.AwsKms)value; AWS.Cryptography.KeyStore.AwsKms converted = new AWS.Cryptography.KeyStore.AwsKms(); if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(concrete._grantTokens);
      if (concrete._kmsClient.is_Some) converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(concrete._kmsClient); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(AWS.Cryptography.KeyStore.AwsKms value)
    {
      value.Validate();
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      Amazon.KeyManagementService.IAmazonKeyManagementService var_kmsClient = value.IsSetKmsClient() ? value.KmsClient : (Amazon.KeyManagementService.IAmazonKeyManagementService)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.AwsKms(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(var_grantTokens), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(var_kmsClient));
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(software.amazon.cryptography.keystore.internaldafny.types._IStorage value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.Storage concrete = (software.amazon.cryptography.keystore.internaldafny.types.Storage)value;
      var converted = new AWS.Cryptography.KeyStore.Storage(); if (value.is_ddb)
      {
        converted.Ddb = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(concrete.dtor_ddb);
        return converted;
      }
      if (value.is_custom)
      {
        converted.Custom = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(concrete.dtor_custom);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.Storage state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IStorage ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(AWS.Cryptography.KeyStore.Storage value)
    {
      value.Validate(); if (value.IsSetDdb())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.Storage.create_ddb(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(value.Ddb));
      }
      if (value.IsSetCustom())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.Storage.create_custom(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(value.Custom));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.Storage state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAes FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAes value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAes concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAes)value; AWS.Cryptography.KeyStoreAdmin.KmsAes converted = new AWS.Cryptography.KeyStoreAdmin.KmsAes(); converted.KmsAesIdentifier = (AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M16_KmsAesIdentifier(concrete._KmsAesIdentifier);
      converted.AwsKms = (AWS.Cryptography.KeyStore.AwsKms)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M6_AwsKms(concrete._AwsKms); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAes ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes(AWS.Cryptography.KeyStoreAdmin.KmsAes value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAes(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M16_KmsAesIdentifier(value.KmsAesIdentifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M6_AwsKms(value.AwsKms));
    }
    public static AWS.Cryptography.KeyStoreAdmin.TrustStorage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage)value; AWS.Cryptography.KeyStoreAdmin.TrustStorage converted = new AWS.Cryptography.KeyStoreAdmin.TrustStorage(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(AWS.Cryptography.KeyStoreAdmin.TrustStorage value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage();
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member(AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M6_KmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M6_KmsArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M23_CustomEncryptionContext(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_MutableBranchKeyProperities__M23_CustomEncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> value)
    {
      return value.is_None ? (Amazon.KeyManagementService.IAmazonKeyManagementService)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference((Amazon.KeyManagementService.IAmazonKeyManagementService)value));
    }
    public static AWS.Cryptography.KeyStore.DynamoDBTable FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(AWS.Cryptography.KeyStore.DynamoDBTable value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static AWS.Cryptography.KeyStore.IKeyStorageInterface FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(AWS.Cryptography.KeyStore.IKeyStorageInterface value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M16_KmsAesIdentifier(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsAesIdentifier ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M16_KmsAesIdentifier(AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_KmsAesIdentifier(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M6_AwsKms(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S6_KmsAes__M6_AwsKms(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem)value; AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem converted = new AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem(); converted.ItemType = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(concrete._ItemType);
      converted.Description = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(concrete._Description); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(value.ItemType), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(value.Description));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(Dafny.ISequence<byte> value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return utf8.GetString(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(string value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return Dafny.Sequence<byte>.FromArray(utf8.GetBytes(value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(System.Collections.Generic.Dictionary<string, string> value)
    {
      return Dafny.Map<Dafny.ISequence<char>, Dafny.ISequence<char>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<char>, Dafny.ISequence<char>>(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(pair.Value))
     ));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member).ToArray());
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value);
    }
    public static AWS.Cryptography.KeyStore.DynamoDBTable FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable concrete = (software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable)value; AWS.Cryptography.KeyStore.DynamoDBTable converted = new AWS.Cryptography.KeyStore.DynamoDBTable(); converted.DdbTableName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(concrete._ddbTableName);
      if (concrete._ddbClient.is_Some) converted.DdbClient = (Amazon.DynamoDBv2.IAmazonDynamoDB)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(concrete._ddbClient); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(AWS.Cryptography.KeyStore.DynamoDBTable value)
    {
      value.Validate();
      Amazon.DynamoDBv2.IAmazonDynamoDB var_ddbClient = value.IsSetDdbClient() ? value.DdbClient : (Amazon.DynamoDBv2.IAmazonDynamoDB)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(value.DdbTableName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(var_ddbClient));
    }
    public static AWS.Cryptography.KeyStore.IKeyStorageInterface FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(AWS.Cryptography.KeyStore.IKeyStorageInterface value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(value);
    }
    public static Amazon.DynamoDBv2.IAmazonDynamoDB FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> value)
    {
      return value.is_None ? (Amazon.DynamoDBv2.IAmazonDynamoDB)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference((Amazon.DynamoDBv2.IAmazonDynamoDB)value));
    }
    public static string FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static Amazon.DynamoDBv2.IAmazonDynamoDB FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value);
    }
    public static software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value);
    }
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.keystoreadmin.internaldafny.types._IError value)
    {
      switch (value)
      {
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_AwsCryptographyKeyStore dafnyVal:
          return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyKeyStore
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsDynamodb dafnyVal:
          return Com.Amazonaws.Dynamodb.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsDynamodb
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsKms dafnyVal:
          // MANUAL EDIT KMS -> Kms
          return Com.Amazonaws.Kms.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsKms
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
        default:
          // The switch MUST be complete for _IError, so `value` MUST NOT be an _IError. (How did you get here?)
          return new OpaqueError();
      }
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IError ToDafny_CommonError(System.Exception value)
    {
      switch (value.GetType().Namespace)
      {
        case "AWS.Cryptography.KeyStore":
          return software.amazon.cryptography.keystoreadmin.internaldafny.types.Error.create_AwsCryptographyKeyStore(
            AWS.Cryptography.KeyStore.TypeConversion.ToDafny_CommonError(value)
          );
        case "Com.Amazonaws.Dynamodb":
          return software.amazon.cryptography.keystoreadmin.internaldafny.types.Error.create_ComAmazonawsDynamodb(
            Com.Amazonaws.Dynamodb.TypeConversion.ToDafny_CommonError(value)
          );
      }
      switch (value)
      {
        case AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationConflictException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationFromException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationInvalidException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationLockInvalidException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S28_MutationLockInvalidException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationToException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationVerificationException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(exception);
        case AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(exception);
        case CollectionOfErrors collectionOfErrors:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors(
            Dafny.Sequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IError>
              .FromArray(
                collectionOfErrors.list.Select
                    (x => TypeConversion.ToDafny_CommonError(x))
                  .ToArray()),
            Dafny.Sequence<char>.FromString(collectionOfErrors.Message)
          );
        // OpaqueError is redundant, but listed for completeness.
        case OpaqueError exception:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(exception);
        case System.Exception exception:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(exception);
        default:
          // The switch MUST be complete for System.Exception, so `value` MUST NOT be an System.Exception. (How did you get here?)
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(value);
      }
    }
  }
}
